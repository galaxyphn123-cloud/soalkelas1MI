# Bank Soal Kelas 1 MI (Fase A)

Bank soal digital 1.000 soal per mata pelajaran berdasarkan ATP (file ATP/KKTP ada di folder utama).

| # | Mapel | Status | Folder |
|---|-------|--------|--------|
| 1 | Fikih | **Selesai** (1.000 soal) | `fikih/` |
| 2 | Al-Qur'an Hadis | **Selesai** (1.000 soal) | `alquran_hadis/` |
| 3 | Bahasa Arab | **Selesai** (1.000 soal) | `bahasa_arab/` |
| 4 | Akidah Akhlak | **Selesai** (1.000 soal) | `akidah_akhlak/` |
| 5 | Bahasa Indonesia | **Selesai** (1.000 soal) | `bahasa_indonesia/` |
| 6 | Matematika | **Selesai** (1.000 soal) | `matematika/` |
| 7 | Pendidikan Pancasila | **Selesai** (1.000 soal) | `pancasila/` |
| 8 | PJOK | Belum | - |
| 9 | Bahasa Inggris | Belum | - |

Tiap mapel punya 4 berkas: bank soal, `*_blueprint.json`, `*_teacher_answer_key.json`, `*_qa_report.json`.

## Fikih
`fikih/fikih_bank_1000_FIXED_gabungan.json` adalah satu-satunya sumber yang dipakai (berkas per-materi lama
di `files (15).zip` sudah usang). Posisi kunci pilihan ganda sudah diseimbangkan ulang (A-D merata).
Temuan yang belum diperbaiki ada di `fikih_qa_report.json` (bagian `rekomendasi`): soal benar/salah ~80% "Benar",
dan kunci pilihan ganda cenderung opsi terpanjang.

## Al-Qur'an Hadis
7 materi x 4 TP = 28 TP (143 soal per materi, Hadis 142). Prefix ID `AQH-<kode>-NNNN`:
HJ (Huruf Hijaiah & Tanda Baca), FA (Al-Fatihah), IK (Al-Ikhlas), HT (Terpisah & Tersambung),
NS (An-Nas), FL (Al-Falaq), HK (Hadis Kebersihan).
Soal dibangkitkan dari tabel fakta + skenario tulisan tangan di `alquran_hadis/generator/`
(`python3 -I build_aqh.py ../aqh_bank_1000.json` lalu `python3 -I make_files.py ../aqh_bank_1000.json ..`).
Pengecekan duplikat lintas materi dilakukan saat pemilihan soal dan pada audit akhir.

## Bahasa Arab
4 materi x 4 TP = 16 TP (250 soal per materi, semua 14 JP). Prefix ID `BAR-<kode>-NNNN`:
PK (Perkenalan), KL (Keluargaku), RM (Rumahku), SK (Sekolahku). Kosakata dan pola kalimat dibatasi pada ATP.
Pembangkit di `bahasa_arab/generator/` (`python3 -I build_bar.py ../bar_bank_1000.json`, lalu `python3 -I make_files.py ../bar_bank_1000.json ..`).

## Akidah Akhlak
7 materi, 26 TP. Soal dibagi sebanding alokasi JP (total 58 JP): Syahadat 104, Kalimat Tayibah 103, Pola Hidup Sehat 155,
Adab Belajar 207, Kisah Nabi Muhammad 155, Rukun Iman 207, Sifat Wajib Allah 69. Prefix ID `AKA-<kode>-NNNN`
(SY, TY, SH, AB, KN, RI, SW). Pembangkit di `akidah_akhlak/generator/`
(`python3 -I build_aka.py ../aka_bank_1000.json`, lalu `python3 -I make_files.py ../aka_bank_1000.json ..`).
Teks soal tidak kembar di dalam mapel maupun terhadap Fikih, Al-Qur'an Hadis, dan Bahasa Arab.

## Bahasa Indonesia
8 bab, 36 TP (ILMA). ATP tidak merinci JP per bab, jadi soal dibagi sebanding jumlah TP: bab 4 TP = 111 soal, bab 5 TP = 139 soal.
Prefix ID `BIN-B<n>-NNNN`. Pembangkit di `bahasa_indonesia/generator/`
(`python3 -I build_bin.py ../bin_bank_1000.json`, lalu `python3 -I make_files.py ../bin_bank_1000.json ..`).

## Matematika
8 bab, 30 TP (ILMA). Soal dibagi sebanding jumlah TP: bab 4 TP = 133/134 soal, bab 3 TP (Mengenal Bentuk, Data) = 100 soal.
Prefix ID `MTK-B<n>-NNNN`. Kunci soal hitung (penjumlahan, pengurangan, perbandingan, nilai tempat, data) dihitung oleh program.
Pembangkit di `matematika/generator/` (`python3 -I build_mtk.py ../mtk_bank_1000.json`, lalu `python3 -I make_files.py ../mtk_bank_1000.json ..`).

## Pendidikan Pancasila
4 bab, 14 TP (ILMA). Soal dibagi sebanding jumlah TP: Bab 1 dan 2 (3 TP) = 214 soal, Bab 3 dan 4 (4 TP) = 286 soal.
Prefix ID `PPN-B<n>-NNNN`. Pembangkit di `pancasila/generator/`
(`python3 -I build_ppn.py ../ppn_bank_1000.json`, lalu `python3 -I make_files.py ../ppn_bank_1000.json ..`).
