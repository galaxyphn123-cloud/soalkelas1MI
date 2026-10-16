# -*- coding: utf-8 -*-
"""Pindai urutan deret baku (rukun Islam, rukun iman, sila, waktu salat, hari, bulan, dst.) pada bank final.
Hanya segmen yang MENYATAKAN urutan yang dinilai: soal, penjelasan, kunci, opsi kunci, dan pernyataan benar-salah berkunci Benar.
Opsi pengecoh dan pernyataan berkunci Salah diabaikan (urutan salah di sana disengaja)."""
import json, re, csv, collections, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
bank = json.load(open(os.path.join(ROOT, 'final_bank/bank_final_lulus.json'), encoding='utf-8'))
SER = {
 'rukun_islam': dict(canon=['syahadat', 'salat', 'zakat', 'puasa', 'haji'], alt=[['syahadat', 'salat', 'puasa', 'zakat', 'haji']],
    pat={'syahadat': r'syahadat|syahadatain|dua kalimat', 'salat': r'\bsalat\b|\bshalat\b|\bsholat\b', 'zakat': r'\bzakat\b', 'puasa': r'\bpuasa\b|\bshaum\b', 'haji': r'\bhaji\b'}),
 'rukun_iman': dict(canon=['allah', 'malaikat', 'kitab', 'rasul', 'hari akhir', 'qada qadar'],
    pat={'allah': r'iman kepada allah|beriman kepada allah', 'malaikat': r'malaikat', 'kitab': r'kitab-kitab|kitab allah|kitab suci', 'rasul': r'\brasul\b|\bnabi\b', 'hari akhir': r'hari akhir|hari kiamat|\bkiamat\b', 'qada qadar': r'qada|qadar|takdir'}),
 'sila': dict(canon=['ketuhanan', 'kemanusiaan', 'persatuan', 'kerakyatan', 'keadilan'],
    pat={'ketuhanan': r'ketuhanan', 'kemanusiaan': r'kemanusiaan', 'persatuan': r'persatuan', 'kerakyatan': r'kerakyatan|musyawarah', 'keadilan': r'keadilan'}),
 'waktu_salat': dict(canon=['subuh', 'zuhur', 'asar', 'magrib', 'isya'],
    pat={'subuh': r'\bsubuh\b|\bsubuh\b', 'zuhur': r'\bzuhur\b|\bzhuhur\b|\bdzuhur\b', 'asar': r'\basar\b|\bashar\b', 'magrib': r'\bmagrib\b|\bmaghrib\b', 'isya': r"\bisya\b|\bisya'\b|\bisyak\b"}),
 'hari': dict(canon=['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'], alt=[['minggu', 'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']],
    pat={'senin': r'\bsenin\b', 'selasa': r'\bselasa\b', 'rabu': r'\brabu\b', 'kamis': r'\bkamis\b', 'jumat': r"\bjum'?at\b", 'sabtu': r'\bsabtu\b', 'minggu': r'\bminggu\b'}),
 'bulan_hijriah': dict(canon=['muharam', 'safar', 'rabiulawal', 'rabiulakhir', 'jumadilawal', 'jumadilakhir', 'rajab', 'syaban', 'ramadan', 'syawal', 'zulkaidah', 'zulhijah'],
    pat={'muharam': r'\bmuharram\b|\bmuharam\b', 'safar': r'\bsafar\b', 'rabiulawal': r"rabiul awal|rabi'ul awal", 'rabiulakhir': r'rabiul akhir', 'jumadilawal': r'jumadil awal', 'jumadilakhir': r'jumadil akhir', 'rajab': r'\brajab\b', 'syaban': r"\bsya'?ban\b", 'ramadan': r'\bramadan\b|\bramadhan\b', 'syawal': r'\bsyawal\b', 'zulkaidah': r'zulkaidah|dzulqa', 'zulhijah': r'zulhijah|dzulhijjah'}),
 'sifat_wajib': dict(canon=['wujud', 'qidam', 'baqa'],
    pat={'wujud': r'\bwujud\b', 'qidam': r'\bqidam\b', 'baqa': r"\bbaqa'?\b"}),
 'angka_kata': dict(canon=['satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh'],
    pat={k: r'\b%s\b' % k for k in ['satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh']}),
 'wudu_tayamum': dict(canon=['niat', 'wajah', 'tangan', 'kepala', 'kaki', 'tertib'],
    pat={'niat': r'\bniat\b', 'wajah': r'wajah|muka', 'tangan': r'\btangan\b', 'kepala': r'\bkepala\b', 'kaki': r'\bkaki\b', 'tertib': r'\btertib\b'}),
 'surah': dict(canon=['fatihah', 'ikhlas', 'falaq', 'nas'],
    pat={'fatihah': r'fatihah', 'ikhlas': r'ikhlas', 'falaq': r'falaq', 'nas': r'\ban-?nas\b|\bnas\b'}),
}
def segs(r):
    out = []
    t = r['question_type']; a = r['answer']
    q = re.sub(r'^benar atau salah:\s*', '', r['question'], flags=re.I)
    if t == 'true_false':
        if a == 'Benar': out.append(('soal(Benar)', q))
        return out + [('penjelasan', r.get('explanation') or '')] if a == 'Benar' else out
    out.append(('soal', q)); out.append(('penjelasan', r.get('explanation') or ''))
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual') and isinstance(r['options'], list):
        for o in r['options']:
            if o.startswith(a + '.'): out.append(('kunci', o[2:].strip()))
    elif t == 'ordering': out.append(('kunci_urutan', ', '.join(a)))
    elif t in ('fill_in_short', 'completion'): out.append(('kunci', str(a)))
    return out
