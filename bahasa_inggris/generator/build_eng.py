# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from en_atp import BABS
import importlib

def mix():
    return [('multiple_choice', 0.28), ('multiple_choice_visual', 0.06), ('contextual', 0.07), ('true_false', 0.18),
            ('fill_in_short', 0.09), ('completion', 0.06), ('matching', 0.03), ('ordering', 0.05), ('grouping', 0.02),
            ('performance_task', 0.08)]

def pools():
    out = []
    for B in BABS:
        p = lib.Pool(B['code'], B['name'], B['tps'], B['quota'], mix=mix())
        p.cap = 4
        try:
            m = importlib.import_module('en_b' + B['code'][1:])
        except ImportError:
            continue
        getattr(m, 'b' + B['code'][1:])(p)
        out.append(p)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'dry':
        for p in pools():
            print(p.code, len(p.items), p.quota, dict(sorted(collections.Counter(x['tp'] for x in p.items).items())), dict(collections.Counter(x['type'] for x in p.items)))
        sys.exit()
    recs = lib.finalize(pools(), seed=20261018)
    json.dump(recs, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
