# Laporan Audit Penuh — Fikih Kelas 1 MI (Fase A)

Tanggal: 2026-10-12 · Berkas bank: `fikih/fikih_bank_1000_FIXED_gabungan.json` (tidak diubah; hash SHA-256 sebelum dan sesudah audit sama)

## 1. Ringkasan
| Ukuran | Jumlah |
|---|---|
| Soal awal | 1000 |
| Soal diperiksa | 1000 (seluruh ID, dari FIK-RI-0001 sampai FIK-WT-0266) |
| PASS (layak tanpa perubahan substantif) | 569 |
| REVISE (perbaikan teridentifikasi) | 266 |
| NEEDS_REVIEW (menunggu guru/ahli; **tidak boleh diubah**) | 165 |
| REJECT | 0 (mesin tidak menolak soal; hanya ahli yang dapat) |
| Duplikat identik / kandidat duplikat substantif | 0 / 0 |
| TP tanpa pemetaan ke ATP | 0 (15 dari 15 TP tertelusur ke teks ATP) |

## 2. Metode dan batasnya
1. **Mesin audit** (`audit/audit_engine.py`, `audit/audit_full.py`): pemeriksaan struktur kunci, duplikasi, beban baca, keselarasan kata kunci terhadap TP/materi/kompetensi, serta pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan berbukti.
2. **Tinjau baca**: seluruh 1.000 soal Fikih dibaca satu per satu oleh model AI (bukan guru/ahli); hanya pengecualian yang dicatat (`fikih/manual_review.json`). Ini mengurangi, tetapi tidak menggantikan, tinjauan ahli fikih dan guru kelas 1.
3. **Yang belum bisa diverifikasi**: kebenaran fakta fikih per mazhab, kesesuaian usia secara pedagogis, dan kualitas pengecoh secara menyeluruh; semua ada pada antrean ahli.
4. **Pemetaan KBC/PM/Profil** adalah usulan berbukti (kata kunci pada kunci/penjelasan dan TP; rujukan: KMA 1503/2025, Panduan KBC Tabel 1, PDF Pembelajaran Mendalam, dokumen Dimensi Kompetensi Profil Lulusan SD/MI). Pemetaan final perlu guru/ahli.

## 3. Temuan utama
| Temuan | Jumlah soal | Status | Contoh ID |
|---|---|---|---|
| Kunci jawaban opsi terpanjang menonjol (≥1,5× opsi kedua terpanjang) | 260 | REVISE jika tidak ada temuan ahli | lihat CSV |
| Isian bertipe `fill_in_short`/`completion` tetapi jawabannya terbuka ("Contoh jawaban: …") | 46 | REVISE (metadata tipe + rubrik) | FIK-RI-0024, FIK-RI-0037 |
| Kunci pengelompokan rusak (nilai kelompok berupa deretan huruf) | 1 | REVISE | FIK-RI-0026 |
| Topik di luar atau di tepi ATP (terindikasi) | 85 | NEEDS_REVIEW | salat/azan/rakaat (CP memuat, TP tidak), hari raya/kurban, kebersihan hati, tata bahasa Arab |
| Topik dengan bukti dokumen kuat di luar ATP/CP | 3 | NEEDS_REVIEW | FIK-RI-0227, FIK-RI-0250, FIK-RI-0258 |
| Perlu keputusan ahli tentang kebenaran (mazhab/khilafiah/kaitan konsep) | 33 | NEEDS_REVIEW | FIK-RI-0066, FIK-TH-0021, FIK-WT-0120 |
| Kunci saling bertentangan di dalam bank | 3 | NEEDS_REVIEW | FIK-WT-0048, FIK-WT-0216, FIK-WT-0205 |
| Materi/istilah terlalu rinci untuk kelas 1 | 54 | NEEDS_REVIEW | tingkatan najis, nisab, rukun tayamum |
| Jawaban ganda/ambigu | 5 | NEEDS_REVIEW | FIK-WT-0164, FIK-TH-0025 |
| Stem negatif; soal pengelompokan yang membocorkan jawaban | 3 / 1 | REVISE | FIK-RI-0265, FIK-RI-0258 |

Pola tingkat bank: jawaban benar/salah condong "Benar" (168 Benar : 42 Salah), kunci opsi terpanjang 402/517, soal sulit 163 (16%) dan mudah hanya 115.
Nomor ID: `FIK-RI-0126` tidak ada (bank tetap 1.000 soal); perlu dikonfirmasi apakah soal itu dipindah.

