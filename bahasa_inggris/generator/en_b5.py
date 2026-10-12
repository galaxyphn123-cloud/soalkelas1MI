# -*- coding: utf-8 -*-
from en_gen import *
from en_common import COLOR

ROOM = [('ruang tamu', 'living room', 'ruang dengan sofa untuk menerima tamu'), ('kamar tidur', 'bedroom', 'kamar dengan tempat tidur dan bantal'), ('dapur', 'kitchen', 'ruang dengan kompor dan lemari piring'),
        ('kamar mandi', 'bathroom', 'ruang dengan bak mandi dan gayung'), ('ruang makan', 'dining room', 'ruang dengan meja makan dan kursi'), ('taman', 'garden', 'halaman rumah dengan bunga dan rumput'),
        ('garasi', 'garage', 'ruang tempat mobil diparkir'), ('halaman', 'yard', 'tanah terbuka di depan rumah')]
ACT = [('memasak', 'kitchen'), ('tidur', 'bedroom'), ('mandi', 'bathroom'), ('makan bersama', 'dining room'), ('menerima tamu', 'living room'), ('menanam bunga', 'garden'), ('memarkir mobil', 'garage')]
POS = [('Ibu ada di dapur', 'Mother is in the kitchen.'), ('Ayah ada di garasi', 'Father is in the garage.'), ('Kakak ada di kamar tidur', 'My sister is in the bedroom.'),
       ('Nenek ada di ruang tamu', 'Grandmother is in the living room.'), ('Adik ada di kamar mandi', 'My brother is in the bathroom.'), ('Kakek ada di taman', 'Grandfather is in the garden.'),
       ('Kami ada di ruang makan', 'We are in the dining room.')]
COL = [('Color the door brown.', 'brown'), ('Color the roof red.', 'red'), ('Color the window blue.', 'blue'), ('Color the sun yellow.', 'yellow'), ('Color the grass green.', 'green'),
       ('Color the wall white.', 'white'), ('Color the circle orange.', 'orange'), ('Color the square pink.', 'pink'), ('Color the triangle purple.', 'purple'), ('Color the chimney black.', 'black')]
SHC = [('triangle', 'red', 'sebuah segitiga berwarna merah'), ('rectangle', 'blue', 'sebuah persegi panjang berwarna biru'), ('circle', 'yellow', 'sebuah lingkaran berwarna kuning'),
       ('square', 'green', 'sebuah persegi berwarna hijau'), ('triangle', 'orange', 'sebuah segitiga berwarna oranye'), ('rectangle', 'brown', 'sebuah persegi panjang berwarna cokelat'),
       ('circle', 'white', 'sebuah lingkaran berwarna putih'), ('square', 'purple', 'sebuah persegi berwarna ungu')]
DESCR = [('Dapurku bersih', 'The kitchen is clean.'), ('Kamar tidurku berwarna biru', 'My bedroom is blue.'), ('Ruang tamuku besar', 'The living room is big.'), ('Tamanku indah', 'My garden is beautiful.'),
         ('Kamar mandiku kecil', 'My bathroom is small.'), ('Ruang makanku berwarna kuning', 'My dining room is yellow.'), ('Garasi kami luas', 'Our garage is wide.'), ('Rumahku berwarna putih', 'My house is white.')]


