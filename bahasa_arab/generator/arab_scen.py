# -*- coding: utf-8 -*-
"""Skenario penerapan (TP4) Bahasa Arab: sikap & praktik, ditulis tangan.
Tuple: (tp, soal_panjang, awalan_pernyataan, benar, [3 salah], penjelasan, kesulitan, visual)"""

SCEN = {}
SCEN['PK'] = [
 (4, "Aisyah bertemu teman baru di kelas. Agar memperkenalkan diri dengan sopan dan ramah, Aisyah sebaiknya ....",
  "Saat bertemu teman baru, Aisyah", "tersenyum, mengucap salam, lalu menyebut namanya dengan \"اِسْمِيْ ....\"", ["diam sambil menunduk", "langsung meminta jajanan temannya", "memalingkan wajah dan pergi"],
  "Perkenalan yang sopan dimulai dengan senyum, salam, lalu menyebut nama.", 'easy', None),
 (4, "Temanmu menyapa, \"اَلسَّلَامُ عَلَيْكُمْ\". Jawaban yang tepat adalah ....",
  "Ketika temannya mengucap \"اَلسَّلَامُ عَلَيْكُمْ\", Rafi menjawab", "\"وَعَلَيْكُمُ السَّلَامُ\"", ["\"صَبَاحُ الْخَيْرِ\"", "\"شُكْرًا\"", "\"مَعَ السَّلَامَةِ\""],
  "Salam dijawab dengan وَعَلَيْكُمُ السَّلَامُ.", 'easy', None),
 (4, "Bu Guru masuk kelas dan berkata, \"صَبَاحُ الْخَيْرِ\". Murid menjawab dengan ramah, \"....\"",
  "Ketika gurunya berkata \"صَبَاحُ الْخَيْرِ\", murid menjawab", "\"صَبَاحُ النُّوْرِ\"", ["\"مَعَ السَّلَامَةِ\"", "\"عَفْوًا\"", "\"مَسَاءُ الْخَيْرِ\""],
  "Selamat pagi dijawab dengan صَبَاحُ النُّوْرِ.", 'medium', None),
 (4, "Temanmu meminjamkan penghapus kepadamu. Kamu mengucapkan ....",
  "Setelah dipinjami penghapus, Zaki mengucapkan", "\"شُكْرًا\"", ["\"عَفْوًا\"", "\"مَرْحَبًا\"", "\"مَعَ السَّلَامَةِ\""],
  "شُكْرًا berarti terima kasih.", 'easy', None),
 (4, "Seorang tamu datang ke rumahmu. Kamu menyambutnya dengan ....",
  "Menyambut tamu di rumah, Hana mengucapkan", "\"أَهْلًا وَسَهْلًا\"", ["\"مَعَ السَّلَامَةِ\"", "\"شُكْرًا\"", "\"صَبَاحُ النُّوْرِ\""],
  "أَهْلًا وَسَهْلًا berarti selamat datang.", 'easy', None),
 (4, "Waktu pulang sekolah, kamu berpamitan kepada gurumu dengan ....",
  "Berpamitan pada guru, murid mengucapkan", "\"مَعَ السَّلَامَةِ\"", ["\"أَهْلًا وَسَهْلًا\"", "\"صَبَاحُ الْخَيْرِ\"", "\"مَرْحَبًا\""],
  "مَعَ السَّلَامَةِ berarti selamat tinggal.", 'easy', None),
 (4, "Bu Guru bertanya, \"كَيْفَ حَالُكَ؟\" Jawaban yang tepat dan penuh syukur adalah ....",
  "Ketika ditanya \"كَيْفَ حَالُكَ؟\", Bagas menjawab", "\"أَنَا بِخَيْرٍ، اَلْحَمْدُ لِلّٰهِ\"", ["\"اِسْمِيْ أَحْمَدُ\"", "\"هٰذَا قَلَمٌ\"", "\"مَعَ السَّلَامَةِ\""],
  "كَيْفَ حَالُكَ؟ ditanyakan kabar; dijawab أَنَا بِخَيْرٍ.", 'medium', None),
 (4, "Kamu ingin menanyakan nama teman perempuanmu dalam bahasa Arab. Kalimat yang tepat adalah ....",
  "Menanyakan nama teman perempuan, murid mengatakan", "\"مَا اسْمُكِ؟\"", ["\"مَا اسْمُكَ؟\"", "\"مَنْ هُوَ؟\"", "\"كَيْفَ حَالُكَ؟\""],
  "مَا اسْمُكِ؟ untuk perempuan.", 'medium', None),
 (4, "Kamu ingin menanyakan nama teman laki-lakimu dalam bahasa Arab. Kalimat yang tepat adalah ....",
  "Menanyakan nama teman laki-laki, murid mengatakan", "\"مَا اسْمُكَ؟\"", ["\"مَا اسْمُكِ؟\"", "\"مَنْ هِيَ؟\"", "\"شُكْرًا\""],
  "مَا اسْمُكَ؟ untuk laki-laki.", 'medium', None),
 (4, "Ada murid pindahan yang pemalu di kelasmu. Sikap yang baik adalah ....",
  "Melihat murid pindahan yang pemalu, Dinda", "menyapa dengan ramah dan mengajaknya berkenalan", ["mengejeknya karena pemalu", "membiarkannya sendirian", "menjauhinya"],
  "Ramah kepada teman baru adalah wujud cinta sesama.", 'easy', None),
 (4, "Temanmu bertanya siapa namamu. Sikap jujur yang benar adalah ....",
  "Saat ditanya namanya, Salma", "menyebut nama aslinya dengan jujur", ["menyebut nama palsu untuk bercanda", "menyuruh orang lain menjawab", "diam saja tanpa menjawab"],
  "Jujur dalam memperkenalkan diri.", 'easy', None),
 (4, "Adikmu belum hafal cara menjawab salam. Sikap yang baik adalah ....",
  "Saat adik belum hafal menjawab salam, kakak", "mengajarinya dengan sabar sambil memberi contoh", ["menertawakannya", "memarahinya", "tidak mau mengajari"],
  "Mengajari dengan sabar adalah wujud cinta sesama.", 'medium', None),
 (4, "Perhatikan gambar! Dua anak saling bersalaman dan tersenyum di halaman madrasah. Ucapan yang tepat dari salah satu anak adalah ....",
  "Gambar dua anak bersalaman, ucapan yang tepat adalah", "\"اَلسَّلَامُ عَلَيْكُمْ\"", ["\"مَعَ السَّلَامَةِ\"", "\"عَفْوًا\"", "\"شُكْرًا\""],
  "Bersalaman biasanya dimulai dengan salam.", 'easy',
  "Dua anak MI berseragam saling bersalaman dan tersenyum di halaman madrasah."),
 (4, "Perhatikan gambar! Seorang anak melambai ceria di gerbang sekolah saat pagi hari sambil menyapa gurunya. Ucapan yang tepat adalah ....",
  "Gambar anak menyapa guru di gerbang pada pagi hari, ucapan yang tepat adalah", "\"صَبَاحُ الْخَيْرِ\"", ["\"مَسَاءُ الْخَيْرِ\"", "\"مَعَ السَّلَامَةِ\"", "\"عَفْوًا\""],
  "Pagi hari: صَبَاحُ الْخَيْرِ.", 'easy',
  "Matahari terbit di atas gerbang madrasah; seorang anak melambai kepada guru yang berdiri menyambut."),
 (4, "Perhatikan gambar! Seorang anak melambaikan tangan di gerbang sekolah saat matahari terbenam setelah pulang sekolah. Ucapan perpisahan yang tepat adalah ....",
  "Gambar anak melambai saat pulang sekolah, ucapan perpisahan yang tepat adalah", "\"مَعَ السَّلَامَةِ\"", ["\"أَهْلًا وَسَهْلًا\"", "\"مَرْحَبًا\"", "\"صَبَاحُ الْخَيْرِ\""],
  "Perpisahan: مَعَ السَّلَامَةِ.", 'easy',
  "Langit jingga sore hari; seorang anak melambaikan tangan di gerbang sekolah kepada teman-temannya."),
]

