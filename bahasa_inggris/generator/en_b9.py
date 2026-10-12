# -*- coding: utf-8 -*-
from en_gen import *

PLAY = [('ayunan', 'swing', 'seorang anak duduk di atas ayunan'), ('perosotan', 'slide', 'seorang anak meluncur di perosotan'), ('jungkat-jungkit', 'seesaw', 'dua anak naik jungkat-jungkit'),
        ('bak pasir', 'sandbox', 'anak bermain di bak pasir dengan sekop'), ('tali lompat', 'jump rope', 'seorang anak melompati tali'), ('panjatan besi', 'monkey bars', 'anak bergelantungan di panjatan besi'),
        ('komidi putar', 'merry-go-round', 'beberapa anak naik komidi putar'), ('tangga', 'ladder', 'seorang anak naik tangga perosotan')]
ACTS = [('berayun di ayunan', 'Swing on the swing.'), ('meluncur di perosotan', 'Slide down the slide.'), ('memanjat tangga', 'Climb the ladder.'), ('melompati tali', 'Jump the rope.'),
        ('menendang bola', 'Kick the ball.'), ('berlari ke pohon', 'Run to the tree.'), ('melempar bola', 'Throw the ball.'), ('menggali pasir', 'Dig in the sand.')]
VERB = [('tali lompat', 'jump'), ('ayunan', 'swing'), ('perosotan', 'slide'), ('bola sepak', 'kick'), ('panjatan besi', 'climb'), ('bak pasir', 'dig'), ('lomba lari', 'run'), ('bola lempar', 'throw'), ('jungkat-jungkit', 'ride')]
REQ = [('meminta izin bermain ayunan', 'Can I play on the swing?'), ('mengajak teman bermain bersama', 'Let us play together.'), ('meminta teman mendorong ayunanmu', 'Can you push me?'),
       ('meminta bergabung bermain', 'May I join you?'), ('mengajak temanmu bermain denganmu', 'Can I play with you?'), ('menjawab dengan setuju', 'Yes, of course.'),
       ('mengingatkan teman menunggu giliran', 'Wait for your turn.'), ('menawarkan giliran kepada teman', 'It is your turn.')]
PC = [('Dina sedang berayun', 'Dina is swinging.'), ('Rafi sedang meluncur', 'Rafi is sliding.'), ('Aku sedang melompat tali', 'I am jumping rope.'), ('Mereka sedang berlari', 'They are running.'),
      ('Kami sedang bermain bola', 'We are playing ball.'), ('Fikri sedang memanjat', 'Fikri is climbing.'), ('Salma sedang menggali pasir', 'Salma is digging in the sand.'), ('Mereka sedang bermain jungkat-jungkit', 'They are playing on the seesaw.')]
ING = [('swing', 'berayun', 'swinging'), ('slide', 'meluncur', 'sliding'), ('run', 'berlari', 'running'), ('jump', 'melompat', 'jumping'), ('climb', 'memanjat', 'climbing'), ('dig', 'menggali', 'digging'), ('kick', 'menendang', 'kicking'), ('throw', 'melempar', 'throwing')]


