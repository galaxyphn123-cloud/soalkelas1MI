# -*- coding: utf-8 -*-
"""Tahap 0-1: rekonsiliasi berkas/ID dan pemeriksaan otomatis deterministik untuk 1.220 ID antrean verifikasi.
Tidak mengubah bank mana pun (hanya membaca). Keluaran: stage1_results.json (di folder ini)."""
import json, csv, os, re, hashlib, collections, itertools, difflib, sys, unicodedata
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
A = os.path.join(ROOT, 'audit')
OUT = os.path.dirname(os.path.abspath(__file__))
SLUG = ['fikih', 'alquran_hadis', 'bahasa_arab', 'akidah_akhlak', 'bahasa_indonesia', 'matematika', 'pancasila', 'pjok', 'bahasa_inggris']

def rd(p):
    return json.load(open(os.path.join(ROOT, p), encoding='utf-8'))

def norm(s):
    t = ''.join(c if (c.isalnum() or unicodedata.category(c).startswith('M')) else ' ' for c in str(s).lower())
    return re.sub(r'\s+', ' ', t).strip()

def keytext(r):
    t, a, o = r['question_type'], r['answer'], r['options']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual') and isinstance(o, list) and isinstance(a, str) and len(a) == 1:
        for x in o:
            if x.startswith(a + '.'): return x[2:].strip()
        return None
    if isinstance(a, (list, dict)): return json.dumps(a, ensure_ascii=False, sort_keys=True)
    return str(a)

def opt_texts(r):
    return [x[2:].strip() for x in r['options']] if isinstance(r['options'], list) and r['options'] and re.match(r'^[A-D]\.', str(r['options'][0])) else []

# ------------------------------------------------------------------ muat sumber
queue = list(csv.DictReader(open(os.path.join(A, 'ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv'), encoding='utf-8')))
final, orig = {}, {}
FILES = {}
for s in SLUG:
    for r in rd(f'audit/FINAL/{s}_final.json'):
        final[r['id']] = r
for r in final.values():
    sr = r['audit']['source_ref']
    FILES.setdefault(sr['berkas_bank_asli'], None)
for f in FILES:
    for r in rd(f):
        orig[r['id']] = r
detail = {r['question_id']: r for r in csv.DictReader(open(os.path.join(A, 'QUESTION_AUDIT_DETAIL.csv'), encoding='utf-8'))}
revs = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(A, 'QUESTION_REVISIONS.csv'), encoding='utf-8')):
    revs[r['question_id']].append(r)
dups = list(csv.DictReader(open(os.path.join(A, 'DUPLICATION_REPORT.csv'), encoding='utf-8')))
atp = {}
for fn in os.listdir(os.path.join(A, 'atp_text')):
    atp[fn] = open(os.path.join(A, 'atp_text', fn), encoding='utf-8').read()
PRE_ATP = {'FIK': 'FIKIH_UNTUK_.txt', 'AQH': 'AL-QUR_AN_HA.txt', 'BAR': 'BAHASA_ARAB_.txt', 'AKA': 'AKIDAH_AKHLA.txt', 'BIN': 'B._INDONESIA.txt',
           'MTK': 'MATEMATIKA_I.txt', 'PPN': 'P_PANCASILA_.txt', 'PJK': 'PJOK.txt', 'ENG': 'ENG.txt'}

# ------------------------------------------------------------------ indeks lintas-bank
stem_map = collections.defaultdict(list)       # stem ternormalisasi -> [(id, key)]
ident = collections.defaultdict(list)
for r in final.values():
    q = norm(re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I))
    kt = keytext(r)
    if r['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual', 'true_false', 'fill_in_short', 'completion', 'short_answer'):
        stem_map[q].append((r['id'], norm(kt or '')))
    ident[(q, norm(kt or ''), r['question_type'] if r['question_type'] in ('true_false',) else '')].append(r['id'])
