"""
Test harness untuk model MiniGPT hasil train.py (PyTorch, CPU).
Mengimpor langsung MiniGPT + WordTokenizer dari train.py agar arsitektur
dan tokenizer PERSIS sama dengan saat training -> tidak ada mismatch.
"""
import json, re, sys, time
from pathlib import Path

import torch

# --- Ambil definisi kelas dari train.py (wajib ada di repo) ---
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
from train import MiniGPT, WordTokenizer          # noqa: E402

# ================= KONFIG =================
CKPT_PATH       = REPO_ROOT / "checkpoints" / "model-final.pt"
TOKENIZER_PATH  = REPO_ROOT / "checkpoints" / "tokenizer.json"
DATASET_PATH    = Path(__file__).parent / "dataset.jsonl"
MAX_LEN         = 256        # samakan dengan --max-len saat train
DEVICE          = torch.device("cpu")
# =========================================


def load_tokenizer() -> WordTokenizer:
    data = json.loads(TOKENIZER_PATH.read_text(encoding="utf-8"))
    tok = WordTokenizer(vocab_size=data["vocab_size"])
    tok.stoi = {w: i for w, i in data["stoi"].items()}
    tok.itos = {i: w for w, i in tok.stoi.items()}
    tok.vocab_size = len(tok.stoi)
    return tok


def load_model(tok: WordTokenizer):
    obj = torch.load(CKPT_PATH, map_location=DEVICE, weights_only=False)
    state = obj["model_state_dict"] if isinstance(obj, dict) and "model_state_dict" in obj else obj

    # Infer config dari bobot checkpoint (robust terhadap perubahan hyperparam)
    d_model = state["token_emb.weight"].shape[1]
    vocab_size = state["token_emb.weight"].shape[0]
    n_layers = max(int(k.split(".")[1]) for k in state if k.startswith("blocks.")) + 1
    n_head = state["self_attn.in_proj_weight"].shape[0] // d_model if False else 4  # lihat catatan*

    model = MiniGPT(
        vocab_size=vocab_size,
        d_model=d_model,
        n_head=n_head,
        n_layers=n_layers,
        max_len=MAX_LEN,
    ).to(DEVICE)
    model.load_state_dict(state)
    model.eval()
    print(f"[INFO] Model dimuat | params={sum(p.numel() for p in model.parameters()):,} "
          f"| d_model={d_model} n_layers={n_layers} vocab={vocab_size}")
    return model

# * Catatan: n_head TIDAK tersimpan dalam state_dict nn.TransformerEncoderLayer.
#   Kalau Anda mengubah --n-head dari default (4), ganti nilai n_head di atas
#   sesuai argumen training Anda. Cara paling aman: simpan config saat train
#   (lihat tips di akhir jawaban).


@torch.no_grad()
def generate(model, tok: WordTokenizer, prompt: str, max_new_tokens: int = 64) -> str:
    """Greedy decoding deterministik (temperature efektif 0)."""
    ids = tok.encode(prompt, max_len=MAX_LEN)[:-1]  # buang EOS bawaan, kita generate sendiri
    generated = list(ids)

    for _ in range(max_new_tokens):
        # Potong ke window MAX_LEN-1 (sesuai kapasitas pos_emb)
        window = generated[-(MAX_LEN - 1):]
        x = torch.tensor([window], dtype=torch.long, device=DEVICE)
        logits = model(x)                          # [1, t, vocab]
        next_id = int(logits[0, -1].argmax())      # greedy
        if next_id == tok.eos_id:                  # stop jika EOS
            break
        generated.append(next_id)

    new_ids = generated[len(ids):]
    words = [tok.itos.get(i, "<unk>") for i in new_ids]
    return " ".join(words).replace(" ", "").strip() or "(kosong)"


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
    if not CKPT_PATH.exists():
        sys.exit(f"[ERROR] Tidak menemukan {CKPT_PATH}. Jalankan train.py dulu.")

    dataset = [json.loads(l) for l in DATASET_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    tok = load_tokenizer()
    model = load_model(tok)

    hasil, detail = {}, []
    for item in dataset:
        prompt = SYSTEM_PROMPT + "Pertanyaan: " + item["pertanyaan"] + "\nJawaban:"
        t0 = time.time()
        out = generate(model, tok, prompt)
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
        "pengetahuan": 0.60,
        "reasoning": 0.50,
        "tidak_dapat_dijawab": 0.70,
        "jebakan": 0.70,
    }
    gagal = [k for k, t in THRESHOLD.items() if skor.get(k, 0) < t]

    Path("test-report.json").write_text(json.dumps(
        {"skor": skor, "threshold": THRESHOLD, "detail": detail},
        ensure_ascii=False, indent=2))

    if gagal:
        print(f"\n❌ TEST GAGAL, di bawah threshold: {gagal}")
        sys.exit(1)
    print("\n✅ SEMUA TEST LULUS.")


if __name__ == "__main__":
    main()