SCEN['KL'] = [
 (4, "Ayah pulang kerja sore hari. Sikap Naufal yang baik adalah ....", "Saat ayah pulang kerja, Naufal", "mengucap salam dan mencium tangan ayah", ["terus bermain tanpa menyapa", "bersembunyi di kamar", "meminta uang jajan tanpa menyapa"], "Menghormati orang tua dengan salam dan mencium tangan.", 'easy', None),
 (4, "Ibu sedang menyiapkan makan malam. Sikap Aulia yang baik adalah ....", "Saat ibu menyiapkan makan malam, Aulia", "membantu merapikan meja dengan senang hati", ["menonton televisi dan tidak peduli", "mengeluh karena lapar", "mengganggu adik hingga menangis"], "Membantu ibu adalah wujud sayang kepada keluarga.", 'easy', None),
 (4, "Adikmu menangis karena mainannya hilang. Sikap yang baik adalah ....", "Melihat adik menangis kehilangan mainan, kakak", "menghibur dan membantu mencarinya", ["menertawakannya", "memarahinya", "pergi tanpa peduli"], "Menyayangi adik berarti menghibur dan membantunya.", 'easy', None),
 (4, "Nenek sedang sakit di rumah. Sikap cucu yang baik adalah ....", "Ketika nenek sakit, cucu", "mendoakan dan membantu mengambilkan minum", ["bermain keras di dekatnya", "tidak mau mendekat", "berteriak memanggil teman"], "Menghargai dan menyayangi nenek.", 'medium', None),
 (4, "Kakek sedang bercerita. Sikap yang baik adalah ....", "Saat kakek bercerita, cucu", "mendengarkan dengan tenang dan sopan", ["pergi sambil bermain", "memotong cerita dengan keras", "berpura-pura tidur"], "Mendengarkan orang tua adalah adab yang baik.", 'easy', None),
 (4, "Kakakmu membantu menjelaskan PR. Setelah itu kamu mengucapkan ....", "Setelah dibantu kakak mengerjakan PR, Nida mengucapkan", "\"شُكْرًا\"", ["\"مَعَ السَّلَامَةِ\"", "\"مَرْحَبًا\"", "\"عَفْوًا\""], "شُكْرًا berarti terima kasih.", 'easy', None),
 (4, "Ibu menunjuk foto ayah dan bertanya, \"مَنْ هُوَ؟\" Jawabanmu adalah ....", "Ditanya \"مَنْ هُوَ؟\" sambil menunjuk foto ayah, anak menjawab", "\"هُوَ أَبِيْ\"", ["\"هِيَ أُمِّيْ\"", "\"هٰذِهِ مَدْرَسَةٌ\"", "\"اِسْمِيْ أَحْمَدُ\""], "هُوَ untuk laki-laki; أَبِيْ ayahku.", 'medium', None),
 (4, "Ayah menunjuk foto nenek dan bertanya, \"مَنْ هِيَ؟\" Jawabanmu adalah ....", "Ditanya \"مَنْ هِيَ؟\" sambil menunjuk foto nenek, anak menjawab", "\"هِيَ جَدَّتِيْ\"", ["\"هُوَ جَدِّيْ\"", "\"هُوَ أَبِيْ\"", "\"هٰذَا بَيْتٌ\""], "هِيَ untuk perempuan; جَدَّتِيْ nenekku.", 'medium', None),
 (4, "Ibu menasihatimu agar tidak pulang terlalu sore. Sikap yang baik adalah ....", "Saat dinasihati ibu, murid", "mendengarkan dan berjanji menaati", ["membantah dengan keras", "menutup telinga", "pergi tanpa menjawab"], "Menaati nasihat orang tua.", 'medium', None),
 (4, "Kamu bertengkar kecil dengan kakakmu. Sikap yang baik adalah ....", "Setelah bertengkar kecil dengan kakak, adik", "meminta maaf dan berdamai", ["tidak mau bicara berhari-hari", "mengadu domba", "membalas dengan marah"], "Berdamai dengan saudara menjaga keharmonisan keluarga.", 'medium', None),
 (4, "Ayah baru pulang dan tampak lelah. Sikap anak yang baik adalah ....", "Melihat ayah yang lelah, anak", "mengambilkan air minum dan tidak berisik", ["bermain keras di dekatnya", "meminta ayah segera bermain", "menutup pintu dengan keras"], "Menghargai ayah yang lelah.", 'medium', None),
 (4, "Keluargamu berkumpul untuk makan malam. Sikap yang baik adalah ....", "Saat makan malam bersama keluarga, anak", "membaca bismillah dan makan bersama dengan tertib", ["makan sendiri di kamar", "berebut makanan", "makan sambil berlari"], "Kebersamaan dan adab makan.", 'easy', None),
 (4, "Perhatikan gambar! Seorang anak mencium tangan ayahnya yang baru pulang. Sikap anak itu menunjukkan ....", "Gambar anak mencium tangan ayah menunjukkan sikap", "hormat dan sayang kepada orang tua", ["malas bergerak", "tidak peduli", "suka bermain"], "Mencium tangan adalah tanda hormat.", 'easy',
  "Seorang anak berseragam MI mencium tangan ayah yang baru pulang membawa tas kerja di depan pintu rumah."),
 (4, "Perhatikan gambar! Seorang anak memeluk neneknya yang duduk di kursi goyang. Sikap anak itu menunjukkan ....", "Gambar anak memeluk nenek menunjukkan sikap", "sayang kepada anggota keluarga", ["takut kepada nenek", "tidak peduli", "bosan di rumah"], "Memeluk nenek menunjukkan rasa sayang.", 'easy',
  "Seorang anak perempuan memeluk nenek berkerudung yang duduk di kursi goyang di ruang tamu."),
 (4, "Perhatikan gambar! Sebuah foto keluarga berisi ayah, ibu, kakak, dan adik. Kalimat Arab yang tepat untuk gambar itu adalah ....", "Gambar foto keluarga, kalimat Arab yang tepat adalah", "\"هٰذِهِ أُسْرَتِيْ\"", ["\"هٰذَا بَيْتٌ\"", "\"هٰذِهِ مَدْرَسَةٌ\"", "\"مَا اسْمُكَ؟\""], "أُسْرَتِيْ berarti keluargaku.", 'medium',
  "Foto berbingkai yang menampilkan ayah, ibu, seorang kakak, dan seorang adik tersenyum bersama."),
]

