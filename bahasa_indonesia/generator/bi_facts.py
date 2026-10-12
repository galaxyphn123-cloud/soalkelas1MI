# -*- coding: utf-8 -*-
"""Fakta, skenario, dan tugas tulisan tangan Bahasa Indonesia. Kunci: (bab, nomor TP dalam bab)."""
R = 'Dinilai guru: ketepatan, kelancaran, dan kesantunan (skala 1-4).'
F = []     # (bab, tp, stem '....', benar, [salah], penjelasan, kesulitan)
S = []     # (bab, tp, panjang, awalan, benar, [salah], penjelasan, kesulitan, visual)
T = []     # (bab, tp, pernyataan, benar?, penjelasan)
P = []     # (bab, tp, tugas)
G = []     # (bab, tp, soal, {kelompok: [item]}, penjelasan)
O = []     # (bab, tp, soal, [urut], penjelasan)
M = []     # (bab, tp, soal, [(kiri, kanan)], penjelasan)

def f(b, t, stem, ok, bad, expl='', diff='easy'): F.append((b, t, stem, ok, bad, expl or f'Jawaban: {ok}.', diff))
def s(b, t, long, short, ok, bad, expl, diff='easy', vis=None): S.append((b, t, long, short, ok, bad, expl, diff, vis))

# ===================================================================== BAB 1: Aku Ciptaan Allah Swt. yang Sempurna
# 1.1 cara membaca dan menulis
f(1, 1, 'Kita membaca tulisan dari arah ....', 'kiri ke kanan', ['kanan ke kiri', 'bawah ke atas', 'tengah ke pinggir'])
f(1, 1, 'Kita menulis huruf dalam satu baris dari arah ....', 'kiri ke kanan', ['kanan ke kiri', 'atas ke bawah saja', 'bawah ke atas'])
f(1, 1, 'Huruf pertama pada awal kalimat ditulis dengan huruf ....', 'kapital (besar)', ['kecil', 'miring saja', 'tebal saja'])
f(1, 1, 'Nama orang ditulis diawali huruf ....', 'kapital (besar)', ['kecil', 'angka', 'bebas'])
f(1, 1, 'Antara dua kata dalam kalimat diberi ....', 'jarak (spasi)', ['gambar', 'angka', 'warna'])
f(1, 1, 'Saat menulis, kita duduk dengan ....', 'tegak dan tenang', ['membungkuk sekali', 'berbaring', 'berdiri di atas kursi'])
f(1, 1, 'Pensil dipegang dengan ....', 'tiga jari secara nyaman', ['kepalan tangan', 'seluruh telapak', 'kaki'])
f(1, 1, 'Gabungan huruf yang diucapkan sekali ucap disebut ....', 'suku kata', ['kalimat', 'paragraf', 'angka'])
f(1, 1, 'Gabungan beberapa suku kata yang bermakna disebut ....', 'kata', ['huruf', 'angka', 'gambar'])
f(1, 1, 'Gabungan kata yang membentuk pikiran lengkap disebut ....', 'kalimat', ['huruf', 'suku kata', 'angka'])
f(1, 1, 'Banyaknya huruf dalam abjad bahasa Indonesia adalah ... huruf.', '26', ['24', '28', '30'])
f(1, 1, 'Huruf pertama dalam abjad adalah ....', 'a', ['b', 'z', 'm'])
f(1, 1, 'Huruf terakhir dalam abjad adalah ....', 'z', ['a', 'y', 'x'])
f(1, 1, 'Bentuk huruf kapital dari "b" adalah ....', 'B', ['d', 'p', 'q'])
f(1, 1, 'Tulisan yang rapi akan mudah ....', 'dibaca', ['hilang', 'dihapus', 'dilupakan'], diff='medium')
f(1, 1, 'Sebelum belajar membaca dan menulis, kita membaca ....', 'basmalah', ['takbir saja', 'lagu', 'tidak membaca apa pun'])
s(1, 1, 'Dina ingin menulis namanya. Huruf pertama nama Dina sebaiknya ditulis ....', 'Saat menulis namanya, Dina menulis huruf pertama dengan', 'huruf kapital', ['huruf kecil saja', 'angka', 'gambar'], 'Nama diawali huruf kapital.')
s(1, 1, 'Raka membaca buku. Ia membaca dari arah ....', 'Raka membaca buku dari', 'kiri ke kanan', ['kanan ke kiri', 'bawah ke atas', 'tengah ke tepi'], 'Membaca dari kiri ke kanan.')
s(1, 1, 'Bu guru berkata, "Tulislah dengan rapi." Sikap Lia adalah ....', 'Menanggapi bu guru, Lia', 'menulis dengan rapi dan pelan', ['menulis asal-asalan', 'mencoret buku', 'menulis sambil berlari'], 'Menulis rapi mudah dibaca.')
s(1, 1, 'Perhatikan gambar! Seorang anak duduk tegak menghadap meja dan memegang pensil dengan benar. Sikap anak itu menunjukkan ....', 'Gambar anak duduk tegak dan memegang pensil dengan benar menunjukkan sikap', 'menulis yang baik', ['bermain', 'malas belajar', 'mengantuk'], 'Duduk tegak dan memegang pensil benar.', 'easy',
  'Anak perempuan duduk tegak di meja belajar, memegang pensil dengan tiga jari, buku bergaris terbuka di depannya.')
T += [(1, 1, 'Kita menulis dari kiri ke kanan.', True, 'Arah menulis huruf latin.'), (1, 1, 'Nama orang ditulis dengan huruf kecil semua.', False, 'Nama diawali huruf kapital.'),
      (1, 1, 'Kalimat diawali dengan huruf kapital.', True, 'Awal kalimat huruf kapital.'), (1, 1, 'Abjad bahasa Indonesia terdiri atas 26 huruf.', True, 'Ada 26 huruf.')]
P += [(1, 1, 'Tulislah namamu dengan huruf kapital di awal dan tulisan yang rapi!'), (1, 1, 'Bacalah satu kalimat pendek dari buku dengan lafal yang jelas!')]
O += [(1, 1, 'Urutkan satuan tulisan dari yang paling kecil!', ['huruf', 'suku kata', 'kata', 'kalimat'], 'Huruf, suku kata, kata, kalimat.'),
      (1, 1, 'Urutkan huruf berikut menurut abjad!', ['a', 'd', 'k', 'z'], 'a, d, k, z.')]

