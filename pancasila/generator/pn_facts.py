# -*- coding: utf-8 -*-
"""Tabel dan fakta Pendidikan Pancasila Kelas 1. Kunci fakta: (bab, tp)."""
R = 'Dinilai guru: ketepatan jawaban, sikap, dan kesantunan (skala 1-4).'
F, S, T, P, G, O, M = [], [], [], [], [], [], []
def f(b, t, stem, ok, bad, expl='', diff='easy'): F.append((b, t, stem, ok, bad, expl or f'Jawaban: {ok}.', diff))
def s(b, t, long, short, ok, bad, expl, diff='medium', vis=None): S.append((b, t, long, short, ok, bad, expl, diff, vis))

# ------------------------------------------------------------------ tabel
SILA_LAMBANG = [(1, 'bintang'), (2, 'rantai'), (3, 'pohon beringin'), (4, 'kepala banteng'), (5, 'padi dan kapas')]
SILA_BUNYI = [(1, 'Ketuhanan Yang Maha Esa'), (2, 'Kemanusiaan yang adil dan beradab'), (3, 'Persatuan Indonesia'),
              (4, 'Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan'), (5, 'Keadilan sosial bagi seluruh rakyat Indonesia')]
SILA_MAKNA = [(1, 'percaya dan taat kepada Tuhan Yang Maha Esa'), (2, 'menyayangi dan memperlakukan sesama manusia dengan adil'), (3, 'bersatu dan mencintai tanah air'),
              (4, 'bermusyawarah untuk mencapai mufakat'), (5, 'bersikap adil kepada semua orang')]
SILA_CONTOH = [(1, 'salat berjemaah bersama keluarga'), (1, 'berdoa sebelum makan bersama'), (2, 'saling menyayangi sesama anggota keluarga'), (2, 'tidak membentak adik'),
               (3, 'bekerja sama membersihkan rumah'), (3, 'berdamai setelah bertengkar'), (4, 'bermusyawarah memilih tempat liburan'), (4, 'menghargai pendapat kakak'),
               (5, 'membagi tugas rumah secara adil'), (5, 'membagi makanan sama banyak')]
AGAMA = [('Islam', 'masjid', "Al-Qur'an", 'Idulfitri'), ('Kristen', 'gereja', 'Alkitab', 'Natal'), ('Hindu', 'pura', 'Weda', 'Nyepi'), ('Buddha', 'vihara', 'Tripitaka', 'Waisak'), ('Konghucu', 'klenteng', 'Si Shu', 'Imlek')]
RUMAH_ADAT = [('Joglo', 'Jawa Tengah'), ('Rumah Gadang', 'Sumatera Barat'), ('Rumah Bolon', 'Sumatera Utara'), ('Rumah Betang', 'Kalimantan'), ('Honai', 'Papua'), ('Rumoh Aceh', 'Aceh')]
TARI = [('Saman', 'Aceh'), ('Pendet', 'Bali'), ('Piring', 'Sumatera Barat'), ('Jaipong', 'Jawa Barat')]
MUSIK = [('angklung', 'Jawa Barat'), ('sasando', 'Nusa Tenggara Timur'), ('kolintang', 'Sulawesi Utara')]
MAKAN = [('rendang', 'Sumatera Barat'), ('pempek', 'Sumatera Selatan'), ('gudeg', 'Yogyakarta')]
TERIMA = [('matur nuwun', 'Jawa'), ('hatur nuhun', 'Sunda'), ('mauliate', 'Batak'), ('suksma', 'Bali')]
HOBI = [('membaca', 'buku'), ('menggambar', 'pensil warna'), ('bermain sepak bola', 'bola'), ('berenang', 'kolam renang'), ('menyanyi', 'lagu'), ('berkebun', 'tanaman'), ('memancing', 'pancing'), ('memasak', 'peralatan dapur')]
BAGIAN = [('halaman', 'tempat bermain dan menanam'), ('selokan', 'mengalirkan air'), ('tempat sampah', 'menampung sampah'), ('musala', 'tempat salat'), ('warung', 'tempat membeli kebutuhan'),
          ('lapangan', 'tempat berolahraga'), ('pagar', 'pembatas rumah'), ('jalan', 'tempat berjalan dan berkendara'), ('kebun', 'tempat menanam sayur'), ('pos ronda', 'tempat berjaga lingkungan')]
GOTONG = [('kerja bakti', 'lingkungan menjadi bersih'), ('ronda malam', 'lingkungan menjadi aman'), ('menjenguk tetangga yang sakit', 'tetangga merasa terhibur'), ('membersihkan selokan bersama', 'air mengalir lancar'),
          ('menanam pohon bersama', 'udara menjadi segar'), ('membuat taman kecil bersama', 'lingkungan menjadi asri'), ('membantu tetangga pindah rumah', 'pekerjaan menjadi ringan'), ('menyiapkan acara pengajian bersama', 'acara berjalan lancar')]
