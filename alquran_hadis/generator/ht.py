# -*- coding: utf-8 -*-
"""Materi: Mengenal Huruf Hijaiah secara Terpisah dan Tersambung (HT)."""
import random
import lib
from hijaiah import L, CH, NAME, AMB, IDX

TAT = 'ـ'
NONCON = ['ا', 'د', 'ذ', 'ر', 'ز', 'و']          # tidak dapat disambung dengan huruf sesudahnya
CON = [c for c in CH if c not in NONCON]
NC2 = NONCON + ['ء']                                # ء (hamzah) juga tidak menyambung


def forms(c):
    iso = c
    if c in NONCON:
        return dict(terpisah=iso, awal=iso, tengah=TAT + c, akhir=TAT + c)
    return dict(terpisah=iso, awal=c + TAT, tengah=TAT + c + TAT, akhir=TAT + c)


def form_in_word(letters, i):
    c = letters[i]
    prev = i > 0 and letters[i - 1] not in NC2
    nxt = i < len(letters) - 1 and c not in NC2
    if prev and nxt: return 'tengah'
    if nxt: return 'awal'
    if prev: return 'akhir'
    return 'terpisah'


WORDS = [('باب', 'bab', 'pintu'), ('كتاب', 'kitab', 'buku'), ('قلم', 'qalam', 'pena'), ('بيت', 'bait', 'rumah'), ('شمس', 'syams', 'matahari'),
         ('قمر', 'qamar', 'bulan'), ('ماء', "ma'", 'air'), ('ولد', 'walad', 'anak laki-laki'), ('بنت', 'bint', 'anak perempuan'), ('نور', 'nur', 'cahaya'),
         ('جمل', 'jamal', 'unta'), ('سمك', 'samak', 'ikan'), ('تمر', 'tamr', 'kurma'), ('ورد', 'ward', 'bunga mawar'), ('مسجد', 'masjid', 'masjid'),
         ('سماء', "sama'", 'langit'), ('كلب', 'kalb', 'anjing'), ('فيل', 'fil', 'gajah'), ('يد', 'yad', 'tangan'), ('عين', "'ain", 'mata'),
         ('لبن', 'laban', 'susu'), ('ملح', 'milh', 'garam'), ('رجل', 'rajul', 'laki-laki dewasa'), ('بحر', 'bahr', 'laut'), ('نهر', 'nahr', 'sungai'),
         ('جبل', 'jabal', 'gunung'), ('ورق', 'waraq', 'kertas'), ('كرسي', 'kursi', 'kursi'), ('مفتاح', 'miftah', 'kunci'), ('خبز', 'khubz', 'roti')]


def variants(word):
    """Penulisan keliru untuk sebuah kata: terpisah semua, putus di awal, putus di akhir, tukar urutan."""
    ls = list(word)
    out = []
    out.append(' '.join(ls))
    joins = [i for i in range(len(ls) - 1) if ls[i] not in NC2]
    if joins:
        a = joins[0]; out.append(''.join(ls[:a + 1]) + ' ' + ''.join(ls[a + 1:]))
        b = joins[-1]; out.append(''.join(ls[:b + 1]) + ' ' + ''.join(ls[b + 1:]))
    if len(ls) >= 3:
        t = ls[:]; t[0], t[1] = t[1], t[0]; out.append(''.join(t))
    out += [''.join(reversed(ls)), ' '.join(reversed(ls))]
    return [v for v in dict.fromkeys(out) if v != word]


