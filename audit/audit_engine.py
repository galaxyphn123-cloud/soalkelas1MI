# -*- coding: utf-8 -*-
"""Mesin audit bank soal MI Darul Arifin Kelas 1 (aturan eksplisit; semua keluaran bersifat TEMUAN OTOMATIS).
Setiap label KBC / Pembelajaran Mendalam / Profil Lulusan disertai bukti (potongan teks atau field) dan tingkat relevansi.
Keputusan yang butuh ahli ditandai NEEDS_REVIEW; tidak ada soal yang dihapus atau diubah ID-nya."""
import json, re, os, collections, unicodedata, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANKS = collections.OrderedDict([
    ('Fikih', 'fikih/fikih_bank_1000_FIXED_gabungan.json'), ('Al-Quran Hadis', 'alquran_hadis/aqh_bank_1000.json'),
    ('Bahasa Arab', 'bahasa_arab/bar_bank_1000.json'), ('Akidah Akhlak', 'akidah_akhlak/aka_bank_1000.json'),
    ('Bahasa Indonesia', 'bahasa_indonesia/bin_bank_1000.json'), ('Matematika', 'matematika/mtk_bank_1000.json'),
    ('Pancasila', 'pancasila/ppn_bank_1000.json'), ('PJOK', 'pjok/pjk_bank_1000.json'), ('Bahasa Inggris', 'bahasa_inggris/eng_bank_1000.json')])
ATPFILE = {'Fikih': 'FIKIH_UNTUK_', 'Al-Quran Hadis': 'AL-QUR_AN_HA', 'Bahasa Arab': 'BAHASA_ARAB_', 'Akidah Akhlak': 'AKIDAH_AKHLA', 'Bahasa Indonesia': 'B._INDONESIA',
           'Matematika': 'MATEMATIKA_I', 'Pancasila': 'P_PANCASILA_', 'PJOK': 'PJOK', 'Bahasa Inggris': 'ENG'}
STOP = set('murid mampu peserta didik dapat dengan yang dan di dalam untuk secara benar tepat dari ke pada sebagai atau serta adalah ini itu apa mana berikut'.split())


def norm(s):
    t = ''.join(c if (c.isalnum() or unicodedata.category(c).startswith('M')) else ' ' for c in str(s).lower())
    return re.sub(r'\s+', ' ', t).strip()

def stem(w):
    for p in ('meng', 'meny', 'mem', 'men', 'ber', 'per', 'pen', 'peng', 'ter'):
        if w.startswith(p) and len(w) - len(p) >= 4: w = w[len(p):]; break
    else:
        if w.startswith('di') and len(w) >= 8: w = w[2:]
    for q in ('kan', 'nya', 'lah'):
        if w.endswith(q) and len(w) - len(q) >= 4: w = w[:-len(q)]; break
    return w

def toks(s):
    return [stem(w) for w in re.findall(r'\w+', str(s).lower()) if w not in STOP and len(w) > 2]

def load():
    out = []
    for subj, f in BANKS.items():
        for x in json.load(open(os.path.join(ROOT, f), encoding='utf-8')):
            x = dict(x); x['_subj'] = subj; x['_src'] = f
            out.append(x)
    return out

