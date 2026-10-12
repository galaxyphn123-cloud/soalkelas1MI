# -*- coding: utf-8 -*-
"""Tabel dan fakta PJOK Kelas 1. Kunci: (elemen, nomor TP/ATP dalam elemen)."""
R = 'Dinilai guru: ketepatan gerak, kesungguhan, sikap sportif, dan keselamatan (skala 1-4).'
F, S, T, P, G, O, M = [], [], [], [], [], [], []
def f(e, t, stem, ok, bad, expl='', diff='easy'): F.append((e, t, stem, ok, bad, expl or f'Jawaban: {ok}.', diff))
def s(e, t, long, short, ok, bad, expl, diff='medium', vis=None): S.append((e, t, long, short, ok, bad, expl, diff, vis))
def perf(e, t, *qs):
    for q in qs: P.append((e, t, q))

# ---------------------------------------------------------------- tabel
LOKO = [('berjalan', 'melangkahkan kaki bergantian dan salah satu kaki selalu menyentuh tanah'), ('berlari', 'bergerak cepat dan ada saat kedua kaki melayang'),
        ('melompat', 'bertumpu pada satu kaki dan mendarat pada kaki yang sama'), ('meloncat', 'bertumpu pada dua kaki dan mendarat pada dua kaki'),
        ('berjingkat', 'berjalan dengan bertumpu pada ujung jari kaki'), ('merayap', 'bergerak dengan tubuh dekat lantai'), ('berguling', 'memutar badan ke samping di atas matras')]
NONLOKO = [('membungkuk', 'menekuk badan ke depan di tempat'), ('meregang', 'menarik tubuh atau anggota tubuh selurus mungkin'), ('memutar', 'menggerakkan badan atau kepala berputar di tempat'),
           ('mengayun', 'menggerakkan lengan atau kaki ke depan dan ke belakang di tempat'), ('mendorong', 'menekan benda menjauhi badan'), ('menarik', 'membawa benda mendekati badan'),
           ('menekuk', 'melipat sendi seperti lutut atau siku'), ('berdiri satu kaki', 'menjaga keseimbangan tubuh di atas satu kaki')]
MANIP = [('melempar bola', 'tangan'), ('menangkap bola', 'kedua tangan'), ('menendang bola', 'kaki'), ('memantulkan bola', 'telapak tangan'), ('menggiring bola dengan kaki', 'kaki'),
         ('memukul bola dengan raket', 'tangan yang memegang raket'), ('menyundul bola', 'kepala'), ('menahan bola dengan dada', 'dada')]
GIZI = [('nasi', 'sumber karbohidrat'), ('kentang', 'sumber karbohidrat'), ('ikan', 'sumber protein'), ('tahu', 'sumber protein'), ('telur', 'sumber protein'), ('bayam', 'sayuran'),
        ('wortel', 'sayuran'), ('pisang', 'buah-buahan'), ('jeruk', 'buah-buahan'), ('susu', 'sumber kalsium')]
MANFAAT = [('berolahraga', 'badan menjadi kuat'), ('berjalan kaki ke sekolah', 'badan menjadi bugar'), ('bermain di luar rumah', 'hati menjadi gembira'), ('bersepeda', 'otot kaki menjadi kuat'),
           ('berenang', 'seluruh tubuh bergerak sehat'), ('senam pagi', 'tubuh menjadi segar'), ('melompat tali', 'kaki dan jantung menjadi kuat'), ('bermain bersama teman', 'kita belajar bekerja sama')]
BAHAYA = [('kabel listrik yang terkelupas', 'menjauh dan memberi tahu orang dewasa'), ('api kompor yang menyala', 'menjauh dan memanggil orang tua'), ('pisau yang tajam', 'tidak menyentuh dan memberi tahu orang dewasa'),
          ('jalan raya yang ramai', 'menyeberang bersama orang dewasa di tempat aman'), ('kolam yang dalam', 'tidak mendekat tanpa orang dewasa'), ('obat-obatan di meja', 'tidak meminumnya dan memberi tahu orang tua'),
          ('makanan yang sudah basi', 'tidak memakannya dan memberi tahu orang tua'), ('orang asing yang mengajak pergi', 'menolak dan segera mencari guru atau orang tua'),
          ('lantai yang licin', 'berjalan pelan dan berhati-hati'), ('tangga yang tinggi', 'berpegangan dan turun pelan-pelan')]
# (aturan, taat, tidak, manfaat)
FAIR = [
 ('bermain sesuai aturan', 'mengikuti aturan permainan', 'mengubah aturan seenaknya', 'permainan menjadi adil'),
 ('menunggu giliran', 'menunggu giliran dengan sabar', 'menyerobot giliran teman', 'semua mendapat kesempatan'),
 ('jujur saat bermain', 'mengaku jika melakukan kesalahan', 'pura-pura tidak tahu saat salah', 'permainan dapat dipercaya'),
 ('menerima kekalahan', 'memberi selamat kepada pemenang', 'marah dan menangis', 'pertemanan tetap terjaga'),
 ('menerima kemenangan dengan rendah hati', 'tidak menyombongkan diri', 'mengejek lawan', 'lawan tidak sakit hati'),
 ('menghormati keputusan guru atau wasit', 'menerima keputusan wasit', 'membantah keputusan wasit', 'permainan berjalan lancar'),
 ('tidak berbuat kasar', 'bermain tanpa mendorong atau memukul', 'mendorong teman', 'tidak ada yang cedera'),
 ('bermain di tempat yang aman', 'bermain di lapangan', 'bermain di jalan raya', 'terhindar dari bahaya'),
 ('mengajak semua teman bermain', 'mengajak teman yang berbeda bermain', 'mengucilkan teman', 'semua teman merasa senang'),
 ('merapikan alat setelah bermain', 'mengembalikan bola ke tempatnya', 'meninggalkan alat berserakan', 'alat tidak hilang'),
 ('berdoa sebelum berolahraga', 'berdoa agar diberi keselamatan', 'langsung bermain tanpa berdoa', 'kegiatan menjadi berkah'),
 ('melakukan pemanasan', 'melakukan pemanasan sebelum bermain', 'langsung berlari tanpa pemanasan', 'otot siap dan terhindar cedera'),
]
KOLAB = [
 ('estafet', 'menyerahkan tongkat kepada teman dengan tepat', 'menjatuhkan tongkat dengan sengaja', 'tim bergerak lebih cepat'),
 ('mengoper bola', 'mengoper bola kepada teman yang bebas', 'menahan bola sendiri terus', 'semua ikut bermain'),
 ('membagi peran', 'menerima peran yang dibagikan', 'memilih peran semaunya sendiri', 'tugas tim terbagi rata'),
 ('memberi semangat', 'menyemangati teman yang tertinggal', 'mengejek teman yang tertinggal', 'tim menjadi kompak'),
 ('berkomunikasi', 'menyebut nama teman sebelum mengoper', 'diam tanpa memberi isyarat', 'tidak saling bertabrakan'),
 ('menjaga posisi', 'kembali ke posisi masing-masing', 'berkumpul di satu tempat', 'lapangan terjaga rapi'),
 ('saling membantu', 'menolong teman yang terjatuh', 'meninggalkan teman yang terjatuh', 'tidak ada yang cedera'),
 ('menyusun strategi', 'berunding sebelum bermain', 'bermain tanpa rencana', 'peluang tim menang lebih besar'),
]