# 1.2 huruf vokal dan konsonan
f(1, 2, 'Huruf vokal berjumlah ... huruf.', '5', ['3', '4', '21'])
f(1, 2, 'Huruf vokal adalah ....', 'a, i, u, e, o', ['b, c, d, f, g', 'a, b, c, d, e', 'k, l, m, n, o'])
f(1, 2, 'Huruf selain vokal disebut huruf ....', 'konsonan', ['kapital', 'angka', 'miring'])
f(1, 2, 'Banyaknya huruf konsonan adalah ... huruf.', '21', ['5', '26', '10'], diff='medium')
f(1, 2, 'Pada kata "ibu" terdapat dua huruf vokal, yaitu ....', 'i dan u', ['b dan u', 'i dan b', 'u dan b'])
f(1, 2, 'Huruf vokal pertama dalam abjad adalah ....', 'a', ['b', 'e', 'o'])
f(1, 2, 'Huruf konsonan pertama dalam abjad adalah ....', 'b', ['a', 'c', 'e'], diff='medium')
f(1, 2, 'Kata yang hanya memiliki satu huruf vokal adalah ....', 'tas', ['ibu', 'bola', 'kuda'], diff='medium')
s(1, 2, 'Rani menulis huruf "o" di papan tulis. Huruf "o" termasuk huruf ....', 'Huruf "o" yang ditulis Rani termasuk huruf', 'vokal', ['konsonan', 'kapital', 'angka'], 'o adalah huruf vokal.')
s(1, 2, 'Bu guru menunjuk huruf "m". Huruf "m" termasuk huruf ....', 'Huruf "m" yang ditunjuk bu guru termasuk huruf', 'konsonan', ['vokal', 'angka', 'tanda baca'], 'm adalah konsonan.')
T += [(1, 2, 'Huruf a, i, u, e, o adalah huruf vokal.', True, 'Lima huruf vokal.'), (1, 2, 'Huruf b termasuk huruf vokal.', False, 'b adalah konsonan.')]
G += [(1, 2, "Kelompokkan huruf berikut: a, b, c, e, i, k, o, t.", {'vokal': ['a', 'e', 'i', 'o'], 'konsonan': ['b', 'c', 'k', 't']}, 'Vokal: a, i, u, e, o.')]
P += [(1, 2, 'Sebutkan lima huruf vokal secara berurutan dengan lantang!'), (1, 2, 'Tunjukkan huruf vokal pada kata "kucing" di papan tulis!')]

# 1.4 anggota tubuh & syukur
f(1, 4, 'Kita melihat tulisan dengan ....', 'mata', ['telinga', 'hidung', 'kaki'])
f(1, 4, 'Kita mendengar suara bu guru dengan ....', 'telinga', ['mata', 'tangan', 'gigi'])
f(1, 4, 'Kita membaca keras-keras dengan ....', 'mulut', ['mata saja', 'telinga', 'hidung'])
f(1, 4, 'Kita menulis dengan ....', 'tangan', ['kaki', 'hidung', 'telinga'])
f(1, 4, 'Kita berpikir dan mengingat pelajaran dengan ....', 'otak', ['jari', 'gigi', 'lutut'])
f(1, 4, 'Kita berjalan ke sekolah dengan ....', 'kaki', ['mata', 'tangan', 'telinga'])
f(1, 4, 'Kita mencium bau harum bunga dengan ....', 'hidung', ['mata', 'telinga', 'jari'])
f(1, 4, 'Allah menciptakan manusia dengan bentuk yang ....', 'sempurna', ['buruk', 'kurang', 'rusak'])
f(1, 4, 'Menggunakan anggota tubuh untuk belajar dengan sungguh-sungguh adalah wujud ... kepada Allah.', 'syukur', ['marah', 'malas', 'sombong'])
f(1, 4, 'Ucapan syukur kepada Allah adalah ....', 'alhamdulillah', ['astaghfirullah', 'innalillahi', 'bismillah'])
f(1, 4, 'Anggota tubuh harus kita jaga dan gunakan untuk hal ....', 'yang baik', ['yang buruk', 'yang berbahaya', 'yang sia-sia'])
f(1, 4, 'Yang kita pakai untuk memegang pensil adalah ....', 'jari', ['kaki', 'telinga', 'hidung'])
s(1, 4, 'Dani mendengarkan bu guru bercerita dengan telinganya. Sikap Dani adalah ....', 'Saat bu guru bercerita, Dani', 'mendengarkan dengan saksama sebagai wujud syukur', ['mengobrol', 'menutup telinga', 'bermain'], 'Menggunakan telinga untuk belajar.')
s(1, 4, 'Lani menulis dengan tangannya dengan rapi. Ini wujud syukur karena Lani ....', 'Menulis dengan rapi, Lani', 'menggunakan tangannya untuk belajar dengan sungguh-sungguh', ['mencoret-coret meja', 'memukul teman', 'merusak buku'], 'Tangan dipakai untuk kebaikan.')
s(1, 4, 'Setelah membaca dengan lancar, Fikri mengucap ....', 'Setelah lancar membaca, Fikri mengucap', 'alhamdulillah', ['astaghfirullah', 'innalillahi', 'tidak mengucap apa pun'], 'Bersyukur atas kemampuan.')
s(1, 4, 'Perhatikan gambar! Seorang anak membaca buku dengan mata yang fokus pada tulisan. Anggota tubuh yang dipakai adalah ....', 'Gambar anak membaca buku menunjukkan anggota tubuh yang dipakai untuk membaca adalah', 'mata', ['telinga', 'hidung', 'kaki'], 'Membaca memakai mata.', 'easy',
  'Anak laki-laki duduk di bangku membaca buku cerita bergambar dengan tatapan fokus pada halaman.')
s(1, 4, 'Perhatikan gambar! Seorang anak mendengarkan guru bercerita sambil tersenyum dan tangan di pangkuan. Anggota tubuh yang dipakai untuk menyimak adalah ....', 'Gambar anak mendengarkan cerita guru menunjukkan anggota tubuh yang dipakai untuk menyimak adalah', 'telinga', ['mata', 'tangan', 'kaki'], 'Menyimak memakai telinga.', 'easy',
  'Guru bercerita di depan kelas, seorang anak duduk rapi mendengarkan sambil tersenyum.')
T += [(1, 4, 'Mata, telinga, dan tangan adalah anggota tubuh ciptaan Allah.', True, 'Semua anggota tubuh ciptaan Allah.'), (1, 4, 'Anggota tubuh boleh dipakai untuk mengganggu teman.', False, 'Dipakai untuk kebaikan.')]
G += [(1, 4, "Kelompokkan anggota tubuh berikut dengan kegunaannya: mata, telinga, tangan, mulut.", {'melihat': ['mata'], 'mendengar': ['telinga'], 'menulis': ['tangan'], 'membaca keras dan berbicara': ['mulut']}, 'Kegunaan anggota tubuh.')]
M += [(1, 4, 'Jodohkan anggota tubuh dengan kegunaannya!', [('mata', 'melihat'), ('telinga', 'mendengar'), ('tangan', 'menulis'), ('kaki', 'berjalan')], 'Kegunaan anggota tubuh.')]
P += [(1, 4, 'Sebutkan lima anggota tubuh dan kegunaannya untuk belajar membaca dan menulis!'), (1, 4, 'Ucapkan alhamdulillah dan ceritakan satu hal yang kamu syukuri tentang tubuhmu!')]

