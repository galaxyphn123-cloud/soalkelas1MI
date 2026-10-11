# -*- coding: utf-8 -*-
"""Pembangkit umum Akidah Akhlak: fakta -> pilihan ganda, benar/salah (benar & salah), isian."""
import random

def apply(p, D, code, seed=0):
    rng = random.Random(seed)
    # --- fakta: (tp, stem diakhiri '....', benar, [salah...], penjelasan, kesulitan)
    for i, (tp, stem, ok, bad, expl, diff) in enumerate(D['facts']):
        p.gk = f'f{code}{i}'
        comp = D.get('comp', {}).get(tp, 'Memahami materi')
        cog = {1: 'memahami', 2: 'mengingat', 3: 'membandingkan', 4: 'menerapkan'}.get(tp, 'memahami')
        p.mc(tp, stem, ok, bad, expl, diff, cog, comp)
        p.tf(tp, stem.replace('....', ok), True, expl, 'easy' if diff == 'easy' else 'medium', 'mengingat', comp)
        p.tf(tp, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
        p.fill(tp, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    p.gk = None
    # --- skenario
    for si, (tp, long, short, ok, bad, expl, diff, vis) in enumerate(D['scen']):
        p.gk = f'sc{code}{si}'
        if vis:
            p.mc(tp, long, ok, bad, expl, diff, 'menerapkan', 'Menerapkan nilai dalam kehidupan', visual=vis)
            continue
        p.ctx(tp, long, ok, bad, expl, diff, 'menerapkan', 'Menerapkan nilai dalam kehidupan')
        p.tf(tp, f'{short} {ok}.', True, expl, 'easy' if diff == 'easy' else 'medium', 'memahami', 'Menerapkan nilai dalam kehidupan')
        p.tf(tp, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', 'Menerapkan nilai dalam kehidupan')
        p.fill(tp, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', 'Menerapkan nilai dalam kehidupan', typ='completion')
    p.gk = None
    for (tp, st, truth, expl) in D.get('tf', []):
        p.tf(tp, st, truth, expl, 'easy', 'memahami', D.get('comp', {}).get(tp, 'Memahami materi'))
    for (tp, q, ok, bad, expl, diff, vis) in D.get('vis', []):
        p.mc(tp, q, ok, bad, expl, diff, 'mengenali', 'Mengamati gambar', visual=vis)
    for (tp, q, g, expl) in D.get('groups', []):
        p.group(tp, q, g, expl, 'medium', 'mengelompokkan', 'Mengelompokkan contoh')
    for (tp, q, items, expl) in D.get('orders', []):
        p.order(tp, q, items, expl, 'medium', 'mengurutkan', 'Mengurutkan')
    for (tp, q, pairs, expl) in D.get('matches', []):
        p.match(tp, q, pairs, expl, 'medium', 'mencocokkan', 'Mencocokkan')
    for (tp, q, r) in D.get('perf', []):
        p.perf(tp, q, r, 'Murid menunjukkan pemahaman dan pengamalan materi.', 'medium', 'menerapkan', 'Praktik dan unjuk kerja')
    p.gk = None