# (aturan, taat, tidak taat, manfaat)
ATURAN = [
 ('salat tepat waktu', 'segera salat ketika azan berkumandang', 'menunda salat sambil bermain', 'hidup menjadi disiplin'),
 ('merapikan mainan', 'menyimpan mainan setelah bermain', 'membiarkan mainan berserakan', 'rumah menjadi rapi'),
 ('meminta izin sebelum keluar rumah', 'berpamitan dan meminta izin kepada orang tua', 'pergi tanpa memberi tahu', 'orang tua tidak khawatir'),
 ('mencuci tangan sebelum makan', 'mencuci tangan dengan sabun sebelum makan', 'langsung makan dengan tangan kotor', 'badan terhindar dari penyakit'),
 ('makan bersama dengan tertib', 'duduk dan menunggu giliran mengambil makanan', 'berebut makanan', 'suasana makan menjadi nyaman'),
 ('tidur tepat waktu', 'tidur pada waktunya setelah berdoa', 'begadang sambil bermain gawai', 'badan menjadi segar'),
 ('belajar pada jam belajar', 'belajar dengan tenang di meja belajar', 'bermain saat jam belajar', 'menjadi pandai'),
 ('berkata jujur', 'mengakui kesalahan dengan jujur', 'berbohong kepada orang tua', 'dipercaya orang lain'),
 ('berbicara sopan kepada orang tua', 'berbicara dengan nada lembut', 'membentak orang tua', 'disayang keluarga'),
 ('membuang sampah pada tempatnya', 'memasukkan sampah ke tempat sampah', 'membuang sampah sembarangan', 'rumah menjadi bersih'),
 ('mematikan lampu yang tidak dipakai', 'mematikan lampu sebelum meninggalkan ruangan', 'membiarkan lampu menyala terus', 'listrik menjadi hemat'),
 ('menutup pintu dengan pelan', 'menutup pintu dengan perlahan', 'membanting pintu', 'suasana rumah tenang'),
 ('menyimpan sepatu di rak', 'meletakkan sepatu di rak setelah dipakai', 'melempar sepatu sembarangan', 'rumah menjadi rapi'),
 ('membantu pekerjaan rumah', 'membantu ibu menyapu atau mencuci piring', 'berpura-pura tidak melihat', 'pekerjaan menjadi ringan'),
 ('tidak mengganggu adik', 'bermain dengan adik secara baik', 'menjahili adik hingga menangis', 'keluarga rukun'),
 ('berdoa sebelum makan', 'membaca bismillah sebelum makan', 'makan tanpa berdoa', 'makanan menjadi berkah'),
 ('mendengarkan nasihat orang tua', 'mendengarkan nasihat dengan baik', 'menutup telinga saat dinasihati', 'terhindar dari kesalahan'),
 ('mengucap salam saat masuk rumah', 'mengucap salam ketika masuk rumah', 'langsung masuk tanpa memberi salam', 'rumah penuh keselamatan'),
]
LINGK_RULES = [
 ('membuang sampah pada tempatnya', 'memasukkan sampah ke tempat sampah', 'membuang sampah sembarangan', 'lingkungan menjadi bersih'),
 ('menyapu halaman', 'menyapu halaman setiap pagi', 'membiarkan halaman kotor', 'halaman menjadi asri'),
 ('membersihkan selokan', 'ikut membersihkan selokan dari sampah', 'membiarkan selokan tersumbat', 'air mengalir lancar'),
 ('merawat tanaman', 'menyiram tanaman secara teratur', 'menginjak dan mencabut tanaman', 'halaman menjadi indah'),
 ('menghemat air', 'menutup keran setelah dipakai', 'membiarkan keran mengalir terus', 'air tidak terbuang sia-sia'),
 ('memilah sampah', 'memisahkan sampah organik dan anorganik', 'mencampur semua sampah', 'sampah mudah diolah'),
 ('menutup tempat sampah', 'menutup tempat sampah dengan rapat', 'membiarkannya terbuka', 'tidak berbau dan tidak mengundang lalat'),
 ('merapikan halaman rumah', 'menata barang di halaman', 'meninggalkan barang berserakan', 'halaman rapi dan aman'),
 ('merawat hewan peliharaan', 'memberi makan dan menjaga kebersihan kandang', 'menelantarkan hewan peliharaan', 'hewan sehat dan lingkungan bersih'),
 ('tidak meludah sembarangan', 'meludah di tempat yang semestinya', 'meludah sembarangan', 'lingkungan terhindar dari penyakit'),
 ('menjaga sumber air', 'menjaga air bersih dari pencemaran', 'membuang sampah ke sungai', 'air tetap bersih dan sehat'),
 ('menanam pohon', 'menanam pohon di sekitar rumah', 'menebang pohon tanpa menanam kembali', 'udara menjadi sejuk'),
]
KERJASAMA = [
 ('kerja bakti membersihkan lingkungan', 'ikut menyapu dan memungut sampah dengan semangat', 'bermain sendiri dan tidak membantu', 'lingkungan cepat bersih'),
 ('membersihkan musala bersama', 'ikut mengelap dan merapikan sajadah', 'langsung pulang', 'musala menjadi nyaman'),
 ('menanam bunga bersama tetangga', 'membantu menyiram dan merawat bunga', 'menginjak bunga', 'lingkungan menjadi indah'),
 ('menolong tetangga yang sakit', 'mengantar makanan dan mendoakan', 'menertawakannya', 'tetangga terbantu'),
 ('membersihkan selokan bersama', 'membawa sapu dan ikut membersihkan', 'membuang sampah ke selokan', 'selokan bersih'),
 ('menyiapkan acara di lingkungan', 'membantu menata kursi', 'mengganggu persiapan', 'acara berjalan lancar'),
 ('mengumpulkan sampah plastik bersama', 'ikut memilah dan mengumpulkan sampah', 'mengacak-acak tumpukan sampah', 'sampah mudah didaur ulang'),
 ('membantu ibu dan tetangga di dapur umum', 'membantu mengambilkan peralatan', 'duduk dan menonton saja', 'pekerjaan menjadi ringan'),
]

# ------------------------------------------------------------------ BAB 1
f(1, 1, 'Setiap orang memiliki identitas yang ....', 'berbeda-beda', ['sama semua', 'tidak ada', 'selalu sama dengan teman'])
f(1, 1, 'Nama, jenis kelamin, dan hobi adalah contoh ....', 'identitas diri', ['bahaya', 'larangan', 'permainan'])
f(1, 1, 'Anak laki-laki dan anak perempuan sama-sama ciptaan ....', 'Allah', ['teman', 'guru', 'orang tua saja'])
f(1, 1, 'Hobi adalah kegiatan yang ....', 'kita sukai dan senang lakukan', ['kita benci', 'dilarang', 'membuat marah'])
f(1, 1, 'Bahasa yang dipakai di rumah dan sekolah di seluruh Indonesia sebagai bahasa pemersatu adalah bahasa ....', 'Indonesia', ['Inggris', 'Arab', 'Mandarin'])
f(1, 1, 'Selain bahasa Indonesia, banyak daerah memiliki bahasa ....', 'daerah', ['asing saja', 'hewan', 'isyarat bendera'])
f(1, 1, 'Teman sekelas kita bisa memiliki hobi yang ....', 'berbeda', ['sama persis', 'tidak ada', 'dilarang'])
f(1, 1, 'Agama yang dianut seseorang adalah bagian dari ....', 'identitasnya', ['permainannya', 'jajanannya', 'bajunya'])
f(1, 1, 'Semboyan negara Indonesia adalah ....', 'Bhinneka Tunggal Ika', ['Merdeka atau Mati', 'Berani Berbuat', 'Tut Wuri Handayani'])
f(1, 1, 'Bhinneka Tunggal Ika artinya ....', 'berbeda-beda tetapi tetap satu', ['semua sama', 'bersatu tidak boleh berbeda', 'berbeda lalu berpisah'])
f(1, 1, 'Semboyan Bhinneka Tunggal Ika tertulis pada pita yang dicengkeram oleh burung ....', 'Garuda', ['Elang Jawa', 'Merpati', 'Rajawali Putih'])
f(1, 1, 'Perbedaan di lingkungan kita harus ....', 'dihargai', ['dijauhi', 'diejek', 'dilarang'])
f(1, 1, 'Identitas diri di lingkungan rumah, sekolah, dan masyarakat ....', 'beragam', ['seragam', 'tidak ada', 'dilarang'])
f(1, 1, 'Teman yang bahasa daerahnya berbeda dari kita tetap ....', 'teman kita', ['musuh kita', 'orang asing', 'tidak boleh diajak bermain'])
s(1, 1, 'Dani suka bermain sepak bola, sedangkan Rafi suka menggambar. Hal ini menunjukkan perbedaan ....', 'Dani suka sepak bola dan Rafi suka menggambar. Hal itu menunjukkan perbedaan', 'hobi', ['nama', 'bahasa', 'agama'], 'Kesukaan kegiatan disebut hobi.', 'easy')
s(1, 1, 'Salma berbicara bahasa Sunda di rumah, Lani berbicara bahasa Jawa. Hal ini menunjukkan perbedaan ....', 'Salma berbahasa Sunda dan Lani berbahasa Jawa di rumah. Hal itu menunjukkan perbedaan', 'bahasa daerah', ['nama', 'hobi', 'jenis kelamin'], 'Bahasa daerah berbeda-beda.', 'easy')
s(1, 1, 'Di kelas ada murid laki-laki dan perempuan. Sikap yang baik adalah ....', 'Terhadap teman laki-laki maupun perempuan, kita', 'menghargai dan berteman dengan semuanya', ['hanya berteman dengan yang sama', 'mengejek yang berbeda', 'menjauhi yang berbeda'], 'Menghargai semua teman.', 'easy')
s(1, 1, 'Perhatikan gambar! Beberapa anak berpakaian berbeda-beda dan bermain bersama dengan gembira di halaman sekolah. Gambar ini menunjukkan ....', 'Gambar anak-anak berpakaian beragam bermain bersama menunjukkan', 'keberagaman yang tetap rukun', ['pertengkaran', 'kesedihan', 'kebosanan'], 'Berbeda tetapi rukun.', 'easy',
  'Enam anak dengan pakaian dan warna kulit beragam bermain bersama tertawa di halaman sekolah.')
