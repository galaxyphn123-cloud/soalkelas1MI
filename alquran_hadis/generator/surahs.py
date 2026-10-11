# -*- coding: utf-8 -*-
import surah_data, surah_gen, surah_scen, lib

def build_pools():
    pools = []
    for i, S in enumerate(surah_data.ALL):
        tps = [f'Murid mampu menjelaskan pesan pokok surah {S["name"]} dengan benar.',
               f'Murid mampu menyesuaikan pelafalan dan menghafal surah {S["name"]} dengan benar.',
               f'Murid mampu menyebutkan arti surah {S["name"]} dengan benar.',
               f'Murid mampu menerapkan pesan pokok surah {S["name"]} dengan benar dalam kehidupan sehari-hari sebagai wujud cinta Allah dan Rasul-Nya, serta cinta Ilmu.']
        p = lib.Pool(S['code'], S['name'] if S['name'].startswith('Surah') else 'Surah ' + S['name'], tps, 143)
        surah_gen.gen(p, S, 100 + i)
        surah_scen.apply(p, S['code'])
        surah_scen.grouping_and_more(p, S, S['code'])
        pools.append(p)
    return pools
