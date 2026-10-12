# -*- coding: utf-8 -*-
"""Fakta, skenario, dan tugas tulisan tangan Matematika. Kunci (bab, tp)."""
R = 'Dinilai guru: ketepatan hasil, cara menghitung, dan sikap (skala 1-4).'
F, S, T, P, G, O, M = [], [], [], [], [], [], []
def f(b, t, stem, ok, bad, expl='', diff='easy'): F.append((b, t, stem, ok, bad, expl or f'Jawaban: {ok}.', diff))
def s(b, t, long, short, ok, bad, expl, diff='medium', vis=None): S.append((b, t, long, short, ok, bad, expl, diff, vis))

# ---------------- BAB 1 TP4 nilai Islam: berbagi adil / sedekah (selain generator share)
f(1, 4, 'Berbagi sama banyak kepada teman disebut berbagi secara ....', 'adil', ['curang', 'pelit', 'asal'])
f(1, 4, 'Memberikan sebagian harta kepada orang yang membutuhkan disebut ....', 'bersedekah', ['berhutang', 'menyimpan', 'menjual'])
f(1, 4, 'Dalam Islam, bersedekah dilakukan dengan hati yang ....', 'ikhlas', ['terpaksa', 'sombong', 'marah'])
f(1, 4, 'Bilangan membantu kita menghitung sedekah yang akan diberikan. Jika bersedekah 2 koin lalu 3 koin, seluruhnya ... koin.', '5', ['4', '6', '1'])
f(1, 4, 'Jika ada 6 permen dan dibagi untuk 2 anak sama banyak, tiap anak mendapat ... permen.', '3', ['2', '4', '6'])
s(1, 4, 'Rafi punya 4 kue. Temannya tidak punya kue. Sikap Rafi yang adil dan peduli adalah ....', 'Melihat temannya tidak punya kue, Rafi', 'membagi kuenya sama banyak, masing-masing 2', ['memakan semua kue', 'memberi temannya 1 saja', 'menyembunyikan kue'], 'Berbagi adil: 4 dibagi 2 = 2.')
s(1, 4, 'Salma menghitung uang tabungannya untuk disedekahkan. Sikap yang baik adalah ....', 'Saat menyedekahkan uang tabungannya, Salma', 'menghitung dengan teliti dan memberi dengan ikhlas', ['asal memberi lalu menyombongkan diri', 'mengambil kembali', 'memberi sambil marah'], 'Sedekah dengan ikhlas dan teliti.')
s(1, 4, 'Perhatikan gambar! Dua anak berbagi sepuluh kelereng sehingga masing-masing mendapat lima. Sikap mereka menunjukkan ....', 'Gambar dua anak membagi sepuluh kelereng sama banyak menunjukkan sikap', 'adil dan saling berbagi', ['curang', 'pelit', 'rebutan'], 'Berbagi sama banyak itu adil.', 'easy',
  'Dua anak duduk di lantai, di antara mereka sepuluh kelereng terbagi menjadi dua tumpukan lima.')
T += [(1, 4, 'Berbagi secara adil artinya membagi sama banyak.', True, 'Adil = sama banyak.'), (1, 4, 'Bersedekah hanya boleh dilakukan oleh orang dewasa.', False, 'Anak-anak pun boleh bersedekah.')]
P += [(1, 4, 'Peragakan membagi tujuh buah jeruk untuk tiga orang secara adil dan jelaskan!')]

# ---------------- BAB 2
f(2, 4, 'Menghitung barang dagangan dengan jujur berarti hasilnya ....', 'sesuai jumlah sebenarnya', ['dikurangi', 'ditambah-tambah', 'asal sebut'])
f(2, 4, 'Orang yang jujur dalam berhitung akan disukai ....', 'Allah dan sesama', ['tidak ada', 'musuhnya', 'setan'])
f(2, 4, 'Mengharapkan rida Allah artinya berbuat baik dengan niat ....', 'karena Allah', ['ingin dipuji', 'ingin hadiah', 'takut dimarahi'])
f(2, 4, 'Saat menghitung uang kembalian, kita harus ....', 'teliti dan jujur', ['asal-asalan', 'curang', 'tergesa-gesa'])
f(2, 4, 'Jika menemukan uang lebih saat menghitung, kita sebaiknya ....', 'mengembalikannya', ['menyimpannya', 'membelanjakannya', 'menyembunyikannya'])
s(2, 4, 'Dina menghitung 3 pensil milik Rani dan 4 pensil miliknya. Ia ingin mengaku hanya punya 3 agar mendapat hadiah. Sikap yang jujur adalah ....', 'Saat ingin mendapat hadiah, Dina yang jujur', 'menyebut jumlah pensilnya yang sebenarnya', ['menyembunyikan pensil', 'berbohong tentang jumlah', 'menyuruh Rani berbohong'], 'Jujur dalam berhitung.')
s(2, 4, 'Fikri membantu ibu menghitung 5 telur ditambah 4 telur di warung. Ia ingin ibu rida. Sikap Fikri adalah ....', 'Membantu ibu menghitung telur, Fikri', 'menghitung dengan teliti dan jujur', ['menghitung asal', 'berbohong supaya cepat selesai', 'menolak membantu'], 'Berhitung jujur mengharap rida.')
s(2, 4, 'Perhatikan gambar! Seorang anak mengembalikan koin lebih yang diberikan penjual karena salah hitung. Sikap anak itu menunjukkan ....', 'Gambar anak mengembalikan koin lebih kepada penjual menunjukkan sikap', 'jujur', ['curang', 'rakus', 'malas'], 'Jujur mengembalikan kelebihan.', 'easy',
  'Anak laki-laki di depan penjual, menyerahkan sebuah koin kembali sambil menunjuk uang kembalian.')
