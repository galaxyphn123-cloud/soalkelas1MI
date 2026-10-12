# Rubrik Audit Bank Soal Kelas 1 MI Darul Arifin (Tahap 2 — uji pada sampel 180 soal)

Semua keluaran mesin (`audit_engine.py`) adalah **temuan otomatis**. Label KBC/PM/Profil Lulusan adalah usulan berbukti yang masih perlu ditinjau guru/ahli.

## 1. Sumber rujukan yang dibaca
| Rujukan | Bagian yang dipakai |
|---|---|
| KMA 1503 Tahun 2025 (perubahan KMA 450/2024) | Bagian G (Pendekatan Pembelajaran Mendalam: 8 dimensi, 3 prinsip, 3 pengalaman belajar, 4 komponen kerangka), Bagian H (KBC, kerangka 5-5-5, Panca Cinta) |
| Panduan Kurikulum Berbasis Cinta (PDF, 91 hlm.) | Bagian E dan Tabel 1 "Materi Pokok KBC" (tujuan dan materi tiap topik Panca Cinta, hlm. 25-29) |
| Pembelajaran Mendalam, Kemendikdasmen (PDF, 62 hlm.) | Delapan Dimensi Profil Lulusan (hlm. 14-15), Prinsip (hlm. 16), Pengalaman Belajar (hlm. 17-18, 25-26), Kerangka Pembelajaran |
| ATP 9 mapel | Berkas ATP di folder utama (`audit/atp_text/` berisi hasil ekstraksi teks) |

Catatan dokumen: dokumen tersendiri tentang "indikator" delapan dimensi Profil Lulusan **belum tersedia**; yang ada hanya definisi 8 dimensi (PDF Pembelajaran Mendalam hlm. 14-15). Karena itu pemetaan Profil Lulusan memakai definisi tersebut, bukan indikator terperinci. Tidak ada perbedaan versi antardokumen yang ditemukan pada bagian yang dipakai (KMA 1503 dan PDF menyebut delapan dimensi dan tiga prinsip yang sama).

## 2. Skor aspek (0-4, tidak dijumlahkan)
| Aspek | Aturan otomatis | Batas |
|---|---|---|
| ATP | 0 = TP tak tertelusur ke teks ATP; 2 = tertelusur tetapi tidak ada kata kunci TP/materi/kompetensi dalam soal; 3 = satu kata kunci; 4 = dua atau lebih | Berbasis kata; **tidak menilai kecocokan makna**. Skor 2 adalah *antrean tinjau*, bukan vonis salah |
| Akurasi | 0 = cacat struktur kunci; 3 = kunci valid, fakta menunggu ahli; 4 dicadangkan untuk jawaban yang diverifikasi ulang secara independen | Mesin tidak dapat memastikan kebenaran fakta agama/bahasa |
| Usia & bahasa | jumlah kata soal: ≤18 = 4, ≤30 = 3, ≤45 = 2, >45 = 1 | Hanya beban baca; bukan kesesuaian isi |
| Konstruksi | 0 = opsi kembar/kunci ganda/visual tanpa deskripsi; 2 = kunci terpanjang, rujuk gambar tanpa visual; 3 = sesuai | Distraktor "masuk akal" belum dinilai mesin |
| Keunikan | 0 = identik dengan ID lain (teks+opsi+jawaban); 4 = tidak ada | Duplikat substantif diaudit terpisah pada Tahap 3 |
| KBC / PM / Profil | tidak diskor; dipetakan berbukti dengan tingkat relevansi | lihat bagian 3 |

**Status:** `REVISE` bila ada cacat struktur atau catatan konstruksi; `NEEDS_REVIEW` bila skor ATP ≤2, akurasi ≤2, atau beban baca tinggi; `REJECT` hanya diberikan manual oleh ahli (mesin tidak menolak soal); selain itu `PASS`. Cacat kunci/ATP tetap memengaruhi status walau skor lain tinggi.

## 3. Aturan pemetaan berbukti
* **KBC (Panca Cinta, lexicon dari Tabel 1 KBC)**: `langsung` hanya jika kata kunci nilai ada pada **kunci jawaban/penjelasan** *dan* pada TP/materi. Bila hanya ada di soal atau TP → `konteks` / `melalui_TP`, yang **tidak dihitung** sebagai bukti. Soal tanpa bukti → `tidak_relevan` (sah; KBC tidak wajib di setiap soal).
* **Pembelajaran Mendalam**: pengalaman belajar diturunkan dari tuntutan tipe soal (Memahami = mengenali/menjelaskan; Mengaplikasi = konteks/praktik; Merefleksi hanya bila soal meminta penilaian diri). Prinsip *bermakna/menggembirakan/berkesadaran* hanya bila ada bukti konteks nyata, aktivitas bermain, atau penyadaran diri. Praktik pedagogis, kemitraan, lingkungan, dan digital **tidak dapat diukur oleh soal**; dicatat sebagai kebutuhan aktivitas pendamping.
* **Profil Lulusan**: pemetaan dengan bukti pada kunci/penjelasan + TP; `melalui_TP` tidak dihitung; Penalaran Kritis `langsung` hanya untuk level kognitif analitis/evaluatif/pemecahan masalah, `indikatif` untuk mengurutkan/mengelompokkan. Kolaborasi, Kemandirian, Kreativitas, Komunikasi lisan lebih tepat dinilai lewat observasi/rubrik/proyek guru.

## 4. Hasil kalibrasi pada sampel (180 soal, 20/mapel, minimal 2 per tipe)
| Temuan | Tindakan pada rubrik |
|---|---|
| Versi awal memberi "Cinta Ilmu/Cinta Diri dan Sesama" hanya karena kata *buku, guru, teman* di soal (mis. soal huruf awal, kosakata keluarga) | Bukti harus ada di kunci/penjelasan; selain itu `konteks` |
| "Cinta Lingkungan" muncul karena kata *bersih* pada soal jajanan sehat | Kata *bersih* dikeluarkan dari leksikon lingkungan |
| Cek "penjelasan memuat kunci" menandai tugas kinerja dan soal melengkapi | Tugas kinerja dikecualikan; hanya jadi catatan |
| Penalaran kritis diberikan pada semua soal mengurutkan/mengelompokkan | Diturunkan menjadi `indikatif` |
| Skor ATP 2 pada 33 dari 180 soal (18%) — sebagian besar kosakata TP berbeda dari kosakata soal | Diperlakukan sebagai antrean tinjau, bukan cacat; perlu ahli |

Hasil akhir sampel: PASS 135, REVISE 10, NEEDS_REVIEW 35. Detail: `sample_audit_detail.json`, `sample_audit_summary.csv`; contoh penerapan: `contoh_penerapan_rubrik.json`.
