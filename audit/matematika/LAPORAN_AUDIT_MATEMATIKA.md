# Laporan Audit Penuh — Matematika Kelas 1 MI (Fase A)

Bank: `matematika/mtk_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `0d1b51e095fe81f5…`). Versi hasil perbaikan: `audit/FINAL/matematika_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 835 | 905 |
| REVISE | 91 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 74 | 95 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 75 / 16 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 2} |

Keselarasan ATP: {'SELARAS_MESIN': 571, 'INDIKASI_TINJAU_BACA': 27, 'SELARAS_TINJAU_BACA': 401, 'INDIKASI_KUAT_DOKUMEN': 1} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'ATP_INDIKASI': 27, 'DUP_DIPERTAHANKAN': 63, 'KONSTRUKSI': 77, 'AKURASI_AHLI': 13, 'USIA_ISI': 24, 'BAHASA': 27, 'AMBIGU': 10, 'DISTRAKTOR_AMBIGU': 1, 'DUP_SUBSTANTIF': 18, 'AKURASI_KONFLIK_INTERNAL': 1, 'ATP_INDIKASI_KUAT': 1}.
Kunci opsi terpanjang pada bank asli: 335/497; benar/salah: {'Benar': 104, 'Salah': 98}; kesulitan: {'easy': 563, 'medium': 397, 'hard': 40}.

## 2. Temuan sistemik dan contoh
- 481 kunci hitung dihitung ulang: 0 kesalahan hitung.
- Soal sikap/nilai tanpa berhitung (B1-04, B2-04, B3-04, B5-04, B7-04) dengan pengecoh absurd.
- Konteks absurd akibat templat (topi dimakan, 10 kursi dibawa); 11 soal "kalah N kelereng" bernuansa taruhan (perlu ahli).
- Istilah "selisih" (hard) di luar ATP; genap/ganjil tidak ada di CP/ATP (MTK-B8-0072).
- Pasangan duplikat substantif (data sama, kata tanya dibalik): B5-0041.. 0063.

Contoh lain untuk ditinjau: MTK-B1-0133 (7 jeruk dibagi 3); MTK-B4-0021/0022/0009 (persegi termasuk persegi panjang).

## 3. Cakupan ATP
18 dari 30 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
95 baris pada `audit/matematika/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/matematika/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
