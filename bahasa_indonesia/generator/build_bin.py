# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, bi_gen, bi_facts as BF

BABS = [
 dict(code='B1', name='Bab 1. Aku Ciptaan Allah Swt. yang Sempurna', quota=111, tps=[
   'Murid mampu memahami cara membaca dan menulis dengan benar.', 'Murid mampu mengenal huruf vokal dan konsonan dengan benar.',
   'Murid mampu membaca dan menulis kata yang berawalan huruf a, h, k, m, r, dan t dengan benar.',
   'Murid mampu menggunakan anggota tubuh ciptaan Allah Swt. untuk belajar membaca dan menulis dengan sungguh-sungguh sebagai wujud syukur kepada-Nya.']),
 dict(code='B2', name='Bab 2. Badanku Sehat dan Kuat', quota=139, tps=[
   'Murid mampu menyimak cerita yang dibacakan dengan benar.', 'Murid mampu menceritakan kembali cerita yang dibacakan dengan benar.',
   'Murid mampu mengenal penggunaan tanda tanya dan tanda seru dengan benar.', 'Murid mampu membaca dan menulis kata yang diawali huruf c, i, p, dan s dengan benar.',
   'Murid mampu menerapkan ilmu yang dipelajari dengan sungguh-sungguh sebagai wujud rasa syukur kepada Allah Swt.']),
 dict(code='B3', name='Bab 3. Keluargaku Sakinah', quota=139, tps=[
   'Murid mampu menyimak cerita yang dibacakan dengan saksama.', 'Murid mampu melengkapi kalimat rumpang dengan benar.',
   'Murid mampu membaca dan menulis kata yang berawalan huruf b, g, l, n, dan o dengan benar.', 'Murid mampu menceritakan kembali gambar yang diamati menggunakan kalimat sendiri dengan kreatif.',
   'Murid mampu menunjukkan sikap belajar dengan sungguh-sungguh dalam kegiatan menyimak, membaca, dan menulis sebagai wujud menghargai ilmu yang telah diajarkan.']),
 dict(code='B4', name='Bab 4. Kebersihan Sebagian dari Iman', quota=111, tps=[
   'Murid mampu meniru berbagai gerakan yang dilakukan oleh tokoh dalam cerita dengan benar sebagai bentuk kreativitas dan ekspresi diri.',
   'Murid mampu membaca dan menulis kata yang berawalan huruf d, e, f, j, dan u dengan benar.',
   'Murid mampu menceritakan kembali isi teks yang telah dibaca menggunakan bahasa sendiri secara runtut dan benar.',
   'Murid mampu menunjukkan sikap percaya diri dan semangat dalam menuntut ilmu sesuai dengan ajaran Islam.']),
 dict(code='B5', name='Bab 5. Asyiknya Bermain', quota=139, tps=[
   'Murid mampu mengenal tanda titik pada akhir kalimat dengan benar.', 'Murid mampu menggunakan tanda titik pada akhir kalimat dengan benar.',
   'Murid mampu membaca dan menulis kata yang berawalan huruf q, v, w, x, y, dan z dengan benar.', 'Murid mampu mengenal ungkapan permisi, tolong, maaf, dan terima kasih dengan benar.',
   'Murid mampu menggunakan ungkapan permisi, tolong, maaf, dan terima kasih dalam kehidupan sehari-hari dengan tepat sesuai kondisi sebagai wujud mengamalkan adab sesuai ajaran Islam.']),
 dict(code='B6', name='Bab 6. Rumahku Surgaku', quota=111, tps=[
   'Murid mampu menyimak cerita yang dibacakan dengan benar.', 'Murid mampu menceritakan kembali cerita yang didengar dengan benar.',
   'Murid mampu menulis dan menyebutkan bilangan satu sampai sepuluh dengan benar.',
   'Murid mampu menerapkan ilmu tentang bilangan dan menyimak cerita yang telah dipelajari dalam kehidupan sehari-hari sebagai bentuk mencintai ilmu.']),
 dict(code='B7', name='Bab 7. Sekolahku Menyenangkan', quota=139, tps=[
   'Murid mampu menceritakan kembali isi cerita yang dibaca dengan sederhana dan runtut.', 'Murid mampu menulis arti kata baru yang ditemukan dengan baik.',
   'Murid mampu menemukan arti kata baru dengan bantuan guru, orang tua, atau kamus secara tepat.', 'Murid mampu bercerita sesuai ide atau gagasan yang dimiliki dengan percaya diri.',
   'Murid mampu memperhatikan adab ketika bercerita sesuai ajaran Islam.']),
 dict(code='B8', name='Bab 8. Lingkungan Sekitarku', quota=111, tps=[
   'Murid mampu membaca kata-kata sederhana tentang arah dan letak serta pekerjaan dengan benar.', 'Murid mampu menulis kata-kata sederhana tentang arah dan letak serta pekerjaan dengan benar.',
   'Murid mampu menceritakan letak suatu benda atau arah suatu tempat dengan baik dan benar agar dapat membantu orang lain.',
   'Murid mampu menerapkan sikap sungguh-sungguh dalam belajar dan mengenal profesi di lingkungan sekitar sebagai wujud mencintai ilmu agar cita-cita di masa depan tercapai.']),
]

