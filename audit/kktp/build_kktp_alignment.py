# -*- coding: utf-8 -*-
"""Keselarasan bank soal dengan KKTP (Fikih, Akidah Akhlak, Al-Qur'an Hadis, Bahasa Arab).
KKTP dipakai sebagai acuan cakupan bab. Hasil = INDIKASI berbasis kata kunci/pemetaan materi, bukan penetapan final.
Tidak ada soal yang diubah, dipindah, atau dihapus."""
import json, re, csv, os, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FINAL = os.path.join(ROOT, 'audit', 'FINAL')
OUT = os.path.dirname(os.path.abspath(__file__))

def parse_md(path, mapel):
    bab, out = None, []
    for ln in open(os.path.join(ROOT, path), encoding='utf-8'):
        c = [x.strip() for x in ln.strip().strip('|').split('|')]
        if len(c) < 2: continue
        m = re.match(r'\*\*(?:BAB|Bab)\s*(\d+)\s*[:.]?\s*(.+?)\*\*$', c[0])
        if m:
            bab = {'bab': int(m.group(1)), 'judul': m.group(2).strip(' :'), 'tp': []}; out.append(bab); continue
        m = re.match(r'(\d+)\.(\d+)\.?\s+(.*)', c[0])
        if m and bab:
            bab['tp'].append({'kode': f'{m.group(1)}.{m.group(2)}', 'tp': m.group(3).strip(), 'indikator': re.sub(r'\*\*', '', c[1])})
    return out

ARAB = [  # dari berkas KKTP Bahasa Arab K-I (Deep Learning); kolom 'Alur Tujuan Pembelajaran'
 {'bab': 1, 'judul': 'التعارف (Perkenalan)', 'tp': 3}, {'bab': 2, 'judul': 'أسرتي (Keluargaku)', 'tp': 3},
 {'bab': 3, 'judul': 'هوايتي (Hobiku)', 'tp': 4}, {'bab': 4, 'judul': 'بيتي (Rumahku)', 'tp': 3},
 {'bab': 5, 'judul': 'أسماء الفواكه (Nama-nama Buah)', 'tp': 3}, {'bab': 6, 'judul': 'الألوان (Warna-warna)', 'tp': 3}]

REF = {
 'Fikih': {'berkas': 'Kriteria Ketercapaian Tujuan Pembelajaran (KKTP) Fikih MI Kelas 1.docx.md', 'bab': parse_md('Kriteria Ketercapaian Tujuan Pembelajaran (KKTP) Fikih MI Kelas 1.docx.md', 'Fikih')},
 'Akidah Akhlak': {'berkas': 'KKTP Akidah 1.docx.md', 'bab': parse_md('KKTP Akidah 1.docx.md', 'Akidah')},
 "Al-Qur'an Hadis": {'berkas': 'KKTP Al-Qur_an Hadis MI Kelas 1.docx.md', 'bab': parse_md('KKTP Al-Qur_an Hadis MI Kelas 1.docx.md', 'AQH')},
 'Bahasa Arab': {'berkas': 'KKTP Bahasa Arab K-I (Deep Learning).docx', 'bab': [{'bab': b['bab'], 'judul': b['judul'], 'jumlah_alur_tp': b['tp']} for b in ARAB]},
}

# kode materi di ID bank -> nomor bab KKTP (None = tidak tercantum di KKTP)
MAP = {
 'FIK': {'RI': [1], 'KS': [2], 'TH': [3, 4], 'WT': [4, 5]},
 'AKA': {'SY': [1], 'TY': [2], 'SH': [3], 'AB': [4], 'KN': [5], 'RI': [6], 'SW': [7]},
 'AQH': {'HJ': [1, 7], 'FA': [2], 'NS': [3], 'FL': [4], 'IK': [5], 'HT': None, 'HK': [13]},
 'BAR': {'PK': [1], 'KL': [2], 'HB': [3], 'RM': [4], 'BH': [5], 'WR': [6], 'SK': None},
}
# topik yang TIDAK tercantum pada indikator KKTP -> (regex, label, kode materi yang diperiksa atau None=semua)
FLAGS = {
 'FIK': [(r'azan|adzan|iqamah|iqamat', 'azan/iqamah tidak ada di KKTP Fikih', None),
         (r'rakaat|rakat|takbiratul|sujud|rukuk|iktidal|tasyahud', 'tata cara/gerakan salat tidak ada di KKTP Fikih (Bab 1 hanya menyebut salat sebagai rukun Islam)', None),
         (r'mughallaz|najis berat|anjing|babi', 'najis berat tidak ada di KKTP (3.2 hanya najis ringan dan sedang)', None),
         (r'hari raya|idulfitri|iduladha|hijriah|tahun baru', 'hari raya/kalender Hijriah tidak ada di KKTP Fikih', None),
         (r'haid|junub|nifas|mandi besar', 'hadas besar tidak ada di KKTP Fikih', None),
         (r'kebersihan hati|hati yang bersih|hati bersih', 'kebersihan hati tidak ada di KKTP Fikih', None)],
 'AKA': [(r'siddiq|amanah|tablig|fathanah', 'empat sifat wajib rasul tidak ada di KKTP (5.2 hanya jujur atau kasih sayang)', None),
         (r'selawat|shalawat|salawat', 'selawat tidak ada di KKTP Akidah', None),
         (r'subhanallah|subhanalloh|tasbih', 'tasbih/Subhanallah tidak ada di KKTP Akidah', None),
         (r'tasyahud|tahiyat', 'tasyahud tidak ada di KKTP Akidah', None),
         (r'silsilah', 'silsilah keluarga Nabi tidak ada di KKTP (Bab 5)', None),
         (r'mukhalafah|qiyamuh|wahdaniyah|sama.|basar|kalam|hayat|qudrat|iradat', 'sifat wajib Allah selain Wujud, Qidam, Baqa\' tidak ada di KKTP (7.1)', ['SW'])],
 'AQH': [(r'al-?lahab|an-?nasr|an-?nashr|al-?kafirun|al-?kautsar|al-?kausar|quraisy|quraish|al-?ma.un', 'surah selain Al-Fatihah, An-Nas, Al-Falaq, Al-Ikhlas disebut di bank sebagai pengecoh/materi (surah itu ada di KKTP Bab 6, 8-12 tetapi belum punya soal pokok)', ['IK', 'NS', 'FL', 'FA'])],
 'BAR': [],
}
HURUF_AKHIR = r'\b(Dal|Dzal|Zai|Sin|Syin|Shad|Dhad|Tha|Zha|Ghain|Fa|Qaf|Kaf|Lam|Mim|Nun|Wawu|Ya)\b'

