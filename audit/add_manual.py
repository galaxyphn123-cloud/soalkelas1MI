import sys, json, os
slug = sys.argv[1]; p = os.path.join(os.path.dirname(os.path.abspath(__file__)), slug, 'manual_review.json')
d = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {'catatan': 'Tinjauan baca oleh model AI (bukan ahli). Hanya pengecualian yang dicatat; soal lain yang dibaca dianggap tidak bermasalah menurut pembaca. Semua temuan perlu keputusan guru/ahli.', 'reviewed_ranges': [], 'temuan': {}}
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'): continue
    if line.startswith('RANGE'):
        d['reviewed_ranges'].append(line.split(None, 1)[1]); continue
    i, code, note = [s.strip() for s in line.split('|', 2)]
    ids = [i]
    if '..' in i:
        pre, rng = i.rsplit('-', 1); a, b = rng.split('..'); ids = [f'{pre}-{n:04d}' for n in range(int(a), int(b) + 1)]
    elif ',' in i:
        pre, rng = i.rsplit('-', 1); ids = [f'{pre}-{int(n):04d}' for n in rng.split(',')]
    for j in ids: d['temuan'].setdefault(j, []).append({'kode': code, 'catatan': note})
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(d['temuan']), 'soal bertemuan;', d['reviewed_ranges'])
