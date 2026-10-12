# -*- coding: utf-8 -*-
from en_gen import *
from en_common import NUMS, COLOR

FAM = [('ayah', 'father', 'seorang ayah berdasi'), ('ibu', 'mother', 'seorang ibu berkerudung yang tersenyum'), ('kakak laki-laki atau adik laki-laki', 'brother', 'seorang anak laki-laki bersama saudaranya'),
       ('kakak perempuan atau adik perempuan', 'sister', 'seorang anak perempuan bersama saudarinya'), ('kakek', 'grandfather', 'seorang kakek berambut putih dengan tongkat'),
       ('nenek', 'grandmother', 'seorang nenek berambut putih berkacamata'), ('paman', 'uncle', 'seorang paman yang bermain dengan keponakannya'), ('bibi', 'aunt', 'seorang bibi yang membawa bingkisan'),
       ('bayi', 'baby', 'seorang bayi di dalam boks'), ('keluarga', 'family', 'sebuah keluarga yang terdiri atas ayah, ibu, dan anak-anak')]
SHAPEOBJ = [('uang koin', 'circle'), ('piring', 'circle'), ('roda', 'circle'), ('jam dinding bulat', 'circle'), ('bola kaki dilihat dari depan', 'circle'),
            ('sapu tangan', 'square'), ('ubin lantai', 'square'), ('kotak kado berbentuk kubus dilihat dari depan', 'square'), ('papan catur', 'square'), ('roti tawar', 'square')]
CS = [('red', 'circle', 'sebuah lingkaran berwarna merah'), ('blue', 'square', 'sebuah persegi berwarna biru'), ('yellow', 'circle', 'sebuah lingkaran berwarna kuning'),
      ('green', 'square', 'sebuah persegi berwarna hijau'), ('black', 'circle', 'sebuah lingkaran berwarna hitam'), ('orange', 'square', 'sebuah persegi berwarna oranye'),
      ('purple', 'circle', 'sebuah lingkaran berwarna ungu'), ('pink', 'square', 'sebuah persegi berwarna merah muda')]
TELL = [('Ini ayahku', 'This is my father.'), ('Ini ibuku', 'This is my mother.'), ('Aku punya dua saudara laki-laki', 'I have two brothers.'), ('Aku punya satu saudara perempuan', 'I have one sister.'),
        ('Dia kakekku', 'He is my grandfather.'), ('Dia nenekku', 'She is my grandmother.'), ('Ibuku baik hati', 'My mother is kind.'), ('Ayahku tinggi', 'My father is tall.'),
        ('Keluargaku bahagia', 'My family is happy.'), ('Ada empat orang di keluargaku', 'There are four people in my family.')]