tok = lambda s: set(norm(s).split())
by_sub = collections.defaultdict(list)
for r in final.values(): by_sub[r['id'].split('-')[0]].append(r)

# ------------------------------------------------------------------ pemeriksaan
SYM = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '−': lambda a, b: a - b, '–': lambda a, b: a - b, '×': lambda a, b: a * b, 'x': lambda a, b: a * b, '÷': lambda a, b: a / b if b else None, ':': lambda a, b: a / b if b else None}
CHAIN = re.compile(r'(?<![\d.,])(\d+(?:\s*[+\-−–×x÷]\s*\d+)+)\s*=\s*(\d+)(?![\d.,]\d)')
EXPR = re.compile(r'(?<![\d.,])(\d+)\s*([+\-−–×x÷:])\s*(\d+)\s*=\s*(\d+)?')

def chk_structure(r):
    t, a, o = r['question_type'], r['answer'], r['options']
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        ot = opt_texts(r)
        if len(ot) != 4 or a not in list('ABCD'): return 'FAIL', 'format pilihan ganda tidak valid'
        if len({x.strip().lower() for x in ot}) < 4: return 'FAIL', 'opsi kembar'
    elif t == 'true_false':
        if a not in ('Benar', 'Salah'): return 'FAIL', 'kunci benar/salah tidak valid'
    elif t == 'ordering':
        if not (isinstance(a, list) and sorted(a) == sorted(o) and a != o): return 'FAIL', 'ordering tidak valid'
    elif t == 'matching':
        if not (isinstance(a, dict) and set(a) == set(o['kolom_kiri']) and sorted(a.values()) == sorted(o['kolom_kanan'])): return 'FAIL', 'matching tidak valid'
    elif t == 'grouping':
        if not (isinstance(a, dict) and sorted(sum(a.values(), [])) is not None): return 'FAIL', 'grouping tidak valid'
    elif t in ('fill_in_short', 'completion', 'short_answer', 'performance_task'):
        if a in (None, '', [], {}): return 'FAIL', 'kunci kosong'
    return 'PASS', ''

def chk_meta(r):
    o = orig.get(r['id']); msgs = []
    if not o: return 'FAIL', 'ID tidak ada di bank asli'
    for f in ('id', 'subject', 'grade', 'phase', 'tp_id', 'tp', 'material', 'competency'):
        if o.get(f) != r.get(f): msgs.append(f'{f} berbeda dari bank asli')
    changed = [f for f in ('question', 'options', 'answer', 'explanation', 'question_type', 'visual_prompt', 'difficulty') if o.get(f) != r.get(f)]
    hist = r.get('revision_history') or []
    covered = set()
    for h in hist: covered |= set((h.get('sebelum') or {}).keys())
    for f in changed:
        if f not in covered: msgs.append(f'{f} berubah tanpa catatan riwayat')
    if hist and not changed: msgs.append('riwayat revisi ada tetapi isi sama dengan bank asli')
    if 'answer' in changed and o['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') and o.get('answer') != r.get('answer'):
        jenis = ' '.join(' '.join(h.get('jenis') or []) for h in hist)
        if 'AKURASI_SALAH_TEGAS' not in jenis and 'kunci' not in jenis.lower(): msgs.append('huruf kunci berubah tanpa jenis revisi pembenar')
    return ('FAIL', '; '.join(msgs)) if msgs else ('PASS', '')

def eval_num(s):
    s = s.replace(',', '.')
    return s

