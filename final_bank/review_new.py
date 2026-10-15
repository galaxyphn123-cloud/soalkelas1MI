# -*- coding: utf-8 -*-
"""Bandingkan penyelesaian buta atas soal baru dengan kunci; tetapkan lolos/ditolak. Argumen: folder hasil agen, berkas soal, berkas keluaran lolos, berkas ditolak."""
import json, glob, re, sys, collections, os
src, soal_f, lolos_f, tolak_f = sys.argv[1:5]
soal = json.load(open(soal_f, encoding='utf-8'))
b = {}
for f in glob.glob(src + '/out_*.json'):
    for x in json.load(open(f, encoding='utf-8'))['hasil']: b[x['id']] = x
nz = lambda s: re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', ' ', str(s).lower())).strip()
STOP = {'yang', 'dan', 'atau', 'dengan', 'untuk', 'di', 'ke', 'dari', 'itu', 'ini', 'kita', 'saya', 'adalah', 'agar', 'supaya'}

def compare(r, x):
    t, a, mine = r['question_type'], r['answer'], x.get('jawaban_saya')
    if t == 'performance_task': return True
    if mine in (None, ''): return False
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'): return str(mine).strip().upper()[:1] == a
    if t == 'true_false': return nz(mine) == nz(a)
    if t in ('fill_in_short', 'completion'):
        xs, ys = nz(mine), nz(a); st = lambda s: {w[:5] for w in s.split() if w not in STOP}
        sx, sy = st(xs), st(ys)
        return xs == ys or (ys and (ys in xs or xs in ys)) or len(sx & sy) / max(1, len(sy)) >= 0.5
    if t == 'ordering': return isinstance(mine, list) and [nz(i) for i in mine] == [nz(i) for i in a]
    try:
        if t == 'matching': return {nz(k): nz(v) for k, v in mine.items()} == {nz(k): nz(v) for k, v in a.items()}
        if t == 'grouping': return {nz(k): sorted(nz(i) for i in v) for k, v in mine.items()} == {nz(k): sorted(nz(i) for i in v) for k, v in a.items()}
    except Exception: return False
    return False

lolos, tolak = [], []
for r in soal:
    x = b.get(r['id']); why = []
    if not x: why.append('tidak ada hasil penyelesaian buta')
    else:
        if not compare(r, x): why.append('jawaban buta berbeda dari kunci: ' + str(x.get('jawaban_saya'))[:80])
        ms = [m for m in (x.get('masalah') or [])]
        if ms: why.append('penyelesai menandai ' + ','.join(ms) + ': ' + (x.get('bukti_masalah') or '')[:120])
        if x.get('kesesuaian_tp') in ('tidak', 'ragu'): why.append('TP ' + x['kesesuaian_tp'] + ': ' + (x.get('alasan_tp') or '')[:100])
        if x.get('jumlah_jawaban_benar') not in (1, None) and r['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual'): why.append('jumlah jawaban benar menurut penyelesai = ' + str(x.get('jumlah_jawaban_benar')))
    (tolak if why else lolos).append((r, why, x))
json.dump([r for r, _, _ in lolos], open(lolos_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump([{'id': r['id'], 'tp_id': r['tp_id'], 'alasan': w, 'soal': r, 'penyelesai': x} for r, w, x in tolak], open(tolak_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('lolos', len(lolos), 'ditolak', len(tolak), 'dari', len(soal), '; hasil buta ada untuk', sum(1 for r in soal if r['id'] in b))
c = collections.Counter(r['id'].split('-')[0] for r, _, _ in tolak); print(dict(c))
print(collections.Counter(w.split(':')[0][:40] for _, ws, _ in tolak for w in ws).most_common(8))
