# -*- coding: utf-8 -*-
from en_gen import *
from en_common import COLOR

TOY = [('boneka', 'doll', 'sebuah boneka perempuan'), ('bola', 'ball', 'sebuah bola karet'), ('mobil-mobilan', 'toy car', 'sebuah mobil-mobilan kecil'), ('balok susun', 'blocks', 'tumpukan balok susun warna-warni'),
       ('layang-layang', 'kite', 'sebuah layang-layang di udara'), ('sepeda', 'bicycle', 'sebuah sepeda roda dua'), ('robot', 'robot', 'sebuah robot mainan'), ('kereta api mainan', 'train', 'sebuah kereta api mainan di atas rel'),
       ('boneka beruang', 'teddy bear', 'sebuah boneka beruang berbulu lembut'), ('puzzle', 'puzzle', 'sebuah puzzle yang belum selesai disusun')]
ACTS = [('melempar bola', 'Throw the ball.'), ('menendang bola', 'Kick the ball.'), ('mendorong mobil-mobilan', 'Push the toy car.'), ('menyusun balok', 'Build the blocks.'),
        ('menerbangkan layang-layang', 'Fly the kite.'), ('memeluk boneka', 'Hug the doll.'), ('menaiki sepeda', 'Ride the bicycle.'), ('merapikan mainan', 'Put away the toys.'),
        ('berbagi mainan', 'Share the toys.'), ('memainkan puzzle', 'Play with the puzzle.')]
TCOL = [('doll', 'pink', 'sebuah boneka berbaju merah muda'), ('ball', 'red', 'sebuah bola berwarna merah'), ('toy car', 'blue', 'sebuah mobil-mobilan berwarna biru'), ('kite', 'yellow', 'sebuah layang-layang berwarna kuning'),
        ('robot', 'black', 'sebuah robot berwarna hitam'), ('train', 'green', 'sebuah kereta mainan berwarna hijau'), ('teddy bear', 'brown', 'sebuah boneka beruang berwarna cokelat'), ('bicycle', 'orange', 'sebuah sepeda berwarna oranye')]
SIZE = [('big', 'besar'), ('small', 'kecil'), ('long', 'panjang'), ('short', 'pendek'), ('tall', 'tinggi')]
SZ = [('a big ball', 'sebuah bola besar'), ('a small car', 'sebuah mobil kecil'), ('a long train', 'sebuah kereta panjang'), ('a short rope', 'sebuah tali pendek'), ('a tall robot', 'sebuah robot tinggi'),
      ('a big teddy bear', 'sebuah boneka beruang besar'), ('a small doll', 'sebuah boneka kecil'), ('a long kite', 'sebuah layang-layang panjang')]
ASK = [('meminta izin meminjam boneka temanmu', 'May I play with your doll?'), ('mengizinkan temanmu meminjam mainanmu', 'Yes, you may.'), ('menolak dengan sopan karena mainan sedang dipakai', 'Sorry, I am using it.'),
       ('berterima kasih setelah meminjam mainan', 'Thank you.'), ('menjawab ucapan terima kasih', 'You are welcome.'), ('meminta izin meminjam bola temanmu', 'May I play with your ball?'),
       ('mengembalikan mainan sambil memberikannya', 'Here you are.'), ('mengajak teman bermain bersama', 'Let us play together.')]
FAV = [('Mainan kesukaanku boneka', 'My favorite toy is a doll.'), ('Aku suka bola', 'I like the ball.'), ('Mobil-mobilanku berwarna biru', 'My toy car is blue.'), ('Bonekaku kecil', 'My doll is small.'),
       ('Aku bermain dengan robotku', 'I play with my robot.'), ('Layang-layangku panjang', 'My kite is long.'), ('Aku suka bermain bersama temanku', 'I like to play with my friend.'), ('Mainan kesukaanku sepeda', 'My favorite toy is a bicycle.')]


