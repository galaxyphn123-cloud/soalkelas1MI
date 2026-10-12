# -*- coding: utf-8 -*-
import json, csv, os, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_engine as E, audit_full as F
M = json.load(open('MASTER_STATS.json'))['per_mapel']
NARR = {
 'Fikih': dict(pola=['Kunci opsi terpanjang pada 402 dari 517 soal pilihan ganda; benar/salah 168 Benar : 42 Salah.', '46 isian bertipe isian singkat tetapi jawabannya terbuka ("Contoh jawaban").', 'CP memuat salat fardu, salat berjemaah, azan/ikamah, zikir, tetapi ATP hanya punya 4 materi; ±85 soal salat/azan/hari raya/kurban/kebersihan hati berada di celah ini.', 'Kunci bergantung mazhab (Syafii) harus ditetapkan: rukun tayamum, tepukan tayamum, air musta\'mal, najis anjing/bayi, khamr.', 'Kunci saling bertentangan: FIK-WT-0048/0216 (satu tepukan) vs FIK-WT-0205 (dua tepukan).'], contoh=['FIK-RI-0227 (bulan Hijriah di luar CP/ATP)', 'FIK-WT-0164 (tujuan wudu-tayamum hadas kecil vs FIK-WT-0165)', 'FIK-TH-0021 (mengulang salat karena najis: khilafiah)']),
 'Al-Quran Hadis': dict(pola=['Penomoran ayat Al-Fatihah menghitung Basmalah sebagai ayat 1; perlu keputusan rujukan mushaf (AQH-FA-0042 dst).', 'Terjemahan "Ath-thuhuru syathrul iman" menjadi "kebersihan sebagian dari iman" (AQH-HK-0057..0079) perlu ahli hadis.', 'Soal arti kosakata Arab (ماء, باب) pada TP yang hanya menulis huruf hijaiah (AQH-HT-0042 dst).', 'Soal urutan tanpa urutan baku (IK-0137, FL-0137, NS-0137, HT-0136, HK-0135).', 'Satu kunci salah dikoreksi: AQH-HT-0111 (رجل: Jim di tengah kata → Benar).'], contoh=['AQH-FA-0006/0026 (Basmalah memuat Ar-Rahman Ar-Rahim vs pengecoh)', 'AQH-FL-0018~0025 (duplikat substantif)']),
 'Bahasa Arab': dict(pola=['Arti طَاوِلَةٌ "meja makan" dan مَكْتَبٌ "meja belajar" (BAR-RM-0039.., BAR-SK-0014..) perlu ahli.', 'Gambar "paman" tidak membedakan عَمٌّ dan خَالٌ (BAR-KL-0083..0089); diperbaiki dengan menyebut hubungan di stem.', 'Templat "termasuk kata benda ...." mencampur kata kerja dan jamak; istilah mudzakkar/muannats/jamak abstrak untuk kelas 1 (25 soal).', 'Kosakata CP seperti hobi, buah, warna, transportasi, alam belum punya soal; ATP hanya nama, keluarga, rumah, madrasah.', 'Soal berurutan tanpa urutan tunggal (BAR-KL-0238, BAR-RM-0239, BAR-SK-0239).'], contoh=['BAR-PK-0088 (pengecoh تِلْمِيْذٌ juga benar)', 'BAR-PK-0210 (menjawab salam: dianjurkan vs wajib)']),
 'Akidah Akhlak': dict(pola=['Konflik kunci: AKA-SW-0020/0031 "tanpa diciptakan = Wujud" vs AKA-SW-0057 "Qidam"; Al-Amin "jujur" vs "amanah" (AKA-KN-0042/0055/0069).', 'Benar/salah masih berisi titik-titik (AKA-RI-0091/0093, AKA-SH-0052).', 'Raqib/Atid, rumusan iman, "pasti azab neraka" perlu ahli.', 'Sifat rasul (siddiq, amanah, tablig, fatanah) tidak ada di CP/ATP (AKA-KN-0040, 0046..0073).', 'CP memuat asmaulhusna, malaikat, kisah Nabi Nuh tanpa TP; Nuh dan asmaulhusna hampir tidak muncul.'], contoh=['AKA-SH-0004 (PHBS "disingkat")', 'AKA-TY-0076 (opsi tidak sejajar, kunci terpanjang)']),
 'Bahasa Indonesia': dict(pola=['211 soal merujuk cerita tetapi teks ceritanya tidak dimuat; teks asli ada di sumber pembangkit dan sudah dimuat pada revisi (soal menjadi lebih panjang, beban baca meningkat).', 'Soal suku kata, kebiasaan sehat, dan sikap belajar lebih dekat ke ATP yang tidak tercantum pada TP bank (BIN: 77 ATP_INDIKASI).', 'Soal "urutan" memakai teks yang urutannya tak bermakna (BIN-B3-0122, B4-0024, B6-0030).', 'Ejaan "qurban" (baku "kurban") perlu keputusan (BIN-B5-0060, 0077, 0084).', 'Isian terbuka dengan banyak jawaban sah.'], contoh=['BIN-B1-0056 ("t_s": tas/tes)', 'BIN-B5-0121/0134 (maaf vs permisi)', 'BIN-B7-0046/0059 (tekun vs rajin)']),
 'Matematika': dict(pola=['481 kunci hitung dihitung ulang: 0 kesalahan hitung.', 'Soal sikap/nilai tanpa berhitung (B1-04, B2-04, B3-04, B5-04, B7-04) dengan pengecoh absurd.', 'Konteks absurd akibat templat (topi dimakan, 10 kursi dibawa); 11 soal "kalah N kelereng" bernuansa taruhan (perlu ahli).', 'Istilah "selisih" (hard) di luar ATP; genap/ganjil tidak ada di CP/ATP (MTK-B8-0072).', 'Pasangan duplikat substantif (data sama, kata tanya dibalik): B5-0041.. 0063.'], contoh=['MTK-B1-0133 (7 jeruk dibagi 3)', 'MTK-B4-0021/0022/0009 (persegi termasuk persegi panjang)']),
 'Pancasila': dict(pola=['Satu sikap bisa masuk lebih dari satu sila (PPN-B3-0092, 0120, 0145, 0166..), sila 2 dan 5 tumpang tindih (B3-0093, 0105).', 'Konflik kunci "menanam pohon bersama": PPN-B4-0115 Salah vs B4-0001/0024/0078/0130; selokan: B4-0091/0134/0153 vs 0081/0103/0148-0150.', 'Fakta budaya daerah (rumah adat, tari, alat musik, makanan) tidak ada di CP/ATP; hanya terkait longgar dengan TP-B1-02.', 'Mengucapkan selamat hari raya agama lain khilafiah (B1-0167, 0175, 0206); klenteng dikunci Konghucu (B1-0093, 0114, 0143).', 'Stem negatif "tidak menaati ..." puluhan kali; blok benar/salah berkunci seragam.'], contoh=['PPN-B1-0134 (eksklusif "yang beragama Islam menyebut Tuhan Allah")', 'PPN-B4-0163/0207 (hadis kebersihan)']),
 'PJOK': dict(pola=['Semua 100 tugas kinerja memakai rubrik generik; banyak yang sebenarnya lisan/gambar.', 'Kunci keliru dikoreksi: PJK-MH-0038 (susu sumber protein), PJK-HA-0037 (olahraga membuat bugar), PJK-MH-0102 (kabel terkelupas: menjauh).', '"melompat" dipakai untuk gerak dua kaki, bertentangan dengan definisi bank (PJK-TB-0001, 0024, 0030..).', 'Risiko keselamatan: menyundul bola, menahan bola dengan dada, berenang, simulasi orang asing (PJK-TB-0216.., MH-0131, HA-0061/0065).', 'Soal pengurangan dalam 10 mengukur numerasi bukan gerak; TP BG-04 sama perilakunya dengan BG-02.'], contoh=['PJK-MH-0083 (nomor darurat 112)', 'PJK-HA-0072 vs HA-0082/0098/0117']),
 'Bahasa Inggris': dict(pola=['Kunci salah dikoreksi: ENG-B2-0076 (an orange crayon); ENG-B3-0076 diusulkan "two".', 'Soal "tersusun benar" (~55) dan anagram "susun huruf" (~55) membingungkan kelas 1 dan menuntut membaca/menulis padahal CP menekankan lisan; anagram sebagian tidak punya kunci unik.', 'Terjemahan -ku vs -nya (ENG-B5-0098/0106/0107); garden vs yard (B5-0016/0025); brother "adik" vs "kakak laki-laki" (B5-0072/0079).', 'Teks bacaan yang dirujuk tidak ada di bank (ENG-B1-0093..0098); dialog dikarang penyusun revisi dan perlu verifikasi.', 'Good night/Good evening dan Goodbye/See you tumpang tindih sebagai kunci (ENG-B1-0078..0087, 0102, 0112).'], contoh=['ENG-B4-0007/0017..0022 (relasi keluarga tak bisa dibedakan dari gambar)', 'ENG "favorite" (ejaan Amerika) perlu keputusan']),
}
SL = F.SLUG
cov_all = list(csv.DictReader(open('ATP_COVERAGE_MATRIX.csv', encoding='utf-8')))
for subj in E.BANKS:
    p = M[subj]; slug = SL[subj]
    if subj == 'Fikih': continue
    cov = [c for c in cov_all if c['mapel'] == subj]
    perhatian = [c for c in cov if c['kualitas_cakupan'] == 'perlu_perhatian']
    n = NARR[subj]; sa = p['status_awal']; sk = p['status_akhir']
    qs = [r for r in csv.DictReader(open(os.path.join(slug, 'ANTRIAN_VERIFIKASI_AHLI.csv'), encoding='utf-8'))]
    md = f"""# Laporan Audit Penuh — {subj} Kelas 1 MI (Fase A)

Bank: `{E.BANKS[subj]}` ({p['awal']} soal; tidak diubah, hash SHA-256 `{p['hash_bank_asli'][:16]}…`). Versi hasil perbaikan: `audit/FINAL/{slug}_final.json`.

## 1. Ringkasan
| Ukuran | Awal (audit) | Akhir (setelah revisi) |
|---|---|---|
| Soal diperiksa | {p['awal']} | {p['awal']} |
| PASS | {sa.get('PASS',0)} | {sk.get('PASS',0)} |
| REVISE | {sa.get('REVISE',0)} | {sk.get('REVISE',0)} |
| NEEDS_REVIEW (tahan, menunggu guru/ahli) | {sa.get('NEEDS_REVIEW',0)} | {sk.get('NEEDS_REVIEW',0)} |
| REJECT | 0 | 0 |
| Revisi diterima validator / ditunda (butuh keputusan) | — | {p['revisi_diterima']} / {p['tidak_direvisi']} |
| Isu struktur tersisa (hanya pada soal NEEDS_REVIEW yang ditahan) | — | {p['isu_struktur_tersisa']} |

Keselarasan ATP: {p['atp_final']} (SELARAS_MESIN = kata kunci TP cocok; SELARAS_TINJAU_BACA = ditandai mesin lalu dinyatakan selaras setelah dibaca; INDIKASI = terindikasi di tepi/luar TP, bukan terbukti).
Kode temuan tinjau baca (satu soal dapat memuat beberapa): {p['tinjau_baca_kode']}.
Kunci opsi terpanjang pada bank asli: {p['kunci_terpanjang']}; benar/salah: {p['tf']}; kesulitan: {p['kesulitan']}.

## 2. Temuan sistemik dan contoh
""" + '\n'.join('- ' + x for x in n['pola']) + f"""

Contoh lain untuk ditinjau: {'; '.join(n['contoh'])}.

## 3. Cakupan ATP
{len(perhatian)} dari {len(cov)} TP berstatus `perlu_perhatian` (porsi benar/salah condong, soal praktik <15% untuk TP berverba praktik, dsb.; rincian di `ATP_COVERAGE_MATRIX.csv`). Soal tertulis tidak dapat membuktikan TP berbasis praktik/observasi; perlu aktivitas pendamping guru.

## 4. Antrean verifikasi guru/ahli
{len(qs)} baris pada `audit/{slug}/ANTRIAN_VERIFIKASI_AHLI.csv` (+ konfirmasi pasca-revisi pada `ANTRIAN_VERIFIKASI_AHLI_SEMUA.csv`).

## 5. Batas audit
Mesin + tinjau baca oleh model AI (bukan guru/ahli). Tidak dapat memverifikasi isi gambar (hanya deskripsi teks), kebenaran fakta mazhab/budaya/bahasa secara otoritatif, dan kesesuaian pedagogis. Pemetaan KBC/Pembelajaran Mendalam/Profil Lulusan adalah usulan berbukti.
Berkas: `audit/{slug}/` — QUESTION_AUDIT_DETAIL, ATP_COVERAGE_MATRIX, KBC_DEEP_LEARNING_PROFILE_MATRIX, DUPLICATION_REPORT, manual_review, revisions_*, REVISIONS_VALIDATED, CONSISTENCY_CHECK, AUDIT_SUMMARY.
"""
    open(os.path.join(slug, f'LAPORAN_AUDIT_{subj.upper().replace(" ", "_")}.md'), 'w', encoding='utf-8').write(md)
print('ok')