### Contoh soal yang perlu ditinjau
**Ketidakcocokan terindikasi dengan ATP (dibedakan dari yang terbukti dokumen)**
  - `FIK-RI-0227` (matching) — Cocokkan nama bulan Hijriah dengan peristiwa penting di dalamnya! → kunci: (lihat bank)
    - Catatan: Bulan Hijriah dan urutan bulan: istilah 'Hijriah'/nama bulan tidak ada pada teks CP maupun ATP Fikih; terkait hanya secara tidak langsung melalui puasa Ramadan dan haji.
  - `FIK-RI-0250` (ordering) — Urutkan tiga bulan Hijriah berikut sesuai kejadian dalam setahun: Syawal, Ramadan, Zulhijah. → kunci: (lihat bank)
    - Catatan: Bulan Hijriah dan urutan bulan: istilah 'Hijriah'/nama bulan tidak ada pada teks CP maupun ATP Fikih; terkait hanya secara tidak langsung melalui puasa Ramadan dan haji.
  - `FIK-RI-0147` (multiple_choice) — Salat yang dikerjakan saat matahari terbit disebut .... → kunci: D. Subuh
    - Catatan: Waktu salat dan jumlah rakaat: CP memuat salat fardu, tetapi ATP Fikih tidak punya TP/materi salat; TP RI-01 hanya 'menyebutkan lima rukun Islam'.
  - `FIK-RI-0192` (multiple_choice) — Mengapa azan dikumandangkan sebelum salat? → kunci: B. Sebagai tanda masuknya waktu salat dan panggilan untuk beribadah
    - Catatan: Azan/muazin/imam-makmum: CP memuat 'melafalkan azan dan ikamah' dan salat berjemaah, tetapi ATP tidak memiliki TP/materi azan atau salat berjemaah.
  - `FIK-TH-0186` (true_false) — Benar atau salah: Taharah mencakup kebersihan badan, pakaian, tempat, dan juga hati. → kunci: Benar
    - Catatan: Kebersihan hati (iri, dengki) adalah topik akhlak/tasawuf, bukan bersuci dari hadas dan najis pada TP taharah; selaras dengan nilai KBC tetapi perlu keputusan ahli.

**Akurasi/konflik kunci**
  - `FIK-WT-0048` (multiple_choice) — Tayamum dilakukan dengan menepukkan tangan ke debu sebanyak .... → kunci: A. Satu kali
    - Catatan: WT-0205 menyatakan tangan 'ditepukkan lagi ke debu' sebelum mengusap tangan (dua tepukan), sedangkan WT-0048 dan WT-0216 menetapkan tepukan 'satu kali'. Kunci saling bertentangan dalam bank yang sama.
  - `FIK-WT-0205` (multiple_choice) — Setelah mengusap wajah dalam tayamum, tangan perlu .... → kunci: A. Ditepukkan lagi ke debu untuk mengusap kedua tangan
    - Catatan: WT-0205 menyatakan tangan 'ditepukkan lagi ke debu' sebelum mengusap tangan (dua tepukan), sedangkan WT-0048 dan WT-0216 menetapkan tepukan 'satu kali'. Kunci saling bertentangan dalam bank yang sama.
  - `FIK-RI-0066` (contextual) — Rina selalu mengucapkan syahadat dengan sungguh-sungguh setiap kali membaca doa sebelum tidur. Sikap Rina mencerminkan pengamalan rukun Islam yang ke .... → kunci: A. Satu
    - Catatan: Syahadat dikaitkan dengan 'membaca doa sebelum tidur'; doa tidur bukan syahadat sehingga kaitan ke rukun Islam ke-1 meragukan.
  - `FIK-TH-0021` (multiple_choice) — Jika seseorang salat dalam keadaan pakaiannya terkena najis tanpa disadari, maka .... → kunci: C. Salatnya perlu diulang setelah pakaian dibersihkan dari najis
    - Catatan: Salat dengan pakaian bernajis tanpa disadari 'perlu diulang' adalah masalah khilafiah antar mazhab; perlu ahli.

