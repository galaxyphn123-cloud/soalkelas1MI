# -*- coding: utf-8 -*-
"""Pembangkit soal Bahasa Indonesia Kelas 1 (kata berawalan huruf, tanda baca, rumpang, ungkapan, bilangan, arti kata, letak, cerita)."""
import random
import bi_words, bi_misc
from bi_words import WORDS

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
VOK = 'aiueo'
R = 'Dinilai guru: ketepatan, kelancaran, dan kesantunan (skala 1-4).'


CONC = [w for L in WORDS for (w, sy, c) in WORDS[L] if c]


def alt_splits(sy):
    """Pemisahan suku kata yang keliru (geser batas satu huruf, atau pisah per huruf)."""
    w = ''.join(sy)
    out = []
    for i in range(len(sy) - 1):
        a, b = sy[i], sy[i + 1]
        if len(a) > 1:
            t = sy[:]; t[i], t[i + 1] = a[:-1], a[-1] + b; out.append(t)
        if len(b) > 1:
            t = sy[:]; t[i], t[i + 1] = a + b[0], b[1:]; out.append(t)
    out.append(list(w))
    res = []
    for t in out:
        j = '-'.join(t)
        if j != '-'.join(sy) and j not in res:
            res.append(j)
    return res


def letter_words(p, letters, tp, seed=0):
    """Membaca dan menulis kata yang berawalan huruf tertentu."""
    rng = random.Random(seed)
    comp = 'Membaca dan menulis kata berawalan huruf ' + ', '.join(letters)
    allw = [(w, L) for L in letters for (w, sy, c) in WORDS[L]]
    TEMP = ['Kata yang diawali huruf {L} adalah ....', 'Manakah kata yang dimulai dengan huruf {L}?', 'Pilih kata yang berawalan huruf {L}!', 'Kata di bawah ini yang awalnya huruf {L} adalah ....']
    for L in letters:
        ws = WORDS[L]
        others = [w for (w, LL) in allw if LL != L] + [w for LL in ALPHA if LL not in letters for (w, sy, c) in WORDS.get(LL, [])][:12]
        for k, (w, sy, conc) in enumerate(ws[:4]):
            p.gk = f'lt{L}{k}'
            p.mc(tp, TEMP[k].format(L=L), w, rng.sample(others, 3), f'Kata {w} diawali huruf {L}.', 'easy', 'mengenali', comp)
        for j, (w, sy, conc) in enumerate(ws):
            p.gk = f'wd{w}'
            cap = L.upper()
            wrongL = [x for x in ALPHA if x != L]
            p.mc(tp, f'Huruf awal kata "{w}" adalah huruf ....', L, rng.sample(wrongL, 3), f'Kata {w} diawali huruf {L}.', 'easy', 'mengenali', comp)
            p.tf(tp, f'Kata "{w}" diawali huruf {L}.', True, f'Benar, {w} diawali {L}.', 'easy', 'mengenali', comp)
            p.tf(tp, f'Kata "{w}" diawali huruf {rng.choice(wrongL)}.', False, f'Salah. {w} diawali {L}.', 'easy', 'mengenali', comp)
            p.fill(tp, f'Isilah: Kata "{w}" dimulai dengan huruf ....', L, f'{w} dimulai huruf {L}.', 'easy', 'mengenali', comp)
            if len(sy) >= 2:
                good = '-'.join(sy)
                alts = alt_splits(sy)
                if len(alts) >= 3:
                    p.mc(tp, f'Kata "{w}" jika dipisah menjadi suku kata adalah ....', good, alts[:3], f'{w} = {good}.', 'medium', 'menganalisis', comp)
                p.mc(tp, f'Kata "{w}" terdiri atas ... suku kata.', str(len(sy)), [str(x) for x in range(1, 7) if x != len(sy)], f'{w} terdiri atas {len(sy)} suku kata ({good}).', 'medium', 'menganalisis', comp)
                p.tf(tp, f'Kata "{w}" terdiri atas {len(sy)} suku kata.', True, f'Benar, {good}.', 'easy', 'menganalisis', comp)
                if len(sy) >= 3:
                    sh = sy[:]
                    while sh == sy:
                        rng.shuffle(sh)
                    p.order(tp, f'Susun suku kata menjadi kata yang benar! (huruf awal {L})', sy, f'{good} = {w}.', 'medium', 'mengurutkan', comp)
            else:
                p.tf(tp, f'Kata "{w}" terdiri atas satu suku kata.', True, f'{w} hanya satu suku kata.', 'easy', 'menganalisis', comp)
            ch = list(w.replace('-', ''))
            if 3 <= len(ch) <= 8 and '-' not in w:
                p.order(tp, f'Susun huruf-huruf berikut menjadi kata yang benar! (huruf awal {L})', ch, f'{"".join(ch)} adalah kata yang benar.', 'medium', 'mengurutkan', comp)
                pos = next((i for i in range(1, len(ch)) if ch[i] in VOK), None)
                if pos:
                    miss = ch[pos]
                    pat = ''.join('_' if i == pos else c for i, c in enumerate(ch))
                    p.fill(tp, f'Lengkapi huruf yang hilang: {pat}', miss, f'Kata yang benar: {w}.', 'medium', 'mengenali', comp)
                    p.mc(tp, f'Huruf yang tepat untuk melengkapi {pat} adalah ....', miss, rng.sample([x for x in VOK if x != miss] + ['b', 'k'], 3), f'Kata yang benar: {w}.', 'medium', 'mengenali', comp)
            if conc:
                p.mc(tp, f'Perhatikan gambar pada kartu huruf {L} nomor {j + 1}! Nama benda pada gambar adalah ....', w, rng.sample([x for x in CONC if x != w], 3),
                     f'Gambar menunjukkan {w}.', 'easy', 'mengenali', comp, visual=f'Kartu bergambar sebuah {w} dengan latar warna cerah dan huruf besar {L.upper()} di pojok.')
    p.gk = None
    # matching & grouping per kelompok huruf
    pairs = []
    for L in letters:
        pairs.append((WORDS[L][0][0], L))
    for s in range(0, len(pairs) - 3):
        p.match(tp, 'Jodohkan kata dengan huruf awalnya!', pairs[s:s + 4], 'Setiap kata dipasangkan dengan huruf awalnya.', 'medium', 'mencocokkan', comp)
    if len(letters) >= 3:
        for s in range(0, len(letters) - 2):
            ls = letters[s:s + 3]
            gl = {l: [x[0] for x in WORDS[l][:2]] for l in ls}
            ws = [w for v in gl.values() for w in v]
            rng.shuffle(ws)
            p.group(tp, 'Kelompokkan kata berikut berdasarkan huruf awalnya: ' + ', '.join(ws) + '.', gl, 'Kelompokkan sesuai huruf awal.', 'medium', 'mengelompokkan', comp)
    for l in letters[:3]:
        p.perf(tp, f'Bacalah dan tulislah tiga kata yang berawalan huruf {l} dengan rapi!', R, 'Murid membaca dan menulis kata berawalan huruf tersebut.', 'medium', 'menerapkan', comp)