def chk_numeric(r):
    """Hitung ulang dari pertanyaan. Mengembalikan (status, bukti). NA bila tidak ada ekspresi numerik yang dapat dihitung."""
    q = re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I)
    kt = keytext(r) or ''
    t = r['question_type']
    res = []
    # (1) ekspresi aritmetika pada soal
    for m in EXPR.finditer(q):
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
        v = SYM[op](a, b)
        if v is None: continue
        if m.group(4) is not None and t in ('true_false',):
            truth = (int(m.group(4)) == v)
            res.append(('tf', truth == (r['answer'] == 'Benar'), f'{a}{op}{b}={v}; pernyataan {"benar" if truth else "salah"}; kunci {r["answer"]}'))
        elif m.group(4) is None or '....' in q[m.end():m.end() + 8] or '...' in q[m.end():m.end() + 6]:
            ks = re.findall(r'-?\d+(?:[.,]\d+)?', kt)
            res.append(('solve', bool(ks) and float(ks[0].replace(',', '.')) == v, f'{a}{op}{b}={v}; kunci "{kt}"'))
    # (2) 'a + b = ....' dengan spasi/tanda tanya
    for m in re.finditer(r'(?<![\d.,])(\d+)\s*([+\-−–×x÷])\s*(\d+)\s*=\s*(?:\.{2,}|\?|\.\.\.\.)', q):
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3)); v = SYM[op](a, b)
        ks = re.findall(r'-?\d+', kt)
        res.append(('solve', bool(ks) and int(ks[0]) == v, f'{a}{op}{b}={v}; kunci "{kt}"'))
    # (3) bilangan terbesar/terkecil/setelah/sebelum
    nums = [int(x) for x in re.findall(r'(?<![\d])(\d+)(?![\d])', q)]
    ql = q.lower()
    if t in ('multiple_choice', 'contextual', 'multiple_choice_visual') and r['id'].startswith('MTK'):
        ot = opt_texts(r)
        def optnum(x):
            m = re.fullmatch(r'\s*(\d+)\s*', x); return int(m.group(1)) if m else None
        on = [optnum(x) for x in ot]
        if all(v is not None for v in on):
            kn = optnum(kt)
            if re.search(r'selisih|jumlah|seluruh|beda', ql): pass
            elif 'terbesar' in ql or 'paling banyak' in ql: res.append(('rank', kn == max(on), f'opsi {on}; terbesar={max(on)}; kunci={kn}'))
            elif 'terkecil' in ql or 'paling sedikit' in ql: res.append(('rank', kn == min(on), f'opsi {on}; terkecil={min(on)}; kunci={kn}'))
            m2 = re.search(r'(?:sesudah|setelah)\s+(?:bilangan\s+)?(\d+)', ql)
            m3 = re.search(r'(?:sebelum)\s+(?:bilangan\s+)?(\d+)', ql)
            if m2 and 'adalah' in ql: res.append(('next', kn == int(m2.group(1)) + 1, f'setelah {m2.group(1)} = {int(m2.group(1)) + 1}; kunci={kn}'))
            if m3 and 'adalah' in ql: res.append(('prev', kn == int(m3.group(1)) - 1, f'sebelum {m3.group(1)} = {int(m3.group(1)) - 1}; kunci={kn}'))
    if r['id'].startswith('MTK') and re.search(r'selisih antara yang terbanyak dan yang paling sedikit', ql):
        dn = [int(x) for x in re.findall(r'(\d+)', q.split('.')[0])]
        kk = re.findall(r'-?\d+', kt)
        if len(dn) >= 2 and kk: res.append(('selisih', int(kk[0]) == max(dn) - min(dn), f'data {dn}; selisih={max(dn) - min(dn)}; kunci={kk[0]}'))
    m5 = re.search(r'banyaknya seluruh data', ql)
    if r['id'].startswith('MTK') and m5:
        dn = [int(x) for x in re.findall(r'(\d+)', q.split('.')[0])]; kk = re.findall(r'-?\d+', kt)
        if dn and kk: res.append(('jumlah', int(kk[0]) == sum(dn), f'data {dn}; jumlah={sum(dn)}; kunci={kk[0]}'))
    # (4) aritmetika pada penjelasan
    ex = []
    for m in CHAIN.finditer(r.get('explanation') or ''):
        parts = re.split(r'\s*([+\-−–×x÷])\s*', m.group(1).strip())
        v = float(parts[0])
        for k in range(1, len(parts), 2):
            f = SYM[parts[k]]; v = f(v, float(parts[k + 1])) if v is not None else None
        c = float(m.group(2))
        ex.append(v is not None and abs(v - c) < 1e-9)
        if not ex[-1]: res.append(('expl', False, f'penjelasan "{m.group(0).strip()}" tetapi hasil benar {v:g}' if v is not None else 'penjelasan tak terhitung'))
    if not res and not ex: return 'NA', ''
    bad = [x for x in res if not x[1]]
    if bad: return 'FAIL', ' | '.join(x[2] for x in bad)
    return 'PASS', ' | '.join(x[2] for x in res)[:300] or 'aritmetika penjelasan benar'

