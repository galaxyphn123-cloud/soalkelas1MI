# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, pj_gen as g, pj_facts as PF

BABS = [
 dict(code='TB', name='Terampil Bergerak', quota=467, perf=0.10, tps=[
   'Murid mampu mempraktikkan keterampilan gerak lokomotor dan menerapkannya dalam berbagai situasi gerak.',
   'Murid mampu mempraktikkan keterampilan gerak non-lokomotor dan menerapkannya dalam berbagai situasi gerak.',
   'Murid mampu mengeksplorasi berbagai cara menggerakkan tubuh.',
   'Murid mampu memanipulasi objek dengan berbagai bagian tubuh.',
   'Murid mampu mempraktikkan keterampilan gerak fundamental dalam situasi yang lebih kompleks.',
   'Murid mampu mengeksplorasi berbagai metode menggerakkan tubuh dan mengontrol gerakannya.',
   'Murid mampu memanipulasi objek dengan akurasi dan kontrol yang lebih meningkat di berbagai ruang serta mengevaluasi efektivitasnya.']),
 dict(code='BG', name='Belajar melalui Gerak', quota=267, perf=0.10, tps=[
   'Murid mampu mengikuti dan menerapkan peraturan dasar untuk mengembangkan permainan yang fair play dalam berbagai aktivitas fisik.',
   'Murid mampu menerapkan strategi dasar dalam berkolaborasi saat berpartisipasi dalam aktivitas fisik.',
   'Murid mampu menerapkan aturan secara konsisten untuk mengembangkan permainan yang fair play dalam berbagai aktivitas fisik.',
   'Murid mampu menerapkan strategi kolaborasi yang lebih menantang selama aktivitas fisik.']),
 dict(code='HA', name='Bergaya Hidup Aktif', quota=133, perf=0.10, tps=[
   'Murid mampu berpartisipasi dalam berbagai aktivitas fisik dan mengeksplorasi manfaatnya.',
   'Murid mampu berpartisipasi dalam berbagai aktivitas fisik dan memahami manfaatnya.']),
 dict(code='MH', name='Memilih Hidup yang Menyehatkan', quota=133, perf=0.10, tps=[
   'Murid mampu mengenali gaya hidup aktif dan sehat, manfaat makanan bergizi seimbang, serta informasi gizi pada produk makanan yang berdampak pada kesehatan.',
   'Murid mampu mengenali risiko kesehatan dan keselamatan serta strategi untuk mencari bantuan dari orang yang dipercaya.']),
]


HEWAN = [('kelinci', 'melompat-lompat dengan dua kaki'), ('gajah', 'berjalan pelan dengan lengan seperti belalai'), ('burung', 'mengepakkan kedua lengan'),
         ('katak', 'melompat rendah dari posisi jongkok'), ('ular', 'merayap dengan tubuh dekat lantai'), ('kura-kura', 'berjalan sangat pelan'),
         ('kuda', 'berlari kecil dengan lutut diangkat tinggi'), ('ikan', 'menggerakkan badan ke kiri dan kanan seperti berenang')]
EKS = [('tinggi', 'berjinjit dengan lengan lurus ke atas'), ('rendah', 'berjongkok dekat lantai'), ('cepat', 'menggerakkan tubuh dengan kecepatan tinggi'),
       ('lambat', 'menggerakkan tubuh dengan sangat pelan'), ('lurus', 'mengikuti garis lurus'), ('zig-zag', 'berbelok bergantian ke kiri dan ke kanan'),
       ('ke samping', 'menggeser kaki ke arah kanan atau kiri'), ('ke belakang', 'melangkah mundur dengan hati-hati')]
GABUNG = [('berlari sambil menggiring bola', 'lokomotor dan manipulatif'), ('melompat sambil melempar bola', 'lokomotor dan manipulatif'),
          ('berjalan sambil memantulkan bola', 'lokomotor dan manipulatif'), ('berlari lalu melompati rintangan', 'dua gerak lokomotor'),
          ('merayap lalu berdiri dan meregang', 'lokomotor dan non-lokomotor'), ('membungkuk lalu menangkap bola', 'non-lokomotor dan manipulatif'),
          ('berguling lalu berdiri', 'lokomotor dan non-lokomotor'), ('berlari lalu berhenti dan memutar badan', 'lokomotor dan non-lokomotor')]
