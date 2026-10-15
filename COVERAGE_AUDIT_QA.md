# COVERAGE AUDIT — QA

## 1. Rekonsiliasi
- ID di bank asli: 9.000 (9 berkas, tiap berkas 1.000 ID unik). ID di `QUESTION_AUDIT_DETAIL.csv`: 9.000, identik. Status akhir: 7.698 PASS, 1.302 NEEDS_REVIEW. ID antrean verifikasi AI (1.302) identik dengan himpunan NEEDS_REVIEW.
- Soal yang dianalisis: **7.698 PASS**. TP bank di `ATP_COVERAGE_MATRIX.csv`: 248, semuanya ditemukan di bank. TP di ATP asli: 252 (selisih 4 = TP Bahasa Indonesia yang tidak ada di bank).
- Pencocokan TP ATP ke TP bank memakai kemiripan teks dalam bab/materi yang sama; seluruh 248 pasangan memiliki kemiripan ≥ 0,9 dan berada pada bab yang sama (tidak ada yang rendah-keyakinan).
- Sumber ATP yang dibaca: Fikih, Al-Qur'an Hadis, Akidah Akhlak, Bahasa Arab, Bahasa Indonesia, Matematika, Pancasila (docx KM Revisi), PJOK (PDF), Grow with English Kelas 1 (RAR, 9 bab RTF). Empat KKTP (Akidah Akhlak, Al-Qur'an Hadis, Fikih, Bahasa Arab) dibaca sebagai pembanding; KKTP Bahasa Arab hanya dibaca garis besarnya.
- Berkas bank yang dipakai (hash untuk pelacakan; tidak ada berkas sumber yang diubah):
- `1272ae6f-ppn_bank_1000.json` sha256:61f4bceba748
- `21cc9d0e-bar_bank_1000.json` sha256:9c637a333d0f
- `2a95935f-mtk_bank_1000.json` sha256:0d1b51e095fe
- `54bad493-bin_bank_1000.json` sha256:6367389c74ba
- `89a271e1-aka_bank_1000.json` sha256:be3ac8a0eb75
- `951fc49e-pjk_bank_1000.json` sha256:137d27911d6c
- `a652f85f-fikih_bank_1000_FIXED_gabungan.json` sha256:e001e39621f1
- `bd653f98-aqh_bank_1000.json` sha256:b9bf7a8e113d
- `c5721fce-eng_bank_1000.json` sha256:69d4143d6ebe

## 2. Pemeriksaan otomatis
| Pemeriksaan | Hasil | Rincian |
|---|---|---|
| Setiap TP asli muncul tepat sekali di TP_COVERAGE_DETAIL | LOLOS | 252 baris, 252 TP unik |
| Himpunan soal yang dipetakan = himpunan PASS | LOLOS | 7.698 ID unik, tiap ID satu tautan utama |
| Tidak ada soal NEEDS_REVIEW dalam pemetaan | LOLOS | irisan dengan 1.302 ID antrean = 0 |
| Setiap klaim keterwakilan (DIRECT>0) punya ID soal bukti | LOLOS |  |
| COVERED/PARTIALLY_COVERED tidak pernah D=0 | LOLOS |  |
| Jumlah DIRECT per TP = jumlah tautan DIRECT utama | LOLOS | 4041 |
| Rekap per mapel = jumlah baris TP dan soal | LOLOS |  |
| Setiap materi ada di ATP dan di MATERIAL_COVERAGE_DETAIL | LOLOS | 55 materi/bab |
| Tidak ada duplikasi ID dihitung sebagai soal berbeda | LOLOS |  |

## 3. Cara penilaian
- 21 kelompok soal (per mapel dan bab) dinilai oleh agen AI, yang membaca teks TP resmi dan tiap soal. Hasil per soal: DIRECT, PARTIAL, CONTEXT_ONLY, UNMAPPED, TP yang sebenarnya diukur (bila dipindahkan), dan facet kompetensi. Agen juga menilai facet kompetensi tiap TP.
- Status akhir TP ditetapkan ulang oleh aturan tetap (§2 laporan). Dua penyesuaian terhadap saran agen: (a) TP dengan nol soal DIRECT diturunkan ke NO_VERIFIED_COVERAGE (satu TP Pancasila, TP-PPN-B2-03, semula PARTIALLY_COVERED); (b) tiga TP ATP tanpa padanan di bank diberi MAPPING_REVIEW_REQUIRED.
- Tautan sekunder ("also") dicatat sebagai PARTIAL pada TP kedua dan tidak menaikkan status.
- Penghitungan "butir berbeda" ada dua: estimasi agen dan hitungan skrip atas stem unik (angka dibuang). Soal templat kembar tidak dianggap menambah kedalaman.

## 4. Sensitivitas dan keterbatasan
1. **Label bersifat penilaian model**: semua dari satu keluarga model, tanpa guru atau ahli. Kesalahan yang berkorelasi dapat lolos. Tidak ada rujukan eksternal (buku teks, mazhab, kurikulum resmi) yang diakses.
2. **Sensitif pada kekerasan penilaian.** Empat kelompok (03, 05, 06, 07) dinilai dua kali oleh agen berbeda. Kesesuaian label hanya 86,0% / 59,3% / 66,7% / 94,3%; jumlah DIRECT turun misalnya dari 180 ke 111 pada kelompok 06 (Bahasa Arab, Perkenalan). Yang dipakai adalah putaran kedua yang lebih ketat. Kelompok lain hanya dinilai sekali, sehingga angka DIRECT di sana bisa lebih longgar atau lebih ketat daripada yang seharusnya. Pemeriksaan acak 14 soal DIRECT (oleh saya sendiri, bukan ahli) menemukan label yang umumnya masuk akal, tetapi dua di antaranya tampak longgar (mis. soal arti satu kata Arab untuk TP "menyebutkan arti surah").
3. **Soal dibaca dari bank asli**, bukan `audit/FINAL/` (tidak terlampir). Sekitar 1.423 soal direvisi pada tahap final; audit revisi menyatakan ID, TP, dan kompetensi tidak berubah, jadi pemetaan ke TP kemungkinan stabil, tetapi tidak diverifikasi. Bank Fikih yang dipakai adalah `fikih_bank_1000_FIXED_gabungan.json`.
4. Soal tertulis tidak dapat membuktikan praktik, lafal lisan, hafalan, pembiasaan, kolaborasi, atau sikap. TP bertuntutan seperti itu paling banyak berstatus PARTIALLY_COVERED atau NO_VERIFIED_COVERAGE; itu bukan otomatis kekurangan soal.
5. Gambar tidak diperiksa (hanya deskripsi teks). Soal bergambar dinilai dari teks.
6. Pembedaan "tidak terukur soal tertulis" vs "celah isi" pada laporan §5 adalah penilaian agen per TP.
7. Pemetaan KBC, Pembelajaran Mendalam, dan Profil Lulusan memakai label audit sebelumnya, tidak diverifikasi ulang.
8. Materi agama dan Bahasa Arab membutuhkan peninjauan ahli sebelum status COVERED dijadikan dasar rilis (kolom `Perlu_ahli` pada `TP_COVERAGE_DETAIL.csv`).
9. 330 soal tambahan Bahasa Arab (KKTP) yang disebut ringkasan verifikasi sebelumnya tidak ada dalam data dan tidak dianalisis.

## 5. Proses yang terganggu
Pekerjaan penilaian terhenti beberapa kali oleh batas penggunaan sesi dan dilanjutkan ulang. Seluruh keluaran akhir dibangun dari berkas yang lengkap (7.698 label, 252 penilaian TP), diperiksa kelengkapannya dengan skrip.
