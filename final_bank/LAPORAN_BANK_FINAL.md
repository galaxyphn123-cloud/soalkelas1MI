# Laporan bank soal final — Kelas 1 MI Darul Arifin (Fase A)

Dokumen utama: `BANK_SOAL_KELAS1_MI_DARUL_ARIFIN_FINAL.docx` (satu dokumen, 8.539 soal dengan kunci dan pembahasan, disusun per mapel > materi > TP, plus lampiran cakupan 252 TP).
Data pendukung: `final_bank/bank_final_lulus.json` (seluruh soal, bentuk sama dengan bank), `cakupan_tp.csv`, `ringkasan.json`, `tp_registry.json`.

## Keputusan yang dipakai
1. Dokumen acuan: berkas ATP per mapel di repositori (dianggap "Laporan CP, TP, ATP Kelas 1 MI Darul Arifin"; tidak ada berkas terpisah dengan nama itu). KKTP tidak menentukan cakupan; 330 soal tambahan Arab berbasis KKTP tidak dimasukkan.
2. Soal yang dimasukkan: 7.698 soal berstatus PASS (versi `audit/FINAL`, setelah revisi audit) + 841 soal baru. 1.302 soal NEEDS_REVIEW tidak dimasukkan.
3. Pemerataan: target per TP = median soal PASS per TP pada mapel itu (dibulatkan ke atas); TP di bawah target ditambah sampai target; TP di atas target tidak dikurangi.
4. TP baru: 4 TP ATP Bahasa Indonesia yang belum ada di bank (2.5, 3.5, 5.5, 7.5), masing-masing 27 soal.

## Hasil
| Mapel | TP | Soal final | Per TP sebelum (min/median/maks) | Per TP sesudah |
|---|---|---|---|---|
| Fikih | 15 | 868 | 32 / 49 / 85 | 49 / 49 / 85 |
| Al-Qur'an Hadis | 28 | 995 | 11 / 33 / 56 | 33 / 33,5 / 56 |
| Bahasa Arab | 16 | 1.036 | 48 / 61,5 / 69 | 62 / 63,5 / 69 |
| Akidah Akhlak | 26 | 1.041 | 7 / 32,5 / 63 | 33 / 33 / 63 |
| Bahasa Indonesia | 36 | 1.039 | 0 / 26 / 43 | 27 / 27 / 43 |
| Matematika | 30 | 1.012 | 15 / 31,5 / 52 | 32 / 32 / 52 |
| Pancasila | 14 | 804 | 24 / 52,5 / 69 | 53 / 53 / 69 |
| PJOK | 15 | 775 | 28 / 47 / 61 | 47 / 47 / 61 |
| Bahasa Inggris | 72 | 969 | 4 / 12 / 22 | 12 / 12 / 22 |
| Total | 252 | 8.539 | | |

Semua 252 TP memiliki soal dan mencapai target. ID unik 8.539 (tidak ada ID ganda); tidak ada duplikat identik (stem + kunci) dan tidak ada konflik kunci pada stem dan opsi yang sama.

## Proses soal baru
- 841 soal ditulis oleh 14 agen AI (satu kelompok TP per agen) dengan instruksi mengukur langsung TP dan memakai teks ATP, lalu divalidasi otomatis (`validate_new.py`: bentuk, opsi kembar, kunci terpanjang, TF berlubang, duplikat terhadap 9.000 soal bank dan antarsoal baru).
- Verifikasi buta oleh 11 agen AI lain (menyelesaikan tanpa kunci, menilai ambigu/usia/TP): ronde 1 meloloskan 786 dari 841; 55 ditolak.
- Ronde 2 menulis 55 pengganti: 51 lolos, 4 ditolak. Ronde 3 menulis 4 pengganti: 4 lolos.
- Satu soal baru (BAR-SK-0904) dibuang karena hampir kembar dengan soal lama (BAR-SK-0054) dan diganti BAR-SK-0924 (lolos verifikasi buta). Satu soal pengganti ronde 4 diperbaiki redaksinya setelah penyelesai menilai istilah terlalu abstrak.
- Total soal baru akhir: 841; seluruhnya lolos verifikasi buta dan validator.

## Keterbatasan (jangan dilewatkan)
- Tidak ada persetujuan guru atau ahli. Verifikasi seluruhnya oleh model AI dari keluarga yang sama; kesalahan yang berkorelasi dapat lolos. Independensi penyelesai buta hanya ditegakkan lewat instruksi.
- Materi agama (Fikih, Akidah Akhlak, Al-Qur'an Hadis) dan Bahasa Arab, termasuk soal baru, wajib ditinjau ahli sebelum dipakai untuk penilaian resmi. Sebagian soal PASS lama tetap membawa catatan audit (mis. indikasi di luar KKTP) yang tidak diubah.
- "Tercakup" diukur dari jumlah soal yang dipetakan pada TP (menurut `tp_id` bank), bukan dari bukti bahwa soal tulis dapat mengukur TP praktik, lisan, hafalan, atau sikap. Hasil audit "ATP Coverage Gap" (COVERED/PARTIAL per soal) tidak tersedia di repositori sehingga tidak dipakai; pemerataan ini berbasis jumlah, bukan label DIRECT/PARTIAL.
- Soal PASS lama dipakai dalam versi `audit/FINAL`, sedangkan audit cakupan dibaca dari bank asli; pada soal yang direvisi, opsi/redaksi dapat berbeda sedikit.
- Teks TP bank memuat frasa tambahan yang tidak ada di ATP pada sebagian TP; rumusan dokumen mengikuti bank, kecuali 4 TP baru yang mengikuti ATP.
- Matematika baru: kunci dihitung ulang oleh penulis dan penyelesai buta, bukan oleh skrip.
- Bahasa Inggris: ATP yang tersedia berupa teks CP dan tabel; kosakata buku Grow with English tidak dapat dicocokkan dengan sumber aslinya.
