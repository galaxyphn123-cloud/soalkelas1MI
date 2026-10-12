# -*- coding: utf-8 -*-
"""Bab dan Tujuan Pembelajaran dari ATP Grow with English Kelas 1 (9 bab, masing-masing 8 JP)."""
D = 'Peserta didik dapat '
def T(*xs): return ['Murid mampu ' + x[0].lower() + x[1:] for x in xs]
BABS = [
 dict(code='B1', name='Bab 1. Hello, How Are You? (Salam Sapaan dan Ucapan Berpisah)', quota=112, tps=T(
   'mengidentifikasi diri sendiri.', 'menggunakan gerakan tubuh untuk menyapa orang lain secara tepat.', 'menggunakan gerakan tubuh untuk merespon salam sapaan orang lain secara tepat.',
   'memahami kosakata sederhana dalam instruksi dan meresponnya dengan gerakan tubuh secara tepat.', 'menggunakan ungkapan-ungkapan untuk menyapa orang lain dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan ungkapan-ungkapan untuk merespon salam sapaan dari orang lain dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan ungkapan-ungkapan untuk mengucapkan selamat tinggal kepada orang lain dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menangkap makna dari suatu bacaan yang memuat informasi mengenai salam sapaan dalam konteks kelas.', 'menuliskan kosakata sederhana mengenai salam sapaan dan respon salam sapaan dalam Bahasa Inggris secara tepat.')),
 dict(code='B2', name="Bab 2. It's a Red Book (Benda di Dalam Kelas)", quota=111, tps=T(
   'menggunakan gerakan tubuh untuk bertanya dan merespon jawaban mengenai benda-benda di dalam kelas secara tepat.', 'mengucapkan nama-nama benda yang ada di dalam kelas dalam Bahasa Inggris dengan benar.',
   'mengidentifikasikan nama-nama benda yang ada di dalam kelas dalam Bahasa Inggris dengan tepat.', 'merespon instruksi mengenai permintaan ditunjukkannya sebuah objek benda yang ada di dalam kelas.',
   'mengidentifikasikan warna benda-benda yang ada di dalam kelas menggunakan Bahasa Inggris yang tepat.', 'mengidentifikasikan nama dan warna benda-benda yang ada di dalam kelas menggunakan Bahasa Inggris yang tepat.',
   'mengungkapkan nama dan warna benda-benda yang ada di dalam kelas menggunakan Bahasa Inggris yang tepat.', 'menuliskan frase sederhana mengenai benda-benda di kelas dalam Bahasa Inggris.')),
 dict(code='B3', name='Bab 3. I Have Two Eyes (Bagian-bagian Wajah)', quota=111, tps=T(
   'mengidentifikasi bagian-bagian wajah dalam Bahasa Inggris dengan tepat.', 'mengetahui letak bagian wajah tertentu dan meresponnya secara fisik.', 'mendeskripsikan bagian-bagian wajah dengan Bahasa Inggris yang tepat.',
   'mengucapkan nama bagian wajah dan jumlahnya dalam Bahasa Inggris dengan tepat.', 'menuliskan frase sederhana mengenai bagian-bagian wajah dalam Bahasa Inggris.')),
 dict(code='B4', name='Bab 4. My Family (Anggota Keluarga)', quota=111, tps=T(
   'mengidentifikasikan anggota keluarga dalam Bahasa Inggris yang tepat.', 'mengucapkan nama-nama anggota keluarga dalam Bahasa Inggris yang tepat.', 'menceritakan tentang anggota keluarganya dengan Bahasa Inggris yang tepat.',
   'mengidentifikasi bentuk lingkaran dan persegi dalam Bahasa Inggris dengan benar.', 'menentukan warna pada bentuk lingkaran dan persegi dalam Bahasa Inggris dengan benar.', 'mengetahui kosakata angka dalam Bahasa Inggris dengan benar.',
   'menuliskan frase sederhana mengenai jumlah anggota keluarga dan warna bangun datar dalam Bahasa Inggris.')),
 dict(code='B5', name='Bab 5. This is My House (Ruangan dalam Rumah)', quota=111, tps=T(
   'mengetahui kosakata mengenai ruangan dalam rumah dengan Bahasa Inggris yang tepat.', 'mengidentifikasikan nama-nama ruangan dalam rumah dalam Bahasa Inggris dengan tepat.', 'mengidentifikasikan warna dalam Bahasa Inggris dengan tepat.',
   'mengidentifikasi beberapa bentuk bangun datar dan warnanya dalam Bahasa Inggris dengan tepat.', 'mewarnai dengan tepat sesuai dengan instruksi yang diberikan.',
   'mengelaborasikan anggota keluarga dengan posisinya di ruangan rumah dalam Bahasa Inggris secara tepat.', 'menuliskan frase sederhana mengenai warna ruangan rumah dan warna bentuk bangun datar dalam Bahasa Inggris.',
   'mendeskripsikan ruangan-ruangan yang ada di rumahnya dengan Bahasa Inggris secara tepat.')),
 dict(code='B6', name='Bab 6. I Have Two Cats (Hewan Peliharaan)', quota=111, tps=T(
   'mengetahui kosakata mengenai hewan peliharaan dalam Bahasa Inggris yang tepat.', 'mengidentifikasikan nama hewan peliharaan dalam Bahasa Inggris dengan tepat.', 'bermain peran mengenai hewan peliharaan.',
   'mengetahui tindakan yang biasanya dilakukan terhadap hewan peliharaan dalam Bahasa Inggris secara tepat.', 'menggambar dan mewarnai hewan peliharaan.', 'mengetahui warna hewan peliharaan yang ada dalam Bahasa Inggris secara tepat.',
   'menghitung jumlah hewan peliharaan yang ada dalam Bahasa Inggris secara tepat.', 'mendeskripsikan hewan peliharaannya secara singkat menggunakan Bahasa Inggris yang tepat.',
   'menuliskan frase sederhana mengenai hewan peliharaan dan warnanya dalam Bahasa Inggris.', 'menyusun gambar sebuah toko hewan peliharaan dengan benar.', 'mendeskripsikan gambar toko hewan peliharaan dalam Bahasa Inggris yang tepat.')),
 dict(code='B7', name='Bab 7. May I Play With Your Doll (Mainan)', quota=111, tps=T(
   'mengetahui kosakata mengenai mainan dalam Bahasa Inggris yang tepat.', 'mengidentifikasikan nama-nama mainan dalam Bahasa Inggris dengan tepat.', 'mewarnai gambar mainan dan mendeskripsikannya secara singkat menggunakan Bahasa Inggris yang tepat.',
   'mengetahui tindakan yang dilakukan terhadap mainan dalam Bahasa Inggris secara tepat.', 'bermain peran mengenai meminta izin meminjam mainan dengan Bahasa Inggris yang tepat.', 'mengidentifikasikan warna mainan dalam Bahasa Inggris dengan tepat.',
   'menghitung jumlah mainan dalam Bahasa Inggris dengan benar.', 'mengetahui ukuran mainan dalam Bahasa Inggris dengan benar.', 'menuliskan frase sederhana mengenai mainan dan ukurannya dalam Bahasa Inggris.',
   'menceritakan secara singkat mengenai mainan kesukaannya dengan Bahasa Inggris secara tepat.')),
 dict(code='B8', name='Bab 8. I Like Mangoes (Buah-buahan)', quota=111, tps=T(
   'mengidentifikasikan nama buah-buahan dalam Bahasa Inggris yang benar.', 'mengetahui tindakan yang dapat dilakukan terhadap buah-buahan menggunakan kata kerja Bahasa Inggris secara tepat.',
   'bertanya mengenai kesukaan orang lain dengan menggunakan Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan ungkapan suka untuk mengekspresikan kesukaannya terhadap buah-buahan dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan ungkapan tidak suka untuk mengekspresikan ketidaksukaannya terhadap buah-buahan dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan gerakan tubuh untuk mengekspresikan rasa suka dan tidak suka secara tepat.', 'menuliskan frase sederhana mengenai buah-buahan dalam Bahasa Inggris secara tepat.', 'menggambar gambar buah kesukaannya.')),
 dict(code='B9', name='Bab 9. We Are Having Fun (Kegiatan di Taman Bermain)', quota=111, tps=T(
   'mengidentifikasikan nama-nama permainan yang ada di taman bermain dalam Bahasa Inggris yang benar.', 'mengetahui tindakan yang dapat dilakukan terhadap permainan di taman bermain menggunakan kata kerja Bahasa Inggris secara tepat.',
   'mengidentifikasikan kata kerja yang tepat untuk permainan tertentu dalam Bahasa Inggris dengan tepat.',
   'menggunakan ungkapan permintaan untuk bermain dengan memperhatikan penggunaan kata kerja dalam Bahasa Inggris yang tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menggunakan kalimat present continuous untuk menunjukkan kegiatan yang sedang dilakukannya di taman bermain dalam Bahasa Inggris secara tepat dalam konteks kelas dan kehidupan sehari-hari.',
   'menuliskan frase sederhana mengenai kegiatan di taman bermain terhadap permainannya dalam Bahasa Inggris secara tepat.')),
]
