# -*- coding: utf-8 -*-
"""Validator soal baru. Pemakaian: python3 validate_new.py <berkas_soal.json> [<berkas_tugas.json>]
Memeriksa bentuk, pengecoh, panjang kunci, TF berlubang, duplikat terhadap seluruh bank (9.000 soal FINAL) dan antarsoal baru."""
import json, sys, os, re, unicodedata, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TYPES = {'multiple_choice', 'multiple_choice_visual', 'contextual', 'true_false', 'fill_in_short', 'completion', 'matching', 'ordering', 'grouping', 'performance_task'}
MC = {'multiple_choice', 'multiple_choice_visual', 'contextual'}

def norm(s):
    t = ''.join(c if (c.isalnum() or unicodedata.category(c).startswith('M')) else ' ' for c in str(s).lower())
    return re.sub(r'\s+', ' ', t).strip()

def keytext(r):
    if r['question_type'] in MC and isinstance(r.get('options'), list) and isinstance(r.get('answer'), str):
        for x in r['options']:
            if x.startswith(r['answer'] + '.'): return x[2:].strip()
    return json.dumps(r.get('answer'), ensure_ascii=False, sort_keys=True) if isinstance(r.get('answer'), (dict, list)) else str(r.get('answer'))

_bank = None
def bank_sigs():
    global _bank
    if _bank is None:
        _bank = {}
        for fn in os.listdir(os.path.join(ROOT, 'audit/FINAL')):
            if fn.endswith('_final.json'):
                for r in json.load(open(os.path.join(ROOT, 'audit/FINAL', fn), encoding='utf-8')):
                    _bank[(norm(re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I)), norm(keytext(r)))] = r['id']
    return _bank

def check(r):
    p = []
    t = r.get('question_type'); q = r.get('question') or ''; a = r.get('answer'); o = r.get('options')
    if t not in TYPES: return ['question_type tidak dikenal']
    if not q.strip(): p.append('soal kosong')
    if len(q.split()) > 45: p.append('soal >45 kata')
    if r.get('difficulty') not in ('easy', 'medium', 'hard'): p.append('difficulty tidak valid')
    if not r.get('cognitive_level'): p.append('cognitive_level kosong')
    if not (r.get('explanation') or '').strip(): p.append('penjelasan kosong')
    if t in MC:
        if not (isinstance(o, list) and len(o) == 4 and all(re.match(r'^[ABCD]\. \S', x) for x in o) and [x[0] for x in o] == list('ABCD')): p.append('format opsi harus ["A. ..","B. ..","C. ..","D. .."]')
        elif a not in list('ABCD'): p.append('kunci harus huruf A-D')
        else:
            tx = [x[3:].strip() for x in o]
            if len({x.lower() for x in tx}) < 4: p.append('opsi kembar')
            k = tx['ABCD'.index(a)]; oth = max(len(x) for i, x in enumerate(tx) if i != 'ABCD'.index(a))
            if len(k) > 12 and len(k) >= 1.5 * oth: p.append('kunci terpanjang menonjol')
    elif t == 'true_false':
        if o != ['Benar', 'Salah'] or a not in ('Benar', 'Salah'): p.append('TF: options harus ["Benar","Salah"], answer Benar/Salah')
        if '...' in q or '....' in q: p.append('TF berlubang')
    elif t in ('fill_in_short', 'completion'):
        if o is not None or not str(a or '').strip(): p.append('isian: options harus null dan answer terisi')
        if '....' not in q and '...' not in q and t == 'completion': p.append('completion tanpa titik-titik')
    elif t == 'ordering':
        if not (isinstance(a, list) and isinstance(o, list) and sorted(a) == sorted(o) and a != o and len(a) >= 3): p.append('ordering: options harus acak dari answer (>=3 butir, urutan berbeda)')
    elif t == 'matching':
        if not (isinstance(o, dict) and isinstance(a, dict) and set(a) == set(o.get('kolom_kiri', [])) and sorted(a.values()) == sorted(o.get('kolom_kanan', [])) and o['kolom_kiri'] and len(a) >= 3): p.append('matching tidak valid (kolom_kiri/kolom_kanan, >=3 pasangan)')
    elif t == 'grouping':
        if not (isinstance(o, dict) and isinstance(o.get('kelompok'), list) and isinstance(a, dict) and set(a) == set(o['kelompok']) and all(isinstance(v, list) and v for v in a.values())): p.append('grouping tidak valid')
    elif t == 'performance_task':
        if not str(a or '').strip(): p.append('rubrik kosong')
    if r.get('visual_required') and not (r.get('visual_prompt') or '').strip(): p.append('visual_required tanpa visual_prompt')
    return p

def main(path, tugas=None):
    items = json.load(open(path, encoding='utf-8'))
    if isinstance(items, dict): items = items.get('soal', items.get('hasil', []))
    sig = bank_sigs(); seen = {}; bad = {}; per_tp = collections.Counter()
    for i, r in enumerate(items):
        pr = check(r)
        k = (norm(re.sub(r'^benar atau salah:\s*', '', r.get('question', ''), flags=re.I)), norm(keytext(r)))
        if r.get('question_type') not in ('matching', 'ordering', 'grouping', 'performance_task'):
            if k in sig: pr.append('duplikat bank: ' + sig[k])
            if k in seen: pr.append(f'duplikat dengan soal baru #{seen[k]}')
        seen.setdefault(k, i)
        per_tp[r.get('tp_id')] += 1
        if pr: bad[i] = pr
    print(f'{len(items)} soal; bermasalah {len(bad)}')
    for i, pr in list(bad.items())[:60]: print(' #%d [%s] %s | %s' % (i, items[i].get('tp_id'), '; '.join(pr), items[i].get('question', '')[:70]))
    if tugas:
        want = {t['tp_id']: t['tambah'] for t in json.load(open(tugas, encoding='utf-8'))['tp']}
        for tp, n in want.items(): 
            if per_tp[tp] != n: print(f'  JUMLAH {tp}: diminta {n}, ada {per_tp[tp]}')
        for tp in per_tp:
            if tp not in want: print('  TP tidak ada di tugas:', tp)
    return len(bad)

if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None) else 0)
