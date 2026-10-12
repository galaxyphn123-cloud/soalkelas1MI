# -*- coding: utf-8 -*-
"""Data tambahan Bahasa Arab Kelas 1 MI untuk tiga bab yang ada di KKTP tetapi belum ada di bank:
Bab III Hobiku (هواياتي), Bab V Nama-nama Buah (أسماء الفواكه), Bab VI Warna-warna (الألوان).
Kalimat TP dikutip dari kolom 'Alur Tujuan Pembelajaran' pada berkas KKTP Bahasa Arab Kelas I.
Format kata: (arab, latin, arti, gender 'm'/'f'/None, deskripsi gambar atau None)."""

# ============================================================================ HOBIKU
HB_WORDS = [
 ('هِوَايَةٌ', 'hiwayatun', 'hobi', None, 'Seorang anak tersenyum sambil menunjuk kartu bertuliskan kata "hobi".'),
 ('قِرَاءَةٌ', 'qira-atun', 'membaca', None, 'Seorang anak membaca buku cerita di perpustakaan.'),
 ('كِتَابَةٌ', 'kitabatun', 'menulis', None, 'Seorang anak menulis di buku tulis dengan pensil.'),
 ('رَسْمٌ', 'rasmun', 'menggambar', None, 'Seorang anak menggambar pemandangan di atas kertas.'),
 ('سِبَاحَةٌ', 'sibahatun', 'berenang', None, 'Seorang anak berenang di kolam renang.'),
 ('جَرْيٌ', 'jaryun', 'berlari', None, 'Seorang anak berlari di lapangan.'),
 ('طَبْخٌ', 'thabkhun', 'memasak', None, 'Seorang anak membantu ibu memasak di dapur.'),
 ('زِرَاعَةٌ', 'zira-atun', 'berkebun', None, 'Seorang anak menyiram tanaman di kebun.'),
 ('كُرَةُ الْقَدَمِ', 'kuratul qadami', 'sepak bola', None, 'Anak-anak bermain sepak bola di lapangan.'),
 ('رُكُوبُ الدَّرَّاجَةِ', 'rukubud darrajati', 'bersepeda', None, 'Seorang anak bersepeda di taman.'),
 ('أُحِبُّ', 'uhibbu', 'saya suka', None, None),
 ('هِوَايَتِي', 'hiwayati', 'hobiku', None, None),
]
HB_SENT = [
 ('مَا هِوَايَتُكَ؟', 'Ma hiwayatuka?', 'Apa hobimu? (kepada laki-laki)'),
 ('مَا هِوَايَتُكِ؟', 'Ma hiwayatuki?', 'Apa hobimu? (kepada perempuan)'),
 ('هِوَايَتِي الْقِرَاءَةُ', 'Hiwayati al-qira-atu', 'Hobiku membaca'),
 ('هِوَايَتِي السِّبَاحَةُ', 'Hiwayati as-sibahatu', 'Hobiku berenang'),
 ('هِوَايَتِي الرَّسْمُ', 'Hiwayati ar-rasmu', 'Hobiku menggambar'),
 ('هِوَايَتِي كُرَةُ الْقَدَمِ', 'Hiwayati kuratul qadami', 'Hobiku sepak bola'),
 ('أُحِبُّ الْقِرَاءَةَ', 'Uhibbul qira-ata', 'Saya suka membaca'),
 ('أُحِبُّ الطَّبْخَ', 'Uhibbuth thabkha', 'Saya suka memasak'),
 ('أُحِبُّ الْجَرْيَ', 'Uhibbul jarya', 'Saya suka berlari'),
 ('هِوَايَةُ أَخِي الرَّسْمُ', 'Hiwayatu akhi ar-rasmu', 'Hobi saudara laki-lakiku menggambar'),
 ('هِوَايَةُ أُخْتِي الطَّبْخُ', 'Hiwayatu ukhti ath-thabkhu', 'Hobi saudara perempuanku memasak'),
]
HB_DIALOG = [
 ('مَا هِوَايَتُكَ؟', 'هِوَايَتِي الْقِرَاءَةُ', 'menanyakan hobi teman laki-laki yang suka membaca'),
 ('مَا هِوَايَتُكِ؟', 'هِوَايَتِي الرَّسْمُ', 'menanyakan hobi teman perempuan yang suka menggambar'),
 ('أَيُّ هِوَايَةٍ تُحِبُّ؟', 'أُحِبُّ السِّبَاحَةَ', 'menanyakan hobi yang disukai teman yang suka berenang'),
 ('السَّلَامُ عَلَيْكُمْ', 'وَعَلَيْكُمُ السَّلَامُ', 'memberi dan menjawab salam sebelum bertanya hobi'),
]
HB_TEXTS = [
 ('اِسْمِي أَحْمَدُ. هِوَايَتِي كُرَةُ الْقَدَمِ. أُحِبُّ الْجَرْيَ.',
  [('Siapa nama anak dalam teks?', 'Ahmad', ['Fatimah', 'Aisyah', 'Ali']),
   ('Hobi anak dalam teks adalah ....', 'sepak bola', ['membaca', 'berenang', 'memasak']),
   ('Kalimat "أُحِبُّ الْجَرْيَ" berarti ....', 'saya suka berlari', ['saya suka membaca', 'saya suka memasak', 'saya suka berenang']),
   ('Kata "هِوَايَتِي" dalam teks berarti ....', 'hobiku', ['namaku', 'sekolahku', 'keluargaku'])]),
 ('اِسْمِي فَاطِمَةُ. هِوَايَتِي الرَّسْمُ. أُحِبُّ الْقِرَاءَةَ.',
  [('Anak dalam teks adalah seorang ....', 'anak perempuan', ['anak laki-laki', 'guru laki-laki', 'kakek']),
   ('Hobi anak dalam teks adalah ....', 'menggambar', ['berenang', 'berlari', 'memasak']),
   ('Selain hobinya, anak itu juga suka ....', 'membaca', ['memasak', 'berenang', 'bersepeda']),
   ('Kata "الرَّسْمُ" dalam teks berarti ....', 'menggambar', ['menulis', 'membaca', 'berlari'])]),
 ('مَا هِوَايَتُكَ؟ هِوَايَتِي السِّبَاحَةُ. شُكْرًا.',
  [('Pertanyaan dalam teks menanyakan ....', 'hobi', ['nama', 'kabar', 'alamat']),
   ('Pertanyaan dalam teks ditujukan kepada ....', 'laki-laki', ['perempuan', 'dua orang perempuan', 'seekor kucing']),
   ('Hobi yang menjawab adalah ....', 'berenang', ['membaca', 'menggambar', 'berlari']),
   ('Kata "شُكْرًا" dalam teks berarti ....', 'terima kasih', ['sama-sama', 'selamat pagi', 'selamat tinggal'])]),
]