def b9(p):
    c = 'Mengenal permainan di taman bermain'
    kv(p, 1, [(i, e) for i, e, _ in PLAY], "Dalam Bahasa Inggris, {k} adalah '{v}'.", "Kata '{v}' berarti ....", c, 'pl', 1)
    vis(p, 1, [(e, d) for _, e, d in PLAY], 'Perhatikan gambar! Gambar menunjukkan {d}. Dalam Bahasa Inggris permainan itu disebut ....', c, 'vp', pool=['bookshelf', 'kitchen'])
    kv(p, 2, ACTS, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Instruksi '{v}' artinya ....", 'Tindakan di taman bermain', 'ac', 2)
    kv(p, 3, VERB, "Kata kerja yang tepat untuk {k} adalah '{v}'.", "Kata kerja '{v}' cocok untuk ....", 'Kata kerja dan permainan', 'vb', 3, match=False)
    kv(p, 4, REQ, "Untuk {k}, kamu berkata '{v}'", "Ungkapan '{v}' dipakai untuk ....", 'Meminta untuk bermain', 'rq', 4)
    kv(p, 5, PC, "Dalam Bahasa Inggris, '{k}' adalah '{v}'", "Kalimat '{v}' artinya ....", 'Present continuous di taman bermain', 'pc', 5)
    kv(p, 5, [(v, ing) for v, idn, ing in ING], "Bentuk -ing dari kata kerja '{k}' adalah '{v}'.", "'{v}' adalah bentuk -ing dari kata kerja ....", 'Present continuous di taman bermain', 'ig', 6, match=False)
    vis(p, 5, [(f'He is {ing}.', f'seorang anak laki-laki sedang {idn}') for v, idn, ing in ING], 'Perhatikan gambar! Gambar menunjukkan {d}. Kalimat yang tepat adalah ....', 'Present continuous di taman bermain', 'vi', pool=['He is sleeping.', 'He is eating.'])
    scr(p, 6, [e for _, e, _ in PLAY if ' ' not in e and '-' not in e] + ['swing', 'slide', 'jump', 'climb', 'play', 'run', 'kick', 'throw'], 'Menulis kosakata', 'w9', 9)
    sent(p, 6, [('I am playing on the swing.', 'aku sedang bermain ayunan'), ('Dina is sliding.', 'Dina sedang meluncur'), ('We are jumping rope.', 'kami sedang melompat tali'), ('They are running.', 'mereka sedang berlari'),
                ('Rafi is climbing the ladder.', 'Rafi sedang memanjat tangga'), ('I am digging in the sandbox.', 'aku sedang menggali di bak pasir'), ('Can I play on the swing?', 'bolehkah aku bermain ayunan'), ('Let us play together.', 'ayo bermain bersama')], 'Menulis kalimat di taman bermain', 's9', 9)
    for v, idn, ing in ING:
        sq(p, 5, f'Perhatikan gambar! Seorang anak sedang {idn} di taman bermain. Teman bertanya, "What are you doing?" Anak itu menjawab ....', f'Ditanya "What are you doing?" saat sedang {idn}, anak menjawab', f'I am {ing}',
           [f'I {x}' for x in ['sleep', 'eat', 'read'] ] , f'Present continuous: I am {ing}.', 'medium', vis=f'Seorang anak sedang {idn} di taman bermain sementara temannya bertanya.', comp='Present continuous di taman bermain')
    for i, e, d in PLAY[:6]:
        sq(p, 4, f'Kamu ingin bermain {i} tetapi sudah ada temanmu di sana. Kamu berkata ....', f'Untuk meminta bergabung bermain {i}, kamu berkata', 'May I join you?', ['Go away!', 'It is my turn now, move!', 'Goodbye, see you'], 'Meminta dengan sopan.', 'easy', comp='Meminta untuk bermain') if e in ('swing', 'slide', 'seesaw') else None
    sq(p, 4, 'Temanmu bertanya, "Can I play with you?" Kamu setuju. Jawabanmu ....', 'Jika setuju diajak bermain, kamu menjawab', 'Yes, of course', ['No, go away', 'Goodbye, friend', 'Open the door'], 'Menerima ajakan.', 'easy', comp='Meminta untuk bermain')
    sq(p, 4, 'Antrean ayunan panjang. Kamu ingin mengingatkan temanmu agar menunggu giliran. Kamu berkata ....', 'Untuk mengingatkan teman menunggu giliran, kamu berkata', 'Wait for your turn, please', ['Push me now', 'Go away', 'I do not like you'], 'Menunggu giliran.', 'medium', comp='Meminta untuk bermain')
    sq(p, 3, 'Guru berkata, "Let us ... the rope." Kata kerja yang tepat untuk tali lompat adalah ....', 'Kata kerja yang tepat pada "Let us ... the rope" adalah', 'jump', ['swing', 'dig', 'slide'], 'Jump the rope.', 'easy', comp='Kata kerja dan permainan')
    sq(p, 3, 'Anak-anak bermain di bak pasir dengan sekop. Kata kerja yang tepat adalah ....', 'Di bak pasir dengan sekop, kata kerja yang tepat adalah', 'dig', ['swing', 'climb', 'slide'], 'Dig in the sand.', 'easy', comp='Kata kerja dan permainan')
    sq(p, 3, 'Anak-anak bergelantungan di panjatan besi. Kata kerja yang tepat adalah ....', 'Di panjatan besi, kata kerja yang tepat adalah', 'climb', ['kick', 'dig', 'throw'], 'Climb the monkey bars.', 'medium', comp='Kata kerja dan permainan')
    for i, e, d in PLAY[:5]:
        p.perf(1, f"Tunjuk gambar '{e}' di taman bermain lalu ucapkan namanya dalam Bahasa Inggris!", R, 'Murid menyebutkan dengan tepat.', 'medium', 'menerapkan', 'Praktik berbicara')
    for cmd, _ in ACTS[:6]:
        p.perf(2, f"Peragakan perintah ini: '{cmd}'", R, 'Murid memeragakan dengan tepat.', 'medium', 'menerapkan', 'Tindakan di taman bermain')
    for s, e in REQ[:4]:
        p.perf(4, f"Bermain peran: ucapkan '{e}' kepada temanmu!", R, 'Murid mengucapkan dengan sopan.', 'medium', 'menerapkan', 'Meminta untuk bermain')
    for s, e in PC[:5]:
        p.perf(5, f"Peragakan gerakan lalu ucapkan '{e}'", R, 'Murid memeragakan dan mengucapkan.', 'medium', 'menerapkan', 'Present continuous di taman bermain')
    p.group(1, 'Kelompokkan: swing; sandbox; slide; ladder; seesaw; jump rope menurut tempat bermain yang memakai pasir atau tidak.', {'memakai pasir': ['sandbox'], 'tidak memakai pasir': ['swing', 'slide', 'ladder', 'seesaw', 'jump rope']}, 'Bak pasir.', 'medium', 'mengelompokkan', c)
    p.group(5, 'Kelompokkan kalimat berikut: I am swinging; I swing every day; She is sliding; They run in the morning; We are jumping; He plays ball every day.', {'sedang terjadi sekarang': ['I am swinging', 'She is sliding', 'We are jumping'], 'kebiasaan sehari-hari': ['I swing every day', 'They run in the morning', 'He plays ball every day']}, 'Present continuous.', 'hard', 'mengelompokkan', 'Present continuous di taman bermain')
    p.order(4, 'Urutkan percakapan meminta bermain berikut!', ['Hello, can I play with you?', 'Yes, of course.', 'Let us play together.', 'Thank you.'], 'Urutan percakapan.', 'medium', 'mengurutkan', 'Meminta untuk bermain')
    p.order(2, 'Urutkan cara bermain perosotan berikut!', ['Climb the ladder.', 'Sit down.', 'Slide down the slide.', 'Stand up.'], 'Urutan bermain perosotan.', 'medium', 'mengurutkan', 'Tindakan di taman bermain')
    tfs(p, 5, [('"She is running" artinya dia sedang berlari.', True, 'is + -ing = sedang.'), ('"She is running" artinya dia berlari setiap hari.', False, 'Itu present continuous (sedang).')], 'Present continuous di taman bermain')
