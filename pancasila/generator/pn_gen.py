# -*- coding: utf-8 -*-
"""Pembangkit berbasis tabel untuk Pendidikan Pancasila Kelas 1."""
import random

R = 'Dinilai guru: ketepatan jawaban, sikap, dan kesantunan (skala 1-4).'
NAMA = ['Dina', 'Rafi', 'Salma', 'Fikri', 'Nisa', 'Hasan', 'Lani', 'Bima', 'Aisyah', 'Zaki', 'Mira', 'Dani', 'Hana', 'Umar', 'Putri', 'Alif']


def kv(p, tp, rows, fwd, rev, comp, tag, seed=0, rev_ok=None, extra_wrong=(), extra_keys=()):
    """rows = [(k, v)]. fwd: stem dengan '....' untuk v; rev: stem dengan '....' untuk k (None = tanpa)."""
    rng = random.Random(seed)
    vals = [v for _, v in rows]
    keys = [k for k, _ in rows]
    for i, (k, v) in enumerate(rows):
        p.gk = f'{tag}{i}'
        wv = [x for x in dict.fromkeys(vals + list(extra_wrong)) if x != v]
        stem = fwd.format(k=k, v='....').replace('.....', '....')
        p.mc(tp, stem, v, wv, f'{k}: {v}.', 'easy', 'mengingat', comp)
        p.tf(tp, fwd.format(k=k, v=v), True, f'Benar, {k}: {v}.', 'easy', 'mengingat', comp)
        p.tf(tp, fwd.format(k=k, v=wv[i % len(wv)]), False, f'Salah. {k}: {v}.', 'medium', 'mengingat', comp)
        p.fill(tp, 'Isilah: ' + stem, v, f'{k}: {v}.', 'medium', 'mengingat', comp)
        if rev and (rev_ok is None or k in rev_ok):
            wk = [str(x) for x in list(keys) + list(extra_keys) if x != k]
            p.mc(tp, rev.format(k='....', v=v).replace('.....', '....'), str(k), wk, f'{v} berkaitan dengan {k}.', 'medium', 'mengenali', comp)
            p.fill(tp, 'Isilah: ' + rev.format(k='....', v=v).replace('.....', '....'), str(k), f'{v} berkaitan dengan {k}.', 'medium', 'mengenali', comp)
    p.gk = None
    for s in range(0, len(rows) - 3, 2):
        p.match(tp, f'Jodohkan pasangan yang tepat ({tag})!', [(str(k), v) for k, v in rows[s:s + 4]], 'Setiap pasangan dicocokkan.', 'medium', 'mencocokkan', comp)


def rules(p, tp_a, tp_b, tp_c, rows, comp_a, comp_b, comp_c, noun, seed=0):
    """rows = (aturan, taat, tidak, manfaat). Menghasilkan soal manfaat (tp_a), uraian taat/tidak (tp_b), penerapan (tp_c)."""
    rng = random.Random(seed)
    taat = [r[1] for r in rows]; tidak = [r[2] for r in rows]; man = [r[3] for r in rows]
    for i, (a, t, x, m) in enumerate(rows):
        nm = NAMA[i % len(NAMA)]
        if tp_a:
            p.gk = f'ra{i}'
            wm = [y for y in man if y != m]
            p.mc(tp_a, f'Manfaat {noun} "{a}" adalah ....', m, wm, f'{noun.capitalize()} {a} bermanfaat: {m}.', 'easy', 'memahami', comp_a)
            p.tf(tp_a, f'Manfaat {noun} "{a}" adalah {m}.', True, f'Benar, {m}.', 'easy', 'memahami', comp_a)
            p.tf(tp_a, f'Manfaat {noun} "{a}" adalah {wm[i % len(wm)]}.', False, f'Salah. Manfaatnya: {m}.', 'medium', 'memahami', comp_a)
            p.fill(tp_a, f'Isilah: Manfaat {noun} "{a}" adalah ....', m, f'Manfaatnya: {m}.', 'medium', 'memahami', comp_a)
        if tp_b:
            p.gk = f'rb{i}'
            p.mc(tp_b, f'Perilaku yang menaati {noun} "{a}" adalah ....', t, [x] + rng.sample([y for y in tidak if y != x], 2), f'{t} sesuai dengan {noun} {a}.', 'easy', 'menganalisis', comp_b)
            p.mc(tp_b, f'Perilaku yang tidak menaati {noun} "{a}" adalah ....', x, [t] + rng.sample([y for y in taat if y != t], 2), f'{x} tidak sesuai dengan {noun} {a}.', 'medium', 'menganalisis', comp_b)
            p.tf(tp_b, f'"{t.capitalize()}" menaati {noun} "{a}".', True, f'Benar, {t} menaati {noun} {a}.', 'easy', 'menganalisis', comp_b)
            p.tf(tp_b, f'"{x.capitalize()}" menaati {noun} "{a}".', False, f'Salah, {x} tidak menaati.', 'easy', 'menganalisis', comp_b)
        if tp_c:
            p.gk = f'rc{i}'
            q = f'Di rumah ada {noun} "{a}". {nm} ingin melaksanakannya dengan baik sebagai wujud ketaatan. Yang dilakukan {nm} adalah ....'
            p.ctx(tp_c, q, t, [x] + rng.sample([y for y in tidak if y != x], 2), f'{nm} menaati dengan cara: {t}.', 'medium', 'menerapkan', comp_c)
            p.tf(tp_c, f'Terhadap {noun} "{a}", {nm} {t}.', True, f'{nm} menaati: {t}.', 'easy', 'menerapkan', comp_c)
            p.tf(tp_c, f'Terhadap {noun} "{a}", {nm} {x}.', False, f'Salah. Yang benar: {t}.', 'easy', 'menerapkan', comp_c)
            p.fill(tp_c, f'Lengkapi: Agar menaati {noun} "{a}", {nm} ....', t, f'{nm} {t}.', 'medium', 'menerapkan', comp_c, typ='completion')
    p.gk = None
    if tp_b:
        for s in range(0, len(rows) - 5, 3):
            ya = [r[1] for r in rows[s:s + 3]]; tdk = [r[2] for r in rows[s:s + 3]]
            items = ya + tdk
            rng.shuffle(items)
            p.group(tp_b, f'Kelompokkan perilaku berikut menjadi menaati atau tidak menaati {noun}: ' + '; '.join(f"'{x}'" for x in items) + '.', {'menaati': ya, 'tidak menaati': tdk}, 'Kelompokkan sesuai kepatuhan.', 'medium', 'mengelompokkan', comp_b)
    if tp_a:
        for s in range(0, len(rows) - 3, 3):
            p.match(tp_a, f'Jodohkan {noun} dengan manfaatnya!', [(r[0], r[3]) for r in rows[s:s + 4]], 'Manfaat tiap aturan.', 'medium', 'mencocokkan', comp_a)