def build(seed=11):
    rng = random.Random(seed)
    tps = ['Murid mampu mengenal huruf hijaiah secara terpisah dan tersambung dengan benar.',
           'Murid mampu merangkaikan huruf hijaiah secara terpisah dan tersambung dengan benar.',
           'Murid mampu menyesuaikan penulisan huruf hijaiah dengan benar.',
           'Murid mampu mempraktikkan penulisan huruf hijaiah secara terpisah dan tersambung dengan benar sebagai wujud cinta Allah dan Rasul-Nya, serta cinta Ilmu.']
    p = lib.Pool('HT', 'Mengenal Huruf Hijaiah secara Terpisah dan Tersambung', tps, 143, tpw=(35, 35, 35, 38))
    POS = ['terpisah', 'awal', 'tengah', 'akhir']
    POSN = {'terpisah': 'berdiri sendiri (terpisah)', 'awal': 'awal kata', 'tengah': 'tengah kata', 'akhir': 'akhir kata'}

    # ================= TP1 =================
    p.mc(1, 'Huruf hijaiah yang berdiri sendiri tanpa menyambung dengan huruf lain disebut huruf ....', 'terpisah', ['tersambung', 'bertasydid', 'bertanwin'], 'Huruf yang berdiri sendiri disebut huruf terpisah.', 'easy', 'mengingat', 'Mengenal huruf terpisah')
    p.mc(1, 'Huruf hijaiah yang disambung dengan huruf lain dalam satu kata disebut huruf ....', 'tersambung', ['terpisah', 'bersukun', 'mati'], 'Huruf yang disambung dalam kata disebut huruf tersambung.', 'easy', 'mengingat', 'Mengenal huruf tersambung')
    p.tf(1, 'Huruf hijaiah dapat ditulis terpisah maupun tersambung.', True, 'Benar, huruf hijaiah memiliki bentuk terpisah dan tersambung.', 'easy', 'mengingat', 'Mengenal huruf terpisah')
    p.tf(1, 'Semua huruf hijaiah dapat disambung dengan huruf sesudahnya.', False, 'Salah. Ada 6 huruf yang tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'memahami', 'Mengenal huruf tersambung')
    p.mc(1, 'Jumlah huruf hijaiah yang tidak dapat disambung dengan huruf sesudahnya adalah ....', '6', ['4', '5', '7', '8'], 'Huruf tersebut: ا د ذ ر ز و.', 'medium', 'mengingat', 'Mengenal huruf tersambung')
    p.fill(1, 'Huruf yang tidak dapat disambung dengan huruf sesudahnya ada .... huruf.', '6', 'Ada enam huruf: ا د ذ ر ز و.', 'medium', 'mengingat', 'Mengenal huruf tersambung')
    p.fill(1, 'Enam huruf yang tidak dapat disambung dengan huruf sesudahnya adalah ا، د، ذ، ر، ز، dan ....', 'و', 'Hurufnya: ا د ذ ر ز و.', 'hard', 'mengingat', 'Mengenal huruf tersambung', typ='completion')
    p.group(1, 'Kelompokkan huruf berikut: ا، ب، د، ت، ر، ج، و، م.', {'dapat disambung': ['ب', 'ت', 'ج', 'م'], 'tidak dapat disambung': ['ا', 'د', 'ر', 'و']}, 'Huruf ا د ذ ر ز و tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'mengelompokkan', 'Mengenal huruf tersambung')
    p.group(1, 'Kelompokkan huruf berikut: ذ، ز، س، ش، ك، ل، ن، ي.', {'dapat disambung': ['س', 'ش', 'ك', 'ل', 'ن', 'ي'], 'tidak dapat disambung': ['ذ', 'ز']}, 'ذ dan ز tidak dapat disambung.', 'medium', 'mengelompokkan', 'Mengenal huruf tersambung')
    p.mc(1, 'Huruf hijaiah dapat berubah bentuk menurut letaknya, yaitu di ....', 'awal, tengah, dan akhir kata', ['tepi buku saja', 'kanan kertas saja', 'atas tulisan saja'], 'Bentuk huruf bergantung pada letaknya dalam kata.', 'medium', 'memahami', 'Mengenal huruf tersambung')
    for c in CH:
        nm = NAME[c]
        con = c not in NONCON
        p.tf(1, f'Huruf {c} {"dapat" if con else "tidak dapat"} disambung dengan huruf sesudahnya.', True, f'Benar. {c} ({nm}) {"dapat" if con else "tidak dapat"} disambung dengan huruf sesudahnya.', 'easy' if not con else 'medium', 'mengenali', 'Mengenal huruf tersambung')
        p.tf(1, f'Huruf {c} {"tidak dapat" if con else "dapat"} disambung dengan huruf sesudahnya.', False, f'Salah. {c} ({nm}) {"dapat" if con else "tidak dapat"} disambung dengan huruf sesudahnya.', 'medium', 'mengenali', 'Mengenal huruf tersambung')
        p.mc(1, f'Huruf {c} {"dapat" if con else "tidak dapat"} disambung dengan huruf sesudahnya. Hal ini berarti huruf {c} ....', 'dapat disambung' if con else 'tidak dapat disambung', ['dapat disambung', 'tidak dapat disambung', 'hanya bisa di akhir kata', 'hanya bisa di awal kata'] if True else [],
             f'{c} {"dapat" if con else "tidak dapat"} disambung.', 'easy', 'memahami', 'Mengenal huruf tersambung') if False else None
    for c in NONCON:
        p.mc(1, f'Huruf berikut yang tidak dapat disambung dengan huruf sesudahnya adalah ....' if c == 'ا' else f'Huruf {c} termasuk kelompok huruf ....', c if c == 'ا' else 'yang tidak dapat disambung dengan huruf sesudahnya',
             [x for x in CON][:3] if c == 'ا' else ['yang dapat disambung ke kedua arah', 'yang selalu ditulis di awal kata', 'yang hanya berupa tanda baca'],
             f'{c} termasuk 6 huruf yang tidak disambung ke huruf sesudahnya.', 'medium', 'mengenali', 'Mengenal huruf tersambung')
    for c in CON:
        p.gk = f'f1{c}'
        f = forms(c); nm = NAME[c]
        for pos in ('awal', 'tengah', 'akhir'):
            others = [f[x] for x in POS if x != pos]
            p.mc(1, f'Bentuk huruf {nm} ({c}) di {POSN[pos]} adalah ....', f[pos], others, f'Bentuk {nm} di {POSN[pos]}: {f[pos]}.', 'medium', 'mengenali', 'Mengenal bentuk huruf tersambung')
            p.mc(1, f'Bentuk {f[pos]} adalah huruf {nm} yang ditulis di ....', POSN[pos], [POSN[x] for x in POS if x != pos], f'{f[pos]} adalah {nm} di {POSN[pos]}.', 'medium', 'mengenali', 'Mengenal bentuk huruf tersambung',
                 visual=f'Kartu besar bertuliskan {f[pos]} dengan panah tulisan {nm}, latar kuning muda.') if pos != 'terpisah' else None
            p.tf(1, f'Huruf {nm} di {POSN[pos]} berbentuk {f[pos]}.', True, f'Benar, {nm} di {POSN[pos]} ditulis {f[pos]}.', 'easy', 'mengenali', 'Mengenal bentuk huruf tersambung')
            wrongpos = POS[(POS.index(pos) + 1) % 4]
            if wrongpos == pos: wrongpos = 'terpisah'
            p.tf(1, f'Huruf {nm} di {POSN[pos]} berbentuk {f[wrongpos]}.', False, f'Salah. {nm} di {POSN[pos]} ditulis {f[pos]}.', 'medium', 'mengenali', 'Mengenal bentuk huruf tersambung')
        p.mc(1, f'Bentuk terpisah huruf {nm} adalah ....', c, [f[x] for x in ('awal', 'tengah', 'akhir')], f'Bentuk terpisah {nm}: {c}.', 'easy', 'mengenali', 'Mengenal huruf terpisah')
    for c in NONCON:
        f = forms(c); nm = NAME[c]
        p.mc(1, f'Bentuk huruf {nm} ({c}) di akhir kata, setelah huruf yang dapat disambung, adalah ....', f['akhir'], [f['terpisah'], CH[(IDX[c] + 2) % 28] + TAT, TAT + CH[(IDX[c] + 2) % 28]],
             f'Setelah huruf yang dapat disambung, {nm} ditulis {f["akhir"]}.', 'hard', 'mengenali', 'Mengenal huruf tersambung')
        p.tf(1, f'Bentuk huruf {nm} di awal kata sama dengan bentuk terpisahnya ({c}).', True, f'Benar, {nm} tidak menyambung ke huruf sesudahnya sehingga di awal kata bentuknya sama dengan terpisah.', 'hard', 'memahami', 'Mengenal huruf tersambung')
    for (w, lat, arti) in WORDS[:12]:
        ls = list(w)
        p.mc(1, f'Kata {w} terdiri atas ... huruf.', str(len(ls)), [str(x) for x in range(2, 7) if x != len(ls)], f'{w} ({arti}) terdiri atas {len(ls)} huruf: {" ".join(ls)}.', 'easy', 'mengingat', 'Mengenal huruf tersambung')
        p.fill(1, f'Kata {w} ({arti}) tersusun dari .... huruf.', str(len(ls)), f'{w} = {" + ".join(ls)}.', 'easy', 'mengingat', 'Mengenal huruf tersambung')
    p.match(1, 'Jodohkan bentuk huruf dengan letaknya!', [(forms('ب')['awal'], 'awal kata'), (forms('ب')['tengah'], 'tengah kata'), (forms('ب')['akhir'], 'akhir kata'), ('ب', 'terpisah')], 'Setiap bentuk memiliki letaknya sendiri.', 'medium', 'mencocokkan', 'Mengenal bentuk huruf tersambung')
    p.match(1, 'Jodohkan bentuk huruf dengan letaknya!', [(forms('م')['awal'], 'awal kata'), (forms('م')['tengah'], 'tengah kata'), (forms('م')['akhir'], 'akhir kata'), ('م', 'terpisah')], 'Setiap bentuk memiliki letaknya sendiri.', 'medium', 'mencocokkan', 'Mengenal bentuk huruf tersambung')
    p.match(1, 'Jodohkan bentuk huruf dengan letaknya!', [(forms('س')['awal'], 'awal kata'), (forms('س')['tengah'], 'tengah kata'), (forms('س')['akhir'], 'akhir kata'), ('س', 'terpisah')], 'Setiap bentuk memiliki letaknya sendiri.', 'medium', 'mencocokkan', 'Mengenal bentuk huruf tersambung')

    # ================= TP2: merangkaikan =================
    for (w, lat, arti) in WORDS:
        p.gk = f'w2{lat}'
        ls = list(w); sep = ' + '.join(ls)
        vs = variants(w)
        if len(vs) < 3:
            vs = vs + [ls[-1] + ''.join(ls[:-1])] + [''.join(reversed(ls))]
            vs = [v for v in dict.fromkeys(vs) if v != w]
        p.mc(2, f'Huruf terpisah {sep} jika dirangkaikan menjadi kata ....', w, vs, f'{sep} = {w} ({lat}), artinya {arti}.', 'medium', 'menerapkan', 'Merangkaikan huruf')
        p.mc(2, f'Kata "{arti}" dalam bahasa Arab ditulis ....', w, [x[0] for x in WORDS if x[0] != w][:6], f'"{arti}" ditulis {w} ({lat}).', 'medium', 'mengenali', 'Merangkaikan huruf')
        p.tf(2, f'{sep} dirangkaikan menjadi {w}.', True, f'Benar, {sep} = {w}.', 'easy', 'menerapkan', 'Merangkaikan huruf')
        p.tf(2, f'{sep} dirangkaikan menjadi {vs[-1]}.', False, f'Salah. Rangkaian yang benar adalah {w}.', 'medium', 'menerapkan', 'Merangkaikan huruf')
        p.fill(2, f'Rangkailah huruf {sep} menjadi satu kata: ....', w, f'{sep} = {w}.', 'medium', 'menerapkan', 'Merangkaikan huruf')
        p.fill(2, f'Kata {w} jika dipisah menjadi huruf-huruf: ....', ' + '.join(ls), f'{w} = {sep}.', 'medium', 'menerapkan', 'Memisahkan huruf')
        sh = ls[:]
        while sh == ls and len(ls) > 1:
            rng.shuffle(sh)
        if len(ls) >= 3:
            p.order(2, f'Susun huruf berikut menjadi kata "{arti}" ({lat})!', ls, f'Urutan huruf: {" + ".join(ls)} = {w}.', 'medium', 'mengurutkan', 'Merangkaikan huruf')
        p.mc(2, f'Huruf pertama pada kata {w} adalah ....', ls[0], [x for x in CH if x != ls[0]], f'Huruf pertama {w} adalah {ls[0]}.', 'easy', 'mengenali', 'Merangkaikan huruf')
        p.mc(2, f'Huruf terakhir pada kata {w} adalah ....', ls[-1], [x for x in CH if x != ls[-1]], f'Huruf terakhir {w} adalah {ls[-1]}.', 'easy', 'mengenali', 'Merangkaikan huruf')
        p.mc(2, f'Kata {w} dibaca dan berarti ....', f'{lat} = {arti}', [f'{x[1]} = {x[2]}' for x in WORDS if x[0] != w][:6], f'{w} dibaca {lat} yang berarti {arti}.', 'medium', 'memahami', 'Merangkaikan huruf')
    for s in range(0, 28, 4):
        sel = WORDS[s:s + 4]
        p.match(2, 'Jodohkan kata Arab dengan artinya!', [(w, a) for (w, l, a) in sel], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Merangkaikan huruf')
        p.match(2, 'Jodohkan huruf-huruf terpisah dengan kata yang dirangkainya!', [(' + '.join(list(w)), w) for (w, l, a) in sel], 'Rangkaian huruf menghasilkan kata.', 'medium', 'mencocokkan', 'Merangkaikan huruf')
    p.group(2, 'Kelompokkan kata berikut berdasarkan jumlah hurufnya: باب، ماء، كتاب، مسجد، قلم، مفتاح.', {'3 huruf': ['باب', 'ماء', 'قلم'], 'lebih dari 3 huruf': ['كتاب', 'مسجد', 'مفتاح']}, 'Hitung huruf pada tiap kata.', 'medium', 'mengelompokkan', 'Merangkaikan huruf')
    p.perf(2, 'Rangkaikan huruf ب + ي + ت menjadi satu kata dan bacalah di depan guru!', 'Dinilai guru: kebenaran rangkaian dan bacaan "bait" (skala 1-4).', 'Murid merangkai huruf menjadi kata.', 'medium', 'menerapkan', 'Merangkaikan huruf')
    p.perf(2, 'Susun kartu huruf menjadi kata كتاب bersama teman, lalu sebutkan hurufnya satu per satu!', 'Dinilai guru: ketepatan susunan dan penyebutan huruf (skala 1-4).', 'Murid menyusun huruf menjadi kata.', 'medium', 'menerapkan', 'Merangkaikan huruf')

    # ================= TP3: menyesuaikan penulisan =================
    for (w, lat, arti) in WORDS:
        p.gk = f'w3{lat}'
        ls = list(w)
        vs = variants(w)
        if len(vs) < 3:
            vs = vs + [''.join(reversed(ls))]
            vs = [v for v in dict.fromkeys(vs) if v != w]
        p.mc(3, f'Penulisan kata "{arti}" ({lat}) yang tersambung dengan benar adalah ....', w, vs, f'Penulisan benar: {w}. Huruf yang dapat disambung ditulis bersambung.', 'hard', 'menganalisis', 'Menyesuaikan penulisan huruf')
        p.tf(3, f'Penulisan "{w}" untuk kata {lat} ({arti}) sudah benar.', True, f'Benar, {w} adalah penulisan yang tepat.', 'easy', 'menganalisis', 'Menyesuaikan penulisan huruf')
        p.tf(3, f'Penulisan "{vs[0]}" untuk kata {lat} ({arti}) sudah benar.', False, f'Salah. Penulisan yang benar adalah {w}.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
        cuts = [ls[i] for i in range(len(ls) - 1) if ls[i] in NC2]
        if len(cuts) == 1:
            p.mc(3, f'Dalam kata {w}, huruf yang tidak tersambung dengan huruf sesudahnya adalah ....', cuts[0], [x for x in CON if x in ls][:3] + [x for x in CON if x not in ls][:3], f'{cuts[0]} tidak menyambung ke huruf sesudahnya.', 'hard', 'menganalisis', 'Menyesuaikan penulisan huruf')
            p.fill(3, f'Huruf pada kata {w} yang tidak tersambung dengan huruf sesudahnya adalah ....', cuts[0], f'{cuts[0]} termasuk huruf yang tidak disambung.', 'hard', 'menganalisis', 'Menyesuaikan penulisan huruf')
        if len(cuts) == 0 and len(ls) >= 3:
            p.tf(3, f'Semua huruf pada kata {w} tersambung dengan huruf sesudahnya.', True, f'Benar, pada {w} tidak ada huruf yang tidak dapat disambung kecuali huruf terakhir.', 'hard', 'menganalisis', 'Menyesuaikan penulisan huruf') if all(c not in NC2 for c in ls[:-1]) else None
        for i, c in enumerate(ls):
            if c not in NAME or c in NONCON or ls.count(c) > 1:
                continue
            pos = form_in_word(ls, i)
            f = forms(c)
            if len(set(f.values())) < 4:
                continue
            p.mc(3, f'Pada kata {w}, huruf {NAME[c]} ({c}) ditulis dalam bentuk ....', f[pos], [f[x] for x in POS if x != pos], f'Pada {w}, {c} berada di {POSN[pos]}, sehingga ditulis {f[pos]}.', 'hard', 'menganalisis', 'Menyesuaikan penulisan huruf')
            p.tf(3, f'Pada kata {w}, huruf {NAME[c]} ditulis di {POSN[pos]}.', True, f'Benar, {c} berada di {POSN[pos]} pada kata {w}.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
            wp = [x for x in ('awal', 'tengah', 'akhir') if x != pos][0]
            p.tf(3, f'Pada kata {w}, huruf {NAME[c]} ditulis di {POSN[wp]}.', False, f'Salah. {c} berada di {POSN[pos]}.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.mc(3, 'Jika huruf ا berada di tengah kata, huruf sesudahnya ....', 'tidak tersambung dengan alif', ['selalu tersambung dengan alif', 'dihilangkan', 'ditulis dua kali'], 'Alif tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.mc(3, 'Sesudah huruf د, huruf berikutnya dalam satu kata ....', 'ditulis terpisah dari د', ['ditulis menyambung dengan د', 'ditulis di atas د', 'dilewati'], 'Dal tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.tf(3, 'Dalam kata بيت, huruf ب dan ي tersambung, begitu juga ي dan ت.', True, 'Benar, ب dan ي dapat disambung.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.tf(3, 'Dalam kata ورد, huruf و tersambung dengan ر.', False, 'Salah. و tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.tf(3, 'Dalam kata ورد, huruf ر tersambung dengan د.', False, 'Salah. ر tidak dapat disambung dengan huruf sesudahnya.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')
    p.perf(3, 'Perbaiki tulisan "ك ت ا ب" menjadi kata yang tersambung dengan benar di papan tulis!', 'Dinilai guru: ketepatan menyambung huruf (skala 1-4).', 'Murid membetulkan penulisan kata.', 'medium', 'menganalisis', 'Menyesuaikan penulisan huruf')

    # ================= TP4: praktik penulisan =================
    p.mc(4, 'Tulisan huruf hijaiah dimulai dari arah ....', 'kanan', ['kiri', 'bawah', 'tengah'], 'Menulis huruf Arab dimulai dari kanan ke kiri.', 'easy', 'mengingat', 'Mempraktikkan penulisan')
    p.tf(4, 'Saat menulis kata Arab, tangan bergerak dari kanan ke kiri.', True, 'Tulisan Arab ditulis dari kanan ke kiri.', 'easy', 'mengingat', 'Mempraktikkan penulisan')
    p.tf(4, 'Saat menulis kata Arab, tangan bergerak dari kiri ke kanan.', False, 'Tulisan Arab ditulis dari kanan ke kiri.', 'easy', 'mengingat', 'Mempraktikkan penulisan')
    p.mc(4, 'Titik huruf hijaiah sebaiknya ditulis ....', 'setelah badan huruf selesai ditulis', ['sebelum menulis huruf', 'di tempat mana saja', 'tidak perlu ditulis'], 'Titik ditulis setelah bentuk huruf selesai.', 'medium', 'memahami', 'Mempraktikkan penulisan')
    p.order(4, 'Urutkan langkah menulis huruf ب berikut!', ['Siapkan pensil dan buku tulis', 'Tulis badan huruf dari kanan ke kiri', 'Tulis satu titik di bawah huruf', 'Periksa kerapian tulisan'], 'Setelah badan huruf selesai, titik ditambahkan.', 'medium', 'mengurutkan', 'Mempraktikkan penulisan')
    p.order(4, 'Urutkan langkah menulis kata بيت berikut!', ['Tulis ب dengan titik di bawah', 'Sambungkan ke ي', 'Tulis dua titik di bawah ي', 'Sambungkan ke ت dan beri dua titik di atas'], 'Huruf ditulis berurutan dari kanan ke kiri.', 'hard', 'mengurutkan', 'Mempraktikkan penulisan')
    p.order(4, 'Urutkan persiapan sebelum menulis huruf hijaiah berikut!', ['Duduk dengan tegak', 'Menyiapkan alat tulis', 'Berdoa sebelum belajar', 'Mulai menulis dengan rapi'], 'Persiapan yang baik membuat tulisan rapi.', 'easy', 'mengurutkan', 'Mempraktikkan penulisan')
    p.ctx(4, 'Maya menulis kata بيت tetapi menulis ب ي ت dengan jarak terpisah. Gurunya meminta Maya ....', 'menyambung huruf-huruf itu menjadi بيت', ['menghapus semua tulisan', 'menulisnya dari kiri ke kanan', 'menambahkan titik sebanyak mungkin'], 'Huruf ب ي ت dapat disambung menjadi بيت.', 'medium', 'menerapkan', 'Mempraktikkan penulisan')
    p.ctx(4, 'Hanif menulis kata باب. Setelah menulis alif, ia mengangkat pensil lalu menulis ب terakhir secara terpisah. Hal itu karena ....', 'alif tidak dapat disambung dengan huruf sesudahnya', ['Hanif lelah', 'ب tidak punya bentuk akhir', 'pensilnya tumpul'], 'Alif tidak menyambung ke huruf sesudahnya.', 'hard', 'menerapkan', 'Mempraktikkan penulisan')
    p.ctx(4, 'Ustazah memberi tugas menulis nama Allah ( الله ) dengan rapi. Sikap yang tepat adalah ....', 'menulis perlahan dan rapi karena cinta kepada Allah', ['menulis cepat tanpa melihat', 'mencoret-coret buku', 'menyuruh teman menulisnya'], 'Menulis dengan rapi menunjukkan cinta Allah dan ilmu.', 'easy', 'menerapkan', 'Menerapkan cinta ilmu')
    p.ctx(4, 'Farhan sering salah menyambung huruf. Cara belajar yang tepat adalah ....', 'berlatih menulis berulang-ulang dan meminta contoh guru', ['berhenti berlatih', 'menyalin tulisan teman tanpa belajar', 'menulis asal-asalan'], 'Latihan berulang membuat tulisan makin benar.', 'easy', 'menerapkan', 'Menerapkan cinta ilmu')
    p.mc(4, 'Perhatikan gambar! Seorang anak menulis di buku bergaris dengan posisi duduk tegak dan buku lurus di depan. Sikap yang ditunjukkan adalah ....', 'sikap menulis yang baik', ['bermain di kelas', 'mengabaikan pelajaran', 'tidur di kelas'], 'Duduk tegak membantu tulisan rapi.', 'easy', 'menerapkan', 'Mempraktikkan penulisan',
         visual='Anak perempuan duduk tegak di meja belajar menulis di buku bergaris, buku diletakkan lurus, pensil dipegang dengan benar.')
    p.mc(4, 'Perhatikan gambar contoh tulisan kata di buku latihan! Tulisan yang benar dan tersambung adalah ....', 'كتاب', ['ك ت ا ب', 'ك تاب', 'باتك'], 'كتاب ditulis bersambung kecuali setelah alif.', 'medium', 'menerapkan', 'Mempraktikkan penulisan',
         visual='Dua halaman buku latihan: kiri bertuliskan ك ت ا ب (terpisah), kanan bertuliskan كتاب (tersambung) dengan centang hijau.')
    p.mc(4, 'Perhatikan gambar papan tulis! Guru menulis ب + ي + ت. Hasil rangkaian yang benar adalah ....', 'بيت', ['تيب', 'ب ي ت', 'يبت'], 'ب + ي + ت = بيت.', 'medium', 'menerapkan', 'Mempraktikkan penulisan',
         visual='Papan tulis hijau: guru menulis tiga huruf terpisah ب ي ت dengan tanda panah ke kata bersambung.')
    p.mc(4, 'Perhatikan gambar! Dua anak sedang berlatih menulis huruf hijaiah di buku tulis. Hal yang perlu diperhatikan adalah ....', 'bentuk huruf, titik, dan arah tulisan', ['jumlah halaman buku', 'warna pensil saja', 'ukuran meja saja'], 'Menulis huruf Arab memperhatikan bentuk, titik, dan arah.', 'medium', 'menerapkan', 'Mempraktikkan penulisan',
         visual='Dua anak MI duduk berdampingan menulis huruf Arab di buku bergaris; guru mengamati di sisi kanan.')
    p.mc(4, 'Perhatikan gambar tiga tulisan nama! Tulisan "محمد" yang tersambung benar adalah ....', 'محمد', ['م ح م د', 'مح مد', 'دمحم'], 'م ح م tersambung, د tidak menyambung ke huruf sesudahnya karena berada di akhir.', 'hard', 'menerapkan', 'Mempraktikkan penulisan',
         visual='Tiga kartu bertuliskan: م ح م د, محمد, دمحم, masing-masing diberi huruf a, b, c.')
    p.mc(4, 'Perhatikan gambar! Seorang anak menulis kata قلم lalu menunjuk pensilnya. Kata قلم berarti ....', 'pena', ['buku', 'meja', 'tas'], 'قلم (qalam) = pena.', 'easy', 'memahami', 'Mempraktikkan penulisan',
         visual='Anak laki-laki menulis kata قلم di buku sambil menunjuk pensil di tangannya.')
    p.mc(4, 'Perhatikan gambar! Kartu bertuliskan باب ditempel di sebuah pintu kelas. Kata باب berarti ....', 'pintu', ['jendela', 'papan', 'lantai'], 'باب (bab) = pintu.', 'easy', 'memahami', 'Mempraktikkan penulisan',
         visual='Kartu putih bertuliskan باب ditempel di pintu kayu ruang kelas.')
    p.mc(4, 'Perhatikan gambar! Kartu bertuliskan ماء tertempel pada botol minum. Kata ماء berarti ....', 'air', ['susu', 'roti', 'garam'], 'ماء (ma\') = air.', 'easy', 'memahami', 'Mempraktikkan penulisan',
         visual='Botol minum bening dengan label kartu bertuliskan ماء.')
    for (w, lat, arti) in WORDS:
        p.gk = f'w4{lat}'
        ls = list(w)
        p.perf(4, f'Tulislah kata {w} ({arti}) dengan huruf tersambung di buku tulismu, lalu bacakan "{lat}"!', 'Dinilai guru: ketepatan menyambung huruf, kerapian, dan bacaan (skala 1-4).', f'Murid menulis kata {w} dengan benar.', 'medium', 'menerapkan', 'Mempraktikkan penulisan')
        if w in ('بيت', 'جمل'):
            p.mc(4, f'Untuk menulis kata "{arti}" dengan benar, kita menyambung huruf-huruf ....', 'yang dapat disambung dan memutus setelah huruf yang tidak dapat disambung',
                 ['semuanya tanpa kecuali', 'tidak ada yang disambung', 'hanya huruf pertama'], f'{w} ditulis dengan menyambung huruf yang dapat disambung.', 'hard', 'menerapkan', 'Mempraktikkan penulisan') if len(ls) >= 3 else None
    for c in ['ب', 'ت', 'ج', 'س', 'م', 'ن', 'ي', 'ك', 'ل', 'ف']:
        f = forms(c)
        p.perf(4, f'Tulislah huruf {NAME[c]} dalam empat bentuk: {c} (terpisah), {f["awal"]} (awal), {f["tengah"]} (tengah), {f["akhir"]} (akhir) pada buku tulismu!', 'Dinilai guru: ketepatan bentuk di tiap posisi dan kerapian (skala 1-4).', f'Murid menulis empat bentuk huruf {NAME[c]}.', 'medium', 'menerapkan', 'Mempraktikkan penulisan')
    p.perf(4, 'Tuliskan namamu dengan huruf hijaiah (sesuai bunyi) bersama bantuan guru, lalu sambungkan hurufnya!', 'Dinilai guru: kerapian, ketepatan sambungan huruf, dan semangat belajar (skala 1-4).', 'Murid menulis nama dengan huruf Arab.', 'hard', 'menerapkan', 'Mempraktikkan penulisan')
    return p