**Ambigu / konstruksi**
  - `FIK-WT-0164` (multiple_choice) — Wudu dan tayamum sama-sama bertujuan untuk .... → kunci: C. Bersuci dari hadas kecil
    - Catatan: Kunci 'hadas kecil' untuk tujuan wudu dan tayamum bertentangan dengan WT-0165 (tayamum juga pengganti mandi wajib/hadas besar); opsi A (hadas besar) tidak sepenuhnya salah.
  - `FIK-RI-0258` (grouping) — Kelompokkan hari raya berikut sesuai bulan pelaksanaannya: 'Idulfitri di bulan Syawal', 'Iduladha di bulan Zulhijah' — masukkan ke kelompok yang sesuai: Syawal, Zulhijah. → kunci: (lihat bank)
    - Catatan: Soal mengelompokkan sudah memuat jawaban pada butir ('Idulfitri di bulan Syawal'); tugas menjadi trivial.

**Tentang pembedaan "terbukti" dan "terindikasi"**: mesin hanya dapat menunjukkan bukti dokumen berupa ketiadaan istilah pada teks ATP/CP atau kemiripan lebih tinggi ke TP lain. Karena itu tidak ada soal yang saya nyatakan *terbukti* tidak selaras; 3 soal berstatus `INDIKASI_KUAT_DOKUMEN` (istilah "Hijriah"/nama bulan tidak ada di CP maupun ATP), 85 berstatus `INDIKASI_TINJAU_BACA`, dan 278 soal yang ditandai mesin karena beda kata kunci dinyatakan `SELARAS_TINJAU_BACA` setelah dibaca. Keputusan akhir ada pada guru/ahli.

## 4. Cakupan ATP per TP
| TP | Soal | PASS | REVISE | NEEDS_REVIEW | Catatan |
|---|---|---|---|---|---|
| TP-FIK-RI-01 | 77 | 49 | 0 | 28 | — |
| TP-FIK-RI-02 | 81 | 43 | 15 | 23 | — |
| TP-FIK-RI-03 | 46 | 8 | 25 | 13 | jawaban benar/salah condong ({'Salah': 1}) |
| TP-FIK-RI-04 | 63 | 33 | 10 | 20 | jawaban benar/salah condong ({'Benar': 5, 'Salah': 2}) |
| TP-FIK-KS-01 | 50 | 33 | 13 | 4 | — |
| TP-FIK-KS-02 | 50 | 41 | 3 | 6 | jawaban benar/salah condong ({'Benar': 9}) |
| TP-FIK-KS-03 | 50 | 17 | 29 | 4 | — |
| TP-FIK-KS-04 | 50 | 27 | 22 | 1 | jawaban benar/salah condong ({'Benar': 11, 'Salah': 2}) |
| TP-FIK-TH-01 | 67 | 47 | 9 | 11 | — |
| TP-FIK-TH-02 | 66 | 33 | 12 | 21 | jawaban benar/salah condong ({'Benar': 13, 'Salah': 4}) |
| TP-FIK-TH-03 | 66 | 23 | 32 | 11 | jawaban benar/salah condong ({'Benar': 11, 'Salah': 2}) |
| TP-FIK-TH-04 | 68 | 38 | 30 | 0 | jawaban benar/salah condong ({'Benar': 21}) |
| TP-FIK-WT-01 | 89 | 59 | 17 | 13 | jawaban benar/salah condong ({'Benar': 20, 'Salah': 6}) |
| TP-FIK-WT-02 | 89 | 59 | 22 | 8 | jawaban benar/salah condong ({'Benar': 19, 'Salah': 4}) |
| TP-FIK-WT-03 | 88 | 59 | 27 | 2 | jawaban benar/salah condong ({'Benar': 26, 'Salah': 1}) |

Catatan cakupan: TP berverba praktik (RI-04, KS-04, TH-04, WT-03) paling cocok dinilai lewat praktik/observasi guru; soal tertulis hanya menguji pengetahuan atau penilaian sikap. Benar/salah cenderung "Benar" pada hampir semua TP. CP memuat salat fardu, salat berjemaah, azan/ikamah, dan zikir sesudah salat, tetapi ATP hanya punya empat materi (Rukun Islam, Kalimah Syahadatain, Taharah, Wudu dan Tayamum); ± 85 soal tentang salat/azan berada di celah ini dan perlu keputusan kurikulum.

