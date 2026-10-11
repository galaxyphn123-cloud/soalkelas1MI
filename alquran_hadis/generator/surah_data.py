# -*- coding: utf-8 -*-
"""Data empat surah pendek: (arab, latin, arti, pesan_ayat)."""

FATIHAH = dict(
 code='FA', name='Al-Fatihah', short='Al-Fatihah', arab_name='سُورَةُ الْفَاتِحَةِ', no=1, jml=7, arti_nama='Pembukaan',
 nama_lain='Ummul Kitab (induk Al-Qur\'an)',
 pesan="Memuji Allah, hanya menyembah Allah, dan memohon petunjuk jalan yang lurus",
 ayat=[
  ('بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ','Bismillahirrahmanirrahim','Dengan menyebut nama Allah Yang Maha Pengasih, Maha Penyayang','memulai segala kegiatan dengan menyebut nama Allah'),
  ('الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ',"Alhamdu lillahi rabbil 'alamin",'Segala puji bagi Allah, Tuhan seluruh alam','bersyukur dan memuji Allah'),
  ('الرَّحْمَٰنِ الرَّحِيمِ','Ar-rahmanir-rahim','Yang Maha Pengasih, Maha Penyayang','yakin bahwa Allah Maha Pengasih dan Maha Penyayang'),
  ('مَالِكِ يَوْمِ الدِّينِ','Maliki yaumid-din','Pemilik hari pembalasan','yakin bahwa Allah menguasai hari pembalasan'),
  ('إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ',"Iyyaka na'budu wa iyyaka nasta'in",'Hanya kepada Engkau kami menyembah dan hanya kepada Engkau kami memohon pertolongan','hanya menyembah dan meminta pertolongan kepada Allah'),
  ('اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ','Ihdinash-shiratal-mustaqim','Tunjukilah kami jalan yang lurus','berdoa agar ditunjukkan jalan yang lurus'),
  ('صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ',"Shiratal-ladzina an'amta 'alaihim ghairil-maghdhubi 'alaihim wa ladh-dhallin",'Jalan orang-orang yang Engkau beri nikmat, bukan jalan mereka yang dimurkai dan bukan jalan mereka yang sesat','mengikuti jalan orang yang diberi nikmat oleh Allah'),
 ],
 words=[('الْحَمْدُ','Alhamdu','segala puji'),('رَبِّ','Rabbi','Tuhan'),('الْعَالَمِينَ',"al-'alamin",'seluruh alam'),
  ('الرَّحْمَٰنِ','Ar-Rahman','Yang Maha Pengasih'),('الرَّحِيمِ','Ar-Rahim','Yang Maha Penyayang'),('مَالِكِ','Maliki','Pemilik'),
  ('يَوْمِ','yaumi','hari'),('الدِّينِ','ad-din','pembalasan'),('نَعْبُدُ',"na'budu",'kami menyembah'),
  ('نَسْتَعِينُ',"nasta'in",'kami memohon pertolongan'),('اهْدِنَا','ihdina','tunjukilah kami'),
  ('الصِّرَاطَ','ash-shirat','jalan'),('الْمُسْتَقِيمَ','al-mustaqim','yang lurus')],
)

IKHLAS = dict(
 code='IK', name='Al-Ikhlas', short='Al-Ikhlas', arab_name='سُورَةُ الْإِخْلَاصِ', no=112, jml=4, arti_nama='Memurnikan (keikhlasan)',
 nama_lain='surah tauhid (mengesakan Allah)',
 pesan="Allah Maha Esa dan menjadi tempat meminta segala sesuatu",
 ayat=[
  ('قُلْ هُوَ اللَّهُ أَحَدٌ','Qul huwallahu ahad','Katakanlah (Muhammad), Dialah Allah Yang Maha Esa','yakin bahwa Allah itu satu, Maha Esa'),
  ('اللَّهُ الصَّمَدُ','Allahush-shamad','Allah tempat meminta segala sesuatu','meminta segala sesuatu hanya kepada Allah'),
  ('لَمْ يَلِدْ وَلَمْ يُولَدْ','Lam yalid wa lam yulad','Allah tidak beranak dan tidak pula diperanakkan','yakin bahwa Allah tidak memiliki anak dan tidak dilahirkan'),
  ('وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ','Wa lam yakun lahu kufuwan ahad','Dan tidak ada sesuatu pun yang setara dengan Dia','yakin bahwa tidak ada yang menyamai Allah'),
 ],
 words=[('قُلْ','qul','katakanlah'),('هُوَ','huwa','Dia'),('أَحَدٌ','ahad','Maha Esa'),('الصَّمَدُ','ash-shamad','tempat meminta segala sesuatu'),
  ('يَلِدْ','yalid','beranak'),('يُولَدْ','yulad','diperanakkan'),('كُفُوًا','kufuwan','setara/sebanding'),('لَهُ','lahu','bagi-Nya')],
)

