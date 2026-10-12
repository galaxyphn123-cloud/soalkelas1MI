# -*- coding: utf-8 -*-
"""Data pendukung Bahasa Indonesia Kelas 1."""

# kalimat berdasarkan tanda baca akhir (TP tanda tanya/seru/titik)
TANYA = ['Siapa namamu', 'Di mana rumahmu', 'Apa warna bajumu', 'Kapan kamu bangun', 'Mengapa kamu tersenyum', 'Berapa jumlah bukumu',
         'Siapa yang membantu ibu', 'Apakah kamu sudah makan', 'Kamu belajar apa hari ini', 'Di mana ayah bekerja']
SERU = ['Aduh, kakiku sakit', 'Hore, kita menang', 'Awas, ada mobil', 'Wah, bunganya indah', 'Tolong, ada kebakaran', 'Cepat, bel sudah berbunyi',
        'Selamat, kamu juara', 'Hati-hati di jalan', 'Alhamdulillah, aku sembuh', 'Ayo, kita berdoa']
BERITA = ['Ibu memasak di dapur', 'Ayah membaca koran', 'Adik bermain bola', 'Aku belajar membaca', 'Kakak menyapu halaman', 'Burung terbang di langit',
          'Nenek menanam bunga', 'Aku mencuci tangan', 'Kami salat berjemaah', 'Bu guru menulis di papan']

# kalimat rumpang: (kalimat dengan ...., benar, [salah])
RUMPANG = [
 ('Ibu memasak nasi di ....', 'dapur', ['sekolah', 'kolam', 'langit']),
 ('Aku menulis dengan ....', 'pensil', ['sendok', 'piring', 'sapu']),
 ('Kakak membaca ....', 'buku', ['batu', 'kursi', 'sepatu']),
 ('Ikan hidup di ....', 'air', ['api', 'pasir kering', 'kandang']),
 ('Matahari terbit di pagi ....', 'hari', ['rumah', 'jalan', 'buku']),
 ('Sebelum makan aku mencuci ....', 'tangan', ['sepatu', 'pintu', 'lantai']),
 ('Burung terbang di ....', 'langit', ['dapur', 'kolam', 'lemari']),
 ('Aku memakai topi di ....', 'kepala', ['kaki', 'perut', 'tangan']),
 ('Kami salat di ....', 'masjid', ['pasar', 'kebun', 'kolam renang']),
 ('Ayam berkokok di ....', 'pagi hari', ['dalam lemari', 'bawah laut', 'atas bulan']),
 ('Adik minum ....', 'susu', ['pasir', 'batu', 'kertas']),
 ('Aku bersyukur kepada ....', 'Allah', ['sepatu', 'meja', 'pintu']),
 ('Aku melihat dengan ....', 'mata', ['telinga', 'hidung', 'tangan']),
 ('Aku mendengar dengan ....', 'telinga', ['mata', 'kaki', 'gigi']),
 ('Kucing suka makan ....', 'ikan', ['batu', 'kertas', 'kaca']),
 ('Hujan turun dari ....', 'langit', ['lantai', 'tanah', 'meja']),
 ('Petani menanam padi di ....', 'sawah', ['laut', 'kelas', 'pasar mobil']),
 ('Aku menggosok gigi dengan sikat ....', 'gigi', ['sepatu', 'baju', 'lantai']),
 ('Setelah belajar, aku merapikan ....', 'buku', ['hujan', 'awan', 'bintang']),
 ('Bu guru mengajar di ....', 'kelas', ['kolam', 'kebun binatang', 'dapur']),
 ('Ayah pergi ke kantor naik ....', 'motor', ['awan', 'bintang', 'pelangi']),
 ('Pada malam hari bulan dan bintang terlihat di ....', 'langit', ['sungai', 'kebun', 'dapur']),
]

