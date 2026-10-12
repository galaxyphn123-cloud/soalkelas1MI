# MASTER AUDIT REPORT — Bank Soal Kelas 1 MI Darul Arifin (9 mata pelajaran)

Tanggal: 2026-10-12 · Cabang: `claude/affectionate-meitner-8psj0c` · Bank asli (9 berkas JSON) **tidak diubah**; hasil perbaikan ada di `audit/FINAL/` sebagai versi terpisah yang dapat dibandingkan.

## 1. Ringkasan eksekutif
- **Diperiksa: 9.000 dari 9.000 soal** (tiap ID tercatat statusnya). Pemeriksaan = mesin audit otomatis (struktur, duplikasi, beban baca, keselarasan kata kunci ATP, pemetaan KBC/PM/Profil berbukti) **ditambah tinjau baca seluruh soal oleh model AI** (bukan guru/ahli). Karena itu seluruh temuan adalah *temuan otomatis/usulan*; tidak ada soal yang telah divalidasi ahli materi.
- **Status awal**: PASS 6.313 · REVISE 1.601 · NEEDS_REVIEW 1.086 · REJECT 0.
- **Status akhir (setelah revisi)**: PASS 7698 · NEEDS_REVIEW 1302 · REVISE 0 · REJECT 0. Soal NEEDS_REVIEW **ditahan** dan tidak diubah, dipindahkan, atau dihapus sampai ada keputusan guru/ahli.
- **Revisi**: 1.423 soal direvisi (hanya berdasarkan temuan teridentifikasi; ID, TP, dan kompetensi tidak berubah; 185 usulan ditunda ke ahli karena memerlukan perubahan kunci/tipe/desain). Tidak ada soal dihapus atau ditolak. Tidak ada pesan moral/label KBC yang ditambahkan ke soal.
- **Kunci jawaban yang berubah (11 soal)**: FIK-RI-0026, AQH-HT-0111, AKA-KN-0110, PPN-B4-0115, PPN-B4-0213, PJK-HA-0037, PJK-MH-0038, PJK-MH-0102, ENG-B3-0019, ENG-B3-0076, ENG-B5-0106 — semuanya kunci yang jelas salah/rusak (atau kunci kelompok) dan **wajib dikonfirmasi** guru/ahli (masuk antrean "KONFIRMASI_PASCA_REVISI").
- **Yang belum terverifikasi** (dinyatakan eksplisit): kebenaran fakta agama/mazhab/budaya/bahasa secara otoritatif, isi gambar (hanya deskripsi teks `visual_prompt`), kesesuaian pedagogis kelas 1, pemetaan final KBC/PM/Profil, dan buku ajar rujukan.

## 2. Status per mata pelajaran
| Mapel | Soal | Awal: PASS / REVISE / NEEDS_REVIEW | Revisi diterima | Revisi ditunda | Akhir: PASS / NEEDS_REVIEW / REVISE |
|---|---|---|---|---|---|
| Fikih | 1000 | 569 / 266 / 165 | 265 | 1 | 830 / 170 / 0 |
| Al-Quran Hadis | 1000 | 871 / 48 / 81 | 48 | 0 | 917 / 83 / 0 |
| Bahasa Arab | 1000 | 915 / 51 / 34 | 51 | 0 | 966 / 34 / 0 |
| Akidah Akhlak | 1000 | 770 / 132 / 98 | 122 | 10 | 891 / 109 / 0 |
| Bahasa Indonesia | 1000 | 634 / 242 / 124 | 239 | 3 | 870 / 130 / 0 |
| Matematika | 1000 | 835 / 91 / 74 | 75 | 16 | 905 / 95 / 0 |
| Pancasila | 1000 | 573 / 239 / 188 | 179 | 62 | 750 / 250 / 0 |
| PJOK | 1000 | 450 / 347 / 203 | 261 | 87 | 706 / 294 / 0 |
| Bahasa Inggris | 1000 | 696 / 185 / 119 | 183 | 6 | 863 / 137 / 0 |
| **Total** | **9.000** | **6.313 / 1.601 / 1.086** | **1.423** | **185** | **7698 / 1302 / 0** |

Kode temuan tinjau baca (satu soal dapat memuat beberapa kode): {'AKURASI_AHLI': 223, 'ATP_INDIKASI': 302, 'USIA_ISI': 254, 'ATP_INDIKASI_KUAT': 4, 'KONSTRUKSI': 953, 'BAHASA': 264, 'AMBIGU': 218, 'DISTRAKTOR_AMBIGU': 108, 'AKURASI_KONFLIK_INTERNAL': 38, 'DUP_DIPERTAHANKAN': 327, 'AKURASI_SALAH_TEGAS': 10, 'DUP_SUBSTANTIF': 41}.

