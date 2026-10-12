# -*- coding: utf-8 -*-
import sys, json, collections, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, pn_gen as g, pn_facts as PF

EX = ['Papua', 'Kalimantan', 'Aceh', 'Nusa Tenggara Barat', 'Sulawesi Selatan']

BABS = [
 dict(code='B1', name='Bab 1. Tentang Diriku', quota=214, tps=[
   'Murid mampu memahami keberagaman identitas di lingkungan rumah, sekolah, dan masyarakat dengan benar.',
   'Murid mampu mengidentifikasi berbagai bentuk keberagaman suku bangsa, budaya, dan agama di lingkungan rumah, sekolah, dan masyarakat dengan benar.',
   'Murid mampu melaksanakan sikap menghargai keberagaman identitas dengan penuh cinta dan toleransi dalam kehidupan sehari-hari.']),
 dict(code='B2', name='Bab 2. Menaati Aturan', quota=214, tps=[
   'Murid mampu memahami pentingnya aturan di lingkungan keluarga dengan benar.', 'Murid mampu menguraikan perilaku menaati dan tidak menaati aturan di lingkungan keluarga dengan benar.',
   'Murid mampu menerapkan perilaku menaati aturan di lingkungan keluarga dengan benar dalam kehidupan sehari-hari sebagai wujud mengamalkan ajaran Islam untuk kebaikan bersama.']),
 dict(code='B3', name='Bab 3. Negaraku Indonesia', quota=286, tps=[
   'Murid mampu memahami simbol dan sila Pancasila pada lambang negara dengan benar.', 'Murid mampu menguraikan makna penting sila-sila Pancasila sebagai dasar negara dengan benar.',
   'Murid mampu memahami nilai-nilai Pancasila di lingkungan keluarga dengan benar.', 'Murid mampu melaksanakan nilai-nilai Pancasila dengan benar dalam kehidupan sehari-hari sebagai wujud cinta tanah air.']),
 dict(code='B4', name='Bab 4. Menjaga Lingkunganku', quota=286, tps=[
   'Murid mampu mengenal karakteristik lingkungan rumah dengan benar.', 'Murid mampu memahami bentuk kerja sama di lingkungan rumah dengan benar.',
   'Murid mampu menguraikan perilaku menjaga lingkungan rumah dengan benar.', 'Murid mampu melaksanakan kerja sama dalam menjaga lingkungan rumah dengan penuh kepedulian dan kebersamaan dalam kehidupan sehari-hari.']),
]

