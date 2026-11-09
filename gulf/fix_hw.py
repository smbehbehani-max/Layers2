import json,sys
EX = {
 'qa': dict(
  src="<b>Example source:</b> Marine Policy, 2018: Marshall et al. report dugong herds of up to 500 animals off western Qatar.",
  srch="<b>Searches like:</b> “Al Zubarah excavation”, “Wadi Debayan Neolithic”, “Dahl Al Misfir cave”, “Qatar dugong survey”.",
  ext="<b>Extracted:</b> Place → Western Qatar coast · Published → 2018 · Finding → herds of up to 500 dugongs · Team → Marshall et al.",
  ttl="<b>Title:</b> Five hundred dugongs in one square kilometre<br><b>العنوان:</b> خمسمئة أتوم في كيلومتر مربع واحد",
  shown="<b>Shown on:</b> Dugongs of Western Qatar card → New research → link to the original source.",
  ex2="<b>Example:</b> Zekreet mesas → “Tables and mushrooms of stone” · Miocene Dam Formation · about 15 million years ago.",
  asrc="<b>مثال على مصدر:</b> Marine Policy، 2018: مارشال وزملاؤه يرصدون قطعانًا من الأتوم تصل إلى 500 حيوان قبالة غرب قطر.",
  asrch="<b>عمليات بحث مثل:</b> «تنقيبات الزبارة»، «وادي دبيان العصر الحجري الحديث»، «كهف دحل المسفر»، «مسح الأتوم في قطر».",
  aext="<b>المستخرج:</b> الموقع ← ساحل قطر الغربي · النشر ← 2018 · النتيجة ← قطعان تصل إلى 500 أتوم · الفريق ← مارشال وزملاؤه.",
  ashown="<b>يظهر في:</b> بطاقة أتوم غرب قطر ← بحث جديد ← رابط المصدر الأصلي.",
  aex2="<b>مثال:</b> هضاب زكريت ← «طاولات وفطر من حجر» · تكوين الدام الميوسيني · قبل نحو 15 مليون سنة."),
 'ae': dict(
  src="<b>Example source:</b> The National, 6 March 2026: new dating of the Marawah Island village pushes its first houses back to about 8,000 years ago.",
  srch="<b>Searches like:</b> “Hili excavation”, “Saruq Al-Hadid metallurgy”, “Wadi Wurayah survey”, “Bu Tinah dugong count”.",
  ext="<b>Extracted:</b> Place → Marawah Island · Published → Mar 2026 · Finding → village dated to c. 8,000 years ago · Team → Abu Dhabi archaeologists.",
  ttl="<b>Title:</b> The oldest houses on the Gulf shore<br><b>العنوان:</b> أقدم البيوت على ساحل الخليج",
  shown="<b>Shown on:</b> Marawah Island card → New research → link to the original source.",
  ex2="<b>Example:</b> Jebel Hafeet → “The mountain that leans” · Cretaceous–Eocene limestone · folded about 30 million years ago.",
  asrc="<b>مثال على مصدر:</b> The National، 6 مارس 2026: تأريخ جديد لقرية جزيرة مروح يعيد أولى بيوتها إلى نحو 8,000 عام.",
  asrch="<b>عمليات بحث مثل:</b> «تنقيبات هيلي»، «معادن ساروق الحديد»، «مسح وادي الوريعة»، «إحصاء الأتوم في بوطينة».",
  aext="<b>المستخرج:</b> الموقع ← جزيرة مروح · النشر ← مارس 2026 · النتيجة ← قرية مؤرخة بنحو 8,000 عام · الفريق ← آثاريو أبوظبي.",
  ashown="<b>يظهر في:</b> بطاقة جزيرة مروح ← بحث جديد ← رابط المصدر الأصلي.",
  aex2="<b>مثال:</b> جبل حفيت ← «الجبل المائل» · حجر جيري طباشيري–إيوسيني · طُوي قبل نحو 30 مليون سنة."),
 'om': dict(
  src="<b>Example source:</b> PLOS ONE, 2024 (Stewart et al.): first excavation of an Arabian lava tube — not in Oman, but the kind of paper the agent reads; for Oman, Willson et al. 2020 on Masirah loggerhead decline.",
  srch="<b>Searches like:</b> “Bat towers excavation”, “Sumhuram inscriptions”, “Jabal Samhan leopard camera traps”, “Masirah loggerhead nesting”.",
  ext="<b>Extracted:</b> Place → Masirah Island · Published → 2020 · Finding → loggerhead nests down sharply in one generation · Team → Willson et al.",
  ttl="<b>Title:</b> A decline inside one lifetime<br><b>العنوان:</b> تراجع في عمر جيل واحد",
  shown="<b>Shown on:</b> Masirah Island Loggerheads card → New research → link to the original source.",
  ex2="<b>Example:</b> Semail Ophiolite → “The sea floor that climbed onto the land” · Late Cretaceous oceanic crust · about 95 million years ago.",
  asrc="<b>مثال على مصدر:</b> Endangered Species Research، 2020: ويلسون وزملاؤه يرصدون تراجعًا حادًا في أعشاش السلاحف ضخمة الرأس في مصيرة.",
  asrch="<b>عمليات بحث مثل:</b> «تنقيبات أبراج بات»، «نقوش سمهرم»، «كاميرات نمور جبل سمحان»، «تعشيش السلاحف في مصيرة».",
  aext="<b>المستخرج:</b> الموقع ← جزيرة مصيرة · النشر ← 2020 · النتيجة ← تراجع حاد في الأعشاش خلال جيل واحد · الفريق ← ويلسون وزملاؤه.",
  ashown="<b>يظهر في:</b> بطاقة سلاحف مصيرة ← بحث جديد ← رابط المصدر الأصلي.",
  aex2="<b>مثال:</b> أفيوليت سمائل ← «قاع البحر الذي صعد إلى اليابسة» · قشرة محيطية من الطباشيري المتأخر · قبل نحو 95 مليون سنة."),
}
EX['om']['src']="<b>Example source:</b> Endangered Species Research, 2020: Willson et al. report a sharp fall in loggerhead nests on Masirah Island within one generation."
KEYS = {
 'src':"<b>Example source:</b> Archeowieści, 2 Dec 2024: Kuwaiti-Polish team discovers figurine, local pottery, and environmental clues.",
 'srch':"<b>Searches like:</b> “Bahra 1 excavation”, “Failaka temple”, “Kuwait mud volcanoes”, “Al-Ahmadi quarry Dammam Formation”.",
 'ext':"<b>Extracted:</b> Place → Bahra 1 · Published → Dec 2024 · Find → Ubaid-style clay head · Team → Kuwaiti-Polish mission.",
 'ttl':"<b>Title:</b> A unique clay head and the Gulf’s oldest pottery workshop at Bahra 1<br><b>العنوان:</b> رأس طيني فريد وأقدم ورشة فخار في الخليج في بحرة 1",
 'shown':"<b>Shown on:</b> Bahra 1 card → New research → link to the original source.",
 'ex2':"<b>Example:</b> Al-Ahmadi quarry → “The Window into Deep Time” · Eocene Dammam Formation · 48–34 million years ago.",
 'asrc':"<b>مثال على مصدر:</b> Archeowieści، 2 ديسمبر 2024: الفريق الكويتي البولندي يكتشف تمثالًا وفخارًا محليًا وأدلة بيئية.",
 'asrch':"<b>عمليات بحث مثل:</b> «تنقيبات بحرة 1»، «معبد فيلكا»، «البراكين الطينية في الكويت»، «محجر الأحمدي تكوين الدمام».",
 'aext':"<b>المستخرج:</b> الموقع ← بحرة 1 · النشر ← ديسمبر 2024 · الاكتشاف ← رأس طيني على طراز العبيد · الفريق ← البعثة الكويتية البولندية.",
 'ashown':"<b>يظهر في:</b> بطاقة بحرة 1 ← بحث جديد ← رابط المصدر الأصلي.",
 'aex2':"<b>مثال:</b> محجر الأحمدي ← «نافذة على الزمن السحيق» · تكوين الدمام الإيوسيني · قبل 48–34 مليون سنة.",
}
for cc in sys.argv[1:]:
    p=f'{cc}/config.json'; c=json.load(open(p))
    for k,key in KEYS.items():
        assert key in c['strings'], (cc,k)
        c['strings'][key]=EX[cc][k]
    json.dump(c,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print(cc,'ok')
