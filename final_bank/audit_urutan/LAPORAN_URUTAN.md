# Penyisiran urutan, ordinal, jumlah, dan ejaan pada Bank Final Lulus

Cakupan: 8.539 soal pada `bank_final_lulus.json`; 3.598 soal yang memuat urutan, ordinal, jumlah, atau enumerasi dibaca penuh oleh 15 agen AI (pembagian per mapel), ditambah pemindai deret otomatis (`scan_series.py`). Tidak ada soal yang diubah. Semua temuan di bawah adalah usulan; keputusan baku ada pada guru/ahli.

## 1. Kasus rukun Islam (yang Anda temukan)
- Urutan yang dipakai pada KUNCI, penjelasan, dan nomor ordinal di bank: **Syahadat, Salat, Zakat, Puasa, Haji** (zakat rukun ke-3, puasa ke-4). Urutan yang sama ada di KKTP Fikih di repositori. ATP tidak menetapkan urutannya.
- Urutan **Syahadat, Salat, Puasa, Zakat, Haji** (seperti yang Anda tulis) tampil pada: FIK-RI-0050 (disajikan sebagai urutan yang SALAH), FIK-RI-0090 (pengecoh), dan sebagai urutan tampilan di FIK-RI-0907 (kolom kiri cocokkan), FIK-RI-0059, FIK-RI-0044, FIK-RI-0049, serta FIK-RI-0043/0005 (kartu acak sebelum diurutkan).
- Jadi bank tidak konsisten pada tampilan, tetapi konsisten pada kunci. Yang perlu Anda putuskan: urutan baku di madrasah ini. Jika memilih puasa sebelum zakat, soal yang harus diubah (kunci, ordinal, penjelasan, pengecoh) terdaftar di `RUKUN_ISLAM_DAMPAK.csv` (19 ID). Saya tidak memutuskan karena ATP diam dan sumbernya (KKTP) berlawanan dengan urutan yang Anda sebut.

## 2. Temuan lain yang serupa (39 temuan, 217 ID terlibat; `TEMUAN_INKONSISTENSI.csv`)
Per jenis: ejaan 19, fakta lain 13, urutan 5, jumlah 2. Keyakinan: sedang 10, rendah 29. Yang paling relevan:
- **Urutan**: AQH-HK-0136 (judul "kegiatan sebelum makan" tetapi kunci memuat makan dan "alhamdulillah" sesudah makan; ini cacat nyata); FIK-RI-0249 (urutan persiapan salat: wudu, kiblat, niat, takbiratulihram, bergantung buku); niat wudu sebagai langkah pertama (FIK-WT-0030/0031/0150/0219) vs niat bersamaan membasuh wajah (FIK-WT-0053); "hal pertama" niat vs basmalah (FIK-TH-0198/0212 vs FIK-WT-0016/0139); urutan menyebut vs menanyakan nama (BAR-PK-0238 vs BAR-PK-0247/0100); urutan anggota keluarga (BAR-KL).
- **Jumlah**: jumlah langkah wudu berbeda menurut kerangka (5 langkah, 6 rukun, 5 anggota; FIK-WT-0030/0219/0123); jumlah kalimat tayibah 3 vs kalimat lain tampil sebagai opsi (AKA-TY).
- **Fakta yang berbeda antar soal**: batas tangan tayamum (sampai siku vs tanpa batas); menemukan air setelah tayamum (batal vs "sebaiknya wudu"; FIK-WT-0098 vs FIK-TH-0201/FIK-WT-0026); melompat (satu kaki) vs peragaan melompat dua kaki (PJK-TB-0008/0016/0059 vs 0064/0200); ucapan pembuka/penutup bercerita (BIN-B7); bacaan sebelum belajar (basmalah vs doa; AKA-TY vs AKA-AB); waktu menyikat gigi (AKA-SH); rumusan ajaran sila ke-2 dan ke-5 (PPN-B3).
- **Ejaan**: sunah/sunnah, Makkah/Mekah, hadis/hadits, Subuh/subuh, Taawuz/ta'awudz, yaumid-din/yaumiddin, syathrul/syathru, "sebagian/bagian dari iman", "Bu Guru/bu guru", kapitalisasi nama sila, klip/klip kertas, topi ulang tahun/topi pesta, "paling sedikit/tersedikit", "ke 114/ke-114".
- Pemindai otomatis tidak menambah temuan urutan baru pada deret yang dicek (rukun iman, sifat wajib, sila, waktu salat, surah) di luar yang dilaporkan agen; hasil pemindai mentah (`urutan_deret_kode.csv`) banyak positif palsu (mis. soal "urutkan" yang butirnya sengaja diacak) dan tidak dipakai sebagai temuan.

## 3. Metadata (temuan saya sendiri)
Label mata pelajaran di `bank_final_lulus.json` tidak seragam: soal lama memakai "Al-Qur'an Hadis" dan "Pendidikan Pancasila", soal baru memakai "Al-Quran Hadis" dan "Pancasila". Sudah diseragamkan ke nama lama pada `bank_final_lulus.json` dan `soal_baru_lolos.json` (hanya bidang `subject`; 132 soal baru). Dokumen DOCX tidak terpengaruh.

## 4. Keterbatasan
- Pemeriksaan semantik dilakukan model AI dari keluarga yang sama; temuan berkeyakinan rendah dan dasar "bergantung buku/mazhab" perlu keputusan guru/ahli.
- Hanya soal yang cocok dengan kata kunci (3.598 dari 8.539) yang dibaca; deret yang tidak tertulis eksplisit pada kata kunci bisa terlewat.
- Agen hanya melihat subset per mapel; konsistensi lintas mapel dibandingkan lewat daftar fakta baku (`FAKTA_BAKU_DIPAKAI.csv`) dan pencarian rukun Islam di seluruh bank.
- Kunci jawaban tidak diperiksa ulang pada tahap ini.
