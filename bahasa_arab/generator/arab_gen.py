# -*- coding: utf-8 -*-
"""Pembangkit soal Bahasa Arab dari tabel kosakata/kalimat/dialog/teks."""
import random, unicodedata
import lib, arab_scen
from arab_data import MATERI

LN = {'ا': 'Alif', 'أ': 'Alif', 'إ': 'Alif', 'آ': 'Alif', 'ب': 'Ba', 'ت': 'Ta', 'ث': 'Tsa', 'ج': 'Jim', 'ح': 'Ha', 'خ': 'Kha', 'د': 'Dal', 'ذ': 'Dzal',
      'ر': 'Ra', 'ز': 'Zai', 'س': 'Sin', 'ش': 'Syin', 'ص': 'Shad', 'ض': 'Dhad', 'ط': 'Tha', 'ظ': 'Zha', 'ع': "'Ain", 'غ': 'Ghain', 'ف': 'Fa', 'ق': 'Qaf',
      'ك': 'Kaf', 'ل': 'Lam', 'م': 'Mim', 'ن': 'Nun', 'و': 'Wawu', 'ه': 'Ha', 'ي': 'Ya', 'ة': 'Ta marbuthah', 'ء': 'Hamzah', 'ى': 'Alif maqshurah'}
MARK = {'ً': 'fathatain', 'ٍ': 'kasratain', 'ٌ': 'dammatain', 'َ': 'fathah', 'ِ': 'kasrah', 'ُ': 'dammah', 'ْ': 'sukun', 'ّ': 'tasydid'}
SND = {'fathatain': 'an', 'kasratain': 'in', 'dammatain': 'un'}


def letters(w):
    return [c for c in w if not unicodedata.category(c).startswith('M') and c in LN]


def lastmark(w):
    # tanda baca terakhir pada huruf terakhir
    i = len(w) - 1
    marks = []
    while i >= 0 and unicodedata.category(w[i]).startswith('M'):
        marks.append(w[i]); i -= 1
    for m in marks:
        if m in MARK:
            return MARK[m]
    return None


def firstmark(w):
    i = 1
    while i < len(w) and unicodedata.category(w[i]).startswith('M'):
        if w[i] in MARK and w[i] != 'ّ':
            return MARK[w[i]]
        i += 1
    return None