def vowels(p, tp):
    comp = 'Mengenal huruf vokal dan konsonan'
    for L in ALPHA:
        p.gk = f'vk{L}'
        v = L in VOK
        nm = 'vokal' if v else 'konsonan'
        wrong = 'konsonan' if v else 'vokal'
        p.mc(tp, f'Huruf "{L}" termasuk huruf ....', nm, [wrong, 'angka', 'tanda baca'], f'Huruf {L} adalah huruf {nm}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Huruf "{L}" termasuk huruf {nm}.', True, f'Benar, {L} adalah {nm}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Huruf "{L}" termasuk huruf {wrong}.', False, f'Salah, {L} adalah {nm}.', 'easy', 'mengenali', comp)
    allw = [(w, sy) for L in WORDS for (w, sy, c) in WORDS[L] if '-' not in w and len(w) >= 3]
    random.Random(5).shuffle(allw)
    for (w, sy) in allw[:36]:
        p.gk = f'vkw{w}'
        vs = [c for c in w if c in VOK]
        cnt = len(vs)
        p.mc(tp, f'Banyaknya huruf vokal pada kata "{w}" adalah ....', str(cnt), [str(x) for x in range(0, 6) if x != cnt][:5], f'Huruf vokal pada {w}: {", ".join(vs)}.', 'medium', 'menganalisis', comp)
        p.fill(tp, f'Isilah: Huruf vokal pertama pada kata "{w}" adalah ....', vs[0], f'Vokal pertama {w}: {vs[0]}.', 'medium', 'menganalisis', comp)
    p.gk = None