# ===================================================================== BAB 2: Badanku Sehat dan Kuat
# 2.3 tanda tanya & seru (fakta tambahan)
f(2, 3, 'Kalimat tanya diakhiri dengan tanda ....', 'tanya (?)', ['seru (!)', 'titik (.)', 'koma (,)'])
f(2, 3, 'Kalimat seru diakhiri dengan tanda ....', 'seru (!)', ['tanya (?)', 'titik (.)', 'koma (,)'])
f(2, 3, 'Tanda "?" disebut tanda ....', 'tanya', ['seru', 'titik', 'koma'])
f(2, 3, 'Tanda "!" disebut tanda ....', 'seru', ['tanya', 'titik', 'petik'])
f(2, 3, 'Kata tanya yang dipakai untuk menanyakan orang adalah ....', 'siapa', ['di mana', 'kapan', 'berapa'], diff='medium')
f(2, 3, 'Kata tanya yang dipakai untuk menanyakan tempat adalah ....', 'di mana', ['siapa', 'kapan', 'berapa'], diff='medium')
f(2, 3, 'Kata tanya yang dipakai untuk menanyakan jumlah adalah ....', 'berapa', ['siapa', 'di mana', 'mengapa'], diff='medium')
f(2, 3, 'Kata tanya yang dipakai untuk menanyakan waktu adalah ....', 'kapan', ['siapa', 'di mana', 'berapa'], diff='medium')
f(2, 3, 'Kalimat seru dipakai untuk menyatakan ....', 'perasaan atau perintah yang kuat', ['pertanyaan', 'jumlah', 'nama'], diff='medium')
G += [(2, 3, "Kelompokkan kalimat berikut: 'Siapa namamu?'; 'Aduh, sakit!'; 'Di mana rumahmu?'; 'Hore, menang!'.", {'kalimat tanya': ['Siapa namamu?', 'Di mana rumahmu?'], 'kalimat seru': ['Aduh, sakit!', 'Hore, menang!']}, 'Tanda ? untuk tanya, ! untuk seru.')]
P += [(2, 3, 'Tulislah satu kalimat tanya dan satu kalimat seru dengan tanda baca yang benar!'), (2, 3, 'Ucapkan kalimat tanya dengan nada naik dan kalimat seru dengan nada kuat!')]

# 2.5 menerapkan ilmu / syukur
f(2, 5, 'Badan yang sehat dan kuat adalah nikmat dari ....', 'Allah', ['teman', 'penjual jajanan', 'televisi'])
f(2, 5, 'Agar badan sehat kita perlu makan makanan yang ....', 'bergizi', ['manis saja', 'sudah basi', 'kotor'])
f(2, 5, 'Agar badan kuat kita rajin ....', 'berolahraga', ['berbaring', 'begadang', 'makan permen'])
f(2, 5, 'Agar badan bersih kita ....', 'mandi dan menggosok gigi', ['bermain lumpur', 'tidak mandi', 'tidak berganti baju'])
f(2, 5, 'Ilmu tentang kesehatan sebaiknya kita ....', 'terapkan setiap hari', ['simpan saja', 'lupakan', 'abaikan'])
f(2, 5, 'Rasa syukur atas badan yang sehat kita tunjukkan dengan ....', 'menjaga kesehatan dan beribadah', ['merusak badan', 'bermalas-malasan', 'berbuat curang'])
f(2, 5, 'Sebelum makan kita mencuci tangan lalu membaca ....', 'bismillah', ['alhamdulillah', 'astaghfirullah', 'innalillahi'])
f(2, 5, 'Setelah makan kita membaca ....', 'alhamdulillah', ['bismillah', 'astaghfirullah', 'innalillahi'])
f(2, 5, 'Tidur yang cukup membuat badan ....', 'segar dan bertenaga', ['lemas', 'sakit', 'lelah terus'])
s(2, 5, 'Dani ingin badannya kuat. Sebaiknya Dani ....', 'Agar badannya kuat, Dani', 'berolahraga dan makan makanan bergizi', ['bermain gawai seharian', 'makan permen saja', 'tidak mau bergerak'], 'Olahraga dan makan bergizi.')
s(2, 5, 'Sinta sudah belajar tentang sayur yang menyehatkan. Sikap Sinta yang baik adalah ....', 'Setelah belajar tentang sayur yang menyehatkan, Sinta', 'makan sayur setiap hari', ['menolak sayur', 'membuang sayur', 'hanya makan jajanan'], 'Menerapkan ilmu yang dipelajari.')
s(2, 5, 'Rafa selesai berolahraga dan merasa sehat. Ia mengucap ....', 'Selesai berolahraga dan merasa sehat, Rafa mengucap', 'alhamdulillah', ['astaghfirullah', 'innalillahi', 'tidak mengucap'], 'Bersyukur kepada Allah.')
s(2, 5, 'Perhatikan gambar! Anak-anak berolahraga senam pagi di halaman sekolah. Kegiatan ini menjaga ....', 'Gambar anak-anak senam pagi menunjukkan kegiatan yang menjaga', 'kesehatan dan kekuatan badan', ['kemalasan', 'kekotoran', 'kesedihan'], 'Senam menyehatkan.', 'easy',
  'Sekitar sepuluh anak berseragam olahraga bersenam bersama di halaman sekolah pada pagi hari.')
T += [(2, 5, 'Makan sayur dan buah membuat badan sehat.', True, 'Gizi dari sayur dan buah.'), (2, 5, 'Olahraga tidak ada manfaatnya bagi badan.', False, 'Olahraga menyehatkan.')]
P += [(2, 5, 'Peragakan senam sederhana lalu ucapkan alhamdulillah!'), (2, 5, 'Ceritakan satu kebiasaan sehat yang kamu lakukan di rumah!')]
M += [(2, 5, 'Jodohkan kebiasaan dengan manfaatnya!', [('makan sayur', 'badan sehat'), ('berolahraga', 'badan kuat'), ('mandi', 'badan bersih'), ('tidur cukup', 'badan segar')], 'Manfaat kebiasaan sehat.')]

# ===================================================================== BAB 3: Keluargaku Sakinah
# 3.4 menceritakan gambar
f(3, 4, 'Untuk menceritakan gambar, kita pertama-tama harus ....', 'mengamati gambar dengan teliti', ['menutup mata', 'membalik gambar', 'tidak melihat gambar'])
f(3, 4, 'Cerita tentang gambar disampaikan dengan kalimat ....', 'sendiri yang jelas', ['yang disalin dari teman', 'yang tidak berhubungan', 'yang membingungkan'])
f(3, 4, 'Saat menceritakan gambar, kita berbicara dengan suara ....', 'jelas dan tidak terlalu cepat', ['sangat pelan hingga tak terdengar', 'berteriak', 'berbisik'])
f(3, 4, 'Dalam gambar keluarga, anggota keluarga yang membuat nasi di dapur biasanya adalah ....', 'ibu', ['bayi', 'kucing', 'televisi'], diff='medium')
f(3, 4, 'Gambar yang menunjukkan ayah, ibu, dan anak menunjukkan ....', 'sebuah keluarga', ['sebuah sekolah', 'sebuah pasar', 'sebuah kebun'])
f(3, 4, 'Saat menceritakan gambar, kita menyebutkan siapa, sedang apa, dan di ....', 'mana', ['kapan saja', 'sana', 'situ saja'], diff='medium')
f(3, 4, 'Cerita yang kreatif tentang gambar boleh ditambah dengan ....', 'ide dan perasaan sendiri', ['kebohongan besar', 'kata kasar', 'cerita lain'])
s(3, 4, 'Perhatikan gambar! Seorang ibu memasak di dapur sementara anak perempuan membantu mengaduk. Kalimat yang tepat untuk menceritakan gambar itu adalah ....', 'Untuk gambar ibu memasak dibantu anak perempuan, kalimat yang tepat adalah', 'Ibu memasak di dapur dibantu anaknya.', ['Ayah membaca koran di taman.', 'Kakak bermain bola di lapangan.', 'Adik tidur di kamar.'], 'Kalimat sesuai gambar.', 'easy',
  'Dapur rumah: seorang ibu berjilbab mengaduk panci di kompor, seorang anak perempuan di sampingnya mengaduk bahan di mangkuk.')
