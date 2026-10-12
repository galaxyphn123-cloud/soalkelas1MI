# Laporan Audit Penuh — PJOK Kelas 1 MI (Fase A)

Bank: `pjok/pjk_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `137d27911d6ca216…`). Versi hasil perbaikan: `audit/FINAL/pjok_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 450 | 706 |
| REVISE | 347 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 203 | 294 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 261 / 87 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 7} |

Keselarasan ATP: {'SELARAS_TINJAU_BACA': 221, 'SELARAS_MESIN': 763, 'INDIKASI_TINJAU_BACA': 16} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'AKURASI_KONFLIK_INTERNAL': 9, 'KONSTRUKSI': 333, 'AKURASI_AHLI': 51, 'DISTRAKTOR_AMBIGU': 44, 'AMBIGU': 74, 'BAHASA': 58, 'DUP_DIPERTAHANKAN': 31, 'USIA_ISI': 13, 'DUP_SUBSTANTIF': 12, 'ATP_INDIKASI': 16, 'AKURASI_SALAH_TEGAS': 3}.
Kunci opsi terpanjang pada bank asli: 192/416; benar/salah: {'Benar': 102, 'Salah': 98}; kesulitan: {'medium': 525, 'easy': 473, 'hard': 2}.

## 2. Temuan sistemik dan contoh
- Semua 100 tugas kinerja memakai rubrik generik; banyak yang sebenarnya lisan/gambar.
- Kunci keliru dikoreksi: PJK-MH-0038 (susu sumber protein), PJK-HA-0037 (olahraga membuat bugar), PJK-MH-0102 (kabel terkelupas: menjauh).
- "melompat" dipakai untuk gerak dua kaki, bertentangan dengan definisi bank (PJK-TB-0001, 0024, 0030..).
- Risiko keselamatan: menyundul bola, menahan bola dengan dada, berenang, simulasi orang asing (PJK-TB-0216.., MH-0131, HA-0061/0065).
- Soal pengurangan dalam 10 mengukur numerasi bukan gerak; TP BG-04 sama perilakunya dengan BG-02.

Contoh lain untuk ditinjau: PJK-MH-0083 (nomor darurat 112); PJK-HA-0072 vs HA-0082/0098/0117.

## 3. Cakupan ATP
3 dari 15 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
219 baris pada `audit/pjok/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/pjok/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
