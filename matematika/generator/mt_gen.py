# -*- coding: utf-8 -*-
"""Pembangkit soal Matematika Kelas 1: kunci dihitung oleh program."""
import random, itertools

R = 'Dinilai guru: ketepatan hasil, cara menghitung, dan sikap (skala 1-4).'
KATA = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas', 'dua belas', 'tiga belas',
        'empat belas', 'lima belas', 'enam belas', 'tujuh belas', 'delapan belas', 'sembilan belas', 'dua puluh']
NAMA = ['Dina', 'Rafi', 'Salma', 'Fikri', 'Nisa', 'Hasan', 'Lani', 'Bima', 'Aisyah', 'Zaki', 'Mira', 'Dani', 'Hana', 'Umar', 'Putri', 'Alif']
OBJ = ['apel', 'jeruk', 'buku', 'pensil', 'kelereng', 'kue', 'bunga', 'permen', 'ikan', 'bola', 'topi', 'kursi', 'telur', 'mangga', 'pisang', 'balon']
OBJD = {o: f'{o} berwarna cerah' for o in OBJ}


def opts(correct, lo, hi, k=3, rng=None):
    pool = [x for x in range(max(lo, correct - 4), min(hi, correct + 4) + 1) if x != correct]
    rng = rng or random.Random(correct)
    if len(pool) < k:
        pool += [x for x in range(lo, hi + 1) if x != correct and x not in pool]
    rng.shuffle(pool)
    return [str(x) for x in pool[:k]]


def count_read(p, tp, lo, hi, seed=0):
    comp = f'Menghitung, membaca, dan menulis bilangan {lo}-{hi}'
    rng = random.Random(seed)
    for n in range(lo, hi + 1):
        p.gk = f'cr{n}'
        w = KATA[n]
        others = [KATA[x] for x in range(max(0, n - 4), min(20, n + 4) + 1) if x != n]
        p.mc(tp, f'Lambang bilangan {n} dibaca ....', w, others, f'{n} dibaca {w}.', 'easy', 'mengenali', comp)
        p.mc(tp, f'Kata bilangan "{w}" dilambangkan dengan angka ....', str(n), opts(n, 0, 20, 3, rng), f'{w} ditulis {n}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Lambang bilangan {n} dibaca {w}.', True, f'Benar, {n} = {w}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Lambang bilangan {n} dibaca {others[n % len(others)]}.', False, f'Salah, {n} = {w}.', 'easy', 'mengenali', comp)
        p.fill(tp, f'Isilah: Kata bilangan "{w}" dilambangkan dengan angka ....', str(n), f'{w} = {n}.', 'easy', 'mengenali', comp)
        o = OBJ[n % len(OBJ)]
        p.mc(tp, f'Perhatikan gambar kartu hitung nomor {n}! Berapa banyak {o} pada gambar?', str(n), opts(n, 0, 20, 3, rng), f'Pada gambar ada {n} {o}.', 'easy', 'menerapkan', comp,
             visual=f'Kartu hitung menampilkan {n} {OBJD[o]} tersusun rapi dalam baris-baris kecil.')
        if n < 20:
            p.mc(tp, f'Bilangan setelah {n} adalah ....', str(n + 1), opts(n + 1, 0, 20, 3, rng), f'Setelah {n} adalah {n+1}.', 'easy', 'mengingat', comp)
        if n > 0:
            p.mc(tp, f'Bilangan sebelum {n} adalah ....', str(n - 1), opts(n - 1, 0, 20, 3, rng), f'Sebelum {n} adalah {n-1}.', 'easy', 'mengingat', comp)
            p.fill(tp, f'Isilah: ..., {n}, {min(n + 1, 20)}  Bilangan yang hilang di depan adalah ....', str(n - 1), f'Urutan: {n-1}, {n}, {min(n+1,20)}.', 'easy', 'mengingat', comp)
    p.gk = None
    for s in range(lo, hi - 2, 3):
        p.match(tp, 'Jodohkan angka dengan tulisannya!', [(str(i), KATA[i]) for i in range(s, min(s + 4, hi + 1))][:4], 'Setiap angka ditulis dengan kata.', 'medium', 'mencocokkan', comp) if min(s + 4, hi + 1) - s >= 4 else None
    p.perf(tp, f'Hitunglah benda di kelasmu, lalu sebutkan dan tulis bilangannya (sampai {hi})!', R, 'Murid menghitung dan menulis bilangan.', 'easy', 'menerapkan', comp)
    p.perf(tp, f'Tulislah angka {lo} sampai {hi} dengan rapi dan bacakan!', R, 'Murid menulis dan membaca bilangan.', 'easy', 'menerapkan', comp)


def compare(p, tp, lo, hi, seed=0, nmax=60):
    comp = f'Membandingkan bilangan sampai {hi}'
    rng = random.Random(seed)
    pairs = [(a, b) for a in range(lo, hi + 1) for b in range(lo, hi + 1) if a != b]
    rng.shuffle(pairs)
    for (a, b) in pairs[:nmax]:
        p.gk = f'cp{a}_{b}'
        sym = '>' if a > b else '<'
        p.mc(tp, f'Tanda yang tepat untuk {a} .... {b} adalah ....', sym, [x for x in ['<', '>', '=', '+'] if x != sym], f'{a} {sym} {b}.', 'easy', 'membandingkan', comp)
        p.tf(tp, f'{a} {sym} {b}.', True, f'Benar, {a} {sym} {b}.', 'easy', 'membandingkan', comp)
        p.tf(tp, f'{a} {"<" if a > b else ">"} {b}.', False, f'Salah, yang benar {a} {sym} {b}.', 'easy', 'membandingkan', comp)
        p.fill(tp, f'Isilah dengan tanda <, >, atau =: {a} .... {b}', sym, f'{a} {sym} {b}.', 'easy', 'membandingkan', comp)
    p.gk = None
    for i in range(14):
        a = rng.randint(lo, hi); b = rng.randint(lo, hi)
        while b == a: b = rng.randint(lo, hi)
        c = rng.randint(lo, hi)
        while c in (a, b): c = rng.randint(lo, hi)
        trio = [a, b, c]
        p.gk = f'cg{i}'
        p.mc(tp, f'Di antara bilangan {a}, {b}, dan {c}, bilangan yang paling besar adalah ....', str(max(trio)), [str(x) for x in trio if x != max(trio)] + [str(max(trio) + 1)], f'Terbesar: {max(trio)}.', 'medium', 'membandingkan', comp)
        p.mc(tp, f'Di antara bilangan {a}, {b}, dan {c}, bilangan yang paling kecil adalah ....', str(min(trio)), [str(x) for x in trio if x != min(trio)] + [str(max(0, min(trio) - 1))], f'Terkecil: {min(trio)}.', 'medium', 'membandingkan', comp)
    p.gk = None
    for i in range(10):
        a = rng.randint(lo, hi); b = rng.randint(lo, hi)
        while a == b: b = rng.randint(lo, hi)
        o1, o2 = rng.sample(OBJ, 2)
        win = 'A' if a > b else 'B'
        p.mc(tp, f'Perhatikan gambar! Keranjang A berisi {a} {o1} dan keranjang B berisi {b} {o1}. Keranjang yang berisi lebih banyak adalah ....', win, [x for x in ['A', 'B', 'sama banyak', 'tidak dapat ditentukan'] if x != win],
             f'{max(a,b)} lebih banyak daripada {min(a,b)}.', 'easy', 'membandingkan', comp, visual=f'Dua keranjang: A berisi {a} {o1} dan B berisi {b} {o1}.')
        p.mc(tp, f'Ibu membeli {a} {o2} dan ayah membeli {b} {o2}. Yang membeli lebih sedikit adalah ....', 'ibu' if a < b else 'ayah', [x for x in ['ibu', 'ayah', 'sama banyak', 'adik'] if x != ('ibu' if a < b else 'ayah')], f'{min(a,b)} lebih sedikit daripada {max(a,b)}.', 'medium', 'membandingkan', comp)
    p.perf(tp, 'Bandingkan dua tumpuk benda di kelas, lalu sebutkan mana yang lebih banyak dan lebih sedikit!', R, 'Murid membandingkan jumlah benda.', 'easy', 'menerapkan', comp)


