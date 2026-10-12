# -*- coding: utf-8 -*-
"""Pembangkit berbasis tabel untuk Bahasa Inggris Kelas 1 (Grow with English)."""
import random

R = 'Dinilai guru: ketepatan ucapan/gerak, keberanian mencoba, dan kesantunan (skala 1-4).'
NAMA = ['Dina', 'Rafi', 'Salma', 'Fikri', 'Nisa', 'Hasan', 'Lani', 'Bima', 'Aisyah', 'Zaki', 'Mira', 'Dani', 'Hana', 'Umar', 'Putri', 'Alif']


def kv(p, tp, rows, fwd, rev, comp, tag, seed=0, rev_ok=None, extra_wrong=(), extra_keys=(), match=True):
    """rows = [(k, v)]. fwd: stem dengan '{v}' untuk jawaban; rev: stem dengan '{v}' yang diketahui dan jawaban k."""
    vals = [v for _, v in rows]
    keys = [k for k, _ in rows]
    for i, (k, v) in enumerate(rows):
        p.gk = f'{tag}{i}'
        wv = [x for x in dict.fromkeys(vals + list(extra_wrong)) if x != v]
        stem = fwd.format(k=k, v='....').replace('.....', '....')
        p.mc(tp, stem, v, wv, f'{k} = {v}.', 'easy', 'mengingat', comp)
        p.tf(tp, fwd.format(k=k, v=v), True, f'Benar, {k} = {v}.', 'easy', 'mengingat', comp)
        p.tf(tp, fwd.format(k=k, v=wv[i % len(wv)]), False, f'Salah. Yang benar: {k} = {v}.', 'medium', 'mengingat', comp)
        p.fill(tp, 'Isilah: ' + stem, v, f'{k} = {v}.', 'medium', 'mengingat', comp)
        if rev and (rev_ok is None or k in rev_ok):
            wk = [str(x) for x in list(keys) + list(extra_keys) if x != k]
            rs = rev.format(k='....', v=v).replace('.....', '....')
            p.mc(tp, rs, str(k), wk, f'{v} = {k}.', 'medium', 'mengenali', comp)
            p.fill(tp, 'Isilah: ' + rs, str(k), f'{v} = {k}.', 'medium', 'mengenali', comp)
    p.gk = None
    if match:
        for s in range(0, len(rows) - 3, 2):
            p.match(tp, f'Jodohkan pasangan yang tepat ({tag})!', [(str(k), v) for k, v in rows[s:s + 4]], 'Setiap pasangan dicocokkan.', 'medium', 'mencocokkan', comp)


def vis(p, tp, rows, tpl, comp, tag, pool=None):
    """rows = [(en, deskripsi gambar)]; tpl memuat {d}. Soal pilihan ganda bergambar; pengecoh dari kata lain."""
    ens = [e for e, _ in rows] + list(pool or [])
    for i, (e, d) in enumerate(rows):
        p.gk = f'{tag}v{i}'
        wr = [x for x in dict.fromkeys(ens) if x != e]
        p.mc(tp, tpl.format(d=d), e, wr, f'Gambar menunjukkan {e}.', 'easy', 'mengenali', comp, visual=d[0].upper() + d[1:] + '.')
    p.gk = None


USED_W = set()


def scr(p, tp, words, comp, tag='sc', seed=0):
    rng = random.Random(seed)
    for w in words:
        if len(w) < 3 or ' ' in w or w in USED_W: continue
        USED_W.add(w)
        l = list(w)
        for _ in range(20):
            rng.shuffle(l)
            if ''.join(l) != w: break
        p.gk = f'{tag}{w}'
        p.fill(tp, 'Susunlah huruf berikut menjadi satu kata Bahasa Inggris: ' + ' - '.join(l) + ' = ....', w, f'Kata yang benar: {w}.', 'medium', 'menerapkan', comp)
    p.gk = None


KEEP_CAP = set(NAMA) | {'I', 'Teacher', 'Mother', 'Father', 'Grandmother', 'Grandfather', 'Sister', 'Brother'}


