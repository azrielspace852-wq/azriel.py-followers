#!/usr/bin/env python3
"""Convert checkpoints/model-final.pt -> checkpoints/model-final.gguf"""
import os
import sys
import subprocess
from pathlib import Path

import torch
from transformers import AutoConfig, AutoModelForCausalLM, PreTrainedTokenizerFast

ROOT = Path(__file__).resolve().parent.parent
CKPT = ROOT / "checkpoints" / "model-final.pt"
TOK_JSON = ROOT / "checkpoints" / "tokenizer.json"
CONFIG_JSON = ROOT / "checkpoints" / "config.json"
HF_DIR = ROOT / "checkpoints" / "hf_model"
GGUF = ROOT / "checkpoints" / "model-final.gguf"
LLAMA_CPP = ROOT / "llama.cpp"

# === SESUAIKAN kalau perlu ===
OUTTYPE = os.environ.get("OUTTYPE", "f16")   # f16, f32, bf16, q8_0
# =============================


def load_state_dict(path: Path):
    print(f"[+] Loading {path}")
    obj = torch.load(path, map_location="cpu", weights_only=False)
    if isinstance(obj, dict):
        for k in ("model", "state_dict", "model_state_dict", "weights"):
            if k in obj and isinstance(obj[k], dict):
                obj = obj[k]
                break
    # hapus prefix "module." / "_orig_mod."
    return {k.replace("module.", "", 1).replace("_orig_mod.", "", 1): v
            for k, v in obj.items()}


def main():
    if not CKPT.exists():
        sys.exit(f"❌ checkpoint tidak ada: {CKPT}")
    if not TOK_JSON.exists():
        sys.exit(f"❌ tokenizer tidak ada: {TOK_JSON}")

    state_dict = load_state_dict(CKPT)

    if not CONFIG_JSON.exists():
        sys.exit("❌ butuh checkpoints/config.json (arsitektur model). "
                 "Kalau arsitektur custom, ganti bagian ini dengan "
                 "definisi model Anda sendiri.")

    config = AutoConfig.from_pretrained(str(CONFIG_JSON))
    print(f"[+] Building model: {config.model_type}")
    model = AutoModelForCausalLM.from_config(config)
    missing, unexpected = model.load_state_dict(state_dict, strict=False)
    print(f"    missing={len(missing)} unexpected={len(unexpected)}")
    if unexpected:
        print("    contoh unexpected:", unexpected[:3])
    if missing:
        print("    contoh missing   :", missing[:3])

    HF_DIR.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(HF_DIR)
    print(f"[+] Saved HF model -> {HF_DIR}")

    tok = PreTrainedTokenizerFast(tokenizer_file=str(TOK_JSON))
    tok.save_pretrained(HF_DIR)
    print(f"[+] Saved tokenizer -> {HF_DIR}")

    convert_script = LLAMA_CPP / "convert_hf_to_gguf.py"
    if not convert_script.exists():
        sys.exit("❌ llama.cpp tidak ada. Clone dulu di step sebelumnya.")

    cmd = [
        sys.executable, str(convert_script),
        str(HF_DIR),
        "--outfile", str(GGUF),
        "--outtype", OUTTYPE,
    ]
    print("[+] Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    size = GGUF.stat().st_size / 1e6
    print(f"✅ Done: {GGUF} ({size:.1f} MB)")


if __name__ == "__main__":
    main()