SCEN['RM'] = [
 (4, "Kamarmu berantakan setelah bermain. Sikap yang baik adalah ....", "Setelah bermain, Raka", "merapikan tempat tidur dan mainannya", ["membiarkannya berantakan", "menyuruh adik membereskan sendirian", "menyembunyikan mainan di bawah kasur"], "Merapikan kamar menjaga kebersihan dan kerapian.", 'easy', None),
 (4, "Lantai rumah terlihat kotor. Alat yang kamu pakai adalah مِكْنَسَةٌ, yaitu ....", "Untuk membersihkan lantai, Dewi memakai مِكْنَسَةٌ, yaitu", "sapu", ["lampu", "kursi", "kulkas"], "مِكْنَسَةٌ berarti sapu.", 'easy', None),
 (4, "Ada sampah di halaman rumahmu. Sikap yang baik adalah ....", "Melihat sampah di halaman, Fikri", "memungut dan membuangnya ke tempat sampah", ["membiarkannya", "menendangnya ke selokan", "menyuruh teman yang membuang"], "Menjaga halaman bersih adalah cinta lingkungan.", 'easy', None),
 (4, "Siang hari lampu kamar masih menyala padahal tidak dipakai. Sikap yang baik adalah ....", "Melihat lampu menyala tanpa dipakai pada siang hari, Nabil", "mematikannya untuk menghemat listrik", ["membiarkannya menyala seharian", "menyalakan semua lampu", "memecahkan lampu itu"], "Hemat energi adalah bagian dari menjaga lingkungan.", 'medium', None),
 (4, "Pagi hari kamu membuka نَافِذَةٌ kamar. Manfaatnya adalah ....", "Membuka نَافِذَةٌ kamar di pagi hari, Syifa", "membuat udara segar masuk", ["membuat kamar semakin gelap", "membuat kamar berdebu terus", "tidak ada manfaatnya"], "نَافِذَةٌ berarti jendela; membukanya menyegarkan udara.", 'medium', None),
 (4, "Tanaman di حَدِيْقَةٌ rumahmu mulai layu. Sikap yang baik adalah ....", "Melihat tanaman di taman layu, Hasan", "menyiramnya dan merawatnya", ["menginjak tanamannya", "mencabut semuanya", "membiarkannya kering"], "حَدِيْقَةٌ berarti taman; merawat tanaman adalah cinta lingkungan.", 'medium', None),
 (4, "Setelah makan, piring kotor menumpuk. Sikap yang baik adalah ....", "Setelah makan, anak yang baik", "mencuci piringnya atau membantu ibu mencuci", ["meninggalkannya begitu saja", "membuangnya ke halaman", "menyembunyikan di lemari"], "Membantu kebersihan rumah.", 'easy', None),
 (4, "Ibu meminta bantuan membersihkan rumah. Sikap yang baik adalah ....", "Saat ibu meminta bantuan membersihkan rumah, Lia", "membantu dengan senang hati", ["pura-pura tidak mendengar", "menjawab dengan nada kasar", "pergi bermain"], "Membantu ibu menunjukkan cinta keluarga.", 'easy', None),
 (4, "Sepatu berserakan di depan pintu. Sikap yang baik adalah ....", "Melihat sepatu berserakan di depan بَابٌ rumah, Farhan", "menatanya di rak sepatu", ["menendangnya ke sudut", "menumpuknya di tengah jalan", "membiarkannya"], "بَابٌ berarti pintu; menata sepatu menjaga kerapian.", 'medium', None),
 (4, "Ibu menunjuk pintu dan bertanya, \"مَا هٰذَا؟\" Jawabanmu adalah ....", "Ditanya \"مَا هٰذَا؟\" sambil menunjuk pintu, anak menjawab", "\"هٰذَا بَابٌ\"", ["\"هٰذِهِ نَافِذَةٌ\"", "\"هٰذِهِ غُرْفَةٌ\"", "\"هُوَ أَبِيْ\""], "بَابٌ (mudzakkar) memakai هٰذَا.", 'medium', None),
 (4, "Ibu menunjuk jendela dan bertanya, \"مَا هٰذِهِ؟\" Jawabanmu adalah ....", "Ditanya \"مَا هٰذِهِ؟\" sambil menunjuk jendela, anak menjawab", "\"هٰذِهِ نَافِذَةٌ\"", ["\"هٰذَا بَابٌ\"", "\"هٰذَا بَيْتٌ\"", "\"اِسْمِيْ نَافِذَةٌ\""], "نَافِذَةٌ (muannats) memakai هٰذِهِ.", 'medium', None),
 (4, "Setelah memakai حَمَّامٌ, hal yang harus dilakukan adalah ....", "Setelah memakai حَمَّامٌ (kamar mandi), anak", "menyiram dan membiarkannya tetap bersih", ["meninggalkannya kotor", "membasahi seluruh lantai", "membiarkan keran menyala"], "حَمَّامٌ berarti kamar mandi; menjaga kebersihan fasilitas rumah.", 'medium', None),
 (4, "Perhatikan gambar! Seorang anak menyapu lantai ruang tamu dengan sapu. Sikap anak itu menunjukkan ....", "Gambar anak menyapu ruang tamu menunjukkan sikap", "peduli kebersihan rumah", ["malas bergerak", "suka mengotori", "tidak mau membantu"], "Menyapu menjaga rumah tetap bersih.", 'easy',
  "Seorang anak menyapu lantai ruang tamu dengan sapu ijuk; debu terkumpul di pengki."),
 (4, "Perhatikan gambar! Seorang anak merapikan selimut dan bantal di tempat tidurnya. Sikap anak itu menunjukkan ....", "Gambar anak merapikan tempat tidur menunjukkan sikap", "disiplin dan menjaga kerapian", ["malas", "suka berantakan", "tidak peduli"], "Merapikan tempat tidur adalah kebiasaan baik.", 'easy',
  "Seorang anak berdiri di samping tempat tidur sambil melipat selimut dan menata bantal."),
 (4, "Perhatikan gambar! Satu keluarga bekerja sama membersihkan rumah: ayah mengepel, ibu merapikan, dan anak menyapu. Hal ini menunjukkan ....", "Gambar keluarga membersihkan rumah bersama menunjukkan", "kerja sama dan cinta lingkungan", ["pertengkaran dalam keluarga", "kemalasan bersama", "kebiasaan membuang sampah"], "Menjaga rumah bersama keluarga.", 'medium',
  "Ayah mengepel lantai, ibu merapikan rak, anak menyapu; semuanya tersenyum di ruang keluarga."),
]

