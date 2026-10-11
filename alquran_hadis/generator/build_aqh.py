# -*- coding: utf-8 -*-
import sys, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, hijaiah, ht, hadis, surahs

def pools():
    sp = {p.code: p for p in surahs.build_pools()}
    return [hijaiah.build(), sp['FA'], sp['IK'], ht.build(), sp['NS'], sp['FL'], hadis.build()]

if __name__ == '__main__':
    recs = lib.finalize(pools())
    out = sys.argv[1]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(recs, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(recs), dict(collections.Counter(r['material'] for r in recs)))