def handwritten(p, bab):
    n = int(p.code[1])
    for (b, t, stem, ok, bad, expl, diff) in BF.F:
        if b != n: continue
        p.gk = f'hf{n}{t}{stem[:30]}'
        comp = p.tps[t - 1][14:70]
        cog = 'memahami'
        p.mc(t, stem, ok, bad, expl, diff, cog, comp)
        p.tf(t, stem.replace('....', ok), True, expl, 'easy', 'mengingat', comp)
        p.tf(t, stem.replace('....', bad[0]), False, f'Salah. {expl}', 'medium', 'mengingat', comp)
        p.fill(t, 'Isilah titik-titik berikut: ' + stem, ok, expl, diff, 'mengingat', comp)
    for si, (b, t, long, short, ok, bad, expl, diff, vis) in enumerate(BF.S):
        if b != n: continue
        p.gk = f'scx{n}{t}{si}'
        comp = 'Menerapkan sikap dan ilmu'
        if vis:
            p.mc(t, long, ok, bad, expl, diff, 'menerapkan', comp, visual=vis)
            continue
        p.ctx(t, long, ok, bad, expl, diff, 'menerapkan', comp)
        p.tf(t, f'{short} {ok}.', True, expl, 'easy', 'memahami', comp)
        p.tf(t, f'{short} {bad[0]}.', False, f'Salah. {expl}', 'medium', 'memahami', comp)
        p.fill(t, f'Lengkapi: {short} ....', ok, expl, diff, 'menerapkan', comp, typ='completion')
    p.gk = None
    for (b, t, st, truth, expl) in BF.T:
        if b == n: p.tf(t, st, truth, expl, 'easy', 'memahami', 'Memahami materi')
    for (b, t, q) in BF.P:
        if b == n: p.perf(t, q, BF.R, 'Murid menunjukkan pemahaman dan keterampilan.', 'medium', 'menerapkan', 'Praktik dan unjuk kerja')
    for (b, t, q, g, e) in BF.G:
        if b == n: p.group(t, q, g, e, 'medium', 'mengelompokkan', 'Mengelompokkan')
    for (b, t, q, it, e) in BF.O:
        if b == n: p.order(t, q, it, e, 'medium', 'mengurutkan', 'Mengurutkan')
    for (b, t, q, pr, e) in BF.M:
        if b == n: p.match(t, q, pr, e, 'medium', 'mencocokkan', 'Mencocokkan')

def programmatic(p):
    g = bi_gen
    c = p.code
    if c == 'B1':
        g.letter_words(p, 'ahkmrt', 3, 1); g.vowels(p, 2)
    elif c == 'B2':
        g.stories(p, 'dani', 1, 2); g.stories(p, 'sinta', 1, 2); g.punct(p, 3, None); g.letter_words(p, 'cips', 4, 2)
    elif c == 'B3':
        g.stories(p, 'keluarga', 1, 4); g.stories(p, 'lani', 1, 4); g.rumpang(p, 2); g.letter_words(p, 'bglno', 3, 3)
    elif c == 'B4':
        g.stories(p, 'bimo', 3, 3); g.stories(p, 'raka', 3, 3); g.stories(p, 'hewan', 1, 1); g.letter_words(p, 'defju', 2, 4)
    elif c == 'B5':
        g.stories(p, 'tia', 5, 5); g.punct_know(p, 1); g.punct(p, None, 2)
        g.letter_words(p, 'qvwxyz', 3, 5); g.ungkapan(p, 4, 5)
    elif c == 'B6':
        g.stories(p, 'rumah', 1, 2); g.stories(p, 'ikan', 1, 2); g.bilangan(p, 3)
    elif c == 'B7':
        g.stories(p, 'salma', 1, 1); g.stories(p, 'kata', 3, 1); g.arti_kata(p, 2)
    elif c == 'B8':
        g.stories(p, 'pos', 1, 3); g.stories(p, 'pasar', 1, 3); g.letak(p, 1, 3, 2)

def pools():
    out = []
    for i, B in enumerate(BABS):
        p = lib.Pool(B['code'], B['name'], B['tps'], B['quota'])
        p.cap = 4
        handwritten(p, B)
        programmatic(p)
        out.append(p)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'dry':
        for p in pools():
            print(p.code, len(p.items), dict(sorted(collections.Counter(x['tp'] for x in p.items).items())), dict(collections.Counter(x['type'] for x in p.items)))
        sys.exit()
    recs = lib.finalize(pools(), seed=20261014)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