SCEN['SK'] = [
 (4, "Guru masuk ke kelas. Sikap murid yang baik adalah ....", "Saat guru masuk kelas, murid", "berdiri sopan dan mengucap salam", ["terus berlarian", "berteriak keras", "pura-pura tidur"], "Menghormati guru.", 'easy', None),
 (4, "Guru sedang menjelaskan pelajaran. Sikap murid yang baik adalah ....", "Saat guru menjelaskan, murid", "mendengarkan dengan tenang dan mencatat", ["mengobrol dengan teman", "bermain di bawah meja", "keluar kelas tanpa izin"], "Belajar sungguh-sungguh adalah wujud cinta ilmu.", 'easy', None),
 (4, "Temanmu tidak membawa قَلَمٌ. Sikap yang baik adalah ....", "Saat teman tidak membawa قَلَمٌ (pena), Rani", "meminjamkan penanya", ["menyembunyikan penanya", "menertawakannya", "tidak mau berbicara dengannya"], "قَلَمٌ berarti pena; berbagi adalah akhlak baik.", 'easy', None),
 (4, "Mejamu kotor oleh serutan pensil. Sikap yang baik adalah ....", "Melihat mejanya kotor, Yusuf", "membersihkannya sendiri", ["membiarkannya", "menyuruh teman membersihkan", "menambah kotoran"], "Menjaga kebersihan kelas.", 'easy', None),
 (4, "Hari ini jadwal piketmu. Sikap yang baik adalah ....", "Saat jadwal piket, Putri", "menyapu dan merapikan kelas dengan sungguh-sungguh", ["pulang lebih awal", "pura-pura sakit", "menyuruh teman mengerjakan"], "Tanggung jawab menjaga kebersihan kelas.", 'medium', None),
 (4, "Kamu menemukan bungkus jajanan di dekat فَصْلٌ. Sikap yang baik adalah ....", "Menemukan bungkus jajanan di dekat فَصْلٌ (kelas), Dimas", "membuangnya ke tempat sampah", ["membiarkannya", "melemparnya ke kebun sekolah", "menyembunyikannya di laci"], "فَصْلٌ berarti kelas; buang sampah pada tempatnya.", 'easy', None),
 (4, "Kamu terlambat masuk kelas. Sikap yang baik adalah ....", "Karena terlambat, Aldi", "mengucap salam, meminta maaf, dan meminta izin masuk dengan sopan", ["langsung masuk tanpa permisi", "menyalahkan temannya", "membanting pintu"], "Sopan dan jujur ketika terlambat.", 'medium', None),
 (4, "PR-mu belum selesai. Sikap yang jujur adalah ....", "Karena PR belum selesai, Mira", "mengakui kepada guru dan berjanji menyelesaikannya", ["menyontek teman", "berbohong bahwa buku tertinggal", "menyobek buku tulis"], "Jujur dan bertanggung jawab.", 'medium', None),
 (4, "Kamu berada di مَكْتَبَةٌ sekolah. Sikap yang baik adalah ....", "Di مَكْتَبَةٌ (perpustakaan), murid", "bersikap tenang dan merapikan buku setelah dibaca", ["berlari sambil berteriak", "mencoret buku", "meninggalkan buku berserakan"], "مَكْتَبَةٌ berarti perpustakaan; menjaga ketenangan dan kerapian.", 'easy', None),
 (4, "Kamu berada di مَسْجِدٌ sekolah. Sikap yang baik adalah ....", "Di مَسْجِدٌ (masjid) sekolah, murid", "tertib dan menata sepatu dengan rapi", ["bermain kejar-kejaran", "berteriak keras", "membuang sampah sembarangan"], "مَسْجِدٌ berarti masjid; menghormati tempat ibadah.", 'easy', None),
 (4, "Guru menunjuk pena dan bertanya, \"مَا هٰذَا؟\" Jawabanmu adalah ....", "Ditanya \"مَا هٰذَا؟\" sambil menunjuk pena, murid menjawab", "\"هٰذَا قَلَمٌ\"", ["\"هٰذِهِ حَقِيْبَةٌ\"", "\"هٰذِهِ مَدْرَسَةٌ\"", "\"هُوَ أَبِيْ\""], "قَلَمٌ (mudzakkar) memakai هٰذَا.", 'medium', None),
 (4, "Guru menunjuk tas dan bertanya, \"مَا هٰذِهِ؟\" Jawabanmu adalah ....", "Ditanya \"مَا هٰذِهِ؟\" sambil menunjuk tas, murid menjawab", "\"هٰذِهِ حَقِيْبَةٌ\"", ["\"هٰذَا قَلَمٌ\"", "\"هٰذَا كِتَابٌ\"", "\"اِسْمِيْ حَقِيْبَةٌ\""], "حَقِيْبَةٌ (muannats) memakai هٰذِهِ.", 'medium', None),
 (4, "Temanmu kesulitan memahami pelajaran Bahasa Arab. Sikap yang baik adalah ....", "Melihat teman kesulitan belajar Bahasa Arab, Salsa", "mengajak belajar bersama dengan sabar", ["menertawakannya", "membiarkannya", "menyembunyikan bukunya"], "Saling membantu belajar.", 'medium', None),
 (4, "Perhatikan gambar! Seorang murid mengangkat tangan sebelum bertanya kepada guru. Sikap itu menunjukkan ....", "Gambar murid mengangkat tangan sebelum bertanya menunjukkan sikap", "sopan dan menghargai guru", ["mengganggu pelajaran", "malas belajar", "tidak peduli"], "Mengangkat tangan adalah adab bertanya.", 'easy',
  "Di dalam kelas, seorang murid mengangkat tangan sementara guru berdiri di depan papan tulis."),
 (4, "Perhatikan gambar! Beberapa murid menyapu dan merapikan kelas bersama-sama. Sikap itu menunjukkan ....", "Gambar murid membersihkan kelas bersama menunjukkan", "kerja sama dan cinta lingkungan", ["kemalasan", "suka membuat kotor", "tidak peduli"], "Bekerja sama menjaga kebersihan.", 'easy',
  "Empat murid: dua menyapu, satu merapikan kursi, satu mengelap papan tulis di dalam kelas."),
 (4, "Perhatikan gambar! Murid-murid berbaris rapi menunggu giliran membeli makanan di مَقْصَفٌ (kantin). Sikap itu menunjukkan ....", "Gambar murid mengantre di مَقْصَفٌ menunjukkan sikap", "tertib dan sabar", ["berebut dan mendorong", "tidak sabar", "memotong antrean"], "Mengantre adalah akhlak baik.", 'easy',
  "Enam murid berbaris rapi di depan kantin sekolah menunggu giliran."),
]