def b5(p):
    c = 'Mengenal ruangan di dalam rumah'
    kv(p, 1, [(i, e) for i, e, _ in ROOM], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'rm', 1)
    kv(p, 2, [(d, e) for _, e, d in ROOM], "Ruangan yang berupa {k} disebut '{v}'.", "'{v}' adalah ....", c, 'rd', 2)
    kv(p, 2, ACT, "Kegiatan {k} dilakukan di '{v}'.", "Di '{v}' kita biasanya ....", c, 'ac', 3)
    vis(p, 2, [(e, f'gambar {d}') for _, e, d in ROOM], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris ruangan itu disebut ....', c, 'vr', pool=['classroom', 'library'])
    kv(p, 3, COLOR, "Kata Bahasa Inggris untuk warna {k} adalah '{v}'.", "Kata '{v}' dipakai untuk warna ....", 'Mengenal warna', 'cl', 4, match=False)
    vis(p, 3, [(en, f'sebuah krayon berwarna {idn}') for idn, en in COLOR], 'Perhatikan gambar! Gambar menunjukkan {d}. Warnanya dalam Bahasa Inggris adalah ....', 'Mengenal warna', 'vl')
    kv(p, 4, [('lingkaran', 'circle'), ('persegi', 'square'), ('segitiga', 'triangle'), ('persegi panjang', 'rectangle')], "Bentuk {k} dalam Bahasa Inggris adalah '{v}'.", "'{v}' adalah bentuk ....", 'Mengenal bangun datar', 'sp', 5, match=False)
    vis(p, 4, [(f'{col} {sh}', d_) for sh, col, d_ in SHC], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris disebut ....', 'Bangun datar dan warnanya', 'vs', pool=['red circle', 'blue square'])
    kv(p, 4, [(d_, f'{col} {sh}') for sh, col, d_ in SHC], "Dalam Bahasa Inggris, {k} disebut '{v}'.", "'{v}' artinya ....", 'Bangun datar dan warnanya', 'sc', 6)
    kv(p, 5, COL, "Guru berkata, '{k}' Warna yang harus dipakai adalah '{v}'.", "Warna '{v}' dipakai ketika guru berkata ....", 'Mewarnai sesuai instruksi', 'cc', 7, match=False)
    kv(p, 6, POS, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Posisi anggota keluarga di rumah', 'ps', 8)
    kv(p, 8, DESCR, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Mendeskripsikan ruangan', 'ds', 9)
    scr(p, 7, [e for _, e, _ in ROOM if ' ' not in e] + ['house', 'color', 'circle', 'square', 'triangle', 'red', 'blue', 'green'], 'Menulis kosakata', 'w5', 5)
    sent(p, 7, [('The kitchen is white.', 'dapurnya putih'), ('My bedroom is blue.', 'kamar tidurku biru'), ('The door is brown.', 'pintunya cokelat'), ('It is a red triangle.', 'itu segitiga merah'),
                ('It is a blue rectangle.', 'itu persegi panjang biru'), ('The garden is green.', 'tamannya hijau'), ('The bathroom is yellow.', 'kamar mandinya kuning'), ('It is a green square.', 'itu persegi hijau')], 'Menulis frase warna dan bentuk', 's5', 5)
    sent(p, 6, [('Mother is in the kitchen.', 'ibu ada di dapur'), ('Father is in the garage.', 'ayah ada di garasi'), ('I am in the bedroom.', 'aku ada di kamar tidur'), ('We are in the garden.', 'kami ada di taman'),
                ('Sister is in the bathroom.', 'kakak ada di kamar mandi')], 'Posisi di rumah', 's5b', 6)
    sent(p, 8, [('This is my house.', 'ini rumahku'), ('My house has three bedrooms.', 'rumahku punya tiga kamar tidur'), ('The living room is big.', 'ruang tamunya besar'), ('I like my garden.', 'aku suka tamanku')], 'Mendeskripsikan rumah', 's5c', 7)
    for who, room, e in [('Mother', 'kitchen', 'ibu'), ('Father', 'garage', 'ayah'), ('Sister', 'bedroom', 'kakak perempuan'), ('Grandfather', 'garden', 'kakek'), ('Brother', 'bathroom', 'kakak laki-laki'), ('Grandmother', 'living room', 'nenek')]:
        sq(p, 6, f'Perhatikan gambar! {e.capitalize()} sedang berada di {dict((b, a) for a, b, _ in ROOM)[room]}. Kalimat yang tepat adalah ....', f'Gambar {e} di {dict((b, a) for a, b, _ in ROOM)[room]} dijelaskan dengan', f'{who} is in the {room}',
           [f'{who} is in the {r}' for r in ['kitchen', 'bedroom', 'garage', 'garden', 'bathroom'] if r != room][:3], f'In the {room}.', 'medium', vis=f'{e.capitalize()} berada di {dict((b, a) for a, b, _ in ROOM)[room]} di dalam rumah.', comp='Posisi anggota keluarga di rumah')
    for i, e, d in ROOM[:6]:
        sq(p, 1, f'Ibu bertanya, "Where is the {e}?" Kamu menunjuk {i}. Itu artinya kamu tahu bahwa {e} adalah ....', f'Ketika menunjuk {i} untuk menjawab "Where is the {e}?", berarti {e} adalah', i, [x for x in ['kamar tidur', 'dapur', 'taman', 'garasi', 'ruang tamu', 'kamar mandi'] if x != i][:3], f'{e} = {i}.', 'easy', comp=c)
    for sh, col, d_ in SHC[:4]:
        p.perf(4, f'Gambar {sh} lalu warnai {col}, dan ucapkan "a {col} {sh}"!', R, 'Murid menggambar, mewarnai, dan menyebut.', 'medium', 'menerapkan', 'Praktik bangun datar')
    for cmd, v in COL[:6]:
        p.perf(5, f"Lakukan instruksi guru pada kertas bergambar rumahmu: '{cmd}'", R, 'Murid mewarnai sesuai instruksi.', 'medium', 'menerapkan', 'Mewarnai sesuai instruksi')
    for s, e in DESCR[:5]:
        p.perf(8, f"Tunjuk ruangan di gambar rumah dan ucapkan '{e}'", R, 'Murid mendeskripsikan dengan jelas.', 'medium', 'menerapkan', 'Praktik berbicara')
    for i, e, d in ROOM[:4]:
        p.perf(2, f"Tunjuk gambar '{e}' lalu ucapkan namanya dalam Bahasa Inggris!", R, 'Murid menyebutkan dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    p.group(2, 'Kelompokkan ruangan menurut tempatnya: kitchen; bedroom; garden; bathroom; garage; yard.', {'di dalam rumah': ['kitchen', 'bedroom', 'bathroom'], 'di luar rumah': ['garden', 'garage', 'yard']}, 'Dalam dan luar rumah.', 'medium', 'mengelompokkan', c)
    p.group(4, 'Kelompokkan: red circle; blue square; green triangle; yellow circle; purple square; orange triangle menurut bentuk.', {'circle': ['red circle', 'yellow circle'], 'square': ['blue square', 'purple square'], 'triangle': ['green triangle', 'orange triangle']}, 'Menurut bentuk.', 'medium', 'mengelompokkan', 'Bangun datar dan warnanya')
    p.order(5, 'Urutkan langkah mewarnai berikut: ambil krayon, dengar instruksi, warnai gambar, simpan krayon!', ['Listen to the teacher.', 'Take the crayon.', 'Color the picture.', 'Put the crayon away.'], 'Urutan mewarnai.', 'medium', 'mengurutkan', 'Mewarnai sesuai instruksi')