# ============================================================================ NAMA-NAMA BUAH
BH_WORDS = [
 ('فَاكِهَةٌ', 'fakihatun', 'buah', 'f', 'Sebuah keranjang berisi aneka buah segar.'),
 ('تُفَّاحَةٌ', 'tuffahatun', 'apel', 'f', 'Sebuah apel merah di atas meja.'),
 ('مَوْزَةٌ', 'mauzatun', 'pisang', 'f', 'Sebuah pisang yang sudah matang.'),
 ('بُرْتُقَالَةٌ', 'burtuqalatun', 'jeruk', 'f', 'Sebuah jeruk berwarna oranye.'),
 ('عِنَبٌ', "'inabun", 'anggur', 'm', 'Setandan anggur di dalam mangkuk.'),
 ('بِطِّيخَةٌ', 'bitthikhatun', 'semangka', 'f', 'Sebuah semangka utuh dan satu irisan semangka.'),
 ('فَرَاوِلَةٌ', 'farawilatun', 'stroberi', 'f', 'Sebuah stroberi segar.'),
 ('لَيْمُونَةٌ', 'laimunatun', 'lemon', 'f', 'Sebuah lemon di atas piring.'),
 ('رُمَّانَةٌ', 'rummanatun', 'delima', 'f', 'Sebuah buah delima yang dibelah.'),
 ('تِينَةٌ', 'tinatun', 'tin (ara)', 'f', 'Sebuah buah tin di atas daun.'),
 ('تَمْرٌ', 'tamrun', 'kurma', 'm', 'Beberapa butir kurma di atas piring.'),
 ('خَوْخٌ', 'khaukhun', 'persik', 'm', 'Sebuah persik di atas meja.'),
]
BH_SENT = [
 ('مَا هٰذَا؟', 'Ma hadza?', 'Apa ini? (benda berjenis laki-laki)'),
 ('مَا هٰذِهِ؟', 'Ma hadzihi?', 'Apa ini? (benda berjenis perempuan)'),
 ('هٰذِهِ تُفَّاحَةٌ', 'Hadzihi tuffahatun', 'Ini sebuah apel'),
 ('هٰذِهِ مَوْزَةٌ', 'Hadzihi mauzatun', 'Ini sebuah pisang'),
 ('هٰذِهِ بُرْتُقَالَةٌ', 'Hadzihi burtuqalatun', 'Ini sebuah jeruk'),
 ('هٰذِهِ بِطِّيخَةٌ', 'Hadzihi bitthikhatun', 'Ini sebuah semangka'),
 ('هٰذِهِ فَاكِهَةٌ', 'Hadzihi fakihatun', 'Ini buah'),
 ('هٰذَا عِنَبٌ', "Hadza 'inabun", 'Ini anggur'),
 ('هٰذَا تَمْرٌ', 'Hadza tamrun', 'Ini kurma'),
 ('هٰذَا خَوْخٌ', 'Hadza khaukhun', 'Ini persik'),
 ('أُحِبُّ الْعِنَبَ', "Uhibbul 'inaba", 'Saya suka anggur'),
]
BH_DIALOG = [
 ('مَا هٰذَا؟', 'هٰذَا عِنَبٌ', 'menanyakan benda berjenis laki-laki yang berupa anggur'),
 ('مَا هٰذِهِ؟', 'هٰذِهِ تُفَّاحَةٌ', 'menanyakan benda berjenis perempuan yang berupa apel'),
 ('مَا هٰذَا؟', 'هٰذَا تَمْرٌ', 'menanyakan benda berjenis laki-laki yang berupa kurma'),
 ('مَا هٰذِهِ؟', 'هٰذِهِ بُرْتُقَالَةٌ', 'menanyakan benda berjenis perempuan yang berupa jeruk'),
]
BH_TEXTS = [
 ('هٰذِهِ فَاكِهَةٌ. هٰذِهِ تُفَّاحَةٌ. هٰذِهِ مَوْزَةٌ. هٰذَا عِنَبٌ.',
  [('Teks ini bercerita tentang ....', 'buah', ['hewan', 'pakaian', 'alat tulis']),
   ('Kata "مَوْزَةٌ" dalam teks berarti ....', 'pisang', ['apel', 'anggur', 'jeruk']),
   ('Kata tunjuk "هٰذَا" dalam teks dipakai untuk ....', 'anggur', ['apel', 'pisang', 'buah']),
   ('Jumlah jenis buah yang disebut dalam teks (tidak termasuk kata "buah") adalah ....', '3', ['1', '2', '4'])]),
 ('مَا هٰذَا؟ هٰذَا تَمْرٌ. مَا هٰذِهِ؟ هٰذِهِ رُمَّانَةٌ.',
  [('Buah pertama yang ditanyakan adalah ....', 'kurma', ['delima', 'apel', 'anggur']),
   ('Buah kedua yang ditanyakan adalah ....', 'delima', ['kurma', 'jeruk', 'pisang']),
   ('Kata "مَا" pada awal pertanyaan berarti ....', 'apa', ['siapa', 'di mana', 'kapan']),
   ('Kata "هٰذِهِ" dalam teks dipakai untuk menunjuk ....', 'delima', ['kurma', 'anggur', 'persik'])]),
 ('هٰذِهِ بِطِّيخَةٌ. هٰذِهِ فَرَاوِلَةٌ. هٰذَا خَوْخٌ. اَلْحَمْدُ لِلّٰهِ.',
  [('Kata "بِطِّيخَةٌ" dalam teks berarti ....', 'semangka', ['stroberi', 'persik', 'lemon']),
   ('Kata "فَرَاوِلَةٌ" dalam teks berarti ....', 'stroberi', ['semangka', 'persik', 'delima']),
   ('Buah yang ditunjuk dengan "هٰذَا" adalah ....', 'persik', ['semangka', 'stroberi', 'apel']),
   ('Ucapan "اَلْحَمْدُ لِلّٰهِ" pada akhir teks menunjukkan sikap ....', 'bersyukur atas nikmat Allah', ['marah kepada teman', 'malas belajar di kelas', 'sombong dengan buah'])]),
]