def handwritten(p):
    n = int(p.code[1])
    for (b, t, stem, ok, bad, expl, diff) in PF.F:
        if b != n: continue
        p.gk = f'hf{n}{t}{stem[:34]}'
        comp = 'Memahami konsep'
        p.mc(t, stem, ok, bad, expl, diff, 'memahami', comp)
        p.tf(t, stem.replace('....', ok), True, expl, 'easy', 'mengingat', comp)
        p.tf(t, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
        p.fill(t, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    for si, (b, t, long, short, ok, bad, expl, diff, vis) in enumerate(PF.S):
        if b != n: continue
        p.gk = f'scx{n}{t}{si}'
        comp = 'Menerapkan sikap dalam kehidupan'
        if vis:
            p.mc(t, long, ok, bad, expl, diff, 'menerapkan', comp, visual=vis); continue
        p.ctx(t, long, ok, bad, expl, diff, 'menerapkan', comp)
        p.tf(t, f'{short} {ok}.', True, expl, 'easy', 'memahami', comp)
        p.tf(t, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', comp)
        p.fill(t, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', comp, typ='completion')
    p.gk = None
    for (b, t, st, truth, e) in PF.T:
        if b == n: p.tf(t, st, truth, e, 'easy', 'memahami', 'Memahami konsep')
    for (b, t, q) in PF.P:
        if b == n: p.perf(t, q, PF.R, 'Murid menunjukkan pemahaman dan sikap.', 'medium', 'menerapkan', 'Praktik dan unjuk kerja')
    for (b, t, q, gg, e) in PF.G:
        if b == n: p.group(t, q, gg, e, 'medium', 'mengelompokkan', 'Mengelompokkan')
    for (b, t, q, it, e) in PF.O:
        if b == n: p.order(t, q, it, e, 'medium', 'mengurutkan', 'Mengurutkan')
    for (b, t, q, pr, e) in PF.M:
        if b == n: p.match(t, q, pr, e, 'medium', 'mencocokkan', 'Mencocokkan')

def sila_contoh(p, tp):
    comp = 'Mengenal nilai Pancasila di keluarga'
    rng = random.Random(3)
    for i, (n, c) in enumerate(PF.SILA_CONTOH):
        p.gk = f'sc{i}'
        p.mc(tp, f'Sikap "{c}" di dalam keluarga sesuai dengan sila ke- ....', str(n), [str(x) for x in range(1, 6) if x != n], f'"{c}" mengamalkan sila ke-{n}.', 'medium', 'menerapkan', comp)
        p.tf(tp, f'Sikap "{c}" sesuai dengan sila ke-{n}.', True, f'Sila ke-{n}.', 'easy', 'menerapkan', comp)
        p.tf(tp, f'Sikap "{c}" sesuai dengan sila ke-{(n % 5) + 1}.', False, f'Yang benar sila ke-{n}.', 'medium', 'menerapkan', comp)
        p.fill(tp, f'Isilah: Sikap "{c}" sesuai dengan sila ke- ....', str(n), f'Sila ke-{n}.', 'medium', 'menerapkan', comp)
    p.gk = None
    p.group(tp, 'Kelompokkan sikap berikut menurut silanya: salat berjemaah; saling menyayangi; bermusyawarah; berbagi adil; bekerja sama.',
            {'sila 1': ['salat berjemaah'], 'sila 2': ['saling menyayangi'], 'sila 3': ['bekerja sama'], 'sila 4': ['bermusyawarah'], 'sila 5': ['berbagi adil']}, 'Kelompokkan sikap menurut sila.', 'medium', 'mengelompokkan', comp)

def programmatic(p):
    c = p.code
    if c == 'B1':
        g.kv(p, 1, PF.HOBI, 'Orang yang hobi {k} memerlukan {v}.', None, 'Memahami keberagaman identitas', 'hb', 1)
        g.kv(p, 2, PF.RUMAH_ADAT, 'Rumah adat {k} berasal dari daerah {v}.', 'Rumah adat dari daerah {v} adalah {k}.', 'Mengidentifikasi keberagaman budaya', 'ra', 2)
        g.kv(p, 2, PF.TARI, 'Tari {k} berasal dari daerah {v}.', 'Tarian dari daerah {v} adalah tari {k}.', 'Mengidentifikasi keberagaman budaya', 'tr', 3, extra_wrong=EX)
        g.kv(p, 2, PF.MUSIK, 'Alat musik {k} berasal dari {v}.', 'Alat musik dari {v} adalah {k}.', 'Mengidentifikasi keberagaman budaya', 'ms', 4, extra_wrong=EX, extra_keys=['biola', 'piano', 'drum'])
        g.kv(p, 2, PF.MAKAN, 'Makanan khas {k} berasal dari {v}.', 'Makanan khas dari {v} adalah {k}.', 'Mengidentifikasi keberagaman budaya', 'mk', 5, extra_wrong=EX, extra_keys=['pizza', 'sushi', 'hamburger'])
        g.kv(p, 2, PF.TERIMA, 'Ucapan terima kasih "{k}" berasal dari suku {v}.', 'Ucapan terima kasih dalam bahasa {v} adalah "{k}".', 'Mengidentifikasi keberagaman bahasa', 'tk', 6)
        ag = [(a, t) for a, t, k, h in PF.AGAMA]
        g.kv(p, 2, ag, 'Tempat ibadah agama {k} adalah {v}.', None, 'Mengidentifikasi keberagaman agama', 'ag1', 7)
        g.kv(p, 2, [(a, k) for a, t, k, h in PF.AGAMA], 'Kitab suci agama {k} adalah {v}.', None, 'Mengidentifikasi keberagaman agama', 'ag2', 8)
        g.kv(p, 2, [(a, h) for a, t, k, h in PF.AGAMA], 'Salah satu hari raya agama {k} adalah {v}.', None, 'Mengidentifikasi keberagaman agama', 'ag3', 9)
        g.kv(p, 2, [(t, a) for a, t, k, h in PF.AGAMA if a != 'Kristen'], '{k} adalah tempat ibadah agama {v}.', None, 'Mengidentifikasi keberagaman agama', 'ag4', 10)
    elif c == 'B2':
        g.rules(p, 1, 2, 3, PF.ATURAN, 'Memahami pentingnya aturan', 'Menguraikan perilaku menaati aturan', 'Menerapkan perilaku menaati aturan', 'aturan', 1)
    elif c == 'B3':
        g.kv(p, 1, PF.SILA_LAMBANG, 'Lambang sila ke-{k} pada Garuda Pancasila adalah {v}.', '{v} adalah lambang sila ke-{k}.', 'Memahami simbol dan sila Pancasila', 'sl', 1)
        g.kv(p, 1, PF.SILA_BUNYI, 'Sila ke-{k} Pancasila berbunyi "{v}".', 'Sila berbunyi "{v}" adalah sila ke-{k}.', 'Memahami bunyi sila Pancasila', 'sb', 2)
        g.kv(p, 2, PF.SILA_MAKNA, 'Sila ke-{k} mengajarkan kita untuk {v}.', 'Ajaran untuk {v} terdapat pada sila ke-{k}.', 'Menguraikan makna sila Pancasila', 'sm', 3)
        sila_contoh(p, 3)
    elif c == 'B4':
        g.kv(p, 1, PF.BAGIAN, 'Fungsi {k} di lingkungan rumah adalah {v}.', None, 'Mengenal karakteristik lingkungan rumah', 'bg', 1)
        g.kv(p, 2, PF.GOTONG, 'Manfaat {k} adalah {v}.', None, 'Memahami bentuk kerja sama', 'gt', 2)
        g.rules(p, None, 3, None, PF.LINGK_RULES, '', 'Menguraikan perilaku menjaga lingkungan', '', 'kebiasaan menjaga lingkungan', 3)
        g.rules(p, 3, None, None, PF.LINGK_RULES, 'Memahami manfaat menjaga lingkungan', '', '', 'kebiasaan menjaga lingkungan', 4) if False else None
        g.rules(p, 2, None, 4, PF.KERJASAMA, 'Memahami bentuk kerja sama', '', 'Melaksanakan kerja sama menjaga lingkungan', 'kegiatan', 5)

def pools():
    out = []
    for B in BABS:
        p = lib.Pool(B['code'], B['name'], B['tps'], B['quota'])
        p.cap = 4
        handwritten(p); programmatic(p)
        out.append(p)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'dry':
        for p in pools():
            print(p.code, len(p.items), dict(sorted(collections.Counter(x['tp'] for x in p.items).items())), dict(collections.Counter(x['type'] for x in p.items)))
        sys.exit()
    recs = lib.finalize(pools(), seed=20261016)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