ABA = [('"mulai"', 'mulai bergerak'), ('"berhenti"', 'berhenti dan diam'), ('"cepat"', 'bergerak dengan cepat'), ('"lambat"', 'bergerak dengan pelan'),
       ('"lompat"', 'melompat'), ('"balik"', 'berbalik arah'), ('"turun"', 'merendahkan tubuh'), ('"naik"', 'berjinjit')]
SASARAN = [('lemparan ke ember', 'melihat ember dan mengatur tenaga'), ('tendangan ke gawang', 'mengarahkan kaki ke gawang'), ('lemparan ke dinding', 'melihat titik sasaran di dinding'),
           ('pantulan bola', 'mengatur tenaga pantulan'), ('tangkapan bola', 'mengikuti bola dengan mata'), ('menggiring bola', 'menjaga bola tetap dekat kaki'),
           ('pukulan bola dengan raket', 'mengayunkan raket tepat ke bola'), ('operan ke teman', 'mengarahkan operan ke teman')]

def hasil(p):
    for n in range(1, 10):
        p.gk = f'hs{n}'
        comp = 'Mengevaluasi hasil gerak'
        p.mc(7, f'Dari 10 lemparan ke ember, {n} lemparan masuk. Lemparan yang tidak masuk ada ....', str(10 - n), [str(x) for x in range(0, 11) if x != 10 - n and abs(x - (10 - n)) <= 3][:5], f'10 - {n} = {10 - n}.', 'medium', 'mengevaluasi', comp)
        p.fill(7, f'Isilah: Dari 10 lemparan ke ember, {n} lemparan masuk. Lemparan yang tidak masuk ada ....', str(10 - n), f'10 - {n} = {10 - n}.', 'medium', 'mengevaluasi', comp)
        p.tf(7, f'Dari 10 lemparan ke ember, {n} masuk. Berarti {10 - n} lemparan tidak masuk.', True, f'10 - {n} = {10 - n}.', 'easy', 'mengevaluasi', comp)
        p.tf(7, f'Dari 10 lemparan ke ember, {n} masuk. Berarti {10 - n + 1 if n < 9 else 0} lemparan tidak masuk.', False, f'Yang benar {10 - n}.', 'medium', 'mengevaluasi', comp)
        if n in (3, 6): p.ctx(7, f'Rafi melempar bola ke ember 10 kali dan {n} kali masuk. Agar hasilnya lebih baik, Rafi sebaiknya ....', 'berlatih lagi dan memperbaiki arah lemparan', ['berhenti berlatih', 'marah pada bola', 'menyalahkan teman'], 'Evaluasi lalu perbaiki.', 'medium', 'mengevaluasi', comp)
    p.gk = None

def mix(perf):
    return [('multiple_choice', 0.30), ('multiple_choice_visual', 0.05), ('contextual', 0.08), ('true_false', 0.20),
            ('fill_in_short', 0.08), ('completion', 0.04), ('matching', 0.03), ('ordering', 0.02), ('grouping', 0.03),
            ('performance_task', perf)]

