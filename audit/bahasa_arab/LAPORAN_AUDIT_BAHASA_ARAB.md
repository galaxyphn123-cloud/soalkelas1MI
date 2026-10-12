# Laporan Audit Penuh — Bahasa Arab Kelas 1 MI (Fase A)

Bank: `bahasa_arab/bar_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `9c637a333d0f010f…`). Versi hasil perbaikan: `audit/FINAL/bahasa_arab_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 915 | 966 |
| REVISE | 51 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 34 | 34 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 51 / 0 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 1} |

Keselarasan ATP: {'SELARAS_MESIN': 580, 'SELARAS_TINJAU_BACA': 420} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'DISTRAKTOR_AMBIGU': 2, 'AMBIGU': 4, 'DUP_DIPERTAHANKAN': 88, 'BAHASA': 9, 'KONSTRUKSI': 25, 'USIA_ISI': 20, 'AKURASI_AHLI': 8}.
Kunci opsi terpanjang pada bank asli: 333/544; benar/salah: {'Benar': 100, 'Salah': 100}; kesulitan: {'medium': 632, 'easy': 258, 'hard': 110}.

## 2. Temuan sistemik dan contoh
- Arti طَاوِلَةٌ "meja makan" dan مَكْتَبٌ "meja belajar" (BAR-RM-0039.., BAR-SK-0014..) perlu ahli.
- Gambar "paman" tidak membedakan عَمٌّ dan خَالٌ (BAR-KL-0083..0089); diperbaiki dengan menyebut hubungan di stem.
- Templat "termasuk kata benda ...." mencampur kata kerja dan jamak; istilah mudzakkar/muannats/jamak abstrak untuk kelas 1 (25 soal).
- Kosakata CP seperti hobi, buah, warna, transportasi, alam belum punya soal; ATP hanya nama, keluarga, rumah, madrasah.
- Soal berurutan tanpa urutan tunggal (BAR-KL-0238, BAR-RM-0239, BAR-SK-0239).

Contoh lain untuk ditinjau: BAR-PK-0088 (pengecoh تِلْمِيْذٌ juga benar); BAR-PK-0210 (menjawab salam: dianjurkan vs wajib).

## 3. Cakupan ATP
8 dari 16 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
34 baris pada `audit/bahasa_arab/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/bahasa_arab/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
