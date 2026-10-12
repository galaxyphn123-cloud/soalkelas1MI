# Tahap 1 — Inventarisasi (dibuat 2026-10-12)

## File yang berhasil dibaca
KMA 1503/2025 (.md), Panduan KBC (PDF 91 hlm.; Tabel 1 dibaca penuh), Pembelajaran Mendalam (PDF 62 hlm.; bagian Profil, Prinsip, Pengalaman Belajar), ATP 9 mapel (8 .docx/.pdf + ATP Bahasa Inggris dari .rar berisi 9 RTF), 9 bank soal JSON.

## Jumlah soal aktual
| Mapel | Soal | ID unik | TP | Materi |
|---|---|---|---|---|
| Fikih | 1000 | 1000 | 15 | 4 |
| Al-Qur'an Hadis | 1000 | 1000 | 28 | 7 |
| Bahasa Arab | 1000 | 1000 | 16 | 4 |
| Akidah Akhlak | 1000 | 1000 | 26 | 7 |
| Bahasa Indonesia | 1000 | 1000 | 32 | 8 |
| Matematika | 1000 | 1000 | 30 | 8 |
| Pendidikan Pancasila | 1000 | 1000 | 14 | 4 |
| PJOK | 1000 | 1000 | 15 | 4 |
| Bahasa Inggris | 1000 | 1000 | 72 | 9 |
| **Total** | **9000** | tidak ada ID ganda lintas mapel | 248 | 55 |

## Struktur data
Delapan belas field seragam (id, subject, grade, phase, tp_id, tp, material, competency, question_type, difficulty, cognitive_level, question, options, answer, explanation, visual_required, visual_prompt, tags); `misconception` pada 696 soal; Fikih punya `prerequisite` dan `mastery_target` (kosong pada 143/103 soal). **Belum ada** field `kbc_mapping`, `deep_learning_mapping`, `graduate_profile_mapping`, `quality_status`, `issues`, `recommended_action`, `revision_notes` — akan ditambahkan pada berkas audit, bukan menimpa bank asli. Nama field berbeda dari permintaan (`id`→`question_id`, `tp`→`tp_text`, `question`→`question_text`, `answer`→`correct_answer`): transformasi dicatat di berkas keluaran.

## Risiko awal (temuan nyata)
1. `sumber_atp` pada blueprint 5 mapel (Bahasa Arab, Akidah Akhlak, Bahasa Indonesia, Matematika, Pendidikan Pancasila) tertulis "KBC (ATP Al-Qur'an Hadis MI Kelas I)" akibat salinan templat — salah rujukan; perlu dikoreksi.
2. `cognitive_level` memakai 12 nilai tidak baku (mengingat, mengenali, mengurutkan, mencocokkan, mengelompokkan, membandingkan, …), bukan taksonomi tunggal; perlu pemetaan ke satu skala.
3. Bank dibangkitkan program dari tabel fakta dan templat (bukan ditulis guru); akibatnya banyak soal berpola sama dan konten fakta (terjemahan, transliterasi, fakta agama/budaya) belum ditinjau ahli.
4. Kunci jawaban merupakan opsi terpanjang (termasuk seri) pada 46-78% soal pilihan ganda per mapel (Fikih 78%, Matematika 67%, Bahasa Indonesia 63%, Akidah Akhlak 62%, Bahasa Arab 61%, Pancasila 56%, Inggris 49%, Al-Qur'an Hadis dan PJOK 46%) — pola yang bisa ditebak murid; soal sulit hanya 535 dari 9000.
5. TP pada bank berbunyi "Murid mampu …" (parafrasa ATP); kemiripan kata dengan teks ATP ≥0,8 untuk 247 dari 248 TP; satu TP (ENG-B5-05) berbeda karena salah ketik "intruksi" di ATP sumber.
6. Soal bergambar hanya punya deskripsi teks (`visual_prompt`); gambar belum dibuat.
7. Dokumen indikator dimensi Profil Lulusan terpisah belum tersedia (hanya definisi 8 dimensi).

## Rencana batch audit (dapat diverifikasi)
Batch = 1 mapel (1000 soal) per batch, urut sesuai README; setiap batch menyimpan `progress.json` (ID terakhir dan hitung status), dilanjutkan Tahap 3 → 4 → 5. Pemeriksaan duplikat substantif lintas 9000 soal dilakukan sesudah semua batch.