# ----------------------------------------------------------------------------- leksikon bukti (dapat diperiksa & diubah ahli)
LEX = {
 'KBC_ALLAH': r'\b(allah|rasul|rasulullah|nabi|muhammad|syahadat|syahadatain|salat|shalat|doa|zikir|iman|ibadah|asmaul|rahmat|al-qur|alquran|quran|surah|hadis|bismillah|alhamdulillah|syukur|takbir|ikhlas)\b',
 'KBC_ILMU': r'\b(belajar|ilmu|guru|membaca|literasi|rajin|bertanya|buku|sekolah|tekun|pelajaran)\b',
 'KBC_DIRI_SESAMA': r'\b(sesama|orang lain|manusia|diri sendiri|teman|keluarga|ayah|ibu|orang tua|kakak|adik|tetangga|saling|menolong|membantu|sopan|jujur|sabar|menghormati|menyayangi|berbagi|maaf|tolong|terima kasih|bersih|kebersihan|sehat|kesehatan|akhlak|santun|toleran|menghargai)\b',
 'KBC_LINGKUNGAN': r'\b(lingkungan|sampah|pohon|tanaman|menyiram|merawat tanaman|alam|membuang sampah|taman|hemat|ciptaan|kebersihan lingkungan|lingkungan bersih)\b',
 'KBC_TANAH_AIR': r'\b(indonesia|tanah air|bangsa|negara|bendera|pancasila|garuda|merah putih|persatuan|keberagaman|suku|budaya|daerah|nusantara|bhinneka|gotong royong|lagu kebangsaan)\b',
 'PL_KEIMANAN': r'\b(allah|rasul|salat|shalat|doa|syahadat|iman|ibadah|wudu|tayamum|puasa|zakat|surah|ayat|hadis|akidah|akhlak|malaikat|kitab|berdoa|bismillah)\b',
 'PL_KEWARGAAN': r'\b(aturan|sila|pancasila|keberagaman|toleransi|tanah air|gotong royong|menaati|lingkungan|bendera|negara|suku|budaya|hak|kewajiban|tanggung jawab|musyawarah)\b',
 'PL_KOLABORASI': r'\b(kerja sama|bekerja sama|bersama|tim|kelompok|gotong royong|berbagi|giliran|estafet|saling|membantu|menolong|beregu)\b',
 'PL_KEMANDIRIAN': r'\b(mandiri|sendiri|tanggung jawab|merapikan|inisiatif|mencoba|berani|tanpa bantuan|menyelesaikan|mengurus|membereskan)\b',
 'PL_KESEHATAN': r'\b(sehat|kesehatan|penyakit|kuman|cuci tangan|mencuci tangan|sabun|sikat gigi|menggosok gigi|gosok gigi|mandi|kuku|olahraga|gizi|bergizi|istirahat|bugar|aktivitas fisik|keselamatan|bahaya|cedera|pemanasan)\b',
 'PL_KREATIVITAS': r'\b(menggambar|mewarnai|mengarang|menciptakan|membuat|merancang|menyusun gambar|bernyanyi|menari|berimajinasi|mengeksplorasi|bereksplorasi|variasi|cerita sendiri)\b',
 'PL_KOMUNIKASI': r'\b(ucapkan|ceritakan|sebutkan|tanyakan|menyapa|berkenalan|bercerita|dialog|percakapan|berbicara|menyampaikan|mengucapkan|melafalkan|menjawab|bertanya|menulis|menuliskan)\b',
}
LEXC = {k: re.compile(v) for k, v in LEX.items()}
def ev(key, text):
    return sorted(set(m.group(0) for m in LEXC[key].finditer(text.lower())))[:4]

def qtext(x):
    """Gabungan teks yang diperiksa: soal + opsi (bukan penjelasan) agar bukti berasal dari tuntutan soal."""
    o = x.get('options')
    if isinstance(o, list): o = ' '.join(map(str, o))
    elif isinstance(o, dict): o = ' '.join(' '.join(map(str, v)) for v in o.values())
    return f"{x['question']} {o or ''}"

def keytext(x):
    """Teks yang benar-benar dinilai: kunci (teks opsi benar / isian) + penjelasan. Dipakai sebagai syarat bukti 'langsung'."""
    a = x['answer']; o = x.get('options'); k = ''
    if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') and isinstance(o, list) and a in 'ABCD':
        k = o['ABCD'.index(a)][3:]
    elif isinstance(a, str) and x['question_type'] not in ('performance_task', 'true_false'):
        k = a
    return f"{k} {x['explanation']}"