## 3. Temuan utama dan risiko kurikulum
1. **Keselarasan ATP (302 soal terindikasi, 4 dengan bukti dokumen kuat)**: sebagian besar bank dibangun dari TP, tetapi ada celah antara CP/ATP dan TP: Fikih (salat, azan/ikamah, hari raya/kurban, kebersihan hati ± 85 soal; CP memuat salat fardu dan azan tetapi ATP hanya punya 4 materi), Akidah Akhlak (asmaulhusna, malaikat, kisah Nabi Nuh tanpa TP), Bahasa Arab (CP memuat hobi, buah, warna, transportasi, alam tetapi bank tidak punya soal), PJOK (doa/syukur di luar teks ATP), Pancasila (fakta budaya daerah), Matematika (selisih, genap/ganjil). Tidak ada soal yang saya nyatakan *terbukti* tidak selaras; mesin hanya memberi bukti dokumen (ketiadaan istilah pada ATP/CP) atau kemiripan ke TP lain.
2. **Akurasi (223 soal butuh ahli, 38 konflik antar-soal, 10 kunci jelas salah)**: bergantung mazhab (Fikih: rukun/tepukan tayamum, najis, air musta'mal), penomoran ayat, terjemahan hadis, arti kosakata Arab, ejaan "qurban/kurban", istilah gerak PJOK. Konflik internal terbanyak pada PJOK (9), Pancasila (9), Inggris (10), Akidah (6).
3. **Kesesuaian usia (254 soal)**: istilah abstrak/teknis (nisab, haul, tingkatan najis, tasydid, mudzakkar-muannats, selisih, present continuous, rukun jumlah).
4. **Konstruksi (≈953 temuan)**: jawaban terbaca dari stem/opsi, pengecoh absurd/generik hasil templat, benar/salah berisi titik-titik, stem negatif, pengecoh anagram/acak kalimat yang mudah dieliminasi (Inggris), teks cerita yang dirujuk tidak dimuat (Bahasa Indonesia 211 soal; sudah dimuat dari sumber pembangkit pada revisi, tetapi soal menjadi lebih panjang).
5. **Pola kunci**: kunci opsi terpanjang pada 46–78% pilihan ganda bank asli (613 soal menonjol → 74 tersisa pada soal yang ditahan); benar/salah condong "Benar" (Fikih 168:42); blok benar/salah berkunci seragam (Pancasila B3, B4); soal sulit hanya 535/9000.
6. **Tugas kinerja**: 100% tugas kinerja PJOK memakai rubrik generik; observasi guru diperlukan untuk kolaborasi, kemandirian, kreativitas, dan kesehatan (soal tertulis tidak dapat membuktikannya).
7. **Metadata**: `sumber_atp` salah pada 5 blueprint (dikoreksi, lihat §8), `cognitive_level` memakai 12 nilai tidak baku, ID `FIK-RI-0126` tidak ada, Fikih punya field tambahan `prerequisite`/`mastery_target`.
8. **Soal bergambar**: hanya deskripsi teks; gambar belum dibuat; sebagian deskripsi membocorkan jawaban (diperbaiki sebagian pada revisi).

## 4. Distribusi pemetaan (usulan berbukti, bukan penetapan final)
Rujukan: KMA 1503/2025 (Bagian G, H), Panduan KBC (Tabel 1 Panca Cinta), PDF Pembelajaran Mendalam (8 dimensi, 3 prinsip, 3 pengalaman belajar), dokumen Dimensi Kompetensi Profil Lulusan SD/MI (subdimensi dan indikator). Label hanya "langsung" bila bukti ada pada kunci/penjelasan dan pada TP/materi; "konteks"/"melalui TP" tidak dihitung. Satu soal dapat memiliki beberapa label; jumlah label bukan bukti keberhasilan kurikulum.
- **KBC langsung**: {'Cinta Allah dan Rasul-Nya': 921, 'Cinta Diri dan Sesama': 600, 'Cinta Lingkungan': 178, 'Cinta Ilmu': 258, 'Cinta Tanah Air': 106}; konteks (tidak dihitung): {'Cinta Allah dan Rasul-Nya': 697, 'Cinta Ilmu': 1025, 'Cinta Diri dan Sesama': 1544, 'Cinta Tanah Air': 216, 'Cinta Lingkungan': 292}.
- **Pembelajaran Mendalam**: pengalaman {'Memahami': 7434, 'Mengaplikasi': 1566, 'Merefleksi': 18}; prinsip {'Menggembirakan': 758, 'Bermakna': 402, 'Berkesadaran': 18}. Praktik pedagogis, kemitraan, lingkungan belajar, pemanfaatan digital tidak dapat diukur soal tertulis → aktivitas pendamping guru.
- **Profil Lulusan langsung**: {'Keimanan dan Ketakwaan terhadap Tuhan YME / Hubungan dengan Tuhan YME': 1060, 'Penalaran Kritis / Penyelesaian Masalah': 801, 'Komunikasi / Berbicara': 22, 'Kewargaan / Kewargaan Lokal': 272, 'Kewargaan / perlu ditetapkan guru': 87, 'Kolaborasi / Kerja sama': 37, 'Kolaborasi / Peduli': 47, 'Kesehatan / Hidup bersih dan sehat': 118, 'Komunikasi / Membaca': 11, 'Penalaran Kritis / Pengambilan Keputusan': 31, 'Kesehatan / Kebugaran, kesehatan fisik, dan kesehatan mental': 78, 'Kemandirian / Bertanggung Jawab': 5, 'Komunikasi / Menulis': 1, 'Kolaborasi / Berbagi': 5, 'Kewargaan / Kewargaan Nasional': 44, 'Kreativitas / Karya': 25, 'Komunikasi / perlu ditetapkan guru': 17}. Catatan: "Penalaran Kritis/Penyelesaian Masalah" (≈800) diturunkan dari `cognitive_level` label bank (membandingkan, menganalisis, memecahkan masalah), bukan dari analisis tiap soal, sehingga cenderung terlalu longgar; "Pengambilan Keputusan" hanya indikatif (350).
- **Rekomendasi pendamping non-tes**: observasi/rubrik/proyek untuk Kolaborasi, Kemandirian, Kreativitas, Komunikasi lisan, Kesehatan (praktik), dan Keimanan (praktik ibadah); refleksi hanya 18 soal.

## 5. Cakupan ATP
178 dari 248 TP berstatus `perlu_perhatian` (benar/salah condong, porsi soal penerapan/praktik <15% untuk TP berverba praktik, dsb.); rincian per TP di `ATP_COVERAGE_MATRIX.csv`. Kompetensi tanpa soal memadai: Bahasa Arab (hobi, buah, warna, transportasi, alam), Akidah Akhlak (asmaulhusna, malaikat, kisah Nuh), Fikih (salat fardu/berjemaah, azan/ikamah, zikir, bila CP dipertahankan). Kompetensi terlalu banyak diulang: satu fakta dibangun menjadi 4–6 bentuk soal (pilihan ganda, benar/salah, isian, melengkapi) di hampir semua mapel.

## 6. Duplikasi
- Duplikat identik pada bank asli: **0**. Setelah revisi muncul 3 kelompok identik (PJK-TB-0450/0457, ENG-B6-0065..0068, ENG-B7-0071..0073) → ditahan (NEEDS_REVIEW), tidak dihapus.
- Kandidat duplikat substantif: 207 pasangan dinilai; 327 ID ditandai `DUP_DIPERTAHANKAN` (kembar templat dengan fakta/angka berbeda, berfungsi sebagai varian), 41 ID ditandai `DUP_SUBSTANTIF` (ditahan; penghapusan hanya setelah keputusan). Rincian: `DUPLICATION_REPORT.csv`.

## 7. Antrean verifikasi guru/ahli
1220 baris (soal unik ≈ 1111) pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`, dikelompokkan menurut peninjau: {'Guru/ahli': 73, 'Ahli materi': 261, 'Ahli materi/penyusun soal': 326, 'Guru kelas 1': 254, 'Kurikulum (ATP/TP)': 306}. Prioritas: (1) 11 kunci yang berubah, (2) AKURASI_KONFLIK_INTERNAL (38) dan AKURASI_SALAH_TEGAS (10), (3) AKURASI_AHLI (223), (4) ATP_INDIKASI (302; keputusan kurikulum: perluas TP/ATP atau keluarkan topik), (5) USIA_ISI (254), (6) AMBIGU/DISTRAKTOR (326), (7) duplikat substantif (41) dan konfirmasi pasca-revisi (25).

## 8. Revisi yang dilakukan
- 1.423 soal; jenis (satu soal dapat memuat lebih dari satu): konstruksi 662, redaksi/bahasa 267, panjang opsi/kunci terpanjang 622, tipe soal isian→short_answer 38, koreksi kunci/terjemahan/kelompok 11. Pembatas otomatis (`apply_revisions.py`): ID/TP/kompetensi tidak berubah; hanya field question/options/explanation/visual_prompt/question_type/answer/difficulty; teks dan huruf kunci pilihan ganda tidak boleh berubah kecuali ada temuan AKURASI_SALAH_TEGAS; opsi tidak boleh kembar; pilihan ganda tidak boleh lagi berkunci opsi terpanjang menonjol. Setiap soal membawa `revision_history` (sebelum/sesudah, alasan, verifikasi).
- Soal NEEDS_REVIEW tidak diubah (kecuali 5 kunci jelas salah yang dikoreksi dan tetap ditahan menunggu konfirmasi).
- Metadata: `sumber_atp` pada blueprint Bahasa Arab, Akidah Akhlak, Bahasa Indonesia, Matematika, Pancasila dikoreksi ke ATP yang benar (nilai lama disimpan pada `sumber_atp_sebelumnya_salah`; templat `make_files.py` pembangkit ikut dikoreksi).
- Hal yang perlu perhatian pada revisi: dialog bacaan ENG-B1-0092..0098 dikarang penyusun revisi; teks cerita BIN ditambahkan dari sumber pembangkit sehingga soal lebih panjang; tugas kinerja PJOK diberi indikator teramati yang merupakan tafsir penyusun; pengecoh baru pada soal sikap perlu dibaca ulang guru.

## 9. Verifikasi konsistensi dan QA akhir
- Seluruh 9 bank: jumlah ID audit = jumlah ID bank (9.000), ID unik, urutan sama; hash SHA-256 bank asli sebelum/sesudah audit sama; dua kali jalan menghasilkan keluaran identik; implementasi independen pemeriksaan struktur cocok dengan mesin (`CONSISTENCY_CHECK.json` tiap mapel).
- Bank FINAL: ID dan urutan identik dengan asli; metadata inti (id, subject, grade, phase, tp_id, tp, material, competency) tidak berubah; setiap soal yang berubah memiliki `revision_history`; tidak ada soal PASS dengan isu struktur tersisa; tidak ada soal NEEDS_REVIEW diubah selain koreksi kunci jelas salah; `VERIFIKASI_FINAL.json` melaporkan 0 masalah.
- Keterbatasan mesin: penyaring ATP berbasis kata kunci menangkap hanya sekitar dua pertiga temuan ATP hasil bacaan (Fikih: 60/88) dan banyak positif palsu; karena itu keselarasan ATP diputuskan lewat tinjau baca, bukan mesin saja.

## 10. Rekomendasi
1. Jadikan antrean §7 sebagai pekerjaan guru/ahli; jangan merilis soal NEEDS_REVIEW ke siswa sebelum ditinjau.
2. Putuskan kebijakan kurikulum: apakah CP (salat, azan, hobi/warna, asmaulhusna) dilengkapi TP/ATP atau soal terkait dikeluarkan.
3. Tetapkan rujukan mazhab (Fikih/Akidah) dan rujukan ejaan/terjemahan.
4. Siapkan gambar untuk soal bergambar dan rubrik teramati untuk tugas kinerja.
5. Tambahkan soal untuk kompetensi yang belum tercakup hanya setelah keputusan kurikulum (tidak dilakukan dalam audit ini).
6. Pertimbangkan bank "kurasi" yang mengurangi varian templat berulang bila bank 1.000 soal/mapel tidak diperlukan.

## 11. Berkas keluaran (`audit/`)
`MASTER_AUDIT_REPORT.md` (ini) · `QUESTION_AUDIT_DETAIL.csv` (9.000 baris) · `QUESTION_REVISIONS.csv` · `ATP_COVERAGE_MATRIX.csv` · `KBC_DEEP_LEARNING_PROFILE_MATRIX.json` · `DUPLICATION_REPORT.csv` · `FINAL/<mapel>_final.json` (FINAL_QUESTION_BANK, 9 berkas) · `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv` · `MASTER_STATS.json` · per mapel `audit/<mapel>/` (laporan, detail JSON, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK) · alat: `audit_engine.py`, `audit_full.py`, `apply_revisions.py`, `build_master.py`, `verify_subject.py`, `verify_final.py` · rubrik: `RUBRIK_AUDIT.md`, `TAHAP1_INVENTARIS.md`.