def b4(p):
    c = 'Mengenal anggota keluarga'
    kv(p, 1, [(i, e) for i, e, _ in FAM], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'fm', 1)
    vis(p, 1, [(e, d) for _, e, d in FAM], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris disebut ....', c, 'vf', pool=['teacher', 'friend'])
    kv(p, 3, TELL, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Menceritakan keluarga', 'tl', 2)
    kv(p, 4, SHAPEOBJ, "Bentuk {k} adalah '{v}'.", None, 'Mengenal bentuk', 'so', 3, extra_wrong=['triangle', 'rectangle'])
    kv(p, 4, [('lingkaran', 'circle'), ('persegi', 'square'), ('segitiga', 'triangle'), ('persegi panjang', 'rectangle')], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "'{v}' berarti ....", 'Mengenal bentuk', 'sh', 4, match=False)
    vis(p, 4, [(sh, f'{d_.split(" berwarna")[0]}') for col, sh, d_ in CS], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris bentuknya disebut ....', 'Mengenal bentuk', 'vs', pool=['triangle', 'rectangle'])
    vis(p, 5, [(col, d_) for col, sh, d_ in CS], 'Perhatikan gambar! Gambar menunjukkan {d}. Warna bentuk itu dalam Bahasa Inggris adalah ....', 'Warna pada bentuk', 'vc')
    kv(p, 5, [(d_, f'{col} {sh}') for col, sh, d_ in CS], "Dalam Bahasa Inggris, {k} disebut '{v}'.", "'{v}' artinya ....", 'Warna pada bentuk', 'cs', 5)
    kv(p, 6, NUMS, "Angka {k} dalam Bahasa Inggris adalah '{v}'.", "Kata '{v}' menunjukkan angka ....", 'Mengenal angka', 'nm', 6)
    count(p, 6, 'apple', 'apel', 'Terlihat {n} {noun}', 'Menghitung', 'ca')
    count(p, 6, 'ball', 'bola', 'Terlihat {n} {noun}', 'Menghitung', 'cb')
    count(p, 6, 'book', 'buku', 'Terlihat {n} {noun}', 'Menghitung', 'cc')
    scr(p, 7, [e for _, e, _ in FAM] + [e for _, e in NUMS] + ['circle', 'square', 'red', 'blue'], 'Menulis kosakata', 'w4', 4)
    sent(p, 7, [('I have two brothers.', 'aku punya dua saudara laki-laki'), ('There are four people in my family.', 'ada empat orang di keluargaku'), ('It is a red circle.', 'itu lingkaran merah'),
                ('This is a blue square.', 'ini persegi biru'), ('I have one sister.', 'aku punya satu saudara perempuan'), ('My father is tall.', 'ayahku tinggi'), ('It is a green square.', 'itu persegi hijau'),
                ('This is a yellow circle.', 'ini lingkaran kuning')], 'Menulis frase keluarga dan bentuk', 's4', 4)
    sent(p, 3, [('This is my mother.', 'ini ibuku'), ('He is my father.', 'dia ayahku'), ('She is my sister.', 'dia saudara perempuanku'), ('My family is happy.', 'keluargaku bahagia'), ('I love my family.', 'aku sayang keluargaku')], 'Menceritakan keluarga', 's4b', 5)
    for i, e, d in FAM[:8]:
        g = 'He' if e in ('father', 'brother', 'grandfather', 'uncle') else 'She'
        sq(p, 2, f'Guru menunjuk gambar {d} dan bertanya, "Who is this?" Jawaban yang tepat adalah ....', f'Ditanya "Who is this?" tentang {d}, murid menjawab',
           f'{g} is my {e}', [f'{g} is my {x}' for x in ['teacher', 'friend', 'doctor', 'driver'] if x != e][:3], f'{e} = {i}.', 'easy', comp='Menyebut anggota keluarga')
    for sh, (obj, shape) in zip(range(6), SHAPEOBJ[:6]):
        pass
    for i, e, d in FAM[:6]:
        p.perf(2, f"Tunjuk gambar anggota keluarga '{e}' lalu ucapkan namanya dengan jelas!", R, 'Murid mengucapkan dengan jelas.', 'medium', 'menerapkan', 'Praktik berbicara')
    for q in ['Ceritakan keluargamu dengan "This is my ..." sambil menunjuk foto keluargamu!', 'Sebutkan jumlah anggota keluargamu dalam Bahasa Inggris!', 'Perkenalkan ayah atau ibumu dengan "This is my ..."!']:
        p.perf(3, q, R, 'Murid bercerita dengan jelas.', 'medium', 'menerapkan', 'Praktik berbicara')
    for col, sh, d_ in CS[:4]:
        p.perf(4, f'Tunjuk benda berbentuk {sh} di kelas lalu ucapkan "{sh}"!', R, 'Murid menunjuk benda berbentuk yang tepat.', 'medium', 'menerapkan', 'Praktik mengenal bentuk')
        p.perf(5, f'Gambarlah {sh} lalu warnai {col}, lalu ucapkan "a {col} {sh}"!', R, 'Murid menggambar, mewarnai, dan menyebut.', 'medium', 'menerapkan', 'Praktik mewarnai bentuk')
    for e, d in [('one', 1), ('three', 3), ('five', 5), ('seven', 7)]:
        p.perf(6, f'Tepuk tangan sebanyak {d} kali sambil menghitung dalam Bahasa Inggris!', R, 'Murid menghitung dengan benar.', 'medium', 'menerapkan', 'Praktik menghitung')
    p.group(4, 'Kelompokkan benda berikut menurut bentuknya: coin; plate; tile; handkerchief; wheel; chessboard.', {'circle': ['coin', 'plate', 'wheel'], 'square': ['tile', 'handkerchief', 'chessboard']}, 'Lingkaran dan persegi.', 'medium', 'mengelompokkan', 'Mengenal bentuk')
    p.group(1, 'Kelompokkan anggota keluarga berikut: father; mother; brother; sister; grandfather; grandmother.', {'laki-laki': ['father', 'brother', 'grandfather'], 'perempuan': ['mother', 'sister', 'grandmother']}, 'Laki-laki dan perempuan.', 'medium', 'mengelompokkan', c)
    p.order(6, 'Urutkan angka berikut dari yang terkecil: three, one, five, two, four.', ['one', 'two', 'three', 'four', 'five'], 'Urutan angka.', 'medium', 'mengurutkan', 'Mengenal angka')
    p.order(6, 'Urutkan angka berikut dari yang terkecil: seven, six, ten, eight, nine.', ['six', 'seven', 'eight', 'nine', 'ten'], 'Urutan angka.', 'medium', 'mengurutkan', 'Mengenal angka')
    p.order(6, 'Urutkan angka berikut dari yang terbesar: two, four, one, three.', ['four', 'three', 'two', 'one'], 'Urutan menurun.', 'medium', 'mengurutkan', 'Mengenal angka')