## 5. Sebaran pemetaan (usulan berbukti; jumlah label ≠ jumlah soal)
- **KBC (relevansi langsung, bukti pada kunci/penjelasan dan TP)**: {"Cinta Allah dan Rasul-Nya": 261, "Cinta Diri dan Sesama": 52, "Cinta Lingkungan": 34}. Latar saja (tidak dihitung bukti): {"Cinta Allah dan Rasul-Nya": 214, "Cinta Ilmu": 164, "Cinta Diri dan Sesama": 256, "Cinta Tanah Air": 2, "Cinta Lingkungan": 13}.
- **Pembelajaran Mendalam (pengalaman belajar)**: {"Memahami": 811, "Mengaplikasi": 189, "Merefleksi": 4}; prinsip: {"Menggembirakan": 65, "Bermakna": 69, "Berkesadaran": 4}. Praktik pedagogis, kemitraan, lingkungan belajar, dan pemanfaatan digital tidak dapat diukur oleh soal tertulis; perlu aktivitas pendamping guru.
- **Profil Lulusan (langsung)**: {"Keimanan dan Ketakwaan terhadap Tuhan YME / Hubungan dengan Tuhan YME": 361, "Penalaran Kritis / Penyelesaian Masalah": 76, "Komunikasi / Berbicara": 12, "Kewargaan / Kewargaan Lokal": 4, "Kewargaan / perlu ditetapkan guru": 22}. Kolaborasi, kemandirian, kreativitas, dan kesehatan hampir tidak terukur oleh soal tertulis Fikih; sarankan observasi/rubrik/proyek guru.

## 6. Verifikasi konsistensi mesin (sebelum lanjut ke mapel lain)
- Kelengkapan: 1000 dari 1000 ID diproses, ID unik dan urutan sama dengan bank; jumlah status = 1000.
- Bank asli tidak berubah (hash sama): True.
- Deterministik (dua kali jalan, hasil identik): True.
- Implementasi independen pemeriksaan struktur cocok dengan mesin: True ({'kunci_terpanjang_menonjol': 260, 'isian_terbuka': 46, 'grouping_tak_valid': 1}).
- Validasi silang ATP dengan metode berbeda (kemiripan n-gram karakter): {"catatan": "persentase soal yang TP-nya berada di luar 3 teratas menurut kemiripan n-gram karakter (metode independen dari kata kunci)", "SELARAS_MESIN": [634, 0.224, 2.53], "SELARAS_TINJAU_BACA": [278, 0.745, 7.54], "INDIKASI_TINJAU_BACA": [85, 0.506, 5.05], "INDIKASI_KUAT_DOKUMEN": [3, 0.333, 6.67], "format": "(jumlah, proporsi rank>3, rata-rata rank)"}. Soal yang ditandai mesin tetapi dinyatakan selaras oleh bacaan memang lebih jauh secara leksikal (rank>3 pada 74%), sehingga penyaring kata kunci menghasilkan banyak positif palsu — itu sebabnya tinjau baca dipakai untuk menyelesaikan tanda mesin.
- Mesin vs tinjau baca: dari 88 soal ATP-terindikasi hasil bacaan, mesin menandai 60 (68%) dan melewatkan 28 (topik menyimpang tetapi masih berbagi kata dengan TP). Artinya mesin saja tidak cukup untuk keselarasan ATP; mapel berikutnya juga membutuhkan tinjau baca.
- Celah nomor ID: {'FIK-RI': [126]}.

## 7. Tindakan lanjutan (belum dilakukan; menunggu persetujuan urutan pelaksanaan)
- **REVISE (266)**: perbaiki panjang opsi/kualitas pengecoh (260 soal kecuali yang menunggu ahli), tandai ulang tipe untuk 46 isian terbuka, perbaiki kunci `FIK-RI-0026`, ubah dua stem (negatif/bocor). Tidak menambah pesan moral.
- **NEEDS_REVIEW (165)**: tidak diubah; antrean di `fikih/ANTRIAN_VERIFIKASI_AHLI.csv` (183 baris, dikelompokkan menurut peninjau).
- Koreksi `sumber_atp` pada blueprint (lima mapel) dilakukan pada tahap revisi lintas mapel.

Berkas keluaran (`audit/fikih/`): `QUESTION_AUDIT_DETAIL.csv/.json`, `ATP_COVERAGE_MATRIX.csv/.json`, `KBC_DEEP_LEARNING_PROFILE_MATRIX.json`, `DUPLICATION_REPORT.csv`, `ANTRIAN_VERIFIKASI_AHLI.csv`, `manual_review.json`, `AUDIT_SUMMARY.json`, `CONSISTENCY_CHECK.json`, `progress.json`.