# ============================================================================ WARNA-WARNA
WR_WORDS = [
 ('لَوْنٌ', 'launun', 'warna', 'm', 'Sebuah kartu bertuliskan kata "warna" di samping kuas yang bersih.'),
 ('أَحْمَرُ', 'ahmaru', 'merah', None, 'Sebuah kartu berwarna merah polos.'),
 ('أَصْفَرُ', 'ashfaru', 'kuning', None, 'Sebuah kartu berwarna kuning polos.'),
 ('أَخْضَرُ', 'akhdharu', 'hijau', None, 'Sebuah kartu berwarna hijau polos.'),
 ('أَزْرَقُ', 'azraqu', 'biru', None, 'Sebuah kartu berwarna biru polos.'),
 ('أَبْيَضُ', 'abyadhu', 'putih', None, 'Sebuah kartu berwarna putih polos.'),
 ('أَسْوَدُ', 'aswadu', 'hitam', None, 'Sebuah kartu berwarna hitam polos.'),
 ('قَلَمٌ', 'qalamun', 'pena', 'm', 'Sebuah pena di atas meja.'),
 ('كِتَابٌ', 'kitabun', 'buku', 'm', 'Sebuah buku di atas meja.'),
 ('بَابٌ', 'babun', 'pintu', 'm', 'Sebuah pintu kayu berwarna cokelat.'),
 ('قَمِيصٌ', 'qamishun', 'kemeja', 'm', 'Sebuah kemeja tergantung pada gantungan baju.'),
 ('سَيَّارَةٌ', 'sayyaratun', 'mobil', 'f', 'Sebuah mobil di tepi jalan.'),
 ('شَجَرَةٌ', 'syajaratun', 'pohon', 'f', 'Sebuah pohon rindang di taman.'),
 ('سَمَاءٌ', "sama-un", 'langit', 'f', 'Langit siang hari dengan beberapa awan.'),
 ('سَبُّورَةٌ', 'sabburatun', 'papan tulis', 'f', 'Sebuah papan tulis di depan kelas.'),
]
WR_SENT = [
 ('مَا لَوْنُ الْقَلَمِ؟', 'Ma launul qalami?', 'Apa warna pena?'),
 ('لَوْنُ الْقَلَمِ أَحْمَرُ', 'Launul qalami ahmaru', 'Warna pena itu merah'),
 ('هٰذَا قَلَمٌ أَحْمَرُ', 'Hadza qalamun ahmaru', 'Ini pena merah'),
 ('هٰذَا كِتَابٌ أَزْرَقُ', 'Hadza kitabun azraqu', 'Ini buku biru'),
 ('هٰذَا بَابٌ أَخْضَرُ', 'Hadza babun akhdharu', 'Ini pintu hijau'),
 ('هٰذَا قَمِيصٌ أَبْيَضُ', 'Hadza qamishun abyadhu', 'Ini kemeja putih'),
 ('هٰذِهِ سَيَّارَةٌ حَمْرَاءُ', 'Hadzihi sayyaratun hamra-u', 'Ini mobil merah'),
 ('هٰذِهِ شَجَرَةٌ خَضْرَاءُ', 'Hadzihi syajaratun khadhra-u', 'Ini pohon hijau'),
 ('هٰذِهِ سَمَاءٌ زَرْقَاءُ', 'Hadzihi sama-un zarqa-u', 'Ini langit biru'),
 ('هٰذِهِ سَبُّورَةٌ سَوْدَاءُ', 'Hadzihi sabburatun sauda-u', 'Ini papan tulis hitam'),
 ('هٰذِهِ مَوْزَةٌ صَفْرَاءُ', 'Hadzihi mauzatun shafra-u', 'Ini pisang kuning'),
]
WR_DIALOG = [
 ('مَا لَوْنُ الْقَلَمِ؟', 'لَوْنُ الْقَلَمِ أَحْمَرُ', 'menanyakan warna pena yang berwarna merah'),
 ('مَا لَوْنُ الْبَابِ؟', 'لَوْنُ الْبَابِ أَخْضَرُ', 'menanyakan warna pintu yang berwarna hijau'),
 ('مَا لَوْنُ السَّمَاءِ؟', 'لَوْنُ السَّمَاءِ أَزْرَقُ', 'menanyakan warna langit siang hari yang berwarna biru'),
 ('مَا لَوْنُ الْكِتَابِ؟', 'لَوْنُ الْكِتَابِ أَبْيَضُ', 'menanyakan warna buku yang berwarna putih'),
]
WR_TEXTS = [
 ('هٰذَا قَلَمٌ أَحْمَرُ. هٰذَا كِتَابٌ أَزْرَقُ. هٰذَا بَابٌ أَخْضَرُ.',
  [('Warna pena dalam teks adalah ....', 'merah', ['biru', 'hijau', 'putih']),
   ('Warna buku dalam teks adalah ....', 'biru', ['merah', 'hijau', 'kuning']),
   ('Warna pintu dalam teks adalah ....', 'hijau', ['merah', 'biru', 'hitam']),
   ('Jumlah benda yang disebut dalam teks adalah ....', '3', ['2', '4', '5'])]),
 ('مَا لَوْنُ السَّمَاءِ؟ لَوْنُ السَّمَاءِ أَزْرَقُ. مَا لَوْنُ الْمَوْزَةِ؟ لَوْنُ الْمَوْزَةِ أَصْفَرُ.',
  [('Warna langit dalam teks adalah ....', 'biru', ['merah', 'kuning', 'hitam']),
   ('Warna pisang dalam teks adalah ....', 'kuning', ['biru', 'hijau', 'putih']),
   ('Kata "لَوْنُ" dalam teks berarti ....', 'warna', ['benda', 'nama', 'hobi']),
   ('Kata "مَا" pada awal pertanyaan berarti ....', 'apa', ['siapa', 'di mana', 'kapan'])]),
 ('هٰذِهِ سَيَّارَةٌ حَمْرَاءُ. هٰذِهِ شَجَرَةٌ خَضْرَاءُ. هٰذَا قَمِيصٌ أَبْيَضُ. هٰذِهِ سَبُّورَةٌ سَوْدَاءُ.',
  [('Mobil dalam teks berwarna ....', 'merah', ['hijau', 'putih', 'hitam']),
   ('Pohon dalam teks berwarna ....', 'hijau', ['merah', 'putih', 'hitam']),
   ('Kemeja dalam teks berwarna ....', 'putih', ['merah', 'hijau', 'hitam']),
   ('Papan tulis dalam teks berwarna ....', 'hitam', ['merah', 'hijau', 'putih'])]),
]