# ----------------------------------------------------------------------------- pemeriksaan struktur (objektif)
def structure(x):
    iss = []
    t = x['question_type']; a = x['answer']; o = x.get('options')
    for f in ('id', 'subject', 'grade', 'phase', 'tp_id', 'tp', 'material', 'question_type', 'difficulty', 'cognitive_level', 'question', 'explanation'):
        if x.get(f) in (None, '', [], {}): iss.append(('metadata_kosong', f))
    if t in ('multiple_choice', 'multiple_choice_visual', 'contextual'):
        if not (isinstance(o, list) and len(o) == 4): iss.append(('mc_opsi_bukan_4', ''))
        elif a not in 'ABCD' or len(str(a)) != 1: iss.append(('mc_kunci_tak_valid', a))
        else:
            txt = [s[3:].strip().lower() for s in o]
            if len(set(txt)) < 4: iss.append(('opsi_kembar', ''))
            key = txt['ABCD'.index(a)]
            if sum(1 for s in txt if s == key) > 1: iss.append(('kunci_ganda', key))
            if re.search(r'semua (jawaban )?benar|semua di atas|tidak ada jawaban', ' '.join(txt)): iss.append(('opsi_semua_benar', ''))
            if max(txt, key=len) == key and len(key) >= 1.5 * sorted(map(len, txt))[-2] and len(key) > 12: iss.append(('petunjuk_kunci_terpanjang', ''))
    if t == 'true_false' and a not in ('Benar', 'Salah'): iss.append(('tf_kunci_tak_valid', a))
    if t in ('fill_in_short', 'completion') and not str(a).strip(): iss.append(('isian_tanpa_kunci', ''))
    if t == 'grouping':
        if not isinstance(a, dict) or any(not isinstance(v, list) for v in a.values()): iss.append(('grouping_kunci_tak_valid', 'nilai kelompok bukan daftar'))
    if t == 'matching' and not (isinstance(a, dict) and isinstance(o, dict) and set(a) == set(o.get('kolom_kiri', [])) and sorted(a.values()) == sorted(o.get('kolom_kanan', []))): iss.append(('matching_kunci_tak_valid', ''))
    if t == 'ordering' and not (isinstance(a, list) and isinstance(o, list) and sorted(a) == sorted(o)): iss.append(('ordering_kunci_tak_valid', ''))
    if t in ('fill_in_short', 'completion') and isinstance(a, str) and re.match(r'\s*contoh jawaban', a.lower()): iss.append(('isian_jawaban_terbuka', 'butuh rubrik/penilaian guru; bukan isian singkat berkunci tunggal'))
    if x['visual_required'] and not x['visual_prompt']: iss.append(('visual_tanpa_deskripsi', ''))
    if re.search(r'(perhatikan|lihat|pada)\s+gambar', x['question'].lower()) and not x['visual_required']: iss.append(('rujuk_gambar_tanpa_visual', ''))
    return iss

# ----------------------------------------------------------------------------- skor aspek (0-4)
def sc_atp(x, atp_ok):
    if not atp_ok: return 0, 'TP tidak ditemukan pada teks ATP'
    qs = set(toks(x['question'] + ' ' + str(x['answer'] if isinstance(x['answer'], str) else '') + ' ' + x['explanation']))
    ref = set(toks(x['tp'] + ' ' + x['material'] + ' ' + x['competency']))
    ov = qs & ref
    if len(ov) >= 2: return 4, 'TP tertelusur; kata kunci bersama: ' + ', '.join(sorted(ov)[:4])
    if len(ov) == 1: return 3, 'TP tertelusur; satu kata kunci bersama: ' + ', '.join(ov)
    return 2, 'TP tertelusur, tetapi tak ada kata kunci TP/materi/kompetensi pada soal (perlu tinjauan ahli)'

def sc_akurasi(x, iss):
    bad = [i for i, _ in iss if i in ('mc_kunci_tak_valid', 'kunci_ganda', 'tf_kunci_tak_valid', 'isian_tanpa_kunci', 'opsi_kembar')]
    if bad: return 0, 'cacat struktur kunci: ' + ','.join(bad)
    ans = x['answer']
    if x['_subj'] == 'Matematika' and x['question_type'] in ('multiple_choice', 'contextual', 'fill_in_short', 'completion') and re.search(r'\d', x['question']):
        return 3, 'kunci konsisten secara struktur; jawaban hitung diverifikasi program pada pembuatan (belum diverifikasi ulang audit)'
    if x['question_type'] == 'performance_task':
        return 3, 'tugas kinerja: kunci berupa rubrik guru; ketepatan isi menunggu tinjauan guru'
    expl_has = False
    if x['question_type'] in ('multiple_choice', 'multiple_choice_visual', 'contextual') and isinstance(x.get('options'), list):
        k = x['options']['ABCD'.index(ans)][3:].strip().lower()
        expl_has = k[:30] in x['explanation'].lower() or any(w in x['explanation'].lower() for w in toks(k)[:3])
    elif isinstance(ans, str):
        expl_has = norm(ans) in norm(x['explanation']) or any(w in x['explanation'].lower() for w in toks(ans)[:3])
    else:
        expl_has = True
    return (3, 'kunci valid secara struktur' + ('; penjelasan memuat kunci' if expl_has else '; catatan: penjelasan tidak memuat kata kunci jawaban') + '; kebenaran fakta menunggu tinjauan ahli/guru')