def chk_keyexpl(r):
    t, a = r['question_type'], r['answer']; e = r.get('explanation') or ''
    if t == 'true_false':
        first = norm(e).split(' ')[:1]
        if first == ['benar'] and a == 'Salah': return 'FAIL', 'penjelasan diawali "Benar" tetapi kunci "Salah"'
        if first == ['salah'] and a == 'Benar': return 'FAIL', 'penjelasan diawali "Salah" tetapi kunci "Benar"'
        return 'PASS', ''
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        ot = opt_texts(r); kt = keytext(r)
        if not ot or kt is None: return 'FAIL', 'kunci tidak terpetakan ke opsi'
        en = norm(e); others = [x for i, x in enumerate(ot) if 'ABCD'[i] != a]
        hit = [x for x in others if len(norm(x)) >= 4 and norm(x) in en and norm(x) not in norm(kt) and norm(kt) not in norm(x)]
        if hit and norm(kt) not in en: return 'FAIL', f'penjelasan memuat opsi lain "{hit[0]}" tetapi tidak memuat kunci'
        return 'PASS', ''
    if t in ('fill_in_short', 'completion', 'short_answer'):
        kn = norm(a)
        if kn and kn not in norm(e) and not (tok(kn) & tok(e)): return 'WARN', 'kunci isian tidak tampak di penjelasan'
        return 'PASS', ''
    return 'PASS', ''

def chk_multi(r):
    """Heuristik lebih dari satu jawaban benar: dua opsi saling mengandung / identik secara normal / opsi lain muncul sebagai afirmasi di penjelasan."""
    if r['question_type'] not in ('multiple_choice', 'multiple_choice_visual', 'contextual'): return 'NA', ''
    ot = opt_texts(r); n = [norm(x) for x in ot]
    for i, j in itertools.combinations(range(4), 2):
        if n[i] and n[j] and (n[i] in n[j] or n[j] in n[i]) and 'ABCD'[i] == r['answer'] or (n[i] in n[j] or n[j] in n[i]) and 'ABCD'[j] == r['answer']:
            if len(n[i]) > 2 and len(n[j]) > 2: return 'WARN', f'opsi {"ABCD"[i]} dan {"ABCD"[j]} saling mengandung'
    return 'PASS', ''

def chk_conflict(r):
    q = norm(re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I))
    ks = {k for i, k in stem_map.get(q, []) if i != r['id']}
    me = norm(keytext(r) or '')
    # soal pilihan ganda dengan stem sama baru konflik bila himpunan opsinya sama
    others = []
    for i, k in stem_map.get(q, []):
        if i == r['id'] or k == me: continue
        o = final[i]
        if r['question_type'] == 'true_false' and o['question_type'] == 'true_false': others.append(i)
        elif r['question_type'] not in ('true_false',) and set(map(norm, opt_texts(r))) == set(map(norm, opt_texts(o))) and opt_texts(r): others.append(i)
        elif r['question_type'] in ('fill_in_short', 'completion', 'short_answer') and o['question_type'] in ('fill_in_short', 'completion', 'short_answer'): others.append(i)
    return ('FAIL', 'stem sama, kunci berbeda: ' + ', '.join(others[:4])) if others else ('PASS', '')

