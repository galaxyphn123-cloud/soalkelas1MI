# Ringkasan verifikasi AI — antrean verifikasi MI Darul Arifin

Semua angka dihitung dari `AI_VERIFICATION_RESULTS.csv` dan `AI_VERIFICATION_EVIDENCE.csv` (satu baris hasil per ID unik; satu ID dapat punya beberapa masalah di berkas bukti).
Status AI adalah **usulan dari model AI, bukan persetujuan ahli**. Tidak ada soal, ID, TP, kompetensi, atau kunci di bank asli maupun `audit/FINAL` yang diubah (hash SHA-256 sembilan bank asli dicocokkan ulang: tidak ada perubahan).

## 1. Cakupan dan rekonsiliasi ID
- Antrean `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv` berisi **1.220 baris**, tetapi hanya **1.111 ID unik** (satu soal dapat muncul pada beberapa baris dengan kode temuan berbeda). Angka "1.220 soal" pada permintaan adalah jumlah baris.
- Audit sebelumnya menandai **1.302 soal NEEDS_REVIEW**; **191** di antaranya **tidak ada di antrean** (sebagian besar penundaan revisi konstruksi/bahasa). Agar tidak ada NEEDS_REVIEW yang terlewat, 191 ID itu ikut diproses dan diberi label `NEEDS_REVIEW_DI_LUAR_ANTREAN`.
- Total diperiksa: **1.302 ID unik** (1.111 antrean + 191 di luar antrean). Semua ID ada di bank final, bank asli, dan audit detail; tidak ada ID yang hilang.

## 2. Hasil status (ID unik)
| Status | Jumlah |
|---|---|
| AI_VERIFIED | 456 |
| AI_FLAGGED | 294 |
| EXPERT_REQUIRED | 354 |
| SOURCE_REQUIRED | 189 |
| UNRESOLVED | 9 |
| Total | 1.302 |

Per daftar: antrean (1.111) → 349 / 259 / 326 / 168 / 9; di luar antrean (191) → 107 / 35 / 28 / 21 / 0 (urutan sama dengan tabel).
Persetujuan manusia: wajib `YA` pada 697 ID; `DISARANKAN` pada 108 ID AI_VERIFIED materi agama/bahasa; `TIDAK` pada 497.
ID dengan minimal satu masalah tercatat: **700**.

## 3. Hasil per pemeriksaan otomatis (ID unik)
| Pemeriksaan | Lolos | Catatan |
|---|---|---|
| C01 ID dan berkas | 1.302 | |
| C02 metadata dan riwayat revisi vs bank asli | 1.302 | |
| C03 struktur soal | 1.302 | |
| C04 hitung ulang dari pertanyaan | 61 lolos, 0 gagal, 1.241 tidak berlaku | hanya soal yang memuat ekspresi/data yang dapat diurai skrip |
| C05 kunci vs penjelasan | 1.290 | 12 peringatan (isian) |
| C06 heuristik jawaban ganda | 626 | 16 peringatan, 660 tidak berlaku |
| C07 konflik kunci antarsoal (stem identik) | 1.302 | |
| C08 duplikasi | 1.275 | 24 peringatan kemiripan, 3 identik |
| C09 beban baca | 1.288 | 14 peringatan |
| C10 bukti pemetaan KBC/Profil | 1.302 | hanya memeriksa bahwa bukti kata ada di kunci/penjelasan |
| C11 TP di teks ATP | 385 | 917 peringatan; hanya informasi karena rumusan TP berbeda dari teks ATP |
| C12 jawaban buta vs kunci | 1.178 cocok, 26 cocok setelah adjudikasi, 62 beda, 36 tidak berlaku | tidak berlaku = tugas unjuk kerja |

## 4. Masalah (ID unik per jenis)
Jawaban ganda menurut adjudikator 112; ambigu menurut penyelesai 316; tidak ada jawaban benar 7; penyelesai menilai kunci keliru 5 (`ENG-B8-0078, FIK-RI-0088, PJK-MH-0104, PJK-TB-0436, PJK-TB-0452`); kesesuaian TP "sebagian" 279 dan "tidak" 27; duplikat identik 3; duplikat substantif 24 + 20 dari audit sebelumnya; beban baca 14; konflik internal semantik belum tuntas 9; tidak dapat ditentukan 5.
Masalah terbanyak ada di PJOK dan Pancasila (butir "manfaat/sikap" yang beberapa opsinya sama-sama benar).