def sc_usia(x):
    n = len(re.findall(r'\w+', x['question']))
    if x['question_type'] in ('multiple_choice', 'contextual', 'multiple_choice_visual'): n += 0
    if n <= 18: return 4, f'{n} kata pada soal'
    if n <= 30: return 3, f'{n} kata pada soal'
    if n <= 45: return 2, f'{n} kata pada soal (cukup panjang untuk kelas 1)'
    return 1, f'{n} kata pada soal (beban baca tinggi untuk kelas 1)'

def sc_konstruksi(x, iss):
    names = [i for i, _ in iss]
    if any(n in names for n in ('opsi_kembar', 'kunci_ganda', 'mc_opsi_bukan_4', 'visual_tanpa_deskripsi')): return 0, ','.join(names)
    pen = [n for n in names if n in ('petunjuk_kunci_terpanjang', 'opsi_semua_benar', 'rujuk_gambar_tanpa_visual')]
    if pen: return 2, 'catatan: ' + ','.join(pen)
    return 3, 'konstruksi sesuai tipe soal'

# ----------------------------------------------------------------------------- pemetaan KBC / PM / PL (dengan bukti)
TP_NILAI = [(r'cinta\s+allah|cinta\s+kepada\s+allah', 'Cinta Allah dan Rasul-Nya'), (r'cinta\s+ilmu', 'Cinta Ilmu'), (r'cinta\s+diri|sesama\s+manusia|cinta\s+sesama', 'Cinta Diri dan Sesama'),
             (r'cinta\s+lingkungan', 'Cinta Lingkungan'), (r'cinta\s+tanah\s+air', 'Cinta Tanah Air')]

def tp_nilai(tp):
    t = tp.lower()
    return [n for rx, n in TP_NILAI if re.search(rx, t)]

def kbc(x):
    qonly = qtext(x); kt = keytext(x)
    out = []
    for key, name in (('KBC_ALLAH', 'Cinta Allah dan Rasul-Nya'), ('KBC_ILMU', 'Cinta Ilmu'), ('KBC_DIRI_SESAMA', 'Cinta Diri dan Sesama'), ('KBC_LINGKUNGAN', 'Cinta Lingkungan'), ('KBC_TANAH_AIR', 'Cinta Tanah Air')):
        e_k = ev(key, kt); e_q = ev(key, qonly); e_tp = ev(key, x['tp'] + ' ' + x['material'])
        if name in tp_nilai(x['tp']): e_tp = e_tp + ['(TP menyebut: ' + name + ')']
        if e_k and e_tp: out.append({'nilai': name, 'relevansi': 'langsung', 'bukti': {'dalam_kunci_atau_penjelasan': e_k, 'dalam_TP_materi': e_tp}})
        elif e_tp and (e_q or e_k): out.append({'nilai': name, 'relevansi': 'konteks', 'bukti': {'dalam_soal': e_q, 'dalam_TP_materi': e_tp}, 'catatan': 'nilai muncul pada TP/latar soal, tetapi kunci tidak mengukurnya'})
        elif e_tp: out.append({'nilai': name, 'relevansi': 'melalui_TP', 'bukti': {'dalam_TP_materi': e_tp}, 'catatan': 'hanya terkait lewat teks TP/materi'})
        elif e_q: out.append({'nilai': name, 'relevansi': 'konteks', 'bukti': {'dalam_soal': e_q}, 'catatan': 'hanya latar cerita/kosakata; tidak dihitung sebagai bukti nilai'})
    if not out: return [{'nilai': None, 'relevansi': 'tidak_relevan', 'catatan': 'KBC tidak harus ada pada setiap soal; soal ini mengukur kompetensi akademik/teknis'}]
    return out