def b7(p):
    c = 'Mengenal mainan'
    kv(p, 1, [(i, e) for i, e, _ in TOY], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'ty', 1)
    vis(p, 2, [(e, d) for _, e, d in TOY], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris mainan itu disebut ....', c, 'vt', pool=['book', 'pencil'])
    kv(p, 3, [(d, f'{col} {t}') for t, col, d in TCOL], "Dalam Bahasa Inggris, {k} disebut '{v}'.", "'{v}' artinya ....", 'Mewarnai dan mendeskripsikan mainan', 'tc', 2)
    kv(p, 4, ACTS, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Instruksi '{v}' artinya ....", 'Tindakan terhadap mainan', 'ac', 3)
    kv(p, 5, ASK, "Untuk {k}, kamu berkata '{v}'", "Ungkapan '{v}' dipakai untuk ....", 'Meminta izin meminjam mainan', 'as', 4)
    kv(p, 6, [(d, col) for t, col, d in TCOL], "Terdapat {k}. Warnanya dalam Bahasa Inggris adalah '{v}'.", None, 'Warna mainan', 'tw', 5, match=False)
    vis(p, 6, [(col, d) for t, col, d in TCOL], 'Perhatikan gambar! Gambar menunjukkan {d}. Warnanya dalam Bahasa Inggris adalah ....', 'Warna mainan', 'vc')
    count(p, 7, 'doll', 'boneka', 'Terlihat {n} {noun} di rak', 'Menghitung mainan', 'cd')
    count(p, 7, 'ball', 'bola', 'Terlihat {n} {noun} di lantai', 'Menghitung mainan', 'cb')
    count(p, 7, 'car', 'mobil mainan', 'Terlihat {n} {noun} berjajar', 'Menghitung mainan', 'cr')
    kv(p, 8, SIZE, "Kata '{k}' berarti ukuran {v}.", "Mainan yang {v} dalam Bahasa Inggris disebut '....'.", 'Ukuran mainan', 'sz', 6, match=False)
    kv(p, 8, SZ, "Dalam Bahasa Inggris, '{k}' artinya {v}.", "{v} dalam Bahasa Inggris adalah '....'", 'Ukuran mainan', 'sm', 7)
    kv(p, 10, FAV, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Menceritakan mainan kesukaan', 'fv', 8)
    scr(p, 9, [e for _, e, _ in TOY if ' ' not in e] + ['big', 'small', 'long', 'short', 'tall', 'play', 'share'], 'Menulis kosakata', 'w7', 7)
    sent(p, 9, [('It is a big ball.', 'itu bola besar'), ('It is a small doll.', 'itu boneka kecil'), ('I have a long kite.', 'aku punya layang-layang panjang'), ('It is a tall robot.', 'itu robot tinggi'),
                ('It is a short rope.', 'itu tali pendek'), ('I have a big teddy bear.', 'aku punya boneka beruang besar'), ('The car is small.', 'mobilnya kecil'), ('The train is long.', 'keretanya panjang')], 'Menulis frase mainan dan ukuran', 's7', 7)
    sent(p, 10, [('My favorite toy is a doll.', 'mainan kesukaanku boneka'), ('I like my robot.', 'aku suka robotku'), ('My toy car is blue.', 'mobil-mobilanku biru'), ('I play with my friend.', 'aku bermain dengan temanku')], 'Menceritakan mainan', 's7b', 8)
    sent(p, 5, [('May I play with your doll?', 'bolehkah aku bermain dengan bonekamu'), ('Yes, you may.', 'ya, boleh'), ('Thank you very much.', 'terima kasih banyak'), ('May I play with your ball?', 'bolehkah aku bermain dengan bolamu')], 'Meminta izin', 's7c', 9)
    for t, col, d in TCOL[:6]:
        sq(p, 5, f'Kamu ingin meminjam {d} milik temanmu. Kamu berkata ....', f'Untuk meminjam {d} temannya, murid berkata', f'May I play with your {t}?',
           [f'Give me the {t} now!', f'I do not like the {t}', f'Goodbye, {t}'], 'Meminta izin dengan sopan.', 'easy', comp='Meminta izin meminjam mainan')
    sq(p, 5, 'Temanmu berkata, "May I play with your robot?" Kamu setuju. Kamu menjawab ....', 'Ditanya "May I play with your robot?" dan setuju, kamu menjawab', 'Yes, you may', ['No, goodbye', 'I am a robot', 'Good night'], 'Mengizinkan.', 'easy', comp='Meminta izin meminjam mainan')
    sq(p, 5, 'Temanmu berkata, "May I play with your ball?" Bolamu sedang dipakai. Kamu menjawab sopan ....', 'Jika bolanya sedang dipakai, kamu menjawab sopan', 'Sorry, I am using it', ['Go away', 'Yes, you must', 'I do not care'], 'Menolak dengan sopan.', 'medium', comp='Meminta izin meminjam mainan')
    sq(p, 5, 'Setelah selesai bermain dengan boneka temanmu, kamu mengembalikannya dan berkata ....', 'Setelah selesai meminjam boneka, kamu mengembalikan sambil berkata', 'Thank you', ['Good night', 'I am sorry, no', 'Stand up'], 'Terima kasih.', 'easy', comp='Meminta izin meminjam mainan')
    sq(p, 4, 'Guru memberi sebuah boneka kepada murid dan berkata, "Play nicely." Artinya ....', 'Perintah "Play nicely" artinya', 'bermainlah dengan baik', ['pecahkan mainannya', 'buang mainannya', 'jangan bermain'], 'Play nicely.', 'medium', comp='Tindakan terhadap mainan')
    for q in ["Bermain peran: pinjam mainan temanmu dengan berkata 'May I play with your doll?'", "Bermain peran: jawab temanmu dengan 'Yes, you may.' lalu berbagi mainan!", "Bermain peran: tolak dengan sopan dengan 'Sorry, I am using it.'", "Bermain peran: ucapkan 'Thank you' lalu 'You are welcome.' dengan temanmu!"]:
        p.perf(5, q, R, 'Murid bermain peran dengan sopan.', 'medium', 'menerapkan', 'Bermain peran')
    for t, col, d in TCOL[:5]:
        p.perf(3, f'Warnai gambar {t} dengan warna {col}, lalu katakan "It is a {col} {t}."', R, 'Murid mewarnai dan mendeskripsikan.', 'medium', 'menerapkan', 'Mewarnai dan mendeskripsikan')
    for cmd, _ in ACTS[:5]:
        p.perf(4, f"Peragakan perintah ini: '{cmd}'", R, 'Murid memeragakan dengan tepat.', 'medium', 'menerapkan', 'Tindakan terhadap mainan')
    for s, e in FAV[:4]:
        p.perf(10, f"Ceritakan mainan kesukaanmu dengan mengucapkan '{e}'", R, 'Murid bercerita singkat.', 'medium', 'menerapkan', 'Menceritakan mainan')
    for t, col, d in TCOL[:4]:
        p.perf(6, f'Ambil krayon {col} lalu tunjuk mainan berwarna {col} di kelas dan ucapkan "{col}"!', R, 'Murid menunjuk warna yang benar.', 'medium', 'menerapkan', 'Warna mainan')
    for a in ['big', 'small', 'long', 'short']:
        p.perf(8, f'Tunjuk mainan atau benda yang "{a}" di sekitarmu dan ucapkan "It is {a}."', R, 'Murid menunjuk dan menyebutkan.', 'medium', 'menerapkan', 'Ukuran mainan')
    for n in ['two', 'four', 'six']:
        p.perf(7, f'Hitung mainan yang disiapkan guru lalu katakan "I have {n} toys."', R, 'Murid menghitung dengan tepat.', 'medium', 'menerapkan', 'Menghitung mainan')
    for i, e, d in TOY[:4]:
        p.perf(2, f"Tunjuk mainan '{e}' lalu ucapkan namanya dalam Bahasa Inggris!", R, 'Murid menyebutkan dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    p.group(1, 'Kelompokkan mainan berikut menurut kegunaannya: ball; kite; doll; robot; teddy bear; bicycle.', {'dimainkan di luar ruangan': ['ball', 'kite', 'bicycle'], 'dimainkan di dalam ruangan': ['doll', 'robot', 'teddy bear']}, 'Di luar atau di dalam.', 'medium', 'mengelompokkan', c)
    p.group(8, 'Kelompokkan ukuran berikut: big; tall; small; short; long; tiny.', {'bertambah (besar)': ['big', 'tall', 'long'], 'berkurang (kecil)': ['small', 'short', 'tiny']}, 'Ukuran besar dan kecil.', 'medium', 'mengelompokkan', 'Ukuran mainan')
    p.order(5, 'Urutkan percakapan meminjam mainan berikut!', ['May I play with your doll?', 'Yes, you may.', 'Thank you.', 'You are welcome.'], 'Urutan percakapan.', 'medium', 'mengurutkan', 'Meminta izin meminjam mainan')
    p.order(4, 'Urutkan kegiatan bermain balok berikut: ambil balok, susun balok, rapikan balok!', ['Take the blocks.', 'Build the blocks.', 'Put away the blocks.'], 'Urutan bermain.', 'medium', 'mengurutkan', 'Tindakan terhadap mainan')