# ----------------------------------------------------------------------------- TP (dikutip dari KKTP Bahasa Arab Kelas I)
MATERI = [
 dict(code='HB', name='Hobiku (هواياتي)', words=HB_WORDS, sent=HB_SENT, dialog=HB_DIALOG, texts=HB_TEXTS, kktp_bab='Bab III',
      tps=['Murid mampu memahami unsur kebahasaan berupa bunyi, kata, dan makna dari teks yang disajikan dengan tema هوايتي.',
           'Murid mampu menyajikan hasil analisis bunyi dari teks dalam bentuk tulisan yang sesuai dengan kaidah penulisan huruf hijaiyah yang benar.',
           'Murid memiliki kepercayaan diri untuk berkomunikasi dengan orang yang ada di sekitarnya, serta mampu bertanggung jawab dalam komunikasi yang mereka lakukan.',
           'Murid mampu menyadari bahwa Bahasa Arab merupakan anugerah Allah dan menggunakannya untuk mengkaji khazanah keislaman.']),
 dict(code='BH', name='Nama-nama Buah (أسماء الفواكه)', words=BH_WORDS, sent=BH_SENT, dialog=BH_DIALOG, texts=BH_TEXTS, kktp_bab='Bab V',
      tps=['Murid mampu mengidentifikasi unsur kebahasaan dalam teks sederhana serta mengaplikasikan penggunaan هذه - هذا dan mendemonstrasikannya.',
           'Murid mampu menganalisis teks sederhana dan menuliskannya sesuai dengan kaidah penulisan huruf hijaiyah yang benar terkait huruf pisah dan sambung.',
           'Murid mampu mengaplikasikan pengetahuan dan kemampuan kebahasaan yang mereka miliki untuk menjalankan sikap santun dalam berkomunikasi dengan lingkungan sekitar, rumah dan sekolah serta disiplin dalam pergaulan dan keberadaannya.']),
 dict(code='WR', name='Warna-warna (الألوان)', words=WR_WORDS, sent=WR_SENT, dialog=WR_DIALOG, texts=WR_TEXTS, kktp_bab='Bab VI',
      tps=['Murid mampu mengungkapkan informasi yang mereka miliki terkait warna-warna dari benda konkret yang berada di sekeliling mereka dan mampu menganalisis bunyi yang diperdengarkan terkait tema tersebut.',
           'Murid mampu menyajikan hasil analisisnya dalam bentuk tulisan dengan memperhatikan kaidah penulisan huruf hijaiyah yang benar.',
           'Murid mampu mengaplikasikan pengetahuan dan kemampuan mereka dalam berkomunikasi dengan menggunakan Bahasa Arab serta menunjukkan perilaku jujur dalam berinteraksi antar sesama.']),
]