def order_nums(p, tp, lo, hi, seed=0, n=18):
    comp = f'Mengurutkan bilangan sampai {hi}'
    rng = random.Random(seed)
    seen = set()
    for i in range(n):
        k = rng.choice([4, 5])
        nums = tuple(sorted(rng.sample(range(lo, hi + 1), k)))
        if nums in seen: continue
        seen.add(nums)
        asc = i % 2 == 0
        seq = list(nums) if asc else list(reversed(nums))
        p.order(tp, 'Urutkan bilangan berikut dari yang ' + ('terkecil' if asc else 'terbesar') + '!', [str(x) for x in seq], 'Urutan: ' + ', '.join(map(str, seq)) + '.', 'medium', 'mengurutkan', comp)
        shuffled = seq[:]
        rng.shuffle(shuffled)
        right = ', '.join(map(str, seq))
        wrong = []
        for _ in range(20):
            t = seq[:]; rng.shuffle(t)
            s = ', '.join(map(str, t))
            if s != right and s not in wrong: wrong.append(s)
            if len(wrong) == 3: break
        p.gk = f'on{i}'
        if len(wrong) == 3:
            p.mc(tp, f'Bilangan {", ".join(map(str, shuffled))} jika diurutkan dari yang {"terkecil" if asc else "terbesar"} menjadi ....', right, wrong, 'Urutan: ' + right + '.', 'medium', 'mengurutkan', comp)
        p.tf(tp, f'Urutan {right} sudah urut dari yang {"terkecil" if asc else "terbesar"}.', True, 'Urutannya benar.', 'easy', 'mengurutkan', comp)
        p.tf(tp, f'Urutan {", ".join(map(str, (list(reversed(seq)))))} sudah urut dari yang {"terkecil" if asc else "terbesar"}.', False, f'Yang benar: {right}.', 'easy', 'mengurutkan', comp)
    p.gk = None
    for i in range(16):
        start = rng.randint(lo, hi - 4)
        run = list(range(start, start + 5))
        gap = rng.randint(1, 3)
        shown = [('....' if j == gap else str(x)) for j, x in enumerate(run)]
        p.mc(tp, 'Bilangan yang hilang pada urutan ' + ', '.join(shown) + ' adalah ....', str(run[gap]), opts(run[gap], 0, hi, 3, rng), f'Urutan lengkap: {", ".join(map(str, run))}.', 'easy', 'mengurutkan', comp)
        p.fill(tp, 'Lengkapi urutan bilangan: ' + ', '.join(shown), str(run[gap]), f'Urutan lengkap: {", ".join(map(str, run))}.', 'easy', 'mengurutkan', comp)
        desc = list(reversed(run))
        gp = rng.randint(1, 3)
        shown2 = [('....' if j == gp else str(x)) for j, x in enumerate(desc)]
        p.fill(tp, 'Lengkapi urutan bilangan menurun: ' + ', '.join(shown2), str(desc[gp]), f'Urutan lengkap: {", ".join(map(str, desc))}.', 'medium', 'mengurutkan', comp)
    p.perf(tp, f'Susun kartu bilangan acak menjadi urutan dari terkecil sampai {hi}!', R, 'Murid mengurutkan kartu bilangan.', 'easy', 'menerapkan', comp)
    p.perf(tp, 'Susun kartu bilangan dari yang terbesar ke yang terkecil lalu bacakan!', R, 'Murid mengurutkan menurun.', 'medium', 'menerapkan', comp)


def pairs_sum(p, tp, smax, seed=0):
    comp = 'Menemukan pasangan bilangan'
    rng = random.Random(seed)
    for s in range(2, smax + 1):
        p.gk = f'ps{s}'
        a = 1
        pairs = [(x, s - x) for x in range(0, s + 1)]
        good = [(x, y) for x, y in pairs if 1 <= x <= y]
        for (x, y) in good[:3]:
            p.mc(tp, f'Pasangan bilangan yang jumlahnya {s} adalah {x} dan ....', str(y), opts(y, 0, 10 if smax <= 10 else 20, 3, rng), f'{x} + {y} = {s}.', 'easy', 'menganalisis', comp)
            p.fill(tp, f'Isilah: {x} dan .... berpasangan menjadi {s}.', str(y), f'{x} + {y} = {s}.', 'easy', 'menganalisis', comp)
            p.tf(tp, f'{x} dan {y} adalah pasangan bilangan yang jumlahnya {s}.', True, f'{x} + {y} = {s}.', 'easy', 'menganalisis', comp)
            p.tf(tp, f'{x} dan {y + 1} adalah pasangan bilangan yang jumlahnya {s}.', False, f'{x} + {y+1} = {x+y+1}, bukan {s}.', 'medium', 'menganalisis', comp)
    p.gk = None
    p.order(tp, 'Urutkan pasangan bilangan yang jumlahnya 5 dari yang dimulai angka 0!', ['0 + 5', '1 + 4', '2 + 3', '3 + 2'], 'Pasangan bilangan 5.', 'medium', 'mengurutkan', comp)
    p.match(tp, 'Jodohkan pasangan bilangan dengan jumlahnya!', [('2 dan 3', '5'), ('4 dan 4', '8'), ('1 dan 6', '7'), ('3 dan 6', '9')], 'Jumlah pasangan bilangan.', 'medium', 'mencocokkan', comp)
    p.match(tp, 'Jodohkan pasangan bilangan dengan jumlahnya!', [('5 dan 5', '10'), ('2 dan 2', '4'), ('3 dan 3', '6'), ('1 dan 2', '3')], 'Jumlah pasangan bilangan.', 'medium', 'mencocokkan', comp)
    p.perf(tp, 'Gunakan sepuluh kancing: carilah semua pasangan bilangan yang jumlahnya 10!', R, 'Murid menemukan pasangan bilangan.', 'medium', 'menerapkan', comp)


