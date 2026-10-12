# -*- coding: utf-8 -*-
from en_gen import *

FACE = [('mata', 'eye', 'sepasang mata pada wajah anak'), ('hidung', 'nose', 'hidung pada wajah anak'), ('mulut', 'mouth', 'mulut yang tersenyum pada wajah anak'),
        ('telinga', 'ear', 'telinga di sisi kepala anak'), ('alis', 'eyebrow', 'alis di atas mata'), ('rambut', 'hair', 'rambut hitam anak'), ('pipi', 'cheek', 'pipi kemerahan anak'),
        ('dahi', 'forehead', 'dahi anak yang sedang ditepuk'), ('gigi', 'tooth', 'gigi putih anak yang sedang tersenyum'), ('lidah', 'tongue', 'lidah anak yang dijulurkan'),
        ('dagu', 'chin', 'dagu anak yang ditunjuk'), ('bibir', 'lip', 'bibir anak')]
FUNC = [('melihat', 'eyes'), ('mendengar', 'ears'), ('mencium bau', 'nose'), ('makan dan berbicara', 'mouth'), ('mengunyah makanan', 'teeth'), ('merasakan rasa makanan', 'tongue')]
LOC = [('di atas mata', 'eyebrows'), ('di tengah wajah di antara mata dan mulut', 'nose'), ('di bawah hidung', 'mouth'), ('di kedua sisi kepala', 'ears'), ('di atas alis', 'forehead'),
       ('di bawah mulut', 'chin'), ('di kedua sisi wajah dekat hidung', 'cheeks'), ('di dalam mulut', 'tongue')]
DESC = [('Aku punya dua mata', 'I have two eyes.'), ('Aku punya satu hidung', 'I have one nose.'), ('Aku punya satu mulut', 'I have one mouth.'), ('Aku punya dua telinga', 'I have two ears.'),
        ('Rambutku hitam', 'My hair is black.'), ('Rambutku panjang', 'My hair is long.'), ('Rambutku pendek', 'My hair is short.'), ('Hidungku kecil', 'My nose is small.'),
        ('Mataku besar', 'My eyes are big.'), ('Pipiku bulat', 'My cheeks are round.')]
CNT = [('mata', 'two eyes'), ('hidung', 'one nose'), ('mulut', 'one mouth'), ('telinga', 'two ears'), ('alis', 'two eyebrows'), ('pipi', 'two cheeks'), ('dahi', 'one forehead'), ('dagu', 'one chin')]
TCH = [('Touch your nose.', 'menyentuh hidungmu'), ('Touch your eyes.', 'menyentuh matamu'), ('Touch your ears.', 'menyentuh telingamu'), ('Touch your mouth.', 'menyentuh mulutmu'),
       ('Point to your hair.', 'menunjuk rambutmu'), ('Touch your cheeks.', 'menyentuh pipimu'), ('Touch your chin.', 'menyentuh dagumu'), ('Close your eyes.', 'memejamkan matamu'),
       ('Open your mouth.', 'membuka mulutmu'), ('Cover your ears.', 'menutup telingamu'), ('Point to your forehead.', 'menunjuk dahimu')]