T += [(1, 1, 'Semua orang harus memiliki hobi yang sama.', False, 'Hobi boleh berbeda.'), (1, 1, 'Bhinneka Tunggal Ika berarti berbeda-beda tetapi tetap satu.', True, 'Arti semboyan negara.'), (1, 1, 'Perbedaan identitas adalah alasan untuk bermusuhan.', False, 'Perbedaan harus dihargai.')]
P += [(1, 1, 'Sebutkan namamu, hobimu, dan bahasa yang kamu pakai di rumah!'), (1, 1, 'Ceritakan satu perbedaan antara dirimu dan temanmu dan satu persamaannya!')]
G += [(1, 1, "Kelompokkan contoh berikut: nama, sepak bola, bahasa Jawa, membaca, bahasa Sunda, menggambar.", {'hobi': ['sepak bola', 'membaca', 'menggambar'], 'bahasa daerah': ['bahasa Jawa', 'bahasa Sunda'], 'identitas lain': ['nama']}, 'Beragam identitas.')]

# TP2 identifikasi keberagaman
f(1, 2, 'Indonesia memiliki banyak suku bangsa, misalnya suku Jawa, Sunda, dan ....', 'Batak', ['Eskimo', 'Maori', 'Aborigin'])
f(1, 2, 'Rumah adat Joglo berasal dari suku ....', 'Jawa', ['Batak', 'Dayak', 'Papua'])
f(1, 2, 'Kain ulos berasal dari suku ....', 'Batak', ['Jawa', 'Bali', 'Sunda'])
f(1, 2, 'Kain batik terkenal berasal dari ....', 'Jawa', ['Papua', 'Eskimo', 'Mesir'])
f(1, 2, 'Pakaian, makanan, dan tarian daerah disebut ....', 'budaya daerah', ['peraturan', 'pelajaran', 'hukuman'])
f(1, 2, 'Agama yang dianut penduduk Indonesia ada .... agama resmi.', '6', ['2', '3', '10'], diff='medium')
f(1, 2, 'Agama yang beribadah di masjid adalah ....', 'Islam', ['Hindu', 'Buddha', 'Konghucu'])
f(1, 2, 'Orang yang beragama Islam menyebut Tuhan dengan nama ....', 'Allah', ['Brahman', 'Sang Buddha', 'Thian'], diff='medium')
f(1, 2, 'Agama Islam, Kristen, Katolik, Hindu, Buddha, dan Konghucu dianut oleh ....', 'rakyat Indonesia', ['rakyat satu daerah saja', 'hanya orang dewasa', 'hanya murid sekolah'])
f(1, 2, 'Lingkungan sekitar kita biasanya dihuni orang dengan .... yang beragam.', 'suku, budaya, dan agama', ['bentuk tangan', 'warna rumput', 'ukuran sepatu'])
s(1, 2, 'Perhatikan gambar! Rumah panggung tinggi dengan atap melengkung besar yang berada di Sumatera Barat. Rumah adat ini disebut ....', 'Gambar rumah panggung beratap melengkung dari Sumatera Barat menunjukkan rumah adat', 'Rumah Gadang', ['Joglo', 'Honai', 'Rumah Betang'], 'Rumah Gadang dari Sumatera Barat.', 'medium', 'Rumah panggung berukir dengan atap runcing melengkung seperti tanduk kerbau.')
s(1, 2, 'Perhatikan gambar! Sekelompok penari mengenakan pakaian adat menarikan tarian Bali di pura. Tarian itu berasal dari ....', 'Gambar penari memakai pakaian adat menarikan tarian di pura menunjukkan tarian dari', 'Bali', ['Aceh', 'Papua', 'Kalimantan'], 'Tari Pendet dari Bali.', 'medium', 'Beberapa penari berpakaian adat Bali menari di halaman pura.')
T += [(1, 2, 'Indonesia hanya memiliki satu suku bangsa.', False, 'Indonesia memiliki banyak suku.'), (1, 2, 'Rumah adat Joglo berasal dari Jawa Tengah.', True, 'Joglo dari Jawa.')]
P += [(1, 2, 'Sebutkan tiga suku bangsa dan satu ciri budayanya!'), (1, 2, 'Sebutkan enam agama yang ada di Indonesia!')]