s(3, 4, 'Perhatikan gambar! Seorang ayah membaca buku cerita kepada dua anak sebelum tidur. Kalimat yang tepat adalah ....', 'Untuk gambar ayah membacakan buku kepada dua anak, kalimat yang tepat adalah', 'Ayah membacakan cerita untuk anak-anaknya.', ['Ibu mencuci baju di sungai.', 'Anak-anak bermain di taman.', 'Kakek menanam padi.'], 'Kalimat sesuai gambar.', 'easy',
  'Kamar tidur: ayah duduk di tepi tempat tidur membaca buku cerita, dua anak berselimut mendengarkan.')
s(3, 4, 'Perhatikan gambar! Satu keluarga duduk melingkar makan bersama di ruang makan. Cerita yang sesuai adalah ....', 'Untuk gambar keluarga makan bersama, cerita yang sesuai adalah', 'Keluargaku makan bersama dengan gembira.', ['Aku sendirian di taman.', 'Ibu pergi ke pasar.', 'Ayah naik pesawat.'], 'Kalimat sesuai gambar.', 'easy',
  'Ayah, ibu, kakak, dan adik duduk mengelilingi meja makan dengan nasi dan lauk.')
s(3, 4, 'Perhatikan gambar! Seorang kakak membantu adiknya memakai sepatu. Kalimat yang tepat adalah ....', 'Untuk gambar kakak membantu adik memakai sepatu, kalimat yang tepat adalah', 'Kakak membantu adik memakai sepatu.', ['Adik membantu ibu memasak.', 'Ayah membersihkan mobil.', 'Nenek membaca koran.'], 'Kalimat sesuai gambar.', 'easy',
  'Seorang anak lebih besar berjongkok membantu adik kecil memakai sepatu di teras rumah.')
T += [(3, 4, 'Menceritakan gambar harus sesuai dengan isi gambar.', True, 'Cerita sesuai gambar.'), (3, 4, 'Menceritakan gambar boleh tidak melihat gambarnya.', False, 'Kita mengamati gambar dahulu.')]
P += [(3, 4, 'Amati gambar keluarga di bukumu lalu ceritakan dengan kalimatmu sendiri!'), (3, 4, 'Ceritakan gambar kegiatan keluarga di rumah dengan tiga kalimat!'), (3, 4, 'Gambarlah keluargamu lalu ceritakan kepada temanmu!')]

# 3.5 sikap belajar
f(3, 5, 'Sikap yang baik saat menyimak adalah ....', 'tenang dan memperhatikan', ['ribut', 'berjalan-jalan', 'mengganggu teman'])
f(3, 5, 'Saat membaca, kita sebaiknya ....', 'fokus dan tidak bermain', ['mengobrol', 'tidur', 'berlarian'])
f(3, 5, 'Saat menulis, kita sebaiknya ....', 'rapi dan pelan-pelan', ['asal cepat', 'mencoret-coret', 'menyalin teman'])
f(3, 5, 'Sikap bersungguh-sungguh dalam belajar menunjukkan kita ....', 'menghargai ilmu', ['meremehkan ilmu', 'malas', 'sombong'])
f(3, 5, 'Sebelum belajar kita berdoa agar ilmu ....', 'bermanfaat', ['hilang', 'sulit', 'tidak berguna'])
f(3, 5, 'Mengerjakan tugas dari guru dengan jujur menunjukkan sikap ....', 'tanggung jawab', ['malas', 'curang', 'sombong'])
f(3, 5, 'Jika belum paham, kita sebaiknya ....', 'bertanya dengan sopan', ['diam saja', 'marah', 'pergi'])
f(3, 5, 'Keluarga yang sakinah adalah keluarga yang ....', 'tenang, damai, dan saling menyayangi', ['sering bertengkar', 'saling membenci', 'tidak peduli'], diff='medium')
s(3, 5, 'Lani sedang menyimak cerita bu guru. Sikap Lani adalah ....', 'Saat bu guru bercerita, Lani', 'duduk tenang dan mendengarkan', ['mengobrol dengan teman', 'berlari di kelas', 'menggambar saja'], 'Menyimak dengan sungguh-sungguh.')
s(3, 5, 'Bimo kesulitan membaca satu kata. Sikap Bimo yang baik adalah ....', 'Saat kesulitan membaca satu kata, Bimo', 'bertanya kepada bu guru', ['menyerah', 'menyobek buku', 'marah-marah'], 'Bertanya adalah tanda ingin belajar.')
s(3, 5, 'Nisa membantu ibu di rumah dan tetap belajar sungguh-sungguh. Ini menunjukkan Nisa ....', 'Dengan membantu ibu sambil tetap belajar, Nisa menunjukkan', 'menghargai keluarga dan ilmu', ['malas', 'tidak peduli', 'ingin bermain saja'], 'Menghargai ilmu dan keluarga.')
s(3, 5, 'Perhatikan gambar! Seorang anak mengerjakan tugas menulis dengan tenang di meja belajar rumah. Sikap anak itu menunjukkan ....', 'Gambar anak mengerjakan tugas menulis dengan tenang menunjukkan sikap', 'bersungguh-sungguh belajar', ['malas belajar', 'bermain', 'mengganggu'], 'Belajar sungguh-sungguh.', 'easy',
  'Anak laki-laki menulis di buku di meja belajar yang rapi, lampu belajar menyala, suasana tenang.')
T += [(3, 5, 'Belajar dengan sungguh-sungguh berarti menghargai ilmu.', True, 'Menghargai ilmu.'), (3, 5, 'Saat menyimak kita boleh mengganggu teman.', False, 'Kita harus tenang.')]
P += [(3, 5, 'Tunjukkan sikap menyimak, membaca, dan menulis yang baik di depan kelas!'), (3, 5, 'Ceritakan bagaimana kamu belajar bersama keluarga di rumah!')]

