# Laporan Audit Penuh — Al-Quran Hadis Kelas 1 MI (Fase A)

Bank: `alquran_hadis/aqh_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `b9bf7a8e113d91f6…`). Versi hasil perbaikan: `audit/FINAL/alquran_hadis_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 871 | 917 |
| REVISE | 48 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 81 | 83 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 48 / 0 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 5} |

Keselarasan ATP: {'SELARAS_MESIN': 836, 'SELARAS_TINJAU_BACA': 153, 'INDIKASI_TINJAU_BACA': 11} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'USIA_ISI': 16, 'DUP_DIPERTAHANKAN': 32, 'AMBIGU': 12, 'DISTRAKTOR_AMBIGU': 5, 'AKURASI_AHLI': 33, 'BAHASA': 1, 'ATP_INDIKASI': 11, 'KONSTRUKSI': 2, 'AKURASI_SALAH_TEGAS': 1, 'DUP_SUBSTANTIF': 2}.
Kunci opsi terpanjang pada bank asli: 250/540; benar/salah: {'Benar': 104, 'Salah': 98}; kesulitan: {'medium': 553, 'easy': 284, 'hard': 163}.

## 2. Temuan sistemik dan contoh
- Penomoran ayat Al-Fatihah menghitung Basmalah sebagai ayat 1; perlu keputusan rujukan mushaf (AQH-FA-0042 dst).
- Terjemahan "Ath-thuhuru syathrul iman" menjadi "kebersihan sebagian dari iman" (AQH-HK-0057..0079) perlu ahli hadis.
- Soal arti kosakata Arab (ماء, باب) pada TP yang hanya menulis huruf hijaiah (AQH-HT-0042 dst).
- Soal urutan tanpa urutan baku (IK-0137, FL-0137, NS-0137, HT-0136, HK-0135).
- Satu kunci salah dikoreksi: AQH-HT-0111 (رجل: Jim di tengah kata → Benar).

Contoh lain untuk ditinjau: AQH-FA-0006/0026 (Basmalah memuat Ar-Rahman Ar-Rahim vs pengecoh); AQH-FL-0018~0025 (duplikat substantif).

## 3. Cakupan ATP
20 dari 28 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
84 baris pada `audit/alquran_hadis/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/alquran_hadis/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