SLUG = {'FIK': 'fikih', 'AKA': 'akidah_akhlak', 'AQH': 'alquran_hadis', 'BAR': 'bahasa_arab'}
NAME = {'FIK': 'Fikih', 'AKA': 'Akidah Akhlak', 'AQH': "Al-Qur'an Hadis", 'BAR': 'Bahasa Arab'}

def text(r):
    return ' '.join(str(r.get(k) or '') for k in ('question', 'options', 'answer', 'explanation'))

def status_audit():
    st = {}
    for row in csv.DictReader(open(os.path.join(ROOT, 'audit', 'QUESTION_AUDIT_DETAIL.csv'), encoding='utf-8')):
        st[row['question_id']] = row['quality_status_akhir']
    return st

def main(arab_tambahan=None):
    st = status_audit()
    rows, cover = [], collections.defaultdict(lambda: collections.Counter())
    for pre in MAP:
        bank = json.load(open(os.path.join(FINAL, SLUG[pre] + '_final.json'), encoding='utf-8'))
        if pre == 'BAR' and arab_tambahan:
            bank = bank + [dict(x, _tambahan=True) for x in json.load(open(arab_tambahan, encoding='utf-8'))]
        for r in bank:
            kode = r['tp_id'].split('-')[2]
            babs = MAP[pre].get(kode, 'x')
            alasan, stat = [], 'SESUAI_BAB_KKTP'
            if babs is None:
                stat = 'BAB_TIDAK_TERCANTUM_DI_KKTP'; alasan.append('materi ini tidak ada pada KKTP %s' % NAME[pre])
            t = text(r)
            for rx, lab, only in FLAGS[pre]:
                if only and kode not in only: continue
                if re.search(rx, t, re.I): alasan.append(lab)
            if alasan and stat == 'SESUAI_BAB_KKTP': stat = 'INDIKASI_DI_LUAR_KKTP'
            if pre == 'FIK' and re.search(r'rukun tayamum', t, re.I) and re.search(r'empat|4\b|tertib', t, re.I):
                alasan.append('KKTP 5.2 menyebut niat, usap wajah, usap tangan; bank menyebut 4 rukun (+tertib). KKTP tidak menyatakan bahwa jumlahnya hanya tiga, jadi belum terbukti konflik'); stat = 'PERLU_TINJAU_AHLI_KKTP'
            if pre == 'AQH' and kode in ('HJ', 'HT') and re.search(HURUF_AKHIR, t):
                alasan.append('membahas huruf di luar rentang ا-خ pada KKTP Bab 1 (informasi; ATP bank dapat mencakup seluruh huruf)')
            for b in (babs if isinstance(babs, list) else []):
                cover[pre][b] += 1
            rows.append({'question_id': r['id'], 'subject': NAME[pre], 'tp_id': r['tp_id'], 'material': r['material'],
                         'status_audit_akhir': st.get(r['id'], 'TAMBAHAN_BARU' if r.get('_tambahan') else ''),
                         'kktp_bab': ','.join(map(str, babs)) if isinstance(babs, list) else '',
                         'kktp_status': stat, 'kktp_catatan': '; '.join(alasan)})
    with open(os.path.join(OUT, 'KKTP_ALIGNMENT_PER_SOAL.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # matriks bab KKTP
    mat = []
    for pre, nm in NAME.items():
        for b in REF[nm]['bab']:
            n = cover[pre].get(b['bab'], 0)
            mat.append({'subject': nm, 'kktp_bab': b['bab'], 'judul': b['judul'], 'jumlah_soal_dipetakan': n,
                        'status': 'ADA_SOAL' if n else 'BELUM_ADA_SOAL'})
    with open(os.path.join(OUT, 'KKTP_COVERAGE_MATRIX.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(mat[0].keys())); w.writeheader(); w.writerows(mat)
    json.dump(REF, open(os.path.join(OUT, 'KKTP_REFERENSI.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = collections.Counter((r['subject'], r['kktp_status']) for r in rows)
    summ = {'total_soal_dinilai': len(rows), 'per_mapel_status': {f'{k[0]}|{k[1]}': v for k, v in sorted(c.items())},
            'bab_belum_ada_soal': [f"{m['subject']} Bab {m['kktp_bab']} {m['judul']}" for m in mat if m['status'] == 'BELUM_ADA_SOAL']}
    json.dump(summ, open(os.path.join(OUT, 'KKTP_SUMMARY.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(summ, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