def pm(x):
    t = x['question_type']; qonly = qtext(x)
    exp, prin = [], []
    if t in ('multiple_choice', 'multiple_choice_visual', 'true_false', 'fill_in_short', 'matching', 'grouping', 'ordering'):
        exp.append(('Memahami', f'tipe {t} meminta mengenali/menjelaskan konsep'))
    if t in ('contextual', 'completion') or (t == 'performance_task'):
        exp.append(('Mengaplikasi', f'tipe {t} meminta penerapan pada situasi/praktik'))
    if re.search(r'\b(menurutmu|perasaanmu|apa yang kamu rasakan|bagaimana perasaan|refleksi|merefleksikan|menilai dirimu|nilai lemparanmu|hasilmu|ceritakan pengalamanmu|kebiasaan yang ingin kamu tingkatkan)\b', qonly.lower()):
        exp.append(('Merefleksi', 'soal meminta penilaian diri/perasaan'))
    if re.search(r'\b(nama|tokoh|teman|keluarga|rumah|sekolah|pasar|di rumah|di sekolah|taman)\b', qonly.lower()) and t in ('contextual', 'performance_task', 'multiple_choice_visual'):
        prin.append(('Bermakna', 'konteks kehidupan sehari-hari anak pada soal'))
    if re.search(r'\b(permainan|bermain|bernyanyi|tebak|lagu|menari|estafet|drama|simulasi|poster|gambarlah|menggambar|kartu|video|peragakan)\b', qonly.lower()):
        prin.append(('Menggembirakan', 'aktivitas bermain/praktik pada soal'))
    if 'Merefleksi' in [e for e, _ in exp]:
        prin.append(('Berkesadaran', 'soal mengajak menyadari proses/perasaan sendiri'))
    return {'pengalaman_belajar': [{'jenis': a, 'bukti': b} for a, b in exp], 'prinsip': [{'jenis': a, 'bukti': b} for a, b in prin],
            'catatan': 'Soal tertulis tidak membuktikan praktik pedagogis, kemitraan, lingkungan, atau pemanfaatan digital; itu dilengkapi aktivitas pendamping guru.'}

