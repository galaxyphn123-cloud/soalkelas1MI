# -*- coding: utf-8 -*-
"""Pembangkit soal tambahan Bahasa Arab Kelas 1 MI (Bab III Hobiku, Bab V Buah, Bab VI Warna) berdasarkan KKTP.
Memakai mesin pembangkit bank asli (../generator) tanpa mengubahnya.
Pemakaian: python3 build_kktp.py <keluaran.json> [dry]"""
import sys, os, json, collections, types
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'generator'))
sys.path.insert(0, HERE)
import lib, arab_gen
import kktp_data as D

QUOTA = {'HB': 110, 'BH': 110, 'WR': 110}
SIKAP_KOMUNIKASI = {'HB': 3, 'BH': 1, 'WR': 1}   # TP tempat butir percakapan ditaruh
DEM_KE_TP1 = ('BH', 'WR')                          # butir kata tunjuk (هذا/هذه) masuk TP1 pada bab ini
COMP = 'Menerapkan sikap dan ungkapan'


class P(lib.Pool):
    direct = False

    def _add(self, d):
        if not self.direct:
            q = d['q']; tp = d['tp']; c = self.code
            dem = any(k in q for k in ('tunjuk', 'هٰذَا', 'هٰذِهِ', 'menunjuk', 'mudzakkar', 'muannats'))
            if q.startswith(('Dalam percakapan', 'Susun percakapan', 'Jodohkan pertanyaan')) or 'dijawab dengan' in q:
                tp = SIKAP_KOMUNIKASI[c]
            elif q.startswith('Bacalah teks berikut'):
                tp = 1
            elif tp in (2, 3, 4):
                tp = 1 if ((c in DEM_KE_TP1 and dem) or (c == 'HB' and 'tanya' in q)) else 2
            d['tp'] = tp
        return super()._add(d)


def apply(p, code):
    p.direct = True
    for si, (tp, long, short, ok, bad, expl, diff) in enumerate(D.SCEN[code]):
        p.gk = f'sc{code}{si}'
        p.ctx(tp, long, ok, bad, expl, diff, 'menerapkan', COMP)
        p.tf(tp, f'{short} {ok}.', True, expl, 'easy' if diff == 'easy' else 'medium', 'memahami', COMP)
        p.tf(tp, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', COMP)
        p.fill(tp, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', COMP, typ='completion')
    p.gk = None
    for fi, (tp, st, truth, expl) in enumerate(D.ADAB[code]):
        p.gk = f'ad{code}{fi}'
        p.tf(tp, st, truth, expl, 'easy', 'memahami', COMP)
    p.gk = None
    for tp, q in D.PERF[code]:
        rub = ('Dinilai guru: ketepatan bentuk huruf hijaiyah (sambung/pisah dan harakat), kerapian, dan kelengkapan hasil (skala 1-4).'
               if tp == 2 else 'Dinilai guru: ketepatan ungkapan/lafal, keberanian, dan kesantunan (skala 1-4).')
        p.perf(tp, q, rub, 'Murid menunjukkan penerapan ungkapan dan sikap yang sesuai.', 'medium', 'menerapkan', COMP)
    for tp, q, g in D.GROUPS[code]:
        p.group(tp, q, g, 'Kelompokkan sesuai makna dan jenisnya.', 'medium', 'mengelompokkan', COMP)
    for tp, q, items in D.ORDERS[code]:
        p.order(tp, q, items, 'Urutan yang benar: ' + ' → '.join(items) + '.', 'medium', 'mengurutkan', COMP)
    if code == 'BH':
        for i, (tp, q, ok, bad, expl, diff) in enumerate(D.BH_PISAH):
            p.gk = f'ps{i}'
            p.mc(tp, q, ok, bad, expl, diff, 'menganalisis', 'Memahami huruf pisah dan sambung')
        p.gk = None
        for st, truth, expl in D.BH_PISAH_TF:
            p.tf(2, st, truth, expl, 'medium', 'menganalisis', 'Memahami huruf pisah dan sambung')
    p.direct = False


arab_gen.MATERI = D.MATERI                                         # distraktor dialog hanya dari bab tambahan
arab_gen.arab_scen = types.SimpleNamespace(apply=apply)


def _n(x):
    return lib.norm(str(x))


def _sig_old(r):
    t, a, o = r['question_type'], r['answer'], r['options']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        a = next(x[3:] for x in o if x.startswith(a + '.'))
    elif t in ('matching', 'grouping', 'performance_task'):
        a = ''
    if t == 'ordering':
        a = a
    return _n(r['question']) + '|' + _n(a)


def _sig_new(it):
    t = it['type']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        a = it['correct']
    elif t == 'true_false':
        a = 'Benar' if it['truth'] else 'Salah'
    elif t in ('fill_in_short', 'completion'):
        a = it['ans']
    elif t == 'ordering':
        a = it['items']
    else:
        a = ''
    q = it['q'] if t != 'true_false' else it['q']
    return _n(q) + '|' + _n(a)


def _kunci_menonjol(it):
    if it['type'] not in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        return False
    k = len(it['correct'])
    return k > 12 and k >= 1.5 * max(len(w) for w in it['wrong'])


_OLD = {_sig_old(r) for r in json.load(open(os.path.join(HERE, '..', 'bar_bank_1000.json'), encoding='utf-8'))}


def pools():
    out = []
    for i, M in enumerate(D.MATERI):
        p = P(M['code'], M['name'], M['tps'], QUOTA[M['code']], tpw=(1,) * len(M['tps']))
        p.cap = 6
        arab_gen.gen(p, M, 70 + i)
        before = len(p.items)
        p.items = [x for x in p.items if x['type'] in ('matching', 'grouping', 'performance_task') or _sig_new(x) not in _OLD]
        p.items = [x for x in p.items if not _kunci_menonjol(x)]
        print(M['code'], 'dibuang karena identik dengan bank asli:', before - len(p.items), file=sys.stderr)
        out.append(p)
    return out


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'dry':
        for p in pools():
            print(p.code, len(p.items), dict(sorted(collections.Counter(x['tp'] for x in p.items).items())), dict(collections.Counter(x['type'] for x in p.items)))
        sys.exit()
    recs = lib.finalize(pools(), seed=20261013)
    for r in recs:
        r['sumber_kktp'] = 'KKTP Bahasa Arab Kelas I (Deep Learning), ' + next(m['kktp_bab'] for m in D.MATERI if m['code'] == r['tp_id'].split('-')[2])
        r['status_verifikasi'] = 'BELUM_DIVERIFIKASI_AHLI'
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
