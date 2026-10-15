# -*- coding: utf-8 -*-
"""Rakit bank final: soal PASS (versi audit/FINAL) + soal baru yang lolos verifikasi. Tidak mengubah bank asli/FINAL.
Keluaran: bank_final_lulus.json, cakupan_tp.csv, ringkasan.json"""
import json, csv, os, glob, collections, statistics, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SLUG = {'Fikih': 'fikih', 'Al-Quran Hadis': 'alquran_hadis', 'Bahasa Arab': 'bahasa_arab', 'Akidah Akhlak': 'akidah_akhlak', 'Bahasa Indonesia': 'bahasa_indonesia',
        'Matematika': 'matematika', 'Pancasila': 'pancasila', 'PJOK': 'pjok', 'Bahasa Inggris': 'bahasa_inggris'}
detail = {r['question_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'audit/QUESTION_AUDIT_DETAIL.csv'), encoding='utf-8'))}
reg = json.load(open('tp_registry.json', encoding='utf-8'))
FIELDS = ['id', 'subject', 'grade', 'phase', 'tp_id', 'tp', 'material', 'competency', 'question_type', 'difficulty', 'cognitive_level', 'question', 'options', 'answer', 'explanation', 'visual_required', 'visual_prompt', 'tags']
lama = []
for sub, slug in SLUG.items():
    for r in json.load(open(os.path.join(ROOT, f'audit/FINAL/{slug}_final.json'), encoding='utf-8')):
        if detail[r['id']]['quality_status_akhir'] == 'PASS':
            d = {k: r.get(k) for k in FIELDS}; d['sumber'] = 'BANK_PASS'; lama.append(d)
baru = json.load(open('soal_baru_lolos.json', encoding='utf-8')) if os.path.exists('soal_baru_lolos.json') else []
allq = lama + baru
by_tp = collections.defaultdict(list)
for r in allq: by_tp[r['tp_id']].append(r)
rows, perSub = [], collections.defaultdict(list)
for e in reg:
    n_lama = len([r for r in by_tp[e['tp_id']] if r['sumber'] == 'BANK_PASS']); n_baru = len([r for r in by_tp[e['tp_id']] if r['sumber'] != 'BANK_PASS'])
    rows.append(dict(subject=e['subject'], material=e['material'], tp_id=e['tp_id'], tp=e['tp'], pass_awal=n_lama, tambahan_lolos=n_baru, total_final=n_lama + n_baru, target=e['target'], tercapai='YA' if n_lama + n_baru >= e['target'] else 'TIDAK', tp_baru_dari_atp='YA' if e['baru'] else ''))
    perSub[e['subject']].append((n_lama, n_lama + n_baru))
with open('cakupan_tp.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
summ = {'total_soal_final': len(allq), 'soal_lama_pass': len(lama), 'soal_baru_lolos': len(baru), 'tp_total': len(reg), 'tp_tanpa_soal': [r['tp_id'] for r in rows if r['total_final'] == 0],
        'tp_di_bawah_target': [r['tp_id'] for r in rows if r['tercapai'] == 'TIDAK'], 'per_mapel': {}}
for s, v in perSub.items():
    a = [x[0] for x in v]; b = [x[1] for x in v]
    summ['per_mapel'][s] = {'tp': len(v), 'soal_final': sum(b), 'awal': {'min': min(a), 'median': statistics.median(a), 'maks': max(a)}, 'akhir': {'min': min(b), 'median': statistics.median(b), 'maks': max(b)}}
json.dump(allq, open('bank_final_lulus.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(summ, open('ringkasan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(summ, ensure_ascii=False, indent=1))