# ===================================================================== BAB 4: Kebersihan Sebagian dari Iman
# 4.1 meniru gerakan
f(4, 1, 'Dalam cerita gerakan hewan, kelinci bergerak dengan cara ....', 'melompat-lompat', ['berenang', 'terbang', 'merayap'])
f(4, 1, 'Gajah berjalan dengan cara ....', 'pelan dan berat', ['melompat', 'terbang', 'berenang'])
f(4, 1, 'Burung bergerak dengan cara ....', 'mengepakkan sayap dan terbang', ['merayap', 'berenang', 'melompat jauh'])
f(4, 1, 'Ikan bergerak dengan cara ....', 'berenang', ['terbang', 'melompat', 'merayap'])
f(4, 1, 'Ular bergerak dengan cara ....', 'merayap', ['terbang', 'melompat', 'berenang di langit'])
f(4, 1, 'Menirukan gerakan tokoh cerita adalah bentuk ....', 'kreativitas dan ekspresi diri', ['kemarahan', 'kemalasan', 'kesedihan'])
f(4, 1, 'Saat menirukan gerakan, kita harus ....', 'berhati-hati dan tidak mengganggu teman', ['mendorong teman', 'berlari tanpa melihat', 'berteriak'])
f(4, 1, 'Cerita tentang membersihkan tangan: tokoh menggosok tangan dengan ....', 'sabun', ['pasir', 'batu', 'arang'])
s(4, 1, 'Bu guru bercerita tentang katak yang melompat. Anak-anak menirukan dengan ....', 'Saat bu guru bercerita tentang katak, anak-anak', 'melompat-lompat kecil dengan hati-hati', ['merayap di lantai', 'berenang di lantai', 'berlari mengejar teman'], 'Menirukan gerakan tokoh.')
s(4, 1, 'Dalam cerita, tokoh menggosok-gosok tangannya dengan sabun. Gerakan yang ditirukan Rafi adalah ....', 'Menirukan tokoh yang mencuci tangan, Rafi', 'menggosok kedua telapak tangannya', ['melompat', 'menepuk perut', 'menutup mata'], 'Menirukan gerakan.')
s(4, 1, 'Perhatikan gambar! Anak-anak menirukan gerakan burung dengan merentangkan tangan seperti sayap. Mereka menirukan tokoh ....', 'Gambar anak-anak merentangkan tangan seperti sayap menirukan tokoh', 'burung', ['ikan', 'ular', 'gajah'], 'Burung memiliki sayap.', 'easy',
  'Lima anak di halaman merentangkan kedua lengan ke samping seolah-olah terbang.')
T += [(4, 1, 'Kita dapat menirukan gerakan tokoh cerita dengan benar.', True, 'Menirukan gerakan adalah ekspresi diri.'), (4, 1, 'Menirukan gerakan berarti mendorong teman.', False, 'Kita menirukan dengan sopan.')]
P += [(4, 1, 'Tirukan gerakan kelinci, gajah, dan burung seperti dalam cerita!'), (4, 1, 'Dengarkan cerita guru lalu tirukan gerakan tokohnya!')]

# 4.4 percaya diri & semangat menuntut ilmu
f(4, 4, 'Menuntut ilmu hukumnya baik bagi ....', 'setiap muslim', ['orang dewasa saja', 'anak laki-laki saja', 'orang kaya saja'])
f(4, 4, 'Sikap percaya diri berarti kita ....', 'yakin dapat melakukan dengan baik', ['takut mencoba', 'malu berbuat', 'tidak mau belajar'])
f(4, 4, 'Orang yang bersemangat menuntut ilmu selalu ....', 'ingin belajar hal baru', ['malas membaca', 'tidak mau bertanya', 'bosan belajar'])
f(4, 4, 'Jika salah menjawab, anak yang percaya diri akan ....', 'memperbaiki dan mencoba lagi', ['menangis dan menyerah', 'menyalahkan teman', 'tidak mau menjawab lagi'])
f(4, 4, 'Ajaran Islam menganjurkan kita menuntut ilmu sejak ....', 'kecil', ['dewasa saja', 'tua', 'tidak pernah'])
f(4, 4, 'Salah satu cara bersemangat belajar adalah ....', 'membaca setiap hari', ['bermain terus', 'tidur terus', 'menunda tugas'])
f(4, 4, 'Berani maju ke depan kelas untuk bercerita menunjukkan sikap ....', 'percaya diri', ['pemalu', 'malas', 'sombong'])
f(4, 4, 'Sebelum belajar kita berdoa agar mendapat ....', 'ilmu yang bermanfaat', ['mainan', 'jajanan', 'uang'])
s(4, 4, 'Fikri diminta membaca di depan kelas, tetapi ia gugup. Sikap yang baik adalah ....', 'Saat diminta membaca di depan kelas dan merasa gugup, Fikri', 'menarik napas, berdoa, lalu membaca dengan berani', ['menolak dan menangis', 'bersembunyi', 'berpura-pura sakit'], 'Percaya diri.')
s(4, 4, 'Dina ingin lancar membaca. Cara bersemangat belajar adalah ....', 'Agar lancar membaca, Dina', 'berlatih membaca setiap hari', ['menunda berlatih', 'bermain terus', 'tidak mau membaca'], 'Rajin berlatih.')
s(4, 4, 'Temanmu takut mencoba menulis di papan tulis. Sikap yang baik adalah ....', 'Melihat temannya takut menulis di papan, Salma', 'menyemangatinya dan mengajaknya mencoba', ['mengejeknya', 'menertawakannya', 'membiarkannya'], 'Saling menyemangati.')
s(4, 4, 'Perhatikan gambar! Seorang anak berdiri di depan kelas dan membaca dengan senyum sementara teman-temannya bertepuk tangan. Sikap anak itu menunjukkan ....', 'Gambar anak membaca di depan kelas dengan senyum menunjukkan sikap', 'percaya diri', ['malu dan takut', 'malas', 'marah'], 'Percaya diri.', 'easy',
  'Seorang anak berdiri di depan kelas memegang buku, tersenyum; teman-teman bertepuk tangan.')
T += [(4, 4, 'Menuntut ilmu sesuai ajaran Islam dilakukan dengan semangat.', True, 'Menuntut ilmu dianjurkan.'), (4, 4, 'Anak yang percaya diri tidak pernah belajar.', False, 'Percaya diri dibangun dengan belajar.')]
P += [(4, 4, 'Maju ke depan kelas dan bacakan satu kalimat dengan percaya diri!'), (4, 4, 'Ceritakan apa yang membuatmu semangat belajar!')]

# ===================================================================== BAB 5: Asyiknya Bermain
# 5.1 tanda titik
f(5, 1, 'Kalimat berita diakhiri dengan tanda ....', 'titik (.)', ['tanya (?)', 'seru (!)', 'koma (,)'])
f(5, 1, 'Tanda "." disebut tanda ....', 'titik', ['tanya', 'seru', 'koma'])
f(5, 1, 'Tanda titik ditulis di ... kalimat berita.', 'akhir', ['awal', 'tengah', 'atas'])
f(5, 1, 'Kalimat yang memberi tahu sesuatu disebut kalimat ....', 'berita', ['tanya', 'seru', 'perintah'], diff='medium')
f(5, 1, 'Setelah tanda titik, kalimat berikutnya diawali huruf ....', 'kapital', ['kecil', 'angka', 'bebas'], diff='medium')
f(5, 1, 'Bentuk tanda titik adalah ....', 'bulatan kecil', ['garis lurus', 'lengkung', 'bintang'])
G += [(5, 1, "Kelompokkan kalimat berikut: 'Ibu memasak.'; 'Siapa namamu?'; 'Aku bermain bola.'; 'Hore, menang!'.", {'berita (titik)': ['Ibu memasak.', 'Aku bermain bola.'], 'bukan berita': ['Siapa namamu?', 'Hore, menang!']}, 'Kalimat berita diakhiri titik.')]
P += [(5, 1, 'Tulislah tiga kalimat berita tentang permainan kesukaanmu dengan tanda titik!'), (5, 1, 'Tunjukkan tanda titik pada kalimat di buku bacaanmu!')]