# TP3 sikap menghargai
f(1, 3, 'Sikap saling menghormati perbedaan disebut ....', 'toleransi', ['egois', 'iri', 'sombong'])
f(1, 3, 'Orang yang bertoleransi akan ....', 'menghargai perbedaan', ['mengejek perbedaan', 'memusuhi teman', 'memaksa teman'])
f(1, 3, 'Teman berbeda agama saat merayakan hari rayanya, kita sebaiknya ....', 'menghormati dan tidak mengganggu', ['mengejek', 'mengganggu', 'melarang'])
f(1, 3, 'Teman berbeda suku yang kesulitan, kita sebaiknya ....', 'menolong dengan ikhlas', ['membiarkan', 'menertawakan', 'menjauhi'])
f(1, 3, 'Cinta kepada sesama manusia menunjukkan bahwa kita ....', 'mengasihi tanpa membedakan', ['pilih-pilih teman', 'suka bertengkar', 'iri hati'])
f(1, 3, 'Dalam Islam ada ajaran "Lakum dinukum waliyadin" yang artinya ....', 'untukmu agamamu dan untukku agamaku', ['semua agama sama', 'kita boleh memaksa', 'agama bisa ditukar'], diff='hard')
f(1, 3, 'Bermain bersama teman tanpa membedakan suku dan agama menunjukkan sikap ....', 'toleran dan rukun', ['sombong', 'bermusuhan', 'curang'])
f(1, 3, 'Berkata kasar kepada teman karena berbeda hobi adalah perbuatan ....', 'tidak baik', ['terpuji', 'benar', 'berani'])
f(1, 3, 'Mengucapkan terima kasih dengan bahasa daerah teman menunjukkan sikap ....', 'menghargai teman', ['meremehkan', 'mengejek', 'sombong'])
f(1, 3, 'Menjaga persatuan walaupun berbeda adalah pengamalan semboyan ....', 'Bhinneka Tunggal Ika', ['Tut Wuri Handayani', 'Berani Jujur', 'Ing Ngarsa Sung Tuladha'])
s(1, 3, 'Teman Rafi berbeda agama dan sedang beribadah. Sikap Rafi yang baik adalah ....', 'Saat temannya yang berbeda agama sedang beribadah, Rafi', 'tidak mengganggu dan menghormatinya', ['mengejeknya', 'mengganggunya', 'berisik di dekatnya'], 'Toleransi beragama.', 'easy')
s(1, 3, 'Ada murid baru dari daerah lain yang logat bicaranya berbeda. Sikap Salma adalah ....', 'Terhadap murid baru yang logatnya berbeda, Salma', 'mengajaknya berteman dan tidak menertawakan', ['menertawakan logatnya', 'menjauhinya', 'meniru untuk mengejek'], 'Menghargai perbedaan.', 'easy')
s(1, 3, 'Hasan tidak suka makanan khas daerah temannya, tetapi temannya menawarkan. Sikap Hasan yang sopan adalah ....', 'Saat ditawari makanan khas daerah temannya, Hasan', 'mengucap terima kasih dan menghargai tawarannya', ['mengejek makanan itu', 'membuang makanan itu', 'marah'], 'Menghargai budaya teman.', 'medium')
s(1, 3, 'Dini dan Lani berbeda suku, tetapi mereka mengerjakan tugas kelompok bersama. Hal ini menunjukkan ....', 'Dini dan Lani yang berbeda suku bekerja sama dengan baik, hal itu menunjukkan', 'persatuan dalam perbedaan', ['permusuhan', 'perbedaan yang memisahkan', 'ketidakpedulian'], 'Bhinneka Tunggal Ika.', 'medium')
s(1, 3, 'Perhatikan gambar! Anak-anak dari berbagai suku berpegangan tangan membentuk lingkaran di halaman. Gambar ini menunjukkan sikap ....', 'Gambar anak-anak berbagai suku berpegangan tangan menunjukkan sikap', 'toleransi dan persatuan', ['permusuhan', 'kesombongan', 'saling membenci'], 'Persatuan dalam perbedaan.', 'easy', 'Delapan anak berpakaian adat berbeda-beda berpegangan tangan membentuk lingkaran sambil tersenyum.')
s(1, 3, 'Perhatikan gambar! Dua anak saling menjabat tangan; satu berpeci dan satu mengenakan kalung salib kecil, keduanya tersenyum. Hal ini menunjukkan ....', 'Gambar dua anak berbeda agama saling menjabat tangan menunjukkan sikap', 'rukun dan saling menghormati', ['bermusuhan', 'sombong', 'acuh'], 'Toleransi beragama.', 'easy', 'Dua anak berseragam MI dan sekolah umum saling menjabat tangan di taman, wajah keduanya ceria.')
T += [(1, 3, 'Menghargai perbedaan adalah ajaran yang baik.', True, 'Toleransi.'), (1, 3, 'Kita boleh memilih teman hanya yang sama suku.', False, 'Kita berteman dengan siapa saja.')]
P += [(1, 3, 'Peragakan cara menyapa teman yang berbeda suku atau agama dengan ramah!'), (1, 3, 'Ceritakan bagaimana kamu berbuat baik kepada temanmu yang berbeda denganmu!')]

# ------------------------------------------------------------------ BAB 2 (selain tabel)
f(2, 1, 'Aturan di rumah dibuat agar ....', 'keluarga hidup tertib dan rukun', ['anak-anak sedih', 'orang tua senang menghukum', 'rumah sepi'])
f(2, 1, 'Orang yang membuat aturan di rumah biasanya ....', 'orang tua', ['tetangga', 'penjual', 'tamu'])
f(2, 1, 'Aturan dibuat untuk kebaikan ....', 'bersama', ['sebagian orang saja', 'orang tua saja', 'anak saja'])
f(2, 1, 'Rumah yang tidak punya aturan dapat menjadi ....', 'kacau dan tidak tertib', ['rapi', 'tenang', 'aman'])
f(2, 1, 'Menaati aturan keluarga adalah wujud ketaatan kepada ....', 'orang tua dan ajaran Islam', ['teman', 'tetangga', 'hewan'])
f(2, 1, 'Islam mengajarkan kita berbakti kepada ....', 'orang tua', ['siapa saja yang kuat', 'hanya guru', 'hanya teman'])
f(2, 1, 'Jika ingin mengubah aturan, kita harus ....', 'berbicara baik-baik dengan orang tua', ['melanggar diam-diam', 'marah-marah', 'melarikan diri'])
T += [(2, 1, 'Aturan di rumah dibuat untuk kebaikan seluruh anggota keluarga.', True, 'Aturan untuk kebaikan bersama.'), (2, 1, 'Aturan di rumah hanya untuk orang dewasa.', False, 'Semua anggota menaati aturan.')]
P += [(2, 1, 'Sebutkan tiga aturan di rumahmu dan manfaatnya!')]
f(2, 2, 'Anak yang menaati aturan akan disayang dan dipercaya oleh ....', 'orang tua', ['tidak ada', 'musuh', 'hewan'])
f(2, 2, 'Contoh perilaku tidak menaati aturan adalah ....', 'melanggar jam tidur', ['merapikan kamar', 'berpamitan', 'berkata jujur'])
f(2, 2, 'Jika melanggar aturan, anak yang baik akan ....', 'meminta maaf dan memperbaiki diri', ['menyalahkan orang lain', 'melarikan diri', 'berbohong'])
f(2, 2, 'Akibat melanggar aturan keluarga bisa berupa ....', 'teguran atau nasihat', ['hadiah', 'pujian', 'libur'], diff='medium')
T += [(2, 2, 'Menaati aturan adalah perilaku terpuji.', True, 'Taat aturan terpuji.'), (2, 2, 'Berbohong termasuk menaati aturan.', False, 'Berbohong melanggar aturan.')]
P += [(2, 2, 'Peragakan perilaku menaati dan tidak menaati aturan memakai drama kecil!')]
f(2, 3, 'Menaati aturan keluarga adalah bagian dari mengamalkan ajaran ....', 'Islam', ['bermain', 'berdagang', 'berpetualang'])
f(2, 3, 'Orang tua rida jika anaknya ....', 'taat dan berbakti', ['melawan', 'berbohong', 'malas'])
f(2, 3, 'Rida orang tua adalah bagian dari rida ....', 'Allah', ['teman', 'tetangga', 'guru'], diff='medium')
f(2, 3, 'Menaati aturan secara terus-menerus akan membentuk kebiasaan yang ....', 'baik', ['buruk', 'sia-sia', 'berbahaya'])
s(2, 3, 'Ibu berpesan agar tidak bermain gawai sebelum PR selesai. Rafi ....', 'Menaati pesan ibu agar tidak bermain gawai sebelum PR selesai, Rafi', 'menyelesaikan PR terlebih dahulu', ['bermain diam-diam', 'berbohong sudah selesai', 'marah'], 'Taat aturan keluarga.', 'medium')
s(2, 3, 'Ayah melarang Salma bermain hujan-hujanan karena sakit. Salma ....', 'Saat ayah melarang bermain hujan karena sakit, Salma', 'menurut dan bermain di dalam rumah', ['tetap keluar', 'menangis dan membantah', 'berpura-pura sehat'], 'Taat aturan demi kebaikan.', 'medium')
s(2, 3, 'Perhatikan gambar! Seorang anak berpamitan dan mencium tangan ibu sebelum berangkat sekolah. Sikap anak itu menunjukkan ....', 'Gambar anak berpamitan dan mencium tangan ibu menunjukkan sikap', 'menaati aturan dan menghormati orang tua', ['melanggar aturan', 'tidak peduli', 'sombong'], 'Berpamitan adalah aturan keluarga.', 'easy', 'Anak berseragam mencium tangan ibu di depan pintu sambil membawa tas.')
T += [(2, 3, 'Menaati aturan keluarga termasuk mengamalkan ajaran Islam untuk kebaikan bersama.', True, 'Taat membawa kebaikan.')]
P += [(2, 3, 'Ceritakan satu aturan keluarga yang paling kamu taati dan alasannya!'), (2, 3, 'Buatlah kartu "Aturan di Rumahku" dengan gambar dan tulisan!')]
O += [(2, 3, 'Urutkan kegiatan menaati aturan sebelum tidur berikut!', ['Merapikan mainan', 'Menggosok gigi', 'Berdoa sebelum tidur', 'Tidur tepat waktu'], 'Rutinitas sebelum tidur.')]

