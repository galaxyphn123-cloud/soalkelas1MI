# -*- coding: utf-8 -*-
"""Materi: Hadis tentang Kebersihan (HK)."""
import random
import lib
import surah_scen

AR = 'الطُّهُورُ شَطْرُ الْإِيمَانِ'
LA = 'Ath-thuhuru syathrul iman'
ARTI = 'Kebersihan itu sebagian dari iman'
WORDS = [('الطُّهُورُ', 'ath-thuhuru', 'kebersihan'), ('شَطْرُ', 'syathru', 'sebagian'), ('الْإِيمَانِ', 'al-iman', 'iman')]
WRONG_LA = ['Ath-thuhuru syathrul islam', 'Ash-shalatu syathrul iman', 'Ath-thuhuru nurul iman', 'Al-ilmu syathrul iman', 'Ath-thuhuru syathrul ihsan']
WRONG_AR = ['الطُّهُورُ شَطْرُ الْإِسْلَامِ', 'الصَّلَاةُ شَطْرُ الْإِيمَانِ', 'الطُّهُورُ نُورُ الْإِيمَانِ', 'الْعِلْمُ شَطْرُ الْإِيمَانِ', 'الطُّهُورُ شَطْرُ الْإِحْسَانِ']
WRONG_ARTI = ['Kebersihan itu sebagian dari Islam', 'Salat itu sebagian dari iman', 'Kebersihan itu cahaya bagi iman', 'Ilmu itu sebagian dari iman', 'Kebersihan itu tidak penting bagi iman']

GOOD = {  # (kegiatan, tempat/jenis, manfaat)
 'diri': [('mencuci tangan dengan sabun sebelum makan', 'kuman tidak masuk ke tubuh'), ('mandi dua kali sehari', 'badan bersih dan segar'),
          ('menyikat gigi sebelum tidur', 'gigi sehat dan mulut tidak bau'), ('memotong kuku secara teratur', 'kuman tidak bersembunyi di kuku'),
          ('menyisir rambut agar rapi', 'penampilan rapi dan nyaman'), ('memakai pakaian yang bersih', 'badan nyaman dan sehat'),
          ('mencuci tangan setelah dari toilet', 'kuman tidak menyebar'), ('mencuci kaki sebelum tidur', 'tubuh bersih saat beristirahat'),
          ('mengganti seragam yang kotor', 'pakaian tetap bersih'), ('menutup mulut dengan siku saat bersin', 'tidak menularkan kuman ke teman')],
 'lingkungan': [('membuang sampah pada tempatnya', 'lingkungan bersih dan indah'), ('menyapu kelas saat piket', 'kelas bersih dan nyaman belajar'),
                ('merapikan tempat tidur setelah bangun', 'kamar rapi dan sehat'), ('membersihkan halaman rumah', 'halaman asri dan sehat'),
                ('menyiram toilet setelah dipakai', 'toilet tetap bersih'), ('memilah sampah organik dan anorganik', 'sampah mudah diolah'),
                ('menjaga kebersihan masjid atau musala', 'tempat ibadah nyaman'), ('menutup tempat sampah', 'sampah tidak berserakan dan tidak berbau'),
                ('mencuci piring setelah makan', 'peralatan makan bersih'), ('menyiram tanaman dan merawat taman sekolah', 'sekolah hijau dan asri')],
}
BAD = {
 'diri': ['makan tanpa mencuci tangan', 'jarang mandi', 'tidak menyikat gigi', 'membiarkan kuku panjang dan hitam', 'memakai baju kotor berhari-hari', 'tidak mencuci tangan setelah dari toilet', 'bersin tanpa menutup mulut'],
 'lingkungan': ['membuang bungkus jajanan sembarangan', 'mencoret-coret dinding kelas', 'membiarkan kamar berantakan', 'meludah sembarangan', 'membuang sampah ke sungai', 'meninggalkan sisa makanan di meja', 'tidak menyiram toilet setelah dipakai'],
}

AKIBAT = {
 'makan tanpa mencuci tangan': 'membuat kuman masuk ke perut', 'jarang mandi': 'membuat badan bau dan mudah gatal',
 'tidak menyikat gigi': 'membuat gigi berlubang', 'membiarkan kuku panjang dan hitam': 'membuat kuman bersarang di kuku',
 'memakai baju kotor berhari-hari': 'membuat badan gatal dan tidak sehat', 'tidak mencuci tangan setelah dari toilet': 'membuat kuman menyebar',
 'bersin tanpa menutup mulut': 'menularkan kuman kepada teman', 'membuang bungkus jajanan sembarangan': 'membuat sekolah kotor',
 'mencoret-coret dinding kelas': 'membuat kelas kotor dan tidak indah', 'membiarkan kamar berantakan': 'membuat kamar tidak nyaman dan berdebu',
 'meludah sembarangan': 'membuat tempat kotor dan menyebarkan penyakit', 'membuang sampah ke sungai': 'membuat sungai tercemar dan banjir',
 'meninggalkan sisa makanan di meja': 'mengundang lalat dan semut', 'tidak menyiram toilet setelah dipakai': 'membuat toilet kotor dan bau'}


