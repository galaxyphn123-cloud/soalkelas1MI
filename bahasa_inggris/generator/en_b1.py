# -*- coding: utf-8 -*-
from en_gen import *

INTRO = [('menanyakan nama temanmu', 'What is your name?'), ('menyebutkan namamu, Dina', 'My name is Dina.'), ('menanyakan kabar temanmu', 'How are you?'),
         ('menjawab bahwa kabarmu baik', 'I am fine, thank you.'), ('berkenalan dengan teman baru', 'Nice to meet you.'), ('menyebutkan bahwa umurmu enam tahun', 'I am six years old.'),
         ('menanyakan umur temanmu', 'How old are you?'), ('menyebutkan bahwa kamu anak laki-laki', 'I am a boy.'), ('menyebutkan bahwa kamu anak perempuan', 'I am a girl.'),
         ('menyebutkan bahwa kamu seorang murid', 'I am a student.')]
GREET = [('bertemu guru pada pagi hari', 'Good morning'), ('bertemu teman pada siang atau sore hari', 'Good afternoon'), ('bertemu tetangga menjelang malam', 'Good evening'),
         ('bertemu teman di sekolah', 'Hello'), ('menyapa dengan menanyakan kabar', 'How are you')]
RESP = [('How are you?', 'I am fine, thank you.'), ('Good morning!', 'Good morning!'), ('Hello!', 'Hello!'), ('What is your name?', 'My name is Rafi.'),
        ('Nice to meet you.', 'Nice to meet you, too.'), ('Thank you.', 'You are welcome.'), ('Good afternoon!', 'Good afternoon!'), ('How old are you?', 'I am six years old.')]
FARE = [('berpisah dengan teman', 'Goodbye'), ('akan bertemu lagi', 'See you'), ('akan bertemu lagi besok', 'See you tomorrow'),
        ('akan tidur pada malam hari', 'Good night'), ('berpisah dan meminta teman berhati-hati', 'Take care')]
CMD = [('Stand up', 'berdiri'), ('Sit down', 'duduk'), ('Open your book', 'buka bukumu'), ('Close your book', 'tutup bukumu'), ('Listen', 'dengarkan'), ('Look at me', 'lihat saya'),
       ('Raise your hand', 'angkat tanganmu'), ('Clap your hands', 'tepuk tangan'), ('Be quiet', 'tenang'), ('Come here', 'kemari'), ('Touch your head', 'sentuh kepalamu'),
       ('Turn around', 'berbalik'), ('Jump', 'melompat'), ('Line up', 'berbaris')]
WORDS = ['hello', 'goodbye', 'morning', 'afternoon', 'evening', 'night', 'fine', 'thank', 'name', 'friend', 'teacher', 'student']
SENT = [('Good morning, Teacher.', 'selamat pagi, Bu Guru'), ('My name is Dina.', 'namaku Dina'), ('I am fine, thank you.', 'saya baik, terima kasih'), ('Nice to meet you.', 'senang bertemu denganmu'),
        ('How are you today?', 'apa kabar hari ini'), ('See you tomorrow.', 'sampai jumpa besok'), ('Goodbye, my friend.', 'selamat tinggal, temanku'), ('Hello, my name is Rafi.', 'halo, namaku Rafi'),
        ('Good night, Mother.', 'selamat malam, Ibu'), ('Good afternoon, friends.', 'selamat siang, teman-teman')]
VIS = [('Good morning', 'seorang anak berseragam melambai kepada gurunya di gerbang sekolah saat matahari terbit'), ('Good afternoon', 'seorang anak berjalan pulang dari sekolah saat matahari tepat di atas kepala dan menyapa tetangga'),
       ('Good evening', 'sebuah keluarga duduk di teras saat langit berwarna jingga menjelang malam'), ('Good night', 'seorang anak berpiama akan tidur dengan bulan dan bintang terlihat dari jendela'),
       ('Goodbye', 'dua anak saling melambaikan tangan di pintu pagar saat salah satunya akan pergi'), ('Hello', 'dua anak saling melambaikan tangan dan tersenyum saat bertemu di halaman')]


