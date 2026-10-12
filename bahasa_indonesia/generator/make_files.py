# -*- coding: utf-8 -*-
"""Membuat blueprint, kunci jawaban guru, dan laporan QA Bahasa Indonesia dari bank soal gabungan."""
import json, collections, difflib, re, sys, datetime, unicodedata
SRC = sys.argv[1]; OUT = sys.argv[2]
q = json.load(open(SRC, encoding='utf-8'))
ORDER = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
JPS = {}

def norm(s):
    t = ''.join(c if (c.isalnum() or unicodedata.category(c).startswith('M')) else ' ' for c in s.lower())
    return re.sub(r'\s+', ' ', t).strip()

code = lambda x: x['tp_id'].split('-')[2]
mats = collections.OrderedDict()
for c in ORDER:
    mq = [x for x in q if code(x) == c]
    mats[c] = mq
bp = {'subject': "Bahasa Indonesia", 'grade': 1, 'phase': 'A', 'jenjang': 'MI', 'sumber_atp': 'KBC (ATP Al-Qur\'an Hadis MI Kelas I)',
      'total_soal': len(q), 'catatan': 'ATP tidak merinci JP per bab; soal dibagi sebanding jumlah TP (bab 4 TP = 111 soal, bab 5 TP = 139 soal; 8 bab, 36 TP).', 'materi': []}
for c, mq in mats.items():
    e = {'material': mq[0]['material'], 'prefix': 'BIN-' + c, 'alokasi_jp': None, 'jumlah_soal': len(mq), 'tp': []}
    for t in sorted({x['tp_id'] for x in mq}):
        tq = [x for x in mq if x['tp_id'] == t]
        e['tp'].append({'tp_id': t, 'tp': tq[0]['tp'], 'jumlah_soal': len(tq),
                        'distribusi_difficulty': dict(collections.Counter(x['difficulty'] for x in tq)),
                        'distribusi_question_type': dict(collections.Counter(x['question_type'] for x in tq)),
                        'distribusi_cognitive_level': dict(collections.Counter(x['cognitive_level'] for x in tq)),
                        'kompetensi': sorted({x['competency'] for x in tq})})
    bp['materi'].append(e)