ADAB = {  # fakta tambahan TP4: (pernyataan, benar?, penjelasan)
 'PK': [("Memperkenalkan diri dengan sopan dimulai dengan salam.", True, "Salam membuka perkenalan dengan baik."),
        ("Saat berkenalan, kita boleh memalingkan wajah dari teman baru.", False, "Kita menghadap, tersenyum, dan ramah."),
        ("Ucapan \"شُكْرًا\" dipakai untuk berterima kasih.", True, "شُكْرًا berarti terima kasih."),
        ("Ucapan \"عَفْوًا\" dipakai untuk menjawab terima kasih.", True, "عَفْوًا berarti sama-sama."),
        ("Menyebutkan nama palsu kepada teman adalah sikap jujur.", False, "Jujur berarti menyebut nama sendiri."),
        ("Menyapa teman baru dengan ramah adalah wujud cinta sesama.", True, "Ramah adalah akhlak terpuji."),
        ("\"مَرْحَبًا\" dipakai untuk mengucapkan selamat tinggal.", False, "مَرْحَبًا berarti selamat datang/halo."),
        ("Menjawab salam hukumnya dianjurkan dengan jawaban yang sama atau lebih baik.", True, "Salam dijawab dengan وَعَلَيْكُمُ السَّلَامُ.")],
 'KL': [("Mencium tangan orang tua adalah tanda hormat.", True, "Menghormati orang tua."),
        ("Membantu ibu di rumah adalah wujud sayang kepada keluarga.", True, "Membantu keluarga."),
        ("Membentak kakek dan nenek adalah sikap terpuji.", False, "Kita harus lembut kepada orang tua dan lansia."),
        ("Kata \"هُوَ أَبِيْ\" dipakai untuk menjawab pertanyaan tentang laki-laki.", True, "هُوَ untuk laki-laki."),
        ("Bertengkar dengan saudara tidak perlu minta maaf.", False, "Meminta maaf menjaga keharmonisan."),
        ("Mendoakan keluarga adalah sikap yang baik.", True, "Mendoakan keluarga adalah bentuk sayang."),
        ("Mendengarkan nasihat ayah dan ibu adalah sikap terpuji.", True, "Menaati nasihat orang tua."),
        ("Berteriak kepada adik agar cepat tidur adalah sikap menyayangi.", False, "Menyayangi adik dengan kelembutan.")],
 'RM': [("Membuang sampah pada tempatnya menjaga kebersihan rumah.", True, "Cinta lingkungan."),
        ("Menyapu halaman termasuk menjaga kebersihan lingkungan rumah.", True, "Halaman bersih membuat rumah nyaman."),
        ("Membiarkan kamar berantakan adalah kebiasaan baik.", False, "Merapikan kamar adalah kebiasaan baik."),
        ("Mematikan lampu yang tidak dipakai adalah sikap hemat.", True, "Hemat energi."),
        ("Mencuci piring setelah makan membantu menjaga kebersihan rumah.", True, "Rumah tetap bersih."),
        ("Meludah sembarangan di dalam rumah tidak masalah.", False, "Itu mengotori rumah dan menyebarkan penyakit."),
        ("Merapikan sepatu di rak menjaga kerapian rumah.", True, "Rumah rapi dan nyaman."),
        ("Membersihkan rumah bersama keluarga adalah kerja sama yang baik.", True, "Gotong royong dalam keluarga.")],
 'SK': [("Mendengarkan guru dengan baik adalah wujud cinta ilmu.", True, "Belajar sungguh-sungguh."),
        ("Mengobrol keras saat guru menjelaskan adalah sikap terpuji.", False, "Kita harus mendengarkan guru."),
        ("Meminjamkan pena kepada teman adalah sikap saling menolong.", True, "Berbagi dengan teman."),
        ("Mengucap salam kepada guru saat bertemu adalah adab yang baik.", True, "Menghormati guru."),
        ("Membuang sampah di laci meja tidak masalah.", False, "Sampah dibuang di tempat sampah."),
        ("Mengangkat tangan sebelum bertanya adalah adab belajar.", True, "Sopan di kelas."),
        ("Berlari dan berteriak di perpustakaan adalah sikap terpuji.", False, "Perpustakaan harus tenang."),
        ("Belajar bersama teman dengan sabar adalah sikap yang baik.", True, "Saling membantu belajar.")],
}