# ------------------------------------------------------------------ BAB 3
f(3, 1, 'Dasar negara Indonesia adalah ....', 'Pancasila', ['Bhinneka Tunggal Ika', 'Merah Putih', 'Garuda'])
f(3, 1, 'Jumlah sila dalam Pancasila adalah .... sila.', '5', ['3', '4', '10'])
f(3, 1, 'Lambang negara Indonesia adalah ....', 'Garuda Pancasila', ['Merah Putih', 'Indonesia Raya', 'Burung Merpati'])
f(3, 1, 'Burung yang menjadi lambang negara adalah burung ....', 'Garuda', ['Merpati', 'Elang', 'Gagak'])
f(3, 1, 'Perisai di dada Garuda berisi lambang sila-sila ....', 'Pancasila', ['Bhinneka', 'Pembukaan', 'Proklamasi'])
f(3, 1, 'Tulisan pada pita yang dicengkeram Garuda adalah ....', 'Bhinneka Tunggal Ika', ['Pancasila', 'Merdeka', 'Indonesia Raya'])
f(3, 1, 'Bendera negara Indonesia berwarna ....', 'merah dan putih', ['merah dan hijau', 'putih dan biru', 'kuning dan merah'])
f(3, 1, 'Bendera Merah Putih bagian atas berwarna ....', 'merah', ['putih', 'biru', 'kuning'])
f(3, 1, 'Warna merah pada bendera berarti ....', 'berani', ['sedih', 'takut', 'malas'])
f(3, 1, 'Warna putih pada bendera berarti ....', 'suci', ['marah', 'kotor', 'takut'])
f(3, 1, 'Lagu kebangsaan Indonesia adalah ....', 'Indonesia Raya', ['Garuda Pancasila', 'Halo-Halo Bandung', 'Rayuan Pulau Kelapa'], diff='medium')
f(3, 1, 'Pencipta lagu Indonesia Raya adalah ....', 'W.R. Supratman', ['Ismail Marzuki', 'Ibu Sud', 'Kusbini'], diff='hard')
f(3, 1, 'Perisai pada Garuda ditempatkan di bagian ....', 'dada', ['kepala', 'kaki', 'sayap'])
f(3, 1, 'Burung Garuda mencengkeram pita dengan ....', 'kedua kakinya', ['paruhnya', 'sayapnya', 'ekornya'])
s(3, 1, 'Perhatikan gambar! Lambang burung bermahkota perisai di dada dengan lima gambar. Lambang itu disebut ....', 'Gambar burung bermahkota dengan perisai di dada menunjukkan lambang', 'Garuda Pancasila', ['bendera Merah Putih', 'peta Indonesia', 'logo sekolah'], 'Lambang negara Garuda Pancasila.', 'easy', 'Burung Garuda keemasan dengan perisai di dada bertuliskan lima lambang dan pita putih di cakarnya.')
s(3, 1, 'Perhatikan gambar! Dua warna bendera: merah di atas dan putih di bawah, berkibar di tiang. Bendera itu adalah bendera ....', 'Gambar bendera merah di atas dan putih di bawah menunjukkan bendera', 'Merah Putih', ['Biru Putih', 'Hijau Putih', 'Kuning Merah'], 'Bendera negara Merah Putih.', 'easy', 'Bendera dua warna berkibar di tiang tinggi di halaman sekolah.')
T += [(3, 1, 'Pancasila terdiri atas lima sila.', True, 'Lima sila.'), (3, 1, 'Pancasila adalah nama lagu kebangsaan.', False, 'Lagu kebangsaan: Indonesia Raya.')]
O += [(3, 1, 'Urutkan sila-sila Pancasila dari sila pertama berdasarkan lambangnya!', ['bintang', 'rantai', 'pohon beringin', 'kepala banteng', 'padi dan kapas'], 'Lambang sila 1 sampai 5.'),
      (3, 1, 'Urutkan tiga sila pertama Pancasila!', ['Ketuhanan Yang Maha Esa', 'Kemanusiaan yang adil dan beradab', 'Persatuan Indonesia'], 'Sila 1, 2, dan 3.')]
