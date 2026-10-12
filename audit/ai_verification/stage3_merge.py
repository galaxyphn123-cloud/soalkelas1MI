# -*- coding: utf-8 -*-
"""Tahap 3-4: gabungkan hasil pemeriksaan deterministik (stage1) dengan penyelesaian buta oleh agen (stage2),
bandingkan dengan kunci, tetapkan status berbasis aturan, tulis lima berkas keluaran. Tidak mengubah bank."""
import json, csv, os, re, glob, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = '/tmp/claude-0/-home-user-soalkelas1MI/df7a5113-ba96-58a1-b311-412b61c68bd2/scratchpad/blind'
sys.path.insert(0, HERE)

s1 = json.load(open(os.path.join(HERE, 'stage1_results.json'), encoding='utf-8'))
recon, hasil = s1['rekonsiliasi'], s1['hasil']
fin = {}
for s in ['fikih', 'alquran_hadis', 'bahasa_arab', 'akidah_akhlak', 'bahasa_indonesia', 'matematika', 'pancasila', 'pjok', 'bahasa_inggris']:
    for r in json.load(open(os.path.join(ROOT, f'audit/FINAL/{s}_final.json'), encoding='utf-8')): fin[r['id']] = r
detail = {r['question_id']: r for r in csv.DictReader(open(os.path.join(ROOT, 'audit/QUESTION_AUDIT_DETAIL.csv'), encoding='utf-8'))}
queue = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(ROOT, 'audit/ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv'), encoding='utf-8')):
    queue[r['question_id']].append(r)

blind = {}
for f in sorted(glob.glob(SP + '/out_*.json')):
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception as e: print('GAGAL baca', f, e); continue
    for x in d.get('hasil', []): blind[x['id']] = x

def nz(s): return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', ' ', str(s).lower())).strip()

def compare(r, b):
    """Bandingkan jawaban buta dengan kunci. Kembalikan ('COCOK'|'BEDA'|'NA', rincian)."""
    t, a = r['question_type'], r['answer']; mine = b.get('jawaban_saya')
    if t == 'performance_task': return 'NA', 'tugas unjuk kerja (dinilai rubrik)'
    if mine in (None, ''): return 'NA', 'agen tidak memberi jawaban'
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        m = str(mine).strip().upper()[:1]
        return ('COCOK' if m == a else 'BEDA'), f'agen={m}; kunci={a}'
    if t == 'true_false':
        return ('COCOK' if nz(mine) == nz(a) else 'BEDA'), f'agen={mine}; kunci={a}'
    if t in ('fill_in_short', 'completion', 'short_answer'):
        x, y = nz(mine), nz(a)
        ok = x == y or (y and (y in x or x in y)) or (set(x.split()) and set(x.split()) == set(y.split()))
        return ('COCOK' if ok else 'BEDA'), f'agen="{mine}"; kunci="{a}"'
    if t == 'ordering':
        return ('COCOK' if [nz(i) for i in (mine if isinstance(mine, list) else [])] == [nz(i) for i in a] else 'BEDA'), f'agen={mine}; kunci={a}'
    if t in ('matching', 'grouping'):
        try:
            if t == 'matching': ok = {nz(k): nz(v) for k, v in mine.items()} == {nz(k): nz(v) for k, v in a.items()}
            else: ok = {nz(k): sorted(nz(i) for i in v) for k, v in mine.items()} == {nz(k): sorted(nz(i) for i in v) for k, v in a.items()}
        except Exception: ok = False
        return ('COCOK' if ok else 'BEDA'), f'agen={json.dumps(mine, ensure_ascii=False)[:120]}; kunci={json.dumps(a, ensure_ascii=False)[:120]}'
    return 'NA', ''

AGAMA = ('FIK', 'AKA', 'AQH', 'BAR')
HARD = {'JAWABAN_GANDA', 'TIDAK_ADA_JAWABAN', 'FAKTA_SALAH', 'KONTRADIKSI_INTERNAL'}
SOFT = {'AMBIGU', 'USIA', 'BAHASA', 'BEBAN_BACA', 'TP_TIDAK_SELARAS', 'LAIN'}