PERF = {
 'PK': ["Perkenalkan dirimu kepada temanmu menggunakan kalimat \"اِسْمِيْ ....\" dan ucapkan salam!",
        "Bermain peran: tanyakan nama temanmu dengan \"مَا اسْمُكَ؟\" atau \"مَا اسْمُكِ؟\" lalu jawab dengan \"اِسْمِيْ ....\"!",
        "Peragakan percakapan salam: \"اَلسَّلَامُ عَلَيْكُمْ\" dan jawabannya bersama teman!",
        "Peragakan percakapan menanyakan kabar: \"كَيْفَ حَالُكَ؟\" dan jawabannya!",
        "Sapalah gurumu di pagi hari dengan \"صَبَاحُ الْخَيْرِ\" dan jawab sapaan balik dengan benar!",
        "Peragakan ucapan terima kasih dan jawabannya: \"شُكْرًا\" dan \"عَفْوًا\"!",
        "Sambutlah tamu kelas dengan \"أَهْلًا وَسَهْلًا\" dan berpamitan dengan \"مَعَ السَّلَامَةِ\"!",
        "Tulislah dalam bahasa Arab satu kalimat perkenalan dirimu dengan rapi!"],
 'KL': ["Tunjukkan foto keluargamu dan sebutkan anggota keluarga dengan \"هُوَ أَبِيْ\" dan \"هِيَ أُمِّيْ\"!",
        "Bermain peran bersama teman: satu bertanya \"مَنْ هُوَ؟\" dan satu menjawab!",
        "Gambarlah keluargamu dan beri tulisan Arab untuk setiap anggota!",
        "Ceritakan di depan kelas bagaimana kamu menyayangi anggota keluargamu!",
        "Peragakan cara mencium tangan orang tua dan mengucap salam!",
        "Tulislah kata أَبِيْ، أُمِّيْ، أَخِيْ، أُخْتِيْ dengan rapi di bukumu!",
        "Nyanyikan atau ucapkan daftar anggota keluarga dalam bahasa Arab secara berurutan!",
        "Buatlah kartu ucapan sederhana untuk ibumu yang bertuliskan \"شُكْرًا\" dan hiasan hati!"],
 'RM': ["Tunjuk dan sebutkan bagian rumah dalam bahasa Arab dengan pola \"هٰذَا .... / هٰذِهِ ....\"!",
        "Bermain peran: tanyakan \"مَا هٰذَا؟\" atau \"مَا هٰذِهِ؟\" lalu jawab sesuai benda!",
        "Gambarlah rumahmu dan beri label Arab pada pintu, jendela, dan kamar!",
        "Rapikan kamarmu di rumah lalu ceritakan kegiatanmu kepada guru!",
        "Peragakan cara membersihkan rumah bersama keluarga dan sebutkan nama alatnya dalam bahasa Arab!",
        "Tulislah kata بَيْتٌ، بَابٌ، نَافِذَةٌ، غُرْفَةٌ dengan rapi!",
        "Tempelkan kartu kosakata Arab pada benda-benda di kelas atau rumah!",
        "Tunjuk benda jauh dan dekat memakai ذٰلِكَ dan تِلْكَ, هٰذَا dan هٰذِهِ!"],
 'SK': ["Tunjuk perlengkapan sekolahmu dan sebutkan namanya dalam bahasa Arab!",
        "Bermain peran: satu murid sebagai guru bertanya \"مَا هٰذَا؟\", satu murid menjawab!",
        "Gambarlah madrasahmu dan beri label Arab pada kelas, masjid, dan perpustakaan!",
        "Ikuti piket kelas dengan sungguh-sungguh lalu ceritakan pengalamanmu!",
        "Peragakan cara bertanya kepada guru dengan sopan!",
        "Tulislah kata قَلَمٌ، كِتَابٌ، حَقِيْبَةٌ، مِسْطَرَةٌ dengan rapi!",
        "Ucapkan salam kepada guru dan teman ketika masuk kelas!",
        "Buatlah kartu kosakata tentang benda di sekolah bersama kelompokmu!"],
}

