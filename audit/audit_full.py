# -*- coding: utf-8 -*-
"""Audit penuh satu mata pelajaran. Pemakaian: python3 -I audit_full.py "Fikih"
Keluaran ke audit/<slug>/ . Bank asli TIDAK diubah (hash sebelum/sesudah dicatat)."""
import sys, os, re, json, csv, collections, hashlib, difflib, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = {'Fikih': 'fikih', 'Al-Quran Hadis': 'alquran_hadis', 'Bahasa Arab': 'bahasa_arab', 'Akidah Akhlak': 'akidah_akhlak', 'Bahasa Indonesia': 'bahasa_indonesia',
        'Matematika': 'matematika', 'Pancasila': 'pancasila', 'PJOK': 'pjok', 'Bahasa Inggris': 'bahasa_inggris'}
INSTR = set('benar salah atau isilah titik berikut lengkapi jodohkan kelompokkan urutkan susunlah perhatikan gambar manakah mana tepat adalah yaitu disebut bagi kita seorang beberapa'.split())
STEM = E.stem

def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()

def atp_text(subj):
    return open(os.path.join(HERE, 'atp_text', E.ATPFILE[subj] + '.txt'), encoding='utf-8').read()

ATPRAW = [None]

def item_terms(x):
    k = E.keytext(x) if x['question_type'] != 'true_false' else ''
    return set(E.toks(' '.join([x['question'], k, E.qtext(x)])))

def atp_tier(x, tp_terms, other_tp_terms, atp_vocab, rare):
    """Mengembalikan (tier, bukti). Tier: SELARAS | INDIKASI_LEKSIKAL | INDIKASI_KUAT_TP_LAIN | INDIKASI_ISTILAH_ABSEN_DI_ATP"""
    it = item_terms(x)
    own = it & tp_terms[x['tp_id']]
    if own:
        return 'SELARAS', {'kata_bersama_TP_materi_kompetensi': sorted(own)[:5]}
    best, bt = None, 0
    for tid, tt in other_tp_terms.items():
        if tid == x['tp_id']: continue
        ov = it & tt
        if len(ov) > bt: best, bt = tid, len(ov)
    raw = [w for w in re.findall(r'\w+', (x['question'] + ' ' + E.keytext(x)).lower()) if len(w) >= 5 and w.isalpha() and w not in INSTR]
    absent = sorted({w for w in raw if w not in ATPRAW[0] and E.stem(w) in rare})
    if absent:
        return 'INDIKASI_ISTILAH_ABSEN_DI_ATP', {'istilah_soal_tidak_ditemukan_di_teks_ATP_CP': absent[:4], 'TP_lain_dengan_kata_bersama': best, 'jumlah_kata_bersama_TP_lain': bt}
    if best and bt >= 2:
        return 'INDIKASI_KUAT_TP_LAIN', {'TP_lain_lebih_cocok': best, 'kata_bersama': sorted(it & other_tp_terms[best])[:5]}
    return 'INDIKASI_LEKSIKAL', {'catatan': 'tidak ada kata bersama dengan TP/materi/kompetensi; istilah soal ada di teks ATP/CP'}

def dedupe_groups(items):
    """Duplikat identik & substantif. Varian bentuk (tipe berbeda pada fakta sama) dipertahankan."""
    def core(x):
        q = E.norm(x['question'])
        for p in ('benar atau salah ', 'isilah titik titik berikut ', 'isilah ', 'lengkapi '):
            if q.startswith(p): q = q[len(p):]
        return q
    ident = collections.defaultdict(list)
    for x in items:
        ident[E.norm(x['question']) + '|' + E.norm(json.dumps([x.get('options'), x['answer']], ensure_ascii=False))].append(x['id'])
    exact = [v for v in ident.values() if len(v) > 1]
    # substantif: tipe sama, inti soal sangat mirip, jawaban sama -> kandidat; tipe berbeda -> varian bentuk
    by_tp = collections.defaultdict(list)
    for x in items: by_tp[(x['tp_id'], x['question_type'])].append(x)
    subst = []
    for (tp, qt), lst in by_tp.items():
        if qt in ('matching', 'ordering', 'grouping', 'performance_task'): continue
        sets = [(x, set(core(x).split())) for x in lst]
        idx = collections.defaultdict(list)
        for i, (x, s) in enumerate(sets):
            for w in s: idx[w].append(i)
        seen = set()
        for i, (x, s) in enumerate(sets):
            cand = collections.Counter(j for w in s if len(idx[w]) < 40 for j in idx[w] if j > i)
            for j, c in cand.items():
                y, s2 = sets[j]
                jac = len(s & s2) / max(1, len(s | s2))
                if jac >= 0.75 and (x['answer'] == y['answer'] or qt == 'true_false'):
                    if difflib.SequenceMatcher(None, core(x), core(y)).ratio() >= 0.9 and x['answer'] == y['answer'] and (i, j) not in seen:
                        seen.add((i, j)); subst.append((x['id'], y['id'], round(jac, 2)))
    return exact, subst