def punct(p, tp_tanya, tp_titik_use):
    """tp_tanya: bab 2 TP 2.3 (tanda tanya & seru). tp_titik_use: bab 5 TP 5.2 (menggunakan titik)."""
    c1 = 'Mengenal tanda tanya dan tanda seru'
    for i, s in enumerate(bi_misc.TANYA if tp_tanya else []):
        p.gk = f'tq{i}'
        p.mc(tp_tanya, f'Kalimat "{s} ...." diakhiri tanda ....', '?', ['.', '!', ','], f'Kalimat tanya ditutup tanda tanya: {s}?', 'easy', 'mengenali', c1)
        p.tf(tp_tanya, f'Kalimat "{s}?" memakai tanda baca yang benar.', True, 'Kalimat tanya memakai ?.', 'easy', 'mengenali', c1)
        p.tf(tp_tanya, f'Kalimat "{s}." memakai tanda baca yang benar.', False, f'Yang benar: {s}?', 'easy', 'mengenali', c1)
        p.fill(tp_tanya, f'Isilah tanda baca yang tepat: {s} ....', '?', f'{s}?', 'easy', 'mengenali', c1)
    for i, s in enumerate(bi_misc.SERU if tp_tanya else []):
        p.gk = f'ts{i}'
        p.mc(tp_tanya, f'Kalimat "{s} ...." diakhiri tanda ....', '!', ['.', '?', ','], f'Kalimat seru ditutup tanda seru: {s}!', 'easy', 'mengenali', c1)
        p.tf(tp_tanya, f'Kalimat "{s}!" memakai tanda baca yang benar.', True, 'Kalimat seru memakai !.', 'easy', 'mengenali', c1)
        p.tf(tp_tanya, f'Kalimat "{s}?" memakai tanda baca yang benar.', False, f'Yang benar: {s}!', 'easy', 'mengenali', c1)
    p.gk = None
    if not tp_titik_use:
        return
    c2 = 'Menggunakan tanda titik pada akhir kalimat'
    for i, s in enumerate(bi_misc.BERITA):
        p.gk = f'bt{i}'
        good = s + '.'
        p.mc(tp_titik_use, 'Penulisan kalimat berita yang benar adalah ....', good, [s + '?', s + '!', s], 'Kalimat berita diakhiri tanda titik.', 'medium', 'menerapkan', c2) if False else None
        p.mc(tp_titik_use, f'Kalimat berita "{s}" ditulis dengan benar sebagai ....', good, [s + '?', s + '!', s + ','], 'Kalimat berita diakhiri tanda titik.', 'medium', 'menerapkan', c2)
        p.tf(tp_titik_use, f'Kalimat "{s}." memakai tanda titik yang benar.', True, 'Kalimat berita memakai titik.', 'easy', 'menerapkan', c2)
        p.tf(tp_titik_use, f'Kalimat "{s}?" memakai tanda baca yang benar.', False, f'Yang benar: {s}.', 'easy', 'menerapkan', c2)
        p.fill(tp_titik_use, f'Lengkapi tanda baca pada akhir kalimat berita: {s} ....', '.', f'{s}.', 'easy', 'menerapkan', c2)
    p.gk = None


def punct_know(p, tp):
    """5.1 mengenal tanda titik: klasifikasi kalimat."""
    comp = 'Mengenal tanda titik pada akhir kalimat'
    for i, s in enumerate(bi_misc.BERITA):
        p.gk = f'pk{i}'
        p.mc(tp, f'Kalimat "{s}." berakhir dengan tanda ....', 'titik', ['tanya', 'seru', 'koma'], 'Kalimat berita berakhir dengan titik.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Kalimat "{s}." adalah kalimat berita.', True, 'Kalimat yang memberi tahu disebut kalimat berita.', 'easy', 'mengenali', comp)
    p.gk = None
    for s in bi_misc.TANYA[:5]:
        p.tf(tp, f'Kalimat "{s}?" adalah kalimat berita.', False, 'Itu kalimat tanya.', 'easy', 'mengenali', comp)
    for s in bi_misc.SERU[:5]:
        p.tf(tp, f'Kalimat "{s}!" adalah kalimat berita.', False, 'Itu kalimat seru.', 'easy', 'mengenali', comp)