P += [(3, 1, 'Sebutkan lima sila Pancasila secara berurutan!'), (3, 1, 'Tunjukkan lambang tiap sila pada lambang Garuda Pancasila yang diperlihatkan gurumu!')]
f(3, 2, 'Sila pertama mengajarkan kita untuk ....', 'beribadah sesuai agama dan menghormati pemeluk agama lain', ['bermain terus', 'memilih teman', 'berbuat curang'])
f(3, 2, 'Sila kedua mengajarkan sikap ....', 'adil dan beradab kepada sesama', ['egois', 'kasar', 'curang'])
f(3, 2, 'Sila ketiga mengajarkan pentingnya ....', 'persatuan', ['perpecahan', 'permusuhan', 'kemalasan'])
f(3, 2, 'Sila keempat mengajarkan cara mengambil keputusan dengan ....', 'musyawarah', ['paksaan', 'undian curang', 'kemauan sendiri'])
f(3, 2, 'Sila kelima mengajarkan agar kita ....', 'berbuat adil dan berbagi', ['pilih kasih', 'serakah', 'iri'])
f(3, 2, 'Musyawarah artinya ....', 'berunding bersama untuk mufakat', ['memaksakan kehendak', 'bertengkar', 'berlomba'])
f(3, 2, 'Pancasila menjadi dasar negara agar rakyat Indonesia hidup ....', 'rukun dan bersatu', ['terpecah', 'bermusuhan', 'tidak teratur'])
f(3, 2, 'Sikap menghormati pemeluk agama lain sesuai dengan sila ke- ....', '1', ['2', '4', '5'], diff='medium')
f(3, 2, 'Sikap gotong royong sesuai dengan sila ke- ....', '3', ['1', '2', '4'], diff='medium')
f(3, 2, 'Sikap berbagi secara adil sesuai dengan sila ke- ....', '5', ['1', '2', '3'], diff='medium')
T += [(3, 2, 'Sila keempat mengajarkan musyawarah.', True, 'Sila 4 = musyawarah.'), (3, 2, 'Sila ketiga mengajarkan sikap bermusuhan.', False, 'Sila 3 = persatuan.')]
P += [(3, 2, 'Jelaskan makna salah satu sila Pancasila dengan bahasamu sendiri!')]
f(3, 3, 'Contoh pengamalan sila pertama di keluarga adalah ....', 'beribadah dan berdoa bersama', ['bertengkar', 'berebut mainan', 'membentak'])
f(3, 3, 'Keluarga yang bermusyawarah saat menentukan tempat liburan mengamalkan sila ke- ....', '4', ['1', '2', '5'])
f(3, 3, 'Keluarga yang saling menyayangi mengamalkan sila ke- ....', '2', ['1', '4', '5'])
s(3, 3, 'Ayah, ibu, dan anak berembuk menentukan menu makan malam dan menyepakati bersama. Hal ini sesuai sila ke- ....', 'Keluarga berembuk menentukan menu dan menyepakati bersama. Hal itu sesuai sila ke', '4', ['1', '2', '3'], 'Musyawarah keluarga.', 'medium')
s(3, 3, 'Kakak dan adik berbagi roti sama besar. Sikap mereka sesuai dengan sila ke- ....', 'Kakak dan adik membagi roti sama besar. Sikap itu sesuai sila ke', '5', ['1', '2', '4'], 'Berbagi adil.', 'medium')
s(3, 3, 'Perhatikan gambar! Satu keluarga duduk di atas sajadah salat berjemaah di rumah. Hal ini sesuai dengan sila ke- ....', 'Gambar keluarga salat berjemaah di rumah sesuai dengan sila ke', '1', ['2', '3', '5'], 'Ibadah bersama = sila 1.', 'easy', 'Ayah di depan, ibu dan dua anak di belakang, salat berjemaah di ruang tamu.')
T += [(3, 3, 'Nilai-nilai Pancasila dapat diamalkan mulai dari keluarga.', True, 'Mulai dari keluarga.')]
P += [(3, 3, 'Ceritakan satu kegiatan keluargamu yang sesuai dengan sila tertentu!')]
f(3, 4, 'Wujud cinta tanah air adalah ....', 'menghormati bendera dan menyanyikan lagu kebangsaan dengan baik', ['mengejek bendera', 'merusak fasilitas umum', 'membuang sampah di jalan'])
f(3, 4, 'Upacara bendera biasanya dilakukan pada hari ....', 'Senin', ['Sabtu', 'Minggu', 'Rabu'])
f(3, 4, 'Saat upacara kita berdiri ....', 'tegak dan tertib', ['bergerak sembarangan', 'berbicara keras', 'berlarian'])
f(3, 4, 'Saat lagu Indonesia Raya dinyanyikan kita bersikap ....', 'sempurna dan khidmat', ['bermain', 'berbicara', 'tertawa'])
f(3, 4, 'Hari Kemerdekaan Indonesia diperingati setiap tanggal ....', '17 Agustus', ['1 Januari', '10 November', '2 Mei'])
f(3, 4, 'Bangsa Indonesia merdeka pada tahun ....', '1945', ['1945 Masehi hanya di Jakarta', '1950', '1900'], diff='hard') if False else None
f(3, 4, 'Kita mencintai tanah air dengan menjaga ....', 'kebersihan dan kerukunan', ['sampah', 'perselisihan', 'kerusakan'])
f(3, 4, 'Mencintai tanah air sejalan dengan ajaran Islam karena ....', 'menjaga negeri adalah bagian dari kebaikan', ['harus membenci negeri lain', 'tidak perlu peduli', 'hanya orang dewasa yang peduli'], diff='hard')
f(3, 4, 'Bendera Merah Putih sebaiknya dikibarkan dalam keadaan ....', 'bersih dan terhormat', ['robek dan kotor', 'terbalik', 'tergeletak di tanah'])
f(3, 4, 'Memakai produk buatan dalam negeri adalah wujud ....', 'cinta tanah air', ['kebencian', 'kemalasan', 'kesombongan'])
s(3, 4, 'Saat upacara bendera, Rafi berdiri tegak dan tidak bercanda. Sikap Rafi menunjukkan ....', 'Berdiri tegak dan tidak bercanda saat upacara, Rafi menunjukkan sikap', 'hormat kepada bendera dan cinta tanah air', ['tidak peduli', 'malas', 'sombong'], 'Cinta tanah air.', 'easy')
s(3, 4, 'Dina menemukan bendera kecil terjatuh di tanah. Sikap Dina adalah ....', 'Menemukan bendera kecil terjatuh di tanah, Dina', 'memungutnya dan merapikannya dengan hormat', ['menginjaknya', 'membiarkannya', 'membuangnya'], 'Menghormati bendera.', 'easy')
s(3, 4, 'Perhatikan gambar! Murid-murid berdiri tegak menghadap tiang bendera sambil memberi hormat. Kegiatan ini adalah ....', 'Gambar murid berdiri tegak memberi hormat kepada bendera menunjukkan kegiatan', 'upacara bendera', ['kerja bakti', 'olahraga', 'kegiatan makan'], 'Upacara bendera.', 'easy', 'Barisan murid berseragam merah putih menghadap tiang bendera, tangan kanan hormat.')
T += [(3, 4, 'Menyanyikan lagu Indonesia Raya dengan khidmat adalah wujud cinta tanah air.', True, 'Cinta tanah air.'), (3, 4, 'Mencoret fasilitas umum adalah wujud cinta tanah air.', False, 'Itu merusak.')]
P += [(3, 4, 'Peragakan sikap sempurna saat menyanyikan lagu Indonesia Raya!'), (3, 4, 'Ceritakan bagaimana kamu menunjukkan cinta tanah air di sekolah!')]