GROUPS = {  # (pertanyaan, {kelompok: [item]})
 'PK': [("Kelompokkan ucapan berikut berdasarkan waktu/keperluannya: 'صَبَاحُ الْخَيْرِ'; 'مَسَاءُ الْخَيْرِ'; 'مَرْحَبًا'; 'أَهْلًا وَسَهْلًا'; 'مَعَ السَّلَامَةِ'; 'شُكْرًا'.",
         {'ucapan sapaan/penyambutan': ['صَبَاحُ الْخَيْرِ', 'مَسَاءُ الْخَيْرِ', 'مَرْحَبًا', 'أَهْلًا وَسَهْلًا'], 'ucapan penutup/terima kasih': ['مَعَ السَّلَامَةِ', 'شُكْرًا']}),
        ("Kelompokkan kata berikut menjadi kata ganti orang: 'أَنَا'; 'هُوَ'; 'هِيَ'; 'اِسْمٌ'; 'تِلْمِيْذٌ'; 'أَنْتَ'.",
         {'kata ganti orang': ['أَنَا', 'هُوَ', 'هِيَ', 'أَنْتَ'], 'kata benda': ['اِسْمٌ', 'تِلْمِيْذٌ']}),
        ("Kelompokkan kata berikut untuk laki-laki atau perempuan: 'تِلْمِيْذٌ'; 'تِلْمِيْذَةٌ'; 'صَدِيْقٌ'; 'صَدِيْقَةٌ'; 'وَلَدٌ'; 'بِنْتٌ'.",
         {'laki-laki': ['تِلْمِيْذٌ', 'صَدِيْقٌ', 'وَلَدٌ'], 'perempuan': ['تِلْمِيْذَةٌ', 'صَدِيْقَةٌ', 'بِنْتٌ']})],
 'KL': [("Kelompokkan anggota keluarga berikut: 'أَبٌ'; 'أُمٌّ'; 'جَدٌّ'; 'جَدَّةٌ'; 'أَخٌ'; 'أُخْتٌ'.",
         {'laki-laki': ['أَبٌ', 'جَدٌّ', 'أَخٌ'], 'perempuan': ['أُمٌّ', 'جَدَّةٌ', 'أُخْتٌ']}),
        ("Kelompokkan sikap berikut terhadap keluarga: 'mencium tangan orang tua'; 'membantu ibu'; 'membentak kakek'; 'menghibur adik'; 'mengejek kakak'; 'menjenguk nenek'.",
         {'sikap terpuji': ['mencium tangan orang tua', 'membantu ibu', 'menghibur adik', 'menjenguk nenek'], 'sikap tercela': ['membentak kakek', 'mengejek kakak']}),
        ("Kelompokkan pertanyaan/jawaban berikut: 'مَنْ هُوَ؟'; 'هُوَ أَبِيْ'; 'مَنْ هِيَ؟'; 'هِيَ أُمِّيْ'.",
         {'tentang laki-laki': ['مَنْ هُوَ؟', 'هُوَ أَبِيْ'], 'tentang perempuan': ['مَنْ هِيَ؟', 'هِيَ أُمِّيْ']})],
 'RM': [("Kelompokkan benda berikut: 'مَطْبَخٌ'; 'حَمَّامٌ'; 'غُرْفَةٌ'; 'مِصْبَاحٌ'; 'مِكْنَسَةٌ'; 'سَرِيْرٌ'.",
         {'bagian rumah': ['مَطْبَخٌ', 'حَمَّامٌ', 'غُرْفَةٌ'], 'perabot/alat': ['مِصْبَاحٌ', 'مِكْنَسَةٌ', 'سَرِيْرٌ']}),
        ("Kelompokkan kata berikut: 'بَيْتٌ'; 'غُرْفَةٌ'; 'بَابٌ'; 'نَافِذَةٌ'; 'مَطْبَخٌ'; 'حَدِيْقَةٌ'.",
         {'memakai هٰذَا': ['بَيْتٌ', 'بَابٌ', 'مَطْبَخٌ'], 'memakai هٰذِهِ': ['غُرْفَةٌ', 'نَافِذَةٌ', 'حَدِيْقَةٌ']}),
        ("Kelompokkan kegiatan berikut: 'menyapu lantai'; 'membuang sampah sembarangan'; 'merapikan kamar'; 'meludah sembarangan'; 'menyiram tanaman'; 'membiarkan piring kotor'.",
         {'menjaga kebersihan': ['menyapu lantai', 'merapikan kamar', 'menyiram tanaman'], 'mengotori': ['membuang sampah sembarangan', 'meludah sembarangan', 'membiarkan piring kotor']})],
 'SK': [("Kelompokkan benda berikut: 'قَلَمٌ'; 'كِتَابٌ'; 'مَسْجِدٌ'; 'مَكْتَبَةٌ'; 'مِسْطَرَةٌ'; 'مَلْعَبٌ'.",
         {'alat tulis dan buku': ['قَلَمٌ', 'كِتَابٌ', 'مِسْطَرَةٌ'], 'tempat di sekolah': ['مَسْجِدٌ', 'مَكْتَبَةٌ', 'مَلْعَبٌ']}),
        ("Kelompokkan kata berikut: 'مُدَرِّسٌ'; 'مُدَرِّسَةٌ'; 'تِلْمِيْذٌ'; 'تِلْمِيْذَةٌ'.",
         {'laki-laki': ['مُدَرِّسٌ', 'تِلْمِيْذٌ'], 'perempuan': ['مُدَرِّسَةٌ', 'تِلْمِيْذَةٌ']}),
        ("Kelompokkan sikap berikut di sekolah: 'mendengarkan guru'; 'berbagi pena'; 'berteriak di kelas'; 'membuang sampah di tempatnya'; 'mencoret meja'; 'mengantre di kantin'.",
         {'sikap terpuji': ['mendengarkan guru', 'berbagi pena', 'membuang sampah di tempatnya', 'mengantre di kantin'], 'sikap tercela': ['berteriak di kelas', 'mencoret meja']})],
}