# ----------------------------------------------------------------------------- skenario sikap & penerapan
# (tp, soal_panjang, awalan_pernyataan, benar, [3 salah], penjelasan, kesulitan)
SCEN = {}
SCEN['HB'] = [
 (3, 'Bu Guru bertanya, "مَا هِوَايَتُكَ؟" Dengan percaya diri, kamu menjawab ....', 'Ketika ditanya hobinya oleh guru, murid yang percaya diri', 'menjawab "هِوَايَتِي ...." sambil tersenyum dan menatap guru', ['diam saja dan menutup wajah dengan buku', 'pergi keluar kelas', 'menyuruh teman lain menjawab'], 'Percaya diri berarti berani menjawab dengan sopan.', 'easy'),
 (3, 'Temanmu pemalu ketika ditanya hobinya. Sikap yang baik adalah ....', 'Ketika temannya pemalu saat ditanya hobi, Salma', 'mendengarkan dengan sabar dan tidak menertawakannya', ['menertawakannya di depan kelas', 'merebut giliran bicaranya', 'meninggalkannya sendirian di kelas'], 'Bertanggung jawab dalam berkomunikasi berarti menghargai teman bicara.', 'easy'),
 (3, 'Temanmu bertanya apa hobimu. Sikap jujur dalam menjawab adalah ....', 'Ketika ditanya hobinya, Rafi yang jujur', 'menyebut hobi yang sebenarnya', ['menyebut hobi palsu agar terlihat hebat', 'menyebut semua hobi yang ia dengar', 'berbohong supaya sama dengan temannya'], 'Jujur berarti menyampaikan hal yang sebenarnya.', 'easy'),
 (3, 'Kamu ingin menanyakan hobi teman perempuanmu dalam bahasa Arab. Kalimat yang tepat adalah ....', 'Menanyakan hobi teman perempuan, murid mengatakan', '"مَا هِوَايَتُكِ؟"', ['"مَا هِوَايَتُكَ؟"', '"مَا اسْمُكِ؟"', '"مَنْ هِيَ؟"'], 'مَا هِوَايَتُكِ؟ ditujukan kepada perempuan.', 'medium'),
 (3, 'Kamu ingin menanyakan hobi teman laki-lakimu dalam bahasa Arab. Kalimat yang tepat adalah ....', 'Menanyakan hobi teman laki-laki, murid mengatakan', '"مَا هِوَايَتُكَ؟"', ['"مَا هِوَايَتُكِ؟"', '"مَا اسْمُكَ؟"', '"مَنْ هُوَ؟"'], 'مَا هِوَايَتُكَ؟ ditujukan kepada laki-laki.', 'medium'),
 (3, 'Temanmu menjawab, "هِوَايَتِي السِّبَاحَةُ". Artinya temanmu suka ....', 'Jika temannya berkata "هِوَايَتِي السِّبَاحَةُ", artinya ia suka', 'berenang', ['membaca', 'memasak', 'berlari'], 'السِّبَاحَةُ berarti berenang.', 'easy'),
 (3, 'Kamu ingin mengatakan bahwa kamu suka membaca. Kalimat yang tepat adalah ....', 'Untuk mengatakan bahwa ia suka membaca, murid berkata', '"أُحِبُّ الْقِرَاءَةَ"', ['"أُحِبُّ الرَّسْمَ"', '"أُحِبُّ السِّبَاحَةَ"', '"أُحِبُّ الطَّبْخَ"'], 'أُحِبُّ الْقِرَاءَةَ berarti saya suka membaca.', 'medium'),
 (3, 'Temanmu memiliki hobi yang berbeda denganmu. Sikap yang baik adalah ....', 'Terhadap teman yang hobinya berbeda, Hana', 'menghargai hobi temannya', ['mengejek hobi temannya', 'memaksa temannya mengikuti hobinya', 'tidak mau berteman lagi'], 'Menghargai perbedaan adalah akhlak terpuji.', 'easy'),
 (4, 'Kamu dapat menyebut hobimu dalam bahasa Arab. Kemampuan ini patut ....', 'Kemampuan berbahasa Arab merupakan anugerah Allah yang patut', 'disyukuri dan dipakai untuk belajar kebaikan', ['disombongkan kepada teman', 'disembunyikan agar tidak dipakai', 'dilupakan begitu saja'], 'Bahasa Arab adalah anugerah Allah; kita bersyukur dan memanfaatkannya.', 'medium'),
 (4, 'Bahasa Arab adalah bahasa yang dipakai dalam Al-Qur\'an. Karena itu, sikap yang baik saat belajar bahasa Arab adalah ....', 'Karena bahasa Arab adalah bahasa Al-Qur\'an, murid belajar bahasa Arab dengan', 'sungguh-sungguh', ['malas-malasan', 'asal-asalan', 'mengejek teman yang salah ucap'], 'Bahasa Arab dipelajari dengan sungguh-sungguh sebagai bekal memahami ajaran Islam.', 'medium'),
]
SCEN['BH'] = [
 (3, 'Ibu memberimu sebuah apel. Kamu mengucapkan ....', 'Setelah diberi apel oleh ibu, murid mengucapkan', '"شُكْرًا"', ['"مَعَ السَّلَامَةِ"', '"مَرْحَبًا"', '"صَبَاحُ الْخَيْرِ"'], 'شُكْرًا berarti terima kasih.', 'easy'),
 (3, 'Sebelum makan buah, sikap yang baik adalah ....', 'Sebelum makan buah, murid yang disiplin', 'mencuci buah dan tangan lalu berdoa', ['langsung makan tanpa mencuci', 'melempar kulit buahnya', 'berebut dengan teman'], 'Mencuci buah dan tangan menjaga kebersihan.', 'easy'),
 (3, 'Setelah makan buah, ucapan syukur yang tepat adalah ....', 'Setelah makan buah, murid mengucapkan', '"اَلْحَمْدُ لِلّٰهِ"', ['"أَهْلًا وَسَهْلًا"', '"مَعَ السَّلَامَةِ"', '"عَفْوًا"'], 'اَلْحَمْدُ لِلّٰهِ berarti segala puji bagi Allah.', 'easy'),
 (3, 'Kamu selesai makan pisang. Kulit pisangnya sebaiknya dibuang ke ....', 'Setelah makan pisang, murid yang disiplin membuang kulitnya ke', 'tempat sampah', ['kolong meja', 'laci teman', 'halaman kelas'], 'Disiplin menjaga kebersihan lingkungan.', 'easy'),
 (3, 'Di depanmu ada benda berjenis perempuan. Kamu ingin bertanya namanya. Kalimat tanya yang tepat adalah ....', 'Untuk menanyakan benda berjenis perempuan, murid berkata', '"مَا هٰذِهِ؟"', ['"مَا هٰذَا؟"', '"مَنْ هُوَ؟"', '"مَا اسْمُكَ؟"'], 'مَا هٰذِهِ؟ dipakai untuk benda berjenis perempuan.', 'medium'),
 (3, 'Di depanmu ada benda berjenis laki-laki. Kamu ingin bertanya namanya. Kalimat tanya yang tepat adalah ....', 'Untuk menanyakan benda berjenis laki-laki, murid berkata', '"مَا هٰذَا؟"', ['"مَا هٰذِهِ؟"', '"مَنْ هِيَ؟"', '"مَا اسْمُكِ؟"'], 'مَا هٰذَا؟ dipakai untuk benda berjenis laki-laki.', 'medium'),
 (3, 'Temanmu menawarkan buah kepadamu. Sikap yang santun adalah ....', 'Ketika ditawari buah oleh teman, murid yang santun', 'mengucapkan terima kasih dan menerimanya dengan tangan kanan', ['merebutnya dari tangan temannya', 'melemparnya kembali ke temannya', 'memalingkan wajah dan diam saja'], 'Santun berarti menghargai pemberian orang lain.', 'easy'),
 (3, 'Temanmu tidak membawa bekal dan kamu membawa dua buah. Sikap yang baik adalah ....', 'Ketika temannya tidak membawa bekal, Dani', 'berbagi buah dengan temannya', ['menyembunyikan buahnya', 'memakan kedua buah sendiri di depan temannya', 'menyuruh temannya pulang'], 'Berbagi adalah akhlak terpuji.', 'easy'),
 (1, 'Kalimat yang benar untuk menunjuk kurma (تَمْرٌ) dari dekat adalah ....', 'Untuk menunjuk kurma (تَمْرٌ) dari dekat, murid berkata', '"هٰذَا تَمْرٌ"', ['"هٰذِهِ تَمْرٌ"', '"تِلْكَ تَمْرٌ"', '"مَنْ تَمْرٌ"'], 'تَمْرٌ adalah kata mudzakkar sehingga memakai هٰذَا.', 'medium'),
 (1, 'Kalimat yang benar untuk menunjuk apel (تُفَّاحَةٌ) dari dekat adalah ....', 'Untuk menunjuk apel (تُفَّاحَةٌ) dari dekat, murid berkata', '"هٰذِهِ تُفَّاحَةٌ"', ['"هٰذَا تُفَّاحَةٌ"', '"ذٰلِكَ تُفَّاحَةٌ"', '"مَنْ تُفَّاحَةٌ"'], 'تُفَّاحَةٌ adalah kata muannats sehingga memakai هٰذِهِ.', 'medium'),
]
SCEN['WR'] = [
 (3, 'Temanmu bertanya warna penamu yang berwarna merah. Sikap jujur adalah menjawab ....', 'Ketika ditanya warna pena yang merah, murid yang jujur menjawab', '"لَوْنُ الْقَلَمِ أَحْمَرُ"', ['"لَوْنُ الْقَلَمِ أَزْرَقُ"', '"لَوْنُ الْقَلَمِ أَخْضَرُ"', '"لَوْنُ الْقَلَمِ أَبْيَضُ"'], 'Jujur berarti menyebut warna sesuai kenyataan.', 'medium'),
 (1, 'Gurumu menunjukkan kartu berwarna kuning dan bertanya warnanya. Jawaban yang benar adalah ....', 'Ketika guru menunjukkan kartu kuning, murid menjawab', '"أَصْفَرُ"', ['"أَخْضَرُ"', '"أَزْرَقُ"', '"أَسْوَدُ"'], 'أَصْفَرُ berarti kuning.', 'easy'),
 (1, 'Langit pada siang hari berwarna biru. Kalimat yang benar adalah ....', 'Untuk menyebut langit siang hari yang biru, murid berkata', '"هٰذِهِ سَمَاءٌ زَرْقَاءُ"', ['"هٰذَا سَمَاءٌ أَزْرَقُ"', '"هٰذِهِ سَمَاءٌ خَضْرَاءُ"', '"هٰذِهِ سَمَاءٌ صَفْرَاءُ"'], 'سَمَاءٌ muannats sehingga memakai هٰذِهِ dan زَرْقَاءُ.', 'hard'),
 (3, 'Temanmu salah menyebut warna benda. Sikap yang baik adalah ....', 'Ketika temannya salah menyebut warna, Zaki', 'membetulkan dengan sopan dan ramah', ['menertawakannya', 'membentaknya', 'membiarkannya salah selamanya'], 'Berinteraksi dengan jujur dan santun.', 'easy'),
 (3, 'Kamu meminjam pensil warna temanmu. Sikap jujur dan santun adalah ....', 'Saat meminjam pensil warna teman, Lani', 'meminta izin dan mengembalikannya', ['mengambilnya diam-diam', 'menyembunyikannya', 'mengatakan itu miliknya'], 'Meminta izin dan mengembalikan barang adalah sikap jujur.', 'easy'),
 (3, 'Kamu tidak sengaja mematahkan pensil warna temanmu. Sikap jujur adalah ....', 'Setelah tidak sengaja mematahkan pensil warna temannya, Umar', 'mengaku dan meminta maaf', ['menyembunyikannya', 'menyalahkan teman lain', 'pura-pura tidak tahu'], 'Jujur berarti berani mengakui kesalahan.', 'medium'),
 (1, 'Kalimat yang benar untuk menunjuk pena merah adalah ....', 'Untuk menunjuk pena merah, murid berkata', '"هٰذَا قَلَمٌ أَحْمَرُ"', ['"هٰذِهِ قَلَمٌ أَحْمَرُ"', '"هٰذَا قَلَمٌ أَزْرَقُ"', '"هٰذَا كِتَابٌ أَحْمَرُ"'], 'قَلَمٌ mudzakkar: هٰذَا قَلَمٌ أَحْمَرُ.', 'medium'),
 (1, 'Kalimat yang benar untuk menunjuk mobil merah adalah ....', 'Untuk menunjuk mobil merah, murid berkata', '"هٰذِهِ سَيَّارَةٌ حَمْرَاءُ"', ['"هٰذَا سَيَّارَةٌ أَحْمَرُ"', '"هٰذِهِ سَيَّارَةٌ خَضْرَاءُ"', '"هٰذِهِ شَجَرَةٌ حَمْرَاءُ"'], 'سَيَّارَةٌ muannats: هٰذِهِ سَيَّارَةٌ حَمْرَاءُ.', 'hard'),
 (1, 'Kamu ingin bertanya warna pintu. Kalimat yang tepat adalah ....', 'Untuk menanyakan warna pintu, murid berkata', '"مَا لَوْنُ الْبَابِ؟"', ['"مَا اسْمُكَ؟"', '"مَنْ هِيَ؟"', '"كَيْفَ حَالُكَ؟"'], 'مَا لَوْنُ ...؟ berarti apa warna ...?', 'medium'),
 (3, 'Warna-warni di sekitar kita adalah ciptaan Allah. Sikap yang baik adalah ....', 'Menghadapi warna-warni ciptaan Allah, murid', 'mensyukuri keindahannya', ['mengabaikannya', 'mengejek warna kesukaan teman', 'merusak tanaman berwarna'], 'Keindahan warna adalah nikmat dari Allah.', 'easy'),
]