# 5.4 / 5.5 tambahan nilai Islam
f(5, 5, 'Mengucapkan permisi, tolong, maaf, dan terima kasih termasuk ... dalam Islam.', 'adab yang baik', ['kebiasaan buruk', 'hal yang sia-sia', 'tidak perlu'], diff='medium')
f(5, 5, 'Orang yang mudah meminta maaf dan berterima kasih disukai oleh ....', 'Allah dan sesama', ['tidak ada yang suka', 'musuh', 'orang jahat'])
f(5, 5, 'Rasulullah mengajarkan kita untuk selalu bersikap ....', 'sopan dan santun', ['kasar', 'sombong', 'acuh'])
s(5, 5, 'Rani ingin meminjam penghapus temannya. Ucapan sopan yang dipakai adalah ....', 'Saat ingin meminjam penghapus, Rani berkata', '"Tolong pinjami aku penghapus, ya."', ['"Berikan penghapusmu!"', '"Mana penghapusmu?"', '"Sini, aku ambil!"'], 'Meminta dengan kata tolong.')
s(5, 5, 'Teman Tia membantu mengambilkan buku yang jatuh. Tia berkata ....', 'Saat dibantu temannya mengambil buku, Tia berkata', '"Terima kasih."', ['"Permisi."', '"Maaf."', '"Tolong."'], 'Berterima kasih setelah dibantu.')
s(5, 5, 'Perhatikan gambar! Seorang anak membungkuk sedikit dan berkata kepada dua orang yang sedang berbincang di lorong sempit. Ucapan yang tepat adalah ....', 'Gambar anak melewati dua orang yang berbincang di lorong sempit, ucapan yang tepat adalah', '"Permisi."', ['"Terima kasih."', '"Maaf."', '"Tolong."'], 'Permisi untuk lewat.', 'easy',
  'Lorong sekolah sempit; dua orang berdiri berbincang, seorang anak membungkuk sedikit hendak lewat sambil tersenyum.')
s(5, 5, 'Perhatikan gambar! Seorang anak menunduk meminta maaf kepada temannya yang bajunya terkena tumpahan air. Ucapan yang tepat adalah ....', 'Gambar anak menumpahkan air ke baju temannya, ucapan yang tepat adalah', '"Maaf, aku tidak sengaja."', ['"Permisi."', '"Terima kasih."', '"Tolong."'], 'Maaf saat berbuat salah.', 'easy',
  'Dua anak di kantin; air tumpah di baju seorang anak, anak lain menunduk dengan raut menyesal.')
T += [(5, 5, 'Mengucap terima kasih adalah adab yang diajarkan Islam.', True, 'Berterima kasih adalah terpuji.'), (5, 5, 'Kita tidak perlu minta maaf jika berbuat salah.', False, 'Kita harus meminta maaf.')]
P += [(5, 5, 'Peragakan percakapan memakai permisi, tolong, maaf, dan terima kasih bersama temanmu!'), (5, 5, 'Ceritakan kapan kamu mengucap terima kasih hari ini!')]

# ===================================================================== BAB 6: Rumahku Surgaku
# 6.4 menerapkan bilangan & menyimak
f(6, 4, 'Bilangan dipakai untuk menyebut ....', 'jumlah benda', ['warna benda', 'bau benda', 'rasa benda'])
f(6, 4, 'Saat membeli dua buah jeruk, kita menyebut jumlah dengan kata ....', 'dua', ['satu', 'tiga', 'empat'])
f(6, 4, 'Jika ada tiga kursi dan ditambah satu kursi, jumlahnya menjadi ... kursi.', 'empat', ['dua', 'tiga', 'lima'], diff='medium')
f(6, 4, 'Dalam satu keluarga ada ayah, ibu, dan dua anak. Jumlah semuanya ... orang.', 'empat', ['dua', 'tiga', 'lima'], diff='medium')
f(6, 4, 'Jumlah jari pada satu tangan adalah ....', 'lima', ['tiga', 'enam', 'sepuluh'])
f(6, 4, 'Jumlah jari pada dua tangan adalah ....', 'sepuluh', ['lima', 'delapan', 'dua'])
f(6, 4, 'Jumlah salat fardu dalam sehari adalah ... kali.', 'lima', ['tiga', 'empat', 'enam'])
f(6, 4, 'Menyimak cerita dengan baik membuat kita ....', 'memahami isi cerita', ['mengantuk', 'bingung', 'lupa'])
f(6, 4, 'Ilmu bilangan membantu kita ketika ....', 'berbelanja dan menghitung benda', ['tidur', 'bermimpi', 'bermain saja'])
s(6, 4, 'Ibu meminta Lia mengambil lima piring. Lia mengambil ....', 'Saat diminta ibu mengambil lima piring, Lia', 'lima piring', ['tiga piring', 'tujuh piring', 'sepuluh piring'], 'Menghitung dengan benar.')
s(6, 4, 'Ayah membeli empat apel. Ia memberikan satu apel kepada adik. Sisa apel ayah adalah ....', 'Setelah memberi satu apel kepada adik, ayah memiliki sisa', 'tiga apel', ['dua apel', 'empat apel', 'lima apel'], 'Empat dikurangi satu sama dengan tiga.', 'medium')
s(6, 4, 'Perhatikan gambar! Di meja makan ada tiga piring dan setiap piring ada satu telur. Jumlah telur adalah ....', 'Pada gambar tiga piring masing-masing berisi satu telur, jumlah telur adalah', 'tiga', ['dua', 'empat', 'satu'], 'Tiga piring masing-masing satu telur.', 'easy',
  'Meja makan dengan tiga piring putih, masing-masing berisi satu telur rebus.')
T += [(6, 4, 'Bilangan satu sampai sepuluh dapat dipakai untuk menghitung benda di rumah.', True, 'Bilangan dipakai sehari-hari.'), (6, 4, 'Rumah yang damai berisi keluarga yang saling menyayangi.', True, 'Rumahku surgaku.')]
P += [(6, 4, 'Hitunglah jumlah benda di kelasmu dan sebutkan hasilnya dengan kata!'), (6, 4, 'Ceritakan kegiatan di rumahmu yang memakai bilangan!')]

