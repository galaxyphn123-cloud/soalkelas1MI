# -*- coding: utf-8 -*-
"""Materi: Mengenal Huruf Hijaiah Beserta Tanda Bacanya (HJ)."""
import random
import lib

# (huruf, nama, bunyi, titik)   titik: (jumlah, posisi)
L = [
 ('ا', 'Alif', 'a', (0, '')), ('ب', 'Ba', 'b', (1, 'bawah')), ('ت', 'Ta', 't', (2, 'atas')), ('ث', 'Tsa', 'ts', (3, 'atas')),
 ('ج', 'Jim', 'j', (1, 'bawah')), ('ح', 'Ha', 'h', (0, '')), ('خ', 'Kha', 'kh', (1, 'atas')), ('د', 'Dal', 'd', (0, '')),
 ('ذ', 'Dzal', 'dz', (1, 'atas')), ('ر', 'Ra', 'r', (0, '')), ('ز', 'Zai', 'z', (1, 'atas')), ('س', 'Sin', 's', (0, '')),
 ('ش', 'Syin', 'sy', (3, 'atas')), ('ص', 'Shad', 'sh', (0, '')), ('ض', 'Dhad', 'dh', (1, 'atas')), ('ط', 'Tha', 'th', (0, '')),
 ('ظ', 'Zha', 'zh', (1, 'atas')), ('ع', "'Ain", "'", (0, '')), ('غ', 'Ghain', 'gh', (1, 'atas')), ('ف', 'Fa', 'f', (1, 'atas')),
 ('ق', 'Qaf', 'q', (2, 'atas')), ('ك', 'Kaf', 'k', (0, '')), ('ل', 'Lam', 'l', (0, '')), ('م', 'Mim', 'm', (0, '')),
 ('ن', 'Nun', 'n', (1, 'atas')), ('و', 'Wawu', 'w', (0, '')), ('ه', 'Ha', 'h', (0, '')), ('ي', 'Ya', 'y', (2, 'bawah')),
]
CH = [x[0] for x in L]
NAME = {x[0]: x[1] for x in L}
SND = {x[0]: x[2] for x in L}
DOT = {x[0]: x[3] for x in L}
AMB = {'ح', 'ه'}        # dua huruf bernama "Ha"
IDX = {c: i + 1 for i, c in enumerate(CH)}

def dot_txt(c):
    n, pos = DOT[c]
    return 'tidak bertitik' if n == 0 else f'{ {1:"satu",2:"dua",3:"tiga"}[n] } titik di {pos}'

ALL_DOT = ['tidak bertitik', 'satu titik di atas', 'dua titik di atas', 'tiga titik di atas', 'satu titik di bawah', 'dua titik di bawah']

# harakat: huruf contoh dipakai: ب
FA, KA, DA, SU, TA, F2, K2, D2 = 'َ', 'ِ', 'ُ', 'ْ', 'ّ', 'ً', 'ٍ', 'ٌ'
HAR = [  # nama, tanda, letak, bunyi, ciri
 ('fathah', FA, 'di atas huruf', 'a', 'garis kecil miring di atas huruf'),
 ('kasrah', KA, 'di bawah huruf', 'i', 'garis kecil miring di bawah huruf'),
 ('dammah', DA, 'di atas huruf', 'u', 'berbentuk seperti huruf wawu kecil di atas huruf'),
 ('sukun', SU, 'di atas huruf', 'huruf mati (tanpa vokal)', 'berbentuk bulatan kecil di atas huruf'),
 ('tasydid', TA, 'di atas huruf', 'huruf dibaca ganda', 'berbentuk seperti huruf w kecil di atas huruf'),
 ('fathatain', F2, 'di atas huruf', 'an', 'dua garis miring di atas huruf'),
 ('kasratain', K2, 'di bawah huruf', 'in', 'dua garis miring di bawah huruf'),
 ('dammatain', D2, 'di atas huruf', 'un', 'dua tanda dammah di atas huruf'),
]

def with_h(c, v):
    """huruf berharakat; alif memakai hamzah sebagai pembawa."""
    if c == 'ا':
        return {FA: 'أَ', KA: 'إِ', DA: 'أُ'}[v]
    return c + v

VOW = [(FA, 'a'), (KA, 'i'), (DA, 'u')]
SIM = {'ب': 'ت', 'ت': 'ب', 'ث': 'س', 'ج': 'ح', 'ح': 'خ', 'خ': 'ح', 'د': 'ذ', 'ذ': 'د', 'ر': 'ز', 'ز': 'ر', 'س': 'ش', 'ش': 'س',
       'ص': 'ض', 'ض': 'ص', 'ط': 'ظ', 'ظ': 'ط', 'ع': 'غ', 'غ': 'ع', 'ف': 'ق', 'ق': 'ف', 'ك': 'ق', 'ل': 'م', 'م': 'ن', 'ن': 'م',
       'و': 'ي', 'ه': 'ح', 'ي': 'و', 'ا': 'ع'}

