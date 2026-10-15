import json, os, collections, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
reg = json.load(open('tp_registry.json', encoding='utf-8'))
SLUG = {'Fikih': 'fikih', 'Al-Quran Hadis': 'alquran_hadis', 'Bahasa Arab': 'bahasa_arab', 'Akidah Akhlak': 'akidah_akhlak', 'Bahasa Indonesia': 'bahasa_indonesia', 'Matematika': 'matematika', 'Pancasila': 'pancasila', 'PJOK': 'pjok', 'Bahasa Inggris': 'bahasa_inggris'}
ATP = {'Fikih': 'FIKIH_UNTUK_.txt', 'Al-Quran Hadis': 'AL-QUR_AN_HA.txt', 'Bahasa Arab': 'BAHASA_ARAB_.txt', 'Akidah Akhlak': 'AKIDAH_AKHLA.txt', 'Bahasa Indonesia': 'B._INDONESIA.txt', 'Matematika': 'MATEMATIKA_I.txt', 'Pancasila': 'P_PANCASILA_.txt', 'PJOK': 'PJOK.txt', 'Bahasa Inggris': 'ENG.txt'}
PRE = {'Fikih': 'FIK', 'Al-Quran Hadis': 'AQH', 'Bahasa Arab': 'BAR', 'Akidah Akhlak': 'AKA', 'Bahasa Indonesia': 'BIN', 'Matematika': 'MTK', 'Pancasila': 'PPN', 'PJOK': 'PJK', 'Bahasa Inggris': 'ENG'}
NB = {'Fikih': 1, 'Al-Quran Hadis': 1, 'Bahasa Arab': 1, 'Akidah Akhlak': 2, 'Bahasa Indonesia': 3, 'Matematika': 2, 'Pancasila': 1, 'PJOK': 1, 'Bahasa Inggris': 2}
bank = {}
for sub, slug in SLUG.items():
    for r in json.load(open(os.path.join(ROOT, f'audit/FINAL/{slug}_final.json'), encoding='utf-8')): bank[r['id']] = r
rng = random.Random(7)
OUT = os.environ['TASKDIR']; os.makedirs(OUT, exist_ok=True)
FIELDS = ['question_type', 'difficulty', 'cognitive_level', 'competency', 'question', 'options', 'answer', 'explanation', 'visual_required', 'visual_prompt']
for sub in SLUG:
    tps = [e for e in reg if e['subject'] == sub and e['tambah'] > 0]
    total = sum(e['tambah'] for e in tps); n = NB[sub]
    cap = -(-total // n)
    batches = [[] for _ in range(n)]; sums = [0] * n
    for e in tps:
        k = min(range(n), key=lambda i: sums[i]) if sums[min(range(n), key=lambda i: sums[i])] + e['tambah'] <= cap + 15 else min(range(n), key=lambda i: sums[i])
        batches[k].append(e); sums[k] += e['tambah']
    for bi, b in enumerate(batches, 1):
        out = {'subject': sub, 'atp_file': '/home/user/soalkelas1MI/audit/atp_text/' + ATP[sub], 'tp': []}
        for e in b:
            ex = [bank[i] for i in e['pass_ids']]
            by = collections.defaultdict(list)
            for r in ex: by[r['question_type']].append(r)
            samp = []
            for t, lst in by.items(): samp.append(rng.choice(lst))
            rng.shuffle(samp); samp = samp[:8]
            mix = dict(collections.Counter(r['question_type'] for r in ex))
            # soal lain di materi yang sama (cuplikan) untuk konteks
            out['tp'].append({'tp_id': e['tp_id'], 'tp': e['tp'], 'material': e['material'], 'tambah': e['tambah'], 'jumlah_pass_sekarang': e['jumlah_pass'], 'baru_dari_atp': e['baru'], 'nomor_atp': e.get('nomor_atp'),
                              'campuran_tipe_sekarang': mix, 'contoh_soal_yang_sudah_ada': [{k: r.get(k) for k in FIELDS} for r in samp]})
        fn = f'{OUT}/tugas_{PRE[sub]}_{bi}.json'
        json.dump(out, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(fn.split('/')[-1], sum(t['tambah'] for t in out['tp']), 'soal', len(out['tp']), 'TP')