def build(seed=21):
    rng = random.Random(seed)
    tps = ['Murid mampu menjelaskan pesan pokok hadis tentang kebersihan dengan benar.',
           'Murid mampu menyesuaikan pelafalan dan menghafal hadis tentang kebersihan dengan benar.',
           'Murid mampu menyebutkan arti hadis tentang kebersihan dengan benar.',
           'Murid mampu menerapkan pola perilaku hidup bersih dengan benar dalam kehidupan sehari-hari sebagai wujud cinta Allah dan Rasul-Nya, cinta diri dan sesama manusia, serta cinta lingkungan.']
    p = lib.Pool('HK', 'Hadis tentang Kebersihan', tps, 142, tpw=(34, 22, 25, 61))
    goods = [(k, g[0], g[1]) for k, v in GOOD.items() for g in v]
    bads = [(k, b) for k, v in BAD.items() for b in v]
    allgood = [g[1] for g in goods]; allbad = [b[1] for b in bads]

    # ================= TP1: pesan pokok =================
    P1 = 'kebersihan merupakan bagian dari iman'
    p.mc(1, 'Hadis "Ath-thuhuru syathrul iman" berpesan bahwa ....', P1, ['kebersihan tidak berkaitan dengan iman', 'kebersihan hanya penting saat hari raya', 'iman hanya tentang salat'], 'Kebersihan adalah bagian dari iman.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.mc(1, 'Pesan pokok hadis tentang kebersihan adalah ....', 'menjaga kebersihan adalah bagian dari iman', ['bermain sepanjang hari', 'menghafal banyak surah saja', 'bekerja keras mencari uang'], 'Pesan pokok hadis: kebersihan sebagian dari iman.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.mc(1, 'Hadis tentang kebersihan diriwayatkan oleh ....', 'Imam Muslim', ['Imam Syafi\'i', 'Imam Malik', 'Imam Ahmad'], 'Hadis ini diriwayatkan oleh Imam Muslim (HR. Muslim).', 'hard', 'mengingat', 'Mengenal hadis kebersihan')
    p.fill(1, 'Hadis "Ath-thuhuru syathrul iman" diriwayatkan oleh Imam ....', 'Muslim', 'Hadis tersebut diriwayatkan oleh Imam Muslim.', 'hard', 'mengingat', 'Mengenal hadis kebersihan')
    p.tf(1, 'Menjaga kebersihan termasuk bagian dari iman.', True, 'Benar, kebersihan sebagian dari iman.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.tf(1, 'Menjaga kebersihan tidak ada hubungannya dengan iman.', False, 'Salah. Kebersihan adalah sebagian dari iman.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.tf(1, 'Orang beriman dianjurkan menjaga kebersihan badan, pakaian, dan lingkungannya.', True, 'Benar, hadis ini mengajarkan hidup bersih.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.tf(1, 'Kebersihan hanya penting bagi orang dewasa.', False, 'Salah. Semua orang, termasuk anak-anak, perlu menjaga kebersihan.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.tf(1, 'Allah menyukai orang yang menjaga kebersihan dan kesucian.', True, 'Benar, Allah mencintai orang yang bersuci.', 'medium', 'memahami', 'Menjelaskan pesan hadis')
    p.tf(1, 'Hadis tentang kebersihan hanya berlaku di bulan Ramadan.', False, 'Salah. Kebersihan harus dijaga setiap hari.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.mc(1, 'Menurut hadis tentang kebersihan, orang yang menjaga kebersihan berarti ....', 'menjaga sebagian dari imannya', ['menyia-nyiakan waktunya', 'mengabaikan ibadah', 'bermalas-malasan'], 'Kebersihan sebagian dari iman.', 'medium', 'memahami', 'Menjelaskan pesan hadis')
    p.mc(1, 'Kebersihan yang diajarkan hadis mencakup kebersihan ....', 'badan, pakaian, tempat, dan lingkungan', ['badan saja', 'pakaian saja', 'hanya tempat salat'], 'Kebersihan mencakup diri, pakaian, tempat, dan lingkungan.', 'medium', 'memahami', 'Menjelaskan pesan hadis')
    p.mc(1, 'Salah satu manfaat menjaga kebersihan adalah ....', 'terhindar dari penyakit', ['mudah sakit', 'banyak kuman', 'tempat menjadi kotor'], 'Hidup bersih membuat kita sehat.', 'easy', 'memahami', 'Menjelaskan manfaat kebersihan')
    p.mc(1, 'Manfaat menjaga kebersihan kelas adalah ....', 'belajar menjadi nyaman', ['kelas menjadi bau', 'banyak sampah', 'teman menjadi sakit'], 'Kelas bersih membuat nyaman belajar.', 'easy', 'memahami', 'Menjelaskan manfaat kebersihan')
    p.mc(1, 'Kebersihan juga merupakan syarat sahnya ibadah, misalnya sebelum salat kita harus ....', 'bersuci (berwudu)', ['makan dahulu', 'bermain dahulu', 'tidur dahulu'], 'Salat memerlukan kesucian badan, pakaian, dan tempat.', 'medium', 'memahami', 'Menjelaskan manfaat kebersihan')
    p.fill(1, 'Kebersihan itu sebagian dari ....', 'iman', 'Hadis: Ath-thuhuru syathrul iman.', 'easy', 'mengingat', 'Menjelaskan pesan hadis')
    p.fill(1, 'Hadis kebersihan mengajarkan kita untuk selalu hidup ....', 'bersih', 'Hidup bersih adalah ajaran Islam.', 'easy', 'memahami', 'Menjelaskan pesan hadis')
    p.fill(1, 'Dengan menjaga kebersihan, kita terhindar dari ....', 'penyakit', 'Kuman penyebab penyakit berkurang.', 'easy', 'memahami', 'Menjelaskan manfaat kebersihan', typ='completion')
    p.mc(1, 'Kebersihan lingkungan dapat dimulai dari ....', 'diri sendiri dan hal-hal kecil', ['orang lain saja', 'pemerintah saja', 'ketika sudah dewasa'], 'Kebersihan dimulai dari diri sendiri.', 'medium', 'memahami', 'Menjelaskan manfaat kebersihan')
    p.mc(1, 'Menjaga kebersihan kelas, halaman, dan sungai merupakan wujud cinta ....', 'lingkungan', ['mainan', 'jajanan', 'hewan peliharaan saja'], 'Menjaga kebersihan tempat di sekitar kita adalah wujud cinta lingkungan.', 'medium', 'memahami', 'Menjelaskan pesan hadis')
    p.group(1, 'Kelompokkan manfaat berikut: badan segar, terhindar penyakit, kelas nyaman, tempat berbau, banyak kuman, sampah berserakan.',
            {'manfaat kebersihan': ['badan segar', 'terhindar penyakit', 'kelas nyaman'], 'akibat tidak bersih': ['tempat berbau', 'banyak kuman', 'sampah berserakan']},
            'Kebersihan memberi manfaat, ketidakbersihan menimbulkan masalah.', 'medium', 'mengelompokkan', 'Menjelaskan manfaat kebersihan')
    p.match(1, 'Jodohkan kegiatan dengan manfaatnya!', [('mencuci tangan', 'kuman tidak masuk ke tubuh'), ('menyikat gigi', 'gigi sehat'), ('memotong kuku', 'kuman tidak bersembunyi'), ('membuang sampah pada tempatnya', 'lingkungan bersih')],
            'Setiap kegiatan bersih memiliki manfaat.', 'medium', 'mencocokkan', 'Menjelaskan manfaat kebersihan')
    p.match(1, 'Jodohkan kegiatan dengan alat yang digunakan!', [('mencuci tangan', 'sabun dan air'), ('menyapu lantai', 'sapu'), ('memotong kuku', 'gunting kuku'), ('membuang sampah', 'tempat sampah')],
            'Setiap kegiatan membutuhkan alat yang tepat.', 'medium', 'mencocokkan', 'Menjelaskan manfaat kebersihan')
    p.match(1, 'Jodohkan benda dengan fungsinya untuk menjaga kebersihan!', [('sabun', 'membersihkan tangan dan badan'), ('sikat gigi', 'membersihkan gigi'), ('sisir', 'merapikan rambut'), ('sapu', 'membersihkan lantai')],
            'Alat kebersihan membantu hidup bersih.', 'easy', 'mencocokkan', 'Menjelaskan manfaat kebersihan')
    p.perf(1, 'Jelaskan dengan bahasamu sendiri mengapa kebersihan itu sebagian dari iman!', 'Dinilai guru: ketepatan penjelasan hubungan kebersihan dan iman (skala 1-4).', 'Murid menjelaskan pesan pokok hadis.', 'medium', 'memahami', 'Menjelaskan pesan hadis')
    p.perf(1, 'Sebutkan tiga manfaat menjaga kebersihan kepada temanmu!', 'Dinilai guru: ketepatan manfaat dan kejelasan penyampaian (skala 1-4).', 'Murid menyebutkan manfaat kebersihan.', 'easy', 'memahami', 'Menjelaskan manfaat kebersihan')

    # ================= TP2: pelafalan =================
    p.mc(2, 'Hadis tentang kebersihan dibaca ....', LA, WRONG_LA, f'Hadis dibaca "{LA}".', 'easy', 'mengingat', 'Melafalkan hadis')
    p.mc(2, f'Cara membaca tulisan Arab {AR} adalah ....', LA, WRONG_LA, f'{AR} dibaca "{LA}".', 'easy', 'mengenali', 'Melafalkan hadis')
    p.mc(2, f'Tulisan Arab dari bacaan "{LA}" adalah ....', AR, WRONG_AR, f'"{LA}" ditulis {AR}.', 'medium', 'mengenali', 'Melafalkan hadis')
    p.tf(2, f'Hadis tentang kebersihan berbunyi "{LA}".', True, f'Benar, bunyinya "{LA}".', 'easy', 'mengingat', 'Melafalkan hadis')
    for i, w in enumerate(WRONG_LA):
        p.tf(2, f'Hadis tentang kebersihan berbunyi "{w}".', False, f'Salah. Bunyi yang benar: "{LA}".', 'medium', 'mengingat', 'Melafalkan hadis')
        p.tf(2, f'Tulisan {WRONG_AR[i]} dibaca "{LA}".', False, f'Salah. {WRONG_AR[i]} bukan hadis kebersihan; hadis kebersihan ditulis {AR}.', 'hard', 'mengenali', 'Melafalkan hadis')
    p.fill(2, 'Banyaknya kata dalam hadis tentang kebersihan adalah ....', '3', 'Tiga kata: ath-thuhuru, syathrul, iman.', 'easy', 'mengingat', 'Melafalkan hadis')
    p.mc(2, 'Hadis tentang kebersihan terdiri dari ... kata.', '3', ['2', '4', '5'], 'Tiga kata: ath-thuhuru, syathrul, iman.', 'easy', 'mengingat', 'Melafalkan hadis')
    ordn = ['pertama', 'kedua', 'ketiga']
    for i, (a, l, t) in enumerate(WORDS):
        others_l = [w[1] for j, w in enumerate(WORDS) if j != i] + ['an-nazhafatu', 'shalatun']
        others_a = [w[0] for j, w in enumerate(WORDS) if j != i] + ['الصَّلَاةُ', 'النَّظَافَةُ']
        p.mc(2, f'Kata {ordn[i]} hadis tentang kebersihan dibaca ....', l, others_l, f'Kata {ordn[i]} adalah {a} ({l}).', 'easy', 'mengingat', 'Melafalkan hadis')
        p.mc(2, f'Kata {ordn[i]} hadis tentang kebersihan ditulis ....', a, others_a, f'Kata {ordn[i]} adalah {a}.', 'medium', 'mengenali', 'Melafalkan hadis')
        words = LA.split(' ')
        blank = ' '.join('....' if j == i else x for j, x in enumerate(words))
        p.fill(2, f'Lengkapi bacaan hadis kebersihan: {blank}', words[i], f'Bacaan lengkap: {LA}.', 'medium', 'mengingat', 'Menghafal hadis', typ='completion')
        awords = AR.split(' ')
        ablank = ' '.join('....' if j == i else x for j, x in enumerate(awords))
        p.mc(2, f'Kata Arab yang melengkapi hadis berikut adalah ....\n{ablank}', awords[i], others_a, f'Hadis lengkap: {AR}.', 'hard', 'mengenali', 'Menghafal hadis')
        p.tf(2, f'Kata {ordn[i]} hadis tentang kebersihan adalah "{l}".', True, f'Benar, kata {ordn[i]} adalah {l}.', 'easy', 'mengingat', 'Melafalkan hadis')
        p.tf(2, f'Kata {ordn[i]} hadis tentang kebersihan adalah "{WORDS[(i + 1) % 3][1]}".', False, f'Salah. Kata {ordn[i]} adalah {l}.', 'medium', 'mengingat', 'Melafalkan hadis')
    p.order(2, 'Urutkan kata-kata hadis tentang kebersihan berikut (tulisan Latin)!', ['Ath-thuhuru', 'syathrul', 'iman'], f'Urutan: {LA}.', 'medium', 'mengurutkan', 'Menghafal hadis')
    p.order(2, 'Urutkan kata-kata hadis tentang kebersihan berikut (tulisan Arab)!', [w[0] for w in WORDS], f'Urutan: {AR}.', 'hard', 'mengurutkan', 'Menghafal hadis')
    p.perf(2, f'Bacalah hadis {AR} dengan lafal yang benar di depan guru!', 'Dinilai guru: ketepatan lafal, kelancaran, dan kejelasan suara (skala 1-4).', 'Murid melafalkan hadis dengan benar.', 'medium', 'menerapkan', 'Melafalkan hadis')
    p.perf(2, 'Hafalkan hadis tentang kebersihan dan bacakan tanpa melihat tulisan!', 'Dinilai guru: kelengkapan hafalan dan ketepatan lafal (skala 1-4).', 'Murid menghafal hadis.', 'hard', 'menerapkan', 'Menghafal hadis')
    p.perf(2, 'Bacalah hadis tentang kebersihan bersama temanmu secara bergantian kata demi kata!', 'Dinilai guru: ketepatan lafal dan kerja sama (skala 1-4).', 'Murid membaca hadis bergantian.', 'medium', 'menerapkan', 'Melafalkan hadis')
    p.perf(2, 'Tulislah hadis tentang kebersihan dengan huruf Arab di bukumu, lalu bacakan!', 'Dinilai guru: ketepatan tulisan, kerapian, dan bacaan (skala 1-4).', 'Murid menulis dan membaca hadis.', 'hard', 'menerapkan', 'Menghafal hadis')

    # ================= TP3: arti =================
    p.mc(3, f'Arti hadis "{LA}" adalah ....', ARTI, WRONG_ARTI, f'"{LA}" artinya "{ARTI}".', 'easy', 'memahami', 'Menyebutkan arti hadis')
    p.mc(3, f'Arti dari tulisan {AR} adalah ....', ARTI, WRONG_ARTI, f'{AR} artinya "{ARTI}".', 'medium', 'memahami', 'Menyebutkan arti hadis')
    p.mc(3, f'Hadis yang artinya "{ARTI}" dibaca ....', LA, WRONG_LA, f'"{ARTI}" adalah arti dari "{LA}".', 'medium', 'memahami', 'Menyebutkan arti hadis')
    p.fill(3, f'Hadis "{LA}" artinya "Kebersihan itu sebagian dari ...."', 'iman', f'Artinya: {ARTI}.', 'easy', 'mengingat', 'Menyebutkan arti hadis', typ='completion')
    p.fill(3, f'Arti hadis {AR} adalah ....', ARTI, f'Artinya: {ARTI}.', 'medium', 'mengingat', 'Menyebutkan arti hadis')
    p.tf(3, f'Hadis "{LA}" artinya "{ARTI}".', True, f'Benar, artinya "{ARTI}".', 'easy', 'mengingat', 'Menyebutkan arti hadis')
    for a in WRONG_ARTI:
        p.tf(3, f'Hadis "{LA}" artinya "{a}".', False, f'Salah. Artinya "{ARTI}".', 'medium', 'memahami', 'Menyebutkan arti hadis')
    for i, (a, l, t) in enumerate(WORDS):
        wa = [w[2] for j, w in enumerate(WORDS) if j != i] + ['salat', 'ilmu', 'sedekah']
        p.mc(3, f'Kata "{l}" dalam hadis kebersihan berarti ....', t, wa, f'{a} ({l}) berarti {t}.', 'easy', 'memahami', 'Menyebutkan arti kata')
        p.mc(3, f'Kata Arab yang berarti "{t}" dalam hadis kebersihan adalah ....', a, [w[0] for j, w in enumerate(WORDS) if j != i] + ['الصَّلَاةُ', 'الْعِلْمُ'], f'{t} = {a} ({l}).', 'medium', 'mengenali', 'Menyebutkan arti kata')
        p.fill(3, f'Arti kata {a} adalah ....', t, f'{a} ({l}) berarti {t}.', 'medium', 'mengingat', 'Menyebutkan arti kata')
        p.tf(3, f'Kata "{l}" berarti {t}.', True, f'Benar, {l} berarti {t}.', 'easy', 'mengingat', 'Menyebutkan arti kata')
        p.tf(3, f'Kata "{l}" berarti {wa[0]}.', False, f'Salah. {l} berarti {t}.', 'medium', 'memahami', 'Menyebutkan arti kata')
    p.match(3, 'Jodohkan kata dalam hadis kebersihan dengan artinya!', [(w[1], w[2]) for w in WORDS], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Menyebutkan arti kata')
    p.match(3, 'Jodohkan kata Arab dalam hadis kebersihan dengan artinya!', [(w[0], w[2]) for w in WORDS], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Menyebutkan arti kata')
    p.order(3, 'Urutkan arti hadis kebersihan berikut dengan benar!', ['Kebersihan', 'itu sebagian', 'dari iman'], f'Arti: {ARTI}.', 'medium', 'mengurutkan', 'Menyebutkan arti hadis')
    p.mc(3, 'Kata "syathru" dalam hadis kebersihan dapat diartikan ....', 'sebagian atau separuh', ['seluruh', 'tidak ada', 'sedikit saja'], 'Syathru berarti sebagian/separuh.', 'medium', 'memahami', 'Menyebutkan arti kata')
    p.mc(3, 'Iman artinya ....', 'percaya atau yakin kepada Allah', ['takut kepada hewan', 'senang bermain', 'suka makan'], 'Iman adalah percaya kepada Allah.', 'easy', 'memahami', 'Menyebutkan arti kata')
    p.mc(3, 'Kata "thuhur" dalam bahasa Indonesia berarti ....', 'kebersihan atau kesucian', ['kekotoran', 'kemalasan', 'kemarahan'], 'Thuhur berarti bersih/suci.', 'medium', 'memahami', 'Menyebutkan arti kata')
    p.perf(3, 'Sebutkan arti hadis tentang kebersihan di depan guru!', 'Dinilai guru: ketepatan arti dan kejelasan penyampaian (skala 1-4).', 'Murid menyebutkan arti hadis.', 'medium', 'memahami', 'Menyebutkan arti hadis')
    p.perf(3, 'Sebutkan arti tiap kata dalam hadis kebersihan satu per satu!', 'Dinilai guru: ketepatan arti tiap kata (skala 1-4).', 'Murid menyebutkan arti kata.', 'medium', 'memahami', 'Menyebutkan arti kata')

    # ================= TP4: perilaku hidup bersih =================
    for (kat, act, benefit) in goods:
        p.gk = f'b{act}'
        subj = 'kebersihan diri' if kat == 'diri' else 'kebersihan lingkungan'
        bads_k = [b[1] for b in bads if b[0] == kat]
        p.mc(4, f'Agar {benefit}, perilaku {subj} yang sesuai dengan hadis kebersihan adalah ....', act, rng.sample(bads_k, 3), f'{act.capitalize()} menjaga {subj} sehingga {benefit}.', 'easy', 'menerapkan', 'Menerapkan perilaku hidup bersih')
        p.tf(4, f'{act.capitalize()} termasuk perilaku hidup bersih.', True, f'Benar, {act} menjaga {subj} sehingga {benefit}.', 'easy', 'menerapkan', 'Menerapkan perilaku hidup bersih')
        p.fill(4, f'Manfaat {act} adalah ....', benefit, f'{act.capitalize()} membuat {benefit}.', 'medium', 'memahami', 'Menerapkan perilaku hidup bersih')
        p.mc(4, f'Salah satu manfaat {act} adalah ....', benefit, [g[2] for g in goods if g[2] != benefit and g[1] != act][:6], f'{act.capitalize()} membuat {benefit}.', 'medium', 'memahami', 'Menerapkan perilaku hidup bersih')
    for (kat, b) in bads:
        p.gk = f'b{b}'
        goods_k = [g[1] for g in goods if g[0] == kat]
        p.tf(4, f'{b.capitalize()} termasuk perilaku hidup bersih.', False, f'Salah. {b.capitalize()} bukan perilaku hidup bersih.', 'easy', 'menerapkan', 'Menerapkan perilaku hidup bersih')
        p.mc(4, f'Perilaku yang tidak sesuai dengan hadis kebersihan adalah ....', b, rng.sample(goods_k, 3), f'{b.capitalize()} bertentangan dengan hidup bersih.', 'easy', 'menerapkan', 'Menerapkan perilaku hidup bersih') if False else None
    for k in range(len(bads)):
        p.gk = f'bm{k}'
        kat, b = bads[k]
        goods_k = [g[1] for g in goods if g[0] == kat]
        p.mc(4, f'Perilaku yang {AKIBAT[b]} dan tidak sesuai dengan hadis kebersihan adalah ....', b, rng.sample(goods_k, 3), f'{b.capitalize()} bertentangan dengan ajaran hidup bersih.', 'medium', 'menganalisis', 'Menerapkan perilaku hidup bersih')
    p.gk = None
    # ordering langkah
    p.order(4, 'Urutkan langkah mencuci tangan dengan benar!', ['Basahi tangan dengan air mengalir', 'Gosok tangan dengan sabun', 'Bilas tangan dengan air bersih', 'Keringkan tangan dengan lap bersih'], 'Basahi, sabun, bilas, keringkan.', 'medium', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    p.order(4, 'Urutkan langkah menyikat gigi dengan benar!', ['Siapkan sikat dan pasta gigi', 'Sikat gigi dari atas ke bawah', 'Berkumur dengan air bersih', 'Cuci dan simpan sikat gigi'], 'Persiapan, menyikat, berkumur, merapikan.', 'medium', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    p.order(4, 'Urutkan kegiatan piket kelas berikut!', ['Merapikan meja dan kursi', 'Menyapu lantai', 'Membuang sampah ke tempat sampah', 'Mengepel lantai'], 'Rapikan, sapu, buang sampah, pel.', 'medium', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    p.order(4, 'Urutkan kegiatan menjaga kebersihan sebelum tidur berikut!', ['Merapikan mainan', 'Mencuci kaki', 'Menyikat gigi', 'Berdoa sebelum tidur'], 'Rapikan, cuci kaki, sikat gigi, berdoa.', 'easy', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    p.order(4, 'Urutkan kegiatan sebelum makan berikut!', ['Mencuci tangan dengan sabun', 'Membaca bismillah', 'Makan dengan tangan kanan', 'Membaca alhamdulillah'], 'Cuci tangan, bismillah, makan, alhamdulillah.', 'easy', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    p.order(4, 'Urutkan cara membuang sampah dengan benar!', ['Mengumpulkan sampah', 'Memilah sampah organik dan anorganik', 'Memasukkan sampah ke tempat yang sesuai', 'Mencuci tangan'], 'Kumpulkan, pilah, masukkan, cuci tangan.', 'medium', 'mengurutkan', 'Menerapkan perilaku hidup bersih')
    # pengelompokan
    for gi in range(3):
        gd = rng.sample([g[1] for g in goods if g[0] == 'diri'], 3) + rng.sample([g[1] for g in goods if g[0] == 'lingkungan'], 3)
        d = {'kebersihan diri': [x for x in gd if x in [g[1] for g in goods if g[0] == 'diri']], 'kebersihan lingkungan': [x for x in gd if x in [g[1] for g in goods if g[0] == 'lingkungan']]}
        items = gd[:]; rng.shuffle(items)
        p.group(4, 'Kelompokkan kegiatan berikut ke dalam kebersihan diri atau kebersihan lingkungan: ' + '; '.join(f"'{x}'" for x in items) + '.', d, 'Kegiatan pada badan termasuk kebersihan diri; pada tempat termasuk kebersihan lingkungan.', 'medium', 'mengelompokkan', 'Menerapkan perilaku hidup bersih')
    for gi in range(3):
        ya = rng.sample(allgood, 3); tidak = rng.sample(allbad, 3)
        items = ya + tidak; rng.shuffle(items)
        p.group(4, 'Kelompokkan perilaku berikut menjadi "sesuai hadis kebersihan" atau "tidak sesuai": ' + '; '.join(f"'{x}'" for x in items) + '.', {'sesuai hadis kebersihan': ya, 'tidak sesuai': tidak}, 'Perilaku bersih sesuai hadis; perilaku kotor tidak sesuai.', 'medium', 'mengelompokkan', 'Menerapkan perilaku hidup bersih')
    # skenario konteks
    surah_scen.SCEN['HK'] = SCEN_HK
    surah_scen.apply(p, 'HK')
    for q, r in [
        ('Praktikkan cara mencuci tangan dengan benar menggunakan sabun dan air mengalir di depan guru!', 'Dinilai guru: urutan langkah, kebersihan, dan hemat air (skala 1-4).'),
        ('Praktikkan cara menyikat gigi dengan benar di depan teman dan guru!', 'Dinilai guru: ketepatan gerakan menyikat dan berkumur (skala 1-4).'),
        ('Ikut piket kelas hari ini: menyapu dan membuang sampah pada tempatnya!', 'Dinilai guru: kerja sama, kebersihan hasil, dan kedisiplinan (skala 1-4).'),
        ('Buatlah poster sederhana tentang hidup bersih yang bertuliskan hadis "Kebersihan sebagian dari iman"!', 'Dinilai guru: kesesuaian pesan, kerapian, dan kreativitas (skala 1-4).'),
        ('Ceritakan tiga kegiatan menjaga kebersihan yang kamu lakukan di rumah setiap hari!', 'Dinilai guru: ketepatan contoh dan kejujuran bercerita (skala 1-4).'),
        ('Ajak teman-temanmu membersihkan halaman sekolah bersama-sama dan laporkan hasilnya!', 'Dinilai guru: kerja sama, ketuntasan, dan sikap saling menghargai (skala 1-4).'),
        ('Peragakan cara menutup mulut saat bersin dan batuk yang benar!', 'Dinilai guru: ketepatan peragaan dan kepedulian kepada sesama (skala 1-4).'),
        ('Rapikan dan bersihkan tempat duduk serta lacimu sebelum pulang sekolah!', 'Dinilai guru: kerapian dan tanggung jawab (skala 1-4).'),
    ]:
        p.perf(4, q, r, 'Murid mempraktikkan perilaku hidup bersih.', 'medium', 'menerapkan', 'Menerapkan perilaku hidup bersih')
    return p


SCEN_HK = [
 (4, "Rafa baru pulang bermain di halaman dan akan makan siang. Sesuai hadis kebersihan, Rafa sebaiknya ....", "Sebelum makan siang, Rafa", "mencuci tangan dengan sabun", ["langsung makan dengan tangan kotor", "mengelap tangan ke baju", "meminta suapan tanpa mencuci tangan"], "Mencuci tangan menghilangkan kuman sebelum makan.", 'easy', None),
 (4, "Salwa menemukan bungkus jajanan di dekat kursi kelas. Ia sebaiknya ....", "Saat menemukan bungkus jajanan di kelas, Salwa", "memungutnya dan membuangnya ke tempat sampah", ["membiarkannya di lantai", "menendangnya ke kolong meja", "menyuruh teman membuangnya tanpa membantu"], "Membuang sampah pada tempatnya menjaga kelas bersih.", 'easy', None),
 (4, "Kuku Dimas sudah panjang dan hitam. Sesuai hadis kebersihan, Dimas sebaiknya ....", "Karena kukunya panjang dan hitam, Dimas", "meminta bantuan orang tua untuk memotongnya", ["membiarkannya tumbuh lebih panjang", "menggigit kukunya", "menyembunyikan tangannya"], "Memotong kuku mencegah kuman bersarang.", 'medium', None),
 (4, "Hari ini giliran Nadia piket kelas. Nadia sebaiknya ....", "Saat giliran piket, Nadia", "menyapu kelas dan merapikan meja dengan senang hati", ["pura-pura sakit agar tidak piket", "menyuruh teman melakukannya sendirian", "pulang lebih awal"], "Piket adalah wujud cinta lingkungan.", 'easy', None),
 (4, "Bayu bersin saat berada di dekat teman-temannya. Tindakan yang tepat adalah ....", "Ketika bersin di dekat teman, Bayu", "menutup hidung dan mulut dengan siku atau tisu", ["bersin langsung ke arah teman", "bersin sambil tertawa", "menepuk punggung teman"], "Menutup mulut mencegah penularan kuman.", 'medium', None),
 (4, "Ibu meminta Tiara menyikat gigi sebelum tidur. Sikap Tiara yang baik adalah ....", "Saat diminta ibu menyikat gigi sebelum tidur, Tiara", "menyikat gigi dengan rapi lalu berdoa", ["pura-pura sudah menyikat gigi", "langsung tidur karena mengantuk", "menunda sampai besok pagi"], "Gigi bersih menjaga kesehatan dan kenyamanan.", 'easy', None),
 (4, "Fahri melihat sampah plastik terapung di selokan depan rumahnya. Sebaiknya ia ....", "Melihat sampah plastik di selokan, Fahri", "mengambilnya dan membuangnya ke tempat sampah dengan bantuan orang dewasa", ["menambah sampah ke dalam selokan", "membiarkan saja karena bukan sampahnya", "melemparkannya ke halaman tetangga"], "Menjaga selokan bersih mencegah banjir dan penyakit.", 'medium', None),
 (4, "Hasna selesai menggunakan toilet sekolah. Hal yang harus dilakukan adalah ....", "Setelah memakai toilet sekolah, Hasna", "menyiram toilet lalu mencuci tangan dengan sabun", ["langsung keluar tanpa menyiram", "mencuci tangan tanpa sabun lalu berlari", "meninggalkan keran tetap menyala"], "Toilet harus tetap bersih dan tangan dicuci agar kuman tidak menyebar.", 'medium', None),
 (4, "Zaki melihat temannya membuang sampah sembarangan di halaman sekolah. Zaki sebaiknya ....", "Saat melihat temannya membuang sampah sembarangan, Zaki", "mengingatkan dengan sopan dan membantu membuangnya ke tempat sampah", ["ikut membuang sampah sembarangan", "mengejek temannya", "pura-pura tidak melihat"], "Saling mengingatkan dalam kebaikan menunjukkan cinta sesama dan lingkungan.", 'medium', None),
 (4, "Sebelum salat di musala, Lutfi melihat lantai musala berdebu. Sikap Lutfi yang baik adalah ....", "Saat musala berdebu, Lutfi", "membantu menyapu dan merapikan sajadah", ["membiarkannya dan langsung pulang", "mengotori lantai lebih banyak", "mengeluh sambil duduk"], "Menjaga kebersihan tempat ibadah termasuk cinta Allah.", 'medium', None),
 (4, "Putri baru selesai bermain lumpur. Sebelum masuk rumah, Putri sebaiknya ....", "Setelah bermain lumpur, Putri", "mencuci kaki dan tangan lalu mengganti pakaian yang kotor", ["langsung masuk rumah dan duduk di kasur", "mengelap kaki ke karpet", "menyembunyikan baju kotor"], "Menjaga kebersihan diri dan rumah.", 'easy', None),
 (4, "Adik makan sambil berserakan di ruang tamu. Kakak yang sesuai hadis kebersihan akan ....", "Melihat adik makan berserakan, kakak", "membantu membersihkan dan mengingatkan adik dengan lembut", ["memarahi adik dengan kasar", "membiarkan sampai berhari-hari", "ikut mengotori ruangan"], "Mengingatkan dengan lembut dan membantu membersihkan.", 'medium', None),
 (1, "Adit bertanya, \"Mengapa kita harus menjaga kebersihan?\" Jawaban yang paling sesuai dengan hadis adalah ....", "Menurut hadis, kita harus menjaga kebersihan karena kebersihan", "sebagian dari iman", ["hanya aturan sekolah", "membuat kita terlihat sibuk", "tidak ada gunanya"], "Hadis: Ath-thuhuru syathrul iman.", 'easy', None),
 (1, "Ibu berkata, \"Kebersihan juga bentuk cinta kita kepada ....\" Jawaban yang tepat adalah ....", "Kebersihan adalah wujud cinta kepada", "Allah, diri sendiri, sesama, dan lingkungan", ["mainan saja", "teman saja", "uang saja"], "Menjaga kebersihan adalah wujud berbagai cinta (Panca Cinta).", 'medium', None),
 (1, "Guru menjelaskan bahwa orang yang menjaga kebersihan dicintai Allah. Alasan yang tepat adalah karena ia ....", "Orang yang menjaga kebersihan dicintai Allah karena ia", "menjalankan ajaran Islam tentang hidup bersih", ["tidak pernah belajar", "suka berbuat sesukanya", "mengabaikan nasihat guru"], "Allah mencintai orang yang bersuci dan menjaga kebersihan.", 'medium', None),
 (4, "Perhatikan gambar! Seorang anak membasahi tangannya di bawah keran dan memakai sabun sebelum makan. Perilaku ini sesuai dengan hadis ....", "Gambar anak mencuci tangan dengan sabun sebelum makan sesuai hadis", "kebersihan sebagian dari iman", ["semua orang boleh berbuat sesukanya", "salat lima waktu", "berbakti kepada orang tua"], "Mencuci tangan adalah contoh menjaga kebersihan.", 'easy',
  "Anak perempuan di depan wastafel sekolah menggosok tangan yang penuh busa sabun, di dekatnya ada kotak sabun cair."),
 (4, "Perhatikan gambar! Beberapa anak memakai sarung tangan sedang memungut sampah di taman sekolah dan memasukkannya ke tempat sampah. Sikap anak-anak itu menunjukkan ....", "Gambar anak memungut sampah di taman sekolah menunjukkan", "cinta lingkungan", ["cinta mainan", "malas belajar", "suka bermain air"], "Menjaga lingkungan bersih adalah cinta lingkungan.", 'easy',
  "Empat anak berseragam MI memakai sarung tangan memungut sampah plastik di taman sekolah dan memasukkannya ke tong sampah besar."),
 (4, "Perhatikan gambar! Dua tempat sampah berwarna hijau dan kuning di halaman sekolah. Sampah daun sebaiknya dimasukkan ke tempat sampah ....", "Pada gambar dua tempat sampah hijau (organik) dan kuning (anorganik), sampah daun dimasukkan ke tempat sampah", "hijau (organik)", ["kuning (anorganik)", "mana saja tanpa memilah", "dibuang ke selokan"], "Daun termasuk sampah organik.", 'medium',
  "Dua tong sampah berdampingan: hijau berlabel ORGANIK dan kuning berlabel ANORGANIK; anak memegang daun kering."),
 (4, "Perhatikan gambar! Seorang anak berdiri di depan cermin kamar mandi sambil menyikat gigi. Kegiatan ini sebaiknya dilakukan ....", "Gambar anak menyikat gigi di depan cermin, sebaiknya kegiatan ini dilakukan", "pagi hari dan sebelum tidur", ["hanya setahun sekali", "hanya saat sakit gigi", "saat sedang makan"], "Menyikat gigi dua kali sehari menjaga kesehatan gigi.", 'medium',
  "Anak laki-laki berpiyama menyikat gigi dengan busa pasta di mulutnya, cermin kamar mandi di depannya."),
 (4, "Perhatikan gambar! Sebuah kamar tidur yang rapi dengan tempat tidur tertata dan buku tersusun di rak. Sikap pemilik kamar adalah ....", "Gambar kamar yang rapi menunjukkan pemiliknya suka", "merapikan dan menjaga kebersihan kamar", ["membiarkan barang berserakan", "tidak peduli kebersihan", "malas bergerak"], "Kamar rapi menunjukkan menjaga kebersihan.", 'easy',
  "Kamar anak dengan tempat tidur tertata, selimut terlipat, dan buku tersusun rapi di rak."),
 (4, "Perhatikan gambar! Seorang anak sedang mencuci piring bekas makannya di dapur dengan bantuan ibu. Sikap anak itu menunjukkan ....", "Gambar anak mencuci piring bekas makan menunjukkan sikap", "mandiri dan peduli kebersihan", ["malas membantu", "suka membuang makanan", "tidak peduli rumah"], "Mencuci piring melatih kemandirian dan kebersihan.", 'easy',
  "Anak perempuan berdiri di atas bangku kecil mencuci piring di bak cuci; ibu mengawasi di sampingnya."),
 (4, "Perhatikan gambar! Anak-anak berbaris rapi mengantre di depan keran air untuk mencuci tangan. Hal baik yang ditunjukkan adalah ....", "Gambar anak-anak mengantre mencuci tangan menunjukkan sikap", "tertib dan peduli kebersihan", ["berebut dan bertengkar", "bermain air berlebihan", "tidak peduli kuman"], "Mengantre dan mencuci tangan menunjukkan kebersihan dan ketertiban.", 'easy',
  "Enam anak MI berbaris di depan deretan keran air di halaman sekolah, masing-masing menunggu giliran mencuci tangan."),
 (4, "Perhatikan gambar! Seorang anak membuang bungkus permen ke tanah di pinggir jalan padahal tempat sampah ada di dekatnya. Sikap yang tepat bagi temannya adalah ....", "Pada gambar anak membuang bungkus permen sembarangan, sikap temannya sebaiknya", "mengingatkan dengan sopan agar membuang di tempat sampah", ["ikut membuang sampah sembarangan", "menertawakan temannya", "memarahi dengan kasar"], "Mengingatkan dengan sopan dalam kebaikan.", 'medium',
  "Dua anak di pinggir jalan; satu anak melempar bungkus permen ke tanah, tempat sampah biru tampak tidak jauh darinya, temannya menunjuk ke tempat sampah."),
]
