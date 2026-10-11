# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, arab_gen
from arab_data import MATERI

def pools():
    out = []
    for i, M in enumerate(MATERI):
        p = lib.Pool(M['code'], M['name'], M['tps'], 250)
        p.cap = 6
        arab_gen.gen(p, M, 50 + i)
        out.append(p)
    return out

if __name__ == '__main__':
    recs = lib.finalize(pools(), seed=20261012)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