def add_ops(p, tp, maxsum, seed=0, nmax=60, minsum=2):
    comp = f'Penjumlahan sampai {maxsum}'
    rng = random.Random(seed)
    combos = [(a, b) for a in range(1, maxsum) for b in range(1, maxsum) if minsum <= a + b <= maxsum]
    rng.shuffle(combos)
    for (a, b) in combos[:nmax]:
        s = a + b
        p.gk = f'ad{a}_{b}'
        p.mc(tp, f'{a} + {b} = ....', str(s), opts(s, 0, maxsum + 1, 3, rng), f'{a} + {b} = {s}.', 'easy', 'menerapkan', comp)
        p.fill(tp, f'Hitunglah: {a} + {b} = ....', str(s), f'{a} + {b} = {s}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{a} + {b} = {s}.', True, f'Benar, {a} + {b} = {s}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{a} + {b} = {s + rng.choice([-1, 1])}.', False, f'Salah, {a} + {b} = {s}.', 'easy', 'menerapkan', comp)
        if b > 1 and rng.random() < 0.6:
            p.fill(tp, f'Isilah titik-titik: {a} + .... = {s}', str(b), f'{a} + {b} = {s}.', 'medium', 'menganalisis', comp)
    p.gk = None
    for i in range(10):
        a, b = combos[i]
        o = OBJ[i % len(OBJ)]
        s = a + b
        p.mc(tp, f'Perhatikan gambar! Ada {a} {o} di kiri dan {b} {o} di kanan. Kalimat matematika yang sesuai adalah ....', f'{a} + {b} = {s}', [f'{a} + {b} = {s + 1}', f'{a} - {b} = {abs(a - b)}', f'{a} + {b} = {max(s - 1, 0)}'], f'Gabungan {a} dan {b} = {s}.', 'medium', 'menerapkan', comp,
             visual=f'Sisi kiri gambar menampilkan {a} {OBJD[o]}, sisi kanan menampilkan {b} {OBJD[o]}, di tengah tanda tambah.')
    p.perf(tp, f'Gunakan benda konkret (kancing atau kelereng) untuk menunjukkan penjumlahan sampai {maxsum}!', R, 'Murid menjumlahkan dengan benda konkret.', 'easy', 'menerapkan', comp)


def sub_ops(p, tp, maxn, seed=0, nmax=60):
    comp = f'Pengurangan sampai {maxn}'
    rng = random.Random(seed)
    combos = [(a, b) for a in range(2, maxn + 1) for b in range(1, a + 1)]
    rng.shuffle(combos)
    for (a, b) in combos[:nmax]:
        d = a - b
        p.gk = f'sb{a}_{b}'
        p.mc(tp, f'{a} - {b} = ....', str(d), opts(d, 0, maxn, 3, rng), f'{a} - {b} = {d}.', 'easy', 'menerapkan', comp)
        p.fill(tp, f'Hitunglah: {a} - {b} = ....', str(d), f'{a} - {b} = {d}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{a} - {b} = {d}.', True, f'Benar, {a} - {b} = {d}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{a} - {b} = {d + rng.choice([1, 2])}.', False, f'Salah, {a} - {b} = {d}.', 'easy', 'menerapkan', comp)
        if b >= 1 and rng.random() < 0.6:
            p.fill(tp, f'Isilah titik-titik: {a} - .... = {d}', str(b), f'{a} - {b} = {d}.', 'medium', 'menganalisis', comp)
    p.gk = None
    for i in range(10):
        a, b = combos[i]
        o = OBJ[(i + 3) % len(OBJ)]
        d = a - b
        p.mc(tp, f'Perhatikan gambar! Ada {a} {o}, lalu {b} {o} diambil. Kalimat matematika yang sesuai adalah ....', f'{a} - {b} = {d}', [f'{a} + {b} = {a + b}', f'{a} - {b} = {d + 1}', f'{b} - {a} = {d}', f'{a} - {b} = {d + 2}'], f'{a} dikurangi {b} = {d}.', 'medium', 'menerapkan', comp,
             visual=f'Gambar menampilkan {a} {OBJD[o]}; {b} di antaranya dicoret silang karena diambil.')
    p.perf(tp, f'Gunakan benda konkret untuk menunjukkan pengurangan sampai {maxn}!', R, 'Murid mengurangi dengan benda konkret.', 'easy', 'menerapkan', comp)


def stories_add(p, tp, maxsum, seed=0, n=30):
    comp = 'Soal cerita penjumlahan'
    rng = random.Random(seed)
    T = ['{n} memiliki {a} {o}. Kemudian {n} mendapat {b} {o} lagi. Berapa {o} {n} sekarang?',
         'Di keranjang ada {a} {o}. Ibu memasukkan {b} {o} lagi. Berapa seluruh {o} di keranjang?',
         '{n} membeli {a} {o} di pagi hari dan {b} {o} di sore hari. Berapa jumlah {o} yang dibeli {n}?']
    combos = [(a, b) for a in range(1, maxsum) for b in range(1, maxsum) if a + b <= maxsum]
    rng.shuffle(combos)
    for i, (a, b) in enumerate(combos[:n]):
        nm = NAMA[i % len(NAMA)]; o = OBJ[(i * 3) % len(OBJ)]
        s = a + b
        q = T[i % 3].format(n=nm, a=a, b=b, o=o)
        p.gk = f'sa{i}'
        p.ctx(tp, q, str(s), opts(s, 0, maxsum + 1, 3, rng), f'{a} + {b} = {s}.', 'medium', 'menerapkan', comp)
        p.fill(tp, q + ' Jawaban: ....', str(s), f'{a} + {b} = {s}.', 'medium', 'menerapkan', comp, typ='completion')
        p.tf(tp, q + f' Jawabannya {s}.', True, f'{a} + {b} = {s}.', 'easy', 'menerapkan', comp)
        p.tf(tp, q + f' Jawabannya {s + rng.choice([-1, 1, 2])}.', False, f'{a} + {b} = {s}.', 'easy', 'menerapkan', comp)
    p.gk = None
    p.perf(tp, 'Buatlah satu soal cerita penjumlahan dari gambar atau bendamu, lalu selesaikan!', R, 'Murid membuat dan menyelesaikan soal cerita.', 'medium', 'menerapkan', comp)