T += [(2, 4, 'Jujur saat berhitung adalah akhlak terpuji.', True, 'Jujur terpuji.'), (2, 4, 'Menambah hasil hitungan agar terlihat pintar adalah perbuatan baik.', False, 'Itu tidak jujur.')]
P += [(2, 4, 'Ceritakan pengalamanmu berhitung dengan jujur lalu tuliskan hasil penjumlahannya!')]

# ---------------- BAB 3 TP1 mengenal pengurangan, TP4 peduli
f(3, 1, 'Pengurangan berarti banyak benda menjadi ....', 'lebih sedikit', ['lebih banyak', 'tetap', 'dua kali lipat'])
f(3, 1, 'Tanda untuk pengurangan adalah ....', '-', ['+', '=', '>'])
f(3, 1, 'Tanda "-" dibaca ....', 'kurang', ['tambah', 'sama dengan', 'lebih dari'])
f(3, 1, 'Tanda "=" dibaca ....', 'sama dengan', ['kurang', 'tambah', 'lebih dari'])
f(3, 1, 'Jika benda diambil atau dibuang dari kumpulan benda, kita menggunakan ....', 'pengurangan', ['penjumlahan', 'pembagian', 'perbandingan'])
f(3, 1, 'Hasil pengurangan disebut juga ....', 'selisih atau sisa', ['jumlah', 'tambahan', 'banyaknya awal'], diff='medium')
f(3, 1, 'Jika dari 6 benda diambil 6 benda, sisanya ....', 'nol', ['satu', 'enam', 'dua belas'], diff='medium')
f(3, 1, 'Jika dari 5 benda diambil 0 benda, sisanya ....', '5', ['0', '1', '10'], diff='medium')
f(3, 1, 'Kalimat matematika "7 - 2 = 5" dibaca ....', 'tujuh kurang dua sama dengan lima', ['tujuh tambah dua sama dengan lima', 'tujuh sama dengan dua kurang lima', 'dua kurang tujuh'], diff='medium')
s(3, 1, 'Perhatikan gambar! Ada 6 burung di dahan, lalu 2 burung terbang. Kalimat yang menggambarkan keadaan itu adalah ....', 'Gambar 6 burung dengan 2 yang terbang menunjukkan kalimat', '6 - 2 = 4', ['6 + 2 = 8', '2 - 6 = 4', '6 - 2 = 8'], 'Ada 6, pergi 2, tersisa 4.', 'medium',
  'Enam burung di dahan; dua di antaranya digambar terbang menjauh dengan anak panah.')
T += [(3, 1, 'Pengurangan membuat jumlah benda menjadi lebih sedikit.', True, 'Mengurangi = lebih sedikit.'), (3, 1, 'Tanda + dipakai untuk pengurangan.', False, 'Tanda - untuk pengurangan.')]
M += [(3, 1, 'Jodohkan simbol dengan bacaannya!', [('+', 'tambah'), ('-', 'kurang'), ('=', 'sama dengan'), ('>', 'lebih dari')], 'Simbol matematika.')]
P += [(3, 1, 'Ambil beberapa kancing dari tumpukan, lalu tuliskan kalimat pengurangannya!')]

