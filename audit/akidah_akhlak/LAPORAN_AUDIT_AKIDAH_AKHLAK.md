# Laporan Audit Penuh — Akidah Akhlak Kelas 1 MI (Fase A)

Bank: `akidah_akhlak/aka_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `be3ac8a0eb75387e…`). Versi hasil perbaikan: `audit/FINAL/akidah_akhlak_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 770 | 891 |
| REVISE | 132 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 98 | 109 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 122 / 10 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 11} |

Keselarasan ATP: {'SELARAS_MESIN': 773, 'SELARAS_TINJAU_BACA': 198, 'INDIKASI_TINJAU_BACA': 29} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'USIA_ISI': 39, 'KONSTRUKSI': 20, 'ATP_INDIKASI': 29, 'AMBIGU': 7, 'BAHASA': 9, 'AKURASI_AHLI': 24, 'DISTRAKTOR_AMBIGU': 2, 'AKURASI_KONFLIK_INTERNAL': 6, 'DUP_DIPERTAHANKAN': 2}.
Kunci opsi terpanjang pada bank asli: 237/380; benar/salah: {'Benar': 117, 'Salah': 114}; kesulitan: {'medium': 606, 'hard': 50, 'easy': 344}.

## 2. Temuan sistemik dan contoh
- Konflik kunci: AKA-SW-0020/0031 "tanpa diciptakan = Wujud" vs AKA-SW-0057 "Qidam"; Al-Amin "jujur" vs "amanah" (AKA-KN-0042/0055/0069).
- Benar/salah masih berisi titik-titik (AKA-RI-0091/0093, AKA-SH-0052).
- Raqib/Atid, rumusan iman, "pasti azab neraka" perlu ahli.
- Sifat rasul (siddiq, amanah, tablig, fatanah) tidak ada di CP/ATP (AKA-KN-0040, 0046..0073).
- CP memuat asmaulhusna, malaikat, kisah Nabi Nuh tanpa TP; Nuh dan asmaulhusna hampir tidak muncul.

Contoh lain untuk ditinjau: AKA-SH-0004 (PHBS "disingkat"); AKA-TY-0076 (opsi tidak sejajar, kunci terpanjang).

## 3. Cakupan ATP
17 dari 26 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
107 baris pada `audit/akidah_akhlak/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/akidah_akhlak/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