# ---------------------------------------------------------------- TB-1 lokomotor
f('TB', 1, 'Gerak berpindah tempat disebut gerak ....', 'lokomotor', ['non-lokomotor', 'diam', 'manipulatif'])
f('TB', 1, 'Contoh gerak lokomotor adalah ....', 'berlari', ['membungkuk', 'meregang', 'memutar badan di tempat'])
f('TB', 1, 'Gerak lokomotor ditandai dengan tubuh yang ....', 'berpindah tempat', ['tetap di tempat', 'diam', 'tidur'])
f('TB', 1, 'Berjalan, berlari, dan melompat termasuk gerak ....', 'lokomotor', ['non-lokomotor', 'manipulatif', 'statis'])
f('TB', 1, 'Gerak lokomotor yang paling cepat di antara berikut adalah ....', 'berlari', ['berjalan', 'berjingkat', 'merayap'], diff='medium')
f('TB', 1, 'Melompat dengan dua kaki dan mendarat dengan dua kaki disebut ....', 'meloncat', ['berjalan', 'merayap', 'berguling'], diff='medium')
f('TB', 1, 'Saat mendarat setelah melompat, lutut sebaiknya ....', 'ditekuk', ['dikunci lurus', 'diangkat tinggi', 'dibuka lebar sekali'], diff='medium')
f('TB', 1, 'Sebelum bergerak lokomotor, kita memeriksa bahwa ruang gerak kita ....', 'aman dan tidak ada penghalang', ['penuh barang', 'licin', 'ramai orang'])
f('TB', 1, 'Pemanasan sebelum berlari bertujuan untuk ....', 'mempersiapkan otot', ['membuat lelah', 'membuat sakit', 'menunda bermain'])
s('TB', 1, 'Guru meminta murid berlari kecil mengelilingi lapangan. Sikap yang baik adalah ....', 'Saat diminta berlari kecil mengelilingi lapangan, Rafi', 'berlari dengan tertib mengikuti arah yang ditentukan', ['mendorong teman', 'berlari melawan arah', 'berhenti mendadak di tengah'], 'Tertib dan aman.', 'easy')
s('TB', 1, 'Perhatikan gambar! Seorang anak berlari dengan kedua lengan diayun ke depan dan belakang di lapangan. Gerakan itu disebut ....', 'Gambar anak berlari mengayun lengan menunjukkan gerak', 'lokomotor', ['non-lokomotor', 'diam', 'manipulatif'], 'Berlari berpindah tempat.', 'easy', 'Anak laki-laki berseragam olahraga berlari di lapangan dengan lengan diayun.')
s('TB', 1, 'Perhatikan gambar! Seorang anak melompat ke depan dengan dua kaki lalu mendarat dengan lutut menekuk. Gerakan itu disebut ....', 'Gambar anak melompat dengan dua kaki dan mendarat menekuk lutut menunjukkan gerak', 'meloncat', ['berjingkat', 'merayap', 'berguling'], 'Dua kaki ke dua kaki = meloncat.', 'medium', 'Anak perempuan meloncat ke depan dengan dua kaki lalu mendarat lutut menekuk di atas matras.')
T += [('TB', 1, 'Berjalan termasuk gerak lokomotor.', True, 'Berjalan berpindah tempat.'), ('TB', 1, 'Membungkuk di tempat termasuk gerak lokomotor.', False, 'Membungkuk di tempat adalah non-lokomotor.')]
G += [('TB', 1, "Kelompokkan gerakan berikut: berlari, membungkuk, melompat, meregang, berjalan, memutar badan.", {'lokomotor': ['berlari', 'melompat', 'berjalan'], 'non-lokomotor': ['membungkuk', 'meregang', 'memutar badan']}, 'Lokomotor berpindah tempat.')]
perf('TB', 1, 'Praktikkan berjalan, berlari kecil, dan melompat di tempat yang aman!', 'Peragakan meloncat dengan dua kaki dan mendarat dengan lutut menekuk!', 'Berjalan zig-zag di antara kerucut tanpa menyentuhnya!', 'Berlari kecil berkeliling lapangan mengikuti arah yang ditentukan guru!')
O += [('TB', 1, 'Urutkan kegiatan sebelum berlari berikut!', ['Berdoa', 'Memeriksa tempat yang aman', 'Melakukan pemanasan', 'Berlari'], 'Persiapan berlari.')]

# ---------------------------------------------------------------- TB-2 non-lokomotor
f('TB', 2, 'Gerak yang dilakukan di tempat tanpa berpindah disebut gerak ....', 'non-lokomotor', ['lokomotor', 'manipulatif', 'cepat'])
f('TB', 2, 'Contoh gerak non-lokomotor adalah ....', 'membungkuk', ['berlari', 'melompat', 'berjalan'])
f('TB', 2, 'Gerak mengayunkan lengan di tempat termasuk gerak ....', 'non-lokomotor', ['lokomotor', 'manipulatif', 'diam'])
f('TB', 2, 'Meregangkan badan sebelum olahraga membuat otot menjadi ....', 'lentur', ['kaku', 'sakit', 'lelah'])
f('TB', 2, 'Berdiri dengan satu kaki melatih ....', 'keseimbangan', ['kecepatan lari', 'kekuatan lompat', 'kekuatan lempar'])
f('TB', 2, 'Saat memutar badan, kaki tetap berada di ....', 'tempat', ['sejauh mungkin', 'depan', 'belakang'], diff='medium')
f('TB', 2, 'Gerak mendorong dan menarik termasuk gerak ....', 'non-lokomotor', ['lokomotor', 'melompat', 'berlari'], diff='medium')
f('TB', 2, 'Gerak non-lokomotor dapat dilakukan di ruang yang ....', 'sempit tetapi aman', ['sangat ramai', 'licin', 'penuh barang'])
s('TB', 2, 'Guru meminta murid berdiri satu kaki selama lima hitungan. Hasan ....', 'Saat diminta berdiri satu kaki, Hasan', 'berusaha menjaga keseimbangan dengan tenang', ['menjatuhkan diri', 'mengganggu teman', 'berlari'], 'Menjaga keseimbangan.', 'easy')
s('TB', 2, 'Perhatikan gambar! Anak-anak berdiri di tempat sambil meregangkan kedua lengan ke atas. Gerakan ini disebut ....', 'Gambar anak-anak berdiri meregangkan kedua lengan ke atas menunjukkan gerak', 'meregang (non-lokomotor)', ['berlari', 'melompat', 'merayap'], 'Meregang di tempat.', 'easy', 'Lima anak berbaris di tempat dengan kedua lengan lurus ke atas.')
T += [('TB', 2, 'Memutar badan di tempat adalah gerak non-lokomotor.', True, 'Tanpa berpindah.'), ('TB', 2, 'Berlari termasuk gerak non-lokomotor.', False, 'Berlari lokomotor.')]
perf('TB', 2, 'Peragakan membungkuk, meregang, dan memutar badan dengan benar!', 'Berdiri satu kaki selama lima hitungan lalu ganti kaki!', 'Ayunkan kedua lengan ke depan dan ke belakang dengan irama!')
M += [('TB', 2, 'Jodohkan gerak non-lokomotor dengan penjelasannya!', [('mendorong', 'menekan benda menjauhi badan'), ('menarik', 'membawa benda mendekati badan'), ('mengayun', 'menggerakkan lengan ke depan dan belakang'), ('membungkuk', 'menekuk badan ke depan')], 'Gerak non-lokomotor.')]

