# -*- coding: utf-8 -*-
import sys, os, json, re, collections, random, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E

bank = E.load()
# ketertelusuran TP -> teks ATP
atp_ok = {}
for subj in E.BANKS:
    txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atp_text', E.ATPFILE[subj] + '.txt'), encoding='utf-8').read()
    parts = re.split(r'\n|\|', txt)
    segt = [set(E.toks(' '.join(parts[i:i + 4]))) for i in range(len(parts))]
    for tid, t in {x['tp_id']: x['tp'] for x in bank if x['_subj'] == subj}.items():
        tt = set(E.toks(t)); atp_ok[tid] = bool(tt) and max(len(tt & s) / len(tt) for s in segt) >= 0.8
# duplikat identik (teks soal + opsi + jawaban) lintas seluruh bank
key = lambda x: E.norm(x['question']) + '|' + E.norm(json.dumps([x.get('options'), x['answer']], ensure_ascii=False))
cnt = collections.defaultdict(list)
for x in bank: cnt[key(x)].append(x['id'])
dup = {i: ','.join(j for j in v if j != i) for v in cnt.values() if len(v) > 1 for i in v}

rng = random.Random(20261020)
sample = []
for subj in E.BANKS:
    items = [x for x in bank if x['_subj'] == subj]
    by = collections.defaultdict(list)
    for x in items: by[x['question_type']].append(x)
    pick = []
    for t, l in sorted(by.items()):
        pick += rng.sample(l, min(2, len(l)))          # minimal 2 per tipe
    rest = [x for x in items if x not in pick]
    pick += rng.sample(rest, 20 - len(pick)) if len(pick) < 20 else []
    sample += pick[:max(20, len(pick))]
res = [E.audit_one(x, atp_ok[x['tp_id']], dup.get(x['id'])) for x in sample]
json.dump(res, open('sample_audit_detail.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('sampel:', len(res), 'dari', len(bank))
print('status:', dict(collections.Counter(r['quality_status'] for r in res)))
print('per mapel:', dict(collections.Counter(r['subject'] for r in res)))
print('skor rata-rata:', {k: round(sum(r['skor'][k] for r in res) / len(res), 2) for k in res[0]['skor']})
print('issue:', dict(collections.Counter(i.split(':')[0] for r in res for i in r['issues'])))
print('KBC relevansi:', dict(collections.Counter(m['relevansi'] for r in res for m in r['kbc_mapping'])))
print('PL dimensi (dimensi, relevansi):', dict(collections.Counter((m['dimensi'], m['relevansi']) for r in res for m in r['graduate_profile_mapping'])))
print('NEEDS_REVIEW karena:', dict(collections.Counter(tuple(k for k, v in r['skor'].items() if v <= 2) for r in res if r['quality_status'] == 'NEEDS_REVIEW')))
print('PM pengalaman:', dict(collections.Counter(m['jenis'] for r in res for m in r['deep_learning_mapping']['pengalaman_belajar'])))

with open('sample_audit_summary.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['question_id', 'subject', 'tp_id', 'question_type', 'quality_status', 'skor_atp', 'skor_akurasi', 'skor_usia_bahasa', 'skor_konstruksi', 'skor_keunikan', 'issues', 'kbc_langsung', 'pl_langsung'])
    for r in res:
        w.writerow([r['question_id'], r['subject'], r['tp_id'], r['question_type'], r['quality_status']] + [r['skor'][k] for k in ('atp', 'akurasi', 'usia_bahasa', 'konstruksi', 'keunikan')] +
                   [';'.join(r['issues']), ';'.join(m['nilai'] for m in r['kbc_mapping'] if m['relevansi'] == 'langsung'), ';'.join(m['dimensi'] for m in r['graduate_profile_mapping'] if m['relevansi'] == 'langsung')])
