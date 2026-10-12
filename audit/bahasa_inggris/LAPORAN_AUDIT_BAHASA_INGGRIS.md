# Laporan Audit Penuh — Bahasa Inggris Kelas 1 MI (Fase A)

Bank: `bahasa_inggris/eng_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `69d4143d6ebe4e6e…`). Versi hasil perbaikan: `audit/FINAL/bahasa_inggris_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 696 | 863 |
| REVISE | 185 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 119 | 137 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 183 / 6 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 3} |

Keselarasan ATP: {'SELARAS_TINJAU_BACA': 205, 'SELARAS_MESIN': 788, 'INDIKASI_TINJAU_BACA': 7} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'DISTRAKTOR_AMBIGU': 12, 'AMBIGU': 45, 'ATP_INDIKASI': 7, 'KONSTRUKSI': 127, 'AKURASI_AHLI': 21, 'BAHASA': 73, 'DUP_DIPERTAHANKAN': 35, 'AKURASI_SALAH_TEGAS': 5, 'USIA_ISI': 31, 'AKURASI_KONFLIK_INTERNAL': 10, 'DUP_SUBSTANTIF': 5}.
Kunci opsi terpanjang pada bank asli: 239/485; benar/salah: {'Salah': 90, 'Benar': 90}; kesulitan: {'medium': 622, 'easy': 377, 'hard': 1}.

## 2. Temuan sistemik dan contoh
- Kunci salah dikoreksi: ENG-B2-0076 (an orange crayon); ENG-B3-0076 diusulkan "two".
- Soal "tersusun benar" (~55) dan anagram "susun huruf" (~55) membingungkan kelas 1 dan menuntut membaca/menulis padahal CP menekankan lisan; anagram sebagian tidak punya kunci unik.
- Terjemahan -ku vs -nya (ENG-B5-0098/0106/0107); garden vs yard (B5-0016/0025); brother "adik" vs "kakak laki-laki" (B5-0072/0079).
- Teks bacaan yang dirujuk tidak ada di bank (ENG-B1-0093..0098); dialog dikarang penyusun revisi dan perlu verifikasi.
- Good night/Good evening dan Goodbye/See you tumpang tindih sebagai kunci (ENG-B1-0078..0087, 0102, 0112).

Contoh lain untuk ditinjau: ENG-B4-0007/0017..0022 (relasi keluarga tak bisa dibedakan dari gambar); ENG "favorite" (ejaan Amerika) perlu keputusan.

## 3. Cakupan ATP
72 dari 72 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
130 baris pada `audit/bahasa_inggris/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/bahasa_inggris/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