# --- rangkaian suku kata: (bagian-bagian, latin per bagian, arti) -------------------------------------
WORDS = [
 (['كَ', 'تَ', 'بَ'], ['ka', 'ta', 'ba'], 'dia telah menulis'), (['دَ', 'رَ', 'سَ'], ['da', 'ra', 'sa'], 'dia telah belajar'),
 (['جَ', 'لَ', 'سَ'], ['ja', 'la', 'sa'], 'dia telah duduk'), (['ذَ', 'هَ', 'بَ'], ['dza', 'ha', 'ba'], 'dia telah pergi'),
 (['فَ', 'تَ', 'حَ'], ['fa', 'ta', 'ha'], 'dia telah membuka'), (['نَ', 'صَ', 'رَ'], ['na', 'sha', 'ra'], 'dia telah menolong'),
 (['عَ', 'لِ', 'مَ'], ["'a", 'li', 'ma'], 'dia telah mengetahui'), (['شَ', 'رِ', 'بَ'], ['sya', 'ri', 'ba'], 'dia telah minum'),
 (['حَ', 'سُ', 'نَ'], ['ha', 'su', 'na'], 'dia menjadi baik'), (['كَ', 'رُ', 'مَ'], ['ka', 'ru', 'ma'], 'dia menjadi mulia'),
 (['سَ', 'مِ', 'عَ'], ['sa', 'mi', "'a"], 'dia telah mendengar'), (['خَ', 'رَ', 'جَ'], ['kha', 'ra', 'ja'], 'dia telah keluar'),
 (['ضَ', 'رَ', 'بَ'], ['dha', 'ra', 'ba'], 'dia telah memukul'), (['قَ', 'رَ', 'أَ'], ['qa', 'ra', "'a"], 'dia telah membaca'),
 (['غَ', 'فَ', 'رَ'], ['gha', 'fa', 'ra'], 'dia telah mengampuni'), (['ثَ', 'بَ', 'تَ'], ['tsa', 'ba', 'ta'], 'dia telah tetap'),
 (['وَ', 'جَ', 'دَ'], ['wa', 'ja', 'da'], 'dia telah mendapati'), (['زَ', 'رَ', 'عَ'], ['za', 'ra', "'a"], 'dia telah menanam'),
 (['طَ', 'لَ', 'بَ'], ['tha', 'la', 'ba'], 'dia telah mencari'), (['صَ', 'بَ', 'رَ'], ['sha', 'ba', 'ra'], 'dia telah bersabar'),
 (['ظَ', 'لَ', 'مَ'], ['zha', 'la', 'ma'], 'dia telah berbuat zalim'), (['يَ', 'دٌ'], ['ya', 'dun'], 'tangan'),
 (['قُ', 'لْ'], ['qu', 'l'], 'katakanlah'), (['لَ', 'مْ'], ['la', 'm'], 'tidak (lampau)'), (['مِ', 'نْ'], ['mi', 'n'], 'dari'),
 (['عَ', 'نْ'], ["'a", 'n'], 'dari/tentang'), (['بَ', 'لْ'], ['ba', 'l'], 'bahkan'), (['هَ', 'لْ'], ['ha', 'l'], 'apakah'),
 (['بِ', 'سْ', 'مِ'], ['bi', 's', 'mi'], 'dengan nama'), (['أُ', 'مٌّ'], ['u', 'mmun'], 'ibu'), (['أَ', 'بٌ'], ['a', 'bun'], 'ayah'),
 (['رَ', 'بِّ'], ['ra', 'bbi'], 'Tuhan'), (['كُ', 'لِّ'], ['ku', 'lli'], 'setiap'), (['ثُ', 'مَّ'], ['tsu', 'mma'], 'kemudian'),
 (['حَ', 'جٌّ'], ['ha', 'jjun'], 'haji'), (['مَ', 'دَّ'], ['ma', 'dda'], 'dia membentangkan'),
]


