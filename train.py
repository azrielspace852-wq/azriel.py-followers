"""
Script Pre-Training Model AI (PyTorch) - dijalankan di GitHub Actions (GitHub-hosted runner, CPU).

Alur:
1. Baca dataset dari file .jsonl (satu JSON object per baris, field "text").
2. Bangun tokenizer sederhana (word-level) dari isi dataset.
3. Bangun model Transformer kecil (decoder-only, gaya GPT mini).
4. Training loop dengan checkpoint per epoch.

Catatan penting:
- Karena GitHub Actions TIDAK punya GPU (kecuali self-hosted runner, yang sengaja
  tidak dipakai di sini), training berjalan di CPU. Jadi ukuran model dan dataset
  harus dijaga kecil/menengah agar selesai dalam batas waktu job (± beberapa jam).
- Jika dataset/model Anda besar, pertimbangkan: mengurangi epoch, mengurangi
  ukuran model, atau melakukan training bertahap (resume dari checkpoint) lewat
  banyak run job (karena GitHub Actions job publik dibatasi ~6 jam per run).
"""

import argparse
import json
import math
import os
import re
import time
from collections import Counter

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


# --------------------------------------------------------------------------
# 1. Load & tokenisasi dataset
# --------------------------------------------------------------------------

def load_jsonl_texts(path):
    """Baca file .jsonl, ambil field teks dari tiap baris."""
    texts = []
    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print(f"[WARN] Baris {line_num} bukan JSON valid, dilewati.")
                continue

            # Coba beberapa nama field yang umum dipakai untuk teks.
            text = None
            for key in ("text", "content", "prompt", "input"):
                if isinstance(obj, dict) and key in obj and isinstance(obj[key], str):
                    text = obj[key]
                    break
                elif isinstance(obj, dict) and key == "prompt" and "completion" in obj:
                    text = str(obj.get("prompt", "")) + " " + str(obj.get("completion", ""))
                    break

            if text is None and isinstance(obj, str):
                text = obj

            if text:
                texts.append(text)

    if not texts:
        raise ValueError(
            "Tidak ada teks yang berhasil diekstrak dari dataset. "
            "Pastikan setiap baris JSON punya field 'text'/'content'/'prompt'."
        )
    return texts


_WORD_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def simple_tokenize(text):
    return _WORD_RE.findall(text.lower())


class WordTokenizer:
    """Tokenizer word-level sederhana, dibangun dari korpus dataset sendiri."""

    def __init__(self, vocab_size=8000):
        self.vocab_size = vocab_size
        self.stoi = {}
        self.itos = {}
        self.pad_id = 0
        self.unk_id = 1
        self.bos_id = 2
        self.eos_id = 3

    def build(self, texts):
        counter = Counter()
        for t in texts:
            counter.update(simple_tokenize(t))

        specials = ["<pad>", "<unk>", "<bos>", "<eos>"]
        most_common = [w for w, _ in counter.most_common(self.vocab_size - len(specials))]
        vocab = specials + most_common

        self.stoi = {w: i for i, w in enumerate(vocab)}
        self.itos = {i: w for w, i in self.stoi.items()}
        self.vocab_size = len(vocab)
        print(f"[INFO] Vocab size aktual: {self.vocab_size}")

    def encode(self, text, max_len=256):
        tokens = simple_tokenize(text)[: max_len - 2]
        ids = [self.bos_id] + [self.stoi.get(tok, self.unk_id) for tok in tokens] + [self.eos_id]
        return ids

    def pad(self, ids, max_len):
        if len(ids) < max_len:
            ids = ids + [self.pad_id] * (max_len - len(ids))
        else:
            ids = ids[:max_len]
        return ids


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_len=256):
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.examples = [tokenizer.pad(tokenizer.encode(t, max_len), max_len) for t in texts]

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        ids = self.examples[idx]
        x = torch.tensor(ids[:-1], dtype=torch.long)
        y = torch.tensor(ids[1:], dtype=torch.long)
        return x, y


# --------------------------------------------------------------------------
# 2. Model: Transformer decoder-only kecil (mini-GPT)
# --------------------------------------------------------------------------