# (tp, pernyataan, benar?, penjelasan)
ADAB = {}
ADAB['HB'] = [
 (1, 'Kata "هِوَايَتِي" berarti hobiku.', True, 'هِوَايَتِي = hobiku.'),
 (3, 'Menghargai hobi teman adalah sikap terpuji.', True, 'Menghargai teman adalah akhlak terpuji.'),
 (3, 'Mengejek hobi teman adalah sikap terpuji.', False, 'Mengejek bukan sikap terpuji.'),
 (3, 'Berani menjawab pertanyaan guru dalam bahasa Arab menunjukkan percaya diri.', True, 'Berani menjawab dengan sopan menunjukkan percaya diri.'),
 (3, 'Berbohong tentang hobi adalah sikap jujur.', False, 'Jujur berarti menyebut yang sebenarnya.'),
 (1, 'Kalimat "مَا هِوَايَتُكِ؟" ditanyakan kepada laki-laki.', False, 'مَا هِوَايَتُكِ؟ ditanyakan kepada perempuan.'),
 (4, 'Bahasa Arab adalah bahasa Al-Qur\'an.', True, 'Al-Qur\'an diturunkan dalam bahasa Arab.'),
 (4, 'Belajar bahasa Arab membantu kita memahami ajaran Islam.', True, 'Bahasa Arab membantu mengkaji khazanah keislaman.'),
]
ADAB['BH'] = [
 (1, 'Kata "هٰذِهِ" dipakai untuk menunjuk buah berjenis perempuan seperti تُفَّاحَةٌ.', True, 'تُفَّاحَةٌ adalah muannats.'),
 (1, 'Kata عِنَبٌ memakai kata tunjuk هٰذِهِ.', False, 'عِنَبٌ memakai هٰذَا.'),
 (3, 'Kita perlu mencuci buah sebelum dimakan.', True, 'Mencuci buah menjaga kebersihan.'),
 (3, 'Mengucapkan "اَلْحَمْدُ لِلّٰهِ" setelah makan adalah wujud syukur.', True, 'اَلْحَمْدُ لِلّٰهِ berarti segala puji bagi Allah.'),
 (3, 'Membuang kulit buah sembarangan adalah sikap disiplin.', False, 'Disiplin berarti membuang sampah pada tempatnya.'),
 (1, 'Kata فَاكِهَةٌ berarti sayuran.', False, 'فَاكِهَةٌ berarti buah.'),
 (2, 'Huruf ا tidak disambung dengan huruf sesudahnya.', True, 'Huruf ا, د, ذ, ر, ز, و tidak disambung ke huruf sesudahnya.'),
 (3, 'Menerima pemberian buah dengan tangan kanan adalah sikap santun.', True, 'Menerima dengan tangan kanan dianjurkan.'),
]
ADAB['WR'] = [
 (1, 'Kata لَوْنٌ berarti warna.', True, 'لَوْنٌ = warna.'),
 (1, 'Warna merah dalam bahasa Arab adalah أَحْمَرُ.', True, 'أَحْمَرُ = merah.'),
 (1, 'Kata أَخْضَرُ berarti biru.', False, 'أَخْضَرُ berarti hijau.'),
 (1, 'Warna hitam dalam bahasa Arab adalah أَبْيَضُ.', False, 'Hitam = أَسْوَدُ; أَبْيَضُ = putih.'),
 (3, 'Menyebut warna benda sesuai kenyataan adalah sikap jujur.', True, 'Jujur sesuai kenyataan.'),
 (3, 'Berbohong tentang warna benda milik teman adalah sikap jujur.', False, 'Berbohong bukan sikap jujur.'),
 (3, 'Kita tidak boleh mengejek warna kesukaan teman.', True, 'Menghargai pilihan teman adalah akhlak terpuji.'),
 (1, 'Kata أَزْرَقُ dipakai untuk warna biru.', True, 'أَزْرَقُ = biru.'),
]

