# -*- coding: utf-8 -*-
import sys, os, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_full as F
subj = sys.argv[1]; d = os.path.join(F.HERE, F.SLUG[subj])
rows = json.load(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), encoding='utf-8'))
import audit_engine as E
bank = {x['id']: x for x in json.load(open(os.path.join(E.ROOT, E.BANKS[subj]), encoding='utf-8'))}
KIND = {'ATP_INDIKASI_KUAT': 'Kurikulum (ATP/TP)', 'ATP_INDIKASI': 'Kurikulum (ATP/TP)', 'AKURASI_AHLI': 'Ahli materi', 'AKURASI_KONFLIK_INTERNAL': 'Ahli materi', 'AMBIGU': 'Ahli materi/penyusun soal',
        'DISTRAKTOR_AMBIGU': 'Ahli materi/penyusun soal', 'USIA_ISI': 'Guru kelas 1'}
Q = {'ATP_INDIKASI_KUAT': 'Apakah topik ini boleh tetap berada pada TP ini, dipindah ke TP lain, atau dikeluarkan dari bank?', 'ATP_INDIKASI': 'Apakah topik turunan ini masuk cakupan TP (atau CP) sehingga layak dipertahankan di TP ini?',
     'AKURASI_AHLI': 'Apakah kunci/pernyataan benar menurut mazhab/rujukan yang dipakai madrasah?', 'AKURASI_KONFLIK_INTERNAL': 'Tentukan mana kunci yang benar; butir lain yang bertentangan harus disesuaikan.',
     'AMBIGU': 'Apakah ada lebih dari satu jawaban yang dapat dibenarkan? Bagaimana redaksi yang tepat?', 'DISTRAKTOR_AMBIGU': 'Apakah pengecoh ini dapat dibenarkan? Jika ya, ganti pengecoh.', 'USIA_ISI': 'Apakah materi/istilah ini sesuai untuk murid kelas 1 MI?'}
out = []
for r in rows:
    if r['quality_status'] != 'NEEDS_REVIEW': continue
    q = bank[r['question_id']]
    for t in r['tinjau_baca']:
        if t['kode'] in KIND:
            out.append([r['question_id'], r['tp_id'], r['question_type'], q['question'][:140], t['kode'], KIND[t['kode']], t['catatan'], Q[t['kode']], 'mesin: ' + r['atp_tier'] + ' / final: ' + r['atp_final']])
    if not any(t['kode'] in KIND for t in r['tinjau_baca']):
        out.append([r['question_id'], r['tp_id'], r['question_type'], q['question'][:140], ';'.join(r['alasan_status']), 'Guru/ahli', '', 'Tinjau', ''])
out.sort(key=lambda z: (z[5], z[4], z[0]))
with open(os.path.join(d, 'ANTRIAN_VERIFIKASI_AHLI.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['question_id', 'tp_id', 'tipe', 'cuplikan_soal', 'kode_temuan', 'peninjau_yang_disarankan', 'alasan_dan_bukti', 'pertanyaan_untuk_peninjau', 'keselarasan_ATP']); w.writerows(out)
print(len(out), 'baris;', collections.Counter(z[5] for z in out))
