# -*- coding: utf-8 -*-
from en_gen import *
from en_common import COLOR

OBJ = [('buku', 'book', 'sebuah buku'), ('pensil', 'pencil', 'sebuah pensil'), ('pulpen', 'pen', 'sebuah pulpen'), ('penghapus', 'eraser', 'sebuah penghapus'), ('penggaris', 'ruler', 'sebuah penggaris'),
       ('tas', 'bag', 'sebuah tas sekolah'), ('meja', 'table', 'sebuah meja'), ('kursi', 'chair', 'sebuah kursi'), ('papan tulis', 'board', 'sebuah papan tulis'), ('pintu', 'door', 'sebuah pintu kelas'),
       ('jendela', 'window', 'sebuah jendela kelas'), ('kapur', 'chalk', 'sebatang kapur'), ('gunting', 'scissors', 'sebuah gunting'), ('krayon', 'crayon', 'sebatang krayon')]
FUNC = [('menulis dengan tinta', 'pen'), ('menghapus tulisan pensil', 'eraser'), ('mengukur dan menarik garis lurus', 'ruler'), ('membawa buku ke sekolah', 'bag'), ('duduk di kelas', 'chair'),
        ('memotong kertas', 'scissors'), ('menulis di papan tulis hitam', 'chalk'), ('membaca cerita', 'book'), ('menulis dengan grafit', 'pencil'), ('masuk ke dalam kelas', 'door'),
        ('mewarnai gambar', 'crayon'), ('meletakkan buku di depan kita', 'table')]
CMD = [('Show me your pencil.', 'menunjukkan pensilmu'), ('Point to the door.', 'menunjuk pintu'), ('Give me the book.', 'memberikan buku'), ('Open the window.', 'membuka jendela'),
       ('Put the pen in the bag.', 'memasukkan pulpen ke dalam tas'), ('Take your ruler.', 'mengambil penggarismu'), ('Pick up the eraser.', 'mengambil penghapus'),
       ('Touch the table.', 'menyentuh meja'), ('Look at the board.', 'melihat papan tulis'), ('Close the door.', 'menutup pintu')]
OC = [('book', 'red', 'sebuah buku berwarna merah'), ('pencil', 'yellow', 'sebuah pensil berwarna kuning'), ('bag', 'blue', 'sebuah tas berwarna biru'), ('ruler', 'green', 'sebuah penggaris berwarna hijau'),
      ('eraser', 'white', 'sebuah penghapus berwarna putih'), ('pen', 'black', 'sebuah pulpen berwarna hitam'), ('chair', 'brown', 'sebuah kursi berwarna cokelat'), ('crayon', 'orange', 'sebatang krayon berwarna oranye'),
      ('notebook', 'purple', 'sebuah buku tulis berwarna ungu'), ('bottle', 'pink', 'sebuah botol minum berwarna merah muda')]


