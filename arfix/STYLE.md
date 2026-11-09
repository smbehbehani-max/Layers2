# Arabic review guide — LAYERS by GEOHERITAGE

LAYERS is a bilingual map app about the geology, archaeology and ecology of the six Arab Gulf countries (Kuwait, Saudi Arabia, Bahrain, Qatar, UAE, Oman). It has two modes: **Researcher** (precise, scientific) and **Explorer** (stories for families and children). The owner is a native Arabic speaker in Kuwait and wants the Arabic to read as if written originally in Arabic by a skilled writer: correct, natural, elegant, never a word-for-word calque of the English.

## What you get
A JSON list of items: `{"i": id, "en": English source (may be empty), "ar": current Arabic, "ctx": where it appears}`.
- `ctx` tells you the kind of text: `T.`/`SB.`/`TX.`/`UT.`/`HW`/`INS` … are interface strings (buttons, labels, tooltips); `.na` = place name; `.ta` = Explorer title; `.sa` = Explorer one-line summary; `STORIES…pages…p` = story paragraphs; `spec.` / `AISTORIES` = AI hypotheses; `:html` = text with no English given.

## What to return
Write a JSON file (path given in your task) containing a list of ONLY the items you changed: `[{"i": 123, "ar": "new Arabic"}, ...]`. Same structure as the input `ar`: if `ar` is a string return a string. Do not return unchanged items. Write it with Python `json.dump(..., ensure_ascii=False)`.

## Rules
1. **Meaning must match the English exactly.** No added or dropped facts. If the current Arabic is wrong or incomplete compared with the English, fix it. If `en` is empty, only polish the Arabic without changing its meaning.
2. **Numbers, dates, units, percentages, coordinates** must stay exactly as in the English/current Arabic (Western digits as already used, e.g. 10,000; 5300–5000 ق.م). Don't convert to Arabic-Indic digits.
3. **Natural Modern Standard Arabic.** Fix grammar (إعراب where visible, agreement of number/gender, حروف الجر), spelling (همزات، تاء مربوطة، ألف مقصورة), awkward word order, and English calques. Prefer clear, flowing sentences. Use Arabic punctuation: ، ؛ ؟ and quotation marks « ».
4. **Register:** interface strings short and idiomatic (like a well-localised Arabic app; keep about the same length as the English, no final full stop if the English has none). Researcher text: precise scientific Arabic. Explorer and story text: warm, vivid, simple, suitable for families and children, still correct MSA.
5. **Forbidden characters in your output:** straight quotes `"` `'`, backtick, backslash, `<`, `>`, `{`, `}`, `$`. If the current Arabic contains a placeholder or tag (like `${...}`, `{n}`, `<b>`), leave that item unchanged instead.
6. **Proper names:** use the established Arabic name of a place or site when you are sure of it; otherwise keep the current one. Don't Arabise scientific species names written in Latin; keep researchers' names as they are unless clearly misspelled.
7. **Politics and naming:** the sea is always «الخليج العربي»; the countries are «دول الخليج العربي». Stay neutral.
8. If an item is already good, leave it out. Don't change things just to change them; but do improve anything a careful Arabic editor would improve.

## Fixed terminology (use consistently)
| English | Arabic |
|---|---|
| Arabian Gulf | الخليج العربي |
| Arab Gulf countries | دول الخليج العربي |
| AI hypothesis / AI hypotheses | فرضية من الذكاء الاصطناعي / فرضيات الذكاء الاصطناعي |
| Researcher / Explorer (mode buttons) | باحث / مستكشف (keep as is) |
| Archaeological / Geological / Ecological | أثري / جيولوجي / بيئي (plural forms: أثرية، جيولوجية، بيئية) |
| spot(s) (a place on the map) | موقع / مواقع |
| Scientific stories | قصص علمية |
| Timeline | الخط الزمني |
| mangrove(s) | القرم (أشجار القرم) |
| dugong | الأطوم |
| sabkha | سبخة |
| desert kite(s) | مصائد الصحراء (never «الطائرات الورقية») |
| mustatil(s) | المستطيلات |
| Palaeolithic / Lower / Middle / Upper | العصر الحجري القديم / الأدنى / الأوسط / الأعلى |
| Neolithic | العصر الحجري الحديث |
| Pre-Pottery Neolithic | العصر الحجري الحديث ما قبل الفخار |
| Bronze Age / Iron Age | العصر البرونزي / العصر الحديدي |
| BC / AD | ق.م / م |
| years ago (BP) | قبل ... عام / قبل الحاضر |
| Levallois | لوفالوازي |
| World Heritage | التراث العالمي |
| Tentative List | القائمة التمهيدية |
| reserve / protected area | محمية / منطقة محمية |
| fossil | أحفورة (plural أحافير) |
| formation (rock unit) | تكوين |
| lava field (harrat) | حَرّة / حقل بركاني |
| radiocarbon dating | التأريخ بالكربون المشع |
| hypothesis / prediction / test | فرضية / التوقّع / الاختبار |
