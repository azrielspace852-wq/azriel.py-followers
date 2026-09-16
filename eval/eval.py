"""
Test harness untuk model MiniGPT hasil train.py (PyTorch, CPU).
Self-contained: mengimpor MiniGPT + WordTokenizer dari eval/model_def.py
agar arsitektur & tokenizer identik dengan saat training, tanpa perlu train.py.
"""
import json
import re
import sys
import time
from pathlib import Path

import torch

# --- Ambil definisi kelas dari model_def.py (satu folder dengan eval.py) ---
sys.path.insert(0, str(Path(__file__).resolve().parent))
from model_def import MiniGPT, WordTokenizer          # noqa: E402

# ================= KONFIG PATH =================
REPO_ROOT      = Path(__file__).resolve().parent.parent
CKPT_PATH      = REPO_ROOT / "checkpoints" / "model-final.pt"
TOKENIZER_PATH = REPO_ROOT / "checkpoints" / "tokenizer.json"
DATASET_PATH   = Path(__file__).resolve().parent / "dataset.jsonl"
DEVICE         = torch.device("cpu")

# Default hyperparameter yang TIDAK tersimpan di state_dict.
# Ubah jika train.py Anda memakai --n-head selain 4.
DEFAULT_N_HEAD = 4
# =================================================


def load_tokenizer() -> WordTokenizer:
    if not TOKENIZER_PATH.exists():
        sys.exit(f"[ERROR] Tidak menemukan {TOKENIZER_PATH}. Pastikan file ini ikut ter-commit.")
    data = json.loads(TOKENIZER_PATH.read_text(encoding="utf-8"))
    tok = WordTokenizer(vocab_size=data.get("vocab_size", len(data["stoi"])))
    tok.stoi = {w: int(i) for w, i in data["stoi"].items()}
    tok.itos = {int(i): w for w, i in tok.stoi.items()}
    tok.vocab_size = len(tok.stoi)
    return tok


def infer_config(state: dict):
    """Infer arsitektur dari key state_dict, format apa pun."""
    d_model    = state["token_emb.weight"].shape[1]
    vocab_size = state["token_emb.weight"].shape[0]
    max_len    = state["pos_emb.weight"].shape[0]

    layer_ids = set()
    for k in state:
        # cocok untuk: blocks.0.*  /  blocks.layers.0.*  /  transformer.layers.0.*
        m = re.match(r"(?:blocks|transformer)(?:\.layers)?\.(\d+)\.", k)
        if m:
            layer_ids.add(int(m.group(1)))
    n_layers = (max(layer_ids) + 1) if layer_ids else 4

    return vocab_size, d_model, n_layers, max_len


def load_model() -> MiniGPT:
    if not CKPT_PATH.exists():
        sys.exit(f"[ERROR] Tidak menemukan {CKPT_PATH}. Jalankan train.py dulu / pastikan ter-commit.")

    obj = torch.load(CKPT_PATH, map_location=DEVICE, weights_only=False)

    cfg   = obj.get("config") if isinstance(obj, dict) else None
    state = obj["model_state_dict"] if isinstance(obj, dict) and "model_state_dict" in obj else obj

    vocab_size, d_model, n_layers, max_len = infer_config(state)
    n_head = int(cfg["n_head"]) if cfg and "n_head" in cfg else DEFAULT_N_HEAD

    model = MiniGPT(
        vocab_size=vocab_size,
        d_model=d_model,
        n_head=n_head,
        n_layers=n_layers,
        max_len=max_len,
    ).to(DEVICE)

    missing, unexpected = model.load_state_dict(state, strict=False)
    if missing or unexpected:
        print(f"[WARN] missing keys   : {missing}")
        print(f"[WARN] unexpected keys: {unexpected}")
        print("[HINT] Pastikan class MiniGPT di eval/model_def.py identik dengan train.py")

    model.eval()
    n_params = sum(p.numel() for p in model.parameters())
    print(f"[INFO] Model dimuat | params={n_params:,} | "
          f"d_model={d_model} n_layers={n_layers} n_head={n_head} vocab={vocab_size} max_len={max_len}")
    return model, max_len


@torch.no_grad()
def generate(model, tok: WordTokenizer, prompt: str, max_len: int, max_new_tokens: int = 64) -> str:
    """Greedy decoding deterministik, berhenti pada EOS."""
    ids = tok.encode(prompt, max_len=max_len)
    # buang trailing EOS/pad bawaan encode, kita generate sendiri
    while ids and ids[-1] in (tok.eos_id, tok.pad_id):
        ids.pop()

    generated = list(ids)
    for _ in range(max_new_tokens):
        window = generated[-(max_len - 1):]           # jaga kapasitas pos_emb
        x = torch.tensor([window], dtype=torch.long, device=DEVICE)
        logits = model(x)                             # [1, t, vocab]
        if isinstance(logits, tuple):
            logits = logits[0]
        next_id = int(logits[0, -1].argmax())         # greedy
        if next_id == tok.eos_id:
            break
        generated.append(next_id)

    new_ids = generated[len(ids):]
    return tok.decode(new_ids).strip() or "(kosong)"


# ---------- Penilaian ----------
SYSTEM_PROMPT = (
    "Anda adalah asisten AI berbahasa Indonesia. Jawablah jujur. "
    "Jika tidak tahu atau informasinya tidak ada, katakan 'saya tidak tahu' "
    "dan jangan mengarang.\n\n"
)


def norm(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def cocok(jawaban: str, kunci_list) -> bool:
    j = norm(jawaban)
    return any(norm(k) in j for k in kunci_list)


def main():
    if not DATASET_PATH.exists():
        sys.exit(f"[ERROR] Tidak menemukan {DATASET_PATH}")

    dataset = [json.loads(l) for l in DATASET_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"[INFO] {len(dataset)} soal test dimuat.")

    tok = load_tokenizer()
    model, max_len = load_model()

    hasil, detail = {}, []
    for item in dataset:
        prompt = SYSTEM_PROMPT + "Pertanyaan: " + item["pertanyaan"] + "\nJawaban:"
        t0 = time.time()
        out = generate(model, tok, prompt, max_len)
        lat = time.time() - t0

        lulus = cocok(out, item["kunci"])
        kat = item["kategori"]
        hasil.setdefault(kat, [0, 0])
        hasil[kat][1] += 1
        hasil[kat][0] += int(lulus)

        print(f"[{'PASS' if lulus else 'FAIL'}] ({kat}) {item['pertanyaan'][:50]}... -> {out[:70]!r} ({lat:.2f}s)")
        detail.append({"id": item.get("id"), "kategori": kat, "lulus": lulus,
                       "latency_s": round(lat, 2), "output": out[:300]})

    print("\n===== RINGKASAN =====")
    skor = {k: round(v[0] / v[1], 3) for k, v in hasil.items()}
    for k, v in hasil.items():
        print(f"{k:22s}: {v[0]}/{v[1]} = {v[0]/v[1]:.1%}")

    THRESHOLD = {
        "pengetahuan":         0.60,
        "reasoning":           0.50,
        "tidak_dapat_dijawab": 0.70,
        "jebakan":             0.70,
    }
    gagal = [k for k, t in THRESHOLD.items() if skor.get(k, 0) < t]

    Path("test-report.json").write_text(json.dumps(
        {"skor": skor, "threshold": THRESHOLD, "detail": detail},
        ensure_ascii=False, indent=2))

    if gagal:
        print(f"\n[FAIL] TEST GAGAL, kategori di bawah threshold: {gagal}")
        sys.exit(1)
    print("\n[PASS] SEMUA TEST LULUS.")


if __name__ == "__main__":
    main()