STRUCT_FATAL = ('mc_kunci_tak_valid', 'kunci_ganda', 'tf_kunci_tak_valid', 'isian_tanpa_kunci', 'opsi_kembar', 'mc_opsi_bukan_4', 'visual_tanpa_deskripsi', 'metadata_kosong', 'grouping_kunci_tak_valid', 'matching_kunci_tak_valid', 'ordering_kunci_tak_valid', 'isian_jawaban_terbuka')
MANUAL = {}
MANUAL_LOADED = False

def load_manual(slug):
    global MANUAL, MANUAL_LOADED
    p = os.path.join(HERE, slug, 'manual_review.json')
    if os.path.exists(p):
        d = json.load(open(p, encoding='utf-8')); MANUAL = d['temuan']; MANUAL_LOADED = True
    else:
        MANUAL, MANUAL_LOADED = {}, False

def main(subj):
    load_manual(SLUG[subj])
    out = os.path.join(HERE, SLUG[subj]); os.makedirs(out, exist_ok=True)
    src = os.path.join(E.ROOT, E.BANKS[subj]); h0 = sha(src)
    items = [x for x in E.load() if x['_subj'] == subj]
    allbank = E.load()
    n0 = len(items)
    txt = atp_text(subj)
    atp_vocab = set(E.toks(txt)); ATPRAW[0] = txt.lower()
    # TP -> istilah
    tps = collections.OrderedDict((x['tp_id'], x) for x in items)
    tp_terms = {tid: set(E.toks(x['tp'] + ' ' + x['material'] + ' ' + x['competency'])) for tid, x in tps.items()}
    df = collections.Counter()
    for x in items: df.update(item_terms(x))
    rare = {t for t, c in df.items() if c <= 8}
    # ketertelusuran TP -> ATP
    parts = re.split(r'\n|\|', txt); segt = [set(E.toks(' '.join(parts[i:i + 4]))) for i in range(len(parts))]
    tp_trace = {tid: round(max(len(set(E.toks(x['tp'])) & s) / max(1, len(set(E.toks(x['tp'])))) for s in segt), 2) for tid, x in tps.items()}
    atp_ok = {tid: v >= 0.8 for tid, v in tp_trace.items()}
    exact, subst = dedupe_groups(items)
    dupmap = collections.defaultdict(list)
    for g in exact:
        for i in g: dupmap[i] += [j for j in g if j != i]
    submap = collections.defaultdict(list)
    for a, b, j in subst: submap[a].append(b); submap[b].append(a)
    rows = []
    for x in items:
        base = E.audit_one(x, atp_ok[x['tp_id']], ','.join(dupmap[x['id']]) or None)
        tier, ebid = atp_tier(x, tp_terms, tp_terms, atp_vocab, rare)
        iss = list(base['issues'])
        man = MANUAL.get(x['id'], [])
        mcodes = {m['kode'] for m in man}
        fatal = [i for i in iss if i.split(':')[0] in STRUCT_FATAL]
        if dupmap[x['id']]: iss.append('duplikat_identik:' + ','.join(dupmap[x['id']]))
        if submap[x['id']]: iss.append('duplikat_substantif_kandidat:' + ','.join(submap[x['id']][:3]))
        # tingkat keselarasan ATP final: mesin (screening) + tinjauan baca
        if mcodes & {'ATP_INDIKASI_KUAT'}: atp_final = 'INDIKASI_KUAT_DOKUMEN'
        elif mcodes & {'ATP_INDIKASI'}: atp_final = 'INDIKASI_TINJAU_BACA'
        elif tier == 'SELARAS': atp_final = 'SELARAS_MESIN'
        else: atp_final = 'SELARAS_TINJAU_BACA' if MANUAL_LOADED else 'BELUM_DITINJAU_' + tier
        for m in man: iss.append(f"tinjau_baca_{m['kode']}")
        expert = mcodes & {'ATP_INDIKASI_KUAT', 'ATP_INDIKASI', 'AKURASI_AHLI', 'AKURASI_KONFLIK_INTERNAL', 'AMBIGU', 'DISTRAKTOR_AMBIGU', 'USIA_ISI'}
        reasons = []
        if expert or atp_final.startswith('BELUM_DITINJAU') or base['skor']['usia_bahasa'] <= 1 or submap[x['id']]:
            status = 'NEEDS_REVIEW'
            reasons = sorted(expert) + (['ATP_leksikal_belum_ditinjau'] if atp_final.startswith('BELUM') else []) + (['beban_baca_tinggi'] if base['skor']['usia_bahasa'] <= 1 else []) + (['kandidat_duplikat_substantif'] if submap[x['id']] else [])
        elif fatal or dupmap[x['id']] or mcodes & {'KONSTRUKSI', 'BAHASA'} or any(i.startswith(('petunjuk_kunci_terpanjang', 'rujuk_gambar', 'opsi_semua')) for i in iss):
            status = 'REVISE'
            reasons = [i.split(':')[0] for i in iss if i.split(':')[0] in STRUCT_FATAL or i.startswith(('petunjuk_kunci_terpanjang', 'rujuk_gambar', 'opsi_semua'))] + sorted(mcodes & {'KONSTRUKSI', 'BAHASA'}) + (['duplikat_identik'] if dupmap[x['id']] else [])
        else:
            status = 'PASS'
        base.update(quality_status=status, issues=iss, atp_tier=tier, atp_final=atp_final, atp_bukti=ebid, alasan_status=reasons, tinjau_baca=man)
        base['recommended_action'] = {
            'PASS': 'tidak ada tindakan',
            'REVISE': 'perbaiki sesuai isu (jangan ubah kebenaran jawaban/TP/kompetensi); catat di riwayat revisi',
            'NEEDS_REVIEW': 'TAHAN: jangan ubah/pindah/hapus sebelum keputusan guru/ahli (' + ', '.join(reasons) + ')',
            'REJECT': 'diputuskan ahli'}[status]
        base['meta'] = {k: x[k] for k in ('tp', 'material', 'difficulty', 'cognitive_level')}
        base['source'] = E.BANKS[subj]
        base['atp_trace_tp'] = tp_trace[x['tp_id']]
        base['recommended_action'] = {
            'PASS': 'tidak ada tindakan', 'REVISE': 'perbaiki sesuai isu (jangan ubah kebenaran jawaban); jangan ubah TP/kompetensi',
            'NEEDS_REVIEW': 'tahan perubahan; minta keputusan guru/ahli ' + ('(ATP/TP)' if tier != 'SELARAS' else '(bahasa/duplikat)'), 'REJECT': 'diputuskan ahli'}[status]
        base['meta'] = {k: x[k] for k in ('tp', 'material', 'difficulty', 'cognitive_level')}
        base['source'] = E.BANKS[subj]
        rows.append(base)
    assert len(rows) == n0 and len({r['question_id'] for r in rows}) == n0
    h1 = sha(src); assert h0 == h1, 'bank asli berubah!'
    json.dump(rows, open(os.path.join(out, 'QUESTION_AUDIT_DETAIL.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(out, 'QUESTION_AUDIT_DETAIL.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['question_id', 'subject', 'tp_id', 'tp_text', 'material', 'question_type', 'difficulty', 'cognitive_level', 'skor_atp', 'skor_akurasi', 'skor_usia_bahasa', 'skor_konstruksi', 'skor_keunikan',
                    'atp_tier_mesin', 'atp_final', 'quality_status', 'alasan_status', 'issues', 'recommended_action', 'kbc_langsung', 'kbc_konteks_atau_melalui_TP', 'dl_pengalaman', 'dl_prinsip', 'pl_langsung_dimensi_subdimensi', 'pl_catatan_pengukuran', 'tinjau_baca_kode_catatan', 'source'])
        for r in rows:
            k = r['kbc_mapping']; l = r['graduate_profile_mapping']
            w.writerow([r['question_id'], r['subject'], r['tp_id'], r['meta']['tp'], r['meta']['material'], r['question_type'], r['meta']['difficulty'], r['meta']['cognitive_level']] + [r['skor'][a] for a in ('atp', 'akurasi', 'usia_bahasa', 'konstruksi', 'keunikan')] +
                       [r['atp_tier'], r['atp_final'], r['quality_status'], ';'.join(r['alasan_status']), ';'.join(r['issues']), r['recommended_action'],
                        ';'.join(f"{m['nilai']}[{','.join(sum(m['bukti'].values(), []))}]" for m in k if m['relevansi'] == 'langsung'), ';'.join(f"{m['nilai']}({m['relevansi']})" for m in k if m['relevansi'] in ('konteks', 'melalui_TP')),
                        ';'.join(a['jenis'] for a in r['deep_learning_mapping']['pengalaman_belajar']), ';'.join(a['jenis'] for a in r['deep_learning_mapping']['prinsip']),
                        ';'.join(f"{m['dimensi']}/{m['subdimensi']}" for m in l if m['relevansi'] == 'langsung'), ';'.join(sorted({m['keterbatasan'] for m in l if m['relevansi'] == 'langsung'})), ' || '.join(f"{t['kode']}: {t['catatan']}" for t in r['tinjau_baca']), r['source']])
    # --- duplikasi
    with open(os.path.join(out, 'DUPLICATION_REPORT.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['jenis', 'id_1', 'id_2', 'kemiripan', 'tindakan_disarankan'])
        for g in exact:
            for a, b in itertools.combinations(g, 2): w.writerow(['identik', a, b, 1.0, 'tinjau; hapus hanya setelah keputusan (ID asli tidak dihapus)'])
        for a, b, j in subst: w.writerow(['substantif_kandidat', a, b, j, 'tinjau; pertahankan bila berfungsi berbeda (pengenalan/penerapan/remedial)'])
    # --- cakupan ATP per TP
    qmap = {r['question_id']: r for r in rows}
    cov = []
    for tid, tx in tps.items():
        tq = [x for x in items if x['tp_id'] == tid]; st = collections.Counter(qmap[x['id']]['quality_status'] for x in tq)
        types = collections.Counter(x['question_type'] for x in tq)
        praktik = bool(re.search(r'mempraktikkan|meniru|menerapkan|melafalkan', tx['tp'].lower()))
        prak_share = (types['performance_task'] + types['contextual'] + types['completion']) / len(tq)
        facts = len({E.norm(x['question']).replace('benar atau salah ', '').replace('isilah titik titik berikut ', '') for x in tq})
        notes = []
        if len(tq) < 30: notes.append('jumlah soal sedikit')
        if praktik and prak_share < 0.15: notes.append('TP berverba praktik/penerapan tetapi porsi soal penerapan/praktik <15%: perlu aktivitas pendamping praktik')
        if types['true_false'] / len(tq) > 0.35: notes.append('proporsi benar/salah tinggi')
        tfb = collections.Counter(x['answer'] for x in tq if x['question_type'] == 'true_false')
        if tfb and max(tfb.values()) / sum(tfb.values()) > 0.7: notes.append(f'jawaban benar/salah condong ({dict(tfb)})')
        sub_n = sum(1 for x in tq if submap[x['id']])
        if sub_n / len(tq) > 0.15: notes.append(f'{sub_n} soal berstatus kandidat duplikat substantif')
        cov.append(dict(tp_id=tid, material=tx['material'], tp_text=tx['tp'], atp_trace=tp_trace[tid], jumlah_soal=len(tq), PASS=st['PASS'], REVISE=st['REVISE'], NEEDS_REVIEW=st['NEEDS_REVIEW'], REJECT=st['REJECT'],
                        tipe=dict(types), kesulitan=dict(collections.Counter(x['difficulty'] for x in tq)), level_kognitif=dict(collections.Counter(x['cognitive_level'] for x in tq)),
                        kualitas_cakupan='perlu_perhatian' if notes else 'memadai', kekurangan=notes))
    with open(os.path.join(out, 'ATP_COVERAGE_MATRIX.json'), 'w', encoding='utf-8') as f: json.dump(cov, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out, 'ATP_COVERAGE_MATRIX.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['tp_id', 'material', 'tp_text', 'kemiripan_TP_ke_ATP', 'jumlah_soal', 'PASS', 'REVISE', 'NEEDS_REVIEW', 'REJECT', 'tipe', 'kesulitan', 'level_kognitif', 'kualitas_cakupan', 'kekurangan_dan_rekomendasi'])
        for c in cov: w.writerow([c['tp_id'], c['material'], c['tp_text'], c['atp_trace'], c['jumlah_soal'], c['PASS'], c['REVISE'], c['NEEDS_REVIEW'], c['REJECT'], json.dumps(c['tipe'], ensure_ascii=False), json.dumps(c['kesulitan']), json.dumps(c['level_kognitif'], ensure_ascii=False), c['kualitas_cakupan'], ' | '.join(c['kekurangan'])])
    # --- profil KBC / DL / PL
    prof = {'KBC_langsung': collections.Counter(), 'KBC_konteks': collections.Counter(), 'KBC_melalui_TP': collections.Counter(), 'DL_pengalaman': collections.Counter(), 'DL_prinsip': collections.Counter(), 'PL_langsung': collections.Counter(), 'PL_melalui_TP': collections.Counter(), 'PL_indikatif': collections.Counter()}
    per_tp = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for r in rows:
        for m in r['kbc_mapping']:
            if m['relevansi'] == 'langsung': prof['KBC_langsung'][m['nilai']] += 1; per_tp[r['tp_id']]['KBC_langsung'][m['nilai']] += 1
            elif m['relevansi'] == 'konteks': prof['KBC_konteks'][m['nilai']] += 1
            elif m['relevansi'] == 'melalui_TP': prof['KBC_melalui_TP'][m['nilai']] += 1
        for a in r['deep_learning_mapping']['pengalaman_belajar']: prof['DL_pengalaman'][a['jenis']] += 1
        for a in r['deep_learning_mapping']['prinsip']: prof['DL_prinsip'][a['jenis']] += 1
        for m in r['graduate_profile_mapping']:
            key = {'langsung': 'PL_langsung', 'melalui_TP': 'PL_melalui_TP', 'indikatif': 'PL_indikatif'}[m['relevansi']]
            prof[key][f"{m['dimensi']} / {m['subdimensi']}"] += 1
            if m['relevansi'] == 'langsung': per_tp[r['tp_id']]['PL_langsung'][m['dimensi']] += 1
    json.dump({'catatan': 'Jumlah label bukan bukti keberhasilan kurikulum; satu soal dapat memiliki lebih dari satu label. Semua label adalah USULAN berbukti yang perlu diverifikasi guru/ahli.',
               'ringkasan': {k: dict(v) for k, v in prof.items()}, 'per_tp': {k: {a: dict(b) for a, b in v.items()} for k, v in per_tp.items()}},
              open(os.path.join(out, 'KBC_DEEP_LEARNING_PROFILE_MATRIX.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # --- ringkasan statistik
    st = collections.Counter(r['quality_status'] for r in rows)
    mc = [x for x in items if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') and isinstance(x['options'], list)]
    longest = sum(1 for x in mc if len(x['options']['ABCD'.index(x['answer'])][3:]) == max(len(o) - 3 for o in x['options']))
    tf = collections.Counter(x['answer'] for x in items if x['question_type'] == 'true_false')
    summ = dict(mapel=subj, tanggal='2026-10-12', soal_awal=n0, soal_diperiksa=len(rows), status=dict(st), valid_PASS=st['PASS'], perlu_revisi=st['REVISE'], ditolak=st['REJECT'], perlu_ahli=st['NEEDS_REVIEW'],
                duplikat_identik_ID=sum(1 for v in dupmap.values() if v), duplikat_substantif_pasangan=len(subst), tanpa_pemetaan_TP=sum(1 for t, v in atp_ok.items() if not v),
                atp_tier_mesin=dict(collections.Counter(r['atp_tier'] for r in rows)), atp_final=dict(collections.Counter(r['atp_final'] for r in rows)), tinjau_baca_kode=dict(collections.Counter(t['kode'] for r in rows for t in r['tinjau_baca'])), tinjau_baca_dimuat=MANUAL_LOADED, issue=dict(collections.Counter(i.split(':')[0] for r in rows for i in r['issues'])),
                kesulitan=dict(collections.Counter(x['difficulty'] for x in items)), level_kognitif=dict(collections.Counter(x['cognitive_level'] for x in items)), tipe=dict(collections.Counter(x['question_type'] for x in items)),
                kunci_pilgan_posisi=dict(collections.Counter(x['answer'] for x in mc)), kunci_opsi_terpanjang=f'{longest}/{len(mc)}', tf_jawaban=dict(tf),
                hash_bank_sebelum=h0, hash_bank_sesudah=h1, profil=json.loads(json.dumps({k: dict(v) for k, v in prof.items()})))
    json.dump(summ, open(os.path.join(out, 'AUDIT_SUMMARY.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'mapel': subj, 'selesai': True, 'jumlah_diproses': len(rows), 'id_terakhir': rows[-1]['question_id']}, open(os.path.join(out, 'progress.json'), 'w'), indent=1)
    return summ, rows, cov

if __name__ == '__main__':
    s, rows, cov = main(sys.argv[1])
    print(json.dumps({k: v for k, v in s.items() if k not in ('profil', 'level_kognitif')}, ensure_ascii=False, indent=1))