PERF = {  # (tp, soal)
 'HB': [(3, 'Katakan kepada temanmu hobimu dengan kalimat "هِوَايَتِي ...."!'),
        (3, 'Bermain peran: tanyakan hobi temanmu dengan "مَا هِوَايَتُكَ؟" atau "مَا هِوَايَتُكِ؟" lalu jawab!'),
        (2, 'Tulislah kata هِوَايَةٌ dan satu nama hobi dalam bahasa Arab dengan rapi dan benar!'),
        (2, 'Gambarlah hobimu dan beri tulisan Arabnya!'),
        (1, 'Bacalah kalimat "أُحِبُّ الْقِرَاءَةَ" dengan lafal yang benar, lalu ganti kata الْقِرَاءَةَ dengan hobimu!'),
        (3, 'Peragakan salah satu hobi (membaca, berenang, atau menggambar) dan minta temanmu menyebut namanya dalam bahasa Arab!')],
 'BH': [(1, 'Tunjuk gambar buah di kartu kosakata dan ucapkan "هٰذِهِ ...." atau "هٰذَا ...." dengan tepat!'),
        (1, 'Bermain peran penjual dan pembeli buah: tanyakan "مَا هٰذَا؟" atau "مَا هٰذِهِ؟" lalu jawab!'),
        (2, 'Tulislah nama tiga buah dalam bahasa Arab dengan memperhatikan huruf pisah dan sambung!'),
        (2, 'Gambarlah satu buah kesukaanmu dan tuliskan namanya dalam bahasa Arab!'),
        (3, 'Ucapkan "شُكْرًا" ketika temanmu memberi buah dan jawab dengan "عَفْوًا" ketika ia berterima kasih!'),
        (1, 'Bacalah teks "هٰذِهِ تُفَّاحَةٌ. هٰذَا عِنَبٌ." dengan lafal yang benar!')],
 'WR': [(1, 'Tunjuk benda berwarna di sekitar kelas dan sebutkan warnanya dalam bahasa Arab!'),
        (1, 'Bermain peran: tanyakan "مَا لَوْنُ ...؟" kepada temanmu lalu jawab dengan nama warna yang tepat!'),
        (2, 'Tulislah nama tiga warna dalam bahasa Arab dengan rapi dan benar!'),
        (2, 'Warnai gambar apel dengan warna yang tepat lalu tulis nama warnanya dalam bahasa Arab!'),
        (3, 'Ceritakan dengan jujur kepada temanmu warna benda yang kamu pinjam, lalu kembalikan dengan baik!'),
        (1, 'Bacalah kalimat "هٰذَا قَلَمٌ أَحْمَرُ" dengan lafal yang benar!')],
}
GROUPS = {  # (tp, soal, {kelompok: [item]})
 'HB': [(3, "Kelompokkan sikap berikut: 'mendengarkan hobi teman'; 'menghargai hobi teman'; 'mengejek hobi teman'; 'menertawakan hobi teman'.",
         {'sikap terpuji': ['mendengarkan hobi teman', 'menghargai hobi teman'], 'sikap tercela': ['mengejek hobi teman', 'menertawakan hobi teman']}),
        (1, "Kelompokkan kalimat berikut menjadi pertanyaan atau jawaban: 'مَا هِوَايَتُكَ؟'; 'هِوَايَتِي الرَّسْمُ'; 'مَا هِوَايَتُكِ؟'; 'هِوَايَتِي السِّبَاحَةُ'.",
         {'pertanyaan': ['مَا هِوَايَتُكَ؟', 'مَا هِوَايَتُكِ؟'], 'jawaban': ['هِوَايَتِي الرَّسْمُ', 'هِوَايَتِي السِّبَاحَةُ']}),
        (1, "Kelompokkan hobi berikut berdasarkan alat yang dipakai: 'كِتَابَةٌ'; 'رَسْمٌ'; 'سِبَاحَةٌ'; 'جَرْيٌ'.",
         {'memakai alat tulis': ['كِتَابَةٌ', 'رَسْمٌ'], 'menggerakkan badan': ['سِبَاحَةٌ', 'جَرْيٌ']})],
 'BH': [(1, "Kelompokkan buah berikut menurut kata tunjuknya: 'تُفَّاحَةٌ'; 'عِنَبٌ'; 'مَوْزَةٌ'; 'تَمْرٌ'; 'خَوْخٌ'; 'بُرْتُقَالَةٌ'.",
         {'هٰذَا': ['عِنَبٌ', 'تَمْرٌ', 'خَوْخٌ'], 'هٰذِهِ': ['تُفَّاحَةٌ', 'مَوْزَةٌ', 'بُرْتُقَالَةٌ']}),
        (3, "Kelompokkan sikap berikut saat makan buah: 'mencuci tangan'; 'berdoa'; 'membuang kulit sembarangan'; 'berebut buah'; 'berbagi'; 'bersyukur'.",
         {'sikap terpuji': ['mencuci tangan', 'berdoa', 'berbagi', 'bersyukur'], 'sikap tercela': ['membuang kulit sembarangan', 'berebut buah']}),
        (1, "Kelompokkan kalimat berikut menjadi pertanyaan atau jawaban: 'مَا هٰذَا؟'; 'هٰذَا عِنَبٌ'; 'مَا هٰذِهِ؟'; 'هٰذِهِ تُفَّاحَةٌ'.",
         {'pertanyaan': ['مَا هٰذَا؟', 'مَا هٰذِهِ؟'], 'jawaban': ['هٰذَا عِنَبٌ', 'هٰذِهِ تُفَّاحَةٌ']})],
 'WR': [(1, "Kelompokkan kata berikut menjadi nama warna atau nama benda: 'أَحْمَرُ'; 'قَلَمٌ'; 'أَزْرَقُ'; 'بَابٌ'; 'أَصْفَرُ'; 'كِتَابٌ'.",
         {'nama warna': ['أَحْمَرُ', 'أَزْرَقُ', 'أَصْفَرُ'], 'nama benda': ['قَلَمٌ', 'بَابٌ', 'كِتَابٌ']}),
        (1, "Kelompokkan benda berikut menurut kata tunjuknya: 'قَلَمٌ'; 'سَيَّارَةٌ'; 'بَابٌ'; 'شَجَرَةٌ'; 'قَمِيصٌ'; 'سَمَاءٌ'.",
         {'هٰذَا': ['قَلَمٌ', 'بَابٌ', 'قَمِيصٌ'], 'هٰذِهِ': ['سَيَّارَةٌ', 'شَجَرَةٌ', 'سَمَاءٌ']}),
        (3, "Kelompokkan sikap berikut saat meminjam pensil warna: 'meminta izin'; 'mengembalikan'; 'mengambil diam-diam'; 'mengaku salah jika rusak'; 'menyembunyikan jika rusak'; 'berterima kasih'.",
         {'sikap jujur dan santun': ['meminta izin', 'mengembalikan', 'mengaku salah jika rusak', 'berterima kasih'], 'sikap tidak jujur': ['mengambil diam-diam', 'menyembunyikan jika rusak']})],
}
ORDERS = {  # (tp, soal, urutan)
 'HB': [(3, 'Urutkan percakapan tentang hobi berikut!', ['السَّلَامُ عَلَيْكُمْ', 'وَعَلَيْكُمُ السَّلَامُ', 'مَا هِوَايَتُكَ؟', 'هِوَايَتِي الْقِرَاءَةُ']),
        (2, 'Urutkan langkah menggambar hobimu berikut!', ['Menyiapkan kertas dan pensil warna', 'Menggambar sketsa', 'Mewarnai gambar', 'Menulis nama gambar dalam bahasa Arab'])],
 'BH': [(1, 'Urutkan percakapan berikut!', ['مَا هٰذِهِ؟', 'هٰذِهِ تُفَّاحَةٌ', 'مَا هٰذَا؟', 'هٰذَا عِنَبٌ']),
        (3, 'Urutkan kegiatan makan buah berikut!', ['Mencuci tangan dan buah', 'Berdoa sebelum makan', 'Memakan buah', 'Mengucap "اَلْحَمْدُ لِلّٰهِ"'])],
 'WR': [(1, 'Urutkan percakapan tentang warna berikut!', ['مَا هٰذَا؟', 'هٰذَا قَلَمٌ', 'مَا لَوْنُهُ؟', 'لَوْنُهُ أَحْمَرُ']),
        (2, 'Urutkan langkah mewarnai gambar berikut!', ['Menyiapkan pensil warna', 'Mengambil pensil warna merah', 'Mewarnai gambar apel', 'Mengembalikan pensil warna ke tempatnya'])],
}