class MiniGPT(nn.Module):
    def __init__(self, vocab_size, d_model=256, n_head=4, n_layers=4, max_len=1024, dropout=0.1):
        super().__init__()
        self.max_len = max_len
        self.token_emb = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.pos_emb = nn.Embedding(max_len, d_model)
        self.drop = nn.Dropout(dropout)

        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_head,
            dim_feedforward=d_model * 4,
            dropout=dropout,
            batch_first=True,
        )
        self.blocks = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, x):
        b, t = x.shape
        pos = torch.arange(t, device=x.device).unsqueeze(0).expand(b, t)
        h = self.drop(self.token_emb(x) + self.pos_emb(pos))

        # Causal mask supaya token hanya bisa "melihat" token sebelumnya.
        mask = nn.Transformer.generate_square_subsequent_mask(t).to(x.device)
        h = self.blocks(h, mask=mask)
        h = self.ln_f(h)
        logits = self.head(h)
        return logits


# --------------------------------------------------------------------------
# 3. Training loop
# --------------------------------------------------------------------------

def train(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Menggunakan device: {device}")

    print(f"[INFO] Membaca dataset dari: {args.dataset}")
    texts = load_jsonl_texts(args.dataset)
    print(f"[INFO] Total contoh teks: {len(texts)}")

    tokenizer = WordTokenizer(vocab_size=args.vocab_size)
    tokenizer.build(texts)

    dataset = TextDataset(texts, tokenizer, max_len=args.max_len)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True, drop_last=True)

    model = MiniGPT(
        vocab_size=tokenizer.vocab_size,
        d_model=args.d_model,
        n_head=args.n_head,
        n_layers=args.n_layers,
        max_len=args.max_len,
    ).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    print(f"[INFO] Jumlah parameter model: {n_params:,}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr)
    criterion = nn.CrossEntropyLoss(ignore_index=tokenizer.pad_id)

    os.makedirs(args.output_dir, exist_ok=True)

    # Simpan tokenizer supaya bisa dipakai lagi saat inference.
    with open(os.path.join(args.output_dir, "tokenizer.json"), "w", encoding="utf-8") as f:
        json.dump({"stoi": tokenizer.stoi, "vocab_size": tokenizer.vocab_size}, f, ensure_ascii=False)

    global_step = 0
    start_time = time.time()

    for epoch in range(1, args.epochs + 1):
        model.train()
        total_loss = 0.0

        for batch_idx, (x, y) in enumerate(loader, 1):
            x, y = x.to(device), y.to(device)

            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits.view(-1, logits.size(-1)), y.view(-1))
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

            total_loss += loss.item()
            global_step += 1

            if batch_idx % args.log_every == 0:
                avg_loss = total_loss / batch_idx
                elapsed = time.time() - start_time
                print(
                    f"[Epoch {epoch}/{args.epochs}] "
                    f"Batch {batch_idx}/{len(loader)} | "
                    f"Loss: {avg_loss:.4f} | "
                    f"PPL: {math.exp(min(avg_loss, 20)):.2f} | "
                    f"Elapsed: {elapsed/60:.1f} menit"
                )

        avg_epoch_loss = total_loss / max(len(loader), 1)
        print(f"[INFO] Epoch {epoch} selesai. Rata-rata loss: {avg_epoch_loss:.4f}")

        ckpt_path = os.path.join(args.output_dir, f"checkpoint-epoch{epoch}.pt")
        torch.save(
            {
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "loss": avg_epoch_loss,
                "config": vars(args),
            },
            ckpt_path,
        )
        print(f"[INFO] Checkpoint disimpan: {ckpt_path}")

    final_path = os.path.join(args.output_dir, "model-final.pt")
    torch.save(model.state_dict(), final_path)
    print(f"[INFO] Model final disimpan: {final_path}")
    print(f"[INFO] Total waktu training: {(time.time() - start_time)/60:.1f} menit")


def parse_args():
    parser = argparse.ArgumentParser(description="Pre-Training Model AI dengan PyTorch")
    parser.add_argument("--dataset", type=str, required=True, help="Path ke file .jsonl")
    parser.add_argument("--output-dir", type=str, default="checkpoints")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=5e-5)
    parser.add_argument("--max-len", type=int, default=256)
    parser.add_argument("--vocab-size", type=int, default=8000)
    parser.add_argument("--d-model", type=int, default=256)
    parser.add_argument("--n-head", type=int, default=4)
    parser.add_argument("--n-layers", type=int, default=4)
    parser.add_argument("--log-every", type=int, default=20)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train(args)