f(3, 4, 'Berbagi kepada teman yang membutuhkan menunjukkan kepedulian kepada ....', 'sesama', ['benda', 'mainan', 'televisi'])
f(3, 4, 'Jika punya 8 roti dan diberikan 3 roti kepada tetangga, sisanya ... roti.', '5', ['3', '4', '11'])
f(3, 4, 'Jika punya 10 permen dan dibagikan 4 kepada adik, sisanya ... permen.', '6', ['4', '5', '14'])
f(3, 4, 'Berbagi membuat hati kita merasa ....', 'senang', ['sedih', 'marah', 'kecewa'])
s(3, 4, 'Hasan punya 9 buku. Temannya tidak punya buku bacaan. Hasan meminjamkan 3 buku. Sisa buku Hasan adalah ....', 'Setelah meminjamkan 3 dari 9 buku, sisa buku Hasan', '6 buku', ['5 buku', '7 buku', '12 buku'], '9 - 3 = 6.')
s(3, 4, 'Mira punya 7 apel. Ia memberi 2 apel kepada tetangga. Sikap Mira menunjukkan ....', 'Memberi 2 dari 7 apel kepada tetangga menunjukkan sikap Mira yang', 'peduli kepada sesama', ['pelit', 'serakah', 'tidak peduli'], 'Berbagi = peduli.', 'easy')
T += [(3, 4, 'Memberikan sebagian milik kepada yang membutuhkan membuat jumlah milik kita berkurang, tetapi hati kita bahagia.', True, 'Berbagi menambah kebahagiaan.')]
P += [(3, 4, 'Ceritakan satu hal yang kamu bagi kepada temanmu dan hitung sisanya!')]

# ---------------- BAB 4 geometri
f(4, 1, 'Bangun datar yang memiliki tiga sisi dan tiga sudut adalah ....', 'segitiga', ['persegi', 'lingkaran', 'persegi panjang'])
f(4, 1, 'Bangun datar yang memiliki empat sisi sama panjang adalah ....', 'persegi', ['segitiga', 'lingkaran', 'persegi panjang'])
f(4, 1, 'Bangun datar yang memiliki empat sisi dengan dua pasang sisi sama panjang adalah ....', 'persegi panjang', ['segitiga', 'lingkaran', 'persegi'])
f(4, 1, 'Bangun datar yang tidak memiliki sudut adalah ....', 'lingkaran', ['segitiga', 'persegi', 'persegi panjang'])
f(4, 1, 'Banyak sisi pada segitiga adalah ....', '3', ['2', '4', '5'])
f(4, 1, 'Banyak sudut pada persegi adalah ....', '4', ['3', '5', '0'])
f(4, 1, 'Banyak sisi pada persegi panjang adalah ....', '4', ['3', '5', '6'])
f(4, 1, 'Segi lima memiliki ... sisi.', '5', ['3', '4', '6'])
f(4, 1, 'Segi enam memiliki ... sisi.', '6', ['4', '5', '8'])
f(4, 1, 'Bangun ruang yang bulat sempurna adalah ....', 'bola', ['kubus', 'balok', 'kerucut'])
f(4, 1, 'Bangun ruang yang semua sisinya berbentuk persegi adalah ....', 'kubus', ['balok', 'bola', 'kerucut'])
f(4, 1, 'Bangun ruang yang sisinya berbentuk persegi panjang adalah ....', 'balok', ['kubus', 'bola', 'kerucut'])
f(4, 1, 'Bangun ruang yang memiliki satu puncak dan alas berbentuk lingkaran adalah ....', 'kerucut', ['bola', 'kubus', 'balok'])
f(4, 1, 'Banyak sisi pada kubus adalah ....', '6', ['4', '8', '12'], diff='medium')
f(4, 1, 'Bangun ruang yang dapat menggelinding ke segala arah adalah ....', 'bola', ['kubus', 'balok', 'kerucut'], diff='medium')
f(4, 1, 'Bangun yang memiliki tebal, lebar, dan panjang disebut bangun ....', 'ruang', ['datar', 'garis', 'titik'], diff='medium')
f(4, 1, 'Bangun yang hanya memiliki panjang dan lebar disebut bangun ....', 'datar', ['ruang', 'bola', 'kubus'], diff='medium')
s(4, 1, 'Perhatikan gambar! Sebuah dadu bermain. Dadu berbentuk ....', 'Gambar dadu permainan menunjukkan bentuk', 'kubus', ['bola', 'kerucut', 'segitiga'], 'Dadu berbentuk kubus.', 'easy', 'Sebuah dadu putih dengan titik hitam di tiap sisinya, diletakkan di atas meja.')
s(4, 1, 'Perhatikan gambar! Sebuah topi ulang tahun berdiri di atas meja. Topi itu berbentuk ....', 'Gambar topi ulang tahun menunjukkan bentuk', 'kerucut', ['kubus', 'bola', 'balok'], 'Topi ulang tahun berbentuk kerucut.', 'easy', 'Sebuah topi ulang tahun berwarna-warni berdiri dengan ujung runcing ke atas.')
s(4, 1, 'Perhatikan gambar! Sebuah jam dinding bulat tergantung di dinding kelas. Bentuk wajah jam adalah ....', 'Gambar jam dinding menunjukkan bentuk wajah jam', 'lingkaran', ['persegi', 'segitiga', 'persegi panjang'], 'Wajah jam berbentuk lingkaran.', 'easy', 'Jam dinding berwajah bulat dengan angka 1-12 tergantung di dinding.')
s(4, 1, 'Dani membawa kotak pensil panjang berbentuk seperti kardus sepatu. Bentuknya ....', 'Kotak pensil Dani yang seperti kardus sepatu berbentuk', 'balok', ['kubus', 'bola', 'kerucut'], 'Kardus sepatu berbentuk balok.', 'medium')
T += [(4, 1, 'Lingkaran tidak memiliki sudut.', True, 'Lingkaran bulat tanpa sudut.'), (4, 1, 'Bola memiliki enam sisi datar.', False, 'Bola tidak memiliki sisi datar.'), (4, 1, 'Kubus memiliki enam sisi berbentuk persegi.', True, 'Sisi kubus semuanya persegi.')]
M += [(4, 1, 'Jodohkan bangun dengan ciri-cirinya!', [('segitiga', '3 sisi'), ('persegi', '4 sisi sama panjang'), ('lingkaran', 'tidak ada sudut'), ('persegi panjang', '2 pasang sisi sama panjang')], 'Ciri bangun datar.'),
      (4, 1, 'Jodohkan bangun ruang dengan ciri-cirinya!', [('bola', 'bulat sempurna'), ('kubus', '6 sisi persegi'), ('balok', 'sisi persegi panjang'), ('kerucut', 'ada puncak')], 'Ciri bangun ruang.')]