ORDERS = {
 'PK': [("Urutkan kegiatan perkenalan berikut!", ["Tersenyum kepada teman baru", "Mengucap \"اَلسَّلَامُ عَلَيْكُمْ\"", "Menyebut \"اِسْمِيْ ....\"", "Menanyakan \"مَا اسْمُكَ؟\""]),
        ("Urutkan percakapan salam berikut!", ["اَلسَّلَامُ عَلَيْكُمْ", "وَعَلَيْكُمُ السَّلَامُ", "كَيْفَ حَالُكَ؟", "أَنَا بِخَيْرٍ"])],
 'KL': [("Urutkan kegiatan menyambut ayah pulang kerja berikut!", ["Membukakan pintu", "Mengucap salam", "Mencium tangan ayah", "Mengambilkan air minum"]),
        ("Urutkan percakapan tentang anggota keluarga berikut!", ["مَنْ هُوَ؟", "هُوَ أَبِيْ", "مَنْ هِيَ؟", "هِيَ أُمِّيْ"])],
 'RM': [("Urutkan kegiatan membersihkan rumah berikut!", ["Merapikan barang", "Menyapu lantai", "Membuang sampah ke tempat sampah", "Mencuci tangan"]),
        ("Urutkan percakapan berikut!", ["مَا هٰذَا؟", "هٰذَا بَيْتٌ", "مَا هٰذِهِ؟", "هٰذِهِ غُرْفَةٌ"])],
 'SK': [("Urutkan kegiatan di kelas berikut!", ["Mengucap salam kepada guru", "Duduk dengan rapi", "Mendengarkan penjelasan guru", "Mencatat pelajaran"]),
        ("Urutkan percakapan berikut!", ["مَا هٰذَا؟", "هٰذَا قَلَمٌ", "مَا هٰذِهِ؟", "هٰذِهِ حَقِيْبَةٌ"])],
}


def apply(p, code):
    for si, (tp, long, short, ok, bad, expl, diff, vis) in enumerate(SCEN[code]):
        p.gk = f'sc{code}{si}'
        if vis:
            p.mc(tp, long, ok, bad, expl, diff, 'menerapkan', 'Menerapkan sikap dan ungkapan', visual=vis)
            continue
        p.ctx(tp, long, ok, bad, expl, diff, 'menerapkan', 'Menerapkan sikap dan ungkapan')
        p.tf(tp, f'{short} {ok}.', True, expl, 'easy' if diff == 'easy' else 'medium', 'memahami', 'Menerapkan sikap dan ungkapan')
        p.tf(tp, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', 'Menerapkan sikap dan ungkapan')
        p.fill(tp, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', 'Menerapkan sikap dan ungkapan', typ='completion')
    p.gk = None
    for fi, (st, truth, expl) in enumerate(ADAB[code]):
        p.gk = f'ad{code}{fi}'
        p.tf(4, st, truth, expl, 'easy', 'memahami', 'Menerapkan sikap dan ungkapan')
    p.gk = None
    for q, r in [(q, 'Dinilai guru: ketepatan ungkapan/lafal, keberanian, dan kesantunan (skala 1-4).') for q in PERF[code]]:
        p.perf(4, q, r, 'Murid menunjukkan penerapan ungkapan dan sikap yang sesuai.', 'medium', 'menerapkan', 'Menerapkan sikap dan ungkapan')
    for q, g in GROUPS[code]:
        p.group(4, q, g, 'Kelompokkan sesuai makna dan jenisnya.', 'medium', 'mengelompokkan', 'Menerapkan sikap dan ungkapan')
    for q, items in ORDERS[code]:
        p.order(4, q, items, 'Urutan yang benar: ' + ' → '.join(items) + '.', 'medium', 'mengurutkan', 'Menerapkan sikap dan ungkapan')