def rumpang(p, tp):
    comp = 'Melengkapi kalimat rumpang'
    for i, (k, ok, bad) in enumerate(bi_misc.RUMPANG):
        p.gk = f'rp{i}'
        full = k.replace('....', ok)
        p.mc(tp, f'Lengkapi kalimat berikut: {k}', ok, bad, f'Kalimat lengkap: {full}', 'easy', 'menerapkan', comp)
        p.tf(tp, f'Kalimat "{full}" sudah tepat.', True, f'Kalimat yang tepat: {full}', 'easy', 'menerapkan', comp)
        p.tf(tp, f'Kalimat "{k.replace("....", bad[0])}" sudah tepat.', False, f'Yang tepat: {full}', 'easy', 'menerapkan', comp)
        p.fill(tp, f'Isilah titik-titik agar kalimat bermakna: {k}', ok, f'Kalimat lengkap: {full}', 'easy', 'menerapkan', comp, typ='completion')
    p.gk = None


def ungkapan(p, tp_kenal, tp_pakai):
    c1 = 'Mengenal ungkapan permisi, tolong, maaf, terima kasih'
    c2 = 'Menggunakan ungkapan sesuai kondisi'
    U = ['permisi', 'tolong', 'maaf', 'terima kasih']
    for u, fn in bi_misc.UNGKAPAN_FACT.items():
        o = [x for x in U if x != u]
        p.gk = f'ug{u}'
        p.mc(tp_kenal, f'Ungkapan "{u}" {fn}. Ungkapan itu dipakai ketika ....', fn.replace('dipakai ', ''), [bi_misc.UNGKAPAN_FACT[x].replace('dipakai ', '') for x in o], f'{u} {fn}.', 'medium', 'memahami', c1)
        p.mc(tp_kenal, f'Ungkapan yang {fn} adalah ....', u, o, f'{u} {fn}.', 'easy', 'mengenali', c1)
        p.tf(tp_kenal, f'Ungkapan "{u}" {fn}.', True, f'Benar, {u} {fn}.', 'easy', 'mengenali', c1)
        p.tf(tp_kenal, f'Ungkapan "{u}" {bi_misc.UNGKAPAN_FACT[o[0]]}.', False, f'Salah, {u} {fn}.', 'medium', 'mengenali', c1)
        p.fill(tp_kenal, f'Isilah: Ungkapan yang {fn} adalah ....', u, f'{u} {fn}.', 'easy', 'mengenali', c1)
    p.gk = None
    for i, (sit, u) in enumerate(bi_misc.UNGKAPAN):
        p.gk = f'sc{i}ug'
        o = [x for x in U if x != u]
        p.ctx(tp_pakai, f'{sit} Ungkapan yang tepat adalah ....', u, o, f'Pada situasi itu dipakai ungkapan {u}.', 'easy', 'menerapkan', c2)
        p.tf(tp_pakai, f'{sit} Ungkapan yang tepat: {u}.', True, f'Benar, ungkapan yang tepat {u}.', 'easy', 'menerapkan', c2)
        p.tf(tp_pakai, f'{sit} Ungkapan yang tepat: {o[i % 3]}.', False, f'Salah, yang tepat {u}.', 'medium', 'menerapkan', c2)
        p.fill(tp_pakai, f'{sit} Ucapkan: ....', u, f'Ungkapan yang tepat: {u}.', 'easy', 'menerapkan', c2, typ='completion')
    p.gk = None
    p.match(tp_kenal, 'Jodohkan ungkapan dengan kegunaannya!', [(u, bi_misc.UNGKAPAN_FACT[u].replace('dipakai untuk ', '').replace('dipakai ', '')) for u in U], 'Fungsi ungkapan.', 'medium', 'mencocokkan', c1)
    p.group(tp_pakai, 'Kelompokkan situasi berikut berdasarkan ungkapan yang tepat: lewat di depan orang; meminjam pensil; menumpahkan air; menerima hadiah.',
            {'permisi': ['lewat di depan orang'], 'tolong': ['meminjam pensil'], 'maaf': ['menumpahkan air'], 'terima kasih': ['menerima hadiah']}, 'Situasi dan ungkapan.', 'medium', 'mengelompokkan', c2)


