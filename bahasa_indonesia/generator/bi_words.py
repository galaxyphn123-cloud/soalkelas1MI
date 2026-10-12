# -*- coding: utf-8 -*-
"""Kosakata per huruf awal. Kata ditulis per suku kata dipisah '-'. Tanda * = benda konkret yang dapat digambar."""
RAW = {
 'a': 'a-pel* a-yam* a-yah* a-tap* a-wan* a-pi* a-ku',
 'h': 'ha-ri hu-tan* hi-jau hi-dung* ha-ti he-wan* hu-jan* ha-us',
 'k': 'ka-ki* ku-da* ku-cing* kur-si* ka-pal* ke-las* ku-pu-ku-pu* kun-ci*',
 'm': 'ma-ta* me-ja* ma-ma* mu-lut* ma-kan mi-num mo-bil* mang-ga*',
 'r': 'ro-ti* ru-mah* ram-but* ru-sa* rok* ra-jin ra-pi ra-di-o*',
 't': 'tas* to-pi* ta-ngan* te-li-nga* ti-kus* ta-hu* tu-lis ti-ga',
 'c': 'ca-cing* ca-bai* cer-min* ci-um ce-ri-ta cu-ci cu-a-ca ci-cak*',
 'i': 'i-bu* i-kan* i-tik* i-ba-dah i-man il-mu in-dah i-ni',
 'p': 'pen-sil* pi-sang* pa-yung* pin-tu* pa-gi pu-tih per-gi pi-ring*',
 's': 'sa-pu* se-pa-tu* sa-pi* su-su* sa-bun* se-ko-lah* se-hat sa-yur*',
 'b': 'bu-ku* bo-la* ba-ju* bu-nga* bu-rung* ba-pak* ba-ik ba-tu*',
 'g': 'gi-gi* ga-jah* gu-la* gun-ting* gar-pu* ge-las* gam-bar* gu-ru*',
 'l': 'lam-pu* la-ri le-ma-ri* la-ngit* li-ma lu-as la-par le-bah*',
 'n': 'na-si* ne-nek* na-ma na-nas* na-ik no-mor',
 'o': 'o-bat* o-tak* o-rang* o-lah-ra-ga o-leh-o-leh om-bak*',
 'd': 'da-du* da-pur* do-a du-a dok-ter* dom-ba* da-un* di-ngin',
 'e': 'em-ber* em-pat e-nam e-lang* e-kor* es*',
 'f': 'fo-to* fa-jar film* fe-bru-a-ri',
 'j': 'jam* ja-ri* ja-lan* jen-de-la* je-ruk* ju-jur ja-ga ja-ket*',
 'u': 'u-lar* u-dang* u-lat* u-da-ra u-ang u-bi* un-ta* u-lang',
 'q': 'qa-ri* qur-ban* qi-ra-at',
 'v': 'vas* vi-de-o* vi-ta-min vo-kal',
 'w': 'wa-jah* war-na wak-tu wor-tel* wu-du wa-ngi wa-rung* wa-yang*',
 'x': 'xi-lo-fon*',
 'y': 'yo-yo* ya-tim ya-kin yo-gurt*',
 'z': 'ze-bra* za-kat za-i-tun zat',
}
WORDS = {}   # huruf -> [(kata, [suku], konkret)]
for L, s in RAW.items():
    WORDS[L] = []
    for tok in s.split():
        conc = tok.endswith('*')
        tok = tok.rstrip('*')
        w = tok.replace('-', '')
        w = {'kupukupu': 'kupu-kupu', 'oleholeh': 'oleh-oleh'}.get(w, w)
        WORDS[L].append((w, tok.split('-'), conc))
BAB_LETTERS = {1: 'ahkmrt', 2: 'cips', 3: 'bglno', 4: 'defju', 5: 'qvwxyz'}
