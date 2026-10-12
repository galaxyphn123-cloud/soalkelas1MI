# -*- coding: utf-8 -*-
import sys, os, json, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
res = {}; tot = collections.Counter(); problems = []
allq = collections.Counter()
for subj in E.BANKS:
    slug = F.SLUG[subj]
    orig = {x['id']: x for x in json.load(open(os.path.join(E.ROOT, E.BANKS[subj]), encoding='utf-8'))}
    fin = json.load(open(os.path.join(F.HERE, 'FINAL', f'{slug}_final.json'), encoding='utf-8'))
    c = collections.Counter()
    assert [x['id'] for x in fin] == list(orig), 'ID/urutan berbeda'
    for y in fin:
        o = orig[y['id']]
        for k in ('id', 'subject', 'grade', 'phase', 'tp_id', 'tp', 'material', 'competency'):
            if y[k] != o[k]: problems.append((y['id'], 'metadata inti berubah', k))
        changed = [k for k in o if y.get(k) != o[k]]
        if changed:
            c['soal_berubah'] += 1
            if not y['revision_history']: problems.append((y['id'], 'berubah tanpa riwayat', changed))
            for k in changed: c['field_' + k] += 1
            if y['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') and y['answer'] != o['answer'] : c['huruf_kunci_berubah'] += 1
        else:
            if y['revision_history']: problems.append((y['id'], 'riwayat tanpa perubahan'))
        if y['audit']['quality_status'] == 'PASS' and y['audit']['isu_struktur_tersisa']: problems.append((y['id'], 'PASS dengan isu struktur', y['audit']['isu_struktur_tersisa']))
        if y['audit']['quality_status'] == 'PASS' and y['audit']['quality_status_awal'] == 'NEEDS_REVIEW': problems.append((y['id'], 'NEEDS_REVIEW menjadi PASS'))
        if y['audit']['quality_status_awal'] == 'NEEDS_REVIEW' and changed and not any(t['kode'] == 'AKURASI_SALAH_TEGAS' for t in y['audit']['tinjau_baca']): problems.append((y['id'], 'soal NEEDS_REVIEW diubah', changed))
        allq[E.norm(y['question']) + '|' + E.norm(json.dumps([y.get('options'), y['answer']], ensure_ascii=False))] += 1
    key_changed = [y['id'] for y in fin if y['answer'] != orig[y['id']]['answer']]
    c['kunci_diubah_ID'] = key_changed
    res[subj] = dict(c)
dups = [k for k, v in allq.items() if v > 1]
res['duplikat_identik_setelah_revisi'] = len(dups)
res['masalah'] = problems[:30]; res['jumlah_masalah'] = len(problems)
json.dump(res, open(os.path.join(F.HERE, 'FINAL', 'VERIFIKASI_FINAL.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1)[:5000])