def stories_sub(p, tp, maxn, seed=0, n=30):
    comp = 'Soal cerita pengurangan'
    rng = random.Random(seed)
    T = ['{n} memiliki {a} {o}. {b} {o} diberikan kepada adik. Berapa sisa {o} {n}?',
         'Di piring ada {a} {o}. Sebanyak {b} {o} dimakan. Berapa {o} yang tersisa?',
         '{n} membawa {a} {o}. Sebanyak {b} {o} jatuh. Berapa {o} yang masih dibawa {n}?']
    combos = [(a, b) for a in range(2, maxn + 1) for b in range(1, a)]
    rng.shuffle(combos)
    for i, (a, b) in enumerate(combos[:n]):
        nm = NAMA[(i + 5) % len(NAMA)]; o = OBJ[(i * 3 + 1) % len(OBJ)]
        d = a - b
        q = T[i % 3].format(n=nm, a=a, b=b, o=o)
        p.gk = f'ss{i}'
        p.ctx(tp, q, str(d), opts(d, 0, maxn, 3, rng), f'{a} - {b} = {d}.', 'medium', 'menerapkan', comp)
        p.fill(tp, q + ' Jawaban: ....', str(d), f'{a} - {b} = {d}.', 'medium', 'menerapkan', comp, typ='completion')
        p.tf(tp, q + f' Jawabannya {d}.', True, f'{a} - {b} = {d}.', 'easy', 'menerapkan', comp)
        p.tf(tp, q + f' Jawabannya {d + rng.choice([1, 2])}.', False, f'{a} - {b} = {d}.', 'easy', 'menerapkan', comp)
    p.gk = None
    p.perf(tp, 'Buatlah satu soal cerita pengurangan dari bendamu, lalu selesaikan!', R, 'Murid membuat dan menyelesaikan soal cerita.', 'medium', 'menerapkan', comp)


def place_value(p, tp, seed=0):
    comp = 'Mengenal nilai tempat'
    rng = random.Random(seed)
    for n in range(10, 21):
        p.gk = f'pv{n}'
        pu, sa = n // 10, n % 10
        p.mc(tp, f'Bilangan {n} terdiri atas ... puluhan dan ... satuan.', f'{pu} puluhan dan {sa} satuan', [f'{pu + 1} puluhan dan {sa} satuan', f'{pu} puluhan dan {sa + 1} satuan', f'{sa} puluhan dan {pu} satuan', f'{pu + 1} puluhan dan {sa + 1} satuan', f'{pu} puluhan dan {sa + 2} satuan'],
             f'{n} = {pu} puluhan dan {sa} satuan.', 'medium', 'memahami', comp)
        p.fill(tp, f'Isilah: Pada bilangan {n}, banyaknya satuan adalah ....', str(sa), f'{n} = {pu} puluhan + {sa} satuan.', 'easy', 'memahami', comp)
        p.fill(tp, f'Isilah: Pada bilangan {n}, banyaknya puluhan adalah ....', str(pu), f'{n} = {pu} puluhan + {sa} satuan.', 'easy', 'memahami', comp)
        p.mc(tp, f'{pu * 10} + {sa} = ....', str(n), opts(n, 0, 20, 3, rng), f'{pu*10} + {sa} = {n}.', 'easy', 'memahami', comp)
        p.tf(tp, f'Bilangan {n} terdiri atas {pu} puluhan dan {sa} satuan.', True, f'Benar, {n} = {pu} puluhan + {sa} satuan.', 'easy', 'memahami', comp)
        p.tf(tp, f'Bilangan {n} terdiri atas {sa} puluhan dan {pu} satuan.', False if sa != pu else True, f'{n} = {pu} puluhan + {sa} satuan.', 'easy', 'memahami', comp) if sa != pu else None
        p.mc(tp, f'{pu} puluhan dan {sa} satuan membentuk bilangan ....', str(n), opts(n, 0, 20, 3, rng), f'{pu} puluhan + {sa} satuan = {n}.', 'medium', 'memahami', comp)
        p.ctx(tp, f'Perhatikan gambar! Ada {pu} ikat berisi sepuluh lidi dan {sa} lidi lepas. Jumlah lidi seluruhnya adalah ....', str(n), opts(n, 0, 20, 3, rng), f'{pu*10} + {sa} = {n}.', 'medium', 'menerapkan', comp) if False else None
        p.mc(tp, f'Perhatikan gambar nilai tempat nomor {n}! Gambar menunjukkan bilangan ....', str(n), opts(n, 0, 20, 3, rng), f'{pu} puluhan + {sa} satuan = {n}.', 'medium', 'menerapkan', comp,
             visual=f'Papan nilai tempat: {pu} ikat lidi (masing-masing sepuluh) di kolom puluhan dan {sa} lidi lepas di kolom satuan.')
    p.gk = None
    p.match(tp, 'Jodohkan bilangan dengan susunan nilai tempatnya!', [('12', '1 puluhan dan 2 satuan'), ('15', '1 puluhan dan 5 satuan'), ('18', '1 puluhan dan 8 satuan'), ('20', '2 puluhan dan 0 satuan')], 'Nilai tempat.', 'medium', 'mencocokkan', comp)
    p.match(tp, 'Jodohkan bilangan dengan susunan nilai tempatnya!', [('11', '1 puluhan dan 1 satuan'), ('14', '1 puluhan dan 4 satuan'), ('17', '1 puluhan dan 7 satuan'), ('13', '1 puluhan dan 3 satuan')], 'Nilai tempat.', 'medium', 'mencocokkan', comp)
    p.perf(tp, 'Ikat sepuluh lidi menjadi satu, lalu tunjukkan bilangan 14 dengan puluhan dan satuan!', R, 'Murid menunjukkan nilai tempat.', 'medium', 'menerapkan', comp)


