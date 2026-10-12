# -*- coding: utf-8 -*-
from en_gen import *
from en_common import COLOR

PET = [('kucing', 'cat', 'seekor kucing sedang duduk'), ('anjing', 'dog', 'seekor anjing sedang menggonggong'), ('burung', 'bird', 'seekor burung di dalam sangkar'), ('ikan', 'fish', 'seekor ikan di dalam akuarium'),
       ('kelinci', 'rabbit', 'seekor kelinci bertelinga panjang'), ('hamster', 'hamster', 'seekor hamster kecil di roda putar'), ('kura-kura', 'turtle', 'seekor kura-kura bercangkang'), ('burung beo', 'parrot', 'seekor burung beo berwarna-warni')]
ACTS = [('memberi makan kucing', 'Feed the cat.'), ('memandikan anjing', 'Wash the dog.'), ('mengajak anjing berjalan', 'Walk the dog.'), ('bermain dengan kelinci', 'Play with the rabbit.'),
        ('membelai kucing', 'Pet the cat.'), ('memberi minum burung', 'Give water to the bird.'), ('memegang hamster dengan lembut', 'Hold the hamster gently.'), ('membersihkan kandang', 'Clean the cage.')]
PCOL = [('cat', 'black', 'seekor kucing berwarna hitam'), ('dog', 'white', 'seekor anjing berwarna putih'), ('bird', 'yellow', 'seekor burung berwarna kuning'), ('fish', 'red', 'seekor ikan berwarna merah'),
        ('rabbit', 'brown', 'seekor kelinci berwarna cokelat'), ('parrot', 'green', 'seekor burung beo berwarna hijau'), ('hamster', 'orange', 'seekor hamster berwarna oranye'), ('turtle', 'green', 'seekor kura-kura berwarna hijau')]
SHOP = [('kandang', 'cage'), ('rak', 'shelf'), ('makanan hewan', 'pet food'), ('penjual', 'seller'), ('pembeli', 'customer'), ('akuarium', 'aquarium'), ('toko hewan', 'pet shop'), ('mainan hewan', 'pet toy')]
PLACE = [('Put the cat in the cage.', 'meletakkan kucing di dalam kandang'), ('Put the fish in the aquarium.', 'meletakkan ikan di dalam akuarium'), ('Put the food on the shelf.', 'meletakkan makanan di atas rak'),
         ('Put the toy on the table.', 'meletakkan mainan di atas meja'), ('Put the bird in the cage.', 'meletakkan burung di dalam sangkar'), ('Put the dog near the door.', 'meletakkan anjing dekat pintu')]
DESC = [('Kucingku kecil', 'My cat is small.'), ('Anjingku besar', 'My dog is big.'), ('Ikanku berwarna merah', 'My fish is red.'), ('Kelinciku suka wortel', 'My rabbit likes carrots.'),
        ('Burungku bisa bernyanyi', 'My bird can sing.'), ('Kura-kuraku berjalan lambat', 'My turtle is slow.'), ('Hamsterku lucu', 'My hamster is cute.'), ('Kucingku lembut', 'My cat is soft.')]