def handwritten(p):
    e = p.code
    for (b, t, stem, ok, bad, expl, diff) in PF.F:
        if b != e: continue
        p.gk = f'hf{e}{t}{stem[:34]}'
        comp = 'Memahami konsep'
        p.mc(t, stem, ok, bad, expl, diff, 'memahami', comp)
        p.tf(t, stem.replace('....', ok), True, expl, 'easy', 'mengingat', comp)
        p.tf(t, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
        p.fill(t, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    for si, (b, t, long, short, ok, bad, expl, diff, vis) in enumerate(PF.S):
        if b != e: continue
        p.gk = f'scx{e}{t}{si}'
        comp = 'Menerapkan sikap dan gerak dalam kehidupan'
        if vis:
            p.mc(t, long, ok, bad, expl, diff, 'menerapkan', comp, visual=vis); continue
        p.ctx(t, long, ok, bad, expl, diff, 'menerapkan', comp)
        p.tf(t, f'{short} {ok}.', True, expl, 'easy', 'memahami', comp)
        p.tf(t, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', comp)
        p.fill(t, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', comp, typ='completion')
    p.gk = None
    for (b, t, st, truth, ex) in PF.T:
        if b == e: p.tf(t, st, truth, ex, 'easy', 'memahami', 'Memahami konsep')
    for (b, t, q) in PF.P:
        if b == e: p.perf(t, q, PF.R, 'Murid menunjukkan gerak yang tepat, sikap sportif, dan menjaga keselamatan.', 'medium', 'menerapkan', 'Praktik dan unjuk kerja')
    for (b, t, q, gg, ex) in PF.G:
        if b == e: p.group(t, q, gg, ex, 'medium', 'mengelompokkan', 'Mengelompokkan')
    for (b, t, q, it, ex) in PF.O:
        if b == e: p.order(t, q, it, ex, 'medium', 'mengurutkan', 'Mengurutkan')
    for (b, t, q, pr, ex) in PF.M:
        if b == e: p.match(t, q, pr, ex, 'medium', 'mencocokkan', 'Mencocokkan')

def perfs(p, tp, rows, tpl, comp='Praktik dan unjuk kerja'):
    for k, *_ in rows:
        p.perf(tp, tpl.format(k=k), PF.R, 'Murid menunjukkan gerak yang tepat, sikap sportif, dan menjaga keselamatan.', 'medium', 'menerapkan', comp)

def programmatic(p):
    c = p.code
    if c == 'TB':
        g.kv(p, 1, PF.LOKO, 'Ciri gerak {k} adalah {v}.', 'Gerak yang dilakukan dengan cara {v} adalah ....', 'Mengenal gerak lokomotor', 'lk', 1)
        g.kv(p, 2, PF.NONLOKO, 'Ciri gerak {k} adalah {v}.', 'Gerak yang berarti {v} adalah ....', 'Mengenal gerak non-lokomotor', 'nl', 2)
        g.kv(p, 4, PF.MANIP, 'Pada gerakan {k}, bagian tubuh yang dipakai adalah {v}.', None, 'Memanipulasi objek', 'mp', 3)
        g.kv(p, 3, HEWAN, 'Saat menirukan {k}, gerak yang dilakukan adalah {v}.', 'Gerak {v} dilakukan saat menirukan ....', 'Mengeksplorasi gerak', 'hw', 4)
        g.kv(p, 3, EKS, 'Bergerak {k} berarti {v}.', 'Gerak yang berarti {v} adalah bergerak ....', 'Mengeksplorasi gerak', 'ek', 5)
        g.kv(p, 5, GABUNG, 'Gerakan {k} menggabungkan gerak {v}.', None, 'Menggabungkan gerak fundamental', 'gb', 6)
        g.kv(p, 6, ABA, 'Saat guru berkata {k}, murid harus {v}.', 'Murid harus {v} saat guru berkata ....', 'Mengontrol gerakan', 'ab', 7)
        g.kv(p, 7, SASARAN, 'Agar {k} tepat, kita perlu {v}.', None, 'Memanipulasi objek dengan akurat', 'sr', 8)
        hasil(p)
        perfs(p, 1, PF.LOKO, 'Peragakan gerak {k} dengan benar dan aman!')
        perfs(p, 2, PF.NONLOKO, 'Peragakan gerak {k} dengan benar dan aman!')
        perfs(p, 4, PF.MANIP, 'Peragakan gerakan {k} dengan benar dan aman!')
        perfs(p, 3, PF.LOKO, 'Tunjukkan dua cara berbeda untuk {k}!')
        perfs(p, 6, PF.NONLOKO, 'Lakukan {k} dengan terkontrol sambil menjaga keseimbangan!')
        perfs(p, 7, PF.MANIP, 'Lakukan {k} dengan tepat sasaran lalu nilai hasilmu!')
        perfs(p, 5, PF.MANIP, 'Gabungkan berlari dengan {k}!')
    elif c == 'BG':
        g.rules(p, 1, 1, None, PF.FAIR, 'Memahami manfaat aturan bermain', 'Menaati aturan bermain', '', 'aturan bermain', 1)
        g.rules(p, 2, 2, 2, PF.KOLAB, 'Memahami manfaat kerja sama', 'Menerapkan kerja sama', 'Menerapkan kerja sama dalam tim', 'kerja sama tim', 2,
                ctx_tpl='Dalam permainan beregu, tim {nm} menghadapi "{a}" ({noun}). Yang dilakukan {nm} adalah ....')
        g.rules(p, None, 3, 3, PF.FAIR, '', 'Menaati aturan secara konsisten', 'Menerapkan aturan secara konsisten', 'aturan yang disepakati', 3,
                ctx_tpl='Saat bermain, {nm} bertemu {noun} "{a}". Walaupun tidak diawasi guru, {nm} ingin tetap konsisten. Yang dilakukan {nm} adalah ....')
        g.rules(p, None, 4, 4, PF.KOLAB, '', 'Menyusun strategi kolaborasi menantang', 'Menerapkan kolaborasi menantang', 'strategi tim', 4,
                ctx_tpl='Dalam permainan yang menantang, tim {nm} menghadapi "{a}" ({noun}). Yang dilakukan {nm} adalah ....')
        perfs(p, 1, PF.FAIR, 'Peragakan sikap {k} saat bermain!')
        perfs(p, 3, PF.FAIR, 'Tunjukkan cara {k} sampai permainan selesai!')
        perfs(p, 2, PF.KOLAB, 'Peragakan kerja sama dalam {k}!')
        perfs(p, 4, PF.KOLAB, 'Praktikkan {k} bersama timmu dalam permainan yang menantang!')
    elif c == 'HA':
        g.kv(p, 2, PF.MANFAAT, 'Manfaat {k} adalah {v}.', 'Kegiatan yang membuat {v} adalah ....', 'Memahami manfaat aktivitas fisik', 'mf', 1)
        g.kv(p, 1, PF.MANFAAT, 'Dengan {k}, kita berpartisipasi dalam aktivitas fisik agar {v}.', 'Agar {v}, kita berpartisipasi dalam kegiatan ....', 'Berpartisipasi dalam aktivitas fisik', 'pt', 2)
        perfs(p, 1, PF.MANFAAT, 'Lakukan kegiatan {k} bersama teman dengan semangat!')
        perfs(p, 2, PF.MANFAAT, 'Ceritakan manfaat {k} yang kamu rasakan!')
    elif c == 'MH':
        g.kv(p, 1, PF.GIZI, 'Makanan {k} termasuk {v}.', 'Makanan yang termasuk sumber kalsium adalah ....', 'Mengenal makanan bergizi', 'gz', 1, rev_ok=['susu'])
        g.kv(p, 2, PF.BAHAYA, 'Jika bertemu {k}, tindakan yang tepat adalah {v}.', 'Tindakan "{v}" tepat dilakukan jika bertemu ....', 'Mengenali risiko dan mencari bantuan', 'bh', 2)
        perfs(p, 1, PF.GIZI, 'Sebutkan manfaat memakan {k} dan golongan makanannya!')
        perfs(p, 2, PF.BAHAYA, 'Peragakan tindakan yang tepat saat bertemu {k}!')

def pools():
    out = []
    for B in BABS:
        p = lib.Pool(B['code'], B['name'], B['tps'], B['quota'], mix=mix(B['perf']))
        p.cap = 4
        handwritten(p); programmatic(p)
        out.append(p)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'dry':
        for p in pools():
            print(p.code, len(p.items), p.quota, dict(sorted(collections.Counter(x['tp'] for x in p.items).items())), dict(collections.Counter(x['type'] for x in p.items)))
        sys.exit()
    recs = lib.finalize(pools(), seed=20261017)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