def chk_dup(r):
    q = norm(re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I)); me = norm(keytext(r) or '')
    ids = [i for i in ident.get((q, me, 'true_false' if r['question_type'] == 'true_false' else ''), []) if i != r['id']]
    ids = [i for i in ids if final[i]['question_type'] == r['question_type'] or r['question_type'] != 'true_false']
    if ids and r['question_type'] not in ('matching', 'ordering', 'grouping', 'performance_task'): return 'FAIL', 'identik: ' + ', '.join(ids[:4])
    # substantif: kemiripan token tinggi + kunci sama pada mapel yang sama (hanya pembanding yang bukan sudah identik)
    tq = tok(q); best = (0, None)
    if len(tq) >= 5:
        for o in by_sub[r['id'].split('-')[0]]:
            if o['id'] == r['id'] or o['question_type'] != r['question_type']: continue
            to = tok(re.sub(r'^benar atau salah:\s*', '', o['question'], flags=re.I))
            if not to: continue
            j = len(tq & to) / len(tq | to)
            if j > best[0] and norm(keytext(o) or '') == me: best = (j, o['id'])
    if best[0] >= 0.8: return 'WARN', f'sangat mirip ({best[0]:.2f}) dengan {best[1]}'
    return 'PASS', ''

def chk_read(r):
    q = re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I)
    words = q.split(); ot = opt_texts(r)
    sents = [s for s in re.split(r'[.!?]\s', q) if s.strip()]
    long_w = [w for w in re.findall(r'[A-Za-z]{13,}', q) if True]
    msgs = []
    if r['id'].startswith('ENG') is False and len(words) > 40: msgs.append(f'soal {len(words)} kata (>40)')
    if r['id'].startswith('ENG') and len(words) > 45: msgs.append(f'soal {len(words)} kata (>45)')
    if max([len(x.split()) for x in ot] + [0]) > 18: msgs.append('opsi sangat panjang (>18 kata)')
    if sents and max(len(s.split()) for s in sents) > 28: msgs.append('kalimat >28 kata')
    if len(long_w) >= 2: msgs.append('banyak kata panjang: ' + ', '.join(long_w[:3]))
    return ('WARN', '; '.join(msgs)) if msgs else ('PASS', f'{len(words)} kata')

def chk_mapping(r):
    a = r['audit']; msgs = []
    key_e = norm((keytext(r) or '') + ' ' + (r.get('explanation') or ''))
    tp_m = norm(r['tp'] + ' ' + r['material'])
    for m in (a.get('kbc_mapping') or []) + (a.get('graduate_profile_mapping') or []):
        if m.get('relevansi') != 'langsung': continue
        b = m.get('bukti') or {}
        if 'level_kognitif' in b:
            if norm(b['level_kognitif']) not in norm(r['cognitive_level'] + ' ' + str(b.get('level_kognitif'))) and r['cognitive_level'] not in str(b): msgs.append('level kognitif bukti tidak cocok metadata')
            continue
        k = b.get('dalam_kunci_atau_penjelasan') or []; tm = b.get('dalam_TP_materi') or []
        if not k or not all(norm(x) in key_e or any(w in key_e for w in norm(x).split()) for x in k): msgs.append(f'bukti "{k}" tidak ditemukan di kunci/penjelasan ({m.get("nilai") or m.get("dimensi")})')
        if not tm: msgs.append(f'tanpa bukti TP/materi ({m.get("nilai") or m.get("dimensi")})')
    return ('FAIL', '; '.join(msgs)) if msgs else ('PASS' if (a.get('kbc_mapping') or a.get('graduate_profile_mapping')) else 'NA', '')

