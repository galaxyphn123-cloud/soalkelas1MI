# -*- coding: utf-8 -*-
"""Pustaka pembangkit bank soal Al-Qur'an Hadis Kelas 1 MI (Fase A)."""
import random, re, collections, difflib, unicodedata

SUBJECT = "Al-Qur'an Hadis"
LET = 'ABCD'

def norm(s):
    # pertahankan tanda baca Arab (kategori M*) agar بَ dan بِ tidak dianggap sama
    t = ''.join(c if (c.isalnum() or unicodedata.category(c).startswith('M')) else ' ' for c in s.lower())
    return re.sub(r'\s+', ' ', t).strip()

class Pool:
    """Kumpulan kandidat soal satu materi. Soal duplikat (teks sama) dibuang otomatis."""
    def __init__(self, code, material, tps, quota, tpw=(1, 1, 1, 1)):
        self.code, self.material, self.tps, self.quota, self.tpw = code, material, tps, quota, tpw
        self.items, self.seen = [], set()
        self.gk = None            # penanda 'fakta' agar satu fakta tidak dipakai berlebihan

    def _add(self, d):
        k = norm(d['q'])
        if d['type'] in ('ordering', 'matching', 'grouping'):
            k += '|' + norm(str(d.get('items') or d.get('pairs') or d.get('groups')))
        if d['type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
            k += '|' + norm(d['correct'])
        if d.get('visual'):
            k += '|' + norm(d['visual'])
        if k in self.seen:
            return False
        self.seen.add(k)
        d['_gk'] = self.gk
        d['_key'] = k
        d['tp'] = min(max(d['tp'], 1), 4)
        self.items.append(d)
        return True

    # --- pembangun tipe soal -------------------------------------------------
    def mc(self, tp, q, correct, wrong, expl, diff='medium', cog='memahami', comp='', mis=None,
           typ='multiple_choice', visual=None):
        wrong = [w for w in dict.fromkeys(wrong) if w != correct]
        if len(wrong) < 3:
            raise ValueError('pengecoh kurang: ' + q)
        wrong = wrong[:3]
        return self._add(dict(tp=tp, type='multiple_choice_visual' if visual else typ, q=q, correct=correct,
                              wrong=wrong, expl=expl, diff=diff, cog=cog, comp=comp, mis=mis, visual=visual))

    def ctx(self, tp, q, correct, wrong, expl, diff='medium', cog='menerapkan', comp='', mis=None):
        return self.mc(tp, q, correct, wrong, expl, diff, cog, comp, mis, typ='contextual')

    def tf(self, tp, statement, truth, expl, diff='easy', cog='mengingat', comp='', mis=None):
        return self._add(dict(tp=tp, type='true_false', q='Benar atau salah: ' + statement, truth=truth,
                              expl=expl, diff=diff, cog=cog, comp=comp, mis=mis))

    def fill(self, tp, q, ans, expl, diff='easy', cog='mengingat', comp='', typ='fill_in_short', mis=None):
        return self._add(dict(tp=tp, type=typ, q=q, ans=ans, expl=expl, diff=diff, cog=cog, comp=comp, mis=mis))

    def order(self, tp, q, items, expl, diff='medium', cog='mengurutkan', comp=''):
        return self._add(dict(tp=tp, type='ordering', q=q, items=items, expl=expl, diff=diff, cog=cog, comp=comp))

    def match(self, tp, q, pairs, expl, diff='medium', cog='mencocokkan', comp=''):
        return self._add(dict(tp=tp, type='matching', q=q, pairs=pairs, expl=expl, diff=diff, cog=cog, comp=comp))

    def group(self, tp, q, groups, expl, diff='medium', cog='mengelompokkan', comp=''):
        return self._add(dict(tp=tp, type='grouping', q=q, groups=groups, expl=expl, diff=diff, cog=cog, comp=comp))

    def perf(self, tp, q, rubric, expl, diff='medium', cog='menerapkan', comp=''):
        return self._add(dict(tp=tp, type='performance_task', q=q, rubric=rubric, expl=expl, diff=diff, cog=cog, comp=comp))


def select(pool, rng, used=frozenset(), cap=3):
    """Pilih persis pool.quota soal: campuran tipe sesuai target, seimbang antar-TP, TF 50:50,
    dan tidak lebih dari `cap` butir dari satu 'fakta' (grup) yang sama agar tidak berulang."""
    n = pool.quota
    mix = collections.OrderedDict([
        ('multiple_choice', 0.33), ('multiple_choice_visual', 0.05), ('contextual', 0.10),
        ('true_false', 0.20), ('fill_in_short', 0.09), ('completion', 0.05),
        ('matching', 0.03), ('ordering', 0.03), ('grouping', 0.03), ('performance_task', 0.05)])
    by = collections.defaultdict(list)
    for it in pool.items:
        if it['_key'] in used:
            continue
        by[it['type']].append(it)
    for v in by.values():
        rng.shuffle(v)
    want = {t: round(n * f) for t, f in mix.items()}
    want['multiple_choice'] += n - sum(want.values())
    short = 0
    for t in list(want):
        have = len(by[t])
        if want[t] > have:
            short += want[t] - have
            want[t] = have
    for t in ('multiple_choice', 'true_false', 'contextual', 'fill_in_short'):
        room = len(by[t]) - want[t]
        take = min(room, short)
        want[t] += take
        short -= take
    if short:
        raise RuntimeError('%s kekurangan %d kandidat' % (pool.code, short))
    tpcount = collections.Counter()
    gcount = collections.Counter()

    def take(lst):
        def k(i):
            x = lst[i]
            over = 1 if (x.get('_gk') and gcount[x['_gk']] >= (2 if x['_gk'].startswith('sc') else cap)) else 0
            return (tpcount[x['tp']] / pool.tpw[x['tp'] - 1], over, i)
        x = lst.pop(min(range(len(lst)), key=k))
        tpcount[x['tp']] += 1
        if x.get('_gk'):
            gcount[x['_gk']] += 1
        return x

    chosen = []
    for t, c in want.items():
        cand = by[t]
        if t == 'true_false':
            tr = [x for x in cand if x['truth']]
            fa = [x for x in cand if not x['truth']]
            half = c // 2
            nt, nf = c - half, half
            if len(tr) < nt: nf += nt - len(tr); nt = len(tr)
            if len(fa) < nf: nt += nf - len(fa); nf = len(fa)
            for lst, k2 in ((tr, nt), (fa, nf)):
                for _ in range(k2):
                    chosen.append(take(lst))
            continue
        for _ in range(c):
            chosen.append(take(cand))
    assert len(chosen) == n, (pool.code, len(chosen), n)
    return chosen


def finalize(pools, seed=20261011):
    rng = random.Random(seed)
    records = []
    used = set()
    for pool in pools:
        ch = select(pool, rng, used)
        used |= {x['_key'] for x in ch}
        # urutkan stabil: per TP lalu urutan kemunculan; lalu acak ringan agar tipe bercampur
        ch.sort(key=lambda x: x['tp'])
        for i, it in enumerate(ch, 1):
            r = dict(id='AQH-%s-%04d' % (pool.code, i), subject=SUBJECT, grade=1, phase='A',
                     tp_id='TP-AQH-%s-%02d' % (pool.code, it['tp']), tp=pool.tps[it['tp'] - 1],
                     material=pool.material, competency=it['comp'], question_type=it['type'],
                     difficulty=it['diff'], cognitive_level=it['cog'], question=it['q'])
            t = it['type']
            if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
                r['_raw'] = it
                r['options'] = None; r['answer'] = None
            elif t == 'true_false':
                r['options'] = ['Benar', 'Salah']; r['answer'] = 'Benar' if it['truth'] else 'Salah'
            elif t in ('fill_in_short', 'completion'):
                r['options'] = None; r['answer'] = it['ans']
            elif t == 'ordering':
                r['options'] = rng.sample(it['items'], len(it['items']))
                while r['options'] == it['items']:
                    r['options'] = rng.sample(it['items'], len(it['items']))
                r['answer'] = it['items']
            elif t == 'matching':
                L = [a for a, b in it['pairs']]; R = [b for a, b in it['pairs']]
                R2 = R[:]
                while R2 == R: rng.shuffle(R2)
                r['options'] = {'kolom_kiri': L, 'kolom_kanan': R2}
                r['answer'] = {a: b for a, b in it['pairs']}
            elif t == 'grouping':
                r['options'] = {'kelompok': list(it['groups'].keys())}
                r['answer'] = it['groups']
            elif t == 'performance_task':
                r['options'] = None; r['answer'] = it['rubric']
            r['explanation'] = it['expl']
            r['visual_required'] = bool(it.get('visual'))
            r['visual_prompt'] = it.get('visual')
            if it.get('mis'): r['misconception'] = it['mis']
            r['tags'] = [r['tp_id'], pool.material.lower().replace(' ', '-')]
            records.append(r)
    # posisi kunci pilihan ganda: seimbang merata di seluruh bank
    mcs = [r for r in records if '_raw' in r]
    cyc = [LET[i % 4] for i in range(len(mcs))]
    rng.shuffle(cyc)
    for r, tgt in zip(mcs, cyc):
        it = r.pop('_raw')
        others = it['wrong'][:]; rng.shuffle(others)
        opts = others[:]; opts.insert(LET.index(tgt), it['correct'])
        r['options'] = ['%s. %s' % (LET[i], o) for i, o in enumerate(opts)]
        r['answer'] = tgt
    return records