def b3(p):
    c = 'Mengenal bagian wajah'
    kv(p, 1, [(i, e) for i, e, _ in FACE], "Bagian wajah {k} dalam Bahasa Inggris adalah '{v}'.", "Kata '{v}' menunjukkan bagian wajah yaitu ....", c, 'fc', 1)
    vis(p, 1, [(e, d) for _, e, d in FACE], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris bagian itu disebut ....', c, 'vf', pool=['hand', 'leg'])
    kv(p, 1, FUNC, "Bagian wajah yang dipakai untuk {k} adalah '{v}'.", "Dengan '{v}', kita dapat ....", c, 'fu', 2)
    kv(p, 2, LOC, "Bagian wajah yang letaknya {k} adalah '{v}'.", None, 'Mengetahui letak bagian wajah', 'lc', 3)
    kv(p, 2, TCH, "Instruksi '{k}' artinya {v}.", "Guru ingin kamu {v}. Instruksi yang tepat adalah ....", 'Merespon instruksi secara fisik', 'tc', 4)
    kv(p, 3, DESC, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Mendeskripsikan wajah', 'ds', 5)
    kv(p, 4, CNT, "Jumlah {k} pada wajah dalam Bahasa Inggris adalah '{v}'.", "'{v}' menunjukkan jumlah dan nama bagian wajah yaitu ....", 'Menyebut nama dan jumlah', 'cn', 6)
    for i, e, d in FACE[:8]:
        sq(p, 2, f'Guru berkata, "Touch your {e}." Murid harus menyentuh ....', f'Mendengar "Touch your {e}", murid menyentuh', i, [x for x in ['mata', 'hidung', 'mulut', 'telinga', 'kaki', 'tangan'] if x != i][:3], f'{e} = {i}.', 'easy', comp='Merespon instruksi secara fisik')
    for i, e, d in FACE[:6]:
        n = 2 if e in ('eye', 'ear') else 1
        pl = e + 's'
        sq(p, 4, f'Seorang anak menunjukkan gambar wajah dan bertanya, "How many {pl} do I have?" Jumlah {i} pada wajah adalah ....',
           f'Jumlah {i} pada wajah anak dalam Bahasa Inggris adalah', 'two' if n == 2 else 'one', [x for x in ['one', 'two', 'three', 'four'] if x != ('two' if n == 2 else 'one')], f'{i}: {n}.', 'medium', comp='Menyebut nama dan jumlah')
    tfs(p, 1, [('"Eyes" artinya mata.', True, 'Eyes = mata.'), ('"Nose" artinya telinga.', False, 'Nose = hidung, ear = telinga.')])
    tfs(p, 3, [('"I have two eyes" artinya aku punya dua mata.', True, 'Terjemahan benar.'), ('"I have two noses" artinya aku punya dua mata.', False, 'noses = hidung.')])
    sq(p, 3, 'Perhatikan gambar! Seorang anak berambut hitam panjang. Kalimat yang menggambarkannya adalah ....', 'Gambar anak berambut hitam panjang dideskripsikan dengan', 'My hair is long and black', ['My hair is short and red', 'My nose is long', 'I have three eyes'], 'Mendeskripsikan rambut.', 'medium', vis='Anak perempuan berambut hitam panjang tersenyum.')
    sq(p, 3, 'Teman bertanya, "What color are your eyes?" Mata Dina berwarna cokelat. Jawaban Dina ....', 'Ditanya warna matanya yang cokelat, Dina menjawab', 'My eyes are brown', ['My nose is brown', 'I have two eyes', 'My eyes are long'], 'Mendeskripsikan mata.', 'medium')
    for e in ['eyes', 'nose', 'mouth', 'ears', 'hair']:
        p.perf(1, f'Tunjuk {e} pada wajahmu dan ucapkan "This is my {e.rstrip("s") if e!="hair" else e}" dengan jelas!', R, 'Murid menunjuk dan mengucapkan dengan benar.', 'medium', 'menerapkan', 'Praktik berbicara')
    for cmd, _ in TCH[:6]:
        p.perf(2, f"Lakukan instruksi guru: '{cmd}'", R, 'Murid merespon dengan gerakan yang tepat.', 'medium', 'menerapkan', 'Merespon instruksi')
    for s, e in DESC[:6]:
        p.perf(3, f"Ucapkan '{e}' sambil menunjuk bagian wajahmu!", R, 'Murid mengucapkan dan menunjuk dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    for s, e in CNT[:6]:
        p.perf(4, f"Tunjuk {s} pada wajahmu lalu katakan '{e}'.", R, 'Murid menyebut jumlah dan nama dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    scr(p, 5, [e for _, e, _ in FACE] + ['eyes', 'ears', 'teeth', 'lips', 'face', 'head'], 'Menulis kosakata wajah', 'w3', 3)
    sent(p, 5, [('I have two eyes.', 'aku punya dua mata'), ('This is my nose.', 'ini hidungku'), ('My hair is black.', 'rambutku hitam'), ('I have one mouth.', 'aku punya satu mulut'), ('I have two ears.', 'aku punya dua telinga'),
                ('My eyes are brown.', 'mataku cokelat'), ('Touch your nose.', 'sentuh hidungmu'), ('My hair is long.', 'rambutku panjang')], 'Menulis frase wajah', 's3', 3)
    p.group(1, 'Kelompokkan: eyes; ears; nose; mouth; tongue; hair menurut bagian yang ada di dalam mulut atau di luar mulut.', {'di dalam mulut': ['tongue'], 'di luar mulut': ['eyes', 'ears', 'nose', 'mouth', 'hair']}, 'Lidah di dalam mulut.', 'medium', 'mengelompokkan', c)
    p.group(4, 'Kelompokkan bagian wajah berikut menurut jumlahnya: two eyes; one nose; two ears; one mouth; two cheeks; one chin.', {'dua (two)': ['two eyes', 'two ears', 'two cheeks'], 'satu (one)': ['one nose', 'one mouth', 'one chin']}, 'Dua dan satu.', 'medium', 'mengelompokkan', 'Menyebut nama dan jumlah')
    p.order(2, 'Urutkan instruksi berikut: sentuh hidung, lalu sentuh mata, lalu sentuh telinga, lalu sentuh mulut!', ['Touch your nose.', 'Touch your eyes.', 'Touch your ears.', 'Touch your mouth.'], 'Urutan instruksi.', 'medium', 'mengurutkan', 'Merespon instruksi')