# Subdimensi & indikator tingkat "Berkembang" dikutip dari dokumen "Dimensi Kompetensi Profil Lulusan SD/MI" (audit/sumber/profil_lulusan_sd_indikator.txt).
# Penetapan level (Berkembang/Cakap/Mahir) untuk kelas 1 adalah keputusan guru; mesin hanya mengusulkan subdimensi.
PL_SUB = {
 'Keimanan dan Ketakwaan terhadap Tuhan YME': [
   ('Hubungan dengan Tuhan YME', r'\b(allah|rasul|salat|shalat|doa|berdoa|syahadat|syahadatain|ibadah|wudu|tayamum|puasa|zakat|haji|zikir|iman|surah|ayat|hadis|takbir|azan|ikamah)\b', 'Mengenai ajaran Tuhan Yang Maha Esa melalui cerita, doa, dan praktek ibadah sesuai agamanya serta mulai memahami nilai kebaikan dalam kehidupan nyata.'),
   ('Hubungan dengan sesama manusia', r'\b(jujur|peduli|tanggung jawab|menolong|membantu|adil|berbagi|sopan|menghormati|menyayangi)\b', 'Mengenal dan mencoba bersikap jujur, peduli, dan tanggung jawab dengan bimbingan.'),
   ('Hubungan dengan lingkungan alam', r'\b(lingkungan|kebersihan lingkungan|sampah|tanaman|alam)\b', 'Menunjukkan pemahaman tentang pentingnya menjaga kebersihan lingkungan dan kelestarian alam dengan bimbingan.')],
 'Kewargaan': [
   ('Kewargaan Lokal', r'\b(aturan|norma|keluarga|sekolah|tetangga|menaati|musyawarah)\b', 'Menunjukkan kesadaran atas aturan, norma, dan nilai sosial budaya yang berlaku di keluarga, satuan pendidikan, dan masyarakat.'),
   ('Kewargaan Nasional', r'\b(indonesia|negara|pancasila|sila|bendera|tanah air|bangsa|garuda)\b', 'Menunjukkan kesadaran atas aturan, norma, dan nilai sosial budaya yang berlaku di lingkup nasional.')],
 'Penalaran Kritis': [
   ('Penyelesaian Masalah', r'.', 'Menyelesaikan masalah sederhana dan menghasilkan solusi namun kurang tepat.'),
   ('Pengambilan Keputusan', r'.', 'Mengambil keputusan namun belum logis dan belum berdasarkan informasi yang relevan.')],
 'Kreativitas': [('Karya', r'.', 'Membuat tindakan dan/atau karya sederhana yang kreatif sesuai minat dan kesukaannya.')],
 'Kolaborasi': [
   ('Peduli', r'\b(peduli|menolong|membantu|menghibur|saling)\b', 'Mulai menunjukkan kepedulian pada teman sebaya dan anggota keluarga dengan bimbingan guru dan orang tua.'),
   ('Berbagi', r'\b(berbagi|sedekah|zakat|memberi)\b', 'Mulai berbagi hal yang dianggap penting dan berharga kepada teman sebaya dan anggota keluarga dengan bimbingan.'),
   ('Kerja sama', r'.', 'Mulai bekerjasama dengan teman sebaya dan anggota keluarga dengan bimbingan guru dan orang tua.')],
 'Kemandirian': [('Bertanggung Jawab', r'.', 'Melakukan upaya mencapai tujuan pembelajaran sesuai arahan.')],
 'Kesehatan': [
   ('Hidup bersih dan sehat', r'\b(kebersihan diri|cuci tangan|mencuci tangan|mandi|sabun|sikat gigi|gosok gigi|menggosok gigi|kuku|kuman|penyakit|sehat|kesehatan)\b', 'Berperilaku hidup bersih dan sehat dengan memperhatikan dan menjaga kebersihan diri namun masih perlu bimbingan.'),
   ('Kebugaran, kesehatan fisik, dan kesehatan mental', r'\b(olahraga|gizi|bergizi|makan|bugar|tidur|aktivitas fisik)\b', 'Berperilaku sehat fisik dan mental, menjaga kebugaran dengan berolahraga secara teratur, menerapkan pola makan sehat dan bergizi seimbang, serta mengendalikan emosi dengan bimbingan penuh.'),
   ('Kesehatan Lingkungan', r'\b(lingkungan|sampah)\b', 'Berperan aktif meningkatkan kesehatan lingkungan rumah dan sekolah dengan bimbingan penuh.')],
 'Komunikasi': [
   ('Berbicara', r'\b(ucapkan|ceritakan|sebutkan|tanyakan|melafalkan|mengucapkan|berbicara|bercerita|lafal)\b', 'Menyampaikan, menggali, dan menanggapi secara lisan berbagai jenis informasi melalui teks lisan sederhana namun belum tepat dan lancar.'),
   ('Menyimak', r'\b(dengar|menyimak|simak|didengar)\b', 'Mendengarkan secara aktif sejumlah teks lisan sederhana yang dipilih untuk mendapatkan informasi eksplisit dan implisit.'),
   ('Membaca', r'\b(baca|membaca|bacaan|teks)\b', 'Membaca secara aktif sejumlah teks tertulis sederhana yang dipilih untuk mendapatkan informasi eksplisit dan implisit.'),
   ('Menulis', r'\b(tulis|menulis|menuliskan|susun)\b', 'Menyampaikan, menggali, dan menanggapi secara lisan berbagai jenis informasi melalui teks tertulis sederhana namun belum tepat dan lancar.')],
}

def pl_sub(dim, text):
    for name, rx, ind in PL_SUB.get(dim, []):
        if re.search(rx, text.lower()): return name, ind
    return None, None

PL_NAMA = [('PL_KEIMANAN', 'Keimanan dan Ketakwaan terhadap Tuhan YME'), ('PL_KEWARGAAN', 'Kewargaan'), ('PL_KOLABORASI', 'Kolaborasi'), ('PL_KEMANDIRIAN', 'Kemandirian'),
           ('PL_KESEHATAN', 'Kesehatan'), ('PL_KREATIVITAS', 'Kreativitas'), ('PL_KOMUNIKASI', 'Komunikasi')]