def decide(i):
    r = fin[i]; e = hasil[i]; ck = e['checks']; b = blind.get(i); pre = i.split('-')[0]
    issues = []   # (kode, bukti, hasil_independen, sumber, keyakinan, alasan_keyakinan, rekomendasi, wajib_manusia)
    st = None
    kodes = set()
    for q in queue.get(i, []): kodes |= {k.strip() for k in q['kode_temuan'].split(';')}
    def add(*a): issues.append(a)
    # --- deterministik
    for n, (s, ev) in ck.items():
        if n == 'C04_HITUNG_ULANG' and s == 'FAIL':
            add('HITUNG_TIDAK_COCOK', ev, 'hitung ulang dari pertanyaan oleh skrip tidak sama dengan kunci/penjelasan', 'perhitungan skrip (aritmetika)', 'tinggi', 'aritmetika deterministik', 'periksa dan koreksi kunci/penjelasan', False)
        if n == 'C03_STRUKTUR_SOAL' and s == 'FAIL': add('STRUKTUR', ev, 'format soal tidak valid', 'validator struktur', 'tinggi', 'aturan format', 'perbaiki format', False)
        if n == 'C05_KUNCI_VS_PENJELASAN' and s == 'FAIL': add('KUNCI_VS_PENJELASAN', ev, 'penjelasan bertentangan dengan kunci', 'teks soal', 'sedang', 'pencocokan teks', 'periksa kunci', True)
        if n == 'C07_KONFLIK_KUNCI_ANTARSOAL' and s == 'FAIL': add('KONFLIK_KUNCI', ev, 'stem sama kunci berbeda', 'seluruh bank final 9.000 soal', 'tinggi', 'perbandingan stem ternormalisasi', 'putuskan kunci yang benar', True)
        if n == 'C08_DUPLIKASI' and s == 'FAIL': add('DUPLIKAT_IDENTIK', ev, 'soal identik (stem+kunci)', 'seluruh bank final', 'tinggi', 'kesamaan teks persis', 'pertahankan satu atau bedakan', True)
        if n == 'C08_DUPLIKASI' and s == 'WARN': add('DUPLIKAT_SUBSTANTIF', ev, 'kemiripan token >= 0,8 dan kunci sama', 'seluruh bank final', 'sedang', 'ukuran Jaccard; fungsi pedagogis belum dinilai', 'tinjau; pertahankan bila fungsinya berbeda', True)
        if n == 'C09_BEBAN_BACA' and s == 'WARN': add('BEBAN_BACA', ev, 'melampaui ambang panjang/kata untuk kelas 1', 'ambang heuristik internal', 'sedang', 'ambang kasar, bukan baku', 'sederhanakan redaksi atau biarkan bila perlu bagi TP', False)
        if n == 'C06_JAWABAN_GANDA_HEURISTIK' and s == 'WARN': add('INDIKASI_JAWABAN_GANDA', ev, 'dua opsi saling mengandung', 'teks opsi', 'rendah', 'heuristik tekstual', 'cek apakah kedua opsi benar', True)
        if n == 'C05_KUNCI_VS_PENJELASAN' and s == 'WARN' and r['question_type'] in ('fill_in_short', 'completion'): pass
    # --- buta
    cmp_, det = ('NA', 'agen tidak memeriksa')
    if b:
        cmp_, det = compare(r, b)
        if cmp_ == 'BEDA':
            add('JAWABAN_BUTA_BEDA', f'soal: {r["question"][:140]}', det, 'penyelesaian buta oleh agen AI (tanpa kunci)', b.get('keyakinan', ''), b.get('alasan_keyakinan', '')[:200], 'selesaikan perbedaan; kunci belum boleh diubah tanpa keputusan', True)
        for m in b.get('masalah') or []:
            if m in HARD | SOFT:
                add('AGEN_' + m, (b.get('bukti_masalah') or '')[:250], (b.get('alasan_keyakinan') or '')[:200], 'penilaian agen AI', b.get('keyakinan', ''), 'penilaian model, belum diverifikasi manusia', 'tinjau', m in HARD)
        if b.get('kesesuaian_tp') in ('tidak', 'sebagian', 'ragu'):
            add('TP_' + b['kesesuaian_tp'].upper(), (b.get('alasan_tp') or '')[:250], f'baca TP: "{r["tp"][:100]}" vs soal', f'teks ATP audit/atp_text; TP {r["tp_id"]}', 'sedang', 'penilaian model atas teks ATP lengkap', 'putuskan kesesuaian TP atau pindah TP (hanya setelah keputusan kurikulum)', True)
    kinds = {x[0] for x in issues}
    # --- keputusan status (urutan prioritas)
    src = b.get('perlu_sumber') if b else None
    ahli = bool(b and b.get('perlu_ahli'))
    konfirm = 'KONFIRMASI_PASCA_REVISI' in kodes
    hard = kinds & {'HITUNG_TIDAK_COCOK', 'STRUKTUR', 'KUNCI_VS_PENJELASAN', 'KONFLIK_KUNCI', 'DUPLIKAT_IDENTIK', 'JAWABAN_BUTA_BEDA'} | {k for k in kinds if k.startswith('AGEN_') and k[5:] in HARD}
    if not b:
        st, why = 'UNRESOLVED', 'tidak ada hasil penyelesaian buta untuk ID ini'
    elif konfirm:
        st, why = 'EXPERT_REQUIRED', 'kunci diubah oleh revisi; konfirmasi manusia wajib'
    elif hard:
        st, why = 'AI_FLAGGED', 'ditemukan: ' + ', '.join(sorted(hard))
    elif src:
        st, why = 'SOURCE_REQUIRED', 'jawaban bergantung sumber: ' + str(src)[:150]
    elif ahli or (pre in AGAMA and ('AKURASI_AHLI' in kodes or 'ATP_INDIKASI_KUAT' in kodes)):
        st, why = 'EXPERT_REQUIRED', 'keputusan menuntut otoritas: ' + (b.get('alasan_ahli') or 'materi agama/bahasa/kurikulum')[:150]
    elif kinds & {'TP_TIDAK', 'TP_SEBAGIAN', 'TP_RAGU'} or 'ATP_INDIKASI_KUAT' in kodes:
        st, why = 'EXPERT_REQUIRED', 'kesesuaian TP perlu keputusan kurikulum'
    elif kinds & {'DUPLIKAT_SUBSTANTIF', 'INDIKASI_JAWABAN_GANDA'} or {k for k in kinds if k.startswith('AGEN_')}:
        st, why = 'AI_FLAGGED', 'ditemukan: ' + ', '.join(sorted(kinds))
    elif b.get('keyakinan') == 'rendah' or cmp_ == 'NA' and r['question_type'] != 'performance_task':
        st, why = 'UNRESOLVED', 'keyakinan penyelesaian buta rendah atau perbandingan tidak dapat dilakukan'
    elif kinds:
        st, why = 'AI_FLAGGED', 'ditemukan: ' + ', '.join(sorted(kinds))
    else:
        st, why = 'AI_VERIFIED', 'semua pemeriksaan otomatis yang dapat diuji terpenuhi; bukan pengganti persetujuan ahli'
    return st, why, issues, cmp_, det, kodes, b