# ungkapan: (situasi, ungkapan benar)
UNGKAPAN = [
 ('Kamu ingin lewat di depan orang yang sedang duduk.', 'permisi'),
 ('Kamu ingin masuk ke ruang guru.', 'permisi'),
 ('Kamu meminta ibu mengambilkan air minum.', 'tolong'),
 ('Kamu ingin teman meminjamkan pensil.', 'tolong'),
 ('Kamu tidak sengaja menginjak kaki temanmu.', 'maaf'),
 ('Kamu terlambat masuk kelas.', 'maaf'),
 ('Temanmu meminjamkan penghapus.', 'terima kasih'),
 ('Ibu memberimu bekal makan siang.', 'terima kasih'),
 ('Kamu ingin lewat di antara dua orang yang sedang berbincang.', 'permisi'),
 ('Kamu meminta bantuan kakak untuk mengikat tali sepatu.', 'tolong'),
 ('Kamu merusak mainan adikmu karena tidak sengaja.', 'maaf'),
 ('Bu guru memberimu hadiah karena rajin.', 'terima kasih'),
 ('Kamu mengetuk pintu rumah tetangga.', 'permisi'),
 ('Kamu ingin teman membantu membawa tas.', 'tolong'),
 ('Kamu menumpahkan air di meja temanmu.', 'maaf'),
 ('Nenek membantumu menyeberang jalan.', 'terima kasih'),
]
UNGKAPAN_FACT = {
 'permisi': 'dipakai untuk meminta izin lewat atau masuk',
 'tolong': 'dipakai untuk meminta bantuan dengan sopan',
 'maaf': 'dipakai ketika kita berbuat salah',
 'terima kasih': 'dipakai ketika kita menerima bantuan atau pemberian',
}

# bilangan
ANGKA = ['satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh']
OBJEK = [('apel', 'buah apel merah'), ('bola', 'bola berwarna-warni'), ('buku', 'buku tulis'), ('pensil', 'pensil berwarna'), ('burung', 'burung kecil'),
         ('bunga', 'bunga mawar'), ('ikan', 'ikan di kolam'), ('kursi', 'kursi kayu'), ('topi', 'topi biru'), ('layang-layang', 'layang-layang di langit')]

# arti kata baru: (kata, arti, kalimat contoh)
ARTI = [
 ('rajin', 'selalu bersungguh-sungguh', 'Andi rajin belajar.'), ('jujur', 'berkata dan berbuat apa adanya', 'Siti jujur kepada ibu.'),
 ('bersih', 'tidak kotor', 'Kelas kami bersih.'), ('rapi', 'tertata dengan baik', 'Buku di mejaku rapi.'),
 ('gembira', 'sangat senang', 'Adik gembira mendapat hadiah.'), ('tekun', 'rajin dan tidak mudah menyerah', 'Dina tekun berlatih menulis.'),
 ('sopan', 'baik dalam bersikap dan berbicara', 'Anak itu sopan kepada guru.'), ('dermawan', 'suka memberi kepada orang lain', 'Pak Haji dermawan.'),
 ('lelah', 'capek setelah bekerja', 'Ayah lelah sepulang kerja.'), ('sehat', 'tidak sakit', 'Badanku sehat.'),
 ('bangga', 'merasa senang dan hormat atas keberhasilan', 'Ibu bangga kepadaku.'), ('kuat', 'tidak mudah lemah', 'Badan Rafi kuat.'),
 ('hemat', 'tidak boros', 'Aku hemat menggunakan air.'), ('sabar', 'tahan menunggu dan tidak mudah marah', 'Kakak sabar menunggu giliran.'),
 ('indah', 'enak dilihat dan bagus', 'Pelangi itu indah.'), ('cita-cita', 'keinginan yang ingin dicapai', 'Cita-citaku menjadi dokter.'),
]