## 5. Temuan yang berbeda dari audit sebelumnya
- 17 soal dinilai berjawaban ganda/tanpa jawaban/kunci keliru padahal audit lama tidak memberi kode AMBIGU, DISTRAKTOR_AMBIGU, AKURASI_AHLI, atau KONFLIK_INTERNAL.
- 7 soal tanpa jawaban benar: `AKA-SW-0020, BIN-B6-0095, BIN-B6-0097, BIN-B6-0108, BIN-B8-0065, BIN-B8-0075, MTK-B4-0018`.
- 5 soal yang kuncinya mungkin keliru (daftar di atas) — keputusan perubahan kunci belum diambil.
- Perhitungan aritmetika Matematika yang dapat diurai (61 butir) cocok semuanya; dua dugaan awal skrip ternyata kesalahan skrip dan sudah diperbaiki sebelum hasil akhir.
- 26 perbedaan awal antara jawaban buta dan kunci dibatalkan oleh adjudikasi (kunci benar atau parafrase setara).

## 6. Metode dan bukti
1. Rekonsiliasi: antrean ↔ bank final ↔ bank asli ↔ audit detail ↔ riwayat revisi (`stage1_checks.py`, `stage1_results.json`).
2. Pemeriksaan deterministik C01–C11 per ID (kode di `stage1_checks.py`).
3. Penyelesaian buta: 15 agen AI menyelesaikan 1.302 soal tanpa kunci dan tanpa penjelasan, membaca TP dan teks ATP lengkap, dan menilai ambiguitas, usia, serta TP.
4. Adjudikasi: 4 agen AI kedua, yang melihat kunci dan jawaban buta, menilai 177 soal yang berbeda atau ditandai bermasalah.
5. Penggabungan dengan aturan tetap (`stage3_merge.py`): kunci diubah revisi → EXPERT_REQUIRED; cek keras gagal → AI_FLAGGED; jawaban bergantung buku teks → SOURCE_REQUIRED; materi agama/bahasa/TP butuh otoritas → EXPERT_REQUIRED; selain itu AI_VERIFIED.

## 7. Keterbatasan
- Seluruh "pemeriksaan independen" dilakukan model AI dari keluarga yang sama; kesalahan yang berkorelasi dapat lolos. Tidak ada ahli manusia, buku teks, atau rujukan eksternal yang diakses. Karena itu tidak ada kutipan halaman atau sumber yang diberikan; kolom sumber hanya menyebut dokumen yang tersedia di repo (teks ATP, KKTP) atau jenis sumber yang diperlukan.
- Independensi penyelesai buta hanya ditegakkan lewat instruksi (tidak ada pemisahan teknis); tidak ada agen yang melaporkan melihat kunci. Satu agen (Matematika) menulis jawabannya lewat skrip buatannya sendiri, bukan bertahap.
- Hitung ulang numerik hanya mencakup 92 soal yang pola aritmetika/datanya dapat diurai; soal cerita lain, gambar, dan hitungan tidak terurai tidak dihitung ulang oleh skrip (hanya oleh penyelesai AI).
- Perbandingan isian terbuka memakai tumpang-tindih kata; kecocokan makna penuh dinilai adjudikator, bukan skrip.
- Pemeriksaan duplikasi memakai kesamaan teks, bukan makna; konflik makna lintas soal tidak teruji penuh (9 ID berstatus UNRESOLVED karena itu).
- Penilaian kesesuaian TP adalah bacaan model atas teks ATP, bukan keputusan kurikulum. C11 hanya informasi.
- Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan: hanya bukti kata yang diverifikasi ulang; label tetap usulan.
- `AI_VERIFIED` pada materi agama dan bahasa Arab bukan pengganti persetujuan ahli (`DISARANKAN` pada 108 ID).
- 330 soal tambahan Bahasa Arab (KKTP) tidak termasuk dalam verifikasi ini.

## 8. Berkas
`AI_VERIFICATION_RESULTS.csv`, `AI_VERIFICATION_EVIDENCE.csv`, `EXPERT_REQUIRED_QUEUE.csv` (354), `SOURCE_REQUIRED_QUEUE.csv` (189), `stage1_results.json`, `stats.json`, skrip `stage1_checks.py` dan `stage3_merge.py`. Hasil mentah agen berada di folder scratchpad sesi dan disalin ke `raw/` untuk jejak.