P += [(4, 1, 'Sebutkan tiga benda di kelas beserta bentuknya!'), (4, 1, 'Tunjukkan benda berbentuk bola, kubus, dan balok di sekitarmu!')]

f(4, 3, 'Dua segitiga yang sama dapat digabung menjadi ....', 'persegi atau persegi panjang', ['lingkaran', 'bola', 'kubus'], diff='medium')
f(4, 3, 'Persegi panjang dapat dibagi menjadi dua ....', 'persegi panjang yang lebih kecil', ['lingkaran', 'bola', 'kerucut'], diff='medium')
f(4, 3, 'Persegi dapat dibagi dua menurut diagonalnya menjadi dua ....', 'segitiga', ['lingkaran', 'persegi panjang', 'bola'], diff='medium')
f(4, 3, 'Menyusun beberapa bentuk menjadi gambar baru disebut ....', 'menyusun bentuk', ['menghapus bentuk', 'merobek bentuk', 'melipat angka'])
f(4, 3, 'Mengurai bentuk berarti ....', 'memecah menjadi bagian-bagian kecil', ['menggabungkan', 'mewarnai', 'menghitung'])
f(4, 3, 'Permainan yang menyusun potongan segitiga dan persegi menjadi gambar disebut ....', 'tangram', ['catur', 'ular tangga', 'congklak'], diff='medium')
f(4, 3, 'Untuk menyusun bentuk dengan baik kita harus ....', 'sabar dan tekun', ['terburu-buru', 'menyerah', 'marah'])
f(4, 3, 'Sikap sabar dan tekun saat menyusun bentuk adalah bentuk ikhtiar dalam ....', 'belajar dan mengembangkan potensi', ['bermain saja', 'malas', 'mengganggu'])
s(4, 3, 'Perhatikan gambar! Dua segitiga siku-siku yang sama digabung pada sisi miringnya. Bentuk yang terjadi adalah ....', 'Gambar dua segitiga siku-siku yang digabung pada sisi miring menunjukkan terbentuknya', 'persegi panjang atau persegi', ['lingkaran', 'bola', 'kubus'], 'Dua segitiga siku-siku sama dapat menjadi persegi/persegi panjang.', 'medium',
  'Dua segitiga siku-siku berwarna berbeda dirapatkan pada sisi miringnya menghasilkan bangun empat sisi.')