def pl(x):
    qonly = qtext(x); out = []
    for key, name in PL_NAMA:
        e_q = ev(key, keytext(x)); e_tp = ev(key, x['tp'] + ' ' + x['material'])
        if e_q and e_tp: out.append({'dimensi': name, 'relevansi': 'langsung', 'bukti': {'dalam_kunci_atau_penjelasan': e_q, 'dalam_TP_materi': e_tp}})
        elif e_tp and key in ('PL_KEIMANAN', 'PL_KEWARGAAN', 'PL_KESEHATAN', 'PL_KOMUNIKASI'): out.append({'dimensi': name, 'relevansi': 'melalui_TP', 'bukti': {'dalam_TP_materi': e_tp}})
    # penalaran kritis: hanya jika tuntutan kognitif analitis/evaluatif atau soal pengelompokan/pengurutan beralasan/hitung
    cl = x['cognitive_level']
    if cl in ('menganalisis', 'mengevaluasi', 'memecahkan_masalah', 'menyimpulkan', 'membandingkan'):
        out.append({'dimensi': 'Penalaran Kritis', 'relevansi': 'langsung', 'bukti': {'level_kognitif': cl, 'tipe': x['question_type']}})
    elif x['question_type'] in ('grouping', 'ordering'):
        out.append({'dimensi': 'Penalaran Kritis', 'relevansi': 'indikatif', 'bukti': {'tipe': x['question_type']}, 'catatan': 'mengelompokkan/mengurutkan melatih logika dasar; bukan bukti penalaran kritis tingkat lanjut'})
    for d in out:
        sub, ind = pl_sub(d['dimensi'], keytext(x) + ' ' + x['question'] + ' ' + x['tp'])
        if d['dimensi'] == 'Penalaran Kritis':
            sub = 'Penyelesaian Masalah' if x['cognitive_level'] in ('memecahkan_masalah', 'menganalisis', 'membandingkan') else 'Pengambilan Keputusan'
            ind = dict((a, c) for a, b, c in PL_SUB['Penalaran Kritis'])[sub]
        d['subdimensi'] = sub or 'perlu ditetapkan guru'
        d['indikator_acuan_berkembang'] = ind
        d['keterbatasan'] = 'Tes tertulis hanya mengukur pengetahuan/pemahaman; perilaku nyata perlu observasi/rubrik guru' if x['question_type'] != 'performance_task' else 'Tugas kinerja dinilai guru dengan rubrik'
    return out

def audit_one(x, atp_ok, dup):
    iss = structure(x)
    s = {}
    s['atp'] = sc_atp(x, atp_ok); s['akurasi'] = sc_akurasi(x, iss); s['usia_bahasa'] = sc_usia(x); s['konstruksi'] = sc_konstruksi(x, iss)
    s['keunikan'] = (0, f'identik dengan {dup}') if dup else (4, 'tidak ada duplikat identik')
    k = kbc(x); p = pm(x); l = pl(x)
    # status: masalah mendasar mengalahkan skor lain (aturan keras J.8)
    names = [i for i, _ in iss]
    fatal = [n for n in names if n in ('mc_kunci_tak_valid', 'kunci_ganda', 'tf_kunci_tak_valid', 'isian_tanpa_kunci', 'opsi_kembar', 'mc_opsi_bukan_4', 'visual_tanpa_deskripsi', 'metadata_kosong')]
    if dup and dup != '-': status = 'REJECT' if False else 'REVISE'
    elif fatal: status = 'REVISE'
    elif s['atp'][0] == 0: status = 'NEEDS_REVIEW'
    elif s['atp'][0] == 2 or s['usia_bahasa'][0] <= 1 or s['akurasi'][0] <= 2: status = 'NEEDS_REVIEW'
    elif names: status = 'REVISE'
    else: status = 'PASS'
    return dict(question_id=x['id'], subject=x['_subj'], tp_id=x['tp_id'], question_type=x['question_type'], skor={k_: v[0] for k_, v in s.items()}, bukti_skor={k_: v[1] for k_, v in s.items()},
                kbc_mapping=k, deep_learning_mapping=p, graduate_profile_mapping=l, quality_status=status, issues=[f'{a}:{b}' if b else a for a, b in iss])