# arah & letak: (kalimat, kata_penunjuk_letak, deskripsi gambar)
LETAK = [
 ('Buku ada ... meja.', 'di atas', 'Sebuah buku diletakkan di atas meja kayu.'),
 ('Kucing tidur ... kursi.', 'di bawah', 'Seekor kucing tidur di bawah kursi.'),
 ('Tas ada ... kelas.', 'di dalam', 'Sebuah tas diletakkan di dalam ruang kelas.'),
 ('Sepatu ada ... rumah.', 'di luar', 'Sepasang sepatu diletakkan di luar pintu rumah.'),
 ('Pohon berada ... rumah.', 'di depan', 'Sebuah pohon besar berdiri di depan rumah.'),
 ('Kebun berada ... rumah.', 'di belakang', 'Sebuah kebun sayur terlihat di belakang rumah.'),
 ('Bola berada ... gawang.', 'di samping', 'Sebuah bola ada di samping tiang gawang.'),
 ('Lampu menggantung ... meja.', 'di atas', 'Sebuah lampu menggantung di atas meja makan.'),
 ('Sandal ada ... tempat tidur.', 'di bawah', 'Sepasang sandal ada di bawah tempat tidur.'),
 ('Ikan berenang ... kolam.', 'di dalam', 'Beberapa ikan berenang di dalam kolam.'),
]
ARAH = [
 ('Dari sekolah, masjid ada di sebelah ....', 'kanan', ['kiri', 'atas', 'bawah']),
 ('Mobil berhenti di lampu merah. Lampu merah artinya ....', 'berhenti', ['jalan terus', 'belok kiri', 'berlari']),
 ('Jika ingin ke taman, kamu berjalan ke arah ....', 'depan (lurus)', ['langit', 'bawah tanah', 'atap']),
 ('Tangan yang dipakai makan adalah tangan ....', 'kanan', ['kiri', 'atas', 'bawah']),
 ('Jantung manusia berada di dada sebelah ....', 'kiri', ['kanan', 'atas', 'bawah']),
 ('Saat berjalan di jalan, kita berjalan di sisi ....', 'tepi (pinggir) jalan', ['tengah jalan', 'atas jalan', 'tengah rel']),
 ('Untuk sampai ke pasar dari rumah, Pak Ali berbelok ke kanan. Berarti ia berbelok ke arah ....', 'tangan kanan', ['tangan kiri', 'belakang', 'atas']),
 ('Jika kamu menghadap depan, teman di sebelah tangan kirimu berada di sebelah ....', 'kiri', ['kanan', 'depan', 'belakang']),
]
PEKERJAAN = [
 ('guru', 'mengajar murid di sekolah', 'Seorang guru menjelaskan pelajaran di depan kelas.'),
 ('dokter', 'mengobati orang sakit', 'Seorang dokter memeriksa pasien dengan stetoskop.'),
 ('petani', 'menanam padi dan sayur', 'Seorang petani menanam padi di sawah.'),
 ('polisi', 'menjaga keamanan dan mengatur lalu lintas', 'Seorang polisi mengatur lalu lintas di perempatan.'),
 ('pedagang', 'menjual barang di pasar', 'Seorang pedagang menjual sayur di pasar.'),
 ('nelayan', 'menangkap ikan di laut', 'Seorang nelayan menarik jaring ikan dari perahu.'),
 ('sopir', 'mengemudikan kendaraan', 'Seorang sopir mengemudikan bus.'),
 ('pilot', 'menerbangkan pesawat', 'Seorang pilot duduk di kokpit pesawat.'),
 ('tukang kayu', 'membuat meja dan kursi', 'Seorang tukang kayu menggergaji papan.'),
 ('perawat', 'merawat orang sakit', 'Seorang perawat membantu pasien di rumah sakit.'),
 ('juru masak', 'memasak makanan', 'Seorang juru masak memasak di dapur restoran.'),
 ('penjahit', 'menjahit pakaian', 'Seorang penjahit menjahit baju dengan mesin jahit.'),
]