s(4, 3, 'Rafi mencoba menyusun tangram menjadi bentuk kelinci, tetapi belum berhasil. Sikap Rafi yang baik adalah ....', 'Karena belum berhasil menyusun tangram, Rafi', 'terus mencoba dengan sabar dan tekun', ['membuang tangram', 'menangis dan berhenti', 'menyalahkan temannya'], 'Sabar dan tekun sebagai ikhtiar.')
s(4, 3, 'Lia menyusun tujuh potongan bentuk menjadi gambar rumah. Hasilnya bagus. Ia mengucap ....', 'Setelah berhasil menyusun gambar rumah, Lia mengucap', 'alhamdulillah', ['astaghfirullah', 'innalillahi', 'tidak mengucap apa pun'], 'Bersyukur atas keberhasilan.', 'easy')
T += [(4, 3, 'Beberapa bentuk dapat disusun menjadi bentuk yang baru.', True, 'Komposisi bentuk.'), (4, 3, 'Mengurai bentuk berarti menggabungkan semua bentuk.', False, 'Mengurai = memecah.')]
O += [(4, 3, 'Urutkan langkah menyusun tangram menjadi gambar berikut!', ['Siapkan potongan tangram', 'Lihat contoh gambar', 'Susun potongan sedikit demi sedikit', 'Periksa hasil dan mengucap hamdalah'], 'Langkah menyusun tangram.')]
P += [(4, 3, 'Susun potongan segitiga dan persegi menjadi gambar rumah lalu ceritakan!'), (4, 3, 'Pecahkan sebuah persegi menjadi dua segitiga dengan melipat kertas!')]

# ---------------- BAB 5
f(5, 1, 'Alat untuk mengukur panjang benda adalah ....', 'penggaris', ['timbangan', 'jam', 'gelas ukur'])
f(5, 1, 'Alat ukur panjang yang digunakan oleh tukang untuk mengukur ruangan adalah ....', 'meteran', ['timbangan', 'termometer', 'jam'])
f(5, 1, 'Satuan tidak baku untuk mengukur panjang dengan telapak tangan terbuka adalah ....', 'jengkal', ['kilogram', 'liter', 'jam'])
f(5, 1, 'Satuan tidak baku yang diukur dengan melangkahkan kaki adalah ....', 'langkah', ['jengkal', 'depa', 'hasta'])
f(5, 1, 'Satuan tidak baku yang diukur dengan merentangkan kedua tangan adalah ....', 'depa', ['jengkal', 'langkah', 'klip'])
f(5, 1, 'Mengukur panjang meja dengan pensil disebut menggunakan satuan ....', 'tidak baku', ['baku', 'berat', 'waktu'])
f(5, 1, 'Ukuran jengkal setiap orang bisa ....', 'berbeda-beda', ['sama persis', 'selalu satu meter', 'tidak ada'], diff='medium')
f(5, 1, 'Saat mengukur dengan penggaris, ujung benda diletakkan sejajar dengan angka ....', 'nol', ['satu', 'sepuluh', 'dua puluh'], diff='medium')
f(5, 1, 'Benda yang dapat dipakai sebagai satuan tidak baku adalah ....', 'klip kertas', ['kilogram', 'liter', 'detik'])
f(5, 1, 'Panjang tali sebaiknya diukur dari ujung ke ....', 'ujung yang lain', ['tengah', 'pinggir saja', 'tidak diukur'])
s(5, 1, 'Perhatikan gambar! Seorang anak merentangkan kedua tangannya untuk mengukur lebar pintu. Satuan yang dipakai adalah ....', 'Gambar anak merentangkan kedua tangan untuk mengukur pintu memakai satuan', 'depa', ['jengkal', 'langkah', 'klip'], 'Merentangkan tangan = depa.', 'medium', 'Anak berdiri di depan pintu merentangkan kedua lengannya selebar mungkin.')
s(5, 1, 'Perhatikan gambar! Anak meletakkan ujung penggaris sejajar dengan ujung pensil. Alat yang dipakai adalah ....', 'Gambar anak mengukur pensil dengan alat panjang menunjukkan alat ukur', 'penggaris', ['timbangan', 'jam', 'gelas'], 'Penggaris mengukur panjang.', 'easy', 'Sebatang pensil sejajar dengan penggaris plastik, ujung pensil pada angka nol.')
T += [(5, 1, 'Jengkal dan langkah adalah satuan tidak baku.', True, 'Ukurannya berbeda-beda.'), (5, 1, 'Timbangan dipakai untuk mengukur panjang.', False, 'Timbangan mengukur berat.')]
M += [(5, 1, 'Jodohkan alat atau satuan dengan kegunaannya!', [('penggaris', 'mengukur panjang buku'), ('meteran', 'mengukur panjang ruangan'), ('jengkal', 'ukuran dengan telapak tangan'), ('langkah', 'ukuran dengan kaki')], 'Alat dan satuan panjang.')]
P += [(5, 1, 'Sebutkan tiga alat atau satuan untuk mengukur panjang dan tunjukkan cara memakainya!')]

