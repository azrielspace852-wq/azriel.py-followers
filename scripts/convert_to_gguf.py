#!/usr/bin/env python3
"""MiniGPT (custom) -> GGUF via GPT-2 wrapper."""
import json
import os
import subprocess
import sys
from pathlib import Path

import torch
from transformers import GPT2Config, GPT2LMHeadModel

ROOT = Path(__file__).resolve().parent.parent
CKPT = ROOT / "checkpoints" / "model-final.pt"
CONFIG = ROOT / "checkpoints" / "config.json"
TOK_JSON = ROOT / "checkpoints" / "tokenizer.json"
HF_DIR = ROOT / "checkpoints" / "hf_model"
GGUF = ROOT / "checkpoints" / "model-final.gguf"
LLAMA_CPP = ROOT / "llama.cpp"
OUTTYPE = os.environ.get("OUTTYPE", "f16")


def remap_keys(sd):
    """MiniGPT state_dict -> HF GPT-2 state_dict."""
    new = {}
    for k, v in sd.items():
        k = k.replace("module.", "").replace("_orig_mod.", "")
        if k == "token_emb.weight":
            new["transformer.wte.weight"] = v
        elif k == "pos_emb.weight":
            new["transformer.wpe.weight"] = v
        elif k == "ln_f.weight":
            new["transformer.ln_f.weight"] = v
        elif k == "ln_f.bias":
            new["transformer.ln_f.bias"] = v
        elif k == "head.weight":
            new["lm_head.weight"] = v
        elif k.startswith("blocks.layers."):
            parts = k.split(".")
            i = parts[2]
            rest = ".".join(parts[3:])
            base = f"transformer.h.{i}."
            if rest == "self_attn.in_proj_weight":
                # PyTorch (3d, d) -> GPT2 c_attn (d, 3d)
                q, kk, vv = v.chunk(3, dim=0)
                new[base + "attn.c_attn.weight"] = torch.cat([q, kk, vv], dim=1).contiguous()
            elif rest == "self_attn.in_proj_bias":
                q, kk, vv = v.chunk(3, dim=0)
                new[base + "attn.c_attn.bias"] = torch.cat([q, kk, vv]).contiguous()
            elif rest == "self_attn.out_proj.weight":
                new[base + "attn.c_proj.weight"] = v
            elif rest == "self_attn.out_proj.bias":
                new[base + "attn.c_proj.bias"] = v
            elif rest == "linear1.weight":
                new[base + "mlp.c_fc.weight"] = v
            elif rest == "linear1.bias":
                new[base + "mlp.c_fc.bias"] = v
            elif rest == "linear2.weight":
                new[base + "mlp.c_proj.weight"] = v
            elif rest == "linear2.bias":
                new[base + "mlp.c_proj.bias"] = v
            elif rest == "norm1.weight":
                new[base + "ln_1.weight"] = v
            elif rest == "norm1.bias":
                new[base + "ln_1.bias"] = v
            elif rest == "norm2.weight":
                new[base + "ln_2.weight"] = v
            elif rest == "norm2.bias":
                new[base + "ln_2.bias"] = v
            else:
                print(f"[WARN] unmapped: {k}")
        else:
            print(f"[WARN] unmapped: {k}")
    return new


def build_hf_tokenizer_files(hf_dir: Path, tok_json_path: Path):
    """Custom tokenizer.json ({"stoi": {...}}) -> vocab.json + merges.txt (GPT-2 format)."""
    data = json.load(open(tok_json_path, encoding="utf-8"))
    stoi = data["stoi"]

    with open(hf_dir / "vocab.json", "w", encoding="utf-8") as f:
        json.dump({tok: int(i) for tok, i in stoi.items()}, f, ensure_ascii=False)

    # Word-level, tanpa BPE merges. Tetap butuh file ini supaya converter GPT-2 jalan.
    with open(hf_dir / "merges.txt", "w", encoding="utf-8") as f:
        f.write("#version: 0.2\n")

    with open(hf_dir / "tokenizer_config.json", "w", encoding="utf-8") as f:
        json.dump({
            "tokenizer_class": "GPT2Tokenizer",
            "model_max_length": 256,
            "bos_token": "<bos>",
            "eos_token": "<eos>",
            "unk_token": "<unk>",
            "pad_token": "<pad>",
        }, f, indent=2)

    with open(hf_dir / "special_tokens_map.json", "w", encoding="utf-8") as f:
        json.dump({
            "bos_token": "<bos>",
            "eos_token": "<eos>",
            "unk_token": "<unk>",
            "pad_token": "<pad>",
        }, f, indent=2)


def main():
    if not CKPT.exists():
        sys.exit(f"❌ checkpoint tidak ada: {CKPT}")
    if not CONFIG.exists():
        sys.exit(f"❌ config tidak ada: {CONFIG}")

    obj = torch.load(CKPT, map_location="cpu", weights_only=False)
    if isinstance(obj, dict) and "model_state_dict" in obj:
        obj = obj["model_state_dict"]
    elif isinstance(obj, dict) and "state_dict" in obj:
        obj = obj["state_dict"]

    sd = remap_keys(obj)

    cfg = GPT2Config.from_json_file(str(CONFIG))
    model = GPT2LMHeadModel(cfg)
    missing, unexpected = model.load_state_dict(sd, strict=False)
    print(f"[+] missing={len(missing)} unexpected={len(unexpected)}")
    if missing:
        print("    missing   :", missing[:5])
    if unexpected:
        print("    unexpected:", unexpected[:5])

    HF_DIR.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(HF_DIR)
    cfg.save_pretrained(HF_DIR)
    build_hf_tokenizer_files(HF_DIR, TOK_JSON)
    print(f"[+] HF dir ready: {HF_DIR}")

    convert = LLAMA_CPP / "convert_hf_to_gguf.py"
    if not convert.exists():
        sys.exit("❌ llama.cpp/convert_hf_to_gguf.py tidak ada")

    subprocess.run([
        sys.executable, str(convert),
        str(HF_DIR),
        "--outfile", str(GGUF),
        "--outtype", OUTTYPE,
    ], check=True)

    print(f"✅ Done: {GGUF} ({GGUF.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