def share(p, tp, seed=0):
    comp = 'Berbagi adil dan bersedekah'
    rng = random.Random(seed)
    for i, a in enumerate([2, 4, 6, 8, 10]):
        nm = NAMA[i]; o = ['kue', 'permen', 'apel', 'jeruk', 'roti'][i]
        h = a // 2
        p.gk = f'sh{i}'
        q = f'{nm} memiliki {a} {o}. {nm} membagi {o} itu sama banyak kepada dirinya dan temannya agar adil. Setiap anak mendapat ....'
        p.ctx(tp, q, f'{h} {o}', [f'{h + 1} {o}', f'{a} {o}', f'{a + 2} {o}', f'{h + 2} {o}'], f'{a} dibagi dua sama banyak = {h}.', 'medium', 'menerapkan', comp)
        p.tf(tp, f'{nm} membagi {a} {o} sama banyak untuk dua anak. Setiap anak mendapat {h} {o}.', True, f'{a} dibagi dua = {h}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{nm} membagi {a} {o} sama banyak untuk dua anak. Setiap anak mendapat {h + 1} {o}.', False, f'Yang benar {h} {o}.', 'easy', 'menerapkan', comp)
    for i, (a, b) in enumerate([(9, 3), (8, 2), (10, 4), (7, 2), (6, 1), (10, 5)]):
        nm = NAMA[i + 6]
        p.gk = f'sd{i}'
        q = f'{nm} memiliki {a} koin. {nm} menyedekahkan {b} koin ke kotak amal. Sisa koin {nm} adalah ....'
        p.ctx(tp, q, str(a - b), opts(a - b, 0, 10, 3, rng), f'{a} - {b} = {a-b}.', 'medium', 'menerapkan', comp)
        p.fill(tp, q, str(a - b), f'{a} - {b} = {a-b}.', 'medium', 'menerapkan', comp)
        p.tf(tp, f'{nm} memiliki {a} koin dan menyedekahkan {b}. Sisa koinnya {a - b}.', True, f'{a} - {b} = {a-b}.', 'easy', 'menerapkan', comp)
    p.gk = None
    for i, (a, b) in enumerate([(3, 4), (2, 5), (4, 4), (1, 6)]):
        nm = NAMA[i + 10]
        q = f'{nm} menyedekahkan {a} buku dan temannya menyedekahkan {b} buku ke perpustakaan masjid. Jumlah buku yang disedekahkan adalah ....'
        p.ctx(tp, q, str(a + b), opts(a + b, 0, 12, 3, random.Random(i)), f'{a} + {b} = {a+b}.', 'medium', 'menerapkan', comp)
    p.perf(tp, 'Bagilah delapan kelereng sama banyak untuk dua temanmu dan ceritakan mengapa berbagi harus adil!', R, 'Murid berbagi adil.', 'medium', 'menerapkan', comp)
    p.perf(tp, 'Ceritakan satu kali kamu berbagi atau bersedekah dan hitung jumlah yang kamu bagikan!', R, 'Murid menerapkan berbagi.', 'medium', 'menerapkan', comp)


LENG = [('meja', 'pensil'), ('buku', 'klip kertas'), ('papan tulis', 'jengkal'), ('tali', 'klip kertas'), ('pita', 'pensil'), ('kain', 'jengkal'), ('tongkat', 'langkah'), ('karpet', 'jengkal'), ('pintu', 'depa'), ('lorong kelas', 'langkah')]


def length(p, tp_cmp, tp_meas, seed=0):
    rng = random.Random(seed)
    cc = 'Membandingkan panjang benda'
    cm = 'Mengukur panjang dengan satuan tidak baku'
    for i, (b, u) in enumerate(LENG):
        other = LENG[(i + 3) % len(LENG)][0]
        a1 = rng.randint(3, 9); a2 = rng.randint(2, 8)
        while a1 == a2: a2 = rng.randint(2, 8)
        p.gk = f'lc{i}'
        win = b if a1 > a2 else other
        lose = other if a1 > a2 else b
        p.mc(tp_cmp, f'Panjang {b} adalah {a1} {u} dan panjang {other} adalah {a2} {u}. Benda yang lebih panjang adalah ....', win, [lose, 'sama panjang', 'tidak dapat dibandingkan'], f'{max(a1,a2)} {u} lebih panjang daripada {min(a1,a2)} {u}.', 'medium', 'membandingkan', cc)
        p.mc(tp_cmp, f'Panjang {b} adalah {a1} {u} dan panjang {other} adalah {a2} {u}. Benda yang lebih pendek adalah ....', lose, [win, 'sama panjang', 'tidak dapat dibandingkan'], f'{min(a1,a2)} {u} lebih pendek.', 'medium', 'membandingkan', cc)
        p.tf(tp_cmp, f'Panjang {b} {a1} {u} dan panjang {other} {a2} {u}. {win.capitalize()} lebih panjang.', True, f'{max(a1,a2)} {u} > {min(a1,a2)} {u}.', 'easy', 'membandingkan', cc)
        p.tf(tp_cmp, f'Panjang {b} {a1} {u} dan panjang {other} {a2} {u}. {lose.capitalize()} lebih panjang.', False, f'Yang lebih panjang {win}.', 'easy', 'membandingkan', cc)
        d = abs(a1 - a2)
        p.gk = f'lm{i}'
        p.mc(tp_meas, f'Panjang {b} adalah {a1} {u} dan panjang {other} adalah {a2} {u}. Selisih panjangnya adalah ... {u}.', str(d), opts(d, 0, 10, 3, rng), f'{max(a1,a2)} - {min(a1,a2)} = {d}.', 'hard', 'menerapkan', cm)
        p.mc(tp_meas, f'Perhatikan gambar! {b.capitalize()} diukur dengan {u}, dan hasilnya {a1} {u}. Ukuran {b} adalah ....', f'{a1} {u}', [f'{a1 + 1} {u}', f'{max(a1 - 1, 1)} {u}', f'{a1 + 2} {u}'], f'Hasil pengukuran: {a1} {u}.', 'easy', 'menerapkan', cm,
             visual=f'Gambar {b} dengan {a1} {u} diletakkan berjajar dari ujung ke ujung tanpa celah.')
        p.fill(tp_meas, f'Isilah: Jika {b} diukur dengan {u}, panjangnya {a1} {u}. Jika dua {b} yang sama disambung, panjangnya ....', str(a1 * 2), f'{a1} + {a1} = {a1*2}.', 'hard', 'menerapkan', cm) if a1 * 2 <= 20 else None
    p.gk = None
    for i in range(8):
        a, b, c = rng.sample(range(2, 12), 3)
        names = ['pita merah', 'pita biru', 'pita kuning']
        trio = sorted(zip([a, b, c], names))
        p.order(tp_cmp, f'Panjang pita merah {a} klip, pita biru {b} klip, dan pita kuning {c} klip. Urutkan dari yang terpendek!', [t[1] for t in trio], 'Urutan: ' + ', '.join(t[1] for t in trio) + '.', 'medium', 'mengurutkan', cc)
        p.mc(tp_cmp, f'Panjang pita merah {a} klip, pita biru {b} klip, dan pita kuning {c} klip. Pita yang paling panjang adalah ....', trio[-1][1], [t[1] for t in trio[:-1]] + ['semua sama'], f'Terpanjang: {trio[-1][1]}.', 'medium', 'membandingkan', cc)
    p.perf(tp_meas, 'Ukur panjang mejamu dengan pensil atau jengkal lalu tulis hasilnya!', R, 'Murid mengukur panjang.', 'easy', 'menerapkan', cm)
    p.perf(tp_meas, 'Ukur panjang lorong kelas dengan langkah kakimu dan ceritakan hasilnya!', R, 'Murid mengukur dengan langkah.', 'medium', 'menerapkan', cm)
    p.perf(tp_cmp, 'Bandingkan panjang dua benda di mejamu secara langsung dan sebutkan mana yang lebih panjang!', R, 'Murid membandingkan panjang.', 'easy', 'menerapkan', cc)