# ----------------------------------------------------------------------------- butir tulis tangan: huruf pisah dan sambung (khusus Bab V)
# (tp, soal, benar, [salah x3], penjelasan, kesulitan)
BH_PISAH = [
 (2, 'Kelompok huruf yang tidak dapat disambung dengan huruf sesudahnya adalah ....', 'ا د ذ ر ز و', ['ب ت ث ج ح خ', 'س ش ص ض ط ظ', 'ع غ ف ق ك ل'], 'Huruf ا, د, ذ, ر, ز, dan و hanya dapat disambung dengan huruf sebelumnya.', 'medium'),
 (2, 'Pada kata لَيْمُونَةٌ, huruf yang tidak disambung dengan huruf sesudahnya adalah ....', 'و (Wawu)', ['ل (Lam)', 'ي (Ya)', 'م (Mim)'], 'و termasuk huruf yang tidak disambung ke huruf sesudahnya.', 'medium'),
 (2, 'Pada kata خَوْخٌ, huruf yang tidak disambung dengan huruf sesudahnya adalah ....', 'و (Wawu)', ['خ (Kha) pertama', 'خ (Kha) terakhir', 'ا (Alif)'], 'و tidak disambung dengan huruf sesudahnya.', 'medium'),
 (2, 'Pada kata تُفَّاحَةٌ, huruf yang tidak disambung dengan huruf sesudahnya adalah ....', 'ا (Alif)', ['ت (Ta)', 'ف (Fa)', 'ح (Ha)'], 'ا tidak disambung ke huruf sesudahnya.', 'medium'),
 (2, 'Pada kata فَاكِهَةٌ, huruf yang tidak disambung dengan huruf sesudahnya adalah ....', 'ا (Alif)', ['ف (Fa)', 'ك (Kaf)', 'ه (Ha)'], 'ا tidak disambung ke huruf sesudahnya.', 'medium'),
]
BH_PISAH_TF = [
 ('Huruf د tidak dapat disambung dengan huruf sesudahnya.', True, 'د termasuk huruf yang tidak disambung ke huruf sesudahnya.'),
 ('Huruf ب dapat disambung dengan huruf sesudahnya.', True, 'ب dapat disambung ke huruf sesudahnya.'),
 ('Huruf ر dapat disambung dengan huruf sesudahnya.', False, 'ر tidak disambung ke huruf sesudahnya.'),
 ('Huruf ز dapat disambung dengan huruf sesudahnya.', False, 'ز tidak disambung ke huruf sesudahnya.'),
 ('Huruf م dapat disambung dengan huruf sesudahnya.', True, 'م dapat disambung ke huruf sesudahnya.'),
 ('Pada kata تُفَّاحَةٌ, huruf ا tidak disambung dengan huruf sesudahnya.', True, 'ا tidak disambung ke huruf sesudahnya.'),
 ('Pada kata مَوْزَةٌ, huruf و tidak disambung dengan huruf sesudahnya.', True, 'و tidak disambung ke huruf sesudahnya.'),
 ('Pada kata بِطِّيخَةٌ, huruf ط tidak dapat disambung dengan huruf sesudahnya.', False, 'ط dapat disambung ke huruf sesudahnya.'),
 ('Huruf ذ tidak dapat disambung dengan huruf sesudahnya.', True, 'ذ termasuk huruf yang tidak disambung ke huruf sesudahnya.'),
 ('Huruf ل tidak dapat disambung dengan huruf sesudahnya.', False, 'ل dapat disambung ke huruf sesudahnya.'),
]
