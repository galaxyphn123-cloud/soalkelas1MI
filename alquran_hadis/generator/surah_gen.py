# -*- coding: utf-8 -*-
"""Pembangkit soal generik untuk surah pendek (dari tabel fakta, bukan salin-tempel)."""
import random
from surah_data import ALL


def lf(t):
    return t if t.startswith('Allah') else t[0].lower() + t[1:]


def pick(lst, k, rng, exclude=()):
    ex = {e.lower() for e in exclude}
    c = [x for x in dict.fromkeys(lst) if x.lower() not in ex]
    rng.shuffle(c)
    return c[:k]


def gen(p, S, seed):
    rng = random.Random(seed)
    N = S['name']; A = S['ayat']; n = len(A)
    ar = [a[0] for a in A]; la = [a[1] for a in A]; ti = [a[2] for a in A]; ps = [a[3] for a in A]
    others = [o for o in ALL if o is not S]
    other_pesan = [o['pesan'] for o in others]
    other_names = [o['short'] for o in others]

    # ================= TP1: pesan pokok =================
    p.mc(1, f'Pesan pokok surah {N} adalah ....', S['pesan'], other_pesan + ['Menceritakan kisah para nabi terdahulu'],
         f'Surah {N} berisi pesan pokok: {lf(S["pesan"])}.', 'easy', 'mengingat', 'Menjelaskan pesan pokok surah')
    p.mc(1, f'Murid belajar surah {N} untuk mengetahui bahwa kita perlu ....', lf(S['pesan']),
         [lf(x) for x in other_pesan] + ['bermain sepanjang hari'], f'Pesan pokok surah {N}: {lf(S["pesan"])}.',
         'medium', 'memahami', 'Menjelaskan pesan pokok surah')
    p.tf(1, f'Pesan pokok surah {N} adalah {lf(S["pesan"])}.', True, f'Benar, itulah pesan pokok surah {N}.', 'easy', 'mengingat', 'Menjelaskan pesan pokok surah')
    for o in others:
        p.tf(1, f'Pesan pokok surah {N} adalah {lf(o["pesan"])}.', False,
             f'Salah. {o["pesan"]} adalah pesan surah {o["short"]}. Pesan surah {N}: {lf(S["pesan"])}.', 'medium', 'membandingkan', 'Membedakan pesan surah')
        p.mc(1, f'Pesan "{lf(o["pesan"])}" terdapat dalam surah ....', o['short'], [N] + [x for x in other_names if x != o['short']] + ['Al-Kautsar'],
             f'Pesan itu adalah pesan pokok surah {o["short"]}.', 'medium', 'membandingkan', 'Membedakan pesan surah')
    p.mc(1, f'Surah yang berpesan "{lf(S["pesan"])}" adalah surah ....', N, other_names + ['Al-Kautsar'],
         f'Pesan tersebut adalah pesan pokok surah {N}.', 'medium', 'mengenali', 'Menjelaskan pesan pokok surah')
    if ' dan ' in S['pesan']:
        head, tail = S['pesan'].rsplit(' dan ', 1)
        p.fill(1, f'Lengkapi pesan surah {N}: "{head} dan ...."', tail, f'Pesan lengkap surah {N}: {lf(S["pesan"])}.',
               'medium', 'mengingat', 'Menjelaskan pesan pokok surah', typ='completion')
    for i in range(n):
        p.gk = f'p1a{i}'
        wrongp = [x for j, x in enumerate(ps) if j != i]
        p.mc(1, f'Ayat "{la[i]}" mengajarkan kita untuk ....', ps[i], wrongp + [lf(x['pesan']) for x in others],
             f'Ayat ke-{i+1} surah {N} mengajarkan kita untuk {ps[i]}.', 'medium', 'memahami', 'Menjelaskan pesan ayat')
        p.mc(1, f'Ayat yang mengajarkan kita untuk {ps[i]} adalah ayat ....', la[i], [x for j, x in enumerate(la) if j != i],
             f'Ayat ke-{i+1} surah {N} ("{la[i]}") mengajarkan kita untuk {ps[i]}.', 'hard', 'menganalisis', 'Menjelaskan pesan ayat')
        j = (i + 1 + rng.randrange(n - 1)) % n
        p.tf(1, f'Ayat "{la[i]}" mengajarkan kita untuk {ps[i]}.', True, f'Benar, ayat ke-{i+1} surah {N} berpesan seperti itu.', 'easy', 'memahami', 'Menjelaskan pesan ayat')
        p.tf(1, f'Ayat "{la[i]}" mengajarkan kita untuk {ps[j]}.', False,
             f'Salah. Ayat itu mengajarkan kita untuk {ps[i]}; "{ps[j]}" adalah pesan ayat ke-{j+1}.', 'medium', 'memahami', 'Menjelaskan pesan ayat')
    p.gk = None
    for s in range(0, n - 3):
        idx = list(range(s, s + 4))
        p.match(1, f'Jodohkan ayat surah {N} dengan pesan yang diajarkannya!', [(la[k], ps[k]) for k in idx],
                'Setiap ayat memiliki pesan yang sesuai dengan artinya.', 'medium', 'mencocokkan', 'Menjelaskan pesan ayat')

    # ================= TP2: pelafalan & hafalan =================
    p.mc(2, f'Surah {N} terdiri dari ... ayat.', f'{n}', [str(x) for x in range(2, 9) if x != n][:5], f'Surah {N} terdiri dari {n} ayat.', 'easy', 'mengingat', 'Menyebutkan jumlah ayat')
    p.fill(2, f'Banyaknya ayat dalam surah {N} adalah .... ayat.', f'{n}', f'Surah {N} terdiri dari {n} ayat.', 'easy', 'mengingat', 'Menyebutkan jumlah ayat')
    p.tf(2, f'Surah {N} terdiri dari {n} ayat.', True, f'Benar, surah {N} memiliki {n} ayat.', 'easy', 'mengingat', 'Menyebutkan jumlah ayat')
    p.tf(2, f'Surah {N} terdiri dari {n + 2} ayat.', False, f'Salah. Surah {N} terdiri dari {n} ayat.', 'easy', 'mengingat', 'Menyebutkan jumlah ayat')
    p.mc(2, f'Ayat pertama surah {N} dibaca ....', la[0], la[1:], f'Ayat pertama surah {N}: "{la[0]}".', 'easy', 'mengingat', 'Melafalkan ayat')
    p.mc(2, f'Ayat terakhir surah {N} dibaca ....', la[-1], la[:-1], f'Ayat terakhir (ke-{n}) surah {N}: "{la[-1]}".', 'easy', 'mengingat', 'Melafalkan ayat')
    p.fill(2, f'Ayat terakhir surah {N} adalah ayat ke- ....', f'{n}', f'Surah {N} berakhir pada ayat ke-{n}.', 'easy', 'mengingat', 'Menyebutkan jumlah ayat')
    p.mc(2, f'Surah {N} berada pada urutan ke-... dalam Al-Qur\'an.', str(S['no']), [x for x in ['1', '2', '112', '113', '114', '36', '18'] if x != str(S['no'])],
         f'Surah {N} adalah surah ke-{S["no"]} dalam Al-Qur\'an.', 'medium', 'mengingat', 'Mengenal urutan surah')
    p.fill(2, f'Nomor urut surah {N} dalam Al-Qur\'an adalah ....', str(S['no']), f'Surah {N} berada pada urutan ke-{S["no"]}.', 'medium', 'mengingat', 'Mengenal urutan surah')
    p.fill(2, f'Tulisan "{S["arab_name"]}" dibaca surah ....', N, f'{S["arab_name"]} dibaca Surah {N}.', 'easy', 'mengenali', 'Mengenal nama surah')
    p.mc(2, f'Perhatikan gambar kartu hafalan surah nomor {S["no"]} dalam Al-Qur\'an! Judul pada kartu itu dibaca surah ....', N, other_names + ['Al-Kautsar'],
         f'Tulisan {S["arab_name"]} dibaca Surah {N}.', 'easy', 'mengenali', 'Mengenal nama surah',
         visual=f'Kartu hafalan berbingkai hijau dengan lencana nomor {S["no"]} di pojok dan judul besar berkaligrafi Arab: {S["arab_name"]}. Di bawahnya ada ornamen bunga sederhana.')

    for i in range(n):
        p.gk = f'p2a{i}'
        o_la = [x for j, x in enumerate(la) if j != i]
        o_ar = [x for j, x in enumerate(ar) if j != i]
        k = i + 1
        p.mc(2, f'Ayat ke-{k} surah {N} berbunyi ....', la[i], o_la, f'Ayat ke-{k} surah {N} berbunyi "{la[i]}".', 'easy', 'mengingat', 'Melafalkan ayat')
        p.mc(2, f'Cara membaca tulisan Arab {ar[i]} adalah ....', la[i], o_la, f'Tulisan {ar[i]} dibaca "{la[i]}".', 'easy', 'mengenali', 'Melafalkan ayat')
        p.mc(2, f'Tulisan Arab dari bacaan "{la[i]}" adalah ....', ar[i], o_ar, f'Bacaan "{la[i]}" ditulis {ar[i]}.', 'medium', 'mengenali', 'Melafalkan ayat')
        p.tf(2, f'Ayat ke-{k} surah {N} berbunyi "{la[i]}".', True, f'Benar, ayat ke-{k} surah {N} berbunyi "{la[i]}".', 'easy', 'mengingat', 'Melafalkan ayat')
        j = (i + 1 + rng.randrange(n - 1)) % n
        p.tf(2, f'Ayat ke-{k} surah {N} berbunyi "{la[j]}".', False, f'Salah. "{la[j]}" adalah ayat ke-{j+1}; ayat ke-{k} berbunyi "{la[i]}".', 'medium', 'mengingat', 'Melafalkan ayat')
        p.tf(2, f'Bacaan "{la[i]}" ditulis {ar[j]}.', False, f'Salah. {ar[j]} dibaca "{la[j]}"; "{la[i]}" ditulis {ar[i]}.', 'medium', 'mengenali', 'Melafalkan ayat')
        p.fill(2, f'Bacaan "{la[i]}" adalah ayat ke- .... surah {N}.', str(k), f'"{la[i]}" adalah ayat ke-{k}.', 'easy', 'mengingat', 'Menghafal ayat')
        if i < n - 1:
            p.mc(2, f'Setelah ayat "{la[i]}", ayat selanjutnya dibaca ....', la[i + 1], [x for j2, x in enumerate(la) if j2 != i + 1],
                 f'Setelah ayat ke-{k} ("{la[i]}") adalah ayat ke-{k+1}: "{la[i+1]}".', 'medium', 'mengingat', 'Menghafal ayat berurutan')
            p.fill(2, f'Sambungkan ayat: "{la[i]}" ... (ayat berikutnya).', la[i + 1], f'Ayat berikutnya adalah "{la[i+1]}".', 'hard', 'mengingat', 'Menghafal ayat berurutan', typ='completion')
        if i > 0:
            p.mc(2, f'Ayat sebelum "{la[i]}" adalah ....', la[i - 1], [x for j2, x in enumerate(la) if j2 != i - 1],
                 f'Sebelum ayat ke-{k} ("{la[i]}") adalah ayat ke-{k-1}: "{la[i-1]}".', 'medium', 'mengingat', 'Menghafal ayat berurutan')
        words = la[i].split(' ')
        if len(words) >= 2:
            b = rng.randrange(len(words))
            blank = ' '.join('....' if t == b else w for t, w in enumerate(words))
            p.fill(2, f'Lengkapi bacaan ayat ke-{k} surah {N}: {blank}', words[b], f'Bacaan lengkapnya: "{la[i]}".', 'medium', 'mengingat', 'Menghafal ayat', typ='completion')
            b2 = (b + 1) % len(words)
            blank2 = ' '.join('....' if t == b2 else w for t, w in enumerate(words))
            p.mc(2, f'Kata yang tepat untuk melengkapi bacaan surah {N} "{blank2}" adalah ....', words[b2],
                 pick([w for z in la for w in z.split(' ')], 6, rng, exclude=[words[b2]] + words), f'Bacaan yang benar: "{la[i]}".', 'medium', 'mengingat', 'Menghafal ayat')
        aw = ar[i].split(' ')
        if len(aw) >= 2:
            b = rng.randrange(len(aw))
            blank = ' '.join('....' if t == b else w for t, w in enumerate(aw))
            p.mc(2, f'Kata Arab yang melengkapi ayat berikut adalah ....\n{blank}', aw[b],
                 pick([w for z in ar for w in z.split(' ')], 6, rng, exclude=[aw[b]] + aw), f'Ayat lengkapnya: {ar[i]}.', 'hard', 'mengenali', 'Menghafal ayat')
        p.perf(2, f'Bacalah ayat ke-{k} surah {N} ({ar[i]}) dengan lafal yang benar di depan guru!',
               'Dinilai guru: ketepatan lafal ayat, kelancaran, dan kejelasan suara (skala 1-4).', f'Murid melafalkan ayat ke-{k} dengan benar.', 'medium', 'menerapkan', 'Melafalkan ayat')
    p.gk = None
    for s in range(0, n - 2):
        w = min(3 + (s % 2), n - s)
        seg = list(range(s, s + w))
        if len(seg) < 3:
            continue
        p.order(2, f'Urutkan ayat-ayat surah {N} berikut dari yang pertama dibaca!', [la[x] for x in seg],
                'Ayat dibaca berurutan sesuai nomor ayatnya: ' + ' → '.join(la[x] for x in seg) + '.', 'medium', 'mengurutkan', 'Menghafal ayat berurutan')
    p.gk = None
    for s in range(0, n - 3):
        idx = list(range(s, s + 4))
        p.match(2, f'Jodohkan tulisan Arab dengan bacaan Latinnya (surah {N})!', [(ar[x], la[x]) for x in idx],
                'Setiap tulisan Arab dibaca sesuai bacaan Latinnya.', 'medium', 'mencocokkan', 'Melafalkan ayat')
    p.perf(2, f'Hafalkan surah {N} dari ayat pertama sampai terakhir dan bacakan di depan guru!', 'Dinilai guru: kelengkapan ayat, urutan, dan ketepatan lafal (skala 1-4).',
           f'Murid menghafal {n} ayat surah {N} secara urut.', 'hard', 'menerapkan', 'Menghafal surah')
    p.perf(2, f'Bacalah surah {N} bersama teman secara bergantian ayat demi ayat!', 'Dinilai guru: ketepatan lafal, ketertiban bergantian, dan kerja sama (skala 1-4).',
           'Murid membaca bergantian dengan lafal yang benar.', 'medium', 'menerapkan', 'Melafalkan ayat')

    # ================= TP3: arti =================
    p.mc(3, f'Nama surah {N} berarti ....', S['arti_nama'], [o['arti_nama'] for o in others] + ['Sapi betina'],
         f'Nama surah {N} berarti {S["arti_nama"]}.', 'medium', 'mengingat', 'Menyebutkan arti nama surah')
    p.tf(3, f'Nama surah {N} berarti {S["arti_nama"]}.', True, f'Benar, {N} berarti {S["arti_nama"]}.', 'easy', 'mengingat', 'Menyebutkan arti nama surah')
    for o in others:
        p.tf(3, f'Nama surah {N} berarti {o["arti_nama"]}.', False, f'Salah. {N} berarti {S["arti_nama"]}; {o["arti_nama"]} adalah arti {o["short"]}.', 'medium', 'membandingkan', 'Menyebutkan arti nama surah')
    p.fill(3, f'Surah {N} artinya ....', S['arti_nama'], f'{N} berarti {S["arti_nama"]}.', 'medium', 'mengingat', 'Menyebutkan arti nama surah')
    for i in range(n):
        p.gk = f'p3a{i}'
        k = i + 1
        o_ti = [x for j, x in enumerate(ti) if j != i]
        p.mc(3, f'Arti ayat "{la[i]}" adalah ....', ti[i], o_ti, f'Ayat "{la[i]}" berarti: {ti[i]}.', 'medium', 'memahami', 'Menyebutkan arti ayat')
        p.mc(3, f'Ayat yang artinya "{ti[i]}" dibaca ....', la[i], [x for j, x in enumerate(la) if j != i],
             f'Arti tersebut adalah arti ayat ke-{k}: "{la[i]}".', 'medium', 'memahami', 'Menyebutkan arti ayat')
        p.mc(3, f'Arti dari tulisan {ar[i]} adalah ....', ti[i], o_ti, f'{ar[i]} berarti: {ti[i]}.', 'hard', 'memahami', 'Menyebutkan arti ayat')
        j = (i + 1 + rng.randrange(n - 1)) % n
        p.tf(3, f'Ayat "{la[i]}" artinya "{ti[i]}".', True, f'Benar, itulah arti ayat ke-{k}.', 'easy', 'mengingat', 'Menyebutkan arti ayat')
        p.tf(3, f'Ayat "{la[i]}" artinya "{ti[j]}".', False, f'Salah. Ayat itu berarti "{ti[i]}".', 'medium', 'memahami', 'Menyebutkan arti ayat')
        p.fill(3, f'Arti ayat ke-{k} surah {N} adalah ....', ti[i], f'Ayat ke-{k} ("{la[i]}") berarti: {ti[i]}.', 'hard', 'mengingat', 'Menyebutkan arti ayat')
    p.gk = None
    for s in range(0, n - 3):
        idx = list(range(s, s + 4))
        p.match(3, f'Jodohkan bacaan ayat surah {N} dengan artinya!', [(la[x], ti[x]) for x in idx], 'Setiap ayat dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Menyebutkan arti ayat')
    W = S['words']; wa = [w[2] for w in W]
    for ai, (wr, wlt, wart) in enumerate(W):
        p.gk = f'p3w{ai}'
        p.mc(3, f'Kata "{wlt}" dalam surah {N} berarti ....', wart, [x for x in wa if x != wart] + [w[2] for o in others for w in o['words']],
             f'Kata {wr} ("{wlt}") berarti {wart}.', 'medium', 'memahami', 'Menyebutkan arti kata')
        p.mc(3, f'Kata Arab yang berarti "{wart}" adalah ....', wr, [w[0] for w in W if w[0] != wr] + [w[0] for o in others for w in o['words'] if w[0] != wr],
             f'{wr} ("{wlt}") berarti {wart}.', 'hard', 'mengenali', 'Menyebutkan arti kata')
        p.tf(3, f'Kata "{wlt}" berarti {wart}.', True, f'Benar, {wlt} berarti {wart}.', 'easy', 'mengingat', 'Menyebutkan arti kata')
        wrong = [x for x in wa if x != wart]
        p.tf(3, f'Kata "{wlt}" berarti {wrong[ai % len(wrong)]}.', False, f'Salah. {wlt} berarti {wart}.', 'medium', 'memahami', 'Menyebutkan arti kata')
        p.fill(3, f'Arti kata {wr} adalah ....', wart, f'{wr} ("{wlt}") berarti {wart}.', 'medium', 'mengingat', 'Menyebutkan arti kata')
        p.fill(3, f'Kata "{wart}" dalam bahasa Arab (surah {N}) ditulis ....', wr, f'"{wart}" = {wr} ({wlt}).', 'hard', 'mengenali', 'Menyebutkan arti kata')
    p.gk = None
    for s in range(0, len(W) - 3, 2):
        idx = list(range(s, s + 4))
        p.match(3, f'Jodohkan kata dalam surah {N} dengan artinya!', [(W[x][1], W[x][2]) for x in idx], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Menyebutkan arti kata')
    p.perf(3, f'Sebutkan arti surah {N} ayat demi ayat di depan guru!', 'Dinilai guru: ketepatan arti tiap ayat dan kejelasan penyampaian (skala 1-4).', f'Murid menyebutkan arti ayat-ayat surah {N}.', 'hard', 'memahami', 'Menyebutkan arti ayat')
    return rng