f(5, 4, 'Mengukur dengan benar dan jujur menunjukkan sikap ....', 'bertanggung jawab', ['curang', 'malas', 'sombong'])
f(5, 4, 'Jika hasil mengukur ternyata salah, kita harus ....', 'mengukur ulang dengan teliti', ['membiarkannya', 'berbohong', 'menyalahkan teman'])
f(5, 4, 'Alat ukur setelah dipakai sebaiknya ....', 'disimpan kembali dengan rapi', ['dibuang', 'dirusak', 'diletakkan sembarangan'])
f(5, 4, 'Ilmu mengukur membantu kita ketika ....', 'membuat atau membeli sesuatu dengan ukuran tepat', ['bermimpi', 'tidur', 'bermain saja'])
s(5, 4, 'Ibu meminta Rani mengukur kain dengan jengkal. Hasilnya 8 jengkal. Rani mengukur dengan teliti dan melaporkan apa adanya. Sikap Rani adalah ....', 'Mengukur kain dan melaporkan hasil apa adanya, Rani menunjukkan sikap', 'bertanggung jawab dan jujur', ['malas', 'curang', 'ceroboh'], 'Bertanggung jawab.')
s(5, 4, 'Alif meminjam penggaris temannya untuk mengukur. Setelah selesai, Alif ....', 'Setelah memakai penggaris teman, Alif', 'mengembalikannya dengan ucapan terima kasih', ['menyimpannya', 'mematahkannya', 'meninggalkannya di lantai'], 'Bertanggung jawab atas barang pinjaman.', 'easy')
T += [(5, 4, 'Mengukur dengan teliti adalah wujud tanggung jawab.', True, 'Teliti dan bertanggung jawab.')]
P += [(5, 4, 'Ukur panjang bukumu dengan klip kertas dan laporkan hasilnya dengan jujur!')]

# ---------------- BAB 6 (selain generator)
f(6, 2, 'Bilangan 10 terdiri atas ... puluhan.', '1', ['0', '2', '10'])
f(6, 2, 'Bilangan 20 terdiri atas ... puluhan.', '2', ['1', '0', '20'])
f(6, 2, 'Nilai tempat pada bilangan dua angka dimulai dari kanan, yaitu ....', 'satuan lalu puluhan', ['puluhan lalu satuan', 'ratusan lalu satuan', 'ribuan'], diff='medium')
f(6, 2, 'Sepuluh satuan sama dengan ... puluhan.', '1', ['2', '10', '0'], diff='medium')
f(6, 4, 'Mengurutkan bilangan sampai 20 membantu kita ....', 'menghitung berurutan', ['melupakan angka', 'mengacak angka', 'tidur'])
s(6, 4, 'Bu guru meminta murid berbaris sesuai nomor 11 sampai 15. Nomor yang berada di depan nomor 13 adalah ....', 'Dalam barisan nomor 11 sampai 15, yang berada tepat di depan nomor 13', 'nomor 12', ['nomor 14', 'nomor 11', 'nomor 15'], 'Sebelum 13 adalah 12.', 'medium')
T += [(6, 4, 'Bilangan 15 lebih besar daripada 12.', True, '15 > 12.'), (6, 4, 'Bilangan 11 lebih besar daripada 18.', False, '11 < 18.')]