# ---------------------------------------------------------------- TB-3 eksplorasi
f('TB', 3, 'Menggerakkan tubuh dengan cara berbeda-beda disebut ....', 'bereksplorasi gerak', ['berhenti', 'bertengkar', 'tidur'])
f('TB', 3, 'Kita dapat bergerak dengan tubuh tinggi atau ....', 'rendah', ['rata', 'gelap', 'basah'])
f('TB', 3, 'Kita dapat bergerak dengan kecepatan cepat atau ....', 'lambat', ['gelap', 'kasar', 'basah'])
f('TB', 3, 'Kita dapat bergerak ke depan, ke belakang, atau ke ....', 'samping', ['langit', 'dalam tanah', 'awan'], diff='medium')
f('TB', 3, 'Menirukan gerak hewan, misalnya kelinci melompat, adalah cara ....', 'mengeksplorasi gerak', ['mengganggu teman', 'bermain curang', 'beristirahat'])
f('TB', 3, 'Gerak yang diiringi musik atau irama disebut gerak ....', 'berirama', ['kaku', 'diam', 'sunyi'], diff='medium')
f('TB', 3, 'Berjalan dengan langkah lebar berbeda dari berjalan dengan langkah ....', 'kecil', ['besar sekali', 'tinggi', 'gelap'], diff='medium')
f('TB', 3, 'Saat mengeksplorasi gerak, kita tetap harus ....', 'berhati-hati dan memperhatikan teman', ['berlari menabrak', 'mendorong teman', 'berteriak'])
s('TB', 3, 'Bu guru bertanya, "Bagaimana cara lain berjalan?" Salma mencoba berjalan ....', 'Saat diminta mencoba cara lain berjalan, Salma', 'dengan langkah kecil, lalu langkah lebar', ['dengan menabrak teman', 'tanpa melihat', 'sambil berteriak'], 'Mencoba beragam gerak.', 'easy')
s('TB', 3, 'Perhatikan gambar! Anak-anak menirukan gajah dengan berjalan pelan dan lengan seperti belalai. Mereka sedang ....', 'Gambar anak-anak berjalan pelan menirukan gajah menunjukkan mereka sedang', 'mengeksplorasi gerak', ['bertengkar', 'beristirahat', 'bermain curang'], 'Menirukan hewan.', 'easy', 'Empat anak berjalan pelan dengan lengan lurus ke depan seperti belalai gajah.')
T += [('TB', 3, 'Satu gerakan hanya dapat dilakukan dengan satu cara.', False, 'Gerak dapat dieksplorasi.'), ('TB', 3, 'Gerak dapat dilakukan cepat maupun lambat.', True, 'Kecepatan beragam.')]
perf('TB', 3, 'Berjalan dengan cara berbeda: langkah kecil, langkah lebar, ujung kaki!', 'Tirukan gerak kelinci, gajah, dan burung!', 'Bergerak tinggi lalu rendah mengikuti hitungan guru!', 'Bergerak mengikuti irama musik sederhana dengan gerakanmu sendiri!')

# ---------------------------------------------------------------- TB-4 manipulasi objek
f('TB', 4, 'Gerak mengendalikan benda seperti bola disebut gerak ....', 'manipulatif', ['lokomotor', 'diam', 'non-lokomotor'])
f('TB', 4, 'Bola dilempar dengan menggunakan ....', 'tangan', ['telinga', 'kaki saja', 'hidung'])
f('TB', 4, 'Bola ditendang dengan menggunakan ....', 'kaki', ['kepala', 'tangan', 'siku'])
f('TB', 4, 'Memantulkan bola ke lantai menggunakan ....', 'telapak tangan', ['dahi', 'siku', 'lutut'])
f('TB', 4, 'Saat menangkap bola, pandangan mata diarahkan ke ....', 'bola', ['langit', 'tanah', 'teman yang jauh'], diff='medium')
f('TB', 4, 'Menangkap bola besar dilakukan dengan ....', 'kedua tangan', ['satu jari', 'kaki', 'hidung'])
f('TB', 4, 'Selain bola, benda yang dapat dimanipulasi adalah ....', 'kantong biji dan selendang', ['batu besar', 'pisau', 'kaca'])
f('TB', 4, 'Bola yang aman dipakai anak kelas 1 adalah bola yang ....', 'lembut dan ringan', ['keras dan berat', 'tajam', 'berduri'], diff='medium')
s('TB', 4, 'Rafi diminta memantulkan bola ke lantai berulang kali. Ia memakai ....', 'Untuk memantulkan bola berulang kali, Rafi memakai', 'telapak tangan', ['hidung', 'siku', 'dagu'], 'Bola dipantulkan dengan tangan.', 'easy')
s('TB', 4, 'Perhatikan gambar! Seorang anak menendang bola dengan punggung kaki ke arah temannya. Bagian tubuh yang dipakai adalah ....', 'Gambar anak menendang bola ke arah temannya menunjukkan bagian tubuh yang dipakai adalah', 'kaki', ['tangan', 'kepala', 'lutut'], 'Menendang memakai kaki.', 'easy', 'Anak laki-laki menendang bola pelan ke arah temannya di lapangan rumput.')
kvm = MANIP
T += [('TB', 4, 'Bola dilempar dengan kaki.', False, 'Dilempar dengan tangan.'), ('TB', 4, 'Menendang bola memakai kaki.', True, 'Menendang dengan kaki.')]
perf('TB', 4, 'Lempar dan tangkap bola kecil dengan temanmu dari jarak dekat!', 'Pantulkan bola ke lantai lima kali berturut-turut!', 'Tendang bola pelan ke arah temanmu!', 'Gerakkan selendang ke atas dan ke bawah dengan kedua tangan!')

