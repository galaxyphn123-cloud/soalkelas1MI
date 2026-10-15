# ATP COVERAGE GAP REPORT — MI Darul Arifin, Kelas 1 (9 mata pelajaran)

Disusun 15 Oktober 2026. Audit keterwakilan saja: tidak ada soal yang dibuat, diperbaiki, atau diubah; kunci, TP, kompetensi, dan ID tidak disentuh. Seluruh penilaian hubungan soal–TP adalah **penilaian model AI**, bukan keputusan guru, ahli materi, atau kurikulum.

## 1. Jawaban singkat

| Pertanyaan | Jawaban |
|---|---|
| Apakah semua TP punya soal PASS? | **Tidak.** Dari 252 TP asli di ATP, 1 TP (BAH-ATP-093, Bahasa Indonesia Bab 2) tidak punya soal PASS sama sekali, karena TP itu ada di ATP tetapi tidak di bank. 251 TP punya paling sedikit satu soal PASS yang terkait. |
| Apakah semua materi terwakili? | **Ya, 55 dari 55 materi** punya minimal satu soal PASS DIRECT. Hanya 3 materi yang semua TP-nya COVERED (Akidah: Rukun Iman; Matematika: Bab 8 Data; PJOK: Memilih Hidup yang Menyehatkan). |
| Tercakup penuh / sebagian / belum / perlu pemetaan? | **COVERED 126 · PARTIALLY_COVERED 108 · NO_VERIFIED_COVERAGE 15 · MAPPING_REVIEW_REQUIRED 3** (total 252). |
| Materi yang belum terwakili | Tidak ada. Tetapi ada TP dalam materi yang terwakili yang belum punya bukti langsung (daftar di §4). |
| Mapel dengan kesenjangan terbesar | Persentase TP COVERED terendah: **PJOK 20.0%**, **Bahasa Indonesia 22.2%**, **Bahasa Inggris 44.4%**. Jumlah TP tanpa bukti langsung terbanyak: Bahasa Inggris (8), Bahasa Indonesia (3 + 3 perlu tinjauan pemetaan). |
| Tindakan paling efisien | Jangan menambah soal secara merata. Lihat §5: sebagian besar kesenjangan ada pada TP praktik, lisan, dan sikap yang tidak dapat dibuktikan soal tertulis. |

## 2. Dasar analisis
- Himpunan soal: **7.698 ID unik berstatus PASS** pada audit akhir (`QUESTION_AUDIT_DETAIL.csv`). Tidak ada yang beririsan dengan 1.302 ID NEEDS_REVIEW (diperiksa terhadap `AI_VERIFICATION_RESULTS.csv`). PASS bukan berarti AI_VERIFIED, persetujuan ahli, atau siap rilis.
- Registry TP: **252 TP asli** dibaca langsung dari dokumen ATP 9 mapel (7 berkas .docx, 1 .pdf PJOK, 9 berkas .rtf Bahasa Inggris dalam RAR). 248 cocok dengan TP bank; 4 TP ATP Bahasa Indonesia tidak punya padanan di bank.
- Hubungan soal–TP: DIRECT 4.041 · PARTIAL 3.293 · CONTEXT_ONLY 361 · UNMAPPED 3 (tiap soal dihitung sekali sebagai tautan utama).
- Aturan status: COVERED = ada soal DIRECT yang mengukur seluruh tuntutan inti TP; PARTIALLY_COVERED = ada DIRECT tetapi sebagian tuntutan hanya terbukti sebagian; NO_VERIFIED_COVERAGE = tidak ada soal DIRECT (hanya PARTIAL/konteks atau tidak ada); MAPPING_REVIEW_REQUIRED = bukti DIRECT hanya dari soal yang dipindahkan penilai AI dari TP lain dan perlu keputusan kurikulum. Jumlah soal tidak dipakai sebagai ukuran kecukupan.

## 3. Rekap per mata pelajaran
| Mapel | TP | COVERED | Sebagian | Tanpa bukti langsung | Tinjau pemetaan | TP dengan DIRECT <3 | Soal PASS | DIRECT |
|---|---|---|---|---|---|---|---|---|
| Fikih | 15 | 10 | 5 | 0 | 0 | 0 | 830 | 396 |
| Al-Quran Hadis | 28 | 18 | 10 | 0 | 0 | 2 | 917 | 522 |
| Bahasa Arab | 16 | 8 | 7 | 1 | 0 | 4 | 966 | 611 |
| Akidah Akhlak | 26 | 16 | 8 | 2 | 0 | 7 | 891 | 441 |
| Bahasa Indonesia | 36 | 8 | 22 | 3 | 3 | 18 | 870 | 313 |
| Matematika | 30 | 21 | 9 | 0 | 0 | 4 | 905 | 662 |
| Pancasila | 14 | 10 | 3 | 1 | 0 | 4 | 750 | 443 |
| Bahasa Inggris | 72 | 32 | 32 | 8 | 0 | 23 | 863 | 476 |
| PJOK | 15 | 3 | 12 | 0 | 0 | 0 | 706 | 177 |
| TOTAL | 252 | 126 | 108 | 15 | 3 | 62 | 7698 | 4041 |