# ---------------- BAB 7
f(7, 1, 'Kalimat 8 + 5 = 13 adalah kalimat ....', 'matematika', ['tanya', 'seru', 'cerita'])
f(7, 1, 'Tanda "=" artinya ....', 'sama dengan', ['lebih dari', 'kurang dari', 'ditambah'])
f(7, 1, 'Penjumlahan sampai 20 berarti jumlah terbesar yang dihasilkan adalah ....', '20', ['10', '15', '100'])
f(7, 1, 'Penjumlahan 10 + 3 hasilnya ....', '13', ['12', '14', '103'])
f(7, 1, 'Pengurangan 15 - 10 hasilnya ....', '5', ['25', '10', '15'])
f(7, 1, 'Penjumlahan dan pengurangan adalah operasi ....', 'hitung', ['huruf', 'warna', 'bentuk'])
f(7, 1, 'Jika 9 + 3 = 12, maka 12 - 3 = ....', '9', ['3', '12', '15'], diff='medium')
f(7, 1, 'Jika 7 + 6 = 13, maka 13 - 6 = ....', '7', ['6', '13', '19'], diff='medium')
s(7, 1, 'Perhatikan gambar! 9 kelereng merah dan 4 kelereng biru digabung. Kalimat matematika yang sesuai adalah ....', 'Gambar 9 kelereng merah dan 4 biru yang digabung menunjukkan kalimat', '9 + 4 = 13', ['9 - 4 = 5', '9 + 4 = 12', '4 - 9 = 5'], '9 + 4 = 13.', 'medium', 'Sembilan kelereng merah dan empat kelereng biru dalam satu kantong.')
T += [(7, 1, 'Penjumlahan dan pengurangan dapat dilakukan sampai bilangan 20.', True, 'Sampai 20.'), (7, 1, '8 + 5 = 12.', False, '8 + 5 = 13.')]
M += [(7, 1, 'Jodohkan kalimat matematika dengan hasilnya!', [('10 + 5', '15'), ('12 + 3', '15'), ('17 - 2', '15'), ('20 - 5', '15')], 'Beberapa kalimat bisa berhasil sama.') if False else (7, 1, 'Jodohkan kalimat matematika dengan hasilnya!', [('10 + 5', '15'), ('12 + 6', '18'), ('17 - 2', '15') if False else ('17 - 5', '12'), ('20 - 5', '15') if False else ('20 - 8', '12')], 'Hasil operasi.') if False else (7, 1, 'Jodohkan kalimat matematika dengan hasilnya!', [('10 + 5', '15'), ('12 + 6', '18'), ('17 - 5', '12'), ('20 - 9', '11')], 'Hasil operasi.')]
f(7, 4, 'Menghitung uang jajan dengan jujur adalah sikap ....', 'terpuji', ['tercela', 'sia-sia', 'sombong'])
f(7, 4, 'Jika uang kembalian dari penjual lebih, kita ....', 'mengembalikannya', ['menyimpannya diam-diam', 'membelanjakannya', 'menyembunyikannya'])
s(7, 4, 'Zaki membeli kue 12 ribu... eh, ia membeli 12 kue untuk dibagi. Ia ingin makan lebih banyak, tetapi harus membagi 12 kue sama banyak kepada 2 anak. Sikap jujur dan adil adalah ....', 'Saat membagi 12 kue untuk 2 anak, Zaki', 'memberi masing-masing 6 kue', ['mengambil 8 kue untuk dirinya', 'menyembunyikan 4 kue', 'memberi 3 kue saja'], '12 : 2 = 6.') if False else None
s(7, 4, 'Aisyah memiliki 14 permen dan memberikan 5 permen kepada temannya. Ia menghitung sisa permennya dengan jujur. Sisa permen Aisyah adalah ....', 'Setelah memberi 5 dari 14 permen, Aisyah menghitung sisa permennya', '9 permen', ['8 permen', '10 permen', '19 permen'], '14 - 5 = 9.', 'medium')
s(7, 4, 'Umar dan Hana membantu penjual menghitung 8 jeruk dan 7 jeruk. Jumlahnya 15 jeruk. Sikap mereka yang baik adalah ....', 'Menghitung jeruk milik penjual, Umar dan Hana', 'menghitung teliti dan melaporkan apa adanya', ['menyembunyikan beberapa jeruk', 'asal menyebut jumlah', 'mengurangi jumlah agar dibayar lebih'], 'Jujur: 8 + 7 = 15.')
T += [(7, 4, 'Mengamalkan ilmu berhitung dengan jujur termasuk akhlak terpuji.', True, 'Jujur terpuji.')]
P += [(7, 4, 'Ceritakan penerapan penjumlahan atau pengurangan yang kamu lakukan dengan jujur di rumah!')]