# ===================================================================== BAB 7: Sekolahku Menyenangkan
# 7.3 menemukan arti kata
f(7, 3, 'Jika menemukan kata baru, kita dapat bertanya kepada ....', 'guru atau orang tua', ['kucing', 'televisi', 'batu'])
f(7, 3, 'Buku yang berisi arti kata disebut ....', 'kamus', ['atlas', 'dongeng', 'buku gambar'])
f(7, 3, 'Kata-kata dalam kamus disusun menurut ....', 'urutan abjad', ['warna', 'ukuran', 'panjang kalimat'], diff='medium')
f(7, 3, 'Kata yang berawalan huruf "a" dicari pada bagian kamus yang ... .', 'awal', ['akhir', 'tengah', 'tidak ada'], diff='medium')
f(7, 3, 'Setelah menemukan arti kata baru, kita ....', 'menuliskannya agar ingat', ['melupakannya', 'menyobeknya', 'mengejeknya'])
f(7, 3, 'Sikap yang baik ketika bertanya arti kata kepada guru adalah ....', 'sopan dan mengangkat tangan', ['berteriak', 'memotong penjelasan', 'bercanda'])
f(7, 3, 'Orang yang rajin bertanya akan ....', 'bertambah ilmunya', ['bertambah malas', 'dijauhi', 'bingung terus'])
s(7, 3, 'Ada kata "dermawan" yang belum dimengerti Hasan. Sikap yang tepat adalah ....', 'Karena belum mengerti kata "dermawan", Hasan', 'bertanya kepada bu guru atau melihat di kamus', ['mengabaikannya', 'menebak-nebak saja', 'mengejek kata itu'], 'Mencari arti kata baru.')
s(7, 3, 'Ayah menjelaskan arti kata "hemat". Setelah paham, Dina ....', 'Setelah ayah menjelaskan arti kata "hemat", Dina', 'menulis arti kata itu di buku', ['melupakannya', 'tidur', 'bermain'], 'Mencatat arti kata.')
s(7, 3, 'Perhatikan gambar! Seorang anak membuka kamus tebal di perpustakaan sambil menunjuk satu kata. Anak itu sedang ....', 'Gambar anak membuka kamus menunjukkan anak sedang', 'mencari arti kata', ['tidur', 'bermain', 'menggambar'], 'Kamus berisi arti kata.', 'easy',
  'Seorang anak di perpustakaan membuka kamus tebal, jarinya menunjuk satu entri di halaman.')
T += [(7, 3, 'Kamus membantu kita menemukan arti kata baru.', True, 'Kamus berisi arti kata.'), (7, 3, 'Kata baru tidak perlu dicari artinya.', False, 'Kita mencari artinya.')]
P += [(7, 3, 'Carilah arti satu kata baru dengan bertanya kepada gurumu, lalu tuliskan!'), (7, 3, 'Buka kamus bersama gurumu dan temukan arti satu kata!')]

# 7.4 bercerita percaya diri
f(7, 4, 'Saat bercerita di depan kelas, kita berbicara dengan suara ....', 'jelas dan lantang', ['berbisik', 'berteriak', 'tidak bersuara'])
f(7, 4, 'Cerita sebaiknya disusun dengan urutan yang ....', 'runtut (berurutan)', ['acak', 'terbalik', 'membingungkan'])
f(7, 4, 'Cerita biasanya dimulai dari ....', 'awal kejadian', ['akhir saja', 'tengah saja', 'tidak jelas'], diff='medium')
f(7, 4, 'Agar percaya diri saat bercerita, kita perlu ....', 'berlatih terlebih dahulu', ['menghindar', 'menunda', 'menangis'])
f(7, 4, 'Ide cerita dapat diambil dari ....', 'pengalaman sehari-hari', ['hal yang tidak kita tahu', 'kebohongan', 'cerita orang lain tanpa izin'])
f(7, 4, 'Saat bercerita, pandangan mata kita sebaiknya ke ....', 'teman-teman pendengar', ['lantai terus', 'langit-langit', 'jendela'])
f(7, 4, 'Cerita yang baik memiliki tokoh, tempat, dan ....', 'peristiwa', ['hadiah', 'jajanan', 'nilai'], diff='medium')
s(7, 4, 'Salma ditunjuk bercerita tentang liburannya. Sikap yang baik adalah ....', 'Saat ditunjuk bercerita tentang liburan, Salma', 'maju dengan percaya diri dan bercerita berurutan', ['menolak', 'menangis', 'bercerita sambil membelakangi teman'], 'Bercerita percaya diri.')
s(7, 4, 'Dani ingin bercerita tentang kucingnya. Ia memulai dengan ....', 'Untuk bercerita tentang kucingnya, Dani memulai dengan', 'menyebut nama kucing dan di mana kucing itu', ['menutup cerita', 'diam saja', 'berbicara tentang hal lain'], 'Cerita dimulai dari tokoh dan tempat.')
s(7, 4, 'Perhatikan gambar! Seorang anak bercerita dengan berdiri di depan kelas dan teman-temannya mendengarkan. Hal baik yang ditunjukkan adalah ....', 'Gambar anak bercerita di depan kelas menunjukkan sikap', 'percaya diri dan didengarkan teman', ['teman tidak peduli', 'anak takut', 'anak bermain'], 'Percaya diri bercerita.', 'easy',
  'Seorang anak berdiri di depan kelas bercerita sambil membuat gerakan tangan; teman-teman duduk rapi menyimak.')
T += [(7, 4, 'Bercerita harus berurutan dari awal sampai akhir.', True, 'Cerita runtut.'), (7, 4, 'Saat bercerita, kita boleh membelakangi pendengar.', False, 'Menghadap pendengar.')]
P += [(7, 4, 'Ceritakan pengalaman liburanmu di depan teman-temanmu dengan percaya diri!'), (7, 4, 'Ceritakan hewan kesayanganmu dengan tiga kalimat!')]