## 4. TP tanpa keterwakilan langsung terverifikasi (18 TP)
- **TP-BAR-SK-04** (Bahasa Arab, Sekolahku (مدرستي)): Murid mampu belajar dengan sungguh-sungguh dan mendengarkan guru sebagai wujud cinta Allah dan Rasul-Nya serta cinta ilmu. — DIRECT 0, PARTIAL 15 → NO_VERIFIED_COVERAGE
- **TP-AKA-TY-03** (Akidah Akhlak, Kalimat Tayibah Basmalah, Hamdalah, dan ): Murid mampu membiasakan mengucap kalimat tayibah basmalah, hamdalah, dan taawuz dalam kehidupan sehari-hari sebagai wujud cinta Al — DIRECT 0, PARTIAL 44 → NO_VERIFIED_COVERAGE
- **TP-AKA-SH-02** (Akidah Akhlak, Pola Hidup Sehat dan Bersih): Murid mampu menyimpulkan cara menjaga kesehatan dan kebersihan dengan benar. — DIRECT 0, PARTIAL 31 → NO_VERIFIED_COVERAGE
- **TP-BIN-B1-04** (Bahasa Indonesia, Bab 1. Aku Ciptaan Allah Swt. yang Sempu): Menggunakan anggota tubuh ciptaan Allah Swt. untuk belajar membaca dan menulis dengan sungguh-sungguh sebagai wujud syukur kepadaN — DIRECT 0, PARTIAL 25 → NO_VERIFIED_COVERAGE
- **BAH-ATP-093** (Bahasa Indonesia, Bab 2. Badanku Sehat dan Kuat): Menerapkan ilmu yang dipelajari dengan sungguh-sungguh sebagai wujud rasa syukur kepada Allah Swt. — DIRECT 0, PARTIAL 0 → NO_VERIFIED_COVERAGE
- **BAH-ATP-098** (Bahasa Indonesia, Bab 3. Keluargaku Sakinah): Menunjukkan sikap belajar dengan sungguhsungguh dalam kegiatan menyimak, membaca, dan menulis sebagai wujud menghargai ilmu yang t — DIRECT 1, PARTIAL 6 → MAPPING_REVIEW_REQUIRED
- **BAH-ATP-107** (Bahasa Indonesia, Bab 5. Asyiknya Bermain): Menggunakan ungkapan permisi, tolong, maaf, dan terima kasih dalam kehidupan sehari-hari dengan tepat sesuai kondisi sebagai wujud — DIRECT 1, PARTIAL 4 → MAPPING_REVIEW_REQUIRED
- **TP-BIN-B6-01** (Bahasa Indonesia, Bab 6. Rumahku Surgaku): Menyimak cerita yang dibacakan dengan benar. — DIRECT 0, PARTIAL 27 → NO_VERIFIED_COVERAGE
- **BAH-ATP-116** (Bahasa Indonesia, Bab 7. Sekolahku Menyenangkan): Memperhatikan adab ketika bercerita sesuai ajaran Islam. — DIRECT 2, PARTIAL 15 → MAPPING_REVIEW_REQUIRED
- **TP-PPN-B2-03** (Pancasila, Bab 2. Menaati Aturan): Menerapkan perilaku menaati aturan di lingkungan keluarga dengan benar dalam kehidupan sehari-hari sebagai wujud mengamalkan ajara — DIRECT 0, PARTIAL 58 → NO_VERIFIED_COVERAGE
- **TP-ENG-B4-07** (Bahasa Inggris, BAB 4 My Family (Anggota Keluarga)): Peserta didik dapat menuliskan frase sederhana mengenai jumlah anggota keluarga dan warna bangun datar dalam Bahasa Inggris. — DIRECT 0, PARTIAL 10 → NO_VERIFIED_COVERAGE
- **TP-ENG-B5-06** (Bahasa Inggris, BAB 5 This is My House (Ruangan dalam Ru): Peserta didik dapat mengelaborasikan anggota keluarga dengan posisinya di ruangan rumah dalam Bahasa Inggris secara tepat. — DIRECT 0, PARTIAL 10 → NO_VERIFIED_COVERAGE
- **TP-ENG-B6-08** (Bahasa Inggris, BAB 6 I Have Two Cats (Hewan Peliharaan)): Peserta didik dapat mendeskripsikan hewan peliharaannya secara singkat menggunakan Bahasa Inggris yang tepat. — DIRECT 0, PARTIAL 6 → NO_VERIFIED_COVERAGE
- **TP-ENG-B6-10** (Bahasa Inggris, BAB 6 I Have Two Cats (Hewan Peliharaan)): Peserta didik dapat menyusun gambar sebuah toko hewan peliharaan dengan benar. — DIRECT 0, PARTIAL 7 → NO_VERIFIED_COVERAGE
- **TP-ENG-B6-11** (Bahasa Inggris, BAB 6 I Have Two Cats (Hewan Peliharaan)): Peserta didik dapat mendeskripsikan gambar toko hewan peliharaan dalam Bahasa Inggris yang tepat. — DIRECT 0, PARTIAL 11 → NO_VERIFIED_COVERAGE
- **TP-ENG-B7-03** (Bahasa Inggris, BAB 7 May I Play With Your Doll (Mainan)): Peserta didik dapat mewarnai gambar mainan dan mendeskripsikannya secara singkat menggunakan Bahasa Inggris yang tepat. — DIRECT 0, PARTIAL 11 → NO_VERIFIED_COVERAGE
- **TP-ENG-B7-05** (Bahasa Inggris, BAB 7 May I Play With Your Doll (Mainan)): Peserta didik dapat bermain peran mengenai meminta izin meminjam mainan dengan Bahasa Inggris yang tepat. — DIRECT 0, PARTIAL 14 → NO_VERIFIED_COVERAGE
- **TP-ENG-B7-10** (Bahasa Inggris, BAB 7 May I Play With Your Doll (Mainan)): Peserta didik dapat menceritakan secara singkat mengenai mainan kesukaannya dengan Bahasa Inggris secara tepat. — DIRECT 0, PARTIAL 8 → NO_VERIFIED_COVERAGE

Selain itu **47 TP hanya punya 1–2 soal DIRECT** (status PARTIALLY_COVERED, kedalaman terbatas). Daftarnya ada di `UNCOVERED_TP_AND_MATERIALS.csv`. Terbanyak di Bahasa Inggris, Bahasa Indonesia, dan Akidah Akhlak.

## 5. Perlukah menambah soal? (indikatif)
Dari 126 TP yang belum COVERED, **118 TP** dinilai agen memuat kompetensi yang tidak dapat dibuktikan soal tertulis (praktik, lafal lisan, hafalan, pembiasaan, sikap, bermain peran, menulis bebas). Soal tulis tambahan pada TP-TP ini tidak menambah bukti; yang diperlukan adalah rubrik observasi, tugas unjuk kerja, atau penilaian lisan oleh guru. Hanya sekitar 8 TP tampak punya celah murni isi/pengetahuan, dan itu pun baru boleh diputuskan setelah ahli atau guru memeriksanya. Kolom `Tidak_terukur_soal_tertulis` dan `Kompetensi_belum_terwakili` di `TP_COVERAGE_DETAIL.csv` memuat rinciannya per TP. Ini penilaian agen, bukan keputusan kurikulum.

## 6. Hubungan dengan KBC, Pembelajaran Mendalam, dan Profil Lulusan (hanya soal DIRECT)
Label berasal dari audit sebelumnya dan hanya memuat bukti kata pada kunci/penjelasan; tidak diverifikasi ulang di sini. Angka = jumlah soal DIRECT dengan bukti langsung.

| Mapel | Soal DIRECT | KBC (bukti langsung) | Profil Lulusan (dimensi) | Pengalaman belajar |
|---|---|---|---|---|
| Akidah Akhlak | 441 | Allah dan Rasul-Nya 107, Ilmu 74, Diri dan Sesama 51, Lingkungan 8 | Keimanan 95, Penalaran Kritis 32, Kewargaan 8, Kesehatan 29 | Memahami 356, Mengaplikasi 85, Merefleksi 1 |
| Al-Quran Hadis | 522 | Allah dan Rasul-Nya 163, Ilmu 11, Diri dan Sesama 9 | Keimanan 198, Penalaran Kritis 71 | Mengaplikasi 98, Memahami 424 |
| Bahasa Arab | 611 | — | Penalaran Kritis 169 | Memahami 523, Mengaplikasi 88 |
| Bahasa Indonesia | 313 | Ilmu 8, Diri dan Sesama 26 | Penalaran Kritis 8, Komunikasi 9, Kesehatan 9 | Memahami 221, Mengaplikasi 92, Merefleksi 3 |
| Bahasa Inggris | 476 | Ilmu 3, Diri dan Sesama 13, Lingkungan 3 | Komunikasi 7, Kreativitas 6 | Memahami 368, Mengaplikasi 108 |
| Fikih | 396 | Allah dan Rasul-Nya 94, Diri dan Sesama 27, Lingkungan 1 | Keimanan 162, Penalaran Kritis 29, Komunikasi 3 | Memahami 308, Mengaplikasi 67, Merefleksi 1 |
| Matematika | 662 | Ilmu 3, Diri dan Sesama 2 | Penalaran Kritis 102, Komunikasi 4, Kolaborasi 2, Kemandirian 2 | Memahami 555, Mengaplikasi 107, Merefleksi 1 |
| PJOK | 177 | Ilmu 17, Diri dan Sesama 21 | Kesehatan 29 | Memahami 87, Mengaplikasi 90, Merefleksi 2 |
| Pancasila | 443 | Diri dan Sesama 33, Tanah Air 32, Lingkungan 66 | Penalaran Kritis 72, Kewargaan 161, Kolaborasi 23 | Memahami 419, Mengaplikasi 24 |

Catatan: Cinta Tanah Air hanya terbukti di Pancasila; dimensi Kemandirian, Kreativitas, dan Kolaborasi hampir tidak terbukti oleh soal tertulis (kecuali Pancasila untuk Kolaborasi); refleksi hampir tidak ada. Ini kebutuhan **aktivitas dan asesmen pendamping**, bukan kekurangan jumlah soal. Label "Penalaran Kritis" cenderung longgar (turunan dari tingkat kognitif).

## 7. Masalah sumber yang ditemukan
1. ATP Bahasa Indonesia memuat 36 TP; bank hanya 32. Empat TP ATP tidak punya TP di bank: Bab 2 (menerapkan ilmu sebagai wujud syukur), Bab 3 (sikap belajar sungguh-sungguh), Bab 5 (menggunakan ungkapan permisi, tolong, maaf, terima kasih), Bab 7 (adab bercerita). Tiga di antaranya hanya mendapat 1–2 soal yang dipindahkan dari TP saudara.
2. Teks TP bank memuat frasa tambahan ("sebagai wujud cinta Allah dan Rasul-Nya…") yang tidak ada di ATP pada 164 dari 248 TP. Audit memakai teks ATP.
3. KKTP yang diunggah berbeda dari ATP: KKTP Al-Qur'an Hadis memuat 6 surah yang tidak ada di ATP (Al-Lahab, An-Nashr, Al-Kafirun, Al-Kautsar, Al-Ma'un, Quraisy) dan penomoran TP yang melompat (8.2, 9.2, …); KKTP Akidah memuat Bab 8 (adab mandi dan berpakaian) dan Bab 9 (jujur, terima kasih, rendah hati) yang tidak ada di ATP; KKTP Bahasa Arab memuat Hobiku, Buah, dan Warna, sedangkan ATP memuat Sekolahku; KKTP Fikih 19 TP vs ATP 15 TP dengan rumusan berbeda. Dokumen KKTP masih berisi placeholder nama sekolah. KKTP tidak dipakai sebagai registry; keputusan dokumen mana yang berlaku ada pada madrasah.
4. ATP Bahasa Inggris (RAR, 2022) masih memakai istilah Profil Pelajar Pancasila dan memuat TP bertumpuk pada beberapa baris materi (mis. 1.C dan 1.D bunyinya sama).
5. ATP PJOK (PDF) memuat 15 TP alur tanpa pemetaan ke bab; materi diambil dari elemen yang sama dengan bank.