def sent(p, tp, sentences, comp, tag='st', seed=0):
    """sentences = [(kalimat_en, arti_id)]. Urutan kata, melengkapi kalimat, dan memilih kalimat benar."""
    rng = random.Random(seed)
    for i, (s, idn) in enumerate(sentences):
        punct = s[-1] if s[-1] in '.?!' else ''
        core = s[:-1].split() if punct else s.split()
        if core[0] not in KEEP_CAP:
            core[0] = core[0].lower()
        words = s.split()
        p.gk = f'{tag}{i}'
        p.order(tp, f'Susunlah kata-kata berikut menjadi kalimat yang benar ({idn})!', core, f'Kalimat yang benar: {s}', 'medium', 'menerapkan', comp)
        cand = [j for j, w in enumerate(words) if len(w.strip('.,?!')) >= 3] or [len(words) - 1]
        j = cand[i % len(cand)]
        blank = words[:]; ans = blank[j].strip('.,?!'); blank[j] = '....'
        p.fill(tp, 'Lengkapi kalimat berikut: ' + ' '.join(blank) + f' ({idn})', ans, f'Kalimat lengkap: {s}', 'medium', 'menerapkan', comp, typ='completion')
        if len(core) >= 3:
            alts = []
            for _ in range(40):
                w2 = core[:]; rng.shuffle(w2)
                if w2 == core: continue
                w2[-1] = w2[-1].rstrip(',')
                t = ' '.join(w2)
                t = t[0].upper() + t[1:] + punct
                if t != s and t not in alts: alts.append(t)
                if len(alts) == 3: break
            if len(alts) == 3:
                p.mc(tp, f'Kalimat Bahasa Inggris yang tersusun benar untuk "{idn}" adalah ....', s, alts, f'Kalimat yang benar: {s}', 'medium', 'menerapkan', comp)
    p.gk = None


def perfs(p, tp, rows, tpl, comp='Praktik berbicara dan bergerak', diff='medium'):
    for r in rows:
        k = r[0] if isinstance(r, (tuple, list)) else r
        v = r[1] if isinstance(r, (tuple, list)) and len(r) > 1 else ''
        p.perf(tp, tpl.format(k=k, v=v), R, 'Murid menunjukkan kemampuan sesuai rubrik.', diff, 'menerapkan', comp)


def count(p, tp, noun_en, noun_id, vis_tpl, comp, tag, upto=10):
    NUM = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for n in range(1, upto + 1):
        p.gk = f'{tag}{n}'
        plural = noun_en + ('s' if n > 1 else '')
        d = vis_tpl.format(n=n, noun=noun_id)
        wr = [x for x in NUM if x != NUM[n - 1]]
        rng = random.Random(n + len(noun_en))
        wr = [NUM[(n - 1 + o) % 10] for o in (1, -1, 2, -2, 3)]
        p.mc(tp, f'Perhatikan gambar! {d}. Berapa jumlahnya dalam Bahasa Inggris? ....', NUM[n - 1], wr, f'{n} = {NUM[n - 1]}.', 'easy', 'mengenali', comp, visual=d + '.')
    p.gk = None


def fq(p, tp, stem, ok, bad, expl='', diff='easy', comp='Memahami kosakata dan ungkapan'):
    """Soal fakta: pilihan ganda + benar/salah (benar & salah) + isian."""
    expl = expl or f'Jawaban: {ok}.'
    p.gk = f'fq{tp}{stem[:40]}'
    p.mc(tp, stem, ok, bad, expl, diff, 'memahami', comp)
    p.tf(tp, stem.replace('....', ok), True, expl, 'easy', 'mengingat', comp)
    p.tf(tp, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
    p.fill(tp, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    p.gk = None


def sq(p, tp, long, short, ok, bad, expl, diff='medium', vis=None, comp='Menggunakan bahasa dalam situasi nyata'):
    """Soal situasi: kontekstual (atau bergambar) + benar/salah + melengkapi."""
    p.gk = f'sq{tp}{long[:40]}'
    if vis:
        p.mc(tp, long, ok, bad, expl, diff, 'menerapkan', comp, visual=vis)
    else:
        p.ctx(tp, long, ok, bad, expl, diff, 'menerapkan', comp)
        p.tf(tp, f'{short} {ok}.', True, expl, 'easy', 'memahami', comp)
        p.tf(tp, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', comp)
        p.fill(tp, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', comp, typ='completion')
    p.gk = None


def tfs(p, tp, items, comp='Memahami konsep'):
    for st, truth, e in items:
        p.tf(tp, st, truth, e, 'easy', 'memahami', comp)
