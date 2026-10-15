# -*- coding: utf-8 -*-
"""Registri TP (252 = 248 TP bank + 4 TP ATP Bahasa Indonesia yang belum ada di bank), cacah soal PASS per TP, dan rencana penambahan agar merata."""
import json, csv, os, math, statistics, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SLUG = {'Fikih': 'fikih', 'Al-Quran Hadis': 'alquran_hadis', 'Bahasa Arab': 'bahasa_arab', 'Akidah Akhlak': 'akidah_akhlak', 'Bahasa Indonesia': 'bahasa_indonesia',
        'Matematika': 'matematika', 'Pancasila': 'pancasila', 'PJOK': 'pjok', 'Bahasa Inggris': 'bahasa_inggris'}
detail = {r['question_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'audit/QUESTION_AUDIT_DETAIL.csv'), encoding='utf-8'))}
reg = collections.OrderedDict()
passed = {}
for sub, slug in SLUG.items():
    for r in json.load(open(os.path.join(ROOT, f'audit/FINAL/{slug}_final.json'), encoding='utf-8')):
        e = reg.setdefault(r['tp_id'], dict(tp_id=r['tp_id'], subject=sub, material=r['material'], tp=r['tp'], pass_ids=[], needs_review_ids=[], baru=False))
        (e['pass_ids'] if detail[r['id']]['quality_status_akhir'] == 'PASS' else e['needs_review_ids']).append(r['id'])
        passed[r['id']] = r
# 4 TP ATP Bahasa Indonesia yang tidak ada di bank (nomor TP mengikuti ATP: 2.5, 3.5, 5.5, 7.5)
NEW = [('TP-BIN-B2-05', 'Bab 2. Badanku Sehat dan Kuat', 'Murid mampu menerapkan ilmu yang dipelajari dengan sungguh-sungguh sebagai wujud rasa syukur kepada Allah Swt.', '2.5'),
       ('TP-BIN-B3-05', 'Bab 3. Keluargaku Sakinah', 'Murid mampu menunjukkan sikap belajar dengan sungguh-sungguh dalam kegiatan menyimak, membaca, dan menulis sebagai wujud menghargai ilmu yang telah diajarkan.', '3.5'),
       ('TP-BIN-B5-05', 'Bab 5. Asyiknya Bermain', 'Murid mampu menggunakan ungkapan permisi, tolong, maaf, dan terima kasih dalam kehidupan sehari-hari dengan tepat sesuai kondisi sebagai wujud mengamalkan adab sesuai ajaran Islam.', '5.5'),
       ('TP-BIN-B7-05', 'Bab 7. Sekolahku Menyenangkan', 'Murid mampu memperhatikan adab ketika bercerita sesuai ajaran Islam.', '7.5')]
# nama materi mengikuti bank
bin_mat = {t['tp_id'].split('-')[2]: t['material'] for t in reg.values() if t['subject'] == 'Bahasa Indonesia'}
for tid, _, tp, no in NEW:
    code = tid.split('-')[2]
    reg[tid] = dict(tp_id=tid, subject='Bahasa Indonesia', material=bin_mat[code], tp=tp, pass_ids=[], needs_review_ids=[], baru=True, nomor_atp=no)
med = {}
for sub in SLUG:
    v = [len(e['pass_ids']) for e in reg.values() if e['subject'] == sub and not e['baru']]
    med[sub] = math.ceil(statistics.median(v))
plan = []
for e in reg.values():
    e['jumlah_pass'] = len(e['pass_ids']); e['target'] = med[e['subject']]; e['tambah'] = max(0, e['target'] - e['jumlah_pass'])
tot = collections.Counter()
for e in reg.values(): tot[e['subject']] += e['tambah']
print('median/target per mapel:', med); print('tambahan per mapel:', dict(tot), 'total', sum(tot.values()))
json.dump(list(reg.values()), open('tp_registry.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(reg), 'TP; tanpa PASS:', [k for k, e in reg.items() if not e['jumlah_pass']])
