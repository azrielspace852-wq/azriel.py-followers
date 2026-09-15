# RENCANA ARSITEKTUR AXION NEURALIS — VERSI 5.0

| Field | Nilai |
|---|---|
| ID Dokumen | ARCH-AXN-V5-001 |
| Project | AXION Neuralis |
| Versi | 5.0.0 |
| Status | **APPROVED** — mengikat seluruh tim (§1.2), efektif 2026-09-12 |
| Disetujui oleh | Owner / CEO (AZRIEL) — **OD-2026-003** |
| Turunan dari | Rencana Arsitektur v4.0 (APPROVE) |
| Dasar penyusunan | PROPOSAL-ARCH-UPGRADE-001 (APPROVED) + Gap Assessment Report v4→v5 |
| Menggantikan | 5.0.0-draft.1, 5.0.0-draft.2, 5.0.0-draft.3 — digabung menjadi satu dokumen tunggal ini (rekomendasi reviewer #1, dieksekusi via OD-2026-003) |
| Disusun oleh | AI drafter — bukan decision authority |
| Otoritas approval | Owner / CEO |
| Tanggal terbit final | 2026-09-12 |

**Catatan hierarki:** dokumen ini berstatus APPROVED — mengikat seluruh tim sesuai §1.2. Jika terjadi konflik, hierarki source of truth tetap berlaku:
`EXPLICIT_OWNER_DECISION > dokumen APPROVED (BIBLE/BLUEPRINT/ROADMAP) > draft > proposal AI`.

**Label yang digunakan dalam dokumen ini:**
- `[OWNER-DECIDED]` — sudah diputuskan otoritas sah, mengikat.
- `[APPROVED BASELINE]` — baseline proposal APPROVED (P01/P02/P03/P04/ARS) yang dipertahankan.
- `[PROPOSED DEFAULT]` — usulan default dari drafter, belum diputuskan Owner; dapat berubah.
- `[UNCERTAIN]` — belum dapat diverifikasi, butuh konfirmasi sumber resmi.

### Changelog

| Versi | Tanggal | Perubahan |
|---|---|---|
| 5.0.0 (FINAL) | 2026-09-12 | Status dokumen berubah dari DRAFT menjadi **APPROVED** per **OD-2026-003**. Digabung dari draft.1 (BAB 1–5) + draft.2 (BAB 6–10) + draft.3 (lapisan integrasi keputusan) menjadi satu dokumen tunggal — satu header, satu changelog terpadu (menjalankan rekomendasi reviewer #1). Menerapkan **OD-2026-001** (+ Adendum) dan **OD-2026-002** (+ Adendum) langsung ke badan dokumen: §6.1.2, §6.1.3, §6.4, §7.1, §7.2.4, §7.4, §8.2.1, §8.2.2, §8.3, §9.1.2, §10.4.2. Notasi opsi ([PROPOSED DEFAULT] / [RE-LABELED] / daftar kandidat trigger) pada bagian yang sudah diputuskan dibersihkan dan ditulis sebagai keputusan arsitektur final. Item yang belum diputuskan Owner (rasio recirculation §6.3.1, burn trigger §6.3.2, target user §6.5.1, skema scoring risiko §9.2, SLA eskalasi §7.3.2, mekanisme distribusi carry-over §6.1.2) tetap terbuka sesuai cakupan OD-2026-003 dan mempertahankan label aslinya. |
| 5.0.0-draft.3 | 2026-09-06 | Integrasi awal OD-2026-001 dan OD-2026-002 sebagai lapisan pencatatan terpisah dari badan arsitektur; tiga temuan (F-1, F-2, F-3) dicatat menunggu konfirmasi Owner. |
| 5.0.0-draft.2 | 2026 | Draft BAB 6–10; menutup GAP-06 s.d. GAP-10; traceability + verifikasi EC-01..EC-13. |
| 5.0.0-draft.1 | 2026 | Draft BAB 1–5; menutup GAP-01 s.d. GAP-05. |

---

# BAB 1: META & LIFECYCLE

> **Pemetaan dokumen inti:** BAB 1 → BIBLE (perusahaan & project).
> **Gap yang ditutup:** GAP-04 (Document Lifecycle Policy).

## 1.1 Document Info

Setiap dokumen arsitektur dan dokumen inti wajib memiliki metadata minimal berikut:

| Field | Wajib | Keterangan |
|---|---|---|
| `id` | ✅ | ID unik dokumen (contoh: `ARCH-AXN-V5-001`) |
| `version` | ✅ | Mengikuti skema versioning §1.3 |
| `status` | ✅ | Salah satu dari status lifecycle §1.2 |
| `author` | ✅ | Penyusun (AI drafter wajib disebutkan sebagai drafter, bukan owner keputusan) |
| `approved_by` | ✅ bila status ≥ APPROVED | Otoritas sah yang menyetujui |
| `last_updated` | ✅ | Tanggal perubahan terakhir (ISO 8601, UTC) |
| `changelog` | ✅ | Riwayat perubahan; tidak boleh kosong untuk dokumen ACTIVE |
| `supersedes` | Opsional | Dokumen/klausul versi lama yang digantikan |

## 1.2 Document Lifecycle Policy

### 1.2.1 Status lifecycle

```
DRAFT → PROPOSED → APPROVED → ACTIVE → DEPRECATED → ARCHIVED
```

(v4 mendefinisikan DRAFT, PROPOSED, APPROVED, ACTIVE, SUPERSEDED, ARCHIVED. Mulai v5, status `DEPRECATED` ditambahkan sebagai tahap penonaktifan terkendali sebelum `ARCHIVED`; `SUPERSEDED` diperlakukan sebagai penanda relasi antar-versi, bukan status mandiri.)

### 1.2.2 Daya ikat per status

| Status | Daya ikat | Aturan |
|---|---|---|
| DRAFT | **Tidak mengikat** | Referensi internal hanya untuk diskusi. Klausul: *"Dokumen berstatus DRAFT tidak boleh dirujuk sebagai aturan mengikat."* |
| PROPOSED | **Belum mengikat** | Diajukan ke CEO/Owner untuk review. Tidak boleh diimplementasikan sebagai kebijakan final. |
| APPROVED | **Mengikat seluruh tim** | Berlaku sebagai acuan implementasi. Perubahan hanya via mekanisme §1.3 dan otoritas §1.4. |
| ACTIVE | **Mengikat + berlaku operasional** | APPROVED dan sedang digunakan dalam operasional/implementasi berjalan. |
| DEPRECATED | **Masih mengikat untuk transisi** | Tidak boleh dipakai untuk pekerjaan baru; migrasi ke pengganti wajib dijadwalkan. |
| ARCHIVED | **Tidak mengikat** | Disimpan sebagai riwayat; tidak boleh dirujuk sebagai acuan aktif. |

### 1.2.3 Aturan tambahan

1. Setiap dokumen wajib mencantumkan status pada header dokumen.
2. Perubahan status hanya dilakukan oleh otoritas sesuai §1.4 (AI tidak boleh mengubah status menjadi APPROVED).
3. `APPROVED` berarti spesifikasi ditetapkan sebagai acuan — **bukan** berarti implementasi/verifikasi selesai (konsisten dengan v4 §12: status implementasi BELUM IMPLEMENTASI, verifikasi NOT_RUN).
4. Dokumen DEPRECATED wajib menunjuk dokumen pengganti.

## 1.3 Change Control & Versioning

### 1.3.1 Skema versioning

Format: `MAJOR.MINOR.PATCH` (contoh: `5.0.0`).

| Komponen | Dinaikkan ketika |
|---|---|
| MAJOR | Perubahan prinsip canonical LOCKED, perubahan kontrak yang membatalkan kompatibilitas, atau restrukturisasi arsitektur fundamental |
| MINOR | Penambahan bab/klausul baru yang backward-compatible |
| PATCH | Koreksi editorial, klarifikasi tanpa perubahan makna |

Draft yang belum APPROVED menggunakan sufiks: `x.y.z-draft.N` (contoh: `5.0.0-draft.1`).

### 1.3.2 Aturan perubahan

1. **Changelog wajib** untuk setiap perubahan — tidak ada silent rewrite (baseline P04, v4 §7.3).
2. Setiap entri changelog minimal memuat: versi, tanggal, ringkasan perubahan, dan referensi keputusan (Decision ID bila ada).
3. Klausul yang digantikan wajib ditandai eksplisit `[SUPERSEDED]` beserta penggantinya (preseden: O3-REV-1 menggantikan ketentuan "100 juta coin per 5 tahun" pada v3).
4. Perubahan pada konten berlabel **LOCKED** (BAB 2) hanya dapat dilakukan melalui Owner Decision dengan Decision ID (§7.2, format `OD-YYYY-NNN`).
5. Versi lama yang digantikan diberi status SUPERSEDED/ARCHIVED dan tetap disimpan untuk audit.

## 1.4 Approval Authority (ringkasan)

Matriks lengkap diatur pada BAB 7 (Decision Authority Matrix). Ringkasan untuk dokumen:

| Objek | Drafter | Approver |
|---|---|---|
| Dokumen arsitektur (dokumen ini) | AI / Tech Lead | Owner / CEO |
| BIBLE (perusahaan & project) | AI / tim | CEO |
| BLUEPRINT (perusahaan & project) | AI / Tech Lead | CEO |
| ROADMAP (perusahaan & project) | AI / PM | CEO |
| OWNER-DECISIONS register | — (hanya Owner) | Owner |
| Perubahan prinsip LOCKED | — (proposal saja) | Owner via `OD-YYYY-NNN` |

Aturan: AI hanya drafter/assistant, bukan decision authority. Status APPROVED hanya sah melalui otoritas yang valid (Owner/CEO) — konsisten v4 §7.3.

---

# BAB 2: CANONICAL PRINCIPLES

> **Pemetaan dokumen inti:** BAB 2 → BIBLE (perusahaan & project).
> **Gap yang ditutup:** GAP-01 (Canonical Principles List Tidak Final).

## 2.0 Deklarasi LOCKED

> **Daftar prinsip pada BAB 2 bersifat FINAL dan LOCKED.**
> Daftar ini adalah satu-satunya daftar prinsip definitif (canonical) untuk seluruh dokumen AXION. Prinsip yang tersebar di dokumen lain harus dirujuk ke daftar ini, bukan didefinisikan ulang.
>
> **Mekanisme perubahan:** prinsip LOCKED hanya dapat diubah, ditambah, atau dihapus melalui **Owner Decision** dengan Decision ID berformat `OD-YYYY-NNN` dan dicatat pada register OWNER-DECISIONS (BAB 7). Setiap aturan turunan (kebijakan, spesifikasi, implementasi) tidak boleh bertentangan dengan prinsip LOCKED; jika bertentangan, aturan turunan yang harus diperbaiki.

## 2.1 Prinsip Desain Sistem (LOCKED)

Konsolidasi definitif dari prinsip yang sebelumnya tersebar di v4 (§2, §4.1, §5.4, §7, §12):

| ID | Prinsip | Sumber |
|---|---|---|
| SD-01 | **No master key** — tidak boleh ada satu credential tunggal yang membuka seluruh infrastruktur | v4 §2, ARS-4, aturan non-negotiable |
| SD-02 | **Scoped credential** — credential memiliki scope berdasarkan service/kategori dan hubungan akses yang diperlukan; penamaan menggambarkan hubungan akses | v4 §2, ARS-4 |
| SD-03 | **Secret tidak di repository** — secret production disimpan sebagai secret/environment variable pada konfigurasi deployment Cloudflare, bukan file `.env` di repository | v4 §2, aturan non-negotiable |
| SD-04 | **Authentication ≠ authorization** — credential valid tidak otomatis memberi akses ke seluruh sistem; identitas service dan permission harus dapat dibedakan | v4 §2 |
| SD-05 | **Append-only audit trail** — setiap event penting (finansial, keamanan, perubahan status) dicatat secara append-only; tidak ada UPDATE/DELETE diam-diam pada riwayat; koreksi hanya melalui reversal/compensating entry | **Prinsip ke-6 (baru, digeneralisasi dari v4 §4.1 & §5.5)** |
| SD-06 | **Explicit state machine** — status kritis hanya berubah melalui transisi yang diizinkan; transisi terlarang dicatat sebagai exception, tidak dikoreksi diam-diam | v4 §4.1 |
| SD-07 | **Idempotency operasi kritis** — duplikat request tidak boleh mengubah hasil akhir | v4 §4.1, §5.5 |
| SD-08 | **D1 bukan dependency validasi credential** — validasi credential antar-worker tidak boleh menjadikan D1 sebagai dependency wajib per request | v4 §2 |
| SD-09 | **Pemisahan dokumen perusahaan & project** — tidak boleh mencampur isi dokumen perusahaan dan project dalam satu dokumen | v4 §7, §12, P04 |
| SD-10 | **Approved decision tidak diubah tanpa otoritas** — perubahan keputusan APPROVED hanya melalui otoritas sah dan tercatat | v4 §12 |
| SD-11 | **Tidak ada klaim verified tanpa evidence** — status VERIFIED membutuhkan bukti (test/build/inspeksi); APPROVED ≠ terverifikasi implementasinya | v4 §12 |
| SD-12 | **Tidak mencetak AXION Coin di luar supply cap** — cap 100.000.000 AXC per tahun kalender UTC | `[OWNER-DECIDED: O3-REV-1]`, v4 §5.1 |

## 2.2 Prinsip Pembayaran (6 Prinsip Canonical, LOCKED)

Berlaku untuk seluruh jalur finansial (pembayaran Xendit, ledger AXION Coin, refund, adjustment):

| ID | Prinsip | Definisi operasional |
|---|---|---|
| PP-01 | **Validate before trust** | Webhook/input eksternal tidak dipercaya sebelum signature/validasi lolos |
| PP-02 | **Persist before process** | Event webhook/finansial dicatat terlebih dahulu sebelum diproses |
| PP-03 | **Idempotent processing** | Duplicate webhook/claim tidak mengubah hasil akhir |
| PP-04 | **Explicit state machine** | Status transaksi hanya berubah melalui transisi yang diizinkan (lihat BLUEPRINT: state machine pembayaran) |
| PP-05 | **Append-only audit trail** | Riwayat perubahan status tidak boleh diubah diam-diam; instance finansial dari SD-05 |
| PP-06 | **No silent terminal override** | Status terminal (`SUCCESS`, `FAILED`, `EXPIRED`) tidak ditimpa otomatis; anomali → exception + `NEEDS_REVIEW` |

**Prinsip operasional turunan (bukan canonical, tetap dipertahankan):** *Database as final record + reconciliation fallback* — turunan dari PP-02 dan PP-05; detail mekanisme rekonsiliasi diatur pada BAB 4 dan BLUEPRINT Project.

## 2.3 Prinsip Keamanan (LOCKED)

| ID | Prinsip | Keterangan |
|---|---|---|
| SEC-01 | **Least privilege** | Akses minimum yang diperlukan per service/role; default deny |
| SEC-02 | **Constant-time comparison** | Seluruh pembandingan credential/secret/signature wajib menggunakan constant-time comparison (detail §4.6) |
| SEC-03 | **Replay protection wajib di jalur finansial** | Timestamp + nonce + window validity + HMAC signature (detail §3.5) |
| SEC-04 | **Redaction** | Authorization header, secret, API key, webhook secret, password, token, OTP, data kartu, dan PII tidak boleh masuk log `[APPROVED BASELINE v4 §3.5]` |
| SEC-05 | **Validasi semua input dari batas eksternal** | Webhook, input user, dan respons API pihak ketiga diperlakukan untrusted |
| SEC-06 | **Defense in depth jalur finansial** | Rate limit + risk engine + idempotency + ledger reconciliation bekerja berlapis, bukan satu kontrol tunggal |

## 2.4 Prinsip Data & Privasi (LOCKED)

| ID | Prinsip | Keterangan |
|---|---|---|
| DP-01 | **Baseline regulasi UU PDP No. 27/2022** | Kepatuhan PDP menjadi baseline desain, bukan afterthought (detail BAB 5) |
| DP-02 | **Data minimization** | Hanya data yang diperlukan yang dikumpulkan, diproses, dan disimpan |
| DP-03 | **Hak subjek data dipenuhi** | Akses, koreksi, hapus, dan portabilitas data disediakan dengan mekanisme yang terdefinisi |
| DP-04 | **Klasifikasi data wajib** | Setiap data diklasifikasikan ke 4 tier (PUBLIC/INTERNAL/CONFIDENTIAL/RESTRICTED) sebelum disimpan/diproses |
| DP-05 | **Data sharing hanya dengan dasar sah** | Berbagi data ke pihak ketiga wajib dasar hukum + DPA |
| DP-06 | **Retention & deletion terdefinisi** | Setiap kategori data memiliki periode retensi dan mekanisme penghapusan/anonimisasi |

---

# BAB 3: THREAT MODEL & SECURITY

> **Pemetaan dokumen inti:** BAB 3 → BLUEPRINT (perusahaan & project).
> **Gap yang ditutup:** GAP-03 (Threat Model Tidak Ada).

## 3.1 Threat Assessment

Minimal 5 kategori ancaman wajib dipertimbangkan dalam setiap desain. Tabel awal (register ancaman):

| ID | Kategori Ancaman | Vektor Serangan (contoh) | Dampak Utama | Mitigasi Utama | Referensi |
|---|---|---|---|---|---|
| T-01 | **Replay attack** | Mengulang/memutar ulang request internal atau finansial yang pernah valid | Duplikasi transaksi, double claim, double spend | Timestamp window ≤ 5 menit + nonce + HMAC signature | §3.5, §4.1, §4.2 |
| T-02 | **Credential theft / interception** | Pencurian secret dari log, repository, environment yang salah konfigurasi, atau intersepsi | Akses tidak sah ke layer internal/finansial | Scoped credential, secret hanya di deployment config, redaction log, TLS, constant-time comparison, rotasi | SD-01..SD-03, SEC-02, SEC-04 |
| T-03 | **Data leakage via AI tools eksternal** | Prompt/konteks yang dikirim ke AI pihak ketiga mengandung secret, PII, atau payload finansial | Kebocoran secret & PII ke pihak ketiga | AI External Usage Policy (§3.2) | §3.2 |
| T-04 | **Unauthorized access (insider)** | Penyalahgunaan akses internal di luar kebutuhan tugas | Perubahan data finansial, kebocoran data | Least privilege, scoped permission, audit trail, monitoring & eskalasi | SEC-01, SD-05, §3.4 |
| T-05 | **Supply chain compromise** | Dependency/library/tool build (termasuk jalur build mobile) yang disusupi | Eksekusi kode berbahaya, kebocoran secret | Review dependency, pin versi, isolasi secret dari environment build, verifikasi tool | §3.2 (approval tool), BAB 9 |
| T-06 | **Webhook forgery / injection** | Webhook palsu yang mengklaim berasal dari payment gateway | Status transaksi palsu, uang tercatat tanpa settlement | Signature validation (PP-01), persist before process, rekonsiliasi | PP-01..PP-03, §4.4 |
| T-07 | **Fraud & sybil AXION Coin** | Multi-akun per device, farming reward, velocity abuse | Inflasi reward di luar budget, drain pool | Risk engine 0–100, device-account binding, velocity limit, rekonsiliasi harian | `[APPROVED BASELINE v4 §5.5, Proposal 03]` |

Setiap perubahan desain yang menyentuh jalur finansial atau data CONFIDENTIAL/RESTRICTED wajib meninjau ulang tabel ini.

## 3.2 AI External Usage Policy

Kebijakan penggunaan AI pihak ketiga (termasuk tool yang direncanakan tim: Qwen Studio, ChatGPT, Claude, Groq, Gemini):

### 3.2.1 Data yang DILARANG dikirim ke AI pihak ketiga

1. **Secret & credential** — production secret, service secret, API key (termasuk `XENDIT_API_KEY`, `XENDIT_WEBHOOK_SECRET`), private key, token, OTP.
2. **PII pengguna** — nama, nomor telepon, email, alamat, dan data identifikasi pribadi lain, baik mentah maupun gabungan yang dapat mengidentifikasi.
3. **Payload finansial** — raw webhook payload, data transaksi, isi ledger, saldo akun, credential scope finansial.
4. **Kode produksi** — source code produksi, terutama yang mengandung atau berdekatan dengan penanganan secret/finansial.

### 3.2.2 Data yang BOLEH dikirim (dengan syarat)

- Deskripsi arsitektur/kebijakan tingkat konsep (seperti dokumen ini).
- Potongan kode sintetis atau contoh yang sudah di-redact (tanpa secret, tanpa data riil).
- Pesan error/log yang sudah dianonimisasi dan di-redact sesuai SEC-04.
- Data sintetis untuk keperluan debugging desain.

Syarat: anonymisasi/redaction dilakukan **sebelum** data meninggalkan lingkungan internal.

### 3.2.3 Approval flow untuk tool AI baru

```
Usulan tool AI baru
  → Evaluasi risiko oleh Security Lead (data apa yang diproses tool, ke mana data dikirim)
  → Keputusan: disetujui / ditolak / disetujui dengan batasan
  → Jika disetujui: dicatat di OWNER-DECISIONS (Decision ID OD-YYYY-NNN)
  → Batasan penggunaan dicantumkan pada dokumen ini
```

Tanpa approval, tool AI baru tidak boleh digunakan pada alur kerja yang menyentuh data INTERNAL ke atas.

## 3.3 Data Classification (4 Tier)

| Tier | Definisi | Contoh | Aturan Handling |
|---|---|---|---|
| **PUBLIC** | Boleh dipublikasikan tanpa dampak | Dokumentasi publik, pengumuman resmi | Tidak memerlukan proteksi khusus; akurasi tetap dijaga |
| **INTERNAL** | Terbatas untuk konsumsi internal; kebocoran menyebabkan gangguan operasional | Kode internal, spesifikasi API, draft arsitektur, notulen internal | Akses terbatas tim; tidak boleh dipublikasikan; tidak dikirim ke AI eksternal tanpa redaction bila memuat desain sensitif |
| **CONFIDENTIAL** | Kebocoran merugikan pengguna dan/atau bisnis | PII pengguna, data transaksi, credential non-produksi, laporan keuangan internal | Enkripsi in-transit; redaction wajib di log (SEC-04); akses need-to-know; dilarang dikirim ke AI eksternal |
| **RESTRICTED** | Proteksi maksimum; kebocoran mengancam keamanan sistem/finansial | Secret produksi, webhook secret, API key payment gateway, private key | Hanya pada environment secret deployment Cloudflare; tidak pernah masuk repository, log, dokumentasi, atau AI tool; akses terbatas + persetujuan Owner |

Kewajiban: setiap penyimpanan data baru (tabel D1, bucket R2, namespace KV) wajib mendeklarasikan tier maksimum data yang ditampung.

## 3.4 Authentication & Authorization Spec

`[APPROVED BASELINE — dipertahankan dari v4 §2, ARS-4]`

1. **Model:** Environment Secret → HTTP Credential → Environment Secret Validation.
   - Pemanggil (contoh: Lapis 2) mengambil credential dari environment variable miliknya.
   - Credential dikirim melalui HTTP request (header `Authorization: Bearer <SERVICE_SECRET>`).
   - Penerima (contoh: Lapis 1) membandingkan credential terhadap environment secret miliknya sendiri — **bukan** ke D1 (SD-08).
   - Sesuai → ACCEPT; tidak sesuai → REJECT.
2. **Development vs production:**
   - Development: secret dapat didefinisikan melalui `.env` lokal (tidak di-commit).
   - Production: secret disimpan sebagai secret/environment variable pada konfigurasi deployment Cloudflare (SD-03).
3. **Identitas service & permission:**
   - Credential yang valid tidak otomatis berarti service memiliki akses ke seluruh sistem (SD-04).
   - Credential memiliki scope per service/kategori dan hubungan akses; penamaan menggambarkan hubungan akses.
   - Contoh penamaan scoped credential: `L2_ACCOUNT_TO_DB_COIN_LEDGER_WRITE`, `L2_ACCOUNT_TO_DB_COIN_READ`.
4. **Authentication vs authorization diperlakukan sebagai dua konsep berbeda:** authentication membuktikan identitas service; authorization memeriksa scope/permission terhadap resource spesifik.
5. **Constant-time comparison wajib** untuk langkah pembandingan credential — detail §4.6 (SEC-02).
6. **Batasan tanggung jawab finansial** `[APPROVED BASELINE v4 §1]`: GateWay adalah satu-satunya layer yang berbicara langsung ke API eksternal; client/Layer 3 tidak boleh menulis ledger coin secara langsung; hanya service dengan credential scoped yang boleh menulis ledger/finansial.

## 3.5 Replay Protection & HMAC Spec

Menutup celah T-01 dan T-06 pada jalur internal dan finansial.

### 3.5.1 Replay protection (wajib untuk seluruh request lintas-layer; nonce wajib untuk jalur finansial)

| Parameter | Spesifikasi | Status |
|---|---|---|
| `X-AXION-Timestamp` | Wajib pada semua request lintas-layer; format UNIX milliseconds | Upgrade v5 (di v4 opsional) |
| Window validity | Maksimum **5 menit (±300 detik)** antara timestamp dan waktu server; di luar window → REJECT | `[APPROVED — PROPOSAL-ARCH-UPGRADE-001, exit criteria EC-03]` |
| `X-AXION-Nonce` | Wajib pada endpoint finansial; string acak unik 16–32 karakter; opsional untuk endpoint non-finansial | Upgrade v5 |
| Nonce uniqueness | Nonce harus unik per kombinasi `(service_id, nonce)` dalam window | Upgrade v5 |
| Nonce storage | KV dengan TTL ≥ window validity + margin `[PROPOSED DEFAULT]` — mekanisme storage final ditetapkan saat implementasi | `[PROPOSED DEFAULT]` |
| Pelanggaran | Timestamp di luar window atau nonce duplikat → `401 REPLAY_DETECTED` + audit log 100% | Upgrade v5 |

### 3.5.2 HMAC signature (wajib untuk endpoint finansial)

`[Persyaratan wajib: APPROVED — PROPOSAL-ARCH-UPGRADE-001, EC-04. Detail konstruksi berikut adalah PROPOSED DEFAULT.]`

| Parameter | Spesifikasi | Status |
|---|---|---|
| Cakupan | Endpoint finansial: pembuatan/status pembayaran, claim/spend/refund/adjustment AXION Coin, penulisan ledger | `[APPROVED]` |
| Header | `X-AXION-Signature` | Upgrade v5 |
| Algoritma | `HMAC-SHA256` | `[PROPOSED DEFAULT]` |
| Kunci | Scoped secret milik pasangan caller–provider yang relevan (bukan master key, SD-01) | `[PROPOSED DEFAULT]` |
| Signing input | `METHOD + "\n" + PATH + "\n" + X-AXION-Timestamp + "\n" + X-AXION-Nonce + "\n" + hex(SHA-256(raw_body))` | `[PROPOSED DEFAULT]` |
| Format signature | `hex(HMAC-SHA256(secret, signing_input))` | `[PROPOSED DEFAULT]` |
| Verifikasi | Wajib menggunakan constant-time comparison (§4.6); gagal → `401 SIGNATURE_INVALID` + audit log | Upgrade v5 |

### 3.5.3 Webhook Xendit

Validasi signature webhook Xendit dilakukan via adapter di Workers GateWay (PP-01). Format header/algoritma spesifik Xendit harus dikonfirmasi dari dokumentasi resmi Xendit — status `[UNCERTAIN]`, verification gate sebelum implementasi (dipertahankan dari v4 §4.3).

### 3.5.4 Insider threat policy

1. Akses produksi mengikuti least privilege (SEC-01) dengan scope per peran.
2. Setiap akses dan operasi pada data CONFIDENTIAL/RESTRICTED tercatat pada audit trail append-only (SD-05).
3. Pemisahan tugas: penulisan finansial hanya oleh service dengan credential scoped finansial; adjustment manual coin membutuhkan reason code + approval reference (bukan self-service) `[APPROVED BASELINE v4 §5.5]`.
4. Anomali akses (mis. credential digunakan di luar pola scope) → deteksi → eskalasi ke Security Lead → Owner bila berdampak finansial/RESTRICTED.
5. Device-account binding anti-fraud dipertahankan: max 2 akun aktif per device, cooldown reward akun baru 3 hari, device high-risk delay 24 jam; device fingerprint pada web wrapper bersifat probabilistik `[UNCERTAIN]` `[APPROVED BASELINE v4 §5.5]`.

---

# BAB 4: TECHNICAL CONTRACTS

> **Pemetaan dokumen inti:** BAB 4 → BLUEPRINT (perusahaan & project).
> **Gap yang ditutup:** GAP-02 (Kontrak Teknis Tidak Utuh), GAP-10 (Integration Contract & SLA).

## 4.1 Header Specification (tabel lengkap)

| # | Header | Tipe | Wajib / Opsional | Format | Contoh |
|---|---|---|---|---|---|
| 1 | `Authorization` | string | **Wajib** — semua request lintas-layer internal | `Bearer <SERVICE_SECRET>` | `Authorization: Bearer <SERVICE_SECRET>` |
| 2 | `X-AXION-Service` | string | **Wajib** — semua request lintas-layer | Identifier service, token kapital/angka | `X-AXION-Service: L2-ACCOUNT` |
| 3 | `X-AXION-Request-ID` | string (UUID v4) | **Wajib** — semua request lintas-layer (baseline v4) | RFC 4122 UUID | `X-AXION-Request-ID: 9f1c2e64-7a2b-4c3d-8e5f-0a1b2c3d4e5f` |
| 4 | `X-AXION-Version` | string | **Wajib** — semua request lintas-layer | `v<MAJOR>` | `X-AXION-Version: v1` |
| 5 | `X-AXION-Timestamp` | integer | **Wajib** (upgrade v5; replay protection §3.5) | UNIX milliseconds | `X-AXION-Timestamp: 1767225600000` |
| 6 | `X-AXION-Nonce` | string | **Wajib** untuk endpoint finansial; opsional lainnya | 16–32 karakter acak unik | `X-AXION-Nonce: f7a9c3e1b2d4068573` |
| 7 | `X-AXION-Signature` | string (hex) | **Wajib** untuk endpoint finansial | `hex(HMAC-SHA256(...))` sesuai §3.5.2 | `X-AXION-Signature: 3f2a9c…e1` |
| 8 | `X-AXION-Idempotency-Key` | string (UUID v4) | **Wajib** untuk POST/PUT finansial; opsional lainnya | RFC 4122 UUID | `X-AXION-Idempotency-Key: 1b4e28ba-…` |
| 9 | `X-AXION-Span-ID` | string | Opsional (tracing) | 16 karakter hex | `X-AXION-Span-ID: 4bf92f3577b34da6` |
| 10 | `X-AXION-Parent-Span-ID` | string | Opsional (tracing) | 16 karakter hex | `X-AXION-Parent-Span-ID: 0af7651916cd43dd` |

Catatan: header 9–10 tetap opsional/minimal sesuai baseline v4; header 1–5 menjadi set minimum wajib v5 untuk seluruh komunikasi lintas-layer.

## 4.2 Authentication Flow (sequence tekstual)

```
LAPIS 2 (pemanggil)                                  LAPIS 1 (penerima)
─────────────────────                                ─────────────────────
1. Ambil scoped secret dari environment
   variable sendiri
   (mis. L2_ACCOUNT_TO_DB_COIN_LEDGER_WRITE)

2. Susun header wajib:
   Authorization, X-AXION-Service,
   X-AXION-Request-ID, X-AXION-Version,
   X-AXION-Timestamp
   (+ X-AXION-Nonce & X-AXION-Signature
    jika jalur finansial, §3.5)

3. Kirim HTTP request ────────────────────────────▶ 4. Terima request

                                                   5. Validasi keberadaan & format
                                                      header wajib (tabel §4.1)
                                                      └─ gagal → 400 VALIDATION_ERROR

                                                   6. Validasi X-AXION-Timestamp
                                                      (window ±300 detik, §3.5.1)
                                                      └─ gagal → 401 REPLAY_DETECTED
                                                                 + audit log

                                                   7. Cek keunikan nonce
                                                      (jalur finansial)
                                                      └─ duplikat → 401 REPLAY_DETECTED
                                                                    + audit log

                                                   8. Bandingkan credential dengan
                                                      CONSTANT-TIME comparison (§4.6)
                                                      └─ tidak sesuai → 401 UNAUTHORIZED
                                                                        + audit log

                                                   9. Cek scope/permission credential
                                                      terhadap resource yang dipanggil
                                                      └─ tidak sesuai → 403 FORBIDDEN
                                                                        + audit log

                                                  10. (Jalur finansial) Verifikasi
                                                      X-AXION-Signature (HMAC, §3.5.2)
                                                      dengan constant-time comparison
                                                      └─ tidak valid → 401 SIGNATURE_INVALID
                                                                       + audit log

                                                  11. ACCEPT → proses request;
                                                      hasil & event penting dicatat
                                                      ke audit trail (SD-05)
```

Kegagalan pada langkah 5–10 tidak boleh membedakan respons berdasarkan alasan secara detail (hindari information leakage) — detail alasan hanya masuk audit log internal.

## 4.3 Error Response Standard

Seluruh error response API internal dan eksternal mengikuti format tunggal:

```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests",
    "detail": { "retry_after_seconds": 30 },
    "timestamp": "2026-01-15T08:30:00Z",
    "request_id": "9f1c2e64-7a2b-4c3d-8e5f-0a1b2c3d4e5f"
  }
}
```

| Field | Wajib | Aturan |
|---|---|---|
| `code` | ✅ | Machine-readable, `UPPER_SNAKE_CASE`, stabil antar versi |
| `message` | ✅ | Human-readable singkat; **dilarang** memuat secret, stack trace internal, atau PII |
| `detail` | Opsional | Objek terstruktur untuk konteks tambahan (mis. `retry_after_seconds`) |
| `timestamp` | ✅ | ISO 8601 UTC |
| `request_id` | ✅ | Gema (echo) dari `X-AXION-Request-ID` request terkait |

### Katalog error code standar

| HTTP | `code` | Kondisi |
|---|---|---|
| 400 | `VALIDATION_ERROR` | Header/format/body tidak valid |
| 401 | `UNAUTHORIZED` | Credential tidak sesuai |
| 401 | `REPLAY_DETECTED` | Timestamp di luar window / nonce duplikat |
| 401 | `SIGNATURE_INVALID` | HMAC signature tidak valid |
| 403 | `FORBIDDEN` | Credential valid tetapi scope/permission tidak mencakup resource |
| 404 | `NOT_FOUND` | Resource tidak ditemukan |
| 409 | `CONFLICT` | Konflik state (termasuk transisi terlarang state machine pembayaran) |
| 409 | `IDEMPOTENCY_CONFLICT` | Idempotency key sama dengan body berbeda |
| 429 | `RATE_LIMITED` | Rate limit terlampaui |
| 500 | `INTERNAL_ERROR` | Kesalahan internal tak terduga |
| 502/504 | `UPSTREAM_ERROR` | Kegagalan/timeout API eksternal |
| 503 | `CIRCUIT_OPEN` | Circuit breaker sedang open untuk target service |

Respons 429 wajib menyertakan header: `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` `[APPROVED BASELINE v4 §3.4]`.

## 4.4 Webhook & Integration SLA

### 4.4.1 SLA webhook masuk (payment gateway → GateWay)

| Parameter | Spesifikasi | Status |
|---|---|---|
| Ack time | GateWay wajib mengirim respons ack **≤ 5 detik** | `[APPROVED — PROPOSAL-ARCH-UPGRADE-001, GAP-10]` |
| Pola pemrosesan | Ack segera; proses berat async melalui `ctx.waitUntil()` + D1 event table + cron fallback | `[APPROVED BASELINE v4 §4.3]` |
| Signature validation | Wajib sebelum event dianggap sah (PP-01); format Xendit `[UNCERTAIN]` — konfirmasi dokumentasi resmi | `[APPROVED BASELINE v4 §4.3]` |
| Persistensi | Raw payload penuh ke R2; metadata + hash ke D1 (PP-02) | `[APPROVED BASELINE v4 §4.3]` |

### 4.4.2 Retry & rekonsiliasi

| Mekanisme | Spesifikasi | Status |
|---|---|---|
| Retry sinkron pemrosesan event | Maks 3× dengan exponential backoff: base delay 250 ms × 2^(attempt-1) + jitter 0–100 ms (formula baseline v4 §3.2) | Upgrade v5 `[PROPOSED DEFAULT untuk jumlah attempt]` |
| Cron `UNPROCESSED_WEBHOOK_RETRY` | Setiap 1–5 menit, max retry 5, backoff | `[APPROVED BASELINE v4 §4.3]` |
| Cron `STALE_PENDING_CHECK` | Setiap 5 menit | `[APPROVED BASELINE v4 §4.3]` |
| Cron `DAILY_MISMATCH_AUDIT` | 1× per hari | `[APPROVED BASELINE v4 §4.3]` |

Timeout baseline tetap berlaku `[APPROVED BASELINE v4 §3.1]`: Layer 3→2 connect 2.000 ms / total 10.000 ms; Layer 2→1 connect 1.500 ms / total 5.000 ms; GateWay→API eksternal non-payment 3.000/10.000 ms; GateWay→Xendit 5.000/15.000 ms; webhook Xendit ack segera dengan proses berat async.

### 4.4.3 Circuit breaker untuk external & internal calls

`[APPROVED BASELINE v4 §3.3]`

| Parameter | Nilai |
|---|---|
| Failure threshold | 5 error berturut-turut dari target service yang sama |
| Error rate threshold | >30% error dalam 30 detik |
| Open state duration | 30 detik |
| Half-open probe | 1 request percobaan |
| Recovery | Circuit ditutup jika probe sukses |
| Respons saat open | `503 CIRCUIT_OPEN` (katalog §4.3) |

Implementasi dapat dimulai per-worker/in-memory. Circuit breaker wajib diterapkan pada panggilan GateWay ke API eksternal (termasuk Xendit).

### 4.4.4 Error handling integrasi

- Semua kegagalan API eksternal dipetakan ke `UPSTREAM_ERROR` / `CIRCUIT_OPEN` dengan format §4.3.
- Retry hanya mengikuti kebijakan v4 §3.2: GET idempotent; POST/PUT/PATCH hanya dengan `Idempotency-Key`; 5xx internal; 429 dengan backoff (hormati `Retry-After`). Tidak ada retry untuk 400/401/403/404/409 dan operasi finansial tanpa `Idempotency-Key`.

## 4.5 Idempotency & Rate Limiting

### 4.5.1 Idempotency

| Aturan | Spesifikasi | Status |
|---|---|---|
| Cakupan wajib | Seluruh operasi finansial: POST/PUT pembayaran, claim/spend/refund/adjustment coin | `[APPROVED — PROPOSAL-ARCH-UPGRADE-001, GAP-10]` |
| Sumber key | Header `X-AXION-Idempotency-Key` (UUID v4) | Upgrade v5 |
| Perilaku duplikat | Key sama + request setara → hasil yang sama dikembalikan ulang; tidak ada pemrosesan ulang | PP-03, SD-07 |
| Key sama, body berbeda | → `409 IDEMPOTENCY_CONFLICT` | Upgrade v5 |
| Natural idempotency coin | Daily claim menggunakan `claim_date` UTC dengan `PRIMARY KEY (account_id, claim_date)` | `[APPROVED BASELINE v4 §5.5]` |
| Retensi record idempotency | Minimal selama window retry + rekonsiliasi aktif; nilai pasti ditetapkan saat implementasi | `[PROPOSED DEFAULT]` |

### 4.5.2 Rate limiting

Mekanisme counter: hot path in-memory di worker (approximate); D1 tidak dibaca/ditulis untuk setiap pengecekan rate limit; kejadian rate-limited ditulis ke log (opsional batch ke KV/R2) `[APPROVED BASELINE v4 §3.4]`.

**Rate limit eksternal** `[APPROVED BASELINE v4 §3.4]`:

| Endpoint / kategori | Limit | Burst | Scope |
|---|---|---|---|
| Public API umum | 120 req/menit | 30 | per IP |
| Login | 5 req/menit | 2 | per IP + account identifier |
| Register | 3 req/jam | 1 | per IP |
| OTP / verification | 3 req/10 menit | 1 | per phone/email/account |
| Token refresh | 30 req/menit | 10 | per account |
| Payment create | 10 req/menit | 3 | per account |
| Webhook Xendit | 300 req/menit | 100 | per source IP Xendit/signature path |

**Rate limit internal** `[APPROVED BASELINE v4 §3.4]`:

| Jalur | Limit | Burst | Scope |
|---|---|---|---|
| Layer 2 → Layer 1 Auth | 2.000 req/menit | 300 | per SERVICE_ID |
| Layer 2 → Layer 1 Database | 3.000 req/menit | 500 | per SERVICE_ID |
| Layer 2 → Layer 1 GateWay | 1.000 req/menit | 200 | per SERVICE_ID |
| Service → service lain | 1.000 req/menit | 200 | per credential scope |

Setiap pelampauan → respons `429 RATE_LIMITED` sesuai §4.3 dengan header `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.

## 4.6 Constant-time Comparison Requirement

| Aspek | Ketentuan |
|---|---|
| Kewajiban | **Wajib** untuk seluruh pembandingan nilai rahasia: bearer service secret, verifikasi HMAC signature, dan pembandingan credential lain (SEC-02) |
| Metode | Fungsi perbandingan constant-time pada runtime yang digunakan. Contoh pada Cloudflare Workers: `crypto.subtle.timingSafeEqual` (atau ekuivalen yang tersedia di runtime) |
| Pola terlarang | Perbandingan string langsung (mis. operator `===`) terhadap secret/signature; perbandingan byte-by-byte yang berhenti lebih awal saat menemukan perbedaan |
| Cakupan tambahan | OTP/token sekali pakai bila dibandingkan di server juga wajib constant-time |
| Verifikasi kepatuhan | Menjadi item checklist code review dan security review sebelum fase implementasi |

---

# BAB 5: DATA GOVERNANCE & PRIVACY

> **Pemetaan dokumen inti:** BAB 5 → BIBLE (kebijakan) + BLUEPRINT (mekanisme teknis).
> **Gap yang ditutup:** GAP-05 (Data Governance & Privacy Framework Tipis).

## 5.1 Regulatory Baseline (UU PDP No. 27/2022)

1. **Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** menjadi baseline kepatuhan desain untuk seluruh pemrosesan data pribadi di ekosistem AXION.
2. Setiap fitur baru yang memproses PII wajib meninjau bab ini sebelum implementasi (gerbang desain).
3. Detail legal drafting dan penunjukan pejabat/fungsi pelindungan data berada di luar scope arsitektur ini (mengacu pada Out of Scope PROPOSAL-ARCH-UPGRADE-001) dan memerlukan review legal terpisah — status `[PROPOSED DEFAULT: jadwalkan review legal sebelum fase implementasi]`.
4. Definisi operasional: *data pribadi* = setiap data tentang orang perseorangan yang teridentifikasi atau dapat diidentifikasi (selaras dengan UU PDP).

## 5.2 Data Subject Rights (Hak Subjek Data)

Hak subjek data yang wajib didukung sistem, beserta mekanisme desainnya:

| Hak | Mekanisme Desain | Status |
|---|---|---|
| **Akses** | Endpoint/layanan pada Workers Account untuk menampilkan data profil & aktivitas yang tersimpan, setelah verifikasi identitas | Upgrade v5 `[PROPOSED DEFAULT: SLA respons ditetapkan pada BLUEPRINT]` |
| **Koreksi** | Mekanisme pembaruan data profil oleh pengguna dengan audit trail perubahan (SD-05) | Upgrade v5 |
| **Hapus** | Permintaan penghapusan akun → penghapusan/anonimisasi PII sesuai §5.5; tunduk pada batasan retensi legal dan integritas ledger | Upgrade v5 — lihat §5.5.3 |
| **Portabilitas** | Ekspor data profil dalam format terstruktur (mis. JSON/CSV) | Upgrade v5 `[PROPOSED DEFAULT: format final ditetapkan saat implementasi]` |

Aturan umum: setiap pelaksanaan hak subjek data diverifikasi identitasnya terlebih dahulu, dicatat pada audit trail, dan tidak boleh membuka data pihak lain.

## 5.3 Data Classification & Handling

Klasifikasi 4 tier didefinisikan pada §3.3 (BAB 3) dan diberlakukan di sini sebagai aturan governance:

1. Setiap dataset (tabel D1, bucket R2, namespace KV, log stream) wajib memiliki label tier maksimum.
2. Tier menentukan aturan handling: lokasi penyimpanan, enkripsi, redaction, akses, dan boleh/tidaknya keluar dari sistem (termasuk ke AI eksternal — §3.2).
3. Contoh penempatan:

| Contoh Data | Tier |
|---|---|
| Dokumentasi publik | PUBLIC |
| Kode internal, spesifikasi API, draft dokumen | INTERNAL |
| PII pengguna, data transaksi, riwayat auth | CONFIDENTIAL |
| `XENDIT_API_KEY`, `XENDIT_WEBHOOK_SECRET`, secret produksi, private key | RESTRICTED |

4. Upgrade tier otomatis: jika sebuah dataset menggabungkan beberapa tier, dataset mengikuti tier tertinggi.

## 5.4 Data Sharing & DPA

1. **Dasar sah wajib:** data pribadi hanya dibagikan ke pihak ketiga jika terdapat dasar pemrosesan yang sah sesuai UU PDP.
2. **DPA wajib:** setiap pihak ketiga yang memproses data pribadi atas nama AXION harus terikat Data Processing Agreement (DPA) sebelum data dibagikan.
3. **Minimisasi:** hanya field minimum yang diperlukan yang dibagikan (DP-02). Untuk payment gateway (Xendit), hanya data yang dipersyaratkan untuk pemrosesan pembayaran yang dikirim.
4. **Register pihak ketiga:** daftar pihak ketiga penerima data (nama, tujuan, kategori data, status DPA) dikelola dan ditinjau berkala; entri awal: Xendit (payment processing) `[APPROVED BASELINE: Xendit sebagai payment gateway, ARS-1]` — detail DPA Xendit perlu dikonfirmasi `[UNCERTAIN — verifikasi legal]`.
5. **Larangan:** dilarang menjual atau membagikan PII untuk keperluan di luar tujuan layanan tanpa dasar sah; dilarang mengirim data CONFIDENTIAL/RESTRICTED ke AI pihak ketiga (§3.2).

## 5.5 Retention & Deletion Policy

### 5.5.1 Tabel retensi

Baseline v4 §3.5 dipertahankan; nilai baru ditandai `[PROPOSED DEFAULT]`.

| Kategori Data | Tier | Retensi | Penyimpanan | Dasar |
|---|---|---|---|---|
| Debug trace biasa | INTERNAL | Pendek — TTL 7 hari | Workers log / Logpush; indeks KV ber-TTL | `[APPROVED BASELINE v4 §3.5]` |
| Indeks trace penting / audit penting | INTERNAL | 30–90 hari | KV ber-TTL | `[APPROVED BASELINE v4 §3.5]` |
| Error internal | INTERNAL | Menengah `[PROPOSED DEFAULT: 30 hari]` | Workers log / Logpush | Baseline v4 + usulan drafter |
| Auth failure / security event | CONFIDENTIAL | Menengah-panjang `[PROPOSED DEFAULT: 12 bulan]` | Log + KV/R2 batch | Baseline v4 + usulan drafter |
| Payment webhook raw payload | CONFIDENTIAL | Panjang `[PROPOSED DEFAULT: ≥ 60 bulan — konfirmasi legal]` | R2 (payload penuh) + D1 (metadata & hash) | `[APPROVED BASELINE pola v4 §4.3]` + usulan durasi |
| Catatan transaksi pembayaran | CONFIDENTIAL | Panjang `[PROPOSED DEFAULT: ≥ 60 bulan — konfirmasi legal]` | D1 | Usulan drafter (rekam finansial) |
| Coin ledger | CONFIDENTIAL | **Permanen — tidak ada penghapusan** (append-only; koreksi hanya reversal entry) | D1 ledger + audit log | SD-05, PP-05 `[APPROVED BASELINE Proposal 03]` |
| Rate limited event | INTERNAL | Pendek-menengah `[PROPOSED DEFAULT: 30 hari]` | Log (100% atau sampled) | Baseline v4 + usulan drafter |
| PII profil pengguna | CONFIDENTIAL | Selama akun aktif + periode pasca-penghapusan sesuai ketentuan legal | D1 | UU PDP |

Durasi bertanda *konfirmasi legal* harus divalidasi melalui review legal terpisah sebelum dikunci menjadi keputusan; sampai saat itu berlaku sebagai PROPOSED DEFAULT.

### 5.5.2 Mekanisme penghapusan

1. Penghapusan dilakukan per kategori sesuai tabel retensi (TTL KV untuk indeks, lifecycle/purge R2 untuk arsip, delete/anonymize D1 untuk data profil).
2. **Redaction mendahului retensi:** log tidak pernah mengandung secret, token, OTP, data kartu, atau PII (SEC-04), sehingga penghapusan log tidak menjadi satu-satunya lapisan proteksi.

### 5.5.3 Resolusi konflik: hak hapus vs ledger append-only

`[PROPOSED DEFAULT — perlu persetujuan Owner + review legal]`

1. Ledger coin bersifat append-only permanen (SD-05, PP-05) — entri ledger **tidak dihapus**.
2. Permintaan hapus data pengguna dipenuhi dengan cara: PII pada profil dihapus/dianonimisasi; referensi akun pada entri ledger dipertahankan sebagai **pseudonymous account identifier** yang tidak dapat dikaitkan kembali ke individu setelah pemetaan identitas dimusnahkan.
3. Pemusnahan pemetaan (account ↔ identitas) dicatat sebagai event audit terpisah.
4. Desain ini menjaga integritas finansial sekaligus memenuhi hak hapus secara substansial; keabsahan akhir terhadap UU PDP menunggu review legal (§5.1.3).

---

# BAB 6: ECONOMIC MODEL

> **Pemetaan dokumen inti:** BAB 6 → BLUEPRINT Project (mekanisme) + ROADMAP (strategi kapasitas) + BIBLE Perusahaan/OWNER-DECISIONS (supply cap).
> **Gap yang ditutup:** GAP-06 (Economic Model Constraints Tidak Ada).

## 6.1 Issuance Capacity Analysis

### 6.1.1 Supply cap (berlaku)

> `[OWNER-DECIDED: O3-REV-1]` Supply cap AXION Coin = **100.000.000 AXC per tahun kalender UTC**.
> `[SUPERSEDED]` ketentuan lama Versi 3.0 "100 juta coin per 5 tahun".
> Jika `issued_new` tahun berjalan mencapai 100.000.000 AXC, new issuance berhenti sampai tahun berikutnya atau keputusan owner yang sah. `[APPROVED BASELINE v4 §5.1]`

### 6.1.2 Budget issuance & Carry-Over

`[APPROVED BASELINE v4 §5.3 + OWNER-DECIDED: OD-2026-002]`

| Periode | Budget |
|---|---|
| Annual | 100.000.000 AXC |
| Monthly | ±8.333.333 AXC |
| Daily | ±273.972 AXC (365 hari) / ±273.224 AXC (kabisat) |
| Hourly | ±11.415–11.416 AXC |

**Aturan carry-over budget issuance** `[OWNER-DECIDED: OD-2026-002, efektif 2026-09-06]`:

Sisa budget issuance tahunan (unused annual budget) dapat dibawa ke tahun kalender berikutnya dengan cap maksimum 20% dari budget tahunan, yaitu 20.000.000 AXC.

Formula: `carryover(tahun N+1) = min(sisa_budget_tahun_N, 20.000.000 AXC)`

Bagian sisa yang melebihi cap hangus (tidak dapat di-issuance lagi). Budget issuance efektif tahun N+1 = 100.000.000 + carry-over(tahun N+1).

Distribusi carry-over ke budget monthly/daily mengikuti pola prorata yang sama dengan tabel di atas (budget efektif ÷ 12, ÷ 365/366) `[PROPOSED DEFAULT — mekanisme distribusi; dapat dikunci saat BLUEPRINT Project]`.

`[SUPERSEDED]`: klausul lama "tidak carry-over otomatis" (v4 §5.1, APPROVED DEFAULT tanpa Decision ID).

Contoh perhitungan:

| Sisa budget tahun N | Carry-over ke N+1 | Hangus | Budget efektif N+1 |
|---|---|---|---|
| 0 | 0 | 0 | 100.000.000 AXC |
| 15.000.000 | 15.000.000 | 0 | 115.000.000 AXC |
| 30.000.000 | 20.000.000 | 10.000.000 | 120.000.000 AXC |

### 6.1.3 Kapasitas reward dari issuance baru

Perhitungan dari budget daily (273.972 AXC) dan reward referensi 5.000 AXC/user/hari `[APPROVED BASELINE v4 §5.2–5.3]`:

| Metrik | Nilai | Basis |
|---|---|---|
| Kapasitas reward penuh (5.000 AXC/user/hari) | **≈ 54 user/hari** (273.972 ÷ 5.000 = 54,79) | v4 §5.3 |
| Kapasitas reward penuh per tahun | 20.000 user-day/tahun (100.000.000 ÷ 5.000) | turunan aritmetika |
| Kapasitas bulanan (reward penuh) | ≈ 1.666 user-day/bulan (8.333.333 ÷ 5.000) | turunan aritmetika |

Kapasitas efektif per level reward (issuance baru saja):

| Reward efektif/user/hari | Kapasitas user/hari |
|---|---|
| 5.000 AXC (maks R1) | ≈ 54 |
| 2.500 AXC | ≈ 109 |
| 1.000 AXC | ≈ 273 |
| 500 AXC | ≈ 547 |

> **Catatan:** recirculation pool menambah kapasitas **tanpa menambah supply baru** (§6.3) `[APPROVED BASELINE v4 §5.3, R3]`. Angka di atas adalah batas atas dari issuance baru saja.

Implikasi kapasitas dengan carry-over maksimum (turunan aritmetika dari §6.1.2 — FACT, bukan kebijakan baru):

| Metrik | Tanpa carry-over | Dengan carry-over maksimum |
|---|---|---|
| Budget tahunan efektif | 100.000.000 AXC | 120.000.000 AXC |
| Daily budget | ±273.972 AXC | ±328.767 AXC (÷365) |
| Kapasitas reward penuh (5.000 AXC/user/hari) | ≈ 54 user/hari | ≈ 65 user/hari |
| Kapasitas reward penuh tahunan | 20.000 user-day | 24.000 user-day |

## 6.2 Reward Mechanism & Constraints

### 6.2.1 Aturan reward (dipertahankan)

`[APPROVED BASELINE v4 §5.4]`

- **R1:** Reward maksimum per user = 5.000 AXC/hari (*configured maximum*, bukan janji mutlak).
- **R2:** `actual_daily_reward = min(configured_daily_reward_max, user_daily_reward_limit, available_pool_allocation)`.
- **R3:** Reward dapat berasal dari daily new issuance budget atau recirculation pool; new issuance tidak boleh melebihi cap tahunan.
- **R4:** Jika pool tidak cukup → kurangi, tunda, antrekan/hold, gunakan recirculation jika tersedia, atau tolak dengan audit. **Dilarang:** mencetak coin di luar cap, memberi reward tanpa ledger entry, mengubah balance tanpa transaction ledger (instansiasi SD-12, PP-05).

### 6.2.2 Parameter referensi

`[APPROVED BASELINE v4 §5.2]`

- Reward referensi awal: 5.000 AXC/hari ≈ 500 IDR (harga dapat berubah).
- Harga AXC terhadap IDR disimpan sebagai *price snapshot*; perubahan harga **tidak mengubah saldo/ledger**.
- Fase awal: tidak ada peer-to-peer transfer; tidak ada coin expiry.
- Sumber reward: login, game, iklan, tugas harian (via AXION Account).

### 6.2.3 Constraint analysis: reward vs kapasitas (baru)

| Constraint | Implikasi desain |
|---|---|
| Cap tahunan 100 juta AXC | Total reward penuh yang dapat didanai issuance baru = 20.000 user-day/tahun; sistem tidak boleh menjanjikan reward penuh ke semua user secara simultan |
| Budget harian ±273.972 AXC | `available_pool_allocation` pada R2 harus dihitung dari sisa budget harian + saldo recirculation pool |
| Larangan cetak di luar cap (R4, SD-12) | Shortfall kapasitas hanya boleh direspons via mekanisme R4 (kurangi/tunda/antre/recirculation/tolak), tidak pernah via issuance ekstra |
| Reward = configured maximum, bukan janji (R1) | Komunikasi produk wajib menyatakan reward "hingga" / "tunduk pada ketersediaan pool" |

## 6.3 Recirculation & Burn

### 6.3.1 Recirculation pool mechanism

Akun sistem terkait `[APPROVED BASELINE v4 §5.5]`: `SYS:RECIRCULATION_POOL`, `SYS:REVENUE`, `SYS:TREASURY_ISSUANCE`, plus pool reward (`SYS:DAILY_REWARD_POOL`, `SYS:TASK_REWARD_POOL`, `SYS:AD_REWARD_POOL`, `SYS:GAME_REWARD_POOL`).

Alur coin kembali ke pool (baru):

```
1. SPEND (user membelanjakan coin)
   Ledger entry: debit saldo user → kredit SYS:REVENUE
   (pencatatan pendapatan, append-only)

2. RECIRCULATION FEED (berkala / cron)
   Ledger entry: debit SYS:REVENUE → kredit SYS:RECIRCULATION_POOL
   sebesar porsi recirculation yang dikonfigurasi

3. REWARD DISTRIBUTION (reward engine)
   Sumber prioritas: daily new issuance budget (SYS:TREASURY_ISSUANCE)
   Fallback: SYS:RECIRCULATION_POOL bila budget issuance tidak cukup (R3)
   Degradasi bila masih kurang: kurangi / tunda / antre / tolak dengan audit (R4)
```

| Parameter | Spesifikasi | Status |
|---|---|---|
| Porsi spend yang masuk recirculation vs revenue | Rasio konfigurasi (mis. 100% recirculation pada fase awal karena volume kecil) | `[PROPOSED DEFAULT — keputusan bisnis Owner]` |
| Frekuensi RECIRCULATION FEED | Cron harian (mengikuti pola `DAILY_MISMATCH_AUDIT`) | `[PROPOSED DEFAULT]` |
| Sumber prioritas reward | Issuance baru dahulu, recirculation sebagai penambah kapasitas | `[PROPOSED DEFAULT — konsisten R3/R4]` |
| Larangan | Recirculation tidak boleh menciptakan supply baru; total `issued_new` tetap ≤ cap tahunan | `[OWNER-DECIDED: O3-REV-1]` |

Seluruh entri recirculation tercatat pada ledger append-only dan terekonsiliasi oleh `COIN_SUPPLY_BUDGET_RECONCILE` `[APPROVED BASELINE v4 §5.5]`.

### 6.3.2 Burn mechanism

| Parameter | Spesifikasi | Status |
|---|---|---|
| Akun burn | `SYS:BURN` | `[APPROVED BASELINE v4 §5.5]` |
| Definisi burn | Transfer append-only ke `SYS:BURN`; saldo `SYS:BURN` dihitung **keluar dari sirkulasi secara permanen** | Upgrade v5 |
| Sifat | Tidak ada mekanisme pengeluaran dari `SYS:BURN`; koreksi hanya reversal entry dengan approval (konsisten SD-05) | Upgrade v5 |
| Pengaruh terhadap cap | Burn **tidak menambah headroom issuance**: cap 100 juta AXC/tahun mengatur `issued_new`, bukan net circulation | `[PROPOSED DEFAULT — perlu konfirmasi Owner]` |
| Trigger burn | Belum didefinisikan pada v4 (tidak ada di Proposal 03) | `[UNCERTAIN — keputusan Owner diperlukan sebelum implementasi]` |

## 6.4 Anti-Inflation Controls

| Kontrol | Spesifikasi | Status |
|---|---|---|
| Maximum supply | 100.000.000 AXC/tahun kalender UTC | `[OWNER-DECIDED: O3-REV-1]` |
| Budget issuance bertingkat | Annual → monthly → daily → hourly (§6.1.2) | `[APPROVED BASELINE]` |
| Carry-over dengan cap 20% | Sisa budget tahunan dapat dibawa ke tahun berikutnya maksimum 20.000.000 AXC; bagian di atas cap hangus; budget efektif tahun berikutnya = 100 juta + carry-over | `[OWNER-DECIDED: OD-2026-002]` |
| Burn mechanism | §6.3.2 | Upgrade v5 |
| Velocity control | 1 tx/detik, 10 tx/menit, 100 tx/jam, 500 tx/hari; max earn 25.000 AXC/hari; spend max 10.000 AXC/tx, 50.000 AXC/hari | `[APPROVED BASELINE v4 §5.5]` |
| Dynamic reward adjustment | Formula R2: `actual_daily_reward = min(...)` — reward turun otomatis saat pool menipis | `[APPROVED BASELINE v4 §5.4]` |
| Degradasi terkontrol (R4) | Kurangi / tunda / antre / recirculation / tolak dengan audit — tidak pernah cetak ekstra | `[APPROVED BASELINE v4 §5.4]` |
| Fraud-driven inflation control | Risk engine 0–100 (LOW 0–30 proses; MEDIUM 31–60 delay/reduce; HIGH 61–80 HOLD; CRITICAL 81–100 REJECT/FREEZE), device-account binding (max 2 akun/device, cooldown 3 hari, high-risk delay 24 jam), rekonsiliasi harian (`COIN_DUPLICATE_CLAIM_SCAN`, `COIN_DEVICE_SYBIL_SCAN`, `COIN_VELOCITY_ANOMALY_SCAN`) | `[APPROVED BASELINE v4 §5.5]` |
| Enforcement cap | Saat `issued_new` tahun berjalan = 100.000.000 → new issuance berhenti sampai tahun berikutnya/keputusan owner | `[OWNER-DECIDED: O3-REV-1]` |

## 6.5 Gap Analysis: Target vs Capacity

### 6.5.1 Baseline kapasitas (fact)

| Parameter | Nilai | Klasifikasi |
|---|---|---|
| Kapasitas reward penuh dari issuance baru | ≈ 54 user/hari | FACT (perhitungan dari baseline APPROVED) |
| Kapasitas reward penuh tahunan | 20.000 user-day/tahun | FACT |
| Kapasitas tambahan dari recirculation | Fungsi volume transaksi; belum terukur | UNKNOWN (belum ada transaksi riil) |
| Target user aktif harian | **Belum ditetapkan dalam dokumen APPROVED** | UNKNOWN — input Owner diperlukan |
| Gap (target − kapasitas) | Tidak dapat dihitung sebelum target ditetapkan | UNKNOWN |

### 6.5.2 Kerangka analisis (wajib dipakai saat target ditetapkan)

```
gap_harian = target_user_rewarded_per_hari − kapasitas_issuance(level_reward) − kapasitas_recirculation(terukur)
```

Jika `gap_harian > 0`, strategi penutupan (berurutan sesuai preferensi risiko):

| # | Strategi | Dasar | Status |
|---|---|---|---|
| 1 | Aktifkan/perbesar recirculation pool | R3, §6.3.1 | Mekanisme baru (draft) |
| 2 | Dynamic reward adjustment (turunkan reward efektif via R2) | R2 | `[APPROVED BASELINE]` |
| 3 | Tiered reward (reward berbeda per segmen aktivitas: login < tugas < iklan < game) | Turunan R1–R2 | `[PROPOSED DEFAULT]` |
| 4 | Antrean/hold reward saat pool kosong | R4 | `[APPROVED BASELINE]` |
| 5 | Monetisasi (ads/pembelian) untuk mengisi pool via revenue → recirculation | §6.3.1 | `[PROPOSED DEFAULT — keputusan bisnis]` |
| 6 | Penyesuaian price snapshot (mengubah nilai IDR per AXC, bukan jumlah ledger) | v4 §5.2 | `[PROPOSED DEFAULT]` |
| 7 | Perubahan supply cap | **Hanya via Owner Decision baru** | `[OWNER-DECIDED: O3-REV-1 mengikat sampai superseded]` |

> Semua target yang bergantung pada kapasitas issuance (mis. "X user mendapat reward penuh per hari") wajib berlabel **ASPIRATIF** sampai baseline dan asumsinya divalidasi (BAB 8 §8.2).

---

# BAB 7: GOVERNANCE & OWNERSHIP

> **Pemetaan dokumen inti:** BAB 7 → BIBLE Perusahaan + OWNER-DECISIONS.md.
> **Gap yang ditutup:** GAP-07 (Ownership & Decision Authority Matrix Tidak Ada).

## 7.1 Decision Authority Matrix

| Domain | Decider | Eskalasi ke | Catatan |
|---|---|---|---|
| Arsitektur teknis | Tech Lead | Owner | Termasuk kontrak teknis BAB 4, pemilihan pola desain |
| Kebijakan bisnis | Owner | — | Termasuk pricing, prioritas produk |
| Keamanan | Security Lead | Owner | Termasuk threat model, AI external policy, insiden |
| Ekonomi token | Owner | — | Supply cap, burn trigger, recirculation ratio, reward level |
| Operasional harian | Ops Lead | Tech Lead | Tuning parameter dalam batas yang sudah APPROVED |

Ketentuan tambahan:
1. Persetujuan dokumen inti mengikuti matriks BAB 1 §1.4 (CEO/Owner sebagai approver final).
2. Perubahan prinsip LOCKED (BAB 2) berada di luar kewenangan seluruh decider di atas — hanya via Owner Decision (§7.2).
3. AI adalah drafter/assistant, bukan decision authority pada domain mana pun `[APPROVED BASELINE v4 §7.3]`.

**Penunjukan pemegang peran** `[OWNER-DECIDED: OD-2026-001, efektif 2026-09-06]`:

| Peran | Pemegang | Dasar |
|---|---|---|
| CEO | AZRIEL | v4 §11 |
| Manager | Kisa | v4 §11 |
| PM | Suhen | v4 §11 |
| Tech Lead | Owner (AZRIEL) — merangkap | OD-2026-001, Opsi A |
| Security Lead | Owner (AZRIEL) — merangkap | OD-2026-001, Opsi A |
| Ops Lead | Owner (AZRIEL) — merangkap | OD-2026-001, Opsi A |

**Klausul transisi** `[OWNER-DECIDED: OD-2026-001 Adendum, 2026-09-12]`:

Penunjukan peran terpisah (Tech Lead / Security Lead / Ops Lead) akan dilakukan via Owner Decision baru ketika **kedua** kondisi berikut terpenuhi bersama (AND):

1. Tersedia kandidat dengan kualifikasi yang dipercaya Owner; **dan**
2. Beban keputusan Owner telah melampaui SLA eskalasi (§7.3.2) selama dua review bulanan berturut-turut.

**Implikasi governance:** seluruh eskalasi domain teknis, keamanan, dan operasional bermuara langsung ke Owner by design. Konsentrasi otoritas meningkatkan relevansi risiko R-007 (keputusan tertunda karena ketergantungan pada ketersediaan Owner) — lihat §9.1.2.

## 7.2 Decision ID System & Register

### 7.2.1 Format Decision ID

```
OD-YYYY-NNN
│   │     └── nomor urut 3 digit, reset tiap tahun
│   └──────── tahun kalender keputusan
└──────────── Owner Decision
```

Contoh: `OD-2026-001`.

### 7.2.2 Aturan penggunaan

1. Setiap keputusan Owner baru wajib diberi Decision ID dan dicatat pada register OWNER-DECISIONS (§7.4).
2. ID legacy (O3-REV-1, P01, P02-D1..D10, P03-D1..D19, P04-D1..D10, ARS-1..4, PROPOSAL-ARCH-UPGRADE-001) **tetap sah** dan tidak dinomori ulang — penjagaan audit trail; tidak ada silent rewrite (BAB 1 §1.3).
3. Setiap dokumen yang merujuk keputusan wajib menyebut Decision ID-nya.
4. Keputusan tanpa ID tidak dapat dianggap OWNER-DECIDED.

### 7.2.3 Register OWNER-DECISIONS

Lokasi: `/docs/company/OWNER-DECISIONS.md` `[APPROVED BASELINE v4 §7.4]`. Field minimal per entri:

| Field | Wajib | Keterangan |
|---|---|---|
| ID | ✅ | `OD-YYYY-NNN` atau ID legacy |
| Tanggal | ✅ | ISO 8601 |
| Keputusan | ✅ | Ringkasan keputusan |
| Status | ✅ | PROPOSED / UNDER_REVIEW / APPROVED / IMPLEMENTED / VERIFIED / REJECTED / SUPERSEDED / DEPRECATED |
| Supersedes | Bila ada | ID keputusan yang digantikan |
| Peminta / drafter | ✅ | Termasuk bila drafter adalah AI |

### 7.2.4 Aturan label DEFAULT vs OWNER-DECIDED

1. Label **OWNER-DECIDED** hanya sah jika terdapat Decision ID pada register.
2. Setiap aturan berlabel "APPROVED DEFAULT" **wajib memiliki Decision ID**; jika tidak ada, labelnya **wajib diubah menjadi PROPOSED DEFAULT** (aturan PROPOSAL-ARCH-UPGRADE-001, APPROVED).
3. Implementasi pertama aturan ini: klausul *unused annual budget tidak carry-over otomatis* (v4 §5.1) — sempat diturunkan menjadi PROPOSED DEFAULT karena tanpa Decision ID, kemudian dikonfirmasi ulang sebagai carry-over dengan cap 20% melalui **OD-2026-002** (lihat §6.1.2).

## 7.3 Escalation Path

### 7.3.1 Trigger eskalasi ke Owner

| # | Trigger | Sumber |
|---|---|---|
| E-1 | Keputusan di luar domain decider pada §7.1 | Matriks otoritas |
| E-2 | Konflik antar dokumen setara → ditandai `[CONFLICT]` | `[APPROVED BASELINE v4 §7.3]` |
| E-3 | Exception finansial: unknown transaction, amount mismatch, terminal conflict, transisi terlarang yang menyangkut uang | `[APPROVED BASELINE v4 §4.2–4.3]` |
| E-4 | Risiko project dengan score ≥ 6 (BAB 9 §9.4) | BAB 9 |
| E-5 | Usulan perubahan prinsip LOCKED (BAB 2) | BAB 2 §2.0 |
| E-6 | Insiden keamanan yang menyentuh data CONFIDENTIAL/RESTRICTED | BAB 3 |
| E-7 | Permintaan perubahan supply cap / parameter ekonomi token | BAB 6, O3-REV-1 |

### 7.3.2 Alur

```
Deteksi (role mana pun)
  → Decider domain (§7.1) menilai: dalam otoritas?
     ├── YA  → diputuskan + dicatat (Decision ID bila Owner decision)
     └── TIDAK / belum selesai dalam SLA → eskalasi ke Owner/CEO
CEO/Owner = arbiter final (hierarki v4 §7.3)
```

SLA respons eskalasi `[PROPOSED DEFAULT]`: P0 (keamanan/data integrity/finansial) → segera; lainnya → 2×24 jam.

## 7.4 Owner Decisions Log

`[APPROVED BASELINE v4 §13 — dipertahankan]`

| ID | Keputusan | Status | Format ID |
|---|---|---|---|
| O3-REV-1 | Supply cap AXION Coin = 100.000.000 AXC per tahun (menggantikan ketentuan 5 tahun) | OWNER DECISION / APPROVED | Legacy |
| P01 | Baseline timeout, retry, rate limit, circuit breaker, audit/tracing | APPROVED | Legacy |
| P02-D1..D10 | State machine pembayaran, terminal state, R2 raw payload, cron, minor units, exception review | APPROVED | Legacy |
| P03-D1..D19 | Ledger append-only, UTC claim date, risk threshold, velocity, spend limit, adjustment approval, annual cap enforcement | APPROVED | Legacy |
| P04-D1..D10 | 6 dokumen wajib, pemisahan perusahaan/project, changelog wajib, AI drafter, struktur /docs, penamaan | APPROVED | Legacy |
| ARS-1 | Xendit sebagai payment gateway uang tunai/digital | APPROVED | Legacy |
| ARS-2 | Build mobile app via Nitron di Google Colab (web wrapper) | APPROVED | Legacy |
| ARS-3 | Workers 3 lapis di Cloudflare | APPROVED | Legacy |
| ARS-4 | Environment Secret → HTTP Credential → Environment Secret Validation, tanpa master key | APPROVED | Legacy |
| PROPOSAL-ARCH-UPGRADE-001 (D-01..D-05) | Kerangka kerja upgrade v4→v5: struktur 10 BAB, exit criteria, out of scope, prioritas blocking-first | APPROVED oleh Owner | Transisi → format OD |
| OD-2026-001 | Opsi A — Owner (AZRIEL) merangkap Tech Lead, Security Lead, dan Ops Lead untuk fase awal (§7.1) | APPROVED (2026-09-06) | OD |
| OD-2026-001 (Adendum) | Trigger klausul transisi Opsi A: kandidat kredibel tersedia **DAN** beban keputusan Owner melampaui SLA eskalasi selama 2 review bulanan berturut-turut (§7.1) | APPROVED (2026-09-12) | OD |
| OD-2026-002 | Opsi C — Carry-over budget issuance dengan cap 20% dari budget tahunan (maks 20.000.000 AXC); sisa di atas cap hangus (§6.1.2, §6.4) | APPROVED (2026-09-06) | OD |
| OD-2026-002 (Adendum) | Konfirmasi interpretasi cap carry-over = `min(sisa_budget, 20.000.000 AXC)`; koreksi tanggal efektif menjadi 2026-09-06 | APPROVED (2026-09-12) | OD |
| OD-2026-003 | APPROVE arsitektur v5 sebagai dokumen tunggal final, bersyarat penerapan OD-2026-001/002 (+ adendum) ke badan dokumen dan penggabungan draft.1+2+3 | APPROVED (2026-09-12) | OD |

ID berikutnya yang tersedia: `OD-2026-004` — kandidat penggunaan: keputusan atas item yang masih terbuka (rasio recirculation §6.3.1, burn trigger §6.3.2, target user §6.5.1, skema scoring risiko §9.2, SLA eskalasi §7.3.2, mekanisme distribusi carry-over §6.1.2).

---

# BAB 8: OKR & STRATEGIC TARGETS

> **Pemetaan dokumen inti:** BAB 8 → ROADMAP Perusahaan + ROADMAP Project.
> **Gap yang ditutup:** GAP-08 (OKR Framework Tanpa Baseline).

## 8.1 Target Framework

Setiap target wajib memiliki tiga komponen:

| Komponen | Definisi |
|---|---|
| **Baseline** | Kondisi saat ini yang terukur/terverifikasi |
| **Asumsi** | Kondisi yang harus true agar target dapat tercapai |
| **Status label** | ASPIRATIF / COMMITTED / VALIDATED (§8.2) |

Target tanpa baseline dan asumsi memadai tidak boleh diberi label COMMITTED atau VALIDATED.

## 8.2 Target Status

| Label | Definisi | Syarat |
|---|---|---|
| **ASPIRATIF** | Target yang belum divalidasi; realisasi belum terbukti | Default untuk semua target baru |
| **COMMITTED** | Target dengan baseline + asumsi terdokumentasi dan Owner mengalokasikan sumber daya; realisasi belum diverifikasi | Baseline + asumsi + komitmen otoritas |
| **VALIDATED** | Target tercapai dengan evidence (VERIFIED — test/inspeksi/hasil operasional) | Evidence sesuai verification contract |

Aturan:
1. Target yang belum divalidasi dan belum memenuhi syarat COMMITTED **wajib berlabel ASPIRATIF**.
2. Transisi label hanya via review cadence (§8.3) atau mekanisme revisi (§8.4).
3. `APPROVED` pada dokumen ≠ VALIDATED pada target (konsisten SD-11 dan v4 §12: APPROVED = acuan ditetapkan, bukan realisasi terbukti).

### 8.2.1 Target jangka pendek — rencana 4 hari `[APPROVED BASELINE v4 §8]`

| Target | Status v4 | Baseline | Asumsi | Label |
|---|---|---|---|---|
| Day 0–1: menyempurnakan arsitektur | ✅ | v4 APPROVED tercapai; v5 APPROVED (OD-2026-003, 2026-09-12) | PROPOSAL-ARCH-UPGRADE-001 disetujui (✅ terpenuhi) | COMMITTED — tercapai (v4 dan v5 selesai) |
| Day 2–3: merancang & membuat BIBLE/BLUEPRINT/ROADMAP perusahaan | ⏳ | 0 dari 3 dokumen inti tertulis | Arsitektur v5 memenuhi exit criteria; prinsip uji BAB 10 terpenuhi | COMMITTED |
| Day 4: audit 3 dokumen (TEAM) + APPROVE/REVISION (CEO) | ⏳ | Belum berjalan | Day 2–3 selesai; checklist audit Day 4 Proposal 04 tersedia | COMMITTED |

### 8.2.2 Target 5 tahun — fase implementasi `[APPROVED BASELINE v4 §9]`

Baseline keseluruhan: Fase 0 (Architecture Completion) sedang berjalan; seluruh proposal BELUM IMPLEMENTASI, verifikasi NOT_RUN `[APPROVED BASELINE v4 §12]`.

| Fase | Nama | Baseline | Asumsi kunci | Label |
|---|---|---|---|---|
| 0 | Architecture Completion | v4 APPROVED; v5 APPROVED (OD-2026-003) | v5 disetujui Owner (✅ terpenuhi) | COMMITTED — tercapai |
| 1 | Documentation & Audit | Belum berjalan | v5 final; 6 dokumen + OWNER-DECISIONS tersedia | COMMITTED |
| 2 | Foundation Workers | Belum berjalan | Fase 1 selesai; credential & budget Cloudflare tersedia | ASPIRATIF |
| 3 | Auth & Account | Belum berjalan | Fase 2 selesai | ASPIRATIF |
| 4 | Payment Xendit | Belum berjalan | Fase 3 selesai; verifikasi signature Xendit `[UNCERTAIN]` tertutup | ASPIRATIF |
| 5 | AXION Coin Core | Belum berjalan | Fase 4 selesai; keputusan ekonomi §6.3 terkunci | ASPIRATIF |
| 6 | Anti-Fraud & Risk Engine | Belum berjalan | Fase 5 selesai | ASPIRATIF |
| 7 | Mobile App | Belum berjalan | Fase 6 selesai; jalur Nitron/Colab tetap valid | ASPIRATIF |
| 8 | AXION AI Integration | Belum berjalan | Fase 7 selesai | ASPIRATIF |

Release gates (dipertahankan): dokumen approved, security review, payment verification, coin ledger verification, audit trail available, CEO approval untuk release penting `[APPROVED BASELINE v4 §9]`.

### 8.2.3 Product roadmap `[APPROVED BASELINE v4 §10]`

| Produk | Prioritas v4 | Baseline | Asumsi kunci | Label |
|---|---|---|---|---|
| AXION AI | High | Belum ada implementasi | Workers seluruh produk tersedia; sistem deteksi terdefinisi | ASPIRATIF |
| AXION Account | High | Belum ada implementasi | Fase 3 selesai | ASPIRATIF |
| AXION Ads | Medium | Belum ada implementasi | Basis pengguna & AXION Account berjalan | ASPIRATIF |
| AXION Coin | Medium | Desain APPROVED (Proposal 03); implementasi belum ada | Fase 5–6 selesai; kapasitas §6.5 dipahami | ASPIRATIF |

Prioritas High/Medium dipertahankan sebagai arah perencanaan APPROVED; label ASPIRATIF merujuk pada **realisasi**, bukan pada validitas prioritas.

## 8.3 Review Cadence

1. **Quarterly review** wajib untuk seluruh target COMMITTED dan ASPIRATIF.
2. Agenda minimum: update baseline, uji asumsi, transisi label, identifikasi target usang.
3. Output review dicatat pada changelog ROADMAP terkait (BAB 1 §1.3).
4. Arsitektur v5 APPROVED per 2026-09-12 (OD-2026-003) — syarat penjadwalan terpenuhi; tanggal pasti review quarterly pertama menunggu penjadwalan Owner `[PROPOSED DEFAULT — tanggal]`.

## 8.4 Revision Mechanism

| Perubahan | Otoritas | Mekanisme |
|---|---|---|
| Koreksi editorial target | PM | Changelog |
| Perubahan baseline/status label | PM + konfirmasi decider domain (§7.1) | Quarterly review |
| Perubahan target COMMITTED (nilai, tanggal, scope) | Owner | Owner Decision `OD-YYYY-NNN` |
| Target baru | Decider domain → Owner bila bisnis/token | Register pada ROADMAP + changelog |

Aturan penurunan label: jika asumsi kunci target COMMITTED terbukti false, target diturunkan ke ASPIRATIF pada review berikutnya dan dicatat alasannya.

---

# BAB 9: RISK MANAGEMENT

> **Pemetaan dokumen inti:** BAB 9 → ROADMAP Perusahaan + ROADMAP Project.
> **Gap yang ditutup:** GAP-09 (Risk Register Framework Tidak Ada).

## 9.1 Risk Register

### 9.1.1 Template

| ID | Risiko | Likelihood (H/M/L) | Impact (H/M/L) | Score | Mitigasi | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-001 | … | … | … | … | … | … | Open / Mitigating / Mitigated / Closed / Escalated |

### 9.1.2 Entri awal (≥ 5 risiko utama project)

| ID | Risiko | L | I | Score | Mitigasi | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-001 | **Scope creep** — penambahan di luar scope v5/implementasi | M | H | 6 | Section Out of Scope pada proposal APPROVED; change control BAB 1 §1.3; owner gate per §7.3 | PM | Open (mitigasi terpasang) |
| R-002 | **Perfectionism loop** — dokumen tidak pernah "cukup matang" | M | H | 6 | Exit Criteria terukur EC-01..EC-13; timebox ±8–10 sesi kerja (proposal APPROVED) | PM / Owner | Open |
| R-003 | **Technical debt accumulation** | M | H | 6 | Kontrak sebelum implementasi (BAB 4); migration additive + feature flags + "jangan hapus ledger" `[APPROVED BASELINE v4 §5.5]`; audit sebelum coding | Tech Lead | Open |
| R-004 | **Security breach** (kebocoran secret/PII, akses tidak sah) | M | H | 6 | BAB 3 (threat model, AI policy, klasifikasi data); release gate security review; redaction SEC-04 | Security Lead | Open |
| R-005 | **Budget overrun** (budget issuance token & budget operasional project) | M | M | 4 | Supply cap O3-REV-1; budget issuance §6.1.2; `COIN_SUPPLY_BUDGET_RECONCILE`; review quarterly biaya operasional | Owner / Ops Lead | Open |
| R-006 | **Over-engineering** fase dokumentasi | M | M | 4 | Prinsip proposal APPROVED: "cukup untuk menurunkan 3 dokumen, bukan untuk implementasi"; Out of Scope | Tech Lead | Open |
| R-007 | **Keputusan tertunda** (ketergantungan pada ketersediaan Owner) | M | M | 4 | Blocking items di-draft dahulu, Owner hanya approve/reject (proposal APPROVED); SLA eskalasi §7.3.2 | PM | Open |

> Catatan peran (final): Peran Tech Lead, Security Lead, dan Ops Lead dipegang oleh Owner berdasarkan **OD-2026-001** (Opsi A) — lihat §7.1. Eskalasi risiko menuju Owner secara langsung by design. Konsentrasi otoritas meningkatkan relevansi R-007 (keputusan tertunda); direkomendasikan pemantauan khusus terhadap R-007 pada review bulanan dan uji asumsi pada quarterly review (§8.3).

### 9.1.3 Relasi dengan risk engine transaksi

Risk engine 0–100 untuk transaksi AXION Coin (LOW 0–30 proses langsung; MEDIUM 31–60 delay/reduce; HIGH 61–80 HOLD; CRITICAL 81–100 REJECT/FREEZE review), velocity limit, dan device-account binding adalah **kontrol anti-fraud operasional** `[APPROVED BASELINE v4 §5.5]` — terpisah dari risk register project ini dan tetap berlaku apa adanya.

## 9.2 Risk Assessment Matrix

Likelihood × Impact, skor 1–3 per dimensi (L=1, M=2, H=3):

| | **Impact L (1)** | **Impact M (2)** | **Impact H (3)** |
|---|---|---|---|
| **Likelihood H (3)** | 3 — LOW | 6 — HIGH | 9 — HIGH |
| **Likelihood M (2)** | 2 — LOW | 4 — MEDIUM | 6 — HIGH |
| **Likelihood L (1)** | 1 — LOW | 2 — LOW | 3 — LOW |

Klasifikasi score:
- **LOW (1–3):** diterima, monitor pada review bulanan.
- **MEDIUM (4–5):** mitigasi wajib + monitor bulanan.
- **HIGH (≥6):** mitigasi wajib + eskalasi ke Owner (§9.4).

Skema scoring ini `[PROPOSED DEFAULT]` (kerangka baru; belum ada Owner Decision).

## 9.3 Mitigation Plans

Untuk risiko HIGH (score ≥ 6):

| ID | Rencana mitigasi | Indikator keberhasilan |
|---|---|---|
| R-001 | (1) Setiap permintaan di luar BAB 1–10 dicatat sebagai rekomendasi, bukan implementasi; (2) perubahan scope hanya via Owner Decision | Nol perubahan di luar scope tanpa Decision ID saat audit berikutnya |
| R-002 | (1) Verifikasi draft ini terhadap EC-01..EC-13 (§ penutup); (2) owner gate: approval/reject maksimal 1 sesi setelah draft final | v5 mencapai status APPROVED atau daftar revisi terbatas |
| R-003 | (1) Seluruh implementasi melewati implementation gate (scope, keputusan, kontrak, kriteria acceptance); (2) rollback strategy additive | Tidak ada perubahan kontrak publik tanpa migration record |
| R-004 | (1) Penutupan item `[UNCERTAIN]` (signature Xendit, device fingerprint) sebelum implementasi; (2) review redaction log; (3) larangan data §3.2 diberlakukan sejak fase dokumentasi | Nol temuan secret/PII dalam log & dokumen saat audit Day 4 |

## 9.4 Review Cadence & Escalation

1. **Review bulanan** risk register oleh PM bersama decider domain; hasil dicatat (changelog ROADMAP).
2. **Eskalasi otomatis ke Owner** bila: score ≥ 6, status memburuk dua review berturut-turut, atau trigger E-3/E-4/E-6 (§7.3) terjadi.
3. Risiko baru ditemukan → entri register dalam 1×24 jam `[PROPOSED DEFAULT]`.
4. Risiko Closed/Mitigated tetap tersimpan sebagai riwayat (append-only pada register — konsistensi SD-05).

---

# BAB 10: MAPPING TO CORE DOCUMENTS

> **Gap yang ditutup:** BAB 10 (Mapping) + traceability temuan audit.
> **Prinsip uji (PROPOSAL-ARCH-UPGRADE-001, APPROVED):** *"Jika seorang engineer/PM baru membaca arsitektur v5 dari halaman pertama hingga terakhir, apakah dia bisa menulis Bible, Blueprint, dan Roadmap tanpa perlu bertanya lagi kepada siapa pun?"* — Jawaban harus: **YA**.

## 10.1 Bible ← Bab 1, 2, 5, 7

Boundary `[APPROVED BASELINE v4 §7.2]`: BIBLE berisi aturan, prinsip, kebijakan global, governance, non-negotiable; **tidak boleh** berisi skema tabel, endpoint API, atau kode spesifik project.

| Sumber v5 | Konten | Tujuan |
|---|---|---|
| §1.2–1.4 | Lifecycle, daya ikat status, approval authority | BIBLE Perusahaan (governance dokumen) |
| §2.1 | Prinsip desain sistem LOCKED (termasuk non-negotiable: no master key, secret tidak di repo, pemisahan dokumen, larangan klaim verified tanpa evidence) | BIBLE Perusahaan |
| §2.2 | 6 prinsip pembayaran canonical LOCKED | BIBLE Perusahaan (kebijakan pembayaran global) |
| §2.3 | Prinsip keamanan LOCKED | BIBLE Perusahaan (kebijakan keamanan global) |
| §2.4 | Prinsip data & privasi LOCKED | BIBLE Perusahaan (kebijakan privasi global) |
| §3.2 | AI External Usage Policy | BIBLE Perusahaan (kebijakan) |
| §3.3 | Klasifikasi data 4 tier | BIBLE Perusahaan (kebijakan) |
| §5.1–5.4 | Baseline UU PDP, hak subjek data, klasifikasi & handling, DPA | BIBLE Perusahaan (kebijakan privasi) |
| §6.1.1 | Supply cap 100 juta AXC/tahun | OWNER-DECISIONS + BIBLE Perusahaan `[APPROVED BASELINE v4 §7.2]` |
| §6.4 | Anti-inflation controls sebagai kebijakan ekonomi digital global | BIBLE Perusahaan |
| §7.1–7.3 | Decision Authority Matrix, Decision ID, eskalasi | BIBLE Perusahaan + OWNER-DECISIONS |
| Ledger append-only coin (SD-05, PP-05) | Invariant ledger | BIBLE Project + BLUEPRINT Project `[APPROVED BASELINE v4 §7.2]` |

## 10.2 Blueprint ← Bab 3, 4, 6

| Sumber v5 | Konten | Tujuan |
|---|---|---|
| §3.1 | Threat assessment | BLUEPRINT Perusahaan (security baseline) |
| §3.4 | Authentication & authorization spec | BLUEPRINT Perusahaan |
| §3.5 | Replay protection & HMAC spec | BLUEPRINT Perusahaan |
| §4.1 | Tabel header lengkap | BLUEPRINT Perusahaan (pola Workers 3 lapis & header internal `[APPROVED BASELINE v4 §7.2]`) |
| §4.2–4.3 | Auth flow sequence, error response standard | BLUEPRINT Perusahaan |
| §4.4–4.5 | Webhook & SLA, idempotency, rate limiting | BLUEPRINT Perusahaan + BLUEPRINT Project (jalur finansial) |
| §4.6 | Constant-time comparison | BLUEPRINT Perusahaan |
| §5.5 | Retention & deletion (mekanisme teknis) | BLUEPRINT Project |
| §6.1–6.5 | Kapasitas issuance, reward mechanism, recirculation, burn, gap analysis | BLUEPRINT Project (mekanisme ekonomi) |
| State machine pembayaran + skema D1 (v4 §4.2–4.4, dipertahankan) | Kontrak transaksi Xendit | BLUEPRINT Project `[APPROVED BASELINE v4 §7.2]` |
| Skema D1 coin (v4 §5.5, dipertahankan) | Ledger & anti-fraud | BLUEPRINT Project |

## 10.3 Roadmap ← Bab 6, 8, 9

| Sumber v5 | Konten | Tujuan |
|---|---|---|
| §6.5 | Gap analysis kapasitas vs target + strategi penutupan | ROADMAP Project (perencanaan kapasitas) |
| §8.2.1 | Rencana 4 hari | ROADMAP Perusahaan (jangka pendek) |
| §8.2.2 | Fase 0–8 + release gates | ROADMAP Project |
| §8.2.3 | Product roadmap (AXION AI/Account/Ads/Coin) | ROADMAP Perusahaan |
| §8.3–8.4 | Review cadence & mekanisme revisi | ROADMAP Perusahaan |
| §9.1–9.4 | Risk register, matrix, mitigasi, review bulanan | ROADMAP Perusahaan + ROADMAP Project |

## 10.4 Traceability Matrix

### 10.4.1 Temuan audit → GAP → BAB v5

| Temuan Audit (43) | GAP | BAB v5 |
|---|---|---|
| Prinsip pembayaran 5/6 | GAP-01 | BAB 2 (§2.2) |
| Header tidak lengkap | GAP-02 | BAB 4 (§4.1) |
| Replay protection tidak ada | GAP-02 | BAB 4 + BAB 3 (§3.5) |
| Constant-time comparison | GAP-02 | BAB 4 (§4.6) |
| AI external policy tidak ada | GAP-03 | BAB 3 (§3.2) |
| Status DRAFT tapi mengikat | GAP-04 | BAB 1 (§1.2) |
| Privacy terlalu tipis | GAP-05 | BAB 5 |
| Kapasitas issuance tidak dihitung | GAP-06 | BAB 6 (§6.1, §6.5) |
| Carry-over tanpa Decision ID | GAP-07 | BAB 7 (§7.2.4, §6.1.2) |
| OKR tanpa baseline | GAP-08 | BAB 8 |
| Risk register tidak ada | GAP-09 | BAB 9 |
| SLA webhook tidak terukur | GAP-10 | BAB 4 (§4.4–4.5) |

### 10.4.2 Verifikasi Exit Criteria (status: inspeksi DRAFT — pengesahan menunggu approval Owner)

| EC | Kriteria | Lokasi | Status draft |
|---|---|---|---|
| EC-01 | 6 prinsip pembayaran canonical + LOCKED | §2.0, §2.2 | ✅ Tercantum |
| EC-02 | Tabel header lengkap | §4.1 | ✅ Tercantum |
| EC-03 | Replay protection (timestamp wajib, window ≤ 5 menit, nonce) | §3.5.1 | ✅ Tercantum |
| EC-04 | HMAC signature jalur finansial | §3.5.2 | ✅ Tercantum |
| EC-05 | Threat model ≥ 5 kategori + AI policy | §3.1–3.2 | ✅ Tercantum (7 kategori) |
| EC-06 | Lifecycle + daya ikat per status | §1.2 | ✅ Tercantum |
| EC-07 | Klasifikasi 4 tier + handling | §3.3 | ✅ Tercantum |
| EC-08 | Privacy + UU PDP | BAB 5 | ✅ Tercantum |
| EC-09 | Economic constraints + gap analysis | §6.1, §6.5 | ✅ Tercantum |
| EC-10 | Decision Authority Matrix + ID system | BAB 7 | ✅ Tercantum |
| EC-11 | OKR baseline + status label | BAB 8 | ✅ Tercantum |
| EC-12 | Risk register + ≥ 5 risiko | BAB 9 | ✅ Tercantum (7 risiko) |
| EC-13 | Integration SLA | §4.4–4.5 | ✅ Tercantum |

**Blocking: 7/7 tercantum. High Priority: 6/6 tercantum** (syarat minimal 5/6 terpenuhi). Status dokumen: **APPROVED** per **OD-2026-003** (2026-09-12).

---

## STATUS DOKUMEN & LANGKAH BERIKUTNYA

1. Dokumen ini adalah versi final tunggal Rencana Arsitektur AXION Neuralis v5, mencakup BAB 1–10, hasil penggabungan draft.1 (BAB 1–5) + draft.2 (BAB 6–10) + draft.3 (lapisan integrasi keputusan) sesuai rekomendasi reviewer #1.
2. **Status: APPROVED** per **OD-2026-003** (2026-09-12). Berlaku mengikat seluruh tim (§1.2) sejak tanggal tersebut. APPROVED berarti spesifikasi ditetapkan sebagai acuan — bukan berarti implementasi/verifikasi selesai (§1.2.3).
3. **Keputusan yang TERTUTUP dan sudah diterapkan ke badan dokumen:**
   - Penunjukan peran Tech Lead / Security Lead / Ops Lead → Owner (AZRIEL) merangkap — **OD-2026-001** (§7.1)
   - Trigger klausul transisi peran: kandidat kredibel tersedia **DAN** SLA eskalasi terlampaui 2 review bulanan berturut-turut — **OD-2026-001 (Adendum)** (§7.1)
   - Carry-over budget issuance cap 20% / interpretasi `min(sisa_budget, 20.000.000 AXC)` — **OD-2026-002** (§6.1.2, §6.1.3, §6.4)
   - Koreksi tanggal efektif OD-2026-002 → 2026-09-06 — **OD-2026-002 (Adendum)**
4. **Item yang masih terbuka** — tidak tercakup dalam OD-2026-003, tetap menunggu Owner Decision terpisah (format `OD-2026-004` dst.) sebelum dikunci:
   - Rasio recirculation pool (§6.3.1)
   - Burn trigger & headroom (§6.3.2)
   - Target user untuk gap analysis (§6.5.1)
   - Skema scoring risiko (§9.2)
   - SLA eskalasi (§7.3.2)
   - Mekanisme distribusi carry-over ke monthly/daily (§6.1.2)
5. **Verification gate** sebelum implementasi (belum berubah status, tidak tercakup OD-2026-003): format signature webhook Xendit (§3.5.3), device fingerprint web wrapper (§3.5.4), status DPA Xendit (§5.4).
6. **Langkah berikutnya:** jalankan Fase 3 PROPOSAL-ARCH-UPGRADE-001 — turunkan arsitektur v5 ke 6 dokumen inti + register OWNER-DECISIONS sesuai BAB 10, dimulai dengan BIBLE; jadwalkan quarterly review pertama (§8.3).
7. Out of scope dokumen ini (mengikuti proposal APPROVED): detail implementasi kode, UI/UX, vendor selection, go-to-market, legal drafting detail, performance benchmark.