## 8. Rekomendasi
1. Putuskan dokumen sumber yang berlaku (ATP vs KKTP) sebelum menambah soal apa pun.
2. Lengkapi 4 TP ATP Bahasa Indonesia yang tidak ada di bank, atau tetapkan bahwa TP itu dicakup asesmen lain.
3. Untuk TP praktik, lisan, dan sikap (§5), siapkan rubrik observasi dan tugas unjuk kerja, bukan soal pilihan ganda.
4. Tinjau 18 TP pada §4 bersama guru mapel; terutama TP Bahasa Inggris Bab 4–7 yang menuntut menulis frase, mendeskripsikan, dan bermain peran.
5. Minta ahli materi menguji sampel label DIRECT pada Fikih, Al-Qur'an Hadis, Akidah, dan Bahasa Arab sebelum dijadikan dasar rilis.

## 9. Keterbatasan penting
Lihat `COVERAGE_AUDIT_QA.md`. Ringkasnya: seluruh label buatan AI satu keluarga model, tanpa ahli; soal dibaca dari bank **asli**, bukan `audit/FINAL`; dan label sangat sensitif pada kekerasan penilaian (§QA 4).

Berkas pendamping: `TP_COVERAGE_DETAIL.csv`, `MATERIAL_COVERAGE_DETAIL.csv`, `PASS_QUESTION_TO_TP_MAPPING.csv`, `UNCOVERED_TP_AND_MATERIALS.csv`, `COVERAGE_SUMMARY_BY_SUBJECT.csv`, `COVERAGE_AUDIT_QA.md`.