def bilangan(p, tp):
    comp = 'Menulis dan menyebutkan bilangan satu sampai sepuluh'
    A = bi_misc.ANGKA
    for i, name in enumerate(A, 1):
        p.gk = f'bl{i}'
        wr = [str(x) for x in range(1, 11) if x != i]
        wn = [x for x in A if x != name]
        p.mc(tp, f'Angka {i} dibaca ....', name, wn, f'{i} dibaca {name}.', 'easy', 'mengenali', comp)
        p.mc(tp, f'Bilangan "{name}" ditulis dengan angka ....', str(i), wr, f'{name} ditulis {i}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Angka {i} dibaca {name}.', True, f'Benar, {i} = {name}.', 'easy', 'mengenali', comp)
        p.tf(tp, f'Angka {i} dibaca {wn[i % len(wn)]}.', False, f'Salah, {i} = {name}.', 'easy', 'mengenali', comp)
        p.fill(tp, f'Isilah: Angka {i} ditulis dengan huruf ....', name, f'{i} = {name}.', 'easy', 'mengenali', comp)
        p.fill(tp, f'Isilah: Bilangan "{name}" ditulis dengan angka ....', str(i), f'{name} = {i}.', 'easy', 'mengenali', comp)
        ob, desc = bi_misc.OBJEK[i - 1]
        p.mc(tp, f'Perhatikan gambar kartu hitung nomor {i}! Berapa banyak benda pada gambar?', name, wn, f'Pada gambar ada {i} {ob}.', 'easy', 'menerapkan', comp,
             visual=f'Kartu hitung menampilkan {i} {desc} tersusun rapi dalam satu baris.')
        if i < 10:
            p.mc(tp, f'Bilangan setelah {name} adalah ....', A[i], [x for x in A if x != A[i] and x != name][:5], f'Setelah {i} adalah {i+1} ({A[i]}).', 'medium', 'mengingat', comp)
        if i > 1:
            p.mc(tp, f'Bilangan sebelum {name} adalah ....', A[i - 2], [x for x in A if x != A[i - 2] and x != name][:5], f'Sebelum {i} adalah {i-1} ({A[i-2]}).', 'medium', 'mengingat', comp)
    p.gk = None
    for s in range(0, 7):
        seg = A[s:s + 4]
        p.order(tp, 'Urutkan bilangan berikut dari yang terkecil!', seg, 'Urutan dari kecil ke besar: ' + ', '.join(seg) + '.', 'medium', 'mengurutkan', comp)
    for s in range(0, 7, 2):
        p.match(tp, 'Jodohkan angka dengan tulisannya!', [(str(i + 1), A[i]) for i in range(s, s + 4)], 'Setiap angka ditulis dengan huruf.', 'medium', 'mencocokkan', comp)
    p.perf(tp, 'Hitunglah benda di kelasmu satu sampai sepuluh lalu sebutkan dengan lantang!', R, 'Murid menyebut bilangan.', 'easy', 'menerapkan', comp)
    p.perf(tp, 'Tulislah angka 1 sampai 10 beserta tulisan hurufnya dengan rapi!', R, 'Murid menulis bilangan.', 'medium', 'menerapkan', comp)