def gen(p, M, seed):
    rng = random.Random(seed)
    W = M['words']; code = M['code']; tema = M['name'].split(' (')[0]
    ar = [w[0] for w in W]; la = [w[1] for w in W]; ti = [w[2] for w in W]
    nouns = [w for w in W if w[3]]
    for i, (a, l, t, g, vis) in enumerate(W):
        p.gk = f'w{code}{i}'
        oa = [x for j, x in enumerate(ar) if j != i]
        ol = [x for j, x in enumerate(la) if j != i]
        ot = [x for j, x in enumerate(ti) if j != i]
        # ---- TP1: kosakata
        p.mc(1, f'Kata {a} berarti ....', t, ot, f'{a} ({l}) berarti {t}.', 'easy', 'mengenali', 'Mengenali kosakata')
        p.mc(1, f'Kata Arab untuk "{t}" adalah ....', a, oa, f'"{t}" dalam bahasa Arab adalah {a} ({l}).', 'medium', 'mengenali', 'Mengenali kosakata')
        p.mc(1, f'Kata {a} dibaca ....', l, ol, f'{a} dibaca {l}.', 'easy', 'mengenali', 'Mengenali bunyi kata')
        p.tf(1, f'Kata {a} berarti {t}.', True, f'Benar, {a} ({l}) berarti {t}.', 'easy', 'mengingat', 'Mengenali kosakata')
        p.tf(1, f'Kata {a} berarti {ot[i % len(ot)]}.', False, f'Salah. {a} berarti {t}.', 'medium', 'mengingat', 'Mengenali kosakata')
        p.fill(1, f'Arti kata {a} adalah ....', t, f'{a} ({l}) berarti {t}.', 'medium', 'mengingat', 'Mengenali kosakata')
        p.mc(1, f'Bunyi "{l}" ditulis dengan huruf Arab ....', a, oa, f'{l} ditulis {a}.', 'medium', 'mengenali', 'Mengenali bunyi kata')
        # ---- TP2: membaca teks/visual
        p.fill(2, f'Bacalah kata {a} dengan huruf Latin: ....', l, f'{a} dibaca {l}.', 'medium', 'mengenali', 'Menyebutkan bunyi kata')
        p.fill(2, f'Tuliskan kata Arab untuk bunyi "{l}": ....', a, f'{l} ditulis {a}.', 'hard', 'mengenali', 'Menyebutkan bunyi kata')
        if vis:
            n = i + 1
            p.mc(2, f'Perhatikan gambar nomor {n} pada kartu kosakata tema {tema}! Kata Arab untuk gambar tersebut adalah ....', a, oa, f'Gambar menunjukkan {t}: {a} ({l}).', 'medium', 'mengenali', 'Menyebutkan kosakata visual', visual=vis)
            p.mc(2, f'Perhatikan gambar kartu nomor {n} tema {tema}! Nama gambar tersebut dibaca ....', l, ol, f'Gambar menunjukkan {t}, dibaca {l}.', 'medium', 'mengenali', 'Menyebutkan kosakata visual', visual=vis)
            if g:
                dem = 'هٰذَا' if g == 'm' else 'هٰذِهِ'; wd = 'هٰذِهِ' if g == 'm' else 'هٰذَا'
                dl = 'Hadza' if g == 'm' else 'Hadzihi'
                p.mc(2, f'Perhatikan gambar nomor {n} tema {tema}! Kalimat yang tepat untuk menunjuk gambar tersebut dari dekat adalah ....', f'{dem} {a}', [f'{wd} {a}', f'{dem} {oa[(i + 1) % len(oa)]}', f'{wd} {oa[(i + 3) % len(oa)]}'],
                     f'Untuk {t} dipakai {dem} karena kata itu {"mudzakkar" if g == "m" else "muannats"}.', 'hard', 'menerapkan', 'Menyebutkan kosakata visual', visual=vis)
        # ---- TP3: huruf, kata, tanda baca
        ls = letters(a)
        if ' ' not in a:
            p.mc(3, f'Kata {a} terdiri dari ... huruf.', str(len(ls)), [str(x) for x in range(2, 9) if x != len(ls)], f'{a} terdiri dari {len(ls)} huruf: {" ".join(ls)}.', 'medium', 'menganalisis', 'Memahami huruf dalam kata')
            fl = LN[ls[0]]
            p.mc(3, f'Huruf pertama pada kata {a} adalah huruf ....', fl, [x for x in ['Ba', 'Mim', 'Kaf', 'Sin', 'Dal', 'Qaf', 'Ra', 'Ha', 'Nun', 'Alif', 'Jim'] if x != fl], f'Huruf pertama {a} adalah {ls[0]} ({fl}).', 'medium', 'menganalisis', 'Memahami huruf dalam kata')
            ll = LN[ls[-1]]
            p.fill(3, f'Huruf terakhir pada kata {a} adalah huruf ....', ll, f'Huruf terakhir {a} adalah {ls[-1]} ({ll}).', 'hard', 'menganalisis', 'Memahami huruf dalam kata')
            lm = lastmark(a)
            if lm in SND:
                p.mc(3, f'Tanda baca pada huruf terakhir kata {a} bernama ....', lm, [x for x in ['fathatain', 'kasratain', 'dammatain', 'fathah', 'kasrah', 'dammah', 'sukun'] if x != lm], f'{a} berakhir dengan {lm}, dibaca "{SND[lm]}".', 'medium', 'menganalisis', 'Memahami tanda baca')
                p.tf(3, f'Kata {a} berakhir dengan tanda baca {lm}.', True, f'Benar, {a} berakhir dengan {lm}.', 'easy', 'menganalisis', 'Memahami tanda baca')
                other = [x for x in SND if x != lm][0]
                p.tf(3, f'Kata {a} berakhir dengan tanda baca {other}.', False, f'Salah. {a} berakhir dengan {lm}.', 'medium', 'menganalisis', 'Memahami tanda baca')
            fm = firstmark(a)
            if fm:
                p.mc(3, f'Huruf pertama kata {a} berharakat ....', fm, [x for x in ['fathah', 'kasrah', 'dammah', 'sukun'] if x != fm], f'Huruf pertama {a} berharakat {fm}.', 'medium', 'menganalisis', 'Memahami tanda baca')
            if a.rstrip('ًٌٍ').endswith('ة') or a.endswith('ةٌ'):
                p.tf(3, f'Kata {a} diakhiri huruf ة (ta marbuthah).', True, f'Benar, {a} berakhir dengan ة.', 'medium', 'menganalisis', 'Memahami huruf dalam kata')
            if g:
                dem = 'هٰذَا' if g == 'm' else 'هٰذِهِ'; wd = 'هٰذِهِ' if g == 'm' else 'هٰذَا'
                gn = 'mudzakkar (laki-laki)' if g == 'm' else 'muannats (perempuan)'
                p.mc(3, f'Kata tunjuk yang tepat untuk {a} adalah ....', dem, [wd, 'ذٰلِكَ' if dem == 'هٰذِهِ' else 'تِلْكَ', 'مَنْ'], f'{a} termasuk kata {gn} sehingga memakai {dem}.', 'hard', 'menganalisis', 'Memahami kalimat sederhana')
                p.tf(3, f'Kalimat "{wd} {a}" adalah susunan yang benar.', False, f'Salah. {a} memakai {dem}: "{dem} {a}".', 'hard', 'menganalisis', 'Memahami kalimat sederhana')
                p.tf(3, f'Kalimat "{dem} {a}" berarti "ini {t}".', True, f'Benar, "{dem} {a}" berarti ini {t}.', 'medium', 'memahami', 'Memahami kalimat sederhana')
                p.mc(3, f'Kata {a} termasuk kata benda ....', gn, [x for x in ['mudzakkar (laki-laki)', 'muannats (perempuan)', 'jamak (banyak)', 'kata kerja'] if x != gn], f'{a} adalah kata {gn}.', 'hard', 'menganalisis', 'Memahami kalimat sederhana')
    p.gk = None

    # ---- kalimat
    S = M['sent']
    sa = [s[0] for s in S]; sl = [s[1] for s in S]; st = [s[2] for s in S]
    for i, (a, l, t) in enumerate(S):
        p.gk = f's{code}{i}'
        oa = [x for j, x in enumerate(sa) if j != i]; ot = [x for j, x in enumerate(st) if j != i]; ol = [x for j, x in enumerate(sl) if j != i]
        p.mc(1, f'Kalimat {a} berarti ....', t, ot, f'{a} ({l}) berarti "{t}".', 'easy', 'memahami', 'Memahami pola kalimat')
        p.mc(1, f'Kalimat Arab untuk "{t}" adalah ....', a, oa, f'"{t}" = {a}.', 'medium', 'memahami', 'Memahami pola kalimat')
        p.tf(1, f'Kalimat {a} berarti "{t}".', True, f'Benar, {a} berarti "{t}".', 'easy', 'mengingat', 'Memahami pola kalimat')
        p.tf(1, f'Kalimat {a} berarti "{ot[i % len(ot)]}".', False, f'Salah. {a} berarti "{t}".', 'medium', 'mengingat', 'Memahami pola kalimat')
        p.fill(1, f'Arti kalimat {a} adalah ....', t, f'{a} berarti "{t}".', 'medium', 'mengingat', 'Memahami pola kalimat')
        p.mc(2, f'Kalimat {a} dibaca ....', l, ol, f'{a} dibaca "{l}".', 'easy', 'mengenali', 'Membaca kalimat sederhana')
        p.mc(2, f'Tulisan Arab dari bacaan "{l}" adalah ....', a, oa, f'"{l}" ditulis {a}.', 'medium', 'mengenali', 'Membaca kalimat sederhana')
        ws = a.split(' ')
        if len(ws) >= 2:
            k = rng.randrange(len(ws))
            blank = ' '.join('....' if x == k else w for x, w in enumerate(ws))
            p.fill(2, f'Lengkapi kalimat: {blank} (artinya "{t}")', ws[k], f'Kalimat lengkap: {a}.', 'medium', 'menerapkan', 'Membaca kalimat sederhana', typ='completion')
            sh = ws[:]
            while sh == ws:
                rng.shuffle(sh)
            p.order(2, f'Susun kata-kata berikut menjadi kalimat yang berarti "{t}"!', ws, f'Kalimat yang benar: {a}.', 'medium', 'mengurutkan', 'Membaca kalimat sederhana')
        if '؟' in a:
            p.tf(3, f'Kalimat {a} adalah kalimat tanya.', True, 'Kalimat berakhir dengan tanda tanya (؟).', 'easy', 'menganalisis', 'Memahami kalimat sederhana')
            p.mc(3, f'Kalimat {a} termasuk kalimat ....', 'tanya', ['perintah', 'pernyataan', 'seruan'], 'Tanda ؟ menunjukkan kalimat tanya.', 'medium', 'menganalisis', 'Memahami kalimat sederhana')
        else:
            p.tf(3, f'Kalimat {a} adalah kalimat tanya.', False, f'Salah. {a} bukan kalimat tanya karena tidak diakhiri tanda ؟.', 'medium', 'menganalisis', 'Memahami kalimat sederhana')
        p.mc(3, f'Kalimat {a} terdiri dari ... kata.', str(len(ws)), [str(x) for x in range(1, 7) if x != len(ws)], f'{a} terdiri dari {len(ws)} kata.', 'medium', 'menganalisis', 'Memahami kalimat sederhana')
    p.gk = None
    # ---- dialog
    D = M['dialog']
    GD = [d for m in MATERI for d in m['dialog']]
    for i, (q, a, desc) in enumerate(D):
        p.gk = f'd{code}{i}'
        wrong = list(dict.fromkeys(x[1] for x in GD if x[0] != q and x[1] != a))
        rng.shuffle(wrong)
        p.ctx(2, f'Dalam percakapan yang {desc}, temanmu bertanya, "{q}" Jawaban yang tepat adalah ....', a, wrong[:6], f'Percakapan {desc}: {q} → {a}.', 'medium', 'memahami', 'Memahami percakapan sederhana')
        wq = list(dict.fromkeys(x[0] for x in GD if x[0] != q and x[1] != a))
        rng.shuffle(wq)
        p.ctx(3, f'Dalam percakapan yang {desc}, jawabannya adalah "{a}". Pertanyaan yang tepat adalah ....', q, wq[:6], f'Percakapan {desc}: {q} → {a}.', 'hard', 'menganalisis', 'Memahami percakapan sederhana')
        p.tf(3, f'Pertanyaan "{q}" dijawab dengan "{a}" ({desc}).', True, f'Benar, ini percakapan yang {desc}.', 'easy', 'memahami', 'Memahami percakapan sederhana')
        p.tf(3, f'Pertanyaan "{q}" dijawab dengan "{wrong[0]}" ({desc}).', False, f'Salah. {q} dijawab {a}.', 'medium', 'memahami', 'Memahami percakapan sederhana')
        p.order(2, 'Susun percakapan berikut dengan urutan yang benar!', [q, a], f'Urutan: pertanyaan "{q}" lalu jawaban "{a}".', 'easy', 'mengurutkan', 'Memahami percakapan sederhana')
    p.gk = None
    for s in range(0, len(D) - 3, 2):
        sel = D[s:s + 4]
        p.match(3, 'Jodohkan pertanyaan dengan jawaban yang tepat!', [(x[0], x[1]) for x in sel], 'Setiap pertanyaan dipasangkan dengan jawabannya.', 'medium', 'mencocokkan', 'Memahami percakapan sederhana')
    for s in range(0, len(W) - 3, 3):
        sel = [w for w in W[s:s + 4]]
        p.match(1, 'Jodohkan kata Arab dengan artinya!', [(w[0], w[2]) for w in sel], 'Setiap kata dipasangkan dengan artinya.', 'medium', 'mencocokkan', 'Mengenali kosakata')
        p.match(2, 'Jodohkan kata Arab dengan bunyi Latinnya!', [(w[0], w[1]) for w in sel], 'Setiap kata dipasangkan dengan bunyi Latinnya.', 'medium', 'mencocokkan', 'Menyebutkan bunyi kata')
    # ---- teks bacaan
    for ti_, (txt, qs) in enumerate(M['texts']):
        for qi, (qq, ok, bad) in enumerate(qs):
            p.gk = f't{code}{ti_}'
            p.ctx(2 if qi < 2 else 3, f'Bacalah teks berikut! "{txt}" {qq}', ok, bad, f'Jawaban berdasarkan teks: {ok}.', 'medium', 'memahami', 'Membaca teks sederhana')
        p.gk = None
        p.perf(2, f'Bacalah teks berikut dengan lafal yang benar: {txt}', 'Dinilai guru: ketepatan lafal, kelancaran, dan intonasi (skala 1-4).', 'Murid membaca teks sederhana dengan benar.', 'medium', 'menerapkan', 'Membaca teks sederhana')
    # ---- huruf & tanda baca umum materi
    p.gk = None
    p.mc(3, 'Tanda "؟" pada akhir kalimat bahasa Arab disebut tanda ....', 'tanya', ['seru', 'titik', 'koma'], 'Tanda ؟ adalah tanda tanya Arab.', 'easy', 'mengingat', 'Memahami tanda baca')
    arab_scen.apply(p, code)