def b6(p):
    c = 'Mengenal hewan peliharaan'
    kv(p, 1, [(i, e) for i, e, _ in PET], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'pt', 1)
    vis(p, 2, [(e, d) for _, e, d in PET], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris hewan itu disebut ....', c, 'vp', pool=['cow', 'horse'])
    kv(p, 2, [('hewan yang mengeong', 'cat'), ('hewan yang menggonggong', 'dog'), ('hewan yang berkicau di sangkar', 'bird'), ('hewan yang berenang di akuarium', 'fish'), ('hewan yang suka wortel', 'rabbit'),
              ('hewan kecil yang berlari di roda putar', 'hamster'), ('hewan yang membawa cangkang', 'turtle'), ('hewan yang bisa menirukan suara manusia', 'parrot')], "Hewan peliharaan {k} disebut '{v}'.", "'{v}' adalah ....", c, 'pd', 2)
    kv(p, 4, ACTS, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Instruksi '{v}' artinya ....", 'Tindakan terhadap hewan peliharaan', 'ac', 3)
    kv(p, 6, [(d, f'{col}') for _, col, d in PCOL], "Terdapat {k}. Warnanya dalam Bahasa Inggris adalah '{v}'.", None, 'Warna hewan peliharaan', 'pc', 4, match=False)
    vis(p, 6, [(col, d) for _, col, d in PCOL], 'Perhatikan gambar! Gambar menunjukkan {d}. Warnanya dalam Bahasa Inggris adalah ....', 'Warna hewan peliharaan', 'vc')
    kv(p, 5, [('Draw a cat.', 'menggambar seekor kucing'), ('Draw a fish.', 'menggambar seekor ikan'), ('Draw a bird.', 'menggambar seekor burung'), ('Draw a dog.', 'menggambar seekor anjing'),
              ('Color the cat black.', 'mewarnai kucing dengan warna hitam'), ('Color the fish red.', 'mewarnai ikan dengan warna merah'), ('Color the bird yellow.', 'mewarnai burung dengan warna kuning'),
              ('Color the rabbit brown.', 'mewarnai kelinci dengan warna cokelat')], "Guru berkata '{k}' Artinya kamu harus {v}.", "Guru ingin kamu {v}. Instruksi yang tepat adalah ....", 'Menggambar dan mewarnai', 'dr', 8)
    count(p, 7, 'cat', 'kucing', 'Terlihat {n} {noun} di sofa', 'Menghitung hewan', 'cc')
    count(p, 7, 'fish', 'ikan', 'Terlihat {n} {noun} di akuarium', 'Menghitung hewan', 'cf')
    count(p, 7, 'bird', 'burung', 'Terlihat {n} {noun} di dahan', 'Menghitung hewan', 'cb')
    kv(p, 8, DESC, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Mendeskripsikan hewan', 'dp', 5)
    kv(p, 10, SHOP, "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", 'Menyusun toko hewan', 'sh', 6)
    kv(p, 10, PLACE, "Instruksi '{k}' artinya {v}.", "Instruksi untuk {v} adalah ....", 'Menyusun toko hewan', 'pl', 7)
    vis(p, 11, [(f'The {a} is in the {b}.', d) for a, b, d in [('cat', 'cage', 'seekor kucing di dalam kandang'), ('fish', 'aquarium', 'seekor ikan di dalam akuarium'), ('bird', 'cage', 'seekor burung di dalam sangkar'),
                ('food', 'shelf', 'makanan hewan di atas rak'), ('rabbit', 'cage', 'seekor kelinci di dalam kandang')]], 'Perhatikan gambar toko hewan! Gambar menunjukkan {d}. Kalimat yang tepat adalah ....', 'Mendeskripsikan toko hewan', 'vs',
        pool=['The dog is on the table.', 'The cat is in the aquarium.'])
    scr(p, 9, [e for _, e, _ in PET if ' ' not in e] + ['pet', 'feed', 'walk', 'play', 'cage', 'shelf', 'shop'], 'Menulis kosakata', 'w6', 6)
    sent(p, 9, [('I have a black cat.', 'aku punya kucing hitam'), ('I have two white dogs.', 'aku punya dua anjing putih'), ('It is a red fish.', 'itu ikan merah'), ('I have a brown rabbit.', 'aku punya kelinci cokelat'),
                ('My bird is yellow.', 'burungku kuning'), ('The turtle is green.', 'kura-kuranya hijau'), ('I have three fish.', 'aku punya tiga ikan'), ('My hamster is orange.', 'hamsterku oranye')], 'Menulis frase hewan dan warna', 's6', 6)
    sent(p, 11, [('The cat is in the cage.', 'kucing ada di dalam kandang'), ('The fish is in the aquarium.', 'ikan ada di akuarium'), ('There are two birds.', 'ada dua burung'), ('The food is on the shelf.', 'makanan ada di rak'),
                 ('This is a pet shop.', 'ini toko hewan')], 'Mendeskripsikan toko hewan', 's6b', 7)
    # peran
    sq(p, 3, 'Dalam bermain peran di toko hewan, pembeli berkata, "I want a cat, please." Penjual menjawab ....', 'Dalam peran penjual, saat pembeli berkata "I want a cat, please", penjual menjawab', 'Here you are', ['Goodbye, Teacher', 'I am a dog', 'Open the door'], 'Menyerahkan sambil menjawab sopan.', 'medium', comp='Bermain peran')
    sq(p, 3, 'Penjual berkata, "This is a white rabbit." Pembeli ingin berterima kasih. Pembeli berkata ....', 'Dalam peran pembeli, untuk berterima kasih, pembeli berkata', 'Thank you', ['Sit down', 'I am sorry, goodbye', 'Stand up'], 'Terima kasih.', 'easy', comp='Bermain peran')
    sq(p, 3, 'Dalam permainan peran, kamu menjadi kucing. Kamu menirukan suara dan gerakan ....', 'Saat berperan menjadi kucing, kamu menirukan', 'mengeong dan berjalan merangkak', ['menggonggong', 'berenang', 'terbang'], 'Peran kucing.', 'easy', comp='Bermain peran')
    sq(p, 3, 'Dalam permainan peran, temanmu menjadi anjing. Ia menirukan suara ....', 'Teman yang berperan menjadi anjing menirukan suara', 'guk-guk (woof)', ['meong (meow)', 'cuit (tweet)', 'muu (moo)'], 'Suara anjing.', 'easy', comp='Bermain peran')
    sq(p, 3, 'Perhatikan gambar! Dua anak bermain peran: satu menjadi penjual hewan dan satu menjadi pembeli. Penjual menyapa, "Hello! Can I help you?" Pembeli menjawab ....', 'Pembeli yang ingin membeli hewan menjawab penjual dengan', 'I want a dog, please', ['I like the door', 'Stand up, please', 'Good night'], 'Menjawab sapaan penjual.', 'medium', vis='Dua anak bermain peran di toko hewan mainan; satu berdiri di balik meja, satu di depan meja.', comp='Bermain peran')
    for i, e, d in PET[:6]:
        sq(p, 1, f'Guru menunjukkan gambar {d} dan bertanya, "What is it?" Jawabanmu ....', f'Ditanya "What is it?" tentang {d}, murid menjawab', f'It is a {e}' if e[0] not in 'aeiou' else f'It is an {e}',
           [f'It is a {x}' for x in ['book', 'table', 'chair', 'door'] if x != e][:3], f'{e} = {i}.', 'easy', comp=c)
    for q in [f"Tirukan gerakan dan suara '{a}' dengan temanmu dalam permainan peran!" for a in ['cat', 'dog', 'bird']] + ['Berperan sebagai penjual hewan dan sapa pembelimu dengan "Hello! Can I help you?"', 'Berperan sebagai pembeli dan katakan "I want a rabbit, please."']:
        p.perf(3, q, R, 'Murid bermain peran dengan percaya diri.', 'medium', 'menerapkan', 'Bermain peran')
    for cmd, _ in ACTS[:5]:
        p.perf(4, f"Peragakan perintah ini dengan boneka hewan: '{cmd}'", R, 'Murid memeragakan dengan tepat.', 'medium', 'menerapkan', 'Tindakan terhadap hewan peliharaan')
    for i, e, d in PET[:5]:
        p.perf(5, f'Gambarlah seekor {i} lalu warnai dengan warna kesukaanmu, lalu sebutkan "It is a ... {e}"!', R, 'Murid menggambar, mewarnai, dan menyebutkan.', 'medium', 'menerapkan', 'Menggambar dan mewarnai')
    for e, col, d in PCOL[:4]:
        p.perf(6, f"Ambil krayon {col} lalu warnai gambar {e}, dan ucapkan 'a {col} {e}'", R, 'Murid memilih warna yang benar.', 'medium', 'menerapkan', 'Warna hewan peliharaan')
    for n, w in [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]:
        p.perf(7, f'Hitung gambar hewan yang disiapkan guru dan katakan "I have {w} pets."', R, 'Murid menghitung dengan benar.', 'medium', 'menerapkan', 'Menghitung hewan')
    for s, e in DESC[:4]:
        p.perf(8, f"Ceritakan hewan peliharaanmu (atau hewan impianmu) dengan mengucapkan '{e}'", R, 'Murid bercerita singkat.', 'medium', 'menerapkan', 'Mendeskripsikan hewan')
    for q in ['Susun gambar toko hewan: tempelkan kandang, rak, dan akuarium pada kertas sesuai instruksi guru!', 'Susun gambar toko hewan lalu tunjuk dan sebutkan "cage", "shelf", dan "aquarium"!', 'Letakkan gambar hewan pada tempatnya di toko hewan sesuai kata guru!']:
        p.perf(10, q, R, 'Murid menyusun gambar dengan benar.', 'medium', 'menerapkan', 'Menyusun toko hewan')
    for q in ['Tunjuk gambar toko hewan lalu katakan "This is a pet shop."', 'Ceritakan isi gambar toko hewan: "There is a cat in the cage."', 'Sebutkan tiga hal yang ada di gambar toko hewan dalam Bahasa Inggris!']:
        p.perf(11, q, R, 'Murid mendeskripsikan gambar.', 'medium', 'menerapkan', 'Mendeskripsikan toko hewan')
    p.group(1, 'Kelompokkan hewan peliharaan berikut: fish; cat; bird; dog; turtle; parrot.', {'hewan berkaki empat': ['cat', 'dog', 'turtle'], 'hewan lain': ['fish', 'bird', 'parrot']}, 'Berkaki empat.', 'medium', 'mengelompokkan', c)
    p.group(4, 'Kelompokkan tindakan: Feed the cat; Hit the dog; Pet the rabbit; Throw the bird; Wash the dog; Hold the hamster gently.', {'tindakan baik': ['Feed the cat', 'Pet the rabbit', 'Wash the dog', 'Hold the hamster gently'], 'tindakan buruk': ['Hit the dog', 'Throw the bird']}, 'Menyayangi hewan.', 'medium', 'mengelompokkan', 'Tindakan terhadap hewan peliharaan')
    p.order(4, 'Urutkan cara merawat kucing berikut: panggil kucing, beri makan, belai, bersihkan mangkuk!', ['Call the cat.', 'Feed the cat.', 'Pet the cat.', 'Clean the bowl.'], 'Urutan merawat kucing.', 'medium', 'mengurutkan', 'Tindakan terhadap hewan peliharaan')
    tfs(p, 4, [('"Feed the cat" artinya beri makan kucing.', True, 'Feed = beri makan.'), ('"Walk the dog" artinya memandikan anjing.', False, 'Walk = berjalan; wash = memandikan.')], 'Tindakan terhadap hewan peliharaan')