# cerita: (judul, teks, [(pertanyaan, benar, [salah])], kejadian (urut), (pesan_benar, [salah]))
CERITA = {
 'dani': ('Dani Suka Olahraga', 'Dani bangun pagi. Ia berdoa lalu mandi. Setelah itu Dani berlari di halaman bersama ayah. Badan Dani menjadi sehat dan kuat. Dani mengucap hamdalah.',
  [('Siapa yang berlari bersama Dani?', 'ayah', ['ibu', 'kakak', 'adik']), ('Apa yang Dani lakukan setelah bangun pagi?', 'berdoa lalu mandi', ['bermain gawai', 'tidur lagi', 'makan permen']),
   ('Di mana Dani berlari?', 'di halaman', ['di kelas', 'di kolam', 'di dapur']), ('Apa yang Dani ucapkan di akhir cerita?', 'hamdalah', ['basmalah', 'taawuz', 'salam'])],
  ['Dani bangun pagi', 'Dani berdoa dan mandi', 'Dani berlari bersama ayah', 'Dani mengucap hamdalah'], ('Berolahraga membuat badan sehat dan kuat', ['Berolahraga membuat badan lelah saja', 'Olahraga tidak penting', 'Lebih baik tidur seharian'])),
 'sinta': ('Sinta Makan Sayur', 'Sinta tidak suka makan sayur. Ibu berkata sayur membuat badan sehat. Sinta mencoba makan bayam. Ternyata rasanya enak. Sejak itu Sinta makan sayur setiap hari.',
  [('Apa yang tidak disukai Sinta pada awalnya?', 'sayur', ['buah', 'susu', 'nasi']), ('Sayur apa yang dicoba Sinta?', 'bayam', ['wortel', 'kentang', 'jagung']),
   ('Apa kata ibu tentang sayur?', 'membuat badan sehat', ['membuat gemuk saja', 'tidak enak', 'mahal']), ('Bagaimana rasa bayam menurut Sinta?', 'enak', ['pahit sekali', 'asin', 'tidak berasa'])],
  ['Sinta tidak suka sayur', 'Ibu menasihati Sinta', 'Sinta mencoba makan bayam', 'Sinta makan sayur setiap hari'], ('Makan sayur menyehatkan badan', ['Sayur harus dijauhi', 'Hanya makan permen', 'Makan sayur membuat sakit'])),
 'keluarga': ('Keluargaku', 'Ayah bekerja di kantor. Ibu memasak di dapur. Kakak membantu ibu. Adik bermain dengan boneka. Sore hari kami makan bersama.',
  [('Siapa yang memasak di dapur?', 'ibu', ['ayah', 'kakak', 'adik']), ('Di mana ayah bekerja?', 'di kantor', ['di sawah', 'di pasar', 'di sekolah']),
   ('Apa yang dilakukan adik?', 'bermain dengan boneka', ['membantu ibu', 'memasak', 'membaca koran']), ('Kapan keluarga makan bersama?', 'sore hari', ['pagi hari', 'tengah malam', 'siang hari saja'])],
  ['Ayah bekerja di kantor', 'Ibu memasak di dapur', 'Kakak membantu ibu', 'Keluarga makan bersama'], ('Keluarga yang saling membantu dan berkumpul hidup rukun', ['Setiap orang sibuk sendiri', 'Keluarga tidak perlu bersama', 'Anak tidak perlu membantu'])),
 'lani': ('Lani Membantu Ibu', 'Lani melihat ibu mencuci piring. Lani ingin membantu. Ia mengelap meja dan menyapu lantai. Ibu tersenyum dan berkata terima kasih. Lani merasa senang.',
  [('Apa yang sedang dilakukan ibu?', 'mencuci piring', ['memasak nasi', 'menyapu', 'membaca']), ('Apa yang Lani lakukan untuk membantu?', 'mengelap meja dan menyapu lantai', ['bermain boneka', 'menonton televisi', 'tidur']),
   ('Apa kata ibu kepada Lani?', 'terima kasih', ['maaf', 'permisi', 'selamat tinggal']), ('Bagaimana perasaan Lani?', 'senang', ['sedih', 'marah', 'takut'])],
  ['Lani melihat ibu mencuci piring', 'Lani ingin membantu', 'Lani mengelap meja dan menyapu', 'Ibu berterima kasih'], ('Membantu orang tua membuat hati senang', ['Membantu itu melelahkan', 'Anak tidak perlu membantu', 'Hanya orang dewasa yang bekerja'])),
 'bimo': ('Bimo dan Sampah', 'Bimo makan roti di taman. Bungkus roti ia masukkan ke tempat sampah. Teman Bimo melihat dan ikut membuang sampah. Taman menjadi bersih.',
  [('Di mana Bimo makan roti?', 'di taman', ['di kelas', 'di dapur', 'di pasar']), ('Ke mana bungkus roti dibuang?', 'ke tempat sampah', ['ke sungai', 'ke lantai', 'ke kebun']),
   ('Apa yang dilakukan teman Bimo?', 'ikut membuang sampah pada tempatnya', ['mengejek Bimo', 'pulang', 'bermain bola']), ('Bagaimana keadaan taman akhirnya?', 'bersih', ['kotor', 'gelap', 'sepi'])],
  ['Bimo makan roti di taman', 'Bimo membuang bungkus ke tempat sampah', 'Teman Bimo ikut membuang sampah', 'Taman menjadi bersih'], ('Membuang sampah pada tempatnya menjaga kebersihan', ['Sampah boleh dibuang di mana saja', 'Taman tidak perlu bersih', 'Bungkus roti harus disimpan di jalan'])),
 'raka': ('Cuci Tangan', 'Raka bermain bola di lapangan. Tangannya kotor. Sebelum makan, Raka mencuci tangan dengan sabun. Ia membilasnya dengan air bersih. Tangan Raka bersih dan wangi.',
  [('Apa yang Raka mainkan?', 'bola', ['layang-layang', 'boneka', 'mobil-mobilan']), ('Mengapa Raka mencuci tangan?', 'tangannya kotor dan akan makan', ['ingin bermain air', 'disuruh teman', 'tidak ada alasan']),
   ('Apa yang dipakai Raka untuk mencuci tangan?', 'sabun dan air', ['pasir', 'pewarna', 'minyak']), ('Bagaimana tangan Raka setelah dicuci?', 'bersih dan wangi', ['kotor', 'basah dan bau', 'luka'])],
  ['Raka bermain bola', 'Tangan Raka kotor', 'Raka mencuci tangan dengan sabun', 'Tangan Raka bersih dan wangi'], ('Kebersihan sebagian dari iman', ['Tangan kotor tidak masalah', 'Mencuci tangan membuang waktu', 'Bermain bola dilarang'])),
 'tia': ('Bermain Bersama', 'Tia dan Rani bermain petak umpet. Tia ingin lewat, lalu berkata permisi. Rani tidak sengaja menabrak Tia dan berkata maaf. Tia menjawab tidak apa-apa. Mereka bermain lagi dengan gembira.',
  [('Permainan apa yang dimainkan Tia dan Rani?', 'petak umpet', ['sepak bola', 'bola basket', 'lompat tali']), ('Apa yang Tia ucapkan saat ingin lewat?', 'permisi', ['maaf', 'tolong', 'terima kasih']),
   ('Apa yang Rani ucapkan setelah menabrak Tia?', 'maaf', ['permisi', 'tolong', 'selamat pagi']), ('Bagaimana akhir cerita?', 'mereka bermain lagi dengan gembira', ['mereka bertengkar', 'mereka pulang menangis', 'mereka berhenti berteman'])],
  ['Tia dan Rani bermain petak umpet', 'Tia berkata permisi', 'Rani berkata maaf', 'Mereka bermain lagi'], ('Ungkapan permisi dan maaf membuat pergaulan menjadi santun', ['Tidak perlu meminta maaf', 'Bermain harus menabrak teman', 'Lewat tanpa permisi itu sopan'])),
 'rumah': ('Rumahku Surgaku', 'Di rumah ada ayah, ibu, dan dua adik. Kami salat berjemaah. Sesudah itu kami makan bersama. Rumahku terasa damai.',
  [('Berapa adik dalam cerita?', 'dua', ['satu', 'tiga', 'empat']), ('Apa yang dilakukan keluarga bersama-sama?', 'salat berjemaah dan makan bersama', ['bermain di luar', 'menonton film', 'bertengkar']),
   ('Siapa saja anggota keluarga yang disebut?', 'ayah, ibu, dan dua adik', ['ayah dan ibu saja', 'kakek dan nenek', 'paman dan bibi']), ('Bagaimana rasa rumah dalam cerita?', 'damai', ['bising', 'gelap', 'menyeramkan'])],
  ['Keluarga salat berjemaah', 'Keluarga makan bersama', 'Rumah terasa damai'], ('Keluarga yang beribadah bersama hidup damai', ['Beribadah sendiri-sendiri lebih baik', 'Rumah harus ramai', 'Tidak perlu makan bersama'])),
 'ikan': ('Ikan di Kolam', 'Ada lima ikan di kolam. Dua ikan berenang ke kiri. Tiga ikan berenang ke kanan. Ibu memberi makan ikan-ikan itu.',
  [('Berapa ikan yang ada di kolam?', 'lima', ['dua', 'tiga', 'sepuluh']), ('Berapa ikan yang berenang ke kiri?', 'dua', ['tiga', 'lima', 'satu']),
   ('Berapa ikan yang berenang ke kanan?', 'tiga', ['dua', 'empat', 'lima']), ('Siapa yang memberi makan ikan?', 'ibu', ['ayah', 'kakak', 'adik'])],
  ['Ada lima ikan di kolam', 'Dua ikan berenang ke kiri', 'Tiga ikan berenang ke kanan', 'Ibu memberi makan ikan'], ('Kita harus menyayangi hewan peliharaan', ['Hewan tidak perlu diberi makan', 'Ikan hanya untuk dimainkan', 'Kolam tidak perlu dirawat'])),
 'salma': ('Hari Pertama Sekolah', 'Hari ini Salma masuk sekolah. Ia bertemu bu guru dan teman baru. Bu guru mengajar membaca. Salma belajar dengan senang.',
  [('Siapa yang masuk sekolah?', 'Salma', ['Dani', 'Rani', 'Lani']), ('Siapa yang ditemui Salma di sekolah?', 'bu guru dan teman baru', ['hanya ayah', 'hanya kakak', 'penjual jajanan']),
   ('Apa yang diajarkan bu guru?', 'membaca', ['menyanyi', 'berenang', 'memasak']), ('Bagaimana perasaan Salma?', 'senang', ['takut', 'marah', 'malas'])],
  ['Salma masuk sekolah', 'Salma bertemu bu guru dan teman baru', 'Bu guru mengajar membaca', 'Salma belajar dengan senang'], ('Belajar di sekolah menyenangkan', ['Sekolah menakutkan', 'Belajar itu membosankan', 'Tidak perlu bertemu teman'])),
 'kata': ('Kata Baru', 'Salma mendengar kata rajin. Ia bertanya kepada bu guru. Bu guru menjawab rajin berarti selalu bersungguh-sungguh. Salma mencatat arti kata itu.',
  [('Kata baru apa yang didengar Salma?', 'rajin', ['jujur', 'bersih', 'gembira']), ('Kepada siapa Salma bertanya?', 'bu guru', ['ibu', 'teman', 'penjaga sekolah']),
   ('Apa arti rajin menurut bu guru?', 'selalu bersungguh-sungguh', ['suka tidur', 'suka bermain', 'suka marah']), ('Apa yang dilakukan Salma setelah tahu artinya?', 'mencatat arti kata', ['melupakannya', 'menyobek buku', 'bermain'])],
  ['Salma mendengar kata baru', 'Salma bertanya kepada bu guru', 'Bu guru menjelaskan artinya', 'Salma mencatat arti kata'], ('Bertanya dan mencatat membantu kita menambah kata baru', ['Malu bertanya itu baik', 'Kata baru dilupakan saja', 'Tidak perlu mencatat'])),
 'pos': ('Pak Pos', 'Pak Pos mengantar surat ke rumah Pak RT. Rumah Pak RT ada di sebelah masjid. Pak Pos berbelok ke kanan lalu berhenti. Ia mengetuk pintu dan memberi salam.',
  [('Apa pekerjaan Pak Pos?', 'mengantar surat', ['menanam padi', 'menangkap ikan', 'mengajar']), ('Rumah Pak RT ada di sebelah ....', 'masjid', ['sekolah', 'pasar', 'taman']),
   ('Pak Pos berbelok ke arah ....', 'kanan', ['kiri', 'belakang', 'atas']), ('Apa yang Pak Pos lakukan di depan rumah?', 'mengetuk pintu dan memberi salam', ['langsung masuk', 'berteriak', 'pulang'])],
  ['Pak Pos membawa surat', 'Pak Pos berbelok ke kanan', 'Pak Pos berhenti di rumah Pak RT', 'Pak Pos mengetuk pintu dan memberi salam'], ('Setiap pekerjaan baik itu mulia', ['Pekerjaan harus dipandang rendah', 'Hanya dokter yang penting', 'Surat tidak berguna'])),
 'pasar': ('Di Pasar', 'Ibu pergi ke pasar bersama Dina. Pedagang ikan berada di sebelah kiri. Pedagang sayur ada di depan. Ibu membeli bayam dan berkata terima kasih.',
  [('Ke mana ibu dan Dina pergi?', 'ke pasar', ['ke sekolah', 'ke masjid', 'ke kebun binatang']), ('Pedagang ikan berada di sebelah ....', 'kiri', ['kanan', 'belakang', 'atas']),
   ('Apa yang dibeli ibu?', 'bayam', ['ikan', 'apel', 'baju']), ('Apa yang ibu ucapkan kepada pedagang?', 'terima kasih', ['maaf', 'permisi', 'tolong'])],
  ['Ibu dan Dina pergi ke pasar', 'Ibu melihat pedagang ikan dan sayur', 'Ibu membeli bayam', 'Ibu mengucap terima kasih'], ('Berterima kasih adalah sikap yang santun', ['Pedagang tidak perlu dihargai', 'Tidak perlu berterima kasih', 'Pasar tempat bermain'])),
 'hewan': ('Gerakan Hewan', 'Kelinci melompat-lompat. Gajah berjalan pelan. Burung mengepakkan sayap. Ikan berenang di air. Anak-anak menirukan gerakan hewan itu.',
  [('Bagaimana gerakan kelinci?', 'melompat-lompat', ['berenang', 'terbang', 'merayap']), ('Hewan apa yang berenang?', 'ikan', ['gajah', 'kelinci', 'burung']),
   ('Apa yang dilakukan burung?', 'mengepakkan sayap', ['melompat', 'berenang', 'berjalan pelan']), ('Apa yang dilakukan anak-anak?', 'menirukan gerakan hewan', ['pergi tidur', 'menggambar saja', 'menangis'])],
  ['Kelinci melompat', 'Gajah berjalan pelan', 'Burung mengepakkan sayap', 'Anak-anak menirukan gerakan'], ('Menirukan gerakan menyenangkan dan melatih tubuh', ['Menirukan gerakan itu berbahaya', 'Gerakan tidak boleh ditiru', 'Anak harus duduk diam'])),
}