# 7.5 adab bercerita
f(7, 5, 'Sebelum bercerita, kita mengucap ....', 'basmalah', ['takbir', 'hamdalah', 'istigfar'])
f(7, 5, 'Saat teman bercerita, kita harus ....', 'mendengarkan dengan tenang', ['memotong cerita', 'mengejek', 'meninggalkannya'])
f(7, 5, 'Cerita yang kita sampaikan harus ....', 'benar dan tidak berbohong', ['dibuat-buat sampai bohong', 'menyakiti orang lain', 'menyombongkan diri'])
f(7, 5, 'Kita tidak boleh bercerita yang ... tentang orang lain.', 'menjelekkan', ['baik', 'jujur', 'menyenangkan'])
f(7, 5, 'Setelah bercerita, kita mengucap ....', 'terima kasih dan hamdalah', ['permisi', 'maaf saja', 'tidak mengucap'])
f(7, 5, 'Bertepuk tangan setelah teman bercerita menunjukkan sikap ....', 'menghargai', ['mengejek', 'iri', 'marah'])
f(7, 5, 'Bila ingin menanggapi cerita teman, kita ....', 'menunggu cerita selesai', ['memotong di tengah', 'berteriak', 'pergi'], diff='medium')
s(7, 5, 'Tia sedang bercerita. Rani ingin bicara. Sikap Rani yang baik adalah ....', 'Saat Tia bercerita dan Rani ingin bicara, Rani', 'menunggu sampai Tia selesai', ['memotong cerita Tia', 'berteriak', 'pergi'], 'Menghargai pembicara.')
s(7, 5, 'Hasan akan bercerita di depan kelas. Hal pertama yang ia ucapkan adalah ....', 'Sebelum bercerita di depan kelas, Hasan mengucapkan', 'basmalah', ['hamdalah', 'taawuz', 'tidak mengucap apa pun'], 'Memulai dengan basmalah.')
s(7, 5, 'Cerita Fikri lucu, tetapi ada kata yang menyinggung temannya. Sikap yang baik adalah ....', 'Menyadari ada kata yang menyinggung temannya, Fikri', 'meminta maaf dan tidak mengulanginya', ['tertawa saja', 'menyalahkan teman', 'mengulangi lebih keras'], 'Menjaga adab.')
T += [(7, 5, 'Mendengarkan teman bercerita adalah adab yang baik.', True, 'Menghargai teman.'), (7, 5, 'Kita boleh mengejek cerita teman yang kurang bagus.', False, 'Tidak boleh mengejek.')]
P += [(7, 5, 'Peragakan adab sebelum, saat, dan sesudah bercerita bersama temanmu!'), (7, 5, 'Ucapkan terima kasih kepada teman yang selesai bercerita!')]

# ===================================================================== BAB 8: Lingkungan Sekitarku
# 8.2 menulis kata arah/letak/pekerjaan
f(8, 2, 'Kata yang menunjukkan benda berada pada bagian atas adalah ....', 'di atas', ['di bawah', 'di dalam', 'di luar'])
f(8, 2, 'Kata yang menunjukkan benda berada pada bagian bawah adalah ....', 'di bawah', ['di atas', 'di dalam', 'di samping'])
f(8, 2, 'Kata "di" pada kata letak ditulis ... dengan kata sesudahnya.', 'terpisah', ['disambung', 'dihapus', 'diganti angka'], diff='medium')
f(8, 2, 'Penulisan yang benar adalah ....', 'di atas meja', ['diatas meja', 'di-atas meja', 'diatas-meja'], diff='medium')
f(8, 2, 'Penulisan yang benar adalah ....', 'di samping rumah', ['disamping rumah', 'di-samping rumah', 'disampingrumah'], diff='medium')
f(8, 2, 'Pekerjaan yang mengobati orang sakit ditulis ....', 'dokter', ['dokte', 'doktor', 'dokteer'], diff='medium')
f(8, 2, 'Pekerjaan yang menanam padi di sawah ditulis ....', 'petani', ['patani', 'petanii', 'petoni'], diff='medium')
f(8, 2, 'Kata arah yang berlawanan dengan kanan adalah ....', 'kiri', ['atas', 'bawah', 'depan'])
f(8, 2, 'Kata arah yang berlawanan dengan depan adalah ....', 'belakang', ['kiri', 'atas', 'bawah'])
s(8, 2, 'Bu guru meminta Lani menulis kata "di bawah". Tulisan yang benar adalah ....', 'Menulis kata letak, Lani menulis', 'di bawah', ['dibawah', 'di-bawah', 'dibawa h'], 'Kata di ditulis terpisah.', 'medium')
s(8, 2, 'Rafi menulis pekerjaan ayah, yaitu seorang guru. Tulisan yang benar adalah ....', 'Menulis pekerjaan ayah, Rafi menulis', 'guru', ['guruu', 'goru', 'gurru'], 'Ejaan guru.')
T += [(8, 2, 'Kata "di" pada "di atas" ditulis terpisah.', True, 'Kata depan ditulis terpisah.'), (8, 2, 'Tulisan "diatas" sudah benar untuk menunjukkan letak.', False, 'Yang benar "di atas".')]
P += [(8, 2, 'Tulislah lima kata tentang letak dan arah dengan tulisan yang rapi dan benar!'), (8, 2, 'Tulislah tiga nama pekerjaan di sekitarmu!')]

# 8.4 sungguh-sungguh & profesi
f(8, 4, 'Orang yang mengobati orang sakit adalah ....', 'dokter', ['petani', 'sopir', 'penjahit'])
f(8, 4, 'Agar bercita-cita tinggi tercapai kita harus ....', 'belajar sungguh-sungguh', ['bermalas-malasan', 'bermain terus', 'menunda belajar'])
f(8, 4, 'Cita-cita adalah ....', 'keinginan yang ingin dicapai', ['barang yang dibeli', 'mainan', 'makanan'], diff='medium')
f(8, 4, 'Setiap pekerjaan yang halal adalah pekerjaan yang ....', 'mulia', ['hina', 'tidak berguna', 'memalukan'])
f(8, 4, 'Kita harus menghargai semua pekerjaan di sekitar kita karena ....', 'semuanya bermanfaat bagi orang lain', ['semuanya mudah', 'tidak ada manfaatnya', 'hanya dokter yang penting'])
f(8, 4, 'Orang yang rajin belajar dan berdoa akan lebih mudah ....', 'mencapai cita-cita', ['malas', 'menyerah', 'bingung'])
f(8, 4, 'Ilmu yang kita pelajari di sekolah dapat membantu kita ....', 'mencapai cita-cita', ['bermalas-malasan', 'meremehkan orang', 'tidak berguna'])
s(8, 4, 'Dani bercita-cita menjadi dokter. Yang perlu ia lakukan adalah ....', 'Agar cita-citanya menjadi dokter tercapai, Dani', 'belajar sungguh-sungguh dan berdoa', ['bermain terus', 'membolos', 'menyontek'], 'Berusaha dan berdoa.')
s(8, 4, 'Lia bertemu seorang petani di sawah. Sikap Lia yang baik adalah ....', 'Bertemu petani di sawah, Lia', 'menyapa dengan sopan dan menghargai pekerjaannya', ['menertawakannya', 'mengotori sawah', 'mengabaikannya'], 'Menghargai pekerjaan.')
s(8, 4, 'Perhatikan gambar! Seorang anak memakai baju polisi mainan sambil mengatur lalu lintas mainan. Anak itu bercita-cita menjadi ....', 'Gambar anak bermain peran memakai seragam polisi menunjukkan cita-cita menjadi', 'polisi', ['dokter', 'petani', 'guru'], 'Bermain peran menunjukkan cita-cita.', 'easy',
  'Anak laki-laki berbaju polisi mainan dengan peluit mengatur mobil-mobilan di lantai.')
T += [(8, 4, 'Belajar sungguh-sungguh membantu mencapai cita-cita.', True, 'Usaha dan doa.'), (8, 4, 'Pekerjaan tukang kebun tidak perlu dihargai.', False, 'Semua pekerjaan halal perlu dihargai.')]
P += [(8, 4, 'Ceritakan cita-citamu dan apa yang akan kamu lakukan untuk mencapainya!'), (8, 4, 'Peragakan pekerjaan yang kamu cita-citakan di depan kelas!')]