# ---------------------------------------------------------------- TB-5 fundamental kompleks
f('TB', 5, 'Berlari sambil menggiring bola menggabungkan gerak ....', 'lokomotor dan manipulatif', ['non-lokomotor saja', 'diam saja', 'lokomotor saja'])
f('TB', 5, 'Berlari lalu melompat melewati rintangan menggabungkan gerak ....', 'berlari dan melompat', ['duduk dan tidur', 'diam dan berbaring', 'berjalan dan duduk'])
f('TB', 5, 'Permainan kucing dan tikus melatih gerak ....', 'berlari, menghindar, dan berhenti', ['hanya duduk', 'hanya berdiri', 'hanya berbaring'])
f('TB', 5, 'Lintasan rintangan terdiri dari beberapa gerak yang dilakukan ....', 'berurutan', ['sekaligus', 'sembarangan', 'terbalik'])
f('TB', 5, 'Dalam lintasan rintangan, kita tidak boleh ....', 'mendorong teman', ['menunggu giliran', 'berhati-hati', 'berlari pelan'])
f('TB', 5, 'Berlari kecil lalu menangkap bola yang dilempar teman menggabungkan gerak ....', 'berlari dan menangkap', ['tidur dan duduk', 'diam dan berdiri', 'merayap dan berguling'], diff='medium')
f('TB', 5, 'Agar tidak bertabrakan saat bermain, kita harus ....', 'memperhatikan ruang gerak teman', ['menutup mata', 'berlari tanpa melihat', 'berteriak'])
s('TB', 5, 'Dalam lintasan rintangan, Dina harus melompati tali, merayap di bawah palang, lalu berlari. Dina ....', 'Dalam lintasan rintangan, Dina', 'melakukan gerak satu per satu dengan urutan yang benar', ['melompati semua rintangan sekaligus', 'melewati rintangan tanpa urutan', 'berhenti di tengah dan pulang'], 'Mengikuti urutan lintasan.', 'medium')
s('TB', 5, 'Perhatikan gambar! Anak-anak melewati lintasan: melompati tali, merayap di bawah palang, lalu berlari ke garis akhir. Lintasan ini melatih gerak ....', 'Gambar anak-anak melewati lintasan rintangan melatih gerak', 'gabungan beberapa gerak', ['satu gerak saja', 'diam saja', 'menulis saja'], 'Gabungan gerak.', 'medium', 'Lintasan berisi tali rendah, palang rendah, dan garis akhir; tiga anak melewatinya bergantian.')
T += [('TB', 5, 'Menggabungkan beberapa gerak dapat dilakukan dalam permainan.', True, 'Permainan menggabungkan gerak.'), ('TB', 5, 'Dalam lintasan rintangan, kita boleh mendorong teman agar lebih cepat.', False, 'Tidak boleh mendorong.')]
O += [('TB', 5, 'Urutkan gerakan pada lintasan rintangan berikut!', ['Berlari ke tali', 'Melompati tali', 'Merayap di bawah palang', 'Berlari ke garis akhir'], 'Urutan lintasan.')]
perf('TB', 5, 'Lewati lintasan rintangan sederhana: lompat, rayap, lalu lari!', 'Berlari sambil menggiring bola dengan kaki dari garis awal ke garis akhir!', 'Mainkan kucing dan tikus dengan tertib bersama teman!', 'Berlari kecil lalu tangkap bola yang dilempar guru!')

# ---------------------------------------------------------------- TB-6 metode & kontrol
f('TB', 6, 'Mengontrol gerakan berarti kita dapat ....', 'berhenti dan bergerak sesuai keinginan', ['bergerak tanpa tujuan', 'jatuh', 'menabrak'])
f('TB', 6, 'Saat diminta berhenti oleh guru, kita harus ....', 'segera berhenti dan diam', ['terus berlari', 'berteriak', 'menabrak teman'])
f('TB', 6, 'Gerak lambat dilakukan dengan tenaga yang ....', 'terkontrol dan kecil', ['sangat besar', 'asal-asalan', 'tidak ada'], diff='medium')
f('TB', 6, 'Agar tidak jatuh saat berdiri satu kaki, tubuh harus ....', 'seimbang', ['bergoyang kuat', 'condong jauh', 'bergerak cepat'])
f('TB', 6, 'Menahan posisi tubuh tanpa bergerak, misalnya patung, melatih ....', 'kontrol tubuh', ['kecepatan', 'kelucuan', 'kemarahan'])
f('TB', 6, 'Bergerak mengikuti irama musik melatih ....', 'kontrol dan ritme gerak', ['kemarahan', 'kelelahan', 'kemalasan'])
f('TB', 6, 'Saat bergerak dalam ruang bersama teman, kita menjaga ....', 'jarak aman', ['jarak sejauh mungkin', 'jarak terlalu dekat', 'jarak yang bebas'])
f('TB', 6, 'Mendarat dengan baik dilakukan dengan lutut ....', 'sedikit ditekuk', ['dikunci', 'diangkat', 'dibuka lebar'])
s('TB', 6, 'Guru memainkan permainan "patung". Saat musik berhenti, murid harus ....', 'Saat musik berhenti dalam permainan patung, Fikri', 'berhenti dan diam tanpa bergerak', ['terus bergerak', 'berlari', 'tertawa keras'], 'Mengontrol gerak.', 'easy')
s('TB', 6, 'Perhatikan gambar! Anak-anak berhenti dalam posisi seperti patung saat musik berhenti. Mereka sedang melatih ....', 'Gambar anak-anak berhenti seperti patung saat musik berhenti menunjukkan latihan', 'kontrol gerakan', ['kecepatan', 'permusuhan', 'kemalasan'], 'Kontrol gerak.', 'easy', 'Lima anak membeku dalam berbagai posisi seperti patung di lapangan.')
T += [('TB', 6, 'Mengontrol gerakan membantu kita terhindar dari cedera.', True, 'Kontrol gerak = aman.'), ('TB', 6, 'Berhenti mendadak tanpa melihat sekitar itu aman.', False, 'Perhatikan sekitar.')]
perf('TB', 6, 'Mainkan "patung": bergerak saat musik berbunyi, berhenti saat musik berhenti!', 'Berdiri satu kaki sambil menahan posisi lima hitungan!', 'Bergerak lambat lalu cepat sesuai aba-aba guru!', 'Mendarat dengan lutut menekuk setelah melompat dua kaki!')

# ---------------------------------------------------------------- TB-7 manipulasi akurat
f('TB', 7, 'Melempar bola ke sasaran menuntut ....', 'ketepatan arah dan tenaga', ['asal lempar', 'tenaga sangat besar', 'menutup mata'])
f('TB', 7, 'Untuk lemparan yang akurat, mata melihat ke ....', 'sasaran', ['langit', 'tanah', 'samping'])
f('TB', 7, 'Jika bola terlalu jauh dari sasaran, lemparan berikutnya sebaiknya ....', 'dikurangi atau ditambah tenaganya dengan tepat', ['dilempar sekuat tenaga', 'dilempar tanpa melihat', 'dihentikan'], diff='medium')
f('TB', 7, 'Mengevaluasi gerakan berarti ....', 'menilai apakah gerakan sudah tepat', ['melupakan gerakan', 'mengejek teman', 'berhenti berlatih'])
f('TB', 7, 'Latihan berulang membuat gerakan menjadi ....', 'semakin tepat', ['semakin salah', 'semakin lambat', 'semakin berbahaya'])
f('TB', 7, 'Menendang bola ke gawang menuntut ....', 'ketepatan arah tendangan', ['tenaga saja', 'menutup mata', 'diam'])
f('TB', 7, 'Jika berhasil memasukkan lima dari sepuluh lemparan, hasil tepatnya ... dari sepuluh.', '5', ['10', '0', '15'], diff='medium')
f('TB', 7, 'Saat melempar ke sasaran, daerah di depan sasaran harus ....', 'kosong dari orang', ['ramai orang', 'dilewati teman', 'licin'])
s('TB', 7, 'Lani melempar bola ke ember dari jarak dekat. Dari lima lemparan, tiga masuk. Lani ....', 'Setelah tiga dari lima lemparannya masuk ember, Lani', 'mencoba lagi dan memperbaiki arah lemparan', ['berhenti dan marah', 'menyalahkan bola', 'menyalahkan teman'], 'Evaluasi dan memperbaiki.', 'medium')
s('TB', 7, 'Perhatikan gambar! Seorang anak melempar bola ke dalam ember kecil dari garis yang ditandai, sementara teman mencatat hasilnya. Kegiatan ini melatih ....', 'Gambar anak melempar bola ke ember sementara teman mencatat hasil menunjukkan latihan', 'ketepatan lemparan dan evaluasi', ['kemalasan', 'kecurangan', 'kelelahan'], 'Akurasi dan evaluasi.', 'medium', 'Anak melempar bola ke ember dari garis kapur, teman mencatat hasil di papan kecil.')
T += [('TB', 7, 'Akurasi lemparan dapat ditingkatkan dengan latihan.', True, 'Latihan menambah akurasi.'), ('TB', 7, 'Lemparan akurat tidak membutuhkan fokus.', False, 'Butuh fokus.')]
perf('TB', 7, 'Lempar bola ke dalam ember sebanyak lima kali lalu catat berapa yang masuk!', 'Tendang bola pelan ke gawang kecil dan hitung yang masuk!', 'Pantulkan bola ke lantai dan tangkap sebanyak yang kamu bisa tanpa gagal!', 'Nilai lemparanmu sendiri: apakah sudah tepat? Ceritakan dengan jujur!')