def b1(p):
    c = 'Menyapa dan memperkenalkan diri'
    kv(p, 1, INTRO, "Untuk {k}, kalimat yang tepat adalah '{v}'", "Kalimat '{v}' digunakan untuk ....", c, 'in', 1)
    kv(p, 5, GREET, "Saat {k}, ungkapan sapaan yang tepat adalah '{v}'.", "Ungkapan '{v}' digunakan saat ....", c, 'gr', 2)
    kv(p, 6, RESP, "Jika temanmu berkata '{k}', jawaban yang tepat adalah '{v}'", "Jawaban '{v}' diucapkan untuk membalas ....", c, 'rs', 3)
    kv(p, 7, FARE, "Saat {k}, ungkapan perpisahan yang tepat adalah '{v}'.", "Ungkapan '{v}' digunakan saat ....", c, 'fw', 4)
    kv(p, 4, CMD, "Instruksi guru '{k}' artinya {v}.", "Instruksi guru yang artinya {v} adalah ....", 'Memahami instruksi sederhana', 'cm', 5, extra_wrong=['duduk di lantai', 'menulis nama'])
    vis(p, 5, VIS, 'Perhatikan gambar! Gambar menunjukkan {d}. Ucapan yang tepat adalah ....', c, 'v1', pool=['Thank you', 'Sorry'])
    scr(p, 9, WORDS, 'Menulis kosakata sapaan', 'w1', 1)
    sent(p, 9, SENT, 'Menulis kalimat sapaan sederhana', 's1', 1)
    # TP2 / TP3: sapaan dengan gerakan tubuh
    sq(p, 2, 'Rafi bertemu gurunya di gerbang sekolah. Gerakan tubuh yang tepat untuk menyapa adalah ....', 'Untuk menyapa gurunya, Rafi', 'melambaikan tangan dan tersenyum atau bersalaman', ['membuang muka', 'menutup telinga', 'berlari menjauh'], 'Gerakan menyapa dengan ramah.', 'easy')
    sq(p, 2, 'Dina melihat temannya dari jauh di halaman. Dina ingin menyapa dengan gerakan. Dina ....', 'Untuk menyapa teman dari jauh, Dina', 'melambaikan tangan', ['menggelengkan kepala', 'menunduk saja', 'berbalik badan'], 'Lambaian tangan = menyapa.', 'easy')
    sq(p, 2, 'Perhatikan gambar! Seorang anak melambaikan tangan sambil tersenyum kepada temannya. Gerakan itu berarti ....', 'Gambar anak melambaikan tangan sambil tersenyum menunjukkan gerakan untuk', 'menyapa teman (Hello)', ['mengusir teman', 'meminta makanan', 'menolak bermain'], 'Menyapa.', 'easy', vis='Seorang anak melambaikan tangan sambil tersenyum kepada temannya di halaman sekolah.')
    sq(p, 2, 'Saat bertemu orang yang lebih tua, gerakan menyapa yang sopan adalah ....', 'Menyapa orang yang lebih tua dengan sopan dilakukan dengan', 'bersalaman dan sedikit membungkuk', ['melambaikan tangan sambil berlari', 'menepuk bahunya keras', 'memalingkan wajah'], 'Sopan santun.', 'medium')
    sq(p, 2, 'Fikri ingin berkata "Hello" tanpa suara karena kelas sedang tenang. Fikri bisa ....', 'Menyapa tanpa suara dapat dilakukan dengan', 'melambaikan tangan dan tersenyum', ['berteriak', 'melempar buku', 'menarik baju teman'], 'Sapaan dengan gerakan.', 'medium')
    sq(p, 3, 'Temanmu melambaikan tangan dan berkata "Hello!" Gerakan tubuh yang tepat untuk membalasnya adalah ....', 'Untuk membalas lambaian temannya, Lani', 'melambaikan tangan dan tersenyum', ['memukul bahunya', 'menutup wajah', 'berjalan pergi'], 'Membalas sapaan.', 'easy')
    sq(p, 3, 'Guru menyapa dengan senyum dan mengangguk. Murid membalas dengan ....', 'Untuk membalas anggukan dan senyum guru, murid', 'tersenyum dan mengangguk', ['cemberut', 'berpaling', 'tidur'], 'Membalas dengan ramah.', 'easy')
    sq(p, 3, 'Perhatikan gambar! Dua anak saling berjabat tangan sambil tersenyum. Gerakan itu menunjukkan ....', 'Gambar dua anak berjabat tangan sambil tersenyum menunjukkan', 'saling menyapa dan membalas sapaan', ['pertengkaran', 'perpisahan marah', 'permainan curang'], 'Salam.', 'easy', vis='Dua anak berjabat tangan dan tersenyum di depan kelas.')
    sq(p, 3, 'Ibu guru melambaikan tangan saat murid akan pulang. Murid sebaiknya ....', 'Saat guru melambaikan tangan ketika murid pulang, murid sebaiknya', 'melambaikan tangan kembali', ['mengabaikan guru', 'berteriak', 'berlari tanpa menoleh'], 'Membalas lambaian.', 'easy')
    tfs(p, 2, [('Melambaikan tangan dan tersenyum adalah gerakan menyapa.', True, 'Itu gerakan menyapa.'), ('Membuang muka adalah cara menyapa yang sopan.', False, 'Tidak sopan.')])
    tfs(p, 3, [('Saat dilambaikan tangan oleh teman, kita boleh membalas dengan melambaikan tangan.', True, 'Membalas sapaan itu baik.'), ('Kita tidak perlu membalas sapaan teman.', False, 'Balaslah sapaan.')])
    # TP4 situasi instruksi
    sq(p, 4, 'Guru berkata, "Stand up!" Yang harus dilakukan murid adalah ....', 'Mendengar "Stand up!", murid', 'berdiri', ['duduk', 'tidur', 'menulis'], 'Stand up = berdiri.', 'easy')
    sq(p, 4, 'Guru berkata, "Sit down, please." Gerakan yang tepat adalah ....', 'Mendengar "Sit down, please", murid', 'duduk', ['berdiri', 'melompat', 'berlari'], 'Sit down = duduk.', 'easy')
    sq(p, 4, 'Guru berkata, "Raise your hand." Rafi ....', 'Mendengar "Raise your hand", Rafi', 'mengangkat tangannya', ['menutup bukunya', 'menepuk tangan', 'berdiri di bangku'], 'Raise your hand.', 'easy')
    sq(p, 4, 'Perhatikan gambar! Guru menunjuk ke papan dan berkata, "Look at the board." Murid sebaiknya ....', 'Mendengar "Look at the board", murid', 'melihat ke papan tulis', ['menutup mata', 'membuka tas', 'bermain pensil'], 'Look at = melihat.', 'easy', vis='Guru menunjuk papan tulis dan murid-murid menoleh ke arah papan.')
    sq(p, 4, 'Guru berkata, "Be quiet, please." Murid sebaiknya ....', 'Mendengar "Be quiet, please", murid', 'diam dan tenang', ['berteriak', 'bernyanyi keras', 'berlari'], 'Be quiet = tenang.', 'medium')
    sq(p, 4, 'Guru berkata, "Open your book." lalu "Close your book." Urutan gerakan murid adalah ....', 'Urutan gerakan murid adalah', 'membuka buku, lalu menutup buku', ['menutup buku, lalu membuka buku', 'membuka tas, lalu menutup tas', 'menulis, lalu membaca'], 'Open lalu close.', 'medium')
    tfs(p, 4, [('Instruksi "Clap your hands" artinya tepuk tangan.', True, 'Clap = tepuk.'), ('Instruksi "Sit down" artinya berdiri.', False, 'Sit down = duduk.')])
    # TP8: membaca (guru membacakan) tentang sapaan
    sq(p, 8, 'Guru membacakan: "Rafi: Good morning, Dina. Dina: Good morning, Rafi. How are you? Rafi: I am fine, thank you." Mereka saling menyapa pada waktu ....', 'Menurut dialog Rafi dan Dina, mereka bertemu pada', 'pagi hari', ['siang hari', 'malam hari', 'sore hari'], 'Good morning = pagi.', 'easy')
    sq(p, 8, 'Guru membacakan: "Nisa: Hello, Teacher. Teacher: Hello, Nisa. How are you? Nisa: I am fine, thank you." Nisa menyapa ....', 'Dalam bacaan, Nisa menyapa', 'gurunya', ['ibunya', 'temannya', 'kakaknya'], 'Teacher = guru.', 'easy')
    sq(p, 8, 'Guru membacakan: "Hasan: Goodbye, Zaki. Zaki: See you tomorrow, Hasan." Zaki mengucapkan ....', 'Dalam bacaan, Zaki mengucapkan salam', 'perpisahan', ['perkenalan', 'terima kasih', 'selamat pagi'], 'See you tomorrow.', 'medium')
    sq(p, 8, 'Guru membacakan: "Mira: Good night, Mother. Mother: Good night, Mira." Mereka berbicara pada waktu ....', 'Dalam bacaan, Mira dan ibunya berbicara pada waktu', 'akan tidur di malam hari', ['sarapan pagi', 'pulang sekolah', 'bermain di siang hari'], 'Good night.', 'medium')
    sq(p, 8, 'Guru membacakan: "Dani: Good afternoon, Umar. How are you? Umar: I am fine, thank you." Salam yang digunakan Dani adalah ....', 'Dalam bacaan, Dani menyapa dengan', 'Good afternoon', ['Good morning', 'Good night', 'Goodbye'], 'Good afternoon.', 'easy')
    sq(p, 8, 'Guru membacakan: "Hana: Hello, my name is Hana. Putri: Hello, I am Putri. Nice to meet you." Dua anak itu sedang ....', 'Dalam bacaan, Hana dan Putri sedang', 'berkenalan', ['bertengkar', 'berpamitan', 'belajar berhitung'], 'Nice to meet you = berkenalan.', 'medium')
    # TP1 tambahan: mengenal diri
    sq(p, 1, 'Seorang teman bertanya, "What is your name?" Namamu Alif. Kamu menjawab ....', 'Ditanya "What is your name?", Alif menjawab', 'My name is Alif', ['I am fine', 'Good night', 'See you'], 'Menyebut nama.', 'easy')
    sq(p, 1, 'Guru bertanya, "How old are you?" Umurmu tujuh tahun. Kamu menjawab ....', 'Ditanya "How old are you?", murid berumur tujuh tahun menjawab', 'I am seven years old', ['My name is seven', 'I am fine', 'Goodbye'], 'Menyebut umur.', 'medium')
    sq(p, 1, 'Seorang anak laki-laki memperkenalkan diri: "I am a ...." Kata yang tepat adalah ....', 'Seorang anak laki-laki memperkenalkan dirinya dengan "I am a"', 'boy', ['girl', 'teacher', 'mother'], 'Boy = anak laki-laki.', 'easy')
    for q in ['Perkenalkan dirimu: sebutkan namamu dan umurmu dalam Bahasa Inggris!', 'Ucapkan "My name is ..." dan sebutkan namamu sendiri!', 'Tanyakan nama temanmu dengan "What is your name?" lalu dengarkan jawabannya!',
              'Perkenalkan temanmu kepada kelas dengan "This is my friend, ..."!']:
        p.perf(1, q, R, 'Murid memperkenalkan diri dengan jelas.', 'medium', 'menerapkan', 'Praktik berbicara')
    perfs(p, 5, GREET, "Ucapkan '{v}' saat {k}!")
    perfs(p, 6, RESP[:6], "Jika temanmu berkata '{k}', balaslah dengan '{v}'")
    perfs(p, 7, FARE, "Ucapkan '{v}' saat {k}, sambil melambaikan tangan!")
    perfs(p, 4, CMD[:8], "Lakukan instruksi guru: '{k}'!")
    perfs(p, 2, [('Hello', ''), ('Hi', ''), ('Good morning', '')], "Sapalah temanmu dengan gerakan tubuh dan ucapkan '{k}'!")
    perfs(p, 3, [('Hello', ''), ('Hi', ''), ('Good morning', '')], "Balaslah sapaan '{k}' dari temanmu dengan gerakan tubuh dan ucapan!")
    perfs(p, 9, [('Hello', ''), ('Goodbye', ''), ('Thank you', '')], "Tulislah kata '{k}' dengan rapi pada bukumu!")
    p.group(5, "Kelompokkan ungkapan berikut menjadi sapaan atau perpisahan: Hello; Goodbye; Good morning; See you; Hi; Bye.", {'sapaan': ['Hello', 'Good morning', 'Hi'], 'perpisahan': ['Goodbye', 'See you', 'Bye']}, 'Sapaan dan perpisahan.', 'medium', 'mengelompokkan', c)
    p.group(7, "Kelompokkan ungkapan berikut menurut waktunya: Good morning; Good night; Good afternoon; Good evening; Goodbye; Hello.", {'ucapan menurut waktu': ['Good morning', 'Good afternoon', 'Good evening', 'Good night'], 'bukan ucapan waktu': ['Goodbye', 'Hello']}, 'Ucapan waktu.', 'medium', 'mengelompokkan', c)
    p.order(5, 'Urutkan percakapan berikut dari awal sampai akhir!', ['Hello, Rafi.', 'Hello, Dina. How are you?', 'I am fine, thank you.', 'Goodbye.'], 'Urutan percakapan.', 'medium', 'mengurutkan', c)
    p.order(6, 'Urutkan percakapan perkenalan berikut!', ['Hello, what is your name?', 'My name is Salma.', 'Nice to meet you.', 'Nice to meet you, too.'], 'Urutan perkenalan.', 'medium', 'mengurutkan', c)
