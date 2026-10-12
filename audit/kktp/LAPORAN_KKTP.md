# Laporan tindak lanjut KKTP (celah CP–TP)

Arahan pengguna: periksa berkas KKTP dan ikuti KKTP untuk celah CP–TP. Semua angka di bawah berasal dari
`audit/kktp/KKTP_SUMMARY.json`, `KKTP_COVERAGE_MATRIX.csv`, dan `KKTP_ALIGNMENT_PER_SOAL.csv`.
Label berbasis kata kunci/pemetaan materi adalah **indikasi**, bukan penetapan; keputusan akhir ada pada guru/ahli.
Tidak ada soal lama yang diubah, dipindah, atau dihapus; ID dan status audit lama tetap.

## Keputusan per celah
| Celah | Isi KKTP | Tindakan |
|---|---|---|
| Fikih: salat dan azan | KKTP Fikih tidak punya TP salat/azan. Salat hanya muncul sebagai rukun Islam (Bab 1). Azan tidak disebut. | Tidak dibuat TP/soal baru (mengikuti KKTP). Soal lama tetap; 28 soal azan/iqamah dan 31 soal gerakan salat diberi indikasi `INDIKASI_DI_LUAR_KKTP`. |
| Akidah Akhlak: Asmaul Husna dan kisah Nuh | KKTP Akidah tidak memuat keduanya. | Tidak dibuat TP/soal baru. Bank lama juga tidak memiliki bab itu. |
| Bahasa Arab: hobi, buah, warna | KKTP Bab III Hobiku, Bab V Buah, Bab VI Warna ada. | Dibuat 330 soal tambahan (110 per bab) di berkas terpisah. TP dikutip dari kolom Alur Tujuan Pembelajaran KKTP. |

## Soal tambahan Bahasa Arab
- Berkas: `bahasa_arab/tambahan_kktp/bar_tambahan_kktp_330.json`; pembangkit `build_kktp.py`, data `kktp_data.py`.
- ID baru `BAR-HB-`, `BAR-BH-`, `BAR-WR-`; tidak bentrok dengan 1.000 soal lama. Soal identik dengan bank lama dibuang saat pembangkitan (36 butir).
- Bank lama `bar_bank_1000.json` tidak disentuh.
- Setiap soal bertanda `status_verifikasi: BELUM_DIVERIFIKASI_AHLI`. Verifikasi yang sudah dilakukan: cek struktur otomatis (0 masalah, ID unik, opsi tidak kembar, kunci bukan opsi terpanjang menonjol) dan satu putaran tinjau baca oleh model AI (bukan ahli bahasa Arab).
- Tinjau baca: 330 soal dibaca, 19 temuan (0 salah Arab, 0 kunci salah, 3 ambigu gambar, 11 TP tidak cocok, 6 lain-lain). Semua sudah diperbaiki di pembangkit (gambar dinetralkan, pemetaan TP diperbaiki, rubrik tulis dibedakan dari rubrik lafal, dialog terima kasih dibuang) dan bank dibangun ulang. Hasil perbaikan belum ditinjau ulang.
- Perlu guru/ahli bahasa Arab: harakat, kesesuaian هذا/هذه, bentuk muannats warna (حَمْرَاءُ dst.), dan kewajaran kalimat.

## Temuan lain dari perbandingan KKTP vs bank (tidak diubah)
- Bahasa Arab: 250 soal Sekolahku (مدرستي) ada di bank tetapi tidak ada di KKTP → `BAB_TIDAK_TERCANTUM_DI_KKTP`.
- Al-Qur'an Hadis: 143 soal penulisan huruf terpisah/tersambung (materi HT) tidak tercantum di KKTP. 6 soal menyebut surah di luar empat surah pokok. Huruf di luar rentang ا–خ dicatat sebagai informasi pada 53 soal.
- Al-Qur'an Hadis: KKTP Bab 6 (Al-Lahab), 8 (An-Nashr), 9 (Al-Kafirun), 10 (Al-Kautsar), 11 (Al-Ma'un), 12 (Quraisy) belum punya soal.
- Akidah Akhlak: KKTP Bab 8 (adab mandi dan berpakaian) dan Bab 9 (jujur, terima kasih, rendah hati) belum punya soal. 55 soal lama berisi topik di luar KKTP (sifat rasul, selawat, tasbih, tasyahud, silsilah, sifat Allah selain Wujud/Qidam/Baqa').
- Fikih: 106 soal berindikasi di luar KKTP (azan, gerakan salat, najis berat, hari raya/Hijriah, hadas besar, kebersihan hati).
- Fikih, rukun tayamum: KKTP 5.2 menyebut niat, usap wajah, usap tangan. Bank menyebut empat rukun (menambah tertib). KKTP tidak menyatakan jumlahnya hanya tiga, jadi konflik belum terbukti. FIK-WT-0083, 0086, 0112, 0141 diberi `PERLU_TINJAU_AHLI_KKTP`, kunci tidak diubah.
- Ketidaksesuaian ATP vs KKTP (jumlah bab AQH, Akidah, Arab) dicatat; keputusan ada pada guru.

## Belum dikerjakan (menunggu keputusan pengguna)
Soal untuk 6 surah AQH dan Akidah Bab 8–9 tidak dibuat, karena arahan hanya menyebut celah Fikih, Akidah (Asmaul Husna/Nuh), dan Arab.
Laporan induk `audit/MASTER_AUDIT_REPORT.md` dan 7 berkas utama audit tidak dihitung ulang: 330 soal baru belum masuk 9.000 soal yang diaudit.