def chk_atp_lex(r):
    pre = r['id'].split('-')[0]; txt = atp.get(PRE_ATP[pre], ''); tn = norm(txt)
    tp = norm(r['tp']); head = ' '.join(tp.split()[:9])
    found = head in tn
    toks = [w for w in set(norm(r['material']).split()) if len(w) > 3]
    mat = sum(1 for w in toks if w in tn) / max(1, len(toks))
    return ('PASS' if found else 'WARN'), f'TP {"ditemukan" if found else "TIDAK ditemukan harfiah"} pada teks ATP; materi {mat:.0%} istilah ada'

CHECKS = [('C01_ID_DAN_BERKAS', None), ('C02_METADATA_RIWAYAT', chk_meta), ('C03_STRUKTUR_SOAL', chk_structure), ('C04_HITUNG_ULANG', chk_numeric),
          ('C05_KUNCI_VS_PENJELASAN', chk_keyexpl), ('C06_JAWABAN_GANDA_HEURISTIK', chk_multi), ('C07_KONFLIK_KUNCI_ANTARSOAL', chk_conflict),
          ('C08_DUPLIKASI', chk_dup), ('C09_BEBAN_BACA', chk_read), ('C10_BUKTI_PEMETAAN', chk_mapping), ('C11_TP_DI_TEKS_ATP', chk_atp_lex)]

def main():
    res, recon = {}, {'antrean_baris': len(queue), 'antrean_id_unik': len({q['question_id'] for q in queue})}
    qids = [q['question_id'] for q in queue]
    recon['id_tak_ada_di_bank_final'] = [i for i in qids if i not in final]
    recon['id_tak_ada_di_bank_asli'] = [i for i in qids if i not in orig]
    recon['id_tak_ada_di_audit_detail'] = [i for i in qids if i not in detail]
    recon['needs_review_di_audit_tetapi_tidak_di_antrean'] = sorted(i for i, d in detail.items() if d['quality_status_akhir'] == 'NEEDS_REVIEW' and i not in set(qids))
    recon['antrean_tetapi_bukan_needs_review'] = [i for i in qids if detail.get(i, {}).get('quality_status_akhir') != 'NEEDS_REVIEW']
    recon['total_bank_final'] = len(final); recon['total_bank_asli'] = len(orig)
    recon['sha256_berkas_asli'] = {f: hashlib.sha256(open(os.path.join(ROOT, f), 'rb').read()).hexdigest() for f in FILES}
    extra = [i for i in recon['needs_review_di_audit_tetapi_tidak_di_antrean']]
    rows = list(queue) + [{'question_id': i, 'mapel': detail[i]['subject'], 'tp_id': detail[i]['tp_id'], 'kode_temuan': 'DI_LUAR_ANTREAN:' + (detail[i]['alasan_status'] or '')[:60]} for i in extra]
    for q in rows:
        i = q['question_id']
        if i in res:  # baris ganda
            res[i]['kode_antrean'].append(q['kode_temuan']); continue
        r = final.get(i)
        e = {'mapel': q['mapel'], 'tp_id': q['tp_id'], 'kode_antrean': [q['kode_temuan']], 'checks': {}}
        res[i] = e
        if not r:
            e['checks']['C01_ID_DAN_BERKAS'] = ['FAIL', 'ID tidak ada di bank final']; continue
        ok = i in orig and i in detail
        e['checks']['C01_ID_DAN_BERKAS'] = ['PASS' if ok else 'FAIL', '' if ok else 'tidak lengkap di bank asli/audit detail']
        for name, fn in CHECKS[1:]:
            try: s, ev = fn(r)
            except Exception as ex: s, ev = 'ERROR', repr(ex)
            e['checks'][name] = [s, ev]
    json.dump({'rekonsiliasi': recon, 'hasil': res}, open(os.path.join(OUT, 'stage1_results.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: (v if not isinstance(v, (list, dict)) else len(v)) for k, v in recon.items()}, ensure_ascii=False))
    c = collections.defaultdict(collections.Counter)
    for e in res.values():
        for n, (s, _) in e['checks'].items(): c[n][s] += 1
    for n, v in c.items(): print(n, dict(v))

if __name__ == '__main__':
    main()
