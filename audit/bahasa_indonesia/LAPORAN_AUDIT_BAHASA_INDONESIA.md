# Laporan Audit Penuh — Bahasa Indonesia Kelas 1 MI (Fase A)

Bank: `bahasa_indonesia/bin_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `6367389c74ba5806…`). Versi hasil perbaikan: `audit/FINAL/bahasa_indonesia_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 634 | 870 |
| REVISE | 242 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 124 | 130 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 239 / 3 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 10} |

Keselarasan ATP: {'SELARAS_TINJAU_BACA': 72, 'INDIKASI_TINJAU_BACA': 77, 'SELARAS_MESIN': 851} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'ATP_INDIKASI': 77, 'KONSTRUKSI': 211, 'DUP_DIPERTAHANKAN': 66, 'BAHASA': 8, 'AMBIGU': 21, 'USIA_ISI': 15, 'AKURASI_AHLI': 15, 'DISTRAKTOR_AMBIGU': 5}.
Kunci opsi terpanjang pada bank asli: 322/510; benar/salah: {'Benar': 100, 'Salah': 100}; kesulitan: {'easy': 508, 'medium': 492}.

## 2. Temuan sistemik dan contoh
- 211 soal merujuk cerita tetapi teks ceritanya tidak dimuat; teks asli ada di sumber pembangkit dan sudah dimuat pada revisi (soal menjadi lebih panjang, beban baca meningkat).
- Soal suku kata, kebiasaan sehat, dan sikap belajar lebih dekat ke ATP yang tidak tercantum pada TP bank (BIN: 77 ATP_INDIKASI).
- Soal "urutan" memakai teks yang urutannya tak bermakna (BIN-B3-0122, B4-0024, B6-0030).
- Ejaan "qurban" (baku "kurban") perlu keputusan (BIN-B5-0060, 0077, 0084).
- Isian terbuka dengan banyak jawaban sah.

Contoh lain untuk ditinjau: BIN-B1-0056 ("t_s": tas/tes); BIN-B5-0121/0134 (maaf vs permisi); BIN-B7-0046/0059 (tekun vs rajin).

## 3. Cakupan ATP
22 dari 32 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
133 baris pada `audit/bahasa_indonesia/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/bahasa_indonesia/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