DATA = [
 ('buah di keranjang', [('apel', 5), ('jeruk', 3), ('pisang', 4)]), ('hewan di kebun binatang', [('gajah', 2), ('zebra', 6), ('kelinci', 4)]),
 ('mainan Dina', [('boneka', 3), ('mobil', 5), ('bola', 2)]), ('warna kesukaan murid', [('merah', 6), ('biru', 4), ('hijau', 5)]),
 ('buku di rak', [('cerita', 7), ('pelajaran', 4), ('gambar', 3)]), ('bunga di taman', [('mawar', 5), ('melati', 2), ('anggrek', 4)]),
 ('kendaraan lewat', [('motor', 8), ('mobil', 5), ('sepeda', 3)]), ('jajanan terjual', [('roti', 4), ('kue', 6), ('permen', 7)]),
 ('hewan peliharaan murid', [('kucing', 6), ('ikan', 5), ('burung', 3)]), ('alat tulis di tas', [('pensil', 5), ('penghapus', 2), ('penggaris', 3)]),
 ('olahraga kesukaan', [('sepak bola', 7), ('lari', 4), ('berenang', 5)]), ('makanan bekal', [('nasi', 6), ('roti', 3), ('mi', 4)]),
]


def tally(n):
    return ' '.join(['|||||'] * (n // 5) + (['|' * (n % 5)] if n % 5 else []))


def data_gen(p, tp_cara, tp_kel, tp_bdg, seed=0):
    rng = random.Random(seed)
    cc, ck, cb = 'Mengenal cara menyajikan data', 'Mengelompokkan data', 'Membandingkan dan menyajikan data'
    for i, (tema, items) in enumerate(DATA):
        names = [x[0] for x in items]; cnt = [x[1] for x in items]
        text = ', '.join(f'{n} {c}' for n, c in items)
        mx = max(cnt); mn = min(cnt)
        top = names[cnt.index(mx)]; low = names[cnt.index(mn)]
        total = sum(cnt)
        p.gk = f'dk{i}'
        p.fill(tp_kel, f'Data {tema}: {text}. Banyaknya seluruh data adalah ....', str(total), f'{" + ".join(map(str, cnt))} = {total}.', 'medium', 'menganalisis', ck)
        p.mc(tp_kel, f'Data {tema}: {text}. Banyaknya {names[0]} adalah ....', str(cnt[0]), opts(cnt[0], 0, 12, 3, rng), f'{names[0]} = {cnt[0]}.', 'easy', 'mengenali', ck)
        p.mc(tp_kel, f'Data {tema}: {text}. Kelompok dengan jumlah terbanyak adalah ....', top, [x for x in names if x != top] + ['semua sama'], f'Terbanyak: {top} ({mx}).', 'medium', 'membandingkan', ck)
        p.gk = f'db{i}'
        p.mc(tp_bdg, f'Data {tema}: {text}. Kelompok dengan jumlah paling sedikit adalah ....', low, [x for x in names if x != low] + ['semua sama'], f'Tersedikit: {low} ({mn}).', 'medium', 'membandingkan', cb)
        d = mx - mn
        p.mc(tp_bdg, f'Data {tema}: {text}. Selisih antara yang terbanyak dan yang paling sedikit adalah ....', str(d), opts(d, 0, 10, 3, rng), f'{mx} - {mn} = {d}.', 'hard', 'menganalisis', cb)
        p.tf(tp_bdg, f'Data {tema}: {text}. {top.capitalize()} adalah yang terbanyak.', True, f'Terbanyak: {top}.', 'easy', 'membandingkan', cb)
        p.tf(tp_bdg, f'Data {tema}: {text}. {low.capitalize()} adalah yang terbanyak.', False, f'Terbanyak: {top}.', 'easy', 'membandingkan', cb)
        p.gk = f'dc{i}'
        s = f'{names[0]}: {tally(cnt[0])}'
        p.mc(tp_cara, f'Perhatikan turus berikut tentang {tema}! {s}. Banyaknya {names[0]} adalah ....', str(cnt[0]), opts(cnt[0], 0, 12, 3, rng), f'Turus {tally(cnt[0])} = {cnt[0]}.', 'medium', 'menerapkan', cc,
             visual=f'Tabel turus: baris "{names[0]}" berisi tanda turus {tally(cnt[0])} (setiap lima turus dikelompokkan).')
        p.mc(tp_cara, f'Perhatikan piktogram {tema}! {names[1]} digambar {cnt[1]} kali dan {names[2]} digambar {cnt[2]} kali. Yang digambar lebih banyak adalah ....', names[1] if cnt[1] > cnt[2] else names[2] if cnt[2] > cnt[1] else 'sama banyak',
             [x for x in [names[1], names[2], 'sama banyak', names[0]] if x != (names[1] if cnt[1] > cnt[2] else names[2] if cnt[2] > cnt[1] else 'sama banyak')][:3], 'Bandingkan banyak gambar.', 'medium', 'membandingkan', cc,
             visual=f'Piktogram {tema}: baris {names[1]} berisi {cnt[1]} gambar kecil, baris {names[2]} berisi {cnt[2]} gambar kecil.')
        p.ctx(tp_bdg, f'Banyak {names[0]} adalah {cnt[0]}. Ditulis dengan turus menjadi ....', tally(cnt[0]), [tally(max(cnt[0] - 1, 1)), tally(cnt[0] + 1), tally(cnt[0] + 2)], f'{cnt[0]} = {tally(cnt[0])}.', 'medium', 'menerapkan', cb)
    p.gk = None
    p.perf(tp_cara, 'Buat tabel turus tentang warna baju temanmu hari ini!', R, 'Murid menyajikan data dengan turus.', 'medium', 'menerapkan', cc)
    p.perf(tp_cara, 'Gambarlah piktogram sederhana tentang buah kesukaan teman sekelompokmu!', R, 'Murid menyajikan data dengan piktogram.', 'medium', 'menerapkan', cc)
    p.perf(tp_kel, 'Kelompokkan alat tulis di mejamu menurut jenisnya lalu hitung tiap kelompok!', R, 'Murid mengelompokkan data.', 'easy', 'menerapkan', ck)
    p.perf(tp_bdg, 'Sajikan hasil hitungan kelompokmu dalam diagram gambar tiga kategori dan bandingkan!', R, 'Murid menyajikan dan membandingkan data.', 'medium', 'menerapkan', cb)


B2D = [('jam dinding', 'lingkaran'), ('koin', 'lingkaran'), ('piring', 'lingkaran'), ('roda sepeda', 'lingkaran'), ('ubin lantai', 'persegi'), ('sapu tangan', 'persegi'),
       ('papan catur', 'persegi'), ('pintu', 'persegi panjang'), ('papan tulis', 'persegi panjang'), ('layar televisi', 'persegi panjang'), ('bendera segitiga', 'segitiga'),
       ('rambu peringatan', 'segitiga'), ('potongan sandwich segitiga', 'segitiga')]
B3D = [('bola sepak', 'bola'), ('kelereng', 'bola'), ('globe', 'bola'), ('dadu', 'kubus'), ('kotak kado berbentuk kubus', 'kubus'), ('kardus sepatu', 'balok'),
       ('batu bata', 'balok'), ('lemari es', 'balok'), ('topi ulang tahun', 'kerucut'), ('cone es krim', 'kerucut'), ('corong', 'kerucut'), ('tumpeng', 'kerucut')]


def shapes_obj(p, tp_desc, tp_group, seed=0):
    rng = random.Random(seed)
    cd, cg = 'Mendeskripsikan benda berdasarkan bentuk', 'Mengelompokkan benda berdasarkan bentuk'
    for dim, data, shapes in (('datar', B2D, ['lingkaran', 'persegi', 'persegi panjang', 'segitiga']), ('ruang', B3D, ['bola', 'kubus', 'balok', 'kerucut'])):
        for i, (b, sh) in enumerate(data):
            p.gk = f'so{b}'
            others = [x for x in shapes if x != sh]
            p.mc(tp_desc, f'Benda "{b}" berbentuk ....', sh, others, f'{b} berbentuk {sh}.', 'easy', 'mengenali', cd)
            p.tf(tp_desc, f'Benda "{b}" berbentuk {sh}.', True, f'Benar, {b} berbentuk {sh}.', 'easy', 'mengenali', cd)
            p.tf(tp_desc, f'Benda "{b}" berbentuk {others[i % 3]}.', False, f'Salah, {b} berbentuk {sh}.', 'easy', 'mengenali', cd)
            p.fill(tp_desc, f'Isilah: Bentuk benda "{b}" adalah ....', sh, f'{b} berbentuk {sh}.', 'easy', 'mengenali', cd)
            p.mc(tp_group, f'Perhatikan gambar nomor {i + 1} bangun {dim}! Benda "{b}" masuk ke dalam kelompok benda berbentuk ....', sh, others, f'{b} termasuk kelompok {sh}.', 'medium', 'mengelompokkan', cg,
                 visual=f'Kartu bergambar {b} dengan siluet bentuk {sh} di bagian bawah.')
    p.gk = None
    for data in (B2D, B3D):
        for i, (b, sh) in enumerate(data):
            same = [x for x, y in data if y == sh and x != b]
            diff = [x for x, y in data if y != sh]
            if not same: continue
            b2 = same[0]; b3 = diff[i % len(diff)]
            p.gk = f'sg{b}'
            p.mc(tp_group, f'Benda yang dapat dikelompokkan bersama "{b}" berdasarkan bentuknya adalah ....', b2, rng.sample(diff, 3), f'{b} dan {b2} sama-sama berbentuk {sh}.', 'medium', 'mengelompokkan', cg)
            p.tf(tp_group, f'"{b}" dan "{b2}" dikelompokkan dalam kelompok bentuk yang sama.', True, f'Keduanya berbentuk {sh}.', 'easy', 'mengelompokkan', cg)
            p.tf(tp_group, f'"{b}" dan "{b3}" dikelompokkan dalam kelompok bentuk yang sama.', False, f'{b} berbentuk {sh}, sedangkan {b3} bentuknya berbeda.', 'easy', 'mengelompokkan', cg)
            p.fill(tp_group, f'Isilah: "{b}" dan "{b2}" termasuk kelompok benda berbentuk ....', sh, f'Keduanya berbentuk {sh}.', 'medium', 'mengelompokkan', cg)
    p.gk = None
    for sh, mem in (('lingkaran', ['jam dinding', 'koin']), ('segitiga', ['bendera segitiga', 'rambu peringatan']), ('persegi', ['ubin lantai', 'papan catur'])):
        pass
    p.group(tp_group, 'Kelompokkan benda berikut berdasarkan bentuknya: jam dinding, ubin lantai, bendera segitiga, koin, sapu tangan, rambu peringatan.',
            {'lingkaran': ['jam dinding', 'koin'], 'persegi': ['ubin lantai', 'sapu tangan'], 'segitiga': ['bendera segitiga', 'rambu peringatan']}, 'Kelompokkan sesuai bentuk.', 'medium', 'mengelompokkan', cg)
    p.group(tp_group, 'Kelompokkan benda berikut berdasarkan bentuknya: bola sepak, dadu, kardus sepatu, kelereng, topi ulang tahun, batu bata.',
            {'bola': ['bola sepak', 'kelereng'], 'kubus': ['dadu'], 'balok': ['kardus sepatu', 'batu bata'], 'kerucut': ['topi ulang tahun']}, 'Kelompokkan sesuai bentuk.', 'medium', 'mengelompokkan', cg)
    p.group(tp_group, 'Kelompokkan: pintu, papan tulis, piring, roda sepeda, layar televisi, koin.',
            {'persegi panjang': ['pintu', 'papan tulis', 'layar televisi'], 'lingkaran': ['piring', 'roda sepeda', 'koin']}, 'Kelompokkan sesuai bentuk.', 'medium', 'mengelompokkan', cg)
    p.group(tp_group, 'Kelompokkan: dadu, cone es krim, globe, lemari es, corong, kotak kado berbentuk kubus.',
            {'bola': ['globe'], 'kubus': ['dadu', 'kotak kado berbentuk kubus'], 'balok': ['lemari es'], 'kerucut': ['cone es krim', 'corong']}, 'Kelompokkan sesuai bentuk.', 'medium', 'mengelompokkan', cg)
    p.match(tp_desc, 'Jodohkan benda dengan bentuknya!', [('jam dinding', 'lingkaran'), ('pintu', 'persegi panjang'), ('ubin lantai', 'persegi'), ('bendera segitiga', 'segitiga')], 'Bentuk benda.', 'medium', 'mencocokkan', cd)
    p.match(tp_desc, 'Jodohkan benda dengan bentuknya!', [('bola sepak', 'bola'), ('dadu', 'kubus'), ('kardus sepatu', 'balok'), ('topi ulang tahun', 'kerucut')], 'Bentuk benda.', 'medium', 'mencocokkan', cd)
    p.perf(tp_group, 'Kumpulkan lima benda di kelas lalu kelompokkan menurut bentuknya!', R, 'Murid mengelompokkan benda.', 'easy', 'menerapkan', cg)


def share_sub(p, tp, seed=0):
    comp = 'Berbagi sebagai wujud kepedulian'
    rng = random.Random(seed)
    for i, (a, b) in enumerate([(10, 3), (9, 4), (8, 5), (7, 3), (6, 2), (10, 6), (9, 2), (8, 1)]):
        nm = NAMA[(i + 2) % len(NAMA)]; o = ['telur', 'roti', 'jeruk', 'buku', 'kue', 'mangga', 'permen', 'apel'][i]
        p.gk = f'ssb{i}'
        q = f'{nm} memiliki {a} {o}. {nm} memberi {b} {o} kepada tetangga yang membutuhkan. Sisa {o} {nm} adalah ....'
        p.ctx(tp, q, str(a - b), opts(a - b, 0, 10, 3, rng), f'{a} - {b} = {a-b}.', 'medium', 'menerapkan', comp)
        p.tf(tp, f'{nm} memiliki {a} {o} dan memberi {b} {o} kepada tetangga. Sisanya {a - b}.', True, f'{a} - {b} = {a-b}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'{nm} memiliki {a} {o} dan memberi {b} {o} kepada tetangga. Sisanya {a - b + 1}.', False, f'{a} - {b} = {a-b}.', 'easy', 'menerapkan', comp)
        p.fill(tp, q, str(a - b), f'{a} - {b} = {a-b}.', 'medium', 'menerapkan', comp)
    p.gk = None


def measure_apply(p, tp, seed=0):
    comp = 'Menerapkan pengukuran panjang dengan bertanggung jawab'
    rng = random.Random(seed)
    for i in range(10):
        nm = NAMA[(i + 7) % len(NAMA)]; b, u = LENG[i]
        a = rng.randint(5, 10); c = rng.randint(1, 4)
        p.gk = f'ma{i}'
        q = f'{nm} memotong {b} sepanjang {a} {u} sebanyak {c} {u} untuk tugas sekolah. Sisa panjang {b} adalah ... {u}.'
        p.ctx(tp, q, str(a - c), opts(a - c, 0, 12, 3, rng), f'{a} - {c} = {a-c}.', 'hard', 'menerapkan', comp)
        q2 = f'{nm} menyambung dua {b} yang panjangnya {c} {u} dan {a} {u}. Panjang sambungannya adalah ... {u}.'
        p.ctx(tp, q2, str(a + c), opts(a + c, 0, 15, 3, rng), f'{a} + {c} = {a+c}.', 'hard', 'menerapkan', comp)
        p.tf(tp, f'{nm} mengukur {b} dengan {u} secara teliti dan jujur sehingga hasilnya dapat dipercaya.', True, 'Mengukur teliti dan jujur adalah tanggung jawab.', 'easy', 'menerapkan', comp)
    p.gk = None


def sign_fill(p, tp, maxn, seed=0, n=24):
    comp = 'Mengenal kalimat matematika dan simbol'
    rng = random.Random(seed)
    for i in range(n):
        if i % 2 == 0:
            a = rng.randint(2, maxn - 1); b = rng.randint(1, maxn - a)
            c = a + b; sg = '+'
        else:
            a = rng.randint(3, maxn); b = rng.randint(1, a - 1)
            c = a - b; sg = '-'
        p.gk = f'sg{i}'
        p.mc(tp, f'Tanda yang tepat untuk melengkapi {a} .... {b} = {c} adalah ....', sg, [x for x in ['+', '-', '>', '<'] if x != sg], f'{a} {sg} {b} = {c}.', 'medium', 'memahami', comp)
        p.fill(tp, f'Isilah tanda + atau - : {a} .... {b} = {c}', sg, f'{a} {sg} {b} = {c}.', 'medium', 'memahami', comp)
        p.tf(tp, f'{a} {sg} {b} = {c}.', True, f'Benar, {a} {sg} {b} = {c}.', 'easy', 'memahami', comp)
        p.tf(tp, f'{a} {"-" if sg == "+" else "+"} {b} = {c}.', False, f'Salah, yang benar {a} {sg} {b} = {c}.', 'easy', 'memahami', comp)
    p.gk = None


def jujur20(p, tp, seed=0):
    comp = 'Mengamalkan ilmu penjumlahan dan pengurangan dengan jujur'
    rng = random.Random(seed)
    for i in range(14):
        nm = NAMA[(i + 3) % len(NAMA)]
        p.gk = f'ju{i}'
        if i % 2 == 0:
            a = rng.randint(6, 12); b = rng.randint(4, 8)
            q = f'{nm} menemukan {a} koin di kelas dan {b} koin di halaman. {nm} menyerahkan semuanya kepada guru dengan jujur. Jumlah koin yang diserahkan adalah ....'
            ans = a + b
            expl = f'{a} + {b} = {ans}.'
        else:
            a = rng.randint(12, 20); b = rng.randint(3, 9)
            q = f'{nm} memiliki {a} kelereng. Dalam permainan, {nm} kalah {b} kelereng dan menghitung sisanya dengan jujur. Sisa kelereng {nm} adalah ....'
            ans = a - b
            expl = f'{a} - {b} = {ans}.'
        p.ctx(tp, q, str(ans), opts(ans, 0, 20, 3, rng), expl, 'medium', 'menerapkan', comp)
        p.fill(tp, q, str(ans), expl, 'medium', 'menerapkan', comp, typ='completion')
        p.tf(tp, q + f' Jawabannya {ans}.', True, expl, 'easy', 'menerapkan', comp)
        p.tf(tp, q + f' Jawabannya {ans + rng.choice([-1, 1])}.', False, expl, 'easy', 'menerapkan', comp)
    p.gk = None