STATUSES = ['AI_VERIFIED', 'AI_FLAGGED', 'EXPERT_REQUIRED', 'SOURCE_REQUIRED', 'UNRESOLVED']

def main():
    out = os.path.join(HERE)
    rows, ev_rows, exp_rows, src_rows = [], [], [], []
    ids = sorted(hasil)
    for i in ids:
        st, why, issues, cmp_, det, kodes, b = decide(i)
        r = fin[i]; ck = hasil[i]['checks']
        row = {'question_id': i, 'mapel': hasil[i]['mapel'], 'tp_id': r['tp_id'], 'tipe': r['question_type'], 'sumber_daftar': 'ANTREAN_VERIFIKASI' if i in queue else 'NEEDS_REVIEW_DI_LUAR_ANTREAN',
               'kode_antrean_audit_sebelumnya': ';'.join(sorted(kodes)) if kodes else 'DI_LUAR_ANTREAN', 'status_audit_sebelumnya': detail[i]['quality_status_akhir'], 'status_ai': st, 'alasan_status': why}
        for n in ck: row[n] = ck[n][0]
        row['C12_JAWABAN_BUTA_VS_KUNCI'] = cmp_
        row['keyakinan_penyelesaian_buta'] = (b or {}).get('keyakinan', '')
        row['jumlah_masalah'] = len(issues)
        row['persetujuan_manusia_wajib'] = 'YA' if (st in ('EXPERT_REQUIRED', 'SOURCE_REQUIRED') or any(x[7] for x in issues)) else ('TIDAK' if st == 'AI_VERIFIED' and False else 'DISARANKAN' if st == 'AI_VERIFIED' and r['id'].split('-')[0] in AGAMA else 'TIDAK')
        rows.append(row)
        for (kode, bukti, indep, sumber, yakin, alasan, rek, wajib) in issues:
            ev_rows.append({'question_id': i, 'masalah': kode, 'bukti_soal_atau_dokumen': bukti, 'hasil_pemeriksaan_independen': indep, 'sumber_rujukan': sumber, 'tingkat_keyakinan': yakin, 'alasan_keyakinan': alasan, 'rekomendasi_koreksi': rek, 'persetujuan_manusia_wajib': 'YA' if wajib else 'TIDAK', 'status_ai': st})
        if cmp_ == 'COCOK' and not issues:
            ev_rows.append({'question_id': i, 'masalah': '(tidak ada)', 'bukti_soal_atau_dokumen': r['question'][:140], 'hasil_pemeriksaan_independen': det, 'sumber_rujukan': 'penyelesaian buta oleh agen AI; cek deterministik C01-C11', 'tingkat_keyakinan': (b or {}).get('keyakinan', ''), 'alasan_keyakinan': ((b or {}).get('alasan_keyakinan') or '')[:200], 'rekomendasi_koreksi': '-', 'persetujuan_manusia_wajib': 'TIDAK' if r['id'].split('-')[0] not in AGAMA else 'DISARANKAN', 'status_ai': st})
        if st == 'EXPERT_REQUIRED':
            exp_rows.append({'question_id': i, 'mapel': row['mapel'], 'tp_id': r['tp_id'], 'peninjau': 'Ahli materi/kurikulum', 'alasan': why, 'kode_antrean': row['kode_antrean_audit_sebelumnya'], 'jawaban_ai_buta': (b or {}).get('jawaban_saya', ''), 'kunci_bank': r['answer'] if not isinstance(r['answer'], (dict, list)) else json.dumps(r['answer'], ensure_ascii=False), 'pertanyaan_ke_ahli': (b or {}).get('alasan_ahli') or 'Setujui kunci/TP atau beri koreksi'})
        if st == 'SOURCE_REQUIRED':
            src_rows.append({'question_id': i, 'mapel': row['mapel'], 'tp_id': r['tp_id'], 'sumber_dibutuhkan': (b or {}).get('perlu_sumber'), 'alasan': why, 'jawaban_ai_buta': (b or {}).get('jawaban_saya', ''), 'kunci_bank': r['answer'] if not isinstance(r['answer'], (dict, list)) else json.dumps(r['answer'], ensure_ascii=False)})
    def w(fn, rs):
        with open(os.path.join(out, fn), 'w', encoding='utf-8', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=list(rs[0].keys()) if rs else ['kosong']); wr.writeheader(); wr.writerows(rs)
    w('AI_VERIFICATION_RESULTS.csv', rows); w('AI_VERIFICATION_EVIDENCE.csv', ev_rows)
    w('EXPERT_REQUIRED_QUEUE.csv', exp_rows); w('SOURCE_REQUIRED_QUEUE.csv', src_rows)
    stats = {'total_id': len(rows), 'status': dict(collections.Counter(r['status_ai'] for r in rows)), 'dengan_hasil_buta': sum(1 for i in ids if i in blind),
             'ada_masalah_unik_id': sum(1 for r in rows if r['jumlah_masalah']),
             'cek_lolos': {n: dict(collections.Counter(r[n] for r in rows)) for n in rows[0] if n.startswith('C')}}
    json.dump(stats, open(os.path.join(out, 'stats.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