# ---------------- BAB 8
f(8, 1, 'Cara menyajikan data dengan tanda garis kecil disebut ....', 'turus', ['piktogram', 'peta', 'peribahasa'])
f(8, 1, 'Cara menyajikan data dengan gambar disebut ....', 'piktogram', ['turus', 'peta', 'puisi'])
f(8, 1, 'Data adalah ....', 'keterangan yang dikumpulkan dan dihitung', ['mainan', 'makanan', 'alat tulis'])
f(8, 1, 'Dalam turus, lima tanda dikelompokkan agar ....', 'mudah dihitung', ['sulit dihitung', 'hilang', 'berwarna'])
f(8, 1, 'Pada piktogram, satu gambar mewakili ....', 'satu benda atau satu data', ['seribu benda', 'tidak ada', 'warna'])
f(8, 1, 'Data dapat disajikan dalam bentuk daftar, turus, dan ....', 'piktogram', ['peribahasa', 'lagu', 'cerita'])
f(8, 1, 'Sebelum menyajikan data kita harus ....', 'mengumpulkan dan menghitung data', ['menghapus data', 'melupakan data', 'membuang data'])
s(8, 1, 'Perhatikan gambar! Sebuah tabel berisi tanda | | | | | | pada baris "apel". Cara menyajikan data ini disebut ....', 'Gambar tabel dengan tanda garis kecil pada baris apel menunjukkan penyajian data dengan', 'turus', ['piktogram', 'diagram batang', 'peta'], 'Tanda garis kecil = turus.', 'medium', 'Tabel tiga baris (apel, jeruk, pisang) dengan tanda garis kecil di tiap baris.')
s(8, 1, 'Perhatikan gambar! Tabel yang menggunakan gambar buah kecil untuk menunjukkan jumlah buah. Cara menyajikan data ini disebut ....', 'Gambar tabel yang memakai gambar buah kecil menunjukkan penyajian data dengan', 'piktogram', ['turus', 'daftar angka', 'peta'], 'Gambar mewakili data = piktogram.', 'medium', 'Tabel buah: tiap baris diisi gambar buah kecil sesuai jumlahnya.')
T += [(8, 1, 'Turus dan piktogram adalah cara menyajikan data.', True, 'Dua cara menyajikan data.'), (8, 1, 'Data tidak perlu dihitung.', False, 'Data dihitung.')]
M += [(8, 1, 'Jodohkan cara penyajian data dengan cirinya!', [('turus', 'tanda garis kecil'), ('piktogram', 'gambar kecil'), ('daftar', 'tulisan dan angka'), ('tabel', 'baris dan kolom')], 'Cara menyajikan data.')]
G += [(8, 2, "Kelompokkan benda berikut: apel, jeruk, pensil, penghapus, pisang, penggaris.", {'buah': ['apel', 'jeruk', 'pisang'], 'alat tulis': ['pensil', 'penghapus', 'penggaris']}, 'Kelompokkan menurut jenisnya.'),
      (8, 2, "Kelompokkan hewan berikut: kucing, ikan, ayam, burung, kambing, lele.", {'hewan darat': ['kucing', 'ayam', 'kambing'], 'hewan yang bisa terbang atau berenang': ['ikan', 'burung', 'lele']}, 'Kelompokkan menurut ciri.') if False else (8, 2, "Kelompokkan hewan berikut: kucing, ikan, ayam, kambing, lele, sapi.", {'hewan darat': ['kucing', 'ayam', 'kambing', 'sapi'], 'hewan air': ['ikan', 'lele']}, 'Kelompokkan menurut tempat hidup.'),
      (8, 2, "Kelompokkan bentuk berikut: bola, kubus, lingkaran, persegi, balok, segitiga.", {'bangun ruang': ['bola', 'kubus', 'balok'], 'bangun datar': ['lingkaran', 'persegi', 'segitiga']}, 'Bangun ruang dan bangun datar.'),
      (8, 2, "Kelompokkan angka berikut: 2, 4, 6, 8, 3, 5, 7, 9.", {'bilangan genap': ['2', '4', '6', '8'], 'bilangan ganjil': ['3', '5', '7', '9']}, 'Genap dan ganjil.')]
f(8, 2, 'Mengelompokkan data berarti memisahkan data menurut ....', 'jenis atau cirinya', ['warnanya saja', 'acak', 'ukuran tulisan'])
f(8, 2, 'Untuk menghitung data dengan mudah, kita ....', 'mengelompokkan terlebih dahulu', ['mencampur semua', 'menghapus data', 'tidak menghitung'])
f(8, 2, 'Benda yang termasuk kelompok buah adalah ....', 'mangga', ['sapu', 'meja', 'buku'])
f(8, 2, 'Benda yang termasuk kelompok alat tulis adalah ....', 'pensil', ['jeruk', 'sendok', 'kursi'])
f(8, 2, 'Bola, kelereng, dan globe dapat dikelompokkan sebagai benda berbentuk ....', 'bola', ['kubus', 'balok', 'kerucut'])
s(8, 2, 'Perhatikan gambar! Di atas meja ada 3 apel, 2 jeruk, dan 4 pisang. Jika dikelompokkan menurut jenisnya, ada ... kelompok.', 'Gambar apel, jeruk, dan pisang yang dikelompokkan menurut jenisnya membentuk', '3 kelompok', ['2 kelompok', '4 kelompok', '9 kelompok'], 'Apel, jeruk, pisang = 3 kelompok.', 'medium', 'Meja berisi 3 apel, 2 jeruk, dan 4 pisang yang diletakkan terpisah.')
P += [(8, 2, 'Kelompokkan benda-benda di mejamu menurut jenis lalu hitung tiap kelompok!'), (8, 2, 'Kumpulkan data jenis baju temanmu hari ini lalu kelompokkan!')]
