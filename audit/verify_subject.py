# -*- coding: utf-8 -*-
"""Verifikasi konsistensi mesin audit untuk satu mapel (pemeriksaan independen)."""
import sys, os, json, re, math, collections, hashlib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
subj = sys.argv[1]; slug = F.SLUG[subj]; d = os.path.join(F.HERE, slug)
res = {}
bank = json.load(open(os.path.join(E.ROOT, E.BANKS[subj]), encoding='utf-8'))
rows = json.load(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), encoding='utf-8'))
# 1. kelengkapan & integritas
ids = [x['id'] for x in bank]; rid = [r['question_id'] for r in rows]
res['jumlah_bank'] = len(ids); res['jumlah_audit'] = len(rid); res['id_sama_urutan'] = ids == rid; res['id_unik'] = len(set(rid)) == len(rid)
res['status_jumlah'] = dict(collections.Counter(r['quality_status'] for r in rows)); res['status_total_cocok'] = sum(res['status_jumlah'].values()) == len(ids)
# nomor ID: celah
nums = collections.defaultdict(list)
for i in ids:
    m = re.match(r'(.+)-(\d+)$', i); nums[m.group(1)].append(int(m.group(2)))
gaps = {k: sorted(set(range(min(v), max(v) + 1)) - set(v)) for k, v in nums.items()}
res['celah_nomor_ID'] = {k: v for k, v in gaps.items() if v}
# 2. hash bank sebelum/sesudah & tidak ada tulis ke bank
s = json.load(open(os.path.join(d, 'AUDIT_SUMMARY.json'))); cur = hashlib.sha256(open(os.path.join(E.ROOT, E.BANKS[subj]), 'rb').read()).hexdigest()
res['hash_bank_tidak_berubah'] = (s['hash_bank_sebelum'] == s['hash_bank_sesudah'] == cur)
# 3. determinisme: jalankan ulang & bandingkan hash keluaran
h1 = hashlib.sha256(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), 'rb').read()).hexdigest()
F.main(subj)
h2 = hashlib.sha256(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), 'rb').read()).hexdigest()
res['deterministik_hash_sama'] = h1 == h2
# 4. implementasi independen pemeriksaan struktur
ind = collections.Counter()
for x in bank:
    t = x['question_type']; a = x['answer']; o = x['options']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        ok = isinstance(o, list) and len(o) == 4 and a in list('ABCD')
        if not ok: ind['mc_tak_valid'] += 1
        else:
            txt = [q.split('. ', 1)[1].strip().lower() for q in o]
            if len(set(txt)) < 4: ind['opsi_kembar'] += 1
            k = txt['ABCD'.index(a)]
            L = sorted(len(q) for q in txt)
            if len(k) == L[-1] and len(k) >= 1.5 * L[-2] and len(k) > 12: ind['kunci_terpanjang_menonjol'] += 1
    if t == 'true_false' and a not in ('Benar', 'Salah'): ind['tf_tak_valid'] += 1
    if t == 'grouping' and (not isinstance(a, dict) or any(not isinstance(v, list) for v in a.values())): ind['grouping_tak_valid'] += 1
    if t in ('fill_in_short', 'completion') and isinstance(a, str) and a.lower().lstrip().startswith('contoh jawaban'): ind['isian_terbuka'] += 1
    if x['visual_required'] and not x['visual_prompt']: ind['visual_tanpa_prompt'] += 1
eng = collections.Counter()
for r in rows:
    for i in r['issues']:
        k = i.split(':')[0]
        eng[{'petunjuk_kunci_terpanjang': 'kunci_terpanjang_menonjol', 'isian_jawaban_terbuka': 'isian_terbuka', 'grouping_kunci_tak_valid': 'grouping_tak_valid', 'opsi_kembar': 'opsi_kembar', 'visual_tanpa_deskripsi': 'visual_tanpa_prompt'}.get(k, k)] += 1
res['struktur_independen'] = dict(ind); res['struktur_mesin'] = {k: eng[k] for k in ind}
res['struktur_cocok'] = all(ind[k] == eng[k] for k in ind)
# 5. validasi silang ATP: kesamaan n-gram karakter (metode berbeda dari kata kunci)
def grams(s, n=4):
    s = re.sub(r'\s+', ' ', E.norm(s)); return collections.Counter(s[i:i + n] for i in range(len(s) - n + 1))
tps = collections.OrderedDict((x['tp_id'], x['tp'] + ' ' + x['material'] + ' ' + x['competency']) for x in bank)
docs = {t: grams(v) for t, v in tps.items()}
df = collections.Counter(g for v in docs.values() for g in v)
N = len(docs)
def vec(c): return {g: (1 + math.log(n)) * math.log(1 + N / df.get(g, 1)) for g, n in c.items()}
dv = {t: vec(c) for t, c in docs.items()}
def cos(a, b):
    num = sum(a[g] * b.get(g, 0) for g in a); da = math.sqrt(sum(v * v for v in a.values())); db = math.sqrt(sum(v * v for v in b.values()))
    return num / (da * db) if da and db else 0
rank = {}
for x in bank:
    qv = vec(grams(x['question'] + ' ' + E.keytext(x)))
    sc = sorted(((cos(qv, v), t) for t, v in dv.items()), reverse=True)
    rank[x['id']] = [t for _, t in sc].index(x['tp_id']) + 1
flag = {r['question_id']: r['atp_final'] for r in rows}
def share(pred, k=3):
    ids_ = [i for i in rank if pred(flag[i])]
    return (len(ids_), round(sum(1 for i in ids_ if rank[i] > k) / max(1, len(ids_)), 3), round(sum(rank[i] for i in ids_) / max(1, len(ids_)), 2))
res['validasi_silang_ATP_ngram'] = {
    'catatan': 'persentase soal yang TP-nya berada di luar 3 teratas menurut kemiripan n-gram karakter (metode independen dari kata kunci)',
    'SELARAS_MESIN': share(lambda f: f == 'SELARAS_MESIN'), 'SELARAS_TINJAU_BACA': share(lambda f: f == 'SELARAS_TINJAU_BACA'),
    'INDIKASI_TINJAU_BACA': share(lambda f: f == 'INDIKASI_TINJAU_BACA'), 'INDIKASI_KUAT_DOKUMEN': share(lambda f: f == 'INDIKASI_KUAT_DOKUMEN'), 'format': '(jumlah, proporsi rank>3, rata-rata rank)'}
# 6. konsistensi mesin vs tinjau baca: berapa soal ATP-indikasi hasil baca yang juga ditandai mesin
mach = {r['question_id']: r['atp_tier'] for r in rows}
rd = [i for i, f in flag.items() if f.startswith('INDIKASI')]
res['tinjau_baca_vs_mesin'] = {'ATP_indikasi_hasil_baca': len(rd), 'juga_ditandai_mesin_(tier != SELARAS)': sum(1 for i in rd if mach[i] != 'SELARAS'), 'lolos_mesin_(tier=SELARAS)': sum(1 for i in rd if mach[i] == 'SELARAS')}
res['mesin_ditandai_dan_dinyatakan_selaras_oleh_bacaan'] = sum(1 for i, f in flag.items() if f == 'SELARAS_TINJAU_BACA')
json.dump(res, open(os.path.join(d, 'CONSISTENCY_CHECK.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
