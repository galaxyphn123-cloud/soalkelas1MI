# -*- coding: utf-8 -*-
import sys, json, collections, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, aa_gen
MODS = ['aa_m1_syahadat', 'aa_m2_tayibah', 'aa_m3_sehat', 'aa_m4_adab', 'aa_m5_kisah', 'aa_m6_rukun', 'aa_m7_sifat']

def pools():
    out = []
    for i, m in enumerate(MODS):
        D = importlib.import_module(m).D
        p = lib.Pool(D['code'], D['name'], D['tps'], D['quota'])
        p.cap = 4
        aa_gen.apply(p, D, D['code'], seed=30 + i)
        out.append(p)
    return out

if __name__ == '__main__':
    recs = lib.finalize(pools(), seed=20261013)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
