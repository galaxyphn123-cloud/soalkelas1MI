# -*- coding: utf-8 -*-
import json, glob, csv, os, collections, shutil
SP = '/tmp/claude-0/-home-user-soalkelas1MI/df7a5113-ba96-58a1-b311-412b61c68bd2/scratchpad/urutan'
os.makedirs('raw', exist_ok=True)
rows, fakta, diper = [], [], {}
for f in sorted(glob.glob(SP + '/out_*.json')):
    shutil.copy(f, 'raw/' + os.path.basename(f))
    d = json.load(open(f, encoding='utf-8')); k = os.path.basename(f)[4:-5]
    diper[k] = d.get('diperiksa')
    for t in d.get('temuan', []):
        rows.append({'berkas_agen': k, 'topik': t['topik'], 'jenis': t['jenis'], 'varian': ' || '.join(f"{v['nilai']} [{', '.join(v['id'])}]" for v in t['varian']),
                     'id_terlibat': ' '.join(sorted({i for v in t['varian'] for i in v['id']})), 'yang_dinilai_baku': t.get('yang_dinilai_baku') or '', 'dasar': t.get('dasar', ''),
                     'keyakinan': t.get('keyakinan', ''), 'catatan': t.get('catatan', '')})
    for x in d.get('fakta_baku_dipakai', []):
        fakta.append({'berkas_agen': k, 'topik': x['topik'], 'urutan_atau_nilai': x.get('urutan_atau_nilai', ''), 'contoh_id': ' '.join(x.get('id', [])[:6])})
for fn, rs in (('TEMUAN_INKONSISTENSI.csv', rows), ('FAKTA_BAKU_DIPAKAI.csv', fakta)):
    with open(fn, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rs[0].keys())); w.writeheader(); w.writerows(rs)
print('diperiksa per berkas:', diper, 'total', sum(v or 0 for v in diper.values()))
print('temuan', len(rows), collections.Counter(r['jenis'] for r in rows), collections.Counter(r['keyakinan'] for r in rows), 'ID unik', len({i for r in rows for i in r['id_terlibat'].split()}))