def build(seed=7):
    rng = random.Random(seed)
    tps = ['Murid mampu mengenal huruf hijaiah dan tanda bacanya dengan benar.',
           'Murid mampu menyesuaikan pelafalan huruf hijaiah dengan baik dan benar.',
           'Murid mampu membandingkan huruf hijaiah dan tanda bacanya dengan benar.',
           'Murid mampu merangkaikan huruf hijaiah bertanda baca dengan baik dan benar sebagai wujud cinta Allah dan Rasul-Nya, serta cinta Ilmu.']
    p = lib.Pool('HJ', 'Mengenal Huruf Hijaiah Beserta Tanda Bacanya', tps, 143, tpw=(40, 40, 30, 33))
    U = [c for c in CH if c not in AMB]            # huruf dengan nama unik

    # ================= TP1: mengenal huruf & tanda baca =================
    p.mc(1, 'Huruf hijaiah berjumlah ... huruf.', '28', ['26', '29', '30', '24'], 'Huruf hijaiah berjumlah 28 huruf, dari Alif sampai Ya.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.fill(1, 'Banyaknya huruf hijaiah adalah .... huruf.', '28', 'Huruf hijaiah ada 28 huruf.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.tf(1, 'Huruf hijaiah berjumlah 28 huruf.', True, 'Benar, ada 28 huruf hijaiah.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.tf(1, 'Huruf hijaiah berjumlah 30 huruf.', False, 'Salah, huruf hijaiah berjumlah 28.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.mc(1, 'Huruf hijaiah yang pertama adalah ....', 'Alif (ا)', ['Ba (ب)', 'Ta (ت)', 'Ya (ي)'], 'Huruf hijaiah pertama adalah Alif.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.mc(1, 'Huruf hijaiah yang terakhir adalah ....', 'Ya (ي)', ['Alif (ا)', 'Ba (ب)', 'Nun (ن)'], 'Huruf hijaiah terakhir adalah Ya.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.fill(1, 'Huruf hijaiah yang terakhir adalah huruf ....', 'Ya (ي)', 'Huruf ke-28 adalah Ya.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.tf(1, 'Huruf hijaiah dibaca dan ditulis dari kanan ke kiri.', True, 'Tulisan Arab bergerak dari kanan ke kiri.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.tf(1, 'Huruf hijaiah dibaca dan ditulis dari kiri ke kanan.', False, 'Tulisan Arab dibaca dan ditulis dari kanan ke kiri.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.mc(1, 'Huruf hijaiah ditulis dari arah ....', 'kanan ke kiri', ['kiri ke kanan', 'atas ke bawah saja', 'bawah ke atas saja'], 'Menulis huruf Arab dimulai dari kanan.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')
    p.mc(1, 'Al-Qur\'an ditulis dengan huruf ....', 'hijaiah', ['latin', 'jawa', 'romawi'], 'Al-Qur\'an menggunakan huruf hijaiah.', 'easy', 'mengingat', 'Mengenal huruf hijaiah')

    for i, c in enumerate(CH):
        p.gk = f'l1{c}'
        nm = NAME[c]; k = i + 1
        others = [NAME[x] for x in CH if NAME[x] != nm]
        p.mc(1, f'Huruf {c} bernama ....', nm, others, f'Huruf {c} bernama {nm}.', 'easy', 'mengenali', 'Mengenal nama huruf')
        p.tf(1, f'Huruf {c} bernama {nm}.', True, f'Benar, {c} bernama {nm}.', 'easy', 'mengenali', 'Mengenal nama huruf')
        wrong_name = [x for x in others][i % len(others)]
        p.tf(1, f'Huruf {c} bernama {wrong_name}.', False, f'Salah. {c} bernama {nm}.', 'easy', 'mengenali', 'Mengenal nama huruf')
        if c not in AMB:
            p.mc(1, f'Huruf {nm} ditulis ....', c, [x for x in CH if x != c], f'{nm} ditulis {c}.', 'easy', 'mengenali', 'Mengenal bentuk huruf')
            p.fill(1, f'Huruf {nm} ditulis dengan lambang ....', c, f'{nm} ditulis {c}.', 'easy', 'mengenali', 'Mengenal bentuk huruf')
        p.mc(1, f'Huruf {c} memiliki titik ....', dot_txt(c), [d for d in ALL_DOT if d != dot_txt(c)], f'Huruf {c} ({nm}) {dot_txt(c)}.', 'medium', 'mengenali', 'Mengenal ciri huruf')
        p.tf(1, f'Huruf {c} {dot_txt(c)}.', True, f'Benar, {c} {dot_txt(c)}.', 'easy', 'mengenali', 'Mengenal ciri huruf')
        wd = [d for d in ALL_DOT if d != dot_txt(c)]
        p.tf(1, f'Huruf {c} {wd[i % len(wd)]}.', False, f'Salah. {c} {dot_txt(c)}.', 'medium', 'mengenali', 'Mengenal ciri huruf')
        p.fill(1, f'Huruf {c} {dot_txt(c)}. Nama huruf itu adalah ....', nm, f'{c} adalah huruf {nm}.', 'hard', 'mengenali', 'Mengenal nama huruf') if c not in AMB and DOT[c][0] > 0 and len([x for x in CH if DOT[x] == DOT[c]]) == 1 else None
        p.fill(1, f'Huruf ke-{k} dalam urutan huruf hijaiah adalah huruf ....', c, f'Huruf ke-{k} adalah {c} ({nm}).', 'hard', 'mengingat', 'Mengenal urutan huruf') if c not in AMB else None
        p.mc(1, f'Huruf {c} berada pada urutan ke-... huruf hijaiah.', str(k), [str(x) for x in range(1, 29) if x != k and abs(x - k) <= 4][:6], f'{c} ({nm}) adalah huruf ke-{k}.', 'hard', 'mengingat', 'Mengenal urutan huruf')
        if i < 27:
            p.mc(1, f'Huruf hijaiah setelah {c} adalah ....', CH[i + 1], [x for x in CH if x not in (CH[i + 1], c)], f'Setelah {c} adalah {CH[i+1]}.', 'medium', 'mengingat', 'Mengenal urutan huruf')
        if i > 0:
            p.mc(1, f'Huruf hijaiah sebelum {c} adalah ....', CH[i - 1], [x for x in CH if x not in (CH[i - 1], c)], f'Sebelum {c} adalah {CH[i-1]}.', 'medium', 'mengingat', 'Mengenal urutan huruf')
    p.gk = None
    for s in range(0, 25):
        seg = CH[s:s + 4]
        p.order(1, 'Urutkan huruf hijaiah berikut sesuai urutan hijaiah!', seg, 'Urutan: ' + ' - '.join(seg) + '.', 'medium', 'mengurutkan', 'Mengenal urutan huruf')
    for s in range(0, 22, 3):
        idx = CH[s:s + 4]
        p.match(1, 'Jodohkan huruf hijaiah dengan namanya!', [(c, NAME[c]) for c in idx if c not in AMB], 'Setiap huruf dipasangkan dengan namanya.', 'medium', 'mencocokkan', 'Mengenal nama huruf')
    p.group(1, 'Kelompokkan huruf berikut berdasarkan titiknya: ا, ب, ت, ث, ج, د, ز, ش, ي, ر.',
            {'tidak bertitik': ['ا', 'د', 'ر'], 'bertitik satu': ['ب', 'ج', 'ز'], 'bertitik dua': ['ت', 'ي'], 'bertitik tiga': ['ث', 'ش']},
            'Hitung jumlah titik pada tiap huruf.', 'medium', 'mengelompokkan', 'Mengenal ciri huruf')
    p.group(1, 'Kelompokkan huruf berikut berdasarkan letak titiknya: ب, ت, ج, خ, ي, ق, ن, ف.',
            {'titik di atas': ['ت', 'خ', 'ق', 'ن', 'ف'], 'titik di bawah': ['ب', 'ج', 'ي']},
            'Perhatikan letak titik pada tiap huruf.', 'medium', 'mengelompokkan', 'Mengenal ciri huruf')
    p.mc(1, 'Huruf hijaiah yang bertitik dua di bawah adalah ....', 'ي', ['ت', 'ب', 'ق'], 'Hanya Ya (ي) yang bertitik dua di bawah.', 'medium', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Huruf yang bertitik satu di bawah adalah ....', 'ب', ['ت', 'ن', 'ف'], 'Ba (ب) dan Jim (ج) bertitik satu di bawah.', 'medium', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Selain Ba, huruf yang bertitik satu di bawah adalah ....', 'ج', ['خ', 'ن', 'ز'], 'Jim (ج) bertitik satu di bawah.', 'medium', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Huruf yang bertitik dua di atas adalah ....', 'ت', ['ب', 'ث', 'ي'], 'Ta (ت) dan Qaf (ق) bertitik dua di atas.', 'medium', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Selain Ta, huruf yang bertitik dua di atas adalah ....', 'ق', ['ن', 'ف', 'ي'], 'Qaf (ق) bertitik dua di atas.', 'hard', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Huruf yang bertitik tiga di atas adalah ....', 'ث', ['ج', 'ب', 'ي'], 'Tsa (ث) dan Syin (ش) bertitik tiga di atas.', 'medium', 'mengenali', 'Mengenal ciri huruf')
    p.mc(1, 'Selain Tsa, huruf yang bertitik tiga di atas adalah ....', 'ش', ['س', 'ص', 'ض'], 'Syin (ش) bertitik tiga di atas.', 'hard', 'mengenali', 'Mengenal ciri huruf')

    # tanda baca
    p.mc(1, 'Tanda-tanda pada huruf hijaiah yang menentukan cara baca disebut ....', 'tanda baca (harakat)', ['titik huruf', 'nomor ayat', 'tanda seru'], 'Harakat adalah tanda baca yang mengatur bunyi huruf.', 'easy', 'mengingat', 'Mengenal tanda baca')
    for (nm, sym, letak, bunyi, ciri) in HAR:
        p.gk = f'h1{nm}'
        o = [h[0] for h in HAR if h[0] != nm]
        ex = 'ب' + sym
        p.mc(1, f'Tanda baca pada huruf {ex} bernama ....', nm, o, f'{ex} memakai {nm}: {ciri}.', 'easy', 'mengenali', 'Mengenal tanda baca',
             visual=f'Kartu besar bergambar huruf Ba dengan tanda baca di atas/bawahnya: {ex}, huruf berwarna biru, tanda baca berwarna merah.') if True else None
        p.mc(1, f'Tanda baca {nm} terletak ....', letak, [x for x in ('di atas huruf', 'di bawah huruf', 'di samping huruf', 'di dalam huruf') if x != letak], f'{nm.capitalize()} {letak}.', 'easy', 'mengingat', 'Mengenal tanda baca')
        p.mc(1, f'Ciri tanda baca {nm} adalah ....', ciri, [h[4] for h in HAR if h[4] != ciri], f'{nm.capitalize()}: {ciri}.', 'medium', 'memahami', 'Mengenal tanda baca')
        p.mc(1, f'Tanda baca yang {ciri} bernama ....', nm, o, f'Itulah {nm}.', 'medium', 'mengenali', 'Mengenal tanda baca')
        p.tf(1, f'Tanda baca {nm} terletak {letak}.', True, f'Benar, {nm} {letak}.', 'easy', 'mengingat', 'Mengenal tanda baca')
        p.tf(1, f'Tanda baca {nm} terletak {"di atas huruf" if letak == "di bawah huruf" else "di bawah huruf"}.', False, f'Salah. {nm.capitalize()} {letak}.', 'easy', 'mengingat', 'Mengenal tanda baca')
        p.fill(1, f'Tanda baca yang {ciri} bernama ....', nm, f'Itulah {nm}.', 'medium', 'mengenali', 'Mengenal tanda baca')
        p.fill(1, f'Huruf {ex} memakai tanda baca ....', nm, f'{ex} memakai {nm}.', 'easy', 'mengenali', 'Mengenal tanda baca')
    p.gk = None
    p.match(1, 'Jodohkan nama tanda baca dengan cirinya!', [(h[0], h[4]) for h in HAR[:4]], 'Setiap tanda baca memiliki ciri sendiri.', 'medium', 'mencocokkan', 'Mengenal tanda baca')
    p.match(1, 'Jodohkan nama tanda baca dengan cirinya!', [(h[0], h[4]) for h in HAR[4:]], 'Setiap tanda baca memiliki ciri sendiri.', 'medium', 'mencocokkan', 'Mengenal tanda baca')
    p.group(1, 'Kelompokkan tanda baca berikut berdasarkan letaknya: fathah, kasrah, dammah, kasratain, fathatain.',
            {'di atas huruf': ['fathah', 'dammah', 'fathatain'], 'di bawah huruf': ['kasrah', 'kasratain']}, 'Kasrah dan kasratain di bawah huruf, lainnya di atas.', 'medium', 'mengelompokkan', 'Mengenal tanda baca')
    p.group(1, 'Kelompokkan tanda baca berikut: fathah, fathatain, kasrah, kasratain, dammah, dammatain.',
            {'satu tanda (bunyi a/i/u)': ['fathah', 'kasrah', 'dammah'], 'dua tanda (tanwin)': ['fathatain', 'kasratain', 'dammatain']}, 'Tanwin berupa dua tanda, bunyinya an, in, un.', 'medium', 'mengelompokkan', 'Mengenal tanda baca')
    p.mc(1, 'Tanda baca yang disebut tanwin adalah ....', 'fathatain, kasratain, dan dammatain', ['fathah, kasrah, dan dammah', 'sukun dan tasydid', 'fathah dan sukun'], 'Tanwin terdiri atas fathatain, kasratain, dan dammatain.', 'medium', 'mengingat', 'Mengenal tanda baca')
    p.fill(1, 'Tanda baca fathah, kasrah, dan dammah berbunyi ...., ...., dan ....', 'a, i, u', 'Fathah = a, kasrah = i, dammah = u.', 'easy', 'mengingat', 'Mengenal tanda baca', typ='completion')

    # ================= TP2: pelafalan =================
    for i, c in enumerate(CH):
        p.gk = f'l2{c}'
        for (v, snd) in VOW:
            s = SND[c]
            full = with_h(c, v) if c != 'ا' else with_h(c, v)
            latin = (s + snd) if c != 'ا' else snd
            if c == 'ع': latin = "'" + snd
            nm = {FA: 'fathah', KA: 'kasrah', DA: 'dammah'}[v]
            wrong = []
            for (v2, s2) in VOW:
                if v2 != v:
                    wrong.append((s + s2) if c != 'ا' else s2)
            sim = SIM[c]
            wrong.append((SND[sim] + snd) if sim != 'ا' else snd)
            wrong = [w if c != 'ع' else "'" + w[-1] for w in wrong[:2]] + wrong[2:]
            p.mc(2, f'Cara membaca {full} adalah ....', latin, wrong + [SND[sim] + 'a', SND[CH[(i + 3) % 28]] + snd, SND[CH[(i + 7) % 28]] + snd], f'{full} dibaca "{latin}" karena {c} berharakat {nm}.', 'easy' if v == FA else 'medium', 'mengenali', 'Melafalkan huruf berharakat')
            p.tf(2, f'{full} dibaca "{latin}".', True, f'Benar, {full} dibaca {latin}.', 'easy', 'mengenali', 'Melafalkan huruf berharakat')
            p.tf(2, f'{full} dibaca "{wrong[0]}".', False, f'Salah. {full} dibaca {latin}.', 'medium', 'mengenali', 'Melafalkan huruf berharakat')
            if c not in AMB and c != 'ا':
                p.mc(2, f'Tulisan Arab untuk bunyi "{latin}" adalah ....', full, [with_h(c, v2) for (v2, _) in VOW if v2 != v] + [with_h(SIM[c], v)],
                     f'Bunyi {latin} ditulis {full}.', 'medium', 'mengenali', 'Melafalkan huruf berharakat')
                p.fill(2, f'Bunyi "{latin}" ditulis dengan huruf Arab ....', full, f'{latin} = {full}.', 'hard', 'mengenali', 'Melafalkan huruf berharakat')
            p.fill(2, f'Huruf {c} berharakat {nm} dibaca ....', latin, f'{c} + {nm} = {latin}.', 'medium', 'mengenali', 'Melafalkan huruf berharakat') if c != 'ا' else None
    # sukun, tasydid, tanwin
    SUK = [('أَبْ', 'ab'), ('أُمْ', 'um'), ('إِسْ', 'is'), ('أَنْ', 'an'), ('إِنْ', 'in'), ('أُنْ', 'un'), ('أَلْ', 'al'), ('إِلْ', 'il'), ('أُلْ', 'ul'), ('أَتْ', 'at'), ('إِتْ', 'it'), ('أُتْ', 'ut')]
    for (a, l) in SUK:
        p.gk = f'suk{a}'
        p.mc(2, f'Cara membaca {a} (huruf kedua bersukun) adalah ....', l, [x[1] for x in SUK if x[1] != l], f'{a} dibaca {l}; huruf bersukun dibaca mati.', 'medium', 'mengenali', 'Melafalkan huruf bersukun')
        p.tf(2, f'{a} dibaca "{l}".', True, f'Benar, {a} dibaca {l}.', 'easy', 'mengenali', 'Melafalkan huruf bersukun')
        p.fill(2, f'Huruf bersukun {a} dibaca ....', l, f'{a} = {l}.', 'medium', 'mengenali', 'Melafalkan huruf bersukun')
    TAS = [('رَبَّ', 'rab-ba'), ('سُمَّ', 'sum-ma'), ('عَمَّ', "'am-ma"), ('رِبِّ', 'rib-bi'), ('مَدَّ', 'mad-da'), ('كُلِّ', 'kul-li'), ('ثُمَّ', 'tsum-ma'), ('شَدَّ', 'syad-da'), ('حَجَّ', 'haj-ja'), ('رُدَّ', 'rud-da')]
    p.gk = None
    for (a, l) in TAS:
        p.gk = f'tas{a}'
        p.mc(2, f'Bacaan huruf bertasydid {a} adalah ....', l, [x[1] for x in TAS if x[1] != l], f'{a} dibaca {l} dengan huruf bertasydid ditekan/dibaca ganda.', 'hard', 'mengenali', 'Melafalkan huruf bertasydid')
        p.tf(2, f'{a} dibaca "{l}".', True, f'Benar, {a} dibaca {l}.', 'medium', 'mengenali', 'Melafalkan huruf bertasydid')
        p.fill(2, f'Cara membaca {a} adalah ....', l, f'{a} = {l}.', 'hard', 'mengenali', 'Melafalkan huruf bertasydid')
    for c in ['ب', 'ت', 'ج', 'ك', 'ل', 'م', 'ن', 'س', 'ر', 'د']:
        s = SND[c]
        for (mark, snd, nm) in [(F2, 'an', 'fathatain'), (K2, 'in', 'kasratain'), (D2, 'un', 'dammatain')]:
            full = c + mark
            if mark == F2: full = c + 'ً' + 'ا'
            lat = s + snd
            others = [s + 'an', s + 'in', s + 'un']
            p.mc(2, f'Bunyi tanwin pada {full} dibaca ....', lat, [x for x in others if x != lat] + [s + 'a'], f'{full} berharakat tanwin {nm}, dibaca {lat}.', 'medium', 'mengenali', 'Melafalkan tanwin')
            p.tf(2, f'{full} dibaca "{lat}".', True, f'Benar, {full} dibaca {lat}.', 'easy', 'mengenali', 'Melafalkan tanwin')
    p.mc(2, 'Bunyi fathatain, kasratain, dan dammatain berturut-turut adalah ....', 'an, in, un', ['a, i, u', 'in, an, un', 'un, in, an'], 'Fathatain = an, kasratain = in, dammatain = un.', 'medium', 'mengingat', 'Melafalkan tanwin')
    p.mc(2, 'Huruf yang dibaca ganda (ditekan) memakai tanda ....', 'tasydid', ['sukun', 'fathah', 'kasrah'], 'Tasydid membuat huruf dibaca ganda.', 'medium', 'mengingat', 'Melafalkan huruf bertasydid')
    p.mc(2, 'Huruf yang dibaca mati (tanpa vokal) memakai tanda ....', 'sukun', ['tasydid', 'dammah', 'kasrah'], 'Sukun membuat huruf dibaca mati.', 'medium', 'mengingat', 'Melafalkan huruf bersukun')
    for s in range(0, 22, 3):
        seg = [c for c in CH[s:s + 7]]
        txt = ' '.join(with_h(c, FA) for c in seg)
        p.perf(2, f'Bacalah huruf hijaiah berfathah berikut dengan lafal yang benar: {txt}', 'Dinilai guru: ketepatan lafal tiap huruf dan kelancaran (skala 1-4).', 'Murid melafalkan huruf berfathah dengan benar.', 'medium', 'menerapkan', 'Melafalkan huruf berharakat')
    p.perf(2, 'Bacalah huruf Ba, Ta, Tsa dengan fathah, kasrah, dan dammah secara berurutan di depan guru!', 'Dinilai guru: ketepatan a-i-u pada tiap huruf (skala 1-4).', 'Murid melafalkan tiga harakat dengan benar.', 'medium', 'menerapkan', 'Melafalkan huruf berharakat')
    p.perf(2, 'Bacalah: أَبْ، أُمْ، إِسْ dengan benar, perhatikan huruf yang bersukun!', 'Dinilai guru: bunyi huruf mati (skala 1-4).', 'Murid melafalkan huruf bersukun dengan benar.', 'medium', 'menerapkan', 'Melafalkan huruf bersukun')
    p.perf(2, 'Bacalah: رَبَّ، سُمَّ، كُلِّ dengan benar, tekan huruf yang bertasydid!', 'Dinilai guru: penekanan tasydid (skala 1-4).', 'Murid melafalkan huruf bertasydid dengan benar.', 'hard', 'menerapkan', 'Melafalkan huruf bertasydid')

    # ================= TP3: membandingkan =================
    PAIRS = [('ب', 'ت', 'Ba (ب) bertitik satu di bawah, Ta (ت) bertitik dua di atas'), ('ت', 'ث', 'Ta (ت) bertitik dua di atas, Tsa (ث) bertitik tiga di atas'),
             ('ب', 'ث', 'Ba (ب) bertitik satu di bawah, Tsa (ث) bertitik tiga di atas'), ('ج', 'ح', 'Jim (ج) bertitik satu di bawah, Ha (ح) tidak bertitik'),
             ('ح', 'خ', 'Ha (ح) tidak bertitik, Kha (خ) bertitik satu di atas'), ('ج', 'خ', 'Jim (ج) bertitik satu di bawah, Kha (خ) bertitik satu di atas'),
             ('د', 'ذ', 'Dal (د) tidak bertitik, Dzal (ذ) bertitik satu di atas'), ('ر', 'ز', 'Ra (ر) tidak bertitik, Zai (ز) bertitik satu di atas'),
             ('س', 'ش', 'Sin (س) tidak bertitik, Syin (ش) bertitik tiga di atas'), ('ص', 'ض', 'Shad (ص) tidak bertitik, Dhad (ض) bertitik satu di atas'),
             ('ط', 'ظ', 'Tha (ط) tidak bertitik, Zha (ظ) bertitik satu di atas'), ('ع', 'غ', "'Ain (ع) tidak bertitik, Ghain (غ) bertitik satu di atas"),
             ('ف', 'ق', 'Fa (ف) bertitik satu di atas, Qaf (ق) bertitik dua di atas'), ('ن', 'ي', 'Nun (ن) bertitik satu di atas, Ya (ي) bertitik dua di bawah'),
             ('ب', 'ن', 'Ba (ب) bertitik satu di bawah, Nun (ن) bertitik satu di atas'), ('ت', 'ق', 'Ta (ت) dan Qaf (ق) sama-sama bertitik dua di atas, tetapi bentuk dasarnya berbeda'),
             ('ث', 'ش', 'Tsa (ث) dan Syin (ش) sama-sama bertitik tiga di atas, tetapi bentuk dasarnya berbeda')]
    for (a, b, why) in PAIRS:
        na, nb = NAME[a], NAME[b]
        if a in AMB or b in AMB:
            tag_a, tag_b = a, b
        p.mc(3, f'Perbedaan huruf {a} dan {b} adalah ....', why,
             ['keduanya tidak bertitik', 'keduanya sama persis', 'keduanya bertitik tiga di bawah'], f'{why}.', 'medium', 'membandingkan', 'Membandingkan huruf')
        p.tf(3, f'Huruf {a} dan {b} sama persis bentuk dan titiknya.', False, f'Salah. {why}.', 'easy', 'membandingkan', 'Membandingkan huruf')
        p.mc(3, f'Perhatikan gambar dua huruf! Huruf yang {dot_txt(b)} adalah ....', b, ([a] if dot_txt(a) != dot_txt(b) else []) + [x for x in CH if dot_txt(x) != dot_txt(b) and x not in (a, b)][3:6],
             f'{why}.', 'medium', 'membandingkan', 'Membandingkan huruf',
             visual=f'Dua kartu huruf besar berdampingan: kartu kiri bertuliskan {a}, kartu kanan bertuliskan {b}.') if DOT[a] != DOT[b] else None
        p.mc(3, f'Perhatikan gambar dua huruf! Huruf yang {dot_txt(a)} adalah ....', a, [b] + [x for x in CH if dot_txt(x) != dot_txt(a) and x not in (a, b)][2:5],
             f'{why}.', 'medium', 'membandingkan', 'Membandingkan huruf',
             visual=f'Dua kartu huruf besar berdampingan: kartu kiri bertuliskan {a}, kartu kanan bertuliskan {b}.') if DOT[a] != DOT[b] else None
        p.tf(3, f'Huruf {a} {dot_txt(a)}, sedangkan huruf {b} {dot_txt(b)}.', True, f'Benar. {why}.', 'easy', 'membandingkan', 'Membandingkan huruf')
        p.tf(3, f'Huruf {a} {dot_txt(b)}, sedangkan huruf {b} {dot_txt(a)}.', False, f'Salah. {why}.', 'medium', 'membandingkan', 'Membandingkan huruf') if DOT[a] != DOT[b] else None
        p.fill(3, f'Huruf {a} dan {b} dibedakan oleh jumlah dan letak ....', 'titik', f'{why}.', 'easy', 'membandingkan', 'Membandingkan huruf') if DOT[a] != DOT[b] else None
    for a, b in [('ب', 'ت'), ('س', 'ش'), ('د', 'ذ'), ('ر', 'ز'), ('ج', 'خ'), ('ف', 'ق')]:
        p.mc(3, f'Huruf yang berbeda dari kelompok titiknya: {a}, {b}, ....', 'tidak ada; semua bertitik sama', ['ا'], 'x', 'easy') if False else None
    # bunyi mirip
    SOUNDS = [('س', 'ص', 'sa', 'sha'), ('ت', 'ط', 'ta', 'tha'), ('د', 'ض', 'da', 'dha'), ('ز', 'ظ', 'za', 'zha'), ('ك', 'ق', 'ka', 'qa'), ('ذ', 'ز', 'dza', 'za'), ('ث', 'س', 'tsa', 'sa'), ('ح', 'خ', 'ha', 'kha')]
    for (a, b, la, lb) in SOUNDS:
        p.mc(3, f'Bacaan huruf {with_h(a, FA)} dan {with_h(b, FA)} berturut-turut adalah ....', f'{la} dan {lb}', [f'{lb} dan {la}', f'{la} dan {la}', f'{lb} dan {lb}'],
             f'{with_h(a, FA)} dibaca {la}, {with_h(b, FA)} dibaca {lb}.', 'medium', 'membandingkan', 'Membandingkan bunyi huruf')
        p.tf(3, f'Bunyi {with_h(a, FA)} ("{la}") sama persis dengan bunyi {with_h(b, FA)} ("{lb}").', False, f'Salah. Bunyinya berbeda: {la} dan {lb}.', 'easy', 'membandingkan', 'Membandingkan bunyi huruf')
        p.fill(3, f'{with_h(a, FA)} dibaca "{la}", sedangkan {with_h(b, FA)} dibaca ....', lb, f'{with_h(b, FA)} dibaca {lb}.', 'medium', 'membandingkan', 'Membandingkan bunyi huruf')
    # membandingkan harakat
    CMP = [('fathah', 'kasrah', 'fathah di atas huruf berbunyi a, kasrah di bawah huruf berbunyi i'),
           ('fathah', 'dammah', 'fathah berbunyi a, dammah berbunyi u'), ('kasrah', 'dammah', 'kasrah berbunyi i dan di bawah huruf, dammah berbunyi u dan di atas huruf'),
           ('fathah', 'fathatain', 'fathah berbunyi a, fathatain berbunyi an'), ('kasrah', 'kasratain', 'kasrah berbunyi i, kasratain berbunyi in'),
           ('dammah', 'dammatain', 'dammah berbunyi u, dammatain berbunyi un'), ('sukun', 'tasydid', 'sukun membuat huruf dibaca mati, tasydid membuat huruf dibaca ganda'),
           ('sukun', 'fathah', 'sukun membuat huruf mati, fathah membuat huruf berbunyi a')]
    for a, b, why in CMP:
        p.mc(3, f'Perbedaan {a} dan {b} adalah ....', why, ['keduanya sama persis', 'keduanya berbunyi a', 'keduanya terletak di bawah huruf'], f'{why.capitalize()}.', 'medium', 'membandingkan', 'Membandingkan tanda baca')
        p.tf(3, f'{a.capitalize()} dan {b} memiliki bunyi yang sama.', False, f'Salah. {why.capitalize()}.', 'easy', 'membandingkan', 'Membandingkan tanda baca')
        p.fill(3, f'{a.capitalize()} dan {b} berbeda pada ....', 'bunyi/cara baca', f'{why.capitalize()}.', 'medium', 'membandingkan', 'Membandingkan tanda baca')
    for c in ['ب', 'ت', 'م', 'ن', 'ك']:
        a, b, d = with_h(c, FA), with_h(c, KA), with_h(c, DA)
        p.mc(3, f'Perhatikan {a}, {b}, dan {d}! Huruf yang dibaca "{SND[c]}i" adalah ....', b, [a, d, c + SU], f'{b} berharakat kasrah sehingga dibaca {SND[c]}i.', 'medium', 'membandingkan', 'Membandingkan huruf berharakat')
        p.mc(3, f'Perhatikan {a}, {b}, dan {d}! Huruf yang dibaca "{SND[c]}u" adalah ....', d, [a, b, c + SU], f'{d} berharakat dammah sehingga dibaca {SND[c]}u.', 'medium', 'membandingkan', 'Membandingkan huruf berharakat')
        p.tf(3, f'{a} dan {b} dibaca dengan bunyi yang sama.', False, f'Salah. {a} dibaca {SND[c]}a, {b} dibaca {SND[c]}i.', 'easy', 'membandingkan', 'Membandingkan huruf berharakat')
    p.group(3, 'Kelompokkan huruf berikut: ب, ت, ث, ج, ح, خ.', {'sama-sama bertitik (berbeda jumlah/letak)': ['ب', 'ت', 'ث'], 'bentuk dasar seperti mangkuk terbuka (ج ح خ)': ['ج', 'ح', 'خ']},
            'Ba–Ta–Tsa berbentuk perahu; Jim–Ha–Kha berbentuk mirip kait.', 'hard', 'mengelompokkan', 'Membandingkan huruf')
    p.group(3, 'Kelompokkan huruf berikut berdasarkan bentuk dasarnya: ب, ت, ث, د, ذ, ر, ز.', {'mirip huruf Ba': ['ب', 'ت', 'ث'], 'mirip huruf Dal': ['د', 'ذ'], 'mirip huruf Ra': ['ر', 'ز']},
            'Huruf dengan bentuk dasar sama dibedakan oleh titik.', 'hard', 'mengelompokkan', 'Membandingkan huruf')
    p.match(3, 'Jodohkan pasangan huruf dengan pembeda utamanya!', [('ب dan ت', 'letak dan jumlah titik'), ('د dan ذ', 'ada atau tidak titik'), ('س dan ش', 'ada atau tidak tiga titik'), ('ف dan ق', 'satu atau dua titik')],
            'Pembeda huruf yang mirip adalah titiknya.', 'medium', 'mencocokkan', 'Membandingkan huruf')
    p.perf(3, 'Tunjukkan perbedaan huruf Ba, Ta, dan Tsa di papan tulis dan jelaskan titik-titiknya!', 'Dinilai guru: ketepatan menunjukkan titik dan penjelasan (skala 1-4).', 'Murid membandingkan huruf mirip dengan benar.', 'medium', 'membandingkan', 'Membandingkan huruf')
    p.perf(3, 'Bandingkan bacaan بَ، بِ، بُ dan jelaskan perbedaan fathah, kasrah, dammah!', 'Dinilai guru: ketepatan bunyi dan penjelasan perbedaan (skala 1-4).', 'Murid membandingkan harakat dengan benar.', 'medium', 'membandingkan', 'Membandingkan tanda baca')

    # ================= TP4: merangkaikan huruf bertanda baca =================
    for (parts, lat, arti) in WORDS:
        p.gk = f'w4{lat}'
        full = ''.join(parts); lw = ''.join(lat)
        joined = ' + '.join(parts)
        wrongs = [''.join(x[1]) for x in WORDS if ''.join(x[1]) != lw]
        rng.shuffle(wrongs)
        p.mc(4, f'Rangkaian {joined} dibaca ....', lw, wrongs[:6], f'{joined} = {full}, dibaca {lw}.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
        p.mc(4, f'Rangkaian bunyi "{lw}" ditulis ....', full, [''.join(x[0]) for x in WORDS if ''.join(x[0]) != full][:6], f'{lw} = {full}.', 'hard', 'menerapkan', 'Merangkaikan huruf bertanda baca')
        p.tf(4, f'{joined} dibaca "{lw}".', True, f'Benar, {full} dibaca {lw} (arti: {arti}).', 'easy', 'menerapkan', 'Merangkaikan huruf bertanda baca')
        p.tf(4, f'{joined} dibaca "{wrongs[0]}".', False, f'Salah. {full} dibaca {lw}.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
        p.fill(4, f'{joined} = ....', full, f'Rangkaian itu ditulis {full}.', 'easy', 'menerapkan', 'Merangkaikan huruf bertanda baca')
        if len(parts) >= 2:
            k = rng.randrange(len(parts))
            blank = ' + '.join('....' if t == k else x for t, x in enumerate(parts))
            p.fill(4, f'Lengkapi rangkaian: {blank} = {full}', parts[k], f'Bagian yang hilang adalah {parts[k]}.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca', typ='completion')
        sh = parts[:]
        rng.shuffle(sh)
        while sh == parts and len(parts) > 1:
            rng.shuffle(sh)
        p.order(4, f'Susun suku kata berikut menjadi bacaan "{lw}"!', parts, f'Urutan suku kata: {" + ".join(parts)} = {full}.', 'medium', 'mengurutkan', 'Merangkaikan huruf bertanda baca') if len(parts) >= 3 else None
        p.perf(4, f'Rangkaikan dan bacalah huruf berikut: {joined}', 'Dinilai guru: ketepatan merangkaikan dan melafalkan (skala 1-4).', f'Murid membaca {lw}.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
    for s in range(0, 33, 4):
        sel = WORDS[s:s + 4]
        if len(sel) == 4:
            p.match(4, 'Jodohkan rangkaian huruf dengan bacaannya!', [(' + '.join(w[0]), ''.join(w[1])) for w in sel], 'Setiap rangkaian dibaca sesuai harakatnya.', 'medium', 'mencocokkan', 'Merangkaikan huruf bertanda baca')
    p.ctx(4, 'Rani ingin membaca رَبِّ. Ia membaca huruf Ra berfathah lalu Ba berkasrah bertasydid. Bacaan yang benar adalah ....', 'rabbi', ['rabi', 'ribba', 'rabbu'], 'رَبِّ dibaca rabbi.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
    p.ctx(4, 'Ustazah menulis كَتَبَ di papan. Fahmi diminta membaca per suku kata sebelum merangkaikannya. Urutan bacanya adalah ....', 'ka-ta-ba', ['ba-ta-ka', 'ta-ka-ba', 'ka-ba-ta'], 'Dibaca dari kanan ke kiri: ka, ta, ba.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
    p.perf(4, 'Rangkaikan sendiri tiga huruf berfathah menjadi satu bacaan lalu bacakan di depan guru!', 'Dinilai guru: ketepatan rangkaian dan bacaan (skala 1-4).', 'Murid mampu merangkai huruf bertanda baca.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
    p.perf(4, 'Bacalah rangkaian huruf hijaiah dari buku Iqra atau buku belajar membaca bersama temanmu secara bergantian!', 'Dinilai guru: ketepatan bacaan dan sikap saling menghargai (skala 1-4).', 'Murid membaca rangkaian huruf dengan benar.', 'medium', 'menerapkan', 'Merangkaikan huruf bertanda baca')
    p.ctx(4, 'Salim membaca Al-Qur\'an dengan tenang dan mengikuti tanda bacanya, karena ia ingin mencintai Al-Qur\'an dan ilmu. Sikap Salim menunjukkan cinta ....', 'Allah dan Rasul-Nya serta cinta ilmu', ['permainan saja', 'kendaraan baru', 'uang jajan'], 'Belajar membaca Al-Qur\'an adalah wujud cinta Allah dan Rasul-Nya serta cinta ilmu.', 'easy', 'menerapkan', 'Menerapkan cinta ilmu')
    p.tf(4, 'Belajar huruf hijaiah dengan tekun merupakan wujud cinta Allah dan cinta ilmu.', True, 'Benar, belajar membaca Al-Qur\'an adalah wujud cinta ilmu dan cinta Allah.', 'easy', 'memahami', 'Menerapkan cinta ilmu')
    p.tf(4, 'Mengabaikan tanda baca saat membaca Al-Qur\'an tidak masalah.', False, 'Salah. Tanda baca menentukan bunyi sehingga harus diperhatikan.', 'easy', 'memahami', 'Menerapkan cinta ilmu')
    return p
