# -*- coding: utf-8 -*-
from en_gen import *

FRUIT = [('mangga', 'mango', 'sebuah mangga kuning'), ('apel', 'apple', 'sebuah apel merah'), ('pisang', 'banana', 'sesisir pisang'), ('jeruk', 'orange', 'sebuah jeruk bulat'),
         ('anggur', 'grapes', 'setandan anggur'), ('semangka', 'watermelon', 'sepotong semangka berdaging merah'), ('nanas', 'pineapple', 'sebuah nanas berduri'), ('pepaya', 'papaya', 'sebuah pepaya berdaging jingga'),
         ('stroberi', 'strawberry', 'sebuah stroberi merah kecil'), ('rambutan', 'rambutan', 'serumpun rambutan berbulu merah')]
PL = {'mango': 'mangoes', 'apple': 'apples', 'banana': 'bananas', 'orange': 'oranges', 'grapes': 'grapes', 'watermelon': 'watermelon', 'pineapple': 'pineapples', 'papaya': 'papaya', 'strawberry': 'strawberries', 'rambutan': 'rambutan'}
ACTS = [('mengupas pisang', 'Peel the banana.'), ('mencuci apel', 'Wash the apple.'), ('memotong semangka', 'Cut the watermelon.'), ('memakan mangga', 'Eat the mango.'), ('memetik jeruk', 'Pick the orange.'),
        ('membeli anggur', 'Buy the grapes.'), ('memeras jeruk', 'Squeeze the orange.'), ('membagi buah', 'Share the fruit.')]
ASKQ = [('menanyakan apakah temanmu suka mangga', 'Do you like mangoes?'), ('menanyakan buah kesukaan temanmu', 'What fruit do you like?'), ('menanyakan apakah temanmu suka apel', 'Do you like apples?'),
        ('menanyakan apakah temanmu suka pisang', 'Do you like bananas?'), ('menanyakan buah kesukaan gurumu', 'What fruit do you like, Teacher?'), ('menanyakan apakah temanmu suka jeruk', 'Do you like oranges?')]
LIKE = [('menyatakan suka mangga', 'I like mangoes.'), ('menyatakan suka apel', 'I like apples.'), ('menyatakan suka pisang', 'I like bananas.'), ('menyatakan sangat suka semangka', 'I love watermelon.'),
        ('menjawab "ya" bahwa kamu suka', 'Yes, I do.'), ('menyatakan suka stroberi', 'I like strawberries.')]
DISL = [('menyatakan tidak suka jeruk', 'I do not like oranges.'), ('menyatakan tidak suka nanas', 'I do not like pineapples.'), ('menyatakan tidak suka anggur', 'I do not like grapes.'),
        ('menjawab "tidak" bahwa kamu tidak suka', 'No, I do not.'), ('menyatakan tidak suka pepaya', 'I do not like papaya.'), ('menyatakan tidak suka rambutan', 'I do not like rambutan.')]
GEST = [('mengacungkan jempol sambil tersenyum', 'suka'), ('mengangguk sambil tersenyum', 'suka'), ('mengusap perut sambil tersenyum', 'enak dan suka'), ('membalikkan jempol ke bawah', 'tidak suka'),
        ('menggelengkan kepala sambil mengernyit', 'tidak suka'), ('menutup hidung dan mengerutkan wajah', 'tidak suka')]


