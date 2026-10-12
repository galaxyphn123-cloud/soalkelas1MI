# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, mt_gen as g, mt_facts as MF

BABS = [
 dict(code='B1', name='Bab 1. Mengenal Bilangan sampai 10', quota=134, tps=[
   'Murid mampu menghitung, membaca, dan menulis bilangan sampai 10 dengan percaya diri.', 'Murid mampu membandingkan bilangan sampai 10 dengan benar.',
   'Murid mampu mengurutkan bilangan sampai 10 dengan benar.', 'Murid mampu menerapkan pengetahuan tentang bilangan dalam kehidupan sehari-hari sesuai ajaran Islam, seperti untuk berbagi secara adil dan bersedekah.']),
 dict(code='B2', name='Bab 2. Penjumlahan sampai dengan 10', quota=134, tps=[
   'Murid mampu menemukan pasangan bilangan dengan benar.', 'Murid mampu melakukan operasi penjumlahan dengan benar.', 'Murid mampu menyelesaikan soal cerita penjumlahan dengan benar.',
   'Murid mampu menerapkan ilmu tentang penjumlahan dalam kehidupan sehari-hari dengan sikap yang jujur dan mengharapkan rida-Nya.']),
 dict(code='B3', name='Bab 3. Pengurangan sampai dengan 10', quota=133, tps=[
   'Murid mampu mengenal cara melakukan pengurangan.', 'Murid mampu melakukan operasi pengurangan dengan benar.', 'Murid mampu menyelesaikan soal cerita pengurangan dengan benar.',
   'Murid mampu menerapkan operasi hitung pengurangan dalam konteks berbagi sebagai wujud kepedulian terhadap sesama.']),
 dict(code='B4', name='Bab 4. Mengenal Bentuk', quota=100, tps=[
   'Murid mampu mendeskripsikan benda berdasarkan bentuk dengan benar sebagai bagian dari mengamalkan ilmu dengan baik.', 'Murid mampu mengelompokkan benda berdasarkan bentuknya dengan benar.',
   'Murid mampu menyusun dan mengurai bentuk benda dengan sabar dan tekun sebagai bentuk ikhtiar dalam belajar dan mengembangkan potensi yang diberikan Allah Swt.']),
 dict(code='B5', name='Bab 5. Pengukuran Panjang', quota=133, tps=[
   'Murid mampu mengenal alat ukur panjang benda dengan benar.', 'Murid mampu membandingkan panjang benda dengan benar.', 'Murid mampu mengukur panjang benda dengan satuan tidak baku.',
   'Murid mampu menerapkan ilmu tentang pengukuran panjang dengan benar dan bertanggung jawab dalam kehidupan sehari-hari.']),
 dict(code='B6', name='Bab 6. Bilangan sampai dengan 20', quota=133, tps=[
   'Murid mampu menulis, membaca, dan menghitung banyak benda sampai 20 dengan benar sehingga menjadi ilmu yang bermanfaat untuk diri sendiri dan orang lain.',
   'Murid mampu mengenal nilai tempat dengan benar.', 'Murid mampu membandingkan banyak benda sampai 20 dengan benar.', 'Murid mampu mengurutkan bilangan sampai 20 dengan benar.']),
 dict(code='B7', name='Bab 7. Penjumlahan dan Pengurangan sampai dengan 20', quota=133, tps=[
   'Murid mampu mengenal penjumlahan dan pengurangan sampai 20.', 'Murid mampu melakukan penjumlahan sampai 20 dengan benar.', 'Murid mampu melakukan pengurangan sampai 20 dengan benar.',
   'Murid mampu mengamalkan ilmu penjumlahan dan pengurangan dengan jujur dalam kehidupan sehari-hari.']),
 dict(code='B8', name='Bab 8. Data', quota=100, tps=[
   'Murid mampu mengenal berbagai cara dalam menyajikan data.', 'Murid mampu mengelompokkan data dengan benar.',
   'Murid mampu membandingkan dan menyajikan data dalam bentuk diagram turus dan gambar tiga kategori sebagai wujud cinta ilmu dengan benar.']),
]

def handwritten(p):
    n = int(p.code[1])
    for (b, t, stem, ok, bad, expl, diff) in MF.F:
        if b != n: continue
        p.gk = f'hf{n}{t}{stem[:34]}'
        comp = 'Memahami konsep'
        p.mc(t, stem, ok, bad, expl, diff, 'memahami', comp)
        p.tf(t, stem.replace('....', ok), True, expl, 'easy', 'mengingat', comp)
        p.tf(t, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
        p.fill(t, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    for si, (b, t, long, short, ok, bad, expl, diff, vis) in enumerate(MF.S):
        if b != n: continue
        p.gk = f'scx{n}{t}{si}'
        comp = 'Menerapkan konsep dalam kehidupan'
        if vis:
            p.mc(t, long, ok, bad, expl, diff, 'menerapkan', comp, visual=vis); continue
        p.ctx(t, long, ok, bad, expl, diff, 'menerapkan', comp)
        p.tf(t, f'{short} {ok}.', True, expl, 'easy', 'memahami', comp)
        p.tf(t, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', comp)
        p.fill(t, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', comp, typ='completion')
    p.gk = None
    for (b, t, st, truth, e) in MF.T:
        if b == n: p.tf(t, st, truth, e, 'easy', 'memahami', 'Memahami konsep')
    for (b, t, q) in MF.P:
        if b == n: p.perf(t, q, MF.R, 'Murid menunjukkan pemahaman dan keterampilan.', 'medium', 'menerapkan', 'Praktik dan unjuk kerja')
    for (b, t, q, gg, e) in MF.G:
        if b == n: p.group(t, q, gg, e, 'medium', 'mengelompokkan', 'Mengelompokkan')
    for (b, t, q, it, e) in MF.O:
        if b == n: p.order(t, q, it, e, 'medium', 'mengurutkan', 'Mengurutkan')
    for (b, t, q, pr, e) in MF.M:
        if b == n: p.match(t, q, pr, e, 'medium', 'mencocokkan', 'Mencocokkan')

def programmatic(p):
    c = p.code
    if c == 'B1':
        g.count_read(p, 1, 1, 10, 1); g.compare(p, 2, 1, 10, 2); g.order_nums(p, 3, 1, 10, 3); g.share(p, 4, 4)
    elif c == 'B2':
        g.pairs_sum(p, 1, 10, 1); g.add_ops(p, 2, 10, 2); g.stories_add(p, 3, 10, 3)
    elif c == 'B3':
        g.sub_ops(p, 2, 10, 1); g.stories_sub(p, 3, 10, 2); g.share_sub(p, 4, 3)
    elif c == 'B4':
        g.shapes_obj(p, 1, 2, 1)
    elif c == 'B5':
        g.length(p, 2, 3, 1); g.measure_apply(p, 4, 2)
    elif c == 'B6':
        g.count_read(p, 1, 11, 20, 1); g.place_value(p, 2, 2); g.compare(p, 3, 11, 20, 3, 50); g.order_nums(p, 4, 11, 20, 4)
    elif c == 'B7':
        g.sign_fill(p, 1, 20, 1); g.add_ops(p, 2, 20, 2, 60, 11); g.stories_add(p, 2, 20, 3, 14); g.sub_ops(p, 3, 20, 4, 60); g.stories_sub(p, 3, 20, 5, 14); g.jujur20(p, 4, 6)
    elif c == 'B8':
        g.data_gen(p, 1, 2, 3, 1)

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
    recs = lib.finalize(pools(), seed=20261015)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
