# -*- coding: utf-8 -*-
"""Cetak daftar soal berstatus REVISE (untuk perbaikan) beserta alasan dan catatan tinjau baca. Pemakaian: python3 dump_revise.py "<Mapel>" <awal> <akhir>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
subj, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
d = os.path.join(F.HERE, F.SLUG[subj])
rows = [r for r in json.load(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), encoding='utf-8')) if r['quality_status'] == 'REVISE']
bank = {x['id']: x for x in E.load() if x['_subj'] == subj}
print(f'# total REVISE {subj}: {len(rows)}; menampilkan {a}..{b}')
for r in rows[a:b]:
    x = bank[r['question_id']]
    o = x['options']
    if isinstance(o, list): o = ' / '.join(('*' if s[0] == x['answer'] else '') + s for s in o) if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') else ' / '.join(o)
    elif isinstance(o, dict): o = json.dumps(o, ensure_ascii=False)
    ans = '' if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') else json.dumps(x['answer'], ensure_ascii=False)
    notes = ' || '.join(f"{t['kode']}: {t['catatan']}" for t in r['tinjau_baca'] if t['kode'] in ('KONSTRUKSI', 'BAHASA', 'AKURASI_SALAH_TEGAS'))
    vis = f" [GAMBAR: {x['visual_prompt']}]" if x['visual_required'] else ''
    print(f"## {x['id']} | {x['question_type']} | alasan: {','.join(r['alasan_status'])}\n Q: {x['question']}{vis}\n OPSI: {o}{(' | KUNCI: ' + ans) if ans else ''}\n PENJELASAN: {x['explanation']}\n CATATAN: {notes or '-'}")