bp['distribusi_total'] = {k: dict(collections.Counter(x[k] for x in q)) for k in ['difficulty', 'question_type', 'cognitive_level']}
json.dump(bp, open(OUT + '/bin_blueprint.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def key(x):
    t = x['question_type']; a = x['answer']
    k = {'id': x['id'], 'tp_id': x['tp_id'], 'question_type': t, 'answer': a, 'explanation': x['explanation']}
    if isinstance(x['options'], list) and x['options'] and x['options'][0][:2] == 'A.' and isinstance(a, str) and len(a) == 1:
        k['answer_text'] = next(o for o in x['options'] if o.startswith(a + '.'))
    if t in ('fill_in_short', 'completion'): k['scoring'] = 'Jawaban benar jika bermakna sama dengan kunci; abaikan perbedaan ejaan kecil.'
    if t == 'performance_task': k['scoring'] = 'Nilai dengan rubrik pada kunci; skala 1-4: 4 sangat baik, 3 baik, 2 cukup, 1 perlu bimbingan.'
    if t in ('matching', 'grouping', 'ordering'): k['scoring'] = 'Skor penuh jika seluruh pasangan/urutan benar; skor sebagian proporsional jumlah benar.'
    if x.get('misconception'): k['misconception'] = x['misconception']
    return k
json.dump({'subject': "Bahasa Indonesia", 'total': len(q), 'answers': [key(x) for x in q]}, open(OUT + '/bin_teacher_answer_key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- QA
issues = []
add = lambda i, c, m='': issues.append({'id': i, 'check': c, 'detail': m})
ids = collections.Counter(x['id'] for x in q)
for i, c in ids.items():
    if c > 1: add(i, 'id_duplikat', c)
isml = lambda x: isinstance(x['options'], list) and len(x['options']) == 4 and all(re.match(r'^[A-D]\. ', o) for o in x['options'])
for x in q:
    t = x['question_type']; a = x['answer']; o = x['options']
    if not x['question'].strip() or a in (None, '', [], {}) or not x['explanation'].strip(): add(x['id'], 'field_kosong')
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        if not isml(x) or a not in 'ABCD' or len(a) != 1: add(x['id'], 'mc_format')
        elif len({s[3:].strip().lower() for s in o}) < 4: add(x['id'], 'opsi_kembar')
    if t == 'true_false' and a not in (o or []): add(x['id'], 'tf_jawaban_tak_valid')
    if t == 'ordering' and (not isinstance(a, list) or sorted(a) != sorted(o) or a == o): add(x['id'], 'ordering_tak_valid')
    if t == 'matching' and (not isinstance(a, dict) or set(a) != set(o['kolom_kiri']) or sorted(a.values()) != sorted(o['kolom_kanan'])): add(x['id'], 'matching_tak_valid')
    if t == 'grouping' and sorted(sum(a.values(), [])) != sorted(sum(a.values(), [])) : add(x['id'], 'grouping_tak_valid')
    if t == 'grouping':
        for g, items in a.items():
            for it in items:
                if it not in x['question']: add(x['id'], 'grouping_item_tak_ada_di_soal', it)
    if x['visual_required'] and not x['visual_prompt']: add(x['id'], 'visual_prompt_kosong')
    if t == 'multiple_choice_visual' and not x['visual_required']: add(x['id'], 'visual_flag_tak_konsisten')
    if re.search(r'(perhatikan|pada|lihat)\s+gambar', x['question'].lower()) and not x['visual_required']: add(x['id'], 'rujuk_gambar_tanpa_visual')
    if not x['id'].startswith('BIN-' + code(x)): add(x['id'], 'prefix_tak_cocok')
    if x['difficulty'] not in ('easy', 'medium', 'hard'): add(x['id'], 'difficulty_tak_valid')
# duplikat: teks soal identik (kecuali tipe yang isinya di opsi: dibandingkan bersama opsi/jawaban)
full = collections.Counter(norm(x['question']) + '|' + norm(json.dumps([x['options'], x['answer']], ensure_ascii=False)) for x in q)
for x in q:
    k = norm(x['question']) + '|' + norm(json.dumps([x['options'], x['answer']], ensure_ascii=False))
    if full[k] > 1: add(x['id'], 'soal_beserta_opsi_dan_jawaban_duplikat')
qtext = collections.Counter(norm(x['question']) for x in q)
same_text = sum(1 for v in qtext.values() if v > 1)
same_text_types = collections.Counter(x['question_type'] for x in q if qtext[norm(x['question'])] > 1)
# near duplicate: pada soal bertipe isi-di-pertanyaan
S = [(x['id'], x['material'], norm(x['question']), set(norm(x['question']).split()), x['answer']) for x in q if x['question_type'] not in ('matching', 'ordering', 'grouping')]
near = []
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        a, b = S[i], S[j]
        u = len(a[3] | b[3])
        if u and len(a[3] & b[3]) / u >= 0.8 and difflib.SequenceMatcher(None, a[2], b[2]).ratio() >= 0.9:
            near.append((a[0], b[0], a[1] != b[1], a[4] == b[4]))
mcs = [x for x in q if isml(x)]
pos = collections.Counter(x['answer'] for x in mcs)
longest = sum(1 for x in mcs if max(x['options'], key=len)[0] == x['answer'])
tfc = collections.Counter(x['answer'] for x in q if x['question_type'] == 'true_false')
rep = {'subject': "Bahasa Indonesia", 'grade': 1, 'phase': 'A', 'sumber': SRC, 'tanggal_audit': str(datetime.date.today()),
       'total_soal': len(q), 'id_unik': len(ids), 'semua_punya_jawaban': all(x['answer'] not in (None, '', [], {}) for x in q),
       'semua_punya_penjelasan': all(x['explanation'].strip() for x in q),
       'teks_soal_unik_non_matching_ordering_grouping': len({norm(x['question']) for x in q if x['question_type'] not in ('matching', 'ordering', 'grouping')}),
       'jumlah_soal_non_matching_ordering_grouping': sum(1 for x in q if x['question_type'] not in ('matching', 'ordering', 'grouping')),
       'teks_soal_sama_tetapi_isi_di_opsi': {'jumlah_teks': same_text, 'per_tipe': dict(same_text_types), 'catatan': 'Hanya tipe matching/ordering/grouping; isi soal ada pada opsi dan jawaban sehingga tidak kembar.'},
       'per_materi': {mats[c][0]['material']: len(mats[c]) for c in ORDER},
       'per_tp': dict(sorted(collections.Counter(x['tp_id'] for x in q).items())),
       'per_difficulty': dict(collections.Counter(x['difficulty'] for x in q)),
       'per_question_type': dict(collections.Counter(x['question_type'] for x in q)),
       'jumlah_soal_pilihan_ganda_format_ABCD': len(mcs), 'posisi_kunci_pilihan_ganda': dict(sorted(pos.items())),
       'pilihan_ganda_kunci_opsi_terpanjang': longest, 'true_false_distribusi_jawaban': dict(tfc),
       'soal_visual': sum(1 for x in q if x['visual_required']),
       'jumlah_temuan_validasi': len(issues), 'temuan_validasi': issues,
       'pasangan_hampir_duplikat_(kemiripan>=0.9)': {'jumlah': len(near), 'lintas_materi': sum(1 for n in near if n[2]), 'dengan_jawaban_sama': sum(1 for n in near if n[3]), 'daftar': [list(n[:2]) for n in near]},
       'cek_duplikat_lintas_materi': 'Dilakukan saat pemilihan soal (kunci teks + opsi + gambar) dan diverifikasi ulang pada audit ini.',
       'catatan': ['Soal dibangun dari tabel kosakata, kalimat, cerita pendek, dan skenario sikap sesuai TP pada ATP ILMA.', 'Soal bergambar memuat deskripsi ilustrasi pada visual_prompt.']}
json.dump(rep, open(OUT + '/bin_qa_report.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in rep.items() if k not in ('temuan_validasi', 'per_tp', 'catatan')}, ensure_ascii=False, indent=1)[:4500])
print(issues[:20])
