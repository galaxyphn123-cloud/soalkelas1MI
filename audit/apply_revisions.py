# -*- coding: utf-8 -*-
"""Validasi usulan revisi (audit/<slug>/revisions_*.json) terhadap bank asli dan aturan keras. Tidak menulis ke bank asli.
Pemakaian: python3 apply_revisions.py "<Mapel>"   -> menulis audit/<slug>/REVISIONS_VALIDATED.json (diterima/ditolak + alasan)"""
import sys, os, json, glob, re, copy, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
ALLOWED = {'question', 'options', 'explanation', 'visual_prompt', 'question_type', 'answer', 'difficulty'}

def keytxt(x):
    return x['options']['ABCD'.index(x['answer'])][3:].strip() if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') else None

def validate(orig, ch, flags):
    errs = []
    new = copy.deepcopy(orig)
    for k, v in ch.items():
        if k not in ALLOWED: errs.append(f'field tidak diizinkan: {k}')
        else: new[k] = v
    if errs: return None, errs
    t = orig['question_type']
    if not str(new['question']).strip(): errs.append('soal kosong')
    if len(new['explanation'].strip()) == 0: errs.append('penjelasan kosong')
    mc = t in ('multiple_choice', 'multiple_choice_visual', 'contextual')
    if mc:
        o = new['options']
        if not (isinstance(o, list) and len(o) == 4 and all(re.match(r'^[A-D]\. \S', s) for s in o) and [s[0] for s in o] == list('ABCD')): errs.append('format opsi A-D rusak')
        else:
            if len({s[3:].strip().lower() for s in o}) < 4: errs.append('opsi kembar')
            if 'AKURASI_SALAH_TEGAS' not in flags:
                if new['answer'] != orig['answer']: errs.append('huruf kunci berubah tanpa temuan AKURASI_SALAH_TEGAS')
                if keytxt(new) != keytxt(orig): errs.append('teks kunci berubah tanpa temuan AKURASI_SALAH_TEGAS')
    else:
        if 'AKURASI_SALAH_TEGAS' not in flags and 'answer' in ch and orig['question_type'] in ('true_false', 'matching', 'ordering', 'fill_in_short', 'completion') :
            errs.append('kunci berubah tanpa temuan AKURASI_SALAH_TEGAS')
    if 'question_type' in ch and ch['question_type'] != t:
        if not (t in ('fill_in_short', 'completion') and ch['question_type'] == 'short_answer' and 'isian_jawaban_terbuka' in flags): errs.append('perubahan tipe hanya untuk isian_jawaban_terbuka -> short_answer')
    if 'isian_jawaban_terbuka' in flags and t in ('fill_in_short', 'completion') and new['question_type'] != 'short_answer' and new['question'] == orig['question']: errs.append('isian terbuka belum ditangani')
    if t == 'true_false' and new['answer'] not in ('Benar', 'Salah'): errs.append('kunci TF tak valid')
    if re.search(r'\.\.\.\.', new['question']) and t == 'true_false': errs.append('benar/salah masih berisi titik-titik')
    if t == 'grouping' and (not isinstance(new['answer'], dict) or any(not isinstance(v, list) for v in new['answer'].values())): errs.append('kunci pengelompokan tak valid')
    if mc and not errs:
        txt = [s[3:].strip() for s in new['options']]; k = keytxt(new)
        L = sorted(len(s) for s in txt)
        if len(k) == L[-1] and len(k) >= 1.5 * L[-2] and len(k) > 12: errs.append('kunci masih opsi terpanjang menonjol')
    return new, errs

def main(subj, only=None):
    slug = F.SLUG[subj]; d = os.path.join(F.HERE, slug)
    bank = {x['id']: x for x in json.load(open(os.path.join(E.ROOT, E.BANKS[subj]), encoding='utf-8'))}
    rows = {r['question_id']: r for r in json.load(open(os.path.join(d, 'QUESTION_AUDIT_DETAIL.json'), encoding='utf-8'))}
    rev, skip = {}, {}
    for f in ([only] if only else sorted(glob.glob(os.path.join(d, 'revisions_*.json')))):
        part = json.load(open(f, encoding='utf-8'))
        for i, v in part.get('revisi', {}).items():
            if i in rev: rev[i]['_dobel'] = True
            rev[i] = dict(v, _berkas=os.path.basename(f))
        skip.update(part.get('tidak_direvisi', {}))
    ok, bad = {}, {}
    for i, v in rev.items():
        r = rows.get(i)
        if not r or r['quality_status'] != 'REVISE': bad[i] = ['bukan berstatus REVISE pada audit']; continue
        flags = set(r['alasan_status']) | {t['kode'] for t in r['tinjau_baca']}
        new, errs = validate(bank[i], v['perubahan'], flags)
        if v.get('_dobel'): errs = (errs or []) + ['ID direvisi lebih dari satu berkas']
        if errs: bad[i] = errs
        else: ok[i] = {'perubahan': v['perubahan'], 'jenis': v.get('jenis', []), 'alasan': v.get('alasan', ''), 'verifikasi': v.get('verifikasi', ''), 'berkas': v['_berkas']}
    belum = [i for i, r in rows.items() if r['quality_status'] == 'REVISE' and i not in ok and i not in skip]
    out = dict(mapel=subj, diterima=ok, ditolak_validasi=bad, tidak_direvisi=skip, belum_ditangani=belum)
    if not only: json.dump(out, open(os.path.join(d, 'REVISIONS_VALIDATED.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out

if __name__ == '__main__':
    o = main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(len(o['diterima']), 'diterima;', len(o['ditolak_validasi']), 'ditolak validasi;', len(o['tidak_direvisi']), 'tidak direvisi;', len(o['belum_ditangani']), 'belum ditangani' + (' (abaikan bila validasi satu berkas)' if len(sys.argv) > 2 else ''))
    for i, e in list(o['ditolak_validasi'].items())[:15]: print(' ', i, e)