NAS = dict(
 code='NS', name='An-Nas', short='An-Nas', arab_name='سُورَةُ النَّاسِ', no=114, jml=6, arti_nama='Manusia',
 nama_lain='surah penutup Al-Qur\'an',
 pesan="Berlindung kepada Allah dari bisikan jahat setan",
 ayat=[
  ('قُلْ أَعُوذُ بِرَبِّ النَّاسِ',"Qul a'udzu birabbin-nas",'Katakanlah, aku berlindung kepada Tuhannya manusia','berlindung kepada Allah, Tuhannya manusia'),
  ('مَلِكِ النَّاسِ','Malikin-nas','Raja manusia','yakin bahwa Allah adalah Raja manusia'),
  ('إِلَٰهِ النَّاسِ','Ilahin-nas','Sembahan manusia','yakin bahwa hanya Allah yang disembah manusia'),
  ('مِنْ شَرِّ الْوَسْوَاسِ الْخَنَّاسِ','Min syarril-waswasil-khannas','Dari kejahatan (bisikan) setan yang bersembunyi','menjauhi bisikan jahat setan yang suka bersembunyi'),
  ('الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ','Alladzi yuwaswisu fi shudurin-nas','Yang membisikkan (kejahatan) ke dalam dada manusia','waspada karena setan membisikkan kejahatan ke dalam hati'),
  ('مِنَ الْجِنَّةِ وَالنَّاسِ','Minal-jinnati wan-nas','Dari (golongan) jin dan manusia','waspada terhadap bisikan jahat dari jin dan manusia'),
 ],
 words=[('قُلْ','qul','katakanlah'),('أَعُوذُ',"a'udzu",'aku berlindung'),('رَبِّ','rabbi','Tuhan'),('النَّاسِ','an-nas','manusia'),
  ('مَلِكِ','maliki','Raja'),('إِلَٰهِ','ilahi','Sembahan'),('شَرِّ','syarri','kejahatan'),('الْوَسْوَاسِ','al-waswas','pembisik (setan)'),
  ('الْخَنَّاسِ','al-khannas','yang bersembunyi'),('يُوَسْوِسُ','yuwaswisu','membisikkan'),('صُدُورِ','shudur','dada'),('الْجِنَّةِ','al-jinnah','jin')],
)

FALAQ = dict(
 code='FL', name='Al-Falaq', short='Al-Falaq', arab_name='سُورَةُ الْفَلَقِ', no=113, jml=5, arti_nama='Waktu subuh (fajar)',
 nama_lain='surah perlindungan (bersama An-Nas disebut mu\'awwidzatain)',
 pesan="Berlindung kepada Allah dari berbagai kejahatan",
 ayat=[
  ('قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ',"Qul a'udzu birabbil-falaq",'Katakanlah, aku berlindung kepada Tuhan yang menguasai waktu subuh','berlindung kepada Allah, Tuhan yang menguasai waktu subuh'),
  ('مِنْ شَرِّ مَا خَلَقَ','Min syarri ma khalaq','Dari kejahatan makhluk yang Dia ciptakan','berlindung dari kejahatan makhluk yang Allah ciptakan'),
  ('وَمِنْ شَرِّ غَاسِقٍ إِذَا وَقَبَ','Wa min syarri ghasiqin idza waqab','Dan dari kejahatan malam apabila telah gelap gulita','berlindung dari kejahatan malam yang gelap gulita'),
  ('وَمِنْ شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ',"Wa min syarrin-naffatsati fil-'uqad",'Dan dari kejahatan para penyihir yang meniup pada buhul-buhul (tali)','berlindung dari kejahatan sihir'),
  ('وَمِنْ شَرِّ حَاسِدٍ إِذَا حَسَدَ','Wa min syarri hasidin idza hasad','Dan dari kejahatan orang yang dengki apabila ia dengki','berlindung dari kejahatan orang yang iri dan dengki'),
 ],
 words=[('قُلْ','qul','katakanlah'),('أَعُوذُ',"a'udzu",'aku berlindung'),('الْفَلَقِ','al-falaq','waktu subuh (fajar)'),('شَرِّ','syarri','kejahatan'),
  ('خَلَقَ','khalaq','Dia ciptakan'),('غَاسِقٍ','ghasiqin','malam yang gelap'),('وَقَبَ','waqab','gelap gulita'),
  ('حَاسِدٍ','hasidin','orang yang dengki'),('حَسَدَ','hasad','dengki'),('الْعُقَدِ',"al-'uqad",'buhul (ikatan tali)')],
)

ALL = [FATIHAH, IKHLAS, NAS, FALAQ]