# ---------------------------------------------------------------- BG-1 fair play aturan
f('BG', 1, 'Bermain adil dan jujur disebut bermain secara ....', 'fair play', ['curang', 'asal-asalan', 'kasar'])
f('BG', 1, 'Aturan permainan dibuat agar permainan ....', 'adil dan aman', ['kacau', 'berbahaya', 'berat sebelah'])
f('BG', 1, 'Jika temanmu tidak sengaja menabrakmu saat bermain, sikap yang baik adalah ....', 'memaafkan', ['membalas', 'mengejek', 'menangis keras'])
f('BG', 1, 'Pemain yang sportif adalah pemain yang ....', 'jujur dan menerima kalah menang', ['curang', 'sombong', 'pemarah'])
f('BG', 1, 'Sebelum bermain, guru biasanya ....', 'menjelaskan aturan permainan', ['menutup lapangan', 'melarang bermain', 'menyuruh pulang'])
f('BG', 1, 'Bermain curang membuat teman merasa ....', 'dirugikan', ['senang', 'bangga', 'untung'])
f('BG', 1, 'Setelah pertandingan selesai, pemain yang baik ....', 'bersalaman dengan lawan', ['bertengkar', 'mengejek lawan', 'meninggalkan lapangan tanpa pamit'])
s('BG', 1, 'Saat bermain petak umpet, Fikri tersentuh temannya tetapi pura-pura tidak merasa. Sikap yang jujur adalah ....', 'Saat tersentuh dalam permainan, Fikri yang jujur', 'mengaku bahwa ia tersentuh', ['pura-pura tidak tersentuh', 'berlari menjauh', 'menyalahkan temannya'], 'Fair play = jujur.', 'easy')
s('BG', 1, 'Tim Dina kalah dalam permainan estafet. Sikap Dina yang baik adalah ....', 'Setelah timnya kalah dalam estafet, Dina', 'memberi selamat kepada tim pemenang', ['menangis dan marah', 'mengejek pemenang', 'menyalahkan temannya'], 'Menerima kekalahan.', 'easy')
s('BG', 1, 'Perhatikan gambar! Dua tim bersalaman dan tersenyum setelah pertandingan. Sikap mereka menunjukkan ....', 'Gambar dua tim bersalaman setelah pertandingan menunjukkan sikap', 'sportif dan fair play', ['curang', 'sombong', 'marah'], 'Sportif.', 'easy', 'Dua barisan anak saling bersalaman di tengah lapangan setelah bermain.')
T += [('BG', 1, 'Fair play berarti bermain jujur dan menaati aturan.', True, 'Itulah fair play.'), ('BG', 1, 'Boleh mengubah aturan jika tim kita akan kalah.', False, 'Aturan tidak boleh diubah seenaknya.')]
perf('BG', 1, 'Peragakan sikap menerima kemenangan dan kekalahan dengan sportif!', 'Mainkan permainan sederhana dan sebutkan aturan yang kamu taati!')

# ---------------------------------------------------------------- BG-2 strategi kolaborasi dasar
f('BG', 2, 'Bekerja sama dalam tim membuat permainan menjadi ....', 'lebih menyenangkan dan lancar', ['kacau', 'membosankan', 'berbahaya'])
f('BG', 2, 'Dalam permainan beregu, setiap anggota memiliki ....', 'peran', ['kekuasaan penuh', 'hak mengubah aturan', 'tempat tidur'])
f('BG', 2, 'Saat teman kesulitan, anggota tim yang baik akan ....', 'membantu', ['mengejek', 'meninggalkan', 'marah'])
f('BG', 2, 'Mengoper bola kepada teman yang tidak dijaga lawan adalah contoh ....', 'strategi kerja sama', ['kecurangan', 'permainan sendiri', 'kemarahan'])
f('BG', 2, 'Berbicara dengan teman tim tentang rencana disebut ....', 'berkomunikasi', ['bertengkar', 'berdiam', 'berlari'])
f('BG', 2, 'Estafet adalah lomba lari yang dilakukan ....', 'berkelompok secara bergantian', ['sendiri', 'sambil berbaring', 'tanpa aturan'])
s('BG', 2, 'Dalam permainan estafet, Lani harus menyerahkan tongkat kepada temannya. Sikap yang baik adalah ....', 'Dalam estafet, Lani', 'menyerahkan tongkat dengan tepat dan hati-hati', ['melempar tongkat sembarangan', 'menyimpan tongkat', 'berlari pulang'], 'Kerja sama dalam tim.', 'easy')
s('BG', 2, 'Temanmu sulit menangkap bola. Sebagai anggota tim kamu ....', 'Saat temannya sulit menangkap bola, Hasan', 'memberi semangat dan mengoper pelan', ['mengejeknya', 'mengoper sekuat tenaga', 'menjauh'], 'Saling mendukung.', 'easy')
s('BG', 2, 'Perhatikan gambar! Anak-anak mengoper bola bergantian membentuk lingkaran. Hal ini menunjukkan ....', 'Gambar anak-anak mengoper bola bergantian dalam lingkaran menunjukkan', 'kerja sama tim', ['permainan sendiri', 'pertengkaran', 'kecurangan'], 'Kerja sama.', 'easy', 'Enam anak membentuk lingkaran dan mengoper bola secara bergantian.')
T += [('BG', 2, 'Dalam tim, semua anggota perlu diberi kesempatan bermain.', True, 'Kerja sama inklusif.'), ('BG', 2, 'Menyimpan bola sendiri membantu tim bekerja sama.', False, 'Itu merugikan tim.')]
perf('BG', 2, 'Mainkan estafet sederhana dengan timmu sambil saling menyemangati!', 'Operkan bola dalam lingkaran secara bergantian tanpa menjatuhkannya!', 'Jelaskan peranmu dalam permainan timmu!')

