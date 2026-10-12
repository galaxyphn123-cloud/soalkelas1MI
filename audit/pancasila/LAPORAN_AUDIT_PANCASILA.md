# Laporan Audit Penuh — Pancasila Kelas 1 MI (Fase A)

Bank: `pancasila/ppn_bank_1000.json` (1000 soal; tidak diubah, hash SHA-256 `61f4bceba748b23d…`). Versi hasil perbaikan: `audit/FINAL/pancasila_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | 1000 | 1000 |
| PASS | 573 | 750 |
| REVISE | 239 | 0 |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | 188 | 250 |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | 179 / 62 |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {'petunjuk_kunci_terpanjang': 7} |

Keselarasan ATP: {'SELARAS_TINJAU_BACA': 182, 'SELARAS_MESIN': 768, 'INDIKASI_TINJAU_BACA': 50} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {'ATP_INDIKASI': 50, 'DISTRAKTOR_AMBIGU': 36, 'BAHASA': 76, 'KONSTRUKSI': 157, 'AMBIGU': 41, 'AKURASI_AHLI': 25, 'USIA_ISI': 42, 'DUP_DIPERTAHANKAN': 10, 'DUP_SUBSTANTIF': 4, 'AKURASI_KONFLIK_INTERNAL': 9, 'AKURASI_SALAH_TEGAS': 1}.
Kunci opsi terpanjang pada bank asli: 209/370; benar/salah: {'Benar': 155, 'Salah': 153}; kesulitan: {'easy': 543, 'medium': 451, 'hard': 6}.

## 2. Temuan sistemik dan contoh
- Satu sikap bisa masuk lebih dari satu sila (PPN-B3-0092, 0120, 0145, 0166..), sila 2 dan 5 tumpang tindih (B3-0093, 0105).
- Konflik kunci "menanam pohon bersama": PPN-B4-0115 Salah vs B4-0001/0024/0078/0130; selokan: B4-0091/0134/0153 vs 0081/0103/0148-0150.
- Fakta budaya daerah (rumah adat, tari, alat musik, makanan) tidak ada di CP/ATP; hanya terkait longgar dengan TP-B1-02.
- Mengucapkan selamat hari raya agama lain khilafiah (B1-0167, 0175, 0206); klenteng dikunci Konghucu (B1-0093, 0114, 0143).
- Stem negatif "tidak menaati ..." puluhan kali; blok benar/salah berkunci seragam.

Contoh lain untuk ditinjau: PPN-B1-0134 (eksklusif "yang beragama Islam menyebut Tuhan Allah"); PPN-B4-0163/0207 (hadis kebersihan).

## 3. Cakupan ATP
8 dari 14 TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
205 baris pada `audit/pancasila/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/pancasila/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