def arti_kata(p, tp):
    comp = 'Menulis arti kata baru'
    AR = bi_misc.ARTI
    for i, (k, a, kal) in enumerate(AR):
        p.gk = f'ak{i}'
        oa = [x[1] for j, x in enumerate(AR) if j != i]
        ok_ = [x[0] for j, x in enumerate(AR) if j != i]
        p.mc(tp, f'Kata "{k}" artinya ....', a, oa, f'{k} berarti {a}.', 'medium', 'memahami', comp)
        p.mc(tp, f'Kata yang artinya "{a}" adalah ....', k, ok_, f'{a} = {k}.', 'medium', 'memahami', comp)
        p.tf(tp, f'Kata "{k}" artinya {a}.', True, f'Benar, {k} = {a}.', 'easy', 'memahami', comp)
        p.tf(tp, f'Kata "{k}" artinya {oa[i % len(oa)]}.', False, f'Salah, {k} = {a}.', 'medium', 'memahami', comp)
        p.fill(tp, f'Isilah: Arti kata "{k}" adalah ....', a, f'{k} berarti {a}.', 'medium', 'memahami', comp)
        p.ctx(tp, f'Dalam kalimat "{kal}" kata "{k}" berarti ....', a, oa, f'{k} berarti {a}.', 'medium', 'menerapkan', comp)
    p.gk = None
    for s in range(0, len(AR) - 3, 3):
        p.match(tp, 'Jodohkan kata dengan artinya!', [(x[0], x[1]) for x in AR[s:s + 4]], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', comp)


def letak(p, tp_baca, tp_ceritakan, tp_tulis):
    c1 = 'Membaca kata letak dan pekerjaan'
    c3 = 'Menceritakan letak benda dan arah'
    LET = ['di atas', 'di bawah', 'di dalam', 'di luar', 'di depan', 'di belakang', 'di samping']
    for i, (k, ok, d) in enumerate(bi_misc.LETAK):
        p.gk = f'lk{i}'
        o = [x for x in LET if x != ok]
        full = k.replace('...', ok)
        p.mc(tp_ceritakan, f'Perhatikan gambar nomor {i + 1} pada kartu letak! Lengkapi kalimat: {k}', ok, o, f'Kalimat: {full}', 'medium', 'menerapkan', c3,
             visual=d)
        p.tf(tp_baca, f'Kalimat "{full}" sesuai dengan letak benda yang digambarkan.', True, f'Kalimat tepat: {full}', 'easy', 'mengenali', c1)
        p.tf(tp_baca, f'Kalimat "{k.replace("...", o[i % len(o)])}" sesuai dengan letak benda yang digambarkan.', False, f'Kalimat tepat: {full}', 'medium', 'mengenali', c1)
        p.fill(tp_tulis, f'Tulislah kata letak yang tepat: {k}', ok, f'Kalimat: {full}', 'easy', 'menerapkan', 'Menulis kata letak', typ='completion')
    p.gk = None
    for i, (q, ok, bad) in enumerate(bi_misc.ARAH):
        p.gk = f'ar{i}'
        p.ctx(tp_ceritakan, q, ok, bad, f'Jawaban: {ok}.', 'medium', 'menerapkan', c3)
        p.fill(tp_ceritakan, 'Isilah: ' + q, ok, f'Jawaban: {ok}.', 'medium', 'menerapkan', c3)
    p.gk = None
    P = bi_misc.PEKERJAAN
    for i, (n, tugas, d) in enumerate(P):
        p.gk = f'pk{n}'
        on = [x[0] for j, x in enumerate(P) if j != i]
        ot = [x[1] for j, x in enumerate(P) if j != i]
        p.mc(tp_baca, f'Pekerjaan yang {tugas} disebut ....', n, on, f'{n} {tugas}.', 'easy', 'mengenali', c1)
        p.mc(tp_baca, f'Seorang {n} bertugas ....', tugas, ot, f'{n} {tugas}.', 'medium', 'memahami', c1)
        p.tf(tp_baca, f'Seorang {n} bertugas {tugas}.', True, f'Benar, {n} {tugas}.', 'easy', 'memahami', c1)
        p.tf(tp_baca, f'Seorang {n} bertugas {ot[i % len(ot)]}.', False, f'Salah, {n} {tugas}.', 'medium', 'memahami', c1)
        p.fill(tp_tulis, f'Tuliskan nama pekerjaan yang {tugas}: ....', n, f'{n} {tugas}.', 'medium', 'mengenali', 'Menulis kata pekerjaan')
        p.mc(tp_baca, f'Perhatikan gambar profesi nomor {i + 1}! Pekerjaan pada gambar adalah ....', n, on, f'Gambar menunjukkan {n}.', 'easy', 'mengenali', c1, visual=d)
    p.gk = None
    p.match(tp_baca, 'Jodohkan pekerjaan dengan tugasnya!', [(x[0], x[1]) for x in P[:4]], 'Tugas pekerjaan.', 'medium', 'mencocokkan', c1)
    p.match(tp_baca, 'Jodohkan pekerjaan dengan tugasnya!', [(x[0], x[1]) for x in P[4:8]], 'Tugas pekerjaan.', 'medium', 'mencocokkan', c1)
    p.match(tp_baca, 'Jodohkan pekerjaan dengan tugasnya!', [(x[0], x[1]) for x in P[8:12]], 'Tugas pekerjaan.', 'medium', 'mencocokkan', c1)
    p.perf(tp_ceritakan, 'Ceritakan letak benda-benda di mejamu menggunakan kata di atas, di bawah, dan di samping!', R, 'Murid menceritakan letak benda.', 'medium', 'menerapkan', c3)
    p.perf(tp_ceritakan, 'Tunjukkan arah ke masjid dari kelasmu kepada temanmu!', R, 'Murid menunjukkan arah.', 'medium', 'menerapkan', c3)
    p.perf(tp_baca, 'Bacalah lima nama pekerjaan di sekitarmu dengan lafal yang jelas!', R, 'Murid membaca kata pekerjaan.', 'easy', 'menerapkan', c1)


def stories(p, key, tp_detail, tp_retell):
    judul, teks, qs, ev, (pm, pw) = bi_misc.CERITA[key]
    comp_d = 'Menyimak cerita'
    comp_r = 'Menceritakan kembali cerita'
    for qi, (q, ok, bad) in enumerate(qs):
        p.gk = f'st{key}{qi}'
        p.ctx(tp_detail, f'Simaklah cerita "{judul}": {teks} {q}', ok, bad, f'Jawaban berdasarkan cerita: {ok}.', 'medium', 'memahami', comp_d)
        p.tf(tp_detail, f'Dalam cerita "{judul}", jawaban dari "{q}" adalah {ok}.', True, f'Sesuai cerita: {ok}.', 'easy', 'memahami', comp_d)
        p.tf(tp_detail, f'Dalam cerita "{judul}", jawaban dari "{q}" adalah {bad[0]}.', False, f'Sesuai cerita: {ok}.', 'medium', 'memahami', comp_d)
        p.fill(tp_detail, f'Isilah menurut cerita "{judul}": {q}', ok, f'Jawaban: {ok}.', 'medium', 'memahami', comp_d)
    p.gk = f'st2{key}'
    p.order(tp_retell, f'Urutkan kejadian dalam cerita "{judul}" dengan benar!', ev, 'Urutan kejadian: ' + ' → '.join(ev) + '.', 'medium', 'mengurutkan', comp_r)
    p.ctx(tp_retell, f'Setelah menyimak cerita "{judul}", pesan yang dapat kita ambil adalah ....', pm, pw, f'Pesan cerita: {pm}.', 'medium', 'menyimpulkan', comp_r)
    p.ctx(tp_retell, f'Kejadian pertama dalam cerita "{judul}" adalah ....', ev[0], ev[1:4] if len(ev) >= 4 else ev[1:] + ['Tidak terjadi apa-apa'], f'Kejadian pertama: {ev[0]}.', 'easy', 'mengingat', comp_r)
    p.ctx(tp_retell, f'Kejadian terakhir dalam cerita "{judul}" adalah ....', ev[-1], ev[:-1][:3] if len(ev) >= 4 else ev[:-1] + ['Tidak terjadi apa-apa'], f'Kejadian terakhir: {ev[-1]}.', 'easy', 'mengingat', comp_r)
    p.perf(tp_retell, f'Ceritakan kembali cerita "{judul}" dengan bahasamu sendiri secara berurutan!', 'Dinilai guru: urutan cerita, kejelasan bahasa, dan kepercayaan diri (skala 1-4).', 'Murid menceritakan kembali.', 'medium', 'menerapkan', comp_r)
    for i in range(len(ev) - 1):
        p.gk = f'st3{key}{i}'
        others = [e for j, e in enumerate(ev) if j != i + 1] + ['Semua tokoh pulang ke rumah']
        p.ctx(tp_retell, f'Dalam cerita "{judul}", setelah "{ev[i]}", kejadian berikutnya adalah ....', ev[i + 1], others, f'Urutan: {ev[i]} → {ev[i + 1]}.', 'medium', 'mengurutkan', comp_r)
        p.tf(tp_retell, f'Dalam cerita "{judul}", "{ev[i + 1]}" terjadi setelah "{ev[i]}".', True, f'Urutan: {ev[i]} → {ev[i + 1]}.', 'easy', 'mengurutkan', comp_r)
        p.tf(tp_retell, f'Dalam cerita "{judul}", "{ev[i]}" terjadi setelah "{ev[i + 1]}".', False, f'Yang benar: {ev[i]} → {ev[i + 1]}.', 'medium', 'mengurutkan', comp_r)
    p.gk = None