# ---------------------------------------------------------------- BG-3 aturan konsisten
f('BG', 3, 'Menaati aturan secara konsisten berarti ....', 'tetap taat di setiap saat', ['taat hanya saat diawasi', 'taat sekali saja', 'taat jika menang'])
f('BG', 3, 'Aturan harus ditaati bahkan ketika kita ....', 'sedang kalah', ['sedang menang saja', 'sedang sendirian saja', 'tidak ada guru saja'])
f('BG', 3, 'Mengingatkan teman yang melanggar aturan sebaiknya dengan ....', 'sopan dan lembut', ['kasar', 'berteriak', 'memukul'])
f('BG', 3, 'Aturan yang sudah disepakati ....', 'tidak diubah seenaknya', ['boleh diubah sendiri', 'dilupakan', 'dilanggar'])
f('BG', 3, 'Tidak diawasi guru, pemain yang jujur tetap ....', 'menaati aturan', ['melanggar aturan', 'berbohong', 'mengubah aturan'])
f('BG', 3, 'Jika semua pemain taat aturan, permainan menjadi ....', 'tertib dan menyenangkan', ['kacau', 'berbahaya', 'membosankan'])
s('BG', 3, 'Saat guru sedang tidak melihat, teman mengajak Zaki menerobos antrean permainan. Zaki ....', 'Saat guru tidak melihat dan diajak menerobos antrean, Zaki', 'menolak dan tetap mengantre', ['ikut menerobos', 'diam saja', 'menyuruh teman lain'], 'Konsisten taat aturan.', 'medium')
s('BG', 3, 'Permainan hampir selesai dan tim Dina tertinggal. Dina ....', 'Walaupun timnya tertinggal, Dina', 'tetap bermain sesuai aturan', ['mengubah aturan', 'curang', 'menyerah dan marah'], 'Aturan tetap berlaku.', 'medium')
T += [('BG', 3, 'Aturan permainan ditaati hanya ketika ada guru.', False, 'Konsisten sepanjang waktu.'), ('BG', 3, 'Taat aturan secara konsisten membuat kita dipercaya.', True, 'Konsisten dipercaya.')]
perf('BG', 3, 'Mainkan permainan sederhana dan tunjukkan bahwa kamu menaati semua aturannya sampai selesai!', 'Ingatkan temanmu dengan sopan saat ia melanggar aturan permainan!')

# ---------------------------------------------------------------- BG-4 kolaborasi menantang
f('BG', 4, 'Dalam permainan yang menantang, tim perlu menyusun ....', 'strategi bersama', ['kecurangan', 'pertengkaran', 'jalan pintas'])
f('BG', 4, 'Membagi tim menjadi penyerang dan penjaga adalah contoh ....', 'pembagian peran', ['kecurangan', 'kekacauan', 'perselisihan'])
f('BG', 4, 'Setelah permainan, tim sebaiknya ....', 'membahas apa yang sudah berjalan baik', ['saling menyalahkan', 'bertengkar', 'meninggalkan lapangan'], diff='medium')
f('BG', 4, 'Jika rencana tim tidak berhasil, tim sebaiknya ....', 'berdiskusi dan mencoba strategi lain', ['saling marah', 'berhenti bermain', 'menyalahkan satu orang'])
f('BG', 4, 'Memberi isyarat dengan tangan kepada teman tim membantu ....', 'berkomunikasi dalam permainan', ['mengganggu', 'mengejek', 'menunda permainan'])
f('BG', 4, 'Kolaborasi yang menantang membutuhkan ....', 'kesabaran dan kepercayaan antaranggota', ['kemarahan', 'kecurangan', 'kesombongan'])
s('BG', 4, 'Tim Rafi bermain "memindahkan bola tanpa tangan" dengan rintangan. Strategi yang baik adalah ....', 'Dalam permainan memindahkan bola dengan rintangan, tim Rafi', 'berunding, membagi tugas, lalu bergerak bersama', ['berlari sendiri-sendiri', 'berebut bola', 'saling menyalahkan'], 'Strategi bersama.', 'medium')
s('BG', 4, 'Perhatikan gambar! Sekelompok anak berdiskusi membentuk lingkaran sebelum permainan tim dimulai. Hal ini menunjukkan ....', 'Gambar sekelompok anak berdiskusi sebelum permainan tim menunjukkan', 'penyusunan strategi', ['perpecahan', 'kemarahan', 'kemalasan'], 'Merencanakan strategi.', 'easy', 'Lima anak merunduk membentuk lingkaran kecil berdiskusi di tengah lapangan.')
T += [('BG', 4, 'Menyusun strategi bersama membuat tim lebih siap.', True, 'Strategi = siap.'), ('BG', 4, 'Menyalahkan teman adalah strategi kolaborasi yang baik.', False, 'Itu merusak tim.')]
perf('BG', 4, 'Susun strategi timmu dalam permainan memindahkan bola lalu praktikkan!', 'Diskusikan dengan timmu apa yang bisa diperbaiki setelah permainan!', 'Mainkan estafet dengan rintangan dan bagi peran dengan adil!')
O += [('BG', 4, 'Urutkan langkah tim sebelum bermain berikut!', ['Berkumpul bersama tim', 'Berunding membagi peran', 'Menyepakati strategi', 'Mulai bermain'], 'Persiapan strategi.')]

# ---------------------------------------------------------------- HA-1 partisipasi & manfaat
f('HA', 1, 'Aktivitas fisik adalah kegiatan yang ....', 'menggerakkan tubuh', ['membuat tubuh diam', 'hanya duduk', 'hanya tidur'])
f('HA', 1, 'Contoh aktivitas fisik adalah ....', 'bermain bola', ['menonton televisi', 'tidur siang', 'duduk lama'])
f('HA', 1, 'Sebelum berolahraga kita melakukan ....', 'pemanasan', ['tidur', 'makan banyak', 'menonton'])
f('HA', 1, 'Setelah berolahraga kita melakukan ....', 'pendinginan dan minum air', ['langsung tidur', 'langsung makan banyak', 'berlari lagi'])
f('HA', 1, 'Minuman yang baik saat berolahraga adalah ....', 'air putih', ['minuman manis', 'minuman bersoda', 'kopi'])
f('HA', 1, 'Pakaian yang cocok untuk berolahraga adalah ....', 'pakaian yang nyaman dan menyerap keringat', ['pakaian sempit', 'pakaian tebal basah', 'sandal licin'])
f('HA', 1, 'Aktivitas fisik sebaiknya dilakukan ....', 'secara rutin', ['jarang sekali', 'hanya saat sakit', 'tidak pernah'])
f('HA', 1, 'Berolahraga bersama teman akan membuat kita ....', 'gembira', ['sedih', 'marah', 'malas'])
s('HA', 1, 'Hari Minggu Dani diajak ayah bersepeda. Dani ....', 'Saat diajak ayah bersepeda, Dani', 'ikut dengan gembira dan memakai pelindung', ['menolak dan tidur', 'bermain gawai saja', 'berpura-pura sakit'], 'Berpartisipasi aktif.', 'easy')
s('HA', 1, 'Perhatikan gambar! Anak-anak melakukan senam pagi bersama di halaman sekolah. Kegiatan ini adalah ....', 'Gambar anak-anak senam pagi bersama di halaman sekolah menunjukkan kegiatan', 'aktivitas fisik', ['kegiatan tidur', 'kegiatan makan', 'kegiatan menonton'], 'Senam adalah aktivitas fisik.', 'easy', 'Dua puluh anak berbaris dan melakukan senam bersama di halaman sekolah pagi hari.')
T += [('HA', 1, 'Berolahraga baik untuk kesehatan tubuh.', True, 'Olahraga menyehatkan.'), ('HA', 1, 'Pendinginan dilakukan sebelum olahraga.', False, 'Pendinginan setelah olahraga.')]
M += [('HA', 1, 'Jodohkan aktivitas fisik dengan manfaatnya!', MANFAAT[:4], 'Manfaat aktivitas fisik.')]
perf('HA', 1, 'Ikuti senam pagi di sekolah dengan semangat!', 'Lakukan pemanasan sederhana sebelum bermain di lapangan!', 'Sebutkan tiga aktivitas fisik yang kamu lakukan minggu ini!')