def b8(p):
    c = 'Mengenal buah-buahan'
    kv(p, 1, [(i, e) for i, e, _ in FRUIT], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'fr', 1)
    vis(p, 1, [(e, d) for _, e, d in FRUIT], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris buah itu disebut ....', c, 'vf', pool=['cabbage', 'carrot'])
    kv(p, 2, ACTS, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Instruksi '{v}' artinya ....", 'Tindakan terhadap buah', 'ac', 2)
    kv(p, 3, ASKQ, "Untuk {k}, kamu berkata '{v}'", "Pertanyaan '{v}' dipakai untuk ....", 'Bertanya tentang kesukaan', 'aq', 3)
    kv(p, 4, LIKE, "Untuk {k}, kamu berkata '{v}'", "Ungkapan '{v}' dipakai untuk ....", 'Menyatakan suka', 'lk', 4)
    kv(p, 5, DISL, "Untuk {k}, kamu berkata '{v}'", "Ungkapan '{v}' dipakai untuk ....", 'Menyatakan tidak suka', 'dl', 5)
    kv(p, 6, GEST, "Gerakan tubuh {k} berarti {v}.", None, 'Gerakan suka dan tidak suka', 'gs', 6, extra_wrong=['bertanya', 'berpamitan'], match=False)
    scr(p, 7, [e for _, e, _ in FRUIT if ' ' not in e] + ['like', 'eat', 'love', 'juice'], 'Menulis kosakata', 'w8', 8)
    sent(p, 7, [('I like mangoes.', 'aku suka mangga'), ('I like red apples.', 'aku suka apel merah'), ('I do not like oranges.', 'aku tidak suka jeruk'), ('Do you like bananas?', 'apakah kamu suka pisang'),
                ('I love watermelon.', 'aku suka sekali semangka'), ('I do not like pineapples.', 'aku tidak suka nanas'), ('What fruit do you like?', 'buah apa yang kamu suka'), ('Yes, I do.', 'ya, aku suka')], 'Menulis frase buah', 's8', 8)
    sent(p, 3, [('Do you like apples?', 'apakah kamu suka apel'), ('Do you like grapes?', 'apakah kamu suka anggur'), ('What fruit do you like?', 'buah apa yang kamu suka')], 'Bertanya kesukaan', 's8b', 9)
    for i, e, d in FRUIT[:8]:
        sq(p, 4, f'Teman bertanya, "Do you like {PL[e]}?" Kamu suka {i}. Jawabanmu ....', f'Ditanya "Do you like {PL[e]}?" oleh teman dan kamu suka {i}, kamu menjawab', f'Yes, I do. I like {PL[e]}',
           ['No, I do not', 'Goodbye, my friend', 'Good night'], 'Menyatakan suka.', 'easy', comp='Menyatakan suka')
    for i, e, d in FRUIT[:8]:
        sq(p, 5, f'Teman bertanya, "Do you like {PL[e]}?" Kamu tidak suka {i}. Jawabanmu ....', f'Ditanya "Do you like {PL[e]}?" oleh teman dan kamu tidak suka {i}, kamu menjawab', f'No, I do not. I do not like {PL[e]}',
           ['Yes, I do', 'Hello, my friend', 'Good morning'], 'Menyatakan tidak suka.', 'easy', comp='Menyatakan tidak suka')
    sq(p, 6, 'Temanmu menawarkan apel. Kamu suka. Gerakan tubuh yang tepat adalah ....', 'Jika menyukai tawaran buah dari teman, kita', 'mengacungkan jempol dan tersenyum', ['menutup hidung', 'menggelengkan kepala keras', 'berpaling'], 'Suka = jempol naik.', 'easy', comp='Gerakan suka dan tidak suka')
    sq(p, 6, 'Temanmu menawarkan durian, tetapi kamu tidak suka. Gerakan tubuh yang sopan untuk menolak adalah ....', 'Jika tidak menyukai tawaran buah dari teman, kita', 'menggelengkan kepala sambil tersenyum sopan', ['melempar buahnya', 'berteriak', 'mengejek temannya'], 'Menolak dengan sopan.', 'medium', comp='Gerakan suka dan tidak suka')
    sq(p, 6, 'Perhatikan gambar! Seorang anak mengacungkan jempol sambil memegang sepotong semangka. Gerakan itu berarti ....', 'Gambar anak mengacungkan jempol sambil memegang semangka berarti', 'dia suka semangka', ['dia tidak suka semangka', 'dia ingin pulang', 'dia sedang marah'], 'Jempol = suka.', 'easy', vis='Anak laki-laki tersenyum mengacungkan jempol sambil memegang sepotong semangka.', comp='Gerakan suka dan tidak suka')
    sq(p, 6, 'Perhatikan gambar! Seorang anak menutup hidung dan mengerutkan wajah di depan sebuah nanas. Gerakan itu berarti ....', 'Gambar anak menutup hidung di depan nanas berarti', 'dia tidak suka nanas', ['dia suka nanas', 'dia ingin membeli nanas', 'dia sedang berpamitan'], 'Mengerutkan wajah = tidak suka.', 'medium', vis='Anak menutup hidung dan mengerutkan wajah sambil menjauhkan sebuah nanas.', comp='Gerakan suka dan tidak suka')
    for i, e, d in FRUIT[:5]:
        p.perf(1, f"Tunjuk gambar '{e}' lalu ucapkan namanya dalam Bahasa Inggris!", R, 'Murid menyebutkan dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    for cmd, _ in ACTS[:5]:
        p.perf(2, f"Peragakan perintah ini dengan buah mainan: '{cmd}'", R, 'Murid memeragakan dengan tepat.', 'medium', 'menerapkan', 'Tindakan terhadap buah')
    for q in ['Tanyakan kepada temanmu: "Do you like mangoes?" lalu dengarkan jawabannya!', 'Tanyakan buah kesukaan temanmu dengan "What fruit do you like?"', 'Bertanyalah kepada tiga temanmu tentang buah kesukaan mereka!', 'Tanyakan kepada gurumu: "Do you like apples?"']:
        p.perf(3, q, R, 'Murid bertanya dengan jelas.', 'medium', 'menerapkan', 'Bertanya tentang kesukaan')
    for s, e in LIKE[:4]:
        p.perf(4, f"Ucapkan '{e}' sambil mengacungkan jempol!", R, 'Murid mengucapkan dengan jelas.', 'medium', 'menerapkan', 'Menyatakan suka')
    for s, e in DISL[:4]:
        p.perf(5, f"Ucapkan '{e}' dengan sopan sambil menggelengkan kepala!", R, 'Murid mengucapkan dengan jelas.', 'medium', 'menerapkan', 'Menyatakan tidak suka')
    for q in ['Peragakan gerakan tubuh untuk menyatakan suka pada buah!', 'Peragakan gerakan tubuh untuk menyatakan tidak suka dengan sopan!', 'Tunjukkan gerakan suka dan tidak suka secara bergantian saat guru menyebut nama buah!']:
        p.perf(6, q, R, 'Murid menggunakan gerakan yang tepat.', 'medium', 'menerapkan', 'Gerakan suka dan tidak suka')
    for e in ['apple', 'mango', 'banana', 'orange', 'grapes', 'strawberry', 'watermelon', 'pineapple']:
        p.perf(8, f'Gambarlah {e} atau buah kesukaanmu, warnai, lalu katakan "I like {e}."', R, 'Murid menggambar dan menyebutkan buah kesukaan.', 'medium', 'menerapkan', 'Menggambar buah kesukaan')
    sq(p, 8, 'Guru berkata, "Draw your favorite fruit." Yang harus kamu lakukan adalah ....', 'Mendengar "Draw your favorite fruit", murid', 'menggambar buah kesukaannya', ['menulis namanya', 'memakan buah', 'menyanyi'], 'Draw = menggambar.', 'easy', comp='Menggambar buah kesukaan')
    sq(p, 8, 'Setelah menggambar buah kesukaanmu, guru bertanya, "What fruit is it?" Kamu menggambar mangga. Jawabanmu ....', 'Ditanya "What fruit is it?" tentang gambar mangga, murid menjawab', 'It is a mango', ['It is a banana', 'It is a table', 'It is a cat'], 'Menyebut buah gambarmu.', 'easy', comp='Menggambar buah kesukaan')
    sq(p, 8, 'Guru berkata, "Color your apple red." Kamu harus menggunakan krayon ....', 'Mendengar "Color your apple red", murid memakai krayon', 'merah', ['biru', 'hijau', 'hitam'], 'Red = merah.', 'easy', comp='Menggambar buah kesukaan')
    sq(p, 8, 'Guru berkata, "Draw a yellow banana." Gambar yang benar adalah ....', 'Mendengar "Draw a yellow banana", murid menggambar', 'pisang berwarna kuning', ['apel berwarna kuning', 'pisang berwarna biru', 'jeruk berwarna hijau'], 'Yellow banana.', 'medium', comp='Menggambar buah kesukaan')
    p.group(1, 'Kelompokkan buah berikut: mango; apple; banana; orange; grapes; watermelon menurut cara memakannya: dikupas atau tidak dikupas.', {'biasanya dikupas': ['banana', 'orange', 'mango'], 'biasanya langsung dimakan': ['apple', 'grapes', 'watermelon']}, 'Cara makan buah.', 'medium', 'mengelompokkan', c)
    p.group(4, 'Kelompokkan ungkapan berikut: I like mangoes; I do not like grapes; I love apples; I do not like oranges; Yes, I do; No, I do not.', {'suka': ['I like mangoes', 'I love apples', 'Yes, I do'], 'tidak suka': ['I do not like grapes', 'I do not like oranges', 'No, I do not']}, 'Suka dan tidak suka.', 'medium', 'mengelompokkan', 'Menyatakan suka')
    p.order(3, 'Urutkan percakapan tentang buah berikut!', ['Do you like mangoes?', 'Yes, I do.', 'What fruit do you like?', 'I like apples.'], 'Urutan tanya jawab.', 'medium', 'mengurutkan', 'Bertanya tentang kesukaan')
    p.order(2, 'Urutkan cara menyiapkan buah berikut!', ['Buy the orange.', 'Wash the orange.', 'Peel the orange.', 'Eat the orange.'], 'Urutan menyiapkan buah.', 'medium', 'mengurutkan', 'Tindakan terhadap buah')
    tfs(p, 4, [('"I like mangoes" artinya aku suka mangga.', True, 'Like = suka.'), ('"I do not like mangoes" artinya aku suka mangga.', False, 'Do not like = tidak suka.')], 'Menyatakan suka')
    tfs(p, 5, [('"I do not like grapes" artinya aku tidak suka anggur.', True, 'Do not like = tidak suka.'), ('Kita boleh mengejek teman yang tidak suka buah tertentu.', False, 'Hormati pilihan teman.')], 'Menyatakan tidak suka')