# ------------------------------------------------------------------ BAB 4
f(4, 1, 'Tempat tinggal kita termasuk wilayah negara ....', 'Kesatuan Republik Indonesia', ['Malaysia', 'Singapura', 'Jepang'])
f(4, 1, 'Lingkungan rumah terdiri atas rumah, halaman, tetangga, dan ....', 'jalan di sekitar rumah', ['bulan', 'matahari', 'laut dalam'])
f(4, 1, 'Orang yang tinggal di dekat rumah kita disebut ....', 'tetangga', ['tamu', 'penjual', 'teman sekolah'])
f(4, 1, 'Lingkungan yang bersih dan rindang disebut lingkungan ....', 'sehat dan asri', ['kotor', 'bising', 'gersang'])
f(4, 1, 'Lingkungan rumah dihuni oleh orang dengan suku dan agama yang ....', 'beragam', ['sama semua', 'tidak ada', 'tidak boleh'])
f(4, 1, 'Wilayah Indonesia terdiri atas banyak ....', 'pulau', ['gunung saja', 'sungai saja', 'padang pasir'])
f(4, 1, 'Lingkungan rumah yang kotor dapat menyebabkan ....', 'penyakit', ['kesehatan', 'kegembiraan', 'keamanan'])
f(4, 1, 'Pohon di halaman membuat lingkungan menjadi ....', 'sejuk', ['panas', 'kotor', 'bising'])
s(4, 1, 'Perhatikan gambar! Rumah dengan halaman berpagar, pohon mangga, jalan kecil, dan rumah tetangga di sebelahnya. Gambar ini menunjukkan ....', 'Gambar rumah berhalaman, pohon, jalan, dan rumah tetangga menunjukkan', 'lingkungan rumah', ['lingkungan sekolah', 'lingkungan pasar', 'lingkungan hutan'], 'Lingkungan rumah.', 'easy', 'Rumah sederhana berpagar rendah, pohon mangga di halaman, jalan gang dan rumah tetangga di sebelahnya.')
s(4, 1, 'Perhatikan gambar! Sebuah gang yang bersih dengan tanaman di pot di depan rumah-rumah. Lingkungan seperti ini disebut ....', 'Gambar gang bersih dengan tanaman di pot menunjukkan lingkungan', 'bersih dan asri', ['kotor', 'gersang', 'berbahaya'], 'Bersih dan asri.', 'easy', 'Gang sempit bersih dengan pot bunga di depan setiap rumah.')
T += [(4, 1, 'Lingkungan rumah kita adalah bagian dari wilayah Negara Kesatuan Republik Indonesia.', True, 'Wilayah NKRI.'), (4, 1, 'Lingkungan rumah terdiri atas rumah saja.', False, 'Termasuk halaman, jalan, tetangga.')]
P += [(4, 1, 'Gambarlah lingkungan rumahmu dan sebutkan benda-benda yang ada!'), (4, 1, 'Ceritakan ciri lingkungan rumahmu: bersih atau kotor, ramai atau tenang!')]
f(4, 2, 'Bekerja sama membersihkan lingkungan disebut ....', 'gotong royong', ['bermain', 'berlomba', 'bertengkar'])
f(4, 2, 'Kerja sama membuat pekerjaan menjadi ....', 'ringan dan cepat selesai', ['berat', 'lama', 'sulit'])
f(4, 2, 'Kerja bakti dilakukan oleh ....', 'warga bersama-sama', ['satu orang', 'hewan', 'tamu'])
f(4, 2, 'Anak kecil dapat ikut kerja sama dengan ....', 'tugas yang ringan', ['tugas berbahaya', 'tidak ikut', 'mengganggu'])
f(4, 2, 'Kerja sama dalam keberagaman berarti kita bekerja sama walaupun ....', 'berbeda suku dan agama', ['sama suku', 'sama agama', 'sama kelas'])
f(4, 2, 'Dalam kerja bakti, ada yang menyapu, ada yang memungut sampah. Hal ini menunjukkan ....', 'pembagian tugas', ['persaingan', 'perpecahan', 'kekacauan'])
T += [(4, 2, 'Gotong royong adalah bekerja sama dengan ikhlas.', True, 'Gotong royong.'), (4, 2, 'Kerja sama membuat pekerjaan jadi lebih berat.', False, 'Kerja sama meringankan.')]
P += [(4, 2, 'Sebutkan tiga bentuk kerja sama di lingkungan rumahmu!'), (4, 2, 'Ceritakan kegiatan kerja bakti yang pernah kamu ikuti!')]
f(4, 3, 'Menjaga lingkungan termasuk bagian dari iman karena ....', 'kebersihan sebagian dari iman', ['tidak ada hubungannya', 'hanya aturan sekolah', 'merepotkan'])
f(4, 3, 'Sampah plastik sebaiknya ....', 'dikumpulkan dan didaur ulang', ['dibakar', 'dibuang ke sungai', 'ditanam di kebun'])
f(4, 3, 'Daun kering sebaiknya dijadikan ....', 'kompos', ['asap', 'sampah di jalan', 'bahan bakar plastik'])
f(4, 3, 'Air yang mengalir dari keran harus ....', 'dihemat', ['dibuang', 'dibiarkan', 'diperebutkan'])
s(4, 3, 'Perhatikan gambar! Seorang anak menyiram tanaman di halaman rumah dengan gembor. Perilaku ini menunjukkan ....', 'Gambar anak menyiram tanaman di halaman menunjukkan perilaku', 'merawat lingkungan', ['merusak lingkungan', 'malas', 'tidak peduli'], 'Merawat tanaman.', 'easy', 'Anak perempuan menyiram bunga di halaman dengan gembor, halaman rapi dan hijau.')
s(4, 3, 'Perhatikan gambar! Seorang anak membuang sampah plastik ke tong biru, sementara tong hijau untuk sisa makanan. Perilaku ini menunjukkan ....', 'Gambar anak memilah sampah ke dua tong menunjukkan perilaku', 'memilah sampah', ['membuang sampah sembarangan', 'mencampur sampah', 'membakar sampah'], 'Memilah sampah.', 'easy', 'Dua tong sampah (hijau dan biru) dengan anak yang memasukkan botol plastik ke tong biru.')
T += [(4, 3, 'Membuang sampah ke sungai menjaga kebersihan lingkungan.', False, 'Itu mencemari sungai.'), (4, 3, 'Menjaga lingkungan rumah adalah kewajiban semua anggota keluarga.', True, 'Tugas bersama.')]
P += [(4, 3, 'Peragakan cara memilah sampah organik dan anorganik!'), (4, 3, 'Ceritakan satu cara kamu menjaga lingkungan rumahmu!')]
f(4, 4, 'Kerja sama dalam menjaga lingkungan dilakukan dengan penuh ....', 'kepedulian dan kebersamaan', ['paksaan', 'permusuhan', 'kemalasan'])
f(4, 4, 'Peduli kepada lingkungan berarti kita ....', 'ikut menjaga dan merawatnya', ['merusaknya', 'mengabaikannya', 'mengotorinya'])
f(4, 4, 'Mengajak tetangga ikut membersihkan lingkungan menunjukkan sikap ....', 'peduli dan bekerja sama', ['sombong', 'pelit', 'acuh'])
f(4, 4, 'Mengucap hamdalah setelah kerja bakti selesai menunjukkan rasa ....', 'syukur', ['marah', 'sombong', 'malas'])
s(4, 4, 'Perhatikan gambar! Warga dari berbagai suku bekerja sama menyapu jalan dan membersihkan selokan. Gambar ini menunjukkan ....', 'Gambar warga berbagai suku bergotong royong membersihkan jalan menunjukkan', 'kerja sama dalam keberagaman', ['permusuhan', 'kemalasan', 'persaingan'], 'Gotong royong dalam keberagaman.', 'easy', 'Warga berpakaian beragam menyapu jalan, mengangkat sampah, dan membersihkan selokan bersama.')
T += [(4, 4, 'Kerja sama menjaga lingkungan dilakukan dengan kepedulian dan kebersamaan.', True, 'Peduli dan bersama.')]
P += [(4, 4, 'Ajak temanmu membersihkan halaman sekolah dan ceritakan pembagian tugas kalian!'), (4, 4, 'Buat daftar kegiatan gotong royong yang bisa kamu lakukan minggu ini!')]