def seq_of(text, ser):
    low = text.lower(); hits = []
    for name, pat in ser['pat'].items():
        for m in re.finditer(pat, low): hits.append((m.start(), name))
    hits.sort(); seq = []
    for _, n in hits:
        if not seq or seq[-1] != n: seq.append(n)
    return seq
def subseq_order(seq, canon):
    idx = [canon.index(x) for x in seq if x in canon]; return idx
rows = []; stat = collections.defaultdict(collections.Counter)
for r in bank:
    for sname, ser in SER.items():
        for field, text in segs(r):
            seq = seq_of(text, ser)
            # dedup keep first occurrence order
            seen = []; [seen.append(x) for x in seq if x not in seen]
            if len(seen) < (3 if sname in ('rukun_islam', 'rukun_iman', 'sila', 'waktu_salat', 'hari', 'bulan_hijriah', 'angka_kata', 'surah') else 3): continue
            canon = ser['canon']; idx = subseq_order(seen, canon)
            ok = idx == sorted(idx)
            alt = any(seen == a[:len(seen)] or [x for x in a if x in seen] == seen for a in ser.get('alt', []))
            if ok: stat[sname]['sesuai_urutan_baku'] += 1; continue
            if alt: stat[sname]['sesuai_varian_alternatif'] += 1; rows.append((r['id'], r['subject'], sname, 'VARIAN_ALTERNATIF', field, ' > '.join(seen), ' > '.join(canon), r['question_type'], text[:140])); continue
            stat[sname]['URUTAN_BERBEDA'] += 1
            rows.append((r['id'], r['subject'], sname, 'URUTAN_BERBEDA', field, ' > '.join(seen), ' > '.join(canon), r['question_type'], text[:140]))
with open('urutan_deret_kode.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['id', 'mapel', 'deret', 'status', 'bagian_soal', 'urutan_ditemukan', 'urutan_baku_dipakai_pemindai', 'tipe', 'cuplikan']); w.writerows(rows)
for s, c in stat.items(): print(s, dict(c))
print(len(rows), len({x[0] for x in rows}))
E=1