# ---------------------------------------------------------------- HA-2 manfaat
f('HA', 2, 'Berolahraga membuat jantung dan otot menjadi ....', 'kuat', ['lemah', 'sakit', 'lelah terus'])
f('HA', 2, 'Aktivitas fisik membuat tidur menjadi ....', 'nyenyak', ['gelisah', 'sulit', 'terganggu'])
f('HA', 2, 'Selain membuat sehat, olahraga juga membuat hati ....', 'gembira', ['sedih', 'marah', 'takut'])
f('HA', 2, 'Terlalu lama bermain gawai tanpa bergerak dapat membuat badan ....', 'kurang sehat', ['lebih kuat', 'lebih lincah', 'lebih bugar'])
f('HA', 2, 'Tulang yang kuat dapat dijaga dengan ....', 'aktif bergerak dan minum susu', ['duduk terus', 'begadang', 'tidak makan'], diff='medium')
f('HA', 2, 'Berolahraga setiap hari dengan senang hati menunjukkan rasa syukur atas ....', 'tubuh yang sehat', ['uang jajan', 'mainan', 'gawai'])
f('HA', 2, 'Jika merasa pusing atau sakit saat berolahraga, kita harus ....', 'berhenti dan memberi tahu guru atau orang dewasa', ['terus berlari', 'menyembunyikan', 'berpura-pura sehat'])
f('HA', 2, 'Anak yang aktif bergerak biasanya ....', 'lebih bugar dan ceria', ['lebih lemas', 'lebih sakit', 'lebih sedih'])
s('HA', 2, 'Setelah bermain bola, Rafi merasa badannya segar dan hatinya senang. Itu adalah ....', 'Setelah bermain bola, badan segar dan hati senang adalah', 'manfaat aktivitas fisik', ['akibat bermalas-malasan', 'tanda sakit', 'hukuman'], 'Manfaat olahraga.', 'easy')
s('HA', 2, 'Salma lebih suka bermain gawai seharian. Ibu mengajaknya bersepeda sebentar. Salma sebaiknya ....', 'Diajak ibu bersepeda sebentar, Salma', 'ikut karena bergerak baik untuk kesehatan', ['menolak dan terus bermain gawai', 'marah', 'tidur'], 'Mengurangi layar, aktif bergerak.', 'medium')
s('HA', 2, 'Perhatikan gambar! Anak laki-laki tersenyum lebar setelah berlari bersama teman-temannya di lapangan. Hal ini menunjukkan manfaat olahraga berupa ....', 'Gambar anak tersenyum setelah berlari bersama teman-temannya menunjukkan manfaat olahraga', 'kegembiraan dan kebugaran', ['kesedihan', 'penyakit', 'kemarahan'], 'Olahraga menggembirakan.', 'easy', 'Beberapa anak berlari di lapangan dengan wajah ceria berkeringat.')
T += [('HA', 2, 'Olahraga membantu tubuh bugar dan hati gembira.', True, 'Manfaat olahraga.'), ('HA', 2, 'Aktivitas fisik tidak memberi manfaat apa pun.', False, 'Banyak manfaatnya.')]
G += [('HA', 2, "Kelompokkan kebiasaan berikut: berolahraga, bermain gawai seharian, tidur cukup, begadang, bermain di luar, duduk terus.", {'menyehatkan': ['berolahraga', 'tidur cukup', 'bermain di luar'], 'kurang sehat': ['bermain gawai seharian', 'begadang', 'duduk terus']}, 'Kebiasaan sehat.')]
perf('HA', 2, 'Ceritakan manfaat yang kamu rasakan setelah berolahraga!', 'Buat jadwal olahraga sederhana untuk satu minggu bersama orang tuamu!', 'Ajak temanmu bermain di luar dan ceritakan perasaanmu!')