# ------------------------------------------------------------------ tambahan skenario
s(3, 4, 'Hari Senin Fikri tiba tepat ketika upacara akan dimulai. Sikap yang baik adalah ....', 'Saat upacara akan dimulai, Fikri', 'segera masuk barisan dengan tertib', ['membuat gaduh', 'bermain di belakang barisan', 'pura-pura sakit'], 'Tertib saat upacara.', 'easy')
s(3, 4, 'Adik kecil Rafi menggunakan bendera mainan sebagai alas duduk. Rafi sebaiknya ....', 'Melihat adiknya memakai bendera mainan sebagai alas duduk, Rafi', 'mengingatkan dengan lembut bahwa bendera harus dihormati', ['membiarkannya', 'menertawakannya', 'ikut menginjaknya'], 'Menghormati bendera.', 'medium')
s(3, 4, 'Sekolah mengadakan lomba 17 Agustus. Sikap Salma adalah ....', 'Mengikuti lomba 17 Agustus, Salma', 'ikut dengan semangat dan bersikap sportif', ['curang agar menang', 'mengejek lawan', 'tidak mau ikut'], 'Memeriahkan hari kemerdekaan dengan sportif.', 'easy')
s(3, 4, 'Dini memakai baju batik pada hari yang ditentukan sekolah. Hal itu menunjukkan ....', 'Memakai baju batik pada hari yang ditentukan, Dini menunjukkan', 'cinta budaya bangsa', ['kebencian', 'kemalasan', 'ketidakpedulian'], 'Cinta budaya.', 'medium')
s(3, 4, 'Hasan lebih suka membeli jajanan buatan pedagang di sekitar rumahnya. Hal itu menunjukkan ....', 'Memilih jajanan buatan pedagang sekitar, Hasan menunjukkan sikap', 'mencintai produk dalam negeri', ['membenci pedagang', 'boros', 'sombong'], 'Mencintai produk lokal.', 'medium')
s(3, 4, 'Lani bermain di taman kota yang indah. Sikap Lani yang mencintai tanah air adalah ....', 'Saat bermain di taman kota, Lani', 'menjaga kebersihan dan tidak mencoret fasilitas', ['mencoret bangku taman', 'membuang bungkus sembarangan', 'mematahkan tanaman'], 'Menjaga fasilitas umum.', 'easy')
s(3, 4, 'Zaki mengajari adiknya menyanyikan lagu Indonesia Raya. Sikap Zaki menunjukkan ....', 'Mengajari adik menyanyikan lagu Indonesia Raya, Zaki menunjukkan', 'cinta tanah air', ['kemalasan', 'kesombongan', 'ketidakpedulian'], 'Cinta tanah air.', 'easy')
s(4, 4, 'Warga sedang kerja bakti membersihkan lingkungan. Rafi ....', 'Saat warga kerja bakti, Rafi', 'membawa sapu dan ikut membantu', ['bermain gawai', 'menonton saja', 'pulang tanpa pamit'], 'Ikut kerja bakti.', 'easy')
s(4, 4, 'Selokan di depan rumah tersumbat sampah. Dina ....', 'Melihat selokan tersumbat sampah, Dina', 'memberi tahu orang dewasa dan mengajak teman membersihkannya bersama', ['membiarkan saja', 'menambah sampah', 'memarahi tetangga'], 'Peduli dan bekerja sama.', 'medium')
s(4, 4, 'Tetangga Hana sedang sakit. Hana ....', 'Mengetahui tetangganya sakit, Hana', 'mengantar makanan bersama ibunya dan mendoakan', ['menertawakannya', 'tidak peduli', 'bermain keras di depan rumahnya'], 'Peduli tetangga.', 'easy')
s(4, 4, 'Pak RT mengajak warga menanam pohon. Alif ....', 'Diajak menanam pohon oleh Pak RT, Alif', 'membantu membawa bibit dan menyiram', ['menolak ikut', 'mencabut bibit', 'bermain di tempat lain'], 'Ikut menanam pohon.', 'easy')
s(4, 4, 'Dalam lomba kebersihan antar-RT, anak-anak membagi tugas. Sikap Bima yang baik adalah ....', 'Saat ada pembagian tugas lomba kebersihan, Bima', 'melaksanakan tugasnya dengan penuh tanggung jawab', ['memilih tugas termudah saja', 'mengganggu teman', 'pergi bermain'], 'Tanggung jawab dalam kerja sama.', 'medium')
s(4, 4, 'Lani melihat anak kecil membuang sampah sembarangan. Lani ....', 'Melihat anak kecil membuang sampah sembarangan, Lani', 'mengingatkan dengan lembut dan memberi contoh membuang sampah di tempatnya', ['memarahinya dengan kasar', 'ikut membuang sampah', 'diam saja'], 'Saling mengingatkan dengan baik.', 'medium')
s(1, 3, 'Murid baru bernama Alif dari Papua sedang diperkenalkan oleh guru. Sikap yang baik adalah ....', 'Saat Alif dari Papua diperkenalkan, teman-teman', 'menyambutnya dengan ramah', ['mengejeknya', 'menjauhinya', 'acuh tak acuh'], 'Menghargai teman dari daerah lain.', 'easy')
s(1, 3, 'Fikri melihat teman yang berbeda agama sedang merayakan hari raya. Fikri ....', 'Melihat temannya merayakan hari raya agamanya, Fikri', 'mengucapkan selamat dengan sopan dan menghormati', ['mengejek', 'mengganggu', 'memaksa temannya ikut agama Fikri'], 'Toleransi.', 'medium')
s(1, 3, 'Dua temanmu berbeda hobi dan berebut ingin diikuti. Kamu sebaiknya ....', 'Melihat dua temannya berebut ingin diikuti, Salma', 'mengajak bermain bergantian sesuai hobi masing-masing', ['memihak salah satu', 'memarahi keduanya', 'meninggalkan keduanya'], 'Menghargai perbedaan hobi.', 'medium')
s(1, 3, 'Seorang teman berbicara dengan bahasa daerah saat berbicara dengan temannya. Hasan ....', 'Mendengar temannya berbicara dalam bahasa daerah, Hasan', 'menghargainya dan bertanya artinya dengan sopan', ['menertawakannya', 'melarangnya', 'meniru untuk mengejek'], 'Menghargai bahasa daerah.', 'medium')
s(1, 3, 'Ada kegiatan membawa makanan khas daerah ke sekolah. Dina ....', 'Saat ada kegiatan membawa makanan khas daerah, Dina', 'membawa makanan khas daerahnya dan mencicipi milik teman', ['mengejek makanan teman', 'tidak mau mencoba', 'menyembunyikan bawaannya'], 'Menghargai budaya.', 'easy')
s(1, 3, 'Dua kelompok bermain beranggotakan anak dari suku berbeda. Rafi ....', 'Dalam bermain bersama anak dari berbagai suku, Rafi', 'bermain dengan adil dan rukun', ['memilih yang sesuku saja', 'berkata kasar', 'curang'], 'Rukun dalam keberagaman.', 'easy')