def b2(p):
    c = 'Mengenal benda di dalam kelas'
    kv(p, 3, [(i, e) for i, e, _ in OBJ], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'ob', 1)
    kv(p, 3, FUNC, "Benda yang dipakai untuk {k} adalah '{v}'.", "'{v}' dipakai untuk ....", c, 'fn', 2)
    kv(p, 4, CMD, "Guru berkata '{k}' Artinya kamu harus {v}.", "Guru ingin kamu {v}. Instruksi yang diucapkan adalah ....", 'Merespon instruksi', 'cm', 3)
    kv(p, 5, COLOR, "Warna {k} dalam Bahasa Inggris adalah '{v}'.", "Kata '{v}' berarti warna ....", 'Mengenal warna', 'co', 4)
    vis(p, 3, [(e, d) for _, e, d in OBJ], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris benda itu disebut ....', c, 'vo', pool=['bottle', 'shelf'])
    vis(p, 5, [(en, f'gambar benda berwarna {idn}') for idn, en in COLOR], 'Perhatikan gambar! Gambar menunjukkan {d}. Warna itu dalam Bahasa Inggris adalah ....', 'Mengenal warna', 'vc')
    vis(p, 6, [(f'a {c_} {o}', d) for o, c_, d in OC], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris disebut ....', 'Menyebut nama dan warna benda', 'vn', pool=['a red pencil', 'a blue book'])
    kv(p, 7, [(d_, f'a {c_} {o}') for o, c_, d_ in OC], "Dalam Bahasa Inggris, {k} disebut '{v}'.", "'{v}' artinya ....", 'Mengungkapkan nama dan warna', 'nc', 5)
    kv(p, 6, [(d_, col) for o, col, d_ in OC], "Terdapat {k}. Warnanya dalam Bahasa Inggris adalah '{v}'.", "Benda berwarna '{v}' adalah ....", 'Menyebut nama dan warna benda', 'oc', 6, match=False)
    kv(p, 6, [(f'a {col} {o}', d_) for o, col, d_ in OC], "'{k}' artinya {v}.", "{v} dalam Bahasa Inggris adalah '....'", 'Menyebut nama dan warna benda', 'oe', 7, match=False)
    for q in ['Tunjuk sebuah benda di kelas dengan jari lalu angguk-angguk untuk menjawab "Is this a book?"', 'Tanyakan "What is this?" dengan menunjuk benda, lalu dengarkan jawaban temanmu!',
              'Gunakan gerakan tubuh untuk menjawab "Is this a pencil?" saat guru menunjuk sebuah pensil!', 'Tunjuk benda-benda di kelas sambil berkata "This is a ..." bergantian dengan temanmu!']:
        p.perf(1, q, R, 'Murid bertanya dan menjawab dengan gerakan.', 'medium', 'menerapkan', 'Praktik bertanya dan menjawab')
    for idn, en, d in OBJ:
        sq(p, 2, f'Guru menunjuk {d} dan bertanya, "What is this?" Jawaban yang tepat adalah ....', f'Ditanya "What is this?" tentang {d}, murid menjawab', f'It is a {en}' if en[0] not in 'aeiou' else f'It is an {en}',
           [f'It is a {w}' for w in ['cat', 'house', 'apple', 'dog', 'car'] if w != en][:3], f'{en} = {idn}.', 'easy')
    for o, col, d in OC:
        sq(p, 7, f'Guru menunjuk {d} dan bertanya, "What color is it?" Jawaban yang tepat adalah ....', f'Ditanya "What color is it?" tentang {d}, murid menjawab', f'It is {col}',
           [f'It is {w}' for w in ['red', 'blue', 'green', 'yellow', 'black', 'white'] if w != col][:3], f'{col} = warna.', 'easy', comp='Mengungkapkan warna benda')
    sq(p, 1, 'Guru menunjuk sebuah buku dan mengangkat alis seperti bertanya. Gerakan tubuh yang tepat untuk menjawab adalah ....', 'Untuk menjawab pertanyaan tentang bendanya dengan gerakan, murid', 'menunjuk benda itu dan mengangguk', ['menutup mata', 'berlari keluar', 'menggeleng terus'], 'Menjawab dengan gerakan.', 'easy')
    sq(p, 1, 'Kamu ingin bertanya "What is this?" tanpa suara sambil menunjuk benda. Gerakan yang tepat adalah ....', 'Bertanya tanpa suara tentang sebuah benda dilakukan dengan', 'menunjuk benda dengan wajah bertanya', ['menepuk meja', 'menutup telinga', 'memalingkan wajah'], 'Bertanya dengan gerakan.', 'medium')
    sq(p, 1, 'Teman menunjuk pintu, lalu mengangguk saat kamu mengangkat pintu. Kamu sedang menjawab "Is this a door?" dengan gerakan ....', 'Menjawab "Is this a door?" dengan anggukan berarti', '"Yes, it is a door"', ['"No, it is not"', '"Goodbye"', '"I am sad"'], 'Mengangguk = ya.', 'medium')
    tfs(p, 1, [('Mengangguk berarti menjawab "Yes".', True, 'Anggukan = ya.'), ('Menggeleng berarti menjawab "Yes".', False, 'Gelengan = no.')])
    for en in ['book', 'pencil', 'ruler', 'chair', 'eraser', 'bag']:
        p.perf(2, f"Tunjuk {en} di kelas lalu ucapkan namanya dengan jelas dalam Bahasa Inggris!", R, 'Murid mengucapkan dengan jelas.', 'medium', 'menerapkan', 'Praktik berbicara')
    for cmd, _ in CMD[:6]:
        p.perf(4, f"Lakukan instruksi guru: '{cmd}'", R, 'Murid merespon dengan tepat.', 'medium', 'menerapkan', 'Merespon instruksi')
    for o, col, _ in OC[:6]:
        p.perf(7, f"Ambil {col} {o} lalu katakan, 'It is a {col} {o}.'", R, 'Murid menyebut nama dan warna.', 'medium', 'menerapkan', 'Praktik berbicara')
    scr(p, 8, [e for _, e, _ in OBJ] + [e for _, e in COLOR], 'Menulis kosakata kelas', 'w2', 2)
    sent(p, 8, [('It is a red book.', 'ini buku merah'), ('It is a yellow pencil.', 'ini pensil kuning'), ('It is a blue bag.', 'ini tas biru'), ('It is a green ruler.', 'ini penggaris hijau'),
                ('It is a white eraser.', 'ini penghapus putih'), ('It is a black pen.', 'ini pulpen hitam'), ('It is a brown chair.', 'ini kursi cokelat'), ('It is an orange crayon.', 'ini krayon oranye')], 'Menulis frase benda', 's2', 2)
    sent(p, 8, [('I have a red pencil.', 'aku punya pensil merah'), ('This is my bag.', 'ini tasku'), ('Open the door.', 'bukalah pintunya'), ('Point to the window.', 'tunjuk jendelanya'), ('The board is black.', 'papan tulisnya hitam'), ('Give me the ruler.', 'berikan penggaris')], 'Menulis kalimat sederhana', 's3', 3)
    p.group(3, 'Kelompokkan benda berikut: pen; chair; pencil; table; ruler; door.', {'alat tulis': ['pen', 'pencil', 'ruler'], 'perabot dan bagian ruangan': ['chair', 'table', 'door']}, 'Alat tulis dan perabot.', 'medium', 'mengelompokkan', c)
    p.group(6, 'Kelompokkan: red book; blue bag; green ruler; black pen; yellow pencil; white eraser menurut warnanya yang sama dengan benda dalam daftar.', {'warna terang': ['yellow pencil', 'white eraser', 'red book'], 'warna lain': ['blue bag', 'green ruler', 'black pen']}, 'Mengelompokkan.', 'medium', 'mengelompokkan', 'Menyebut nama dan warna benda')
    p.order(4, 'Urutkan instruksi guru berikut agar menjadi kegiatan membuka tas!', ['Take your bag.', 'Open your bag.', 'Take your book.', 'Close your bag.'], 'Urutan kegiatan.', 'medium', 'mengurutkan', 'Merespon instruksi')