# ---------------------------------------------------------------- MH-1 gaya hidup & gizi
f('MH', 1, 'Makanan bergizi seimbang terdiri atas karbohidrat, protein, sayur, dan ....', 'buah', ['permen', 'minuman manis', 'gorengan'])
f('MH', 1, 'Fungsi karbohidrat bagi tubuh adalah sebagai sumber ....', 'tenaga', ['warna kulit', 'suara', 'rasa'])
f('MH', 1, 'Fungsi protein bagi tubuh adalah untuk ....', 'pertumbuhan dan memperbaiki tubuh', ['membuat gemuk saja', 'menggantikan air', 'mengurangi tenaga'], diff='medium')
f('MH', 1, 'Sayur dan buah mengandung vitamin yang membuat tubuh ....', 'sehat', ['sakit', 'lemah', 'lelah'])
f('MH', 1, 'Makanan yang tidak baik jika dimakan terlalu banyak adalah ....', 'makanan manis dan berminyak', ['sayur', 'buah', 'air putih'])
f('MH', 1, 'Pada label makanan kemasan, kita dapat melihat ....', 'informasi gizi dan tanggal kedaluwarsa', ['nama pemakan', 'harga mainan', 'warna baju'])
f('MH', 1, 'Makanan kemasan yang sudah kedaluwarsa sebaiknya ....', 'tidak dimakan', ['tetap dimakan', 'dibagikan', 'disimpan lama'])
f('MH', 1, 'Pola makan yang sehat adalah makan ....', 'teratur dan beragam', ['sekali sehari', 'hanya jajanan', 'hanya yang manis'])
f('MH', 1, 'Gaya hidup sehat meliputi makan bergizi, tidur cukup, dan ....', 'rajin bergerak', ['bermalas-malasan', 'begadang', 'jajan berlebihan'])
f('MH', 1, 'Air putih yang cukup diminum setiap hari membuat tubuh ....', 'tidak kekurangan cairan', ['mudah lelah', 'cepat sakit', 'gelisah'])
s('MH', 1, 'Di kantin, Dina memilih bekal. Pilihan yang sehat adalah ....', 'Saat memilih makanan di kantin, Dina yang sehat memilih', 'nasi, ikan, dan sayur', ['hanya permen', 'minuman bersoda', 'gorengan saja'], 'Bergizi seimbang.', 'easy')
s('MH', 1, 'Sebelum membeli snack kemasan, Fikri membaca labelnya. Yang perlu dilihat adalah ....', 'Sebelum membeli snack kemasan, Fikri melihat', 'tanggal kedaluwarsa dan informasi gizi', ['warna kemasan saja', 'gambar mainan', 'nama pembuat saja'], 'Membaca label gizi.', 'medium')
s('MH', 1, 'Perhatikan gambar! Sepiring makan berisi nasi, ikan, sayur bening, dan pisang, ditemani segelas air putih. Hidangan ini disebut ....', 'Gambar sepiring nasi, ikan, sayur, pisang, dan air putih menunjukkan hidangan', 'bergizi seimbang', ['kurang gizi', 'terlalu manis', 'tidak sehat'], 'Isi piringku: seimbang.', 'easy', 'Piring berisi nasi, ikan goreng, sayur bening, dan potongan pisang; gelas air putih di sampingnya.')
T += [('MH', 1, 'Sayur dan buah baik untuk kesehatan.', True, 'Sayur dan buah bergizi.'), ('MH', 1, 'Anak sehat cukup makan jajanan manis saja.', False, 'Perlu gizi seimbang.')]
M += [('MH', 1, 'Jodohkan makanan dengan golongannya!', GIZI[:4], 'Golongan makanan.')]
G += [('MH', 1, "Kelompokkan makanan berikut: nasi, bayam, ikan, pisang, tahu, wortel, jeruk, kentang.", {'karbohidrat': ['nasi', 'kentang'], 'protein': ['ikan', 'tahu'], 'sayur': ['bayam', 'wortel'], 'buah': ['pisang', 'jeruk']}, 'Golongan makanan.')]
perf('MH', 1, 'Sebutkan makanan sehat yang kamu makan hari ini!', 'Gambar piring makan bergizi seimbang dan jelaskan isinya!', 'Baca tanggal kedaluwarsa pada kemasan makanan bersama gurumu!')

# ---------------------------------------------------------------- MH-2 risiko keselamatan
f('MH', 2, 'Jika menemukan kabel listrik yang terkelupas, kita sebaiknya ....', 'menjauh dan memberi tahu orang dewasa', ['memegangnya', 'menariknya', 'memainkannya'])
f('MH', 2, 'Orang dewasa yang dapat dipercaya antara lain ....', 'orang tua dan guru', ['orang asing', 'penjual mainan', 'siapa saja yang ditemui'])
f('MH', 2, 'Jika terluka sedikit, kita memberi tahu ....', 'orang dewasa agar luka dibersihkan', ['tidak ada', 'musuh', 'hewan'])
f('MH', 2, 'Saat menyeberang jalan, kita harus ....', 'ditemani orang dewasa dan melihat kiri-kanan', ['berlari menyeberang', 'menutup mata', 'bermain di jalan'])
f('MH', 2, 'Jika ada orang asing yang mengajak pergi, kita harus ....', 'menolak dan mencari guru atau orang tua', ['ikut', 'menerima hadiah', 'diam saja'])
f('MH', 2, 'Benda tajam seperti pisau sebaiknya ....', 'tidak dimainkan oleh anak kecil', ['dimainkan', 'dibawa ke sekolah', 'dilempar'])
f('MH', 2, 'Obat-obatan hanya diminum atas petunjuk ....', 'orang tua atau dokter', ['teman', 'penjual', 'diri sendiri'])
f('MH', 2, 'Nomor telepon darurat yang dapat dihubungi dengan bantuan orang dewasa adalah ....', '112', ['000', '999', '111'], diff='hard')
f('MH', 2, 'Jika seseorang membuat kita merasa tidak nyaman, kita berhak ....', 'berkata tidak dan segera memberi tahu orang dewasa terpercaya', ['menyimpan sendiri', 'menuruti', 'diam'], diff='medium')
f('MH', 2, 'Saat bermain di luar, kita harus ....', 'memberi tahu orang tua dan bermain di tempat aman', ['pergi tanpa pamit', 'bermain di jalan raya', 'bermain di dekat sungai dalam sendirian'])
s('MH', 2, 'Raka melihat adik bermain dekat kompor yang menyala. Raka ....', 'Melihat adik bermain dekat kompor menyala, Raka', 'menjauhkan adik dan memanggil ibu', ['membiarkan', 'ikut bermain', 'menutup mata'], 'Mencari bantuan orang dewasa.', 'easy')
s('MH', 2, 'Seseorang yang tidak dikenal menawari Salma permen dan mengajak ke mobilnya. Salma ....', 'Ditawari permen oleh orang asing yang mengajak ke mobil, Salma', 'menolak dan segera mencari guru atau orang tua', ['menerima dan ikut', 'diam saja', 'berjalan mengikuti'], 'Aman dan mencari bantuan.', 'easy')
s('MH', 2, 'Perhatikan gambar! Anak berhenti di tepi jalan raya sambil memegang tangan ibunya dan melihat ke kiri dan kanan. Sikap ini menunjukkan ....', 'Gambar anak menunggu di tepi jalan sambil memegang tangan ibu menunjukkan sikap', 'menyeberang jalan dengan aman', ['ceroboh', 'berani sembarangan', 'tidak peduli'], 'Aman menyeberang.', 'easy', 'Anak berseragam memegang tangan ibu di tepi jalan, menoleh ke kiri dan kanan.')
s('MH', 2, 'Perhatikan gambar! Seorang anak memberi tahu gurunya bahwa lututnya luka karena terjatuh di lapangan. Sikap anak itu ....', 'Gambar anak melapor kepada guru karena luka di lutut menunjukkan sikap', 'mencari bantuan orang dewasa', ['menyembunyikan luka', 'marah', 'berlari menjauh'], 'Mencari bantuan.', 'easy', 'Anak menunjuk lututnya yang tergores kepada guru di lapangan.')
T += [('MH', 2, 'Jika ada bahaya, kita harus mencari bantuan orang dewasa terpercaya.', True, 'Mencari bantuan.'), ('MH', 2, 'Boleh bermain kabel listrik jika tidak dialiri listrik.', False, 'Jangan bermain kabel listrik.')]
M += [('MH', 2, 'Jodohkan situasi bahaya dengan tindakan yang tepat!', [('api kompor menyala', 'menjauh dan panggil orang dewasa'), ('lantai licin', 'berjalan pelan'), ('luka kecil', 'lapor dan minta dibersihkan'), ('orang asing mengajak pergi', 'menolak dan cari guru')], 'Tindakan aman.')]
perf('MH', 2, 'Peragakan cara menolak ajakan orang asing dan mencari bantuan guru!', 'Peragakan cara menyeberang jalan dengan aman bersama orang dewasa!', 'Sebutkan siapa saja orang dewasa yang bisa kamu percaya di rumah dan sekolah!', 'Peragakan cara melapor kepada guru jika terluka!')
