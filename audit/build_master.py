# -*- coding: utf-8 -*-
"""Rakit berkas induk: FINAL bank, QUESTION_REVISIONS, QUESTION_AUDIT_DETAIL (9 mapel), ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, antrean ahli. Bank asli tidak diubah."""
import sys, os, json, csv, copy, collections, hashlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F, apply_revisions as AR

OUT = os.path.join(F.HERE, 'FINAL'); os.makedirs(OUT, exist_ok=True)
subjects = list(E.BANKS)
tot = collections.Counter(); per = {}
rev_rows = []; detail_rows = []; all_cov = []; all_dups = []; all_queue = []
profile = {}
integrity = {}
for subj in subjects:
    slug = F.SLUG[subj]; d = os.path.join(F.HERE, slug)
    src = os.path.join(E.ROOT, E.BANKS[subj])
    h0 = hashlib.sha256(open(src, 'rb').read()).hexdigest()
    bank = json.load(open(src, encoding='utf-8'))
    rows = {r['question_id']: r for r in json.load(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), encoding='utf-8'))}
    val = AR.main(subj)                       # menulis REVISIONS_VALIDATED.json
    ok, skip, bad = val['diterima'], val['tidak_direvisi'], val['ditolak_validasi']
    final = []
    st = collections.Counter(); resid = collections.Counter()
    for x in bank:
        i = x['id']; r = rows[i]
        y = copy.deepcopy(x); hist = []
        if i in ok:
            before = {k: x.get(k) for k in ok[i]['perubahan']}
            y.update(ok[i]['perubahan'])
            hist.append({'tanggal': '2026-10-12', 'jenis': ok[i]['jenis'], 'alasan': ok[i]['alasan'], 'verifikasi': ok[i]['verifikasi'], 'sebelum': before, 'berkas_usulan': ok[i]['berkas']})
            rev_rows.append([i, subj, x['tp_id'], ';'.join(ok[i]['jenis']), ';'.join(sorted(r['alasan_status'])), json.dumps({k: x.get(k) for k in ok[i]['perubahan']}, ensure_ascii=False), json.dumps(ok[i]['perubahan'], ensure_ascii=False), ok[i]['verifikasi'], ok[i]['alasan'], ok[i]['berkas']])
        yy = dict(y); yy['_subj'] = subj
        iss_struct = [a for a, _ in E.structure(yy)]
        # status final
        status0 = r['quality_status']
        if status0 == 'PASS': status = 'PASS'; action = 'tidak ada tindakan'
        elif status0 == 'NEEDS_REVIEW': status = 'NEEDS_REVIEW'; action = r['recommended_action']
        elif i in ok:
            status = 'PASS' if not iss_struct else 'REVISE'
            action = 'sudah direvisi; tinjau ulang oleh guru bila diinginkan' if status == 'PASS' else 'revisi belum menghapus semua isu: ' + ','.join(iss_struct)
        elif i in skip: status = 'NEEDS_REVIEW'; action = 'TAHAN: revisi ditunda karena butuh keputusan guru/ahli (' + str(skip[i])[:200] + ')'
        else: status = 'REVISE'; action = 'revisi belum dikerjakan' + (' (usulan ditolak validasi: ' + '; '.join(bad[i]) + ')' if i in bad else '')
        st[status] += 1
        for a in iss_struct: resid[a] += 1
        y['audit'] = {
            'question_id': i, 'tp_text': x['tp'], 'quality_status': status, 'quality_status_awal': status0,
            'atp_keselarasan': r['atp_final'], 'issues': r['issues'] if status0 != 'PASS' else [], 'isu_struktur_tersisa': iss_struct,
            'recommended_action': action, 'revision_notes': (hist[0]['alasan'] if hist else ''),
            'kbc_mapping': E.kbc(yy), 'deep_learning_mapping': E.pm(yy), 'graduate_profile_mapping': E.pl(yy),
            'catatan_pemetaan': 'USULAN berbukti; belum ditetapkan guru/ahli',
            'tinjau_baca': r['tinjau_baca'], 'source_ref': {'berkas_bank_asli': E.BANKS[subj], 'id_asli': i}}
        y['revision_history'] = hist
        final.append(y)
        detail_rows.append([i, subj, x['tp_id'], x['tp'], x['material'], x['question_type'], x['difficulty'], x['cognitive_level']] + [r['skor'][a] for a in ('atp', 'akurasi', 'usia_bahasa', 'konstruksi', 'keunikan')] +
                           [r['atp_final'], status0, status, ';'.join(r['alasan_status']), ';'.join(r['issues']), action, ' || '.join(f"{t['kode']}: {t['catatan']}" for t in r['tinjau_baca']),
                            ';'.join(f"{m['nilai']}[{','.join(sum([v for v in m['bukti'].values()], []))}]" for m in y['audit']['kbc_mapping'] if m['relevansi'] == 'langsung'),
                            ';'.join(f"{m['dimensi']}/{m['subdimensi']}" for m in y['audit']['graduate_profile_mapping'] if m['relevansi'] == 'langsung'),
                            ';'.join(a['jenis'] for a in y['audit']['deep_learning_mapping']['pengalaman_belajar']), E.BANKS[subj]])
    # integritas
    assert len(final) == len(bank) and [z['id'] for z in final] == [z['id'] for z in bank]
    h1 = hashlib.sha256(open(src, 'rb').read()).hexdigest(); assert h0 == h1
    json.dump(final, open(os.path.join(OUT, f'{slug}_final.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    S = json.load(open(os.path.join(d, 'AUDIT_SUMMARY.json')))
    per[subj] = dict(awal=len(bank), status_awal=S['status'], status_akhir=dict(st), revisi_diterima=len(ok), revisi_ditolak_validasi=len(bad), tidak_direvisi=len(skip), belum_ditangani=len(val['belum_ditangani']),
                     isu_struktur_tersisa=dict(resid), atp_final=S['atp_final'], tinjau_baca_kode=S['tinjau_baca_kode'], kesulitan=S['kesulitan'], tipe=S['tipe'], kunci_terpanjang=S['kunci_opsi_terpanjang'], tf=S['tf_jawaban'],
                     hash_bank_asli=h0)
    tot.update(st)
    for c in json.load(open(os.path.join(d, 'ATP_COVERAGE_MATRIX.json'))): c['mapel'] = subj; all_cov.append(c)
    for rr in csv.DictReader(open(os.path.join(d, 'DUPLICATION_REPORT.csv'), encoding='utf-8')): rr['mapel'] = subj; all_dups.append(rr)
    for rr in csv.reader(open(os.path.join(d, 'ANTRIAN_VERIFIKASI_AHLI.csv'), encoding='utf-8')):
        if rr[0] != 'question_id': all_queue.append([subj] + rr)
    profile[subj] = json.load(open(os.path.join(d, 'KBC_DEEP_LEARNING_PROFILE_MATRIX.json')))
    integrity[subj] = json.load(open(os.path.join(d, 'CONSISTENCY_CHECK.json')))
R = F.HERE
hdr = ['question_id', 'subject', 'tp_id', 'tp_text', 'material', 'question_type', 'difficulty', 'cognitive_level', 'skor_atp', 'skor_akurasi', 'skor_usia_bahasa', 'skor_konstruksi', 'skor_keunikan', 'atp_keselarasan', 'quality_status_awal', 'quality_status_akhir', 'alasan_status', 'issues', 'recommended_action', 'tinjau_baca', 'kbc_langsung_dengan_bukti', 'profil_lulusan_langsung', 'dl_pengalaman', 'berkas_sumber']
with open(os.path.join(R, 'QUESTION_AUDIT_DETAIL.csv'), 'w', encoding='utf-8', newline='') as f: w = csv.writer(f); w.writerow(hdr); w.writerows(detail_rows)
with open(os.path.join(R, 'QUESTION_REVISIONS.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['question_id', 'subject', 'tp_id', 'jenis_revisi', 'masalah_ditemukan', 'versi_asli', 'versi_revisi', 'kunci_hasil_verifikasi', 'alasan_lebih_sesuai', 'berkas_usulan']); w.writerows(rev_rows)
with open(os.path.join(R, 'ATP_COVERAGE_MATRIX.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['mapel', 'tp_id', 'material', 'tp_text', 'kemiripan_TP_ke_ATP', 'jumlah_soal', 'PASS_awal', 'REVISE_awal', 'NEEDS_REVIEW_awal', 'tipe', 'kesulitan', 'level_kognitif', 'kualitas_cakupan', 'kekurangan_dan_rekomendasi'])
    for c in all_cov: w.writerow([c['mapel'], c['tp_id'], c['material'], c['tp_text'], c['atp_trace'], c['jumlah_soal'], c['PASS'], c['REVISE'], c['NEEDS_REVIEW'], json.dumps(c['tipe'], ensure_ascii=False), json.dumps(c['kesulitan']), json.dumps(c['level_kognitif'], ensure_ascii=False), c['kualitas_cakupan'], ' | '.join(c['kekurangan'])])
with open(os.path.join(R, 'DUPLICATION_REPORT.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['mapel', 'jenis', 'id_1', 'id_2', 'kemiripan', 'tindakan_disarankan']); [w.writerow([r['mapel'], r['jenis'], r['id_1'], r['id_2'], r['kemiripan'], r['tindakan_disarankan']]) for r in all_dups]
with open(os.path.join(R, 'ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['mapel', 'question_id', 'tp_id', 'tipe', 'cuplikan_soal', 'kode_temuan', 'peninjau_yang_disarankan', 'alasan_dan_bukti', 'pertanyaan_untuk_peninjau', 'keselarasan_ATP']); w.writerows(all_queue)
json.dump({'catatan': 'Jumlah label bukan bukti keberhasilan kurikulum. Semua label adalah USULAN berbukti yang perlu diverifikasi guru/ahli.', 'per_mapel': profile}, open(os.path.join(R, 'KBC_DEEP_LEARNING_PROFILE_MATRIX.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'tanggal': '2026-10-12', 'total': dict(tot), 'jumlah_soal': sum(tot.values()), 'per_mapel': per}, open(os.path.join(R, 'MASTER_STATS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(dict(tot), sum(tot.values()))
for s, p in per.items(): print(s, p['status_awal'], '->', p['status_akhir'], 'rev', p['revisi_diterima'], 'ditolak', p['revisi_ditolak_validasi'], 'tunda', p['tidak_direvisi'], 'belum', p['belum_ditangani'])
