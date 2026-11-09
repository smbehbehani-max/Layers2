"""Layers v5: animated strata hero, morphing layer bars, AI engine, official basemap, logo bar, app home."""
import json, re, os, base64, sys, runpy
sys.path.insert(0, '/tmp/w/layers'); sys.path.insert(0, '/tmp/w')
import hub as H
from onefile2 import patch_edition as patch0
from scene import scene
import map2, kidbg, cartoon, ecotier, storyidx
from html import escape as esc
SITE = '/tmp/w/layers/site'; OUT = '/tmp/w/layers/one'
BASE = 'https://smbehbehani-max.github.io/Layers2/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
os.makedirs(OUT, exist_ok=True)
ART = runpy.run_path('/tmp/w/art.py')['ART']
_w = lambda body: f'<svg viewBox="0 0 400 220" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{body}</svg>'
for m in ('art_a', 'art_g', 'art_e'):
    for k, v in runpy.run_path(f'/tmp/w/{m}.py')['A'].items(): ART[k] = _w(v)
def art(k):
    s = ART[k]
    if 'preserveAspectRatio' not in s: s = s.replace('<svg viewBox="0 0 400 220"', '<svg viewBox="0 0 400 220" preserveAspectRatio="xMidYMid slice"', 1)
    return f'<div class="art" style="width:100%;height:100%">{s}</div>'
KV = open('/tmp/w/layers/kvars.css').read(); ARTCSS = open('/tmp/w/layers/artcss.css').read()

EN = {'lang': 'عربي', 'by': 'by GEOHERITAGE', 'tag1': 'Discover the Arab Gulf Countries Beyond the Ordinary.', 'c1': 'Explore the Arab Gulf countries',
      'lgeo': 'Geological', 'larch': 'Archaeological', 'leco': 'Ecological',
      'k2': 'What is LAYERS', 't2': 'One Landscape. Multiple Stories.', 'st1': 'Ecological', 'st2': 'Archaeological', 'st3': 'Geological',
      'k3': 'Powered by', 'ai': 'Artificial Intelligence', 'aid': 'Connecting knowledge, proposing hypotheses and writing stories.',
      'o1': 'Hypotheses', 'o2': 'Timelines', 'o3': 'Stories', 'o1s': 'labelled untested', 'o2s': 'six countries compared', 'o3s': 'written by AI', 'cy1': 'reading papers', 'cy2': 'linking layers', 'cy3': 'writing stories', 'eng': 'LAYERS AI', 'src': 'New research', 'srcs': 'monitored weekly', 'hum': 'Human check', 'hums': 'before publishing', 'loop': 'new places added', 'hyp': 'Hypotheses', 'hyps': 'labelled untested',
      'tt1': 'Layers of the Arab Gulf countries', 'tt2': 'Six countries · three layers · one map', 'vmap': 'Map', 'vtl': 'Timeline', 'vcmp': 'Compare', 'tlT': 'One timeline, six countries', 'tlS': 'Two scales: the oldest surface rock and most-cited geological places of each country, and the oldest human traces and most-cited archaeological places. Scroll sideways; tap a row to open it in its country.',
      'er1': 'Deep time', 'er2': 'Cenozoic', 'er3': 'Ice ages', 'er4': 'Our era', 'er1s': 'Deep', 'er2s': 'Cenoz.', 'er3s': 'Ice', 'er4s': 'Now', 'ev1': 'The ice ages begin', 'ev2': 'The last ice age ends', 'tk0': '1 billion', 'tk1': '100 Myr', 'tk2': '10 Myr', 'tk3': '1 Myr', 'tk4': '100,000', 'tk5': '10,000 yr', 'tk6': '1,000', 'tk7': 'Today',
      'sa1': 'Archaeological spots', 'sa1t': 'Places where people left traces: settlements, tombs, forts, rock art.', 'sg1': 'Geological spots', 'sg1t': 'Rocks, landforms and fossils that record how the land formed.', 'se1': 'Ecological spots', 'se1t': 'Living places: reserves, wetlands, reefs and nesting beaches.', 'sai1': 'AI hypotheses', 'sai1t': 'Where AI links published records into a new, untested idea: a hypothesis to check, not a finding.', 'sst1': 'Scientific stories', 'sst1t': 'Illustrated stories written by AI from the published research behind each place. The facts and references are real; the storytelling is AI-generated.', 'hp1': 'Tap an Arab Gulf country', 'hp2': 'to discover its layers.', 'k6': 'Why it is different', 't6': 'Five things no tourism map does', 't6s': 'The innovation components of LAYERS, grouped: core, tourism, and platform.',
      'g1': 'Core innovations', 'g2': 'Tourism innovations', 'g3': 'Platform and ecosystem',
      'tag2': 'A new way to experience the Arab Gulf countries.', 'k4': 'Six countries', 't4': 'Explore the Arab Gulf countries', 'hint': 'Tap a country to explore its layers',
      'wl1': 'Arabian Gulf', 'wl2': 'Red Sea', 'wl3': 'Arabian Sea', 'wl4': 'Gulf of Oman',
      'f1': 'GEO — geological and geographical. HERITAGE — what makes a place matter. LAYERS — how you explore it.',
      'priv': 'Privacy', 'made': 'Made in Kuwait',
      'ah1': 'Discover the Arab Gulf countries', 'ah2': 'Beyond the Ordinary.',
      'as': 'Explore destinations through geological, archaeological and ecological layers, with AI revealing the connections and stories behind each place.',
      's1': 'places', 's2': 'countries', 's3': 'layers', 's4': 'languages', 'intro': 'Watch the introduction',
      'k5': 'Always growing', 't5': 'A map that keeps learning', 'l5': 'New research about these places is found, read, written in both languages and checked before it reaches the map. Every record keeps its sources.',
      's5': 'illustrated stories', 's6': 'AI connections', 's7': 'references', 'live': 'Research digest: weekly · last update 7 Nov 2026',
      'mr': 'Researcher', 'me': 'Explorer', 'how': 'How it works', 'inst': 'Install app',
      'ct': 'Across the Arab Gulf countries', 'cs': 'Six editions side by side: places, oldest surface rock, oldest human trace, ecology places, protected areas and World Heritage sites. Tap a country name to open it.',
      'tg': 'Geological time scale', 'tgs': 'The oldest rock exposed at the surface in each country, ranked from oldest to youngest (million years before today, logarithmic).',
      'ta': 'Archaeological time scale', 'tas': 'The oldest human trace recorded in each country, ranked from oldest to youngest (years before today, logarithmic).',
      'e1': 'Precambrian', 'e2': 'Palaeozoic', 'e3': 'Mesozoic', 'e4': 'Cenozoic', 'p1': 'Lower Palaeolithic', 'p2': 'Middle Palaeolithic', 'p3': 'Upper Palaeolithic', 'p4': 'Neolithic', 'p5': 'Bronze Age · Dilmun & Umm an-Nar', 'p6': 'Iron Age', 'p7': 'Late pre-Islamic', 'p8': 'Islamic era', 'eco': 'Ecology', 'econ': 'Living places by the year they were recorded or protected, graded on worldwide criteria.', 'rar1': 'notable', 'rar2': 'rare', 'rar3': 'unique',
      't.common': 'Common', 't.uncommon': 'Uncommon', 't.rare': 'Rare', 't.exceptional': 'Exceptional',
      'td.exceptional': 'UNESCO World Heritage or Biosphere Reserve, or found nowhere else on Earth', 'td.rare': 'Ramsar wetland, UNESCO tentative list, or home to an IUCN Endangered species', 'td.uncommon': 'A protected area, mangroves, coral or nesting beaches', 'td.common': 'Other recorded living places',
      'eaS': 'Ancient', 'esS': 'Seasonal', 'erS2': 'Protected', 'esT': 'Every year — seasonal living events', 'eaT': 'Ancient living places — their own age', 'erT2': 'Recorded or protected — by year', 'erT': 'Ecology rarity', 'erS': 'How many living places in each country reach each worldwide grade.', 'hc8': 'Rarest living place', 'r5': 'Most exceptional living places',
      'cnG': 'Million years ago →', 'cnA': 'Years ago →', 'cnS': 'Month of the year →', 'cnY': 'Year →', 'bk': 'Back to timeline', 'stT': 'Stories', 'stP': 'Picking a story…', 'stF': 'from', 'stGo': 'Opening',
      'k7': 'Two ways in', 't7': 'One map. Two audiences.', 'mrd': 'Sources, data, timelines and hypotheses for people who want depth.', 'med': 'Stories, cartoon maps and gentle colours for families and the curious.',
      'g1l': 'Reads new research every week', 'g2l': 'A person checks every record', 'g3l': 'The map grows — nothing is deleted', 'gcount': 'and counting',
      'refs': 'References', 'refn': 'References used by the places on these scales', 'p1s': 'Lower Pal.', 'p2s': 'Middle Pal.', 'p3s': 'Upper', 'p4s': 'Neolithic', 'e1s': 'Precambrian', 'e2s': 'Palaeozoic', 'e3s': 'Mesozoic', 'e4s': 'Cenozoic', 'now': 'today', 'ma0': 'Ma', 'kya': 'yrs ago',
      'hwT': 'How LAYERS works', 'hwP': 'From a new paper to a story on the map: how research is found, checked and published to the app.',
      'inT': 'Install LAYERS', 'inP': 'The app installs from the browser and works offline.',
      'in1': 'iPhone / iPad', 'in1d': 'Open this page in Safari, tap Share, then “Add to Home Screen”.', 'in2': 'Android', 'in2d': 'Open in Chrome, tap the menu (⋮), then “Install app” or “Add to Home screen”.', 'in3': 'Computer', 'in3d': 'In Chrome or Edge, click the install icon at the right of the address bar.',
      'hc1': 'Country', 'hc2': 'Places', 'hc3': 'Oldest surface rock', 'hc4': 'Oldest human trace', 'hc5': 'Ecology', 'hc6': 'Protected areas', 'hc7': 'World Heritage',
      'ra1': 'About', 'ra2': 'Map', 'ra3': 'Compare', 'ra4': 'Timeline', 'ra9': 'Archaeology scale', 'ra5': 'Records', 'ra6': 'How it learns', 'ra7': 'Install', 'ra8': 'Introduction', 'ra10': 'Innovation', 'ra11': 'References', 'rl': 'All Arab Gulf countries', 'ca': 'Archaeological', 'cg': 'Geological', 'ce': 'Ecology', 'cai': 'AI connections', 'cst': 'Stories',
      'r1': 'Oldest rock at the surface', 'r2': 'Oldest human trace', 'r3': 'Most ecology places', 'r4': 'Most World Heritage sites', 'ya': 'years ago', 'ma': 'million years ago'}
AR = {'lang': 'English', 'by': 'من جيوهيريتيج', 'tag1': 'اكتشف دول الخليج العربي بما يتجاوز المألوف.', 'c1': 'استكشف دول الخليج العربي',
      'lgeo': 'جيولوجيا', 'larch': 'آثار', 'leco': 'بيئة',
      'k2': 'ما هو «طبقات»', 't2': 'أرض واحدة. قصص متعددة.', 'st1': 'البيئة', 'st2': 'الآثار', 'st3': 'الجيولوجيا',
      'k3': 'بقوة', 'ai': 'الذكاء الاصطناعي', 'aid': 'يربط المعرفة، ويقترح الفرضيات، ويؤلّف القصص.',
      'o1': 'فرضيات', 'o2': 'خطوط زمنية', 'o3': 'قصص علمية', 'o1s': 'موسومة غير مختبَرة', 'o2s': 'مقارنة بين ست دول', 'o3s': 'يؤلّفها الذكاء الاصطناعي', 'cy1': 'يقرأ الأبحاث', 'cy2': 'يربط الطبقات', 'cy3': 'يؤلّف القصص', 'eng': 'ذكاء طبقات', 'src': 'أبحاث جديدة', 'srcs': 'تُرصد أسبوعيًا', 'hum': 'مراجعة بشرية', 'hums': 'قبل النشر', 'loop': 'مواقع جديدة تُضاف', 'hyp': 'فرضيات', 'hyps': 'مُعلَّمة غير مختبَرة',
      'tt1': 'طبقات دول الخليج العربي', 'tt2': 'ست دول · ثلاث طبقات · خريطة واحدة', 'vmap': 'الخريطة', 'vtl': 'الخط الزمني', 'vcmp': 'مقارنة', 'tlT': 'خط زمني واحد وست دول', 'tlS': 'مقياسان: أقدم صخرة سطحية وأكثر الأماكن الجيولوجية استشهادًا في كل دولة، وأقدم الآثار البشرية وأكثر الأماكن الأثرية استشهادًا. مرّر جانبيًا؛ واضغط على صف لفتحه في دولته.',
      'er1': 'الزمن السحيق', 'er2': 'السينوزي', 'er3': 'العصور الجليدية', 'er4': 'عصرنا', 'er1s': 'سحيق', 'er2s': 'سينوزي', 'er3s': 'جليدي', 'er4s': 'الآن', 'ev1': 'تبدأ العصور الجليدية', 'ev2': 'ينتهي آخر عصر جليدي', 'tk0': 'مليار', 'tk1': '100 مليون', 'tk2': '10 ملايين', 'tk3': 'مليون', 'tk4': '100 ألف', 'tk5': '10 آلاف', 'tk6': 'ألف', 'tk7': 'اليوم',
      'sa1': 'مواقع أثرية', 'sa1t': 'أماكن ترك فيها البشر آثارًا: مستوطنات ومقابر وحصون ونقوش صخرية.', 'sg1': 'مواقع جيولوجية', 'sg1t': 'صخور وتضاريس وأحافير تسجّل كيف تكوّنت الأرض.', 'se1': 'مواقع بيئية', 'se1t': 'أماكن حية: محميات وأراضٍ رطبة وشعاب وشواطئ تعشيش.', 'sai1': 'فرضيات الذكاء الاصطناعي', 'sai1t': 'حيث يربط الذكاء الاصطناعي سجلات منشورة في فكرة جديدة غير مختبَرة: فرضية للفحص لا نتيجة.', 'sst1': 'قصص علمية', 'sst1t': 'قصص مصوّرة كتبها الذكاء الاصطناعي من الأبحاث المنشورة وراء كل مكان. الحقائق والمراجع حقيقية، أما الصياغة القصصية فمن الذكاء الاصطناعي.', 'hp1': 'اضغط على دولة خليجية', 'hp2': 'لتكتشف طبقاتها.', 'k6': 'لماذا هو مختلف', 't6': 'خمسة أشياء لا تفعلها أي خريطة سياحية', 't6s': 'مكوّنات الابتكار في «طبقات» مجمّعة: الجوهر، والسياحة، والمنصة.',
      'g1': 'ابتكارات جوهرية', 'g2': 'ابتكارات سياحية', 'g3': 'المنصة والمنظومة',
      'tag2': 'طريقة جديدة لتجربة دول الخليج العربي.', 'k4': 'ست دول', 't4': 'استكشف دول الخليج العربي', 'hint': 'اضغط على دولة لاستكشاف طبقاتها',
      'wl1': 'الخليج العربي', 'wl2': 'البحر الأحمر', 'wl3': 'بحر العرب', 'wl4': 'خليج عُمان',
      'f1': 'جيو — الجيولوجيا والجغرافيا. التراث — ما يجعل المكان مهمًا. طبقات — طريقك لاستكشافه.',
      'priv': 'الخصوصية', 'made': 'صُنع في الكويت',
      'ah1': 'اكتشف دول الخليج العربي', 'ah2': 'بما يتجاوز المألوف.',
      'as': 'استكشف الوجهات عبر طبقاتها الجيولوجية والأثرية والبيئية، مع ذكاء اصطناعي يكشف الروابط والقصص خلف كل مكان.',
      's1': 'موقعًا', 's2': 'دول', 's3': 'طبقات', 's4': 'لغتان', 'intro': 'شاهد المقدمة',
      'k5': 'في نموّ دائم', 't5': 'خريطة لا تتوقف عن التعلّم', 'l5': 'تُرصد الأبحاث الجديدة عن هذه الأماكن وتُقرأ وتُكتب باللغتين وتُراجع قبل أن تصل إلى الخريطة. وكل سجل يحتفظ بمصادره.',
      's5': 'قصة مصوّرة', 's6': 'رابطًا ذكيًا', 's7': 'مرجعًا', 'live': 'موجز الأبحاث: أسبوعي · آخر تحديث 7 نوفمبر 2026',
      'mr': 'باحث', 'me': 'مستكشف', 'how': 'كيف يعمل', 'inst': 'ثبّت التطبيق',
      'ct': 'عبر دول الخليج العربي', 'cs': 'النسخ الست جنبًا إلى جنب: المواقع، وأقدم صخرة سطحية، وأقدم أثر بشري، والمواقع البيئية، والمحميات، ومواقع التراث العالمي. اضغط على اسم الدولة لفتحها.',
      'tg': 'المقياس الزمني الجيولوجي', 'tgs': 'أقدم صخرة مكشوفة على السطح في كل دولة، مرتبةً من الأقدم إلى الأحدث (مليون سنة قبل اليوم، لوغاريتمي).',
      'ta': 'المقياس الزمني الأثري', 'tas': 'أقدم أثر بشري مسجَّل في كل دولة، مرتبًا من الأقدم إلى الأحدث (سنوات قبل اليوم، لوغاريتمي).',
      'e1': 'ما قبل الكمبري', 'e2': 'الباليوزي', 'e3': 'الميزوزي', 'e4': 'السينوزي', 'p1': 'العصر الحجري القديم الأسفل', 'p2': 'الحجري القديم الأوسط', 'p3': 'الحجري القديم الأعلى', 'p4': 'العصر الحجري الحديث', 'p5': 'العصر البرونزي · دلمون وأم النار', 'p6': 'العصر الحديدي', 'p7': 'أواخر ما قبل الإسلام', 'p8': 'العصر الإسلامي', 'eco': 'بيئة', 'econ': 'الأماكن الحية حسب سنة تسجيلها أو حمايتها، مصنّفة وفق معايير عالمية.', 'rar1': 'لافت', 'rar2': 'نادر', 'rar3': 'فريد',
      't.common': 'شائع', 't.uncommon': 'غير شائع', 't.rare': 'نادر', 't.exceptional': 'استثنائي',
      'td.exceptional': 'تراث عالمي لليونسكو أو محمية محيط حيوي، أو لا يوجد في أي مكان آخر على الأرض', 'td.rare': 'أرض رطبة في رامسار، أو على القائمة التمهيدية لليونسكو، أو موطن لنوع مهدد بالانقراض وفق الاتحاد الدولي لحفظ الطبيعة', 'td.uncommon': 'منطقة محمية، أو مانغروف أو مرجان أو شواطئ تعشيش', 'td.common': 'أماكن حية أخرى مسجّلة',
      'eaS': 'عريقة', 'esS': 'موسمية', 'erS2': 'محمية', 'esT': 'كل عام — أحداث حية موسمية', 'eaT': 'أماكن حية عريقة — بعمرها الحقيقي', 'erT2': 'سُجّلت أو حُميت — حسب السنة', 'erT': 'ندرة البيئة', 'erS': 'عدد الأماكن الحية في كل دولة لكل درجة عالمية.', 'hc8': 'أندر مكان حي', 'r5': 'الأكثر أماكن حية استثنائية',
      'cnG': 'ملايين السنين ←', 'cnA': 'سنوات مضت ←', 'cnS': 'شهور السنة ←', 'cnY': 'السنة ←', 'bk': 'العودة إلى الخط الزمني', 'stT': 'قصص', 'stP': 'نختار قصة…', 'stF': 'من', 'stGo': 'نفتح',
      'k7': 'طريقان للدخول', 't7': 'خريطة واحدة. جمهوران.', 'mrd': 'مصادر وبيانات وخطوط زمنية وفرضيات لمن يريد العمق.', 'med': 'قصص وخرائط كرتونية وألوان هادئة للعائلات والفضوليين.',
      'g1l': 'يقرأ أبحاثًا جديدة كل أسبوع', 'g2l': 'إنسان يراجع كل سجل', 'g3l': 'تنمو الخريطة ولا يُحذف شيء', 'gcount': 'وفي ازدياد',
      'refs': 'المراجع', 'refn': 'المراجع التي تستند إليها الأماكن في هذه المقاييس', 'p1s': 'حجري قديم أسفل', 'p2s': 'أوسط', 'p3s': 'أعلى', 'p4s': 'حجري حديث', 'e1s': 'ما قبل الكمبري', 'e2s': 'الباليوزي', 'e3s': 'الميزوزي', 'e4s': 'السينوزي', 'now': 'اليوم', 'ma0': 'مليون سنة', 'kya': 'سنة مضت',
      'hwT': 'كيف يعمل «طبقات»', 'hwP': 'من ورقة علمية جديدة إلى قصة على الخريطة: كيف يُرصد البحث ويُراجع ويُنشر في التطبيق.',
      'inT': 'ثبّت «طبقات»', 'inP': 'يُثبَّت التطبيق من المتصفح ويعمل دون إنترنت.',
      'in1': 'آيفون / آيباد', 'in1d': 'افتح هذه الصفحة في سفاري، ثم «مشاركة»، ثم «إضافة إلى الشاشة الرئيسية».', 'in2': 'أندرويد', 'in2d': 'افتح في كروم، ثم القائمة (⋮)، ثم «تثبيت التطبيق».', 'in3': 'الحاسوب', 'in3d': 'في كروم أو إيدج، اضغط على أيقونة التثبيت يمين شريط العنوان.',
      'hc1': 'الدولة', 'hc2': 'المواقع', 'hc3': 'أقدم صخرة سطحية', 'hc4': 'أقدم أثر بشري', 'hc5': 'بيئة', 'hc6': 'محميات', 'hc7': 'تراث عالمي',
      'ra1': 'عن التطبيق', 'ra2': 'الخريطة', 'ra3': 'مقارنة', 'ra4': 'الخط الزمني', 'ra9': 'مقياس الآثار', 'ra5': 'أرقام قياسية', 'ra6': 'كيف يتعلّم', 'ra7': 'تثبيت', 'ra8': 'المقدمة', 'ra10': 'الابتكار', 'ra11': 'المراجع', 'rl': 'كل دول الخليج العربي', 'ca': 'آثار', 'cg': 'جيولوجيا', 'ce': 'بيئة', 'cai': 'روابط ذكية', 'cst': 'قصص',
      'r1': 'أقدم صخرة على السطح', 'r2': 'أقدم أثر بشري', 'r3': 'الأكثر مواقع بيئية', 'r4': 'الأكثر مواقع تراث عالمي', 'ya': 'سنة مضت', 'ma': 'مليون سنة مضت'}
NAMES = {'kw': ('Kuwait', 'الكويت'), 'sa': ('Saudi Arabia', 'السعودية'), 'bh': ('Bahrain', 'البحرين'), 'qa': ('Qatar', 'قطر'), 'ae': ('UAE', 'الإمارات'), 'om': ('Oman', 'عُمان')}
for cc, (e, a) in NAMES.items(): EN['n.' + cc] = e; AR['n.' + cc] = a

def T(k): return f'<span data-i="{k}">{EN[k]}</span>'

# --- map component ---
MD = map2.build()
# small countries get their badge out at sea with a leader line, so the badge never covers the country itself
# each badge sits on its own country; only Bahrain (too small to hold it) is set in the Arabian Gulf just north, with an arrow
BADGE = {'kw': ((47.72, 29.33), None, 'r'), 'sa': ((44.3, 23.9), None, ''), 'bh': ((50.25, 27.95), (50.55, 26.25), ''),
         'qa': ((51.22, 25.12), None, ''), 'ae': ((54.25, 23.65), None, ''), 'om': ((57.4, 20.6), None, '')}
SEA = [('wl1', (53.15, 26.45), 17, 13), ('wl2', (38.0, 20.0), 62, 22), ('wl3', (60.0, 15.5), 0, 22), ('wl4', (58.75, 24.55), 33, 12)]
def mapc(pfx):
    W, Hh = map2.W, map2.H
    nb = ''.join(f'<path class="nb" d="{d}"/>' for d in MD['other'])
    gc = ''.join(f'<path class="cs" data-cc="{cc}" d="{MD["gcc"][cc]}" style="animation-delay:{i*1.5:.1f}s"/>' for i, cc in enumerate(ORDER))
    wl = ''
    for k, (lng, lat), rot, fs in SEA:
        x, y = map2.P(lng, lat); wl += f'<text class="wl" data-i="{k}" x="{x:.0f}" y="{y:.0f}" font-size="{fs}" transform="rotate({rot} {x:.0f} {y:.0f})">{EN[k]}</text>'
    ld = ''; bd = ''
    for cc in ORDER:
        (bl, pt, side) = BADGE[cc]; bx, by = map2.P(*bl)
        if pt:
            px, py = map2.P(*pt); ld += f'<path class="ldr" d="M{bx:.1f} {by:.1f} Q{bx+14:.1f} {(by+py)/2:.1f} {px:.1f} {py-3:.1f}" marker-end="url(#{pfx}arw)"/><circle class="ldp" cx="{px:.1f}" cy="{py:.1f}" r="1.8"/>'
        side = ' r' if side == 'r' else ''
        mx, my = map2.P(*({'sa': (47.2, 24.3)}.get(cc, bl)))
        bd += f'<a class="bd{side} s{cc}" href="#{cc}" data-cc="{cc}" data-x="{bx:.1f}" data-y="{by:.1f}" data-xm="{mx:.1f}" data-ym="{my:.1f}" style="left:{bx/W*100:.2f}%;top:{by/Hh*100:.2f}%" aria-label="{EN["n."+cc]}"><span class="bdl">{H.flag_logo(cc, pfx+"b"+cc)}</span><span class="bdn" data-i="n.{cc}">{EN["n."+cc]}</span></a>'
    return f'<div class="map"><div class="mapin"><svg viewBox="0 0 {W} {Hh}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Map of the Arab Gulf countries"><defs><marker id="{pfx}arw" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#fffaf0"/></marker></defs>{nb}{gc}{wl}{ld}</svg>{bd}</div></div>'

HAND = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#3a1d10" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11m0-1.5a1.5 1.5 0 0 1 3 0V12m0-1a1.5 1.5 0 0 1 3 0v4a6 6 0 0 1-6 6h-1a6 6 0 0 1-4.9-2.5L4.3 15.3a1.5 1.5 0 0 1 2.4-1.8L9 16"/></svg>'

IC = {'link': '<path d="M9 15l6-6M8 12a4 4 0 0 1 0-6l1-1a4 4 0 0 1 6 6M16 12a4 4 0 0 1 0 6l-1 1a4 4 0 0 1-6-6"/>',
 'spark': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
 'book': '<path d="M4 5h6a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H4zM20 5h-6a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h7z"/>',
 'radar': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/>',
 'route': '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8 17h5a4 4 0 0 0 0-8h-2a3 3 0 0 1 0-6h5"/>',
 'layers': '<path d="M12 3l9 5-9 5-9-5zM3 13l9 5 9-5M3 17l9 5 9-5"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 'pin': '<path d="M12 21s-6-5.3-6-11a6 6 0 0 1 12 0c0 5.7-6 11-6 11z"/><circle cx="12" cy="10" r="2.5"/>',
 'school': '<path d="M3 9l9-4 9 4-9 4zM6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5M21 9v6"/>',
 'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'leaf': '<path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7"/>',
 'check': '<path d="M4 12l5 5L20 7"/>',
 'people': '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M15 20a5 5 0 0 1 7 0"/>',
 'map': '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'}
INNO5 = [('link', '#5847b0', '01', 'AI connecting disciplines', 'Geology, archaeology and ecology read together, so one place tells one connected story.', 'ذكاء يربط التخصصات', 'الجيولوجيا والآثار والبيئة تُقرأ معًا، فيروي المكان قصة واحدة متصلة.'),
 ('spark', '#bf2f7d', '02', 'AI hypotheses', 'New, testable ideas about links between places — always labelled as untested.', 'فرضيات ذكية', 'أفكار جديدة قابلة للاختبار عن الروابط بين الأماكن، مُعلَّمة دائمًا كغير مختبَرة.'),
 ('book', '#b4521c', '03', 'Research made accessible', 'Scientific papers turned into illustrated stories and clear explanations, in two languages.', 'أبحاث في متناول الجميع', 'أوراق علمية تتحوّل إلى قصص مصوّرة وشروح واضحة باللغتين.'),
 ('radar', '#2c6e72', '04', 'Self-updating knowledge', 'New discoveries are found, read and checked every week, so the map never goes stale.', 'معرفة تُحدِّث نفسها', 'تُرصد الاكتشافات الجديدة وتُقرأ وتُراجع كل أسبوع، فلا تشيخ الخريطة.'),
 ('route', '#2c7a4c', '05', 'Science into journeys', 'Knowledge becomes destinations, thematic routes and learning experiences for visitors.', 'من العلم إلى الرحلات', 'تتحوّل المعرفة إلى وجهات ومسارات موضوعية وتجارب تعلّم للزوّار.')]
INNO17 = [('g1', '#5847b0', [('layers', 'Multidisciplinary integration', 'Geology, archaeology and ecology in one exploration experience.', 'تكامل متعدد التخصصات', 'الجيولوجيا والآثار والبيئة في تجربة استكشاف واحدة.'),
   ('link', 'Cross-disciplinary interpretation', 'AI finds relationships between disciplines instead of listing disconnected facts.', 'تفسير عابر للتخصصات', 'يجد الذكاء الاصطناعي العلاقات بين التخصصات بدل سرد حقائق متفرقة.'),
   ('spark', 'AI-powered hypotheses', 'Possible links not yet documented, e.g. geology shaping ancient settlement — clearly separated from established findings.', 'فرضيات مدعومة بالذكاء الاصطناعي', 'روابط محتملة لم تُوثَّق بعد، مثل تأثير الجيولوجيا على الاستيطان القديم، مفصولة بوضوح عن النتائج المثبتة.'),
   ('book', 'Research democratisation', 'Papers and technical reports become stories, visuals and interactive experiences.', 'تبسيط البحث العلمي', 'تتحوّل الأوراق والتقارير التقنية إلى قصص ورسوم وتجارب تفاعلية.'),
   ('radar', 'Automated heritage discovery', 'Credible sources are monitored for newly documented sites, prepared for verification.', 'اكتشاف تراثي آلي', 'تُرصد مصادر موثوقة بحثًا عن مواقع موثَّقة حديثًا وتُجهَّز للمراجعة.'),
   ('globe', 'Interconnected knowledge', 'Similarities between distant places, including across the six countries.', 'معرفة مترابطة', 'أوجه الشبه بين أماكن متباعدة، حتى عبر الدول الست.'),
   ('clock', 'Space and time together', 'Geography combined with geological time, archaeological chronology and environmental change.', 'المكان والزمان معًا', 'الجغرافيا مع الزمن الجيولوجي والتسلسل الأثري والتغيّر البيئي.')]),
 ('g2', '#b4521c', [('compass', 'Intelligent discovery', 'Find destinations by interest: geological wonders, ancient civilisations, living ecosystems.', 'اكتشاف ذكي', 'اعثر على الوجهات حسب الاهتمام: عجائب جيولوجية، حضارات قديمة، نظم بيئية حية.'),
   ('route', 'Thematic journeys', 'Routes that connect places by a shared scientific, historical or environmental theme.', 'رحلات موضوعية', 'مسارات تربط الأماكن بموضوع علمي أو تاريخي أو بيئي مشترك.'),
   ('pin', 'Context-aware recommendations', 'Suggestions by interest, location, time available and what each place offers.', 'توصيات واعية بالسياق', 'اقتراحات حسب الاهتمام والموقع والوقت المتاح وما يقدّمه كل مكان.'),
   ('school', 'Educational tourism', 'Destinations become learning experiences for families, students and enthusiasts.', 'سياحة تعليمية', 'تتحوّل الوجهات إلى تجارب تعلّم للعائلات والطلاب والهواة.'),
   ('eye', 'Hidden heritage', 'Overlooked places that conventional tourism platforms do not highlight.', 'تراث خفي', 'أماكن مُهمَلة لا تُبرزها منصات السياحة التقليدية.')]),
 ('g3', '#2c6e72', [('leaf', 'Living platform', 'Content evolves as new research and verified information arrive.', 'منصة حية', 'يتطوّر المحتوى مع وصول أبحاث جديدة ومعلومات مُراجعة.'),
   ('check', 'Transparent validation', 'Published evidence, scientific interpretation and AI hypotheses are kept apart.', 'تحقق شفاف', 'تُفصل الأدلة المنشورة عن التفسير العلمي وعن فرضيات الذكاء الاصطناعي.'),
   ('people', 'Citizen science', 'Visitors, researchers and communities can contribute observations and finds.', 'علم المواطن', 'يمكن للزوّار والباحثين والمجتمعات المساهمة بالملاحظات والاكتشافات.'),
   ('map', 'One regional framework', 'Six countries explored through a common geographical-heritage lens.', 'إطار إقليمي واحد', 'ست دول تُستكشف عبر عدسة تراث جغرافي مشتركة.'),
   ('chart', 'Visual storytelling', 'Interactive maps, layers and timelines explain what text and photos cannot.', 'سرد بصري', 'خرائط وطبقات وخطوط زمنية تفاعلية تشرح ما لا يشرحه النص والصور.')])]
def inno5():
    out = ''
    for n, (ic, c, num, en, d, ar, da) in enumerate(INNO5):
        EN[f'i{n}'] = en; AR[f'i{n}'] = ar; EN[f'i{n}d'] = d; AR[f'i{n}d'] = da
        out += f'<div class="ic" style="--c:{c}"><i><svg viewBox="0 0 24 24">{IC[ic]}</svg></i><small>{num}</small><b data-i="i{n}">{en}</b><span data-i="i{n}d">{d}</span></div>'
    return out
def inno17():
    out = ''; n = 0
    for g, c, items in INNO17:
        out += f'<div class="igroup" data-i="{g}">{EN[g]}</div><div class="ilist">'
        for ic, en, d, ar, da in items:
            EN[f'j{n}'] = en; AR[f'j{n}'] = ar; EN[f'j{n}d'] = d; AR[f'j{n}d'] = da
            out += f'<div><i style="--c:{c}"><svg viewBox="0 0 24 24">{IC[ic]}</svg></i><div><b data-i="j{n}">{en}</b><span data-i="j{n}d">{d}</span></div></div>'; n += 1
        out += '</div>'
    return out

def engine(cnt=None):
    cnt = cnt or {}
    C = {'geo': '#5847b0', 'arch': '#b4521c', 'eco': '#2c7a4c', 'gold': '#c99a2e'}
    ins = [('lgeo', 120, C['geo'], 'M120 50 V112 H262 V178'), ('larch', 300, C['arch'], 'M300 50 V178'), ('leco', 480, C['eco'], 'M480 50 V112 H338 V178')]
    outs = [('o1', 120, 'M262 322 V372 H120 V408'), ('o2', 300, 'M300 322 V408'), ('o3', 480, 'M338 322 V372 H480 V408')]
    s = ''
    # research feeds the engine from the left; a human check sits on the way out at the right; new stories feed back to the top (always growing)
    side = [('src', 'srcs', 110, 'M200 250 H226', C['gold'], 'M-7 -8h14v16h-14zM-3 -3h6M-3 1h6M-3 5h3'), ('hum', 'hums', 490, 'M374 250 H400', '#2fbf71', 'M-7 0l5 5 9-9')]
    for k, k2, x, d, c, ic in side:
        s += f'<path class="tr" d="{d}" stroke="{c}" opacity=".35"/><path class="tr f" d="{d}" stroke="{c}"/><circle r="5" fill="{c}"><animateMotion dur="1.2s" repeatCount="indefinite" path="{d}"/></circle>'
        s += f'<rect x="{x-90}" y="226" width="180" height="48" rx="24" fill="#fffaf0" stroke="{c}" stroke-width="2"/><path d="{ic}" transform="translate({x-66} 250)" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        s += f'<text class="otx" x="{x+10}" y="246" data-i="{k}">{EN[k]}</text><text class="stx" x="{x+10}" y="263" data-i="{k2}">{EN[k2]}</text>'
    loop = 'M20 250 H2 V-8 H480 V14'  # new research adds new places to all three layers
    s += ''.join(f'<path class="tr" d="M{x} -8 V14" stroke="{C["gold"]}" opacity=".3" stroke-dasharray="4 7"/>' for x in (120, 300))
    s += f'<path class="tr" d="{loop}" stroke="{C["gold"]}" opacity=".3" stroke-dasharray="4 7"/><circle r="5" fill="{C["gold"]}"><animateMotion dur="5s" repeatCount="indefinite" path="{loop}"/></circle>'
    s += f'<text class="stx" x="-8" y="140" transform="rotate(-90 -8 140)" text-anchor="middle" data-i="loop" fill="{C["gold"]}" font-weight="700" letter-spacing="1">{EN["loop"]}</text>'
    for k, x, c, d in ins:
        s += f'<path class="tr" d="{d}" stroke="{c}" opacity=".35"/><path class="tr f" d="{d}" stroke="{c}"/>'
        s += f'<circle r="6" fill="{c}"><animateMotion dur="1.8s" repeatCount="indefinite" path="{d}" begin="{(x%7)*.15:.2f}s"/></circle>'
        s += f'<rect x="{x-78}" y="14" width="156" height="38" rx="19" fill="{c}"/><text class="etx" x="{x}" y="38" data-i="{k}">{EN[k]}</text>'
        if k in cnt: s += f'<g class="bdg"><circle cx="{x+74}" cy="16" r="15" fill="#fffaf0" stroke="{c}" stroke-width="2"/><text x="{x+74}" y="20.5" text-anchor="middle" font-family="Instrument Sans,system-ui,sans-serif" font-weight="700" font-size="11.5" fill="{c}">{cnt[k]}</text></g>'
    for k, x, d in outs:
        s += f'<path class="tr" d="{d}" stroke="{C["gold"]}" opacity=".35"/><path class="tr f" d="{d}" stroke="{C["gold"]}"/>'
        s += f'<circle r="5" fill="{C["gold"]}"><animateMotion dur="1.6s" repeatCount="indefinite" path="{d}" begin="{.9+(x%5)*.1:.2f}s"/></circle>'
        s += f'<rect x="{x-74}" y="408" width="148" height="38" rx="19" fill="#fffaf0" stroke="{C["gold"]}" stroke-width="2"/><text class="otx" x="{x}" y="432" data-i="{k}">{EN[k]}</text><text class="stx" x="{x}" y="466" data-i="{k}s">{EN[k+"s"]}</text>'
        if k in cnt: s += f'<g class="bdg"><circle cx="{x+70}" cy="410" r="15" fill="{C["gold"]}"/><text x="{x+70}" y="414.5" text-anchor="middle" font-family="Instrument Sans,system-ui,sans-serif" font-weight="700" font-size="11.5" fill="#fffaf0">{cnt[k]}</text></g>'
    pins = ''
    for i in range(6):
        o = 234 + i * 26.4
        pins += f'<rect class="pin" x="{o:.1f}" y="170" width="6" height="10" rx="2"/><rect class="pin" x="{o:.1f}" y="320" width="6" height="10" rx="2"/><rect class="pin" x="220" y="{o-54:.1f}" width="10" height="6" rx="2"/><rect class="pin" x="370" y="{o-54:.1f}" width="10" height="6" rx="2"/>'
    grid = ''.join(f'<path d="M{258+i*14} 208V292M258 {208+i*14}H342" stroke="#2c6e72" stroke-width="1" opacity=".55"/>' for i in range(7))
    leds = ''.join(f'<circle class="blink b{i+1}" cx="{246+i*12}" cy="314" r="2.6" fill="#7fe0c6"/>' for i in range(3))
    chip = (f'<circle cx="300" cy="250" r="118" fill="none" stroke="#c99a2e" stroke-width="1.5" stroke-dasharray="3 9" class="rot" opacity=".7"/>'
            f'<circle cx="300" cy="250" r="100" fill="none" stroke="#2c6e72" stroke-width="2" stroke-dasharray="22 12" class="rot2" opacity=".6"/>'
            f'{pins}<rect class="chip" x="226" y="176" width="148" height="148" rx="18"/>'
            f'<g class="coreg"><rect x="252" y="202" width="96" height="96" rx="10" fill="#0e1918" stroke="#2c6e72" stroke-width="1.5"/>{grid}'
            f'<rect class="scan" x="254" y="204" width="92" height="8" fill="#7fe0c6" opacity=".5" rx="3"/></g>'
            + ''.join(f'<g opacity="0"><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.06;.28;.34;1" dur="6s" begin="{(i-1)*2}s" repeatCount="indefinite"/><text x="300" y="287" text-anchor="middle" font-family="Instrument Sans,system-ui,sans-serif" font-weight="600" font-size="9" fill="#7fe0c6" data-i="cy{i}">{EN[f"cy{i}"]}</text></g>' for i in (1, 2, 3)) +
            f'<text x="300" y="262" text-anchor="middle" font-family="Instrument Sans,system-ui,sans-serif" font-weight="700" font-size="34" fill="#f6c24a" letter-spacing="2">AI</text>'
            f'<text x="300" y="196" text-anchor="middle" font-family="Instrument Sans,system-ui,sans-serif" font-weight="700" font-size="9.5" fill="#c99a2e" letter-spacing="2.5" data-i="eng">{EN["eng"]}</text>{leds}')
    return f'<svg viewBox="-22 -16 628 492" role="img" aria-label="AI engine connecting the geological, archaeological and ecological layers, fed by new research and checked by people">{s}{chip}</svg>'

KID = kidbg.uri(kidbg.button()) + " center/100% 100% no-repeat"
def chipcss(sel_i, keyattr):
    return ''.join(f"html[data-mode=e] {sel_i.replace('K', k)}{{background:{cartoon.uri(v)} center/contain no-repeat;width:16px;height:16px;border-radius:0}}" for k, v in cartoon.CHIP.items() if k in ('archaeological', 'geological', 'ecology', 'speculative', 'stories'))
# Explorer mode: same theme and the same map as Researcher; only the bars become stickers (cartoon icons, thick rounded outlines)
U = cartoon.uri
MODE_CANON = (
 "§{position:relative;width:96px;height:34px;flex:none;padding:0;border-radius:999px;border:1px solid rgba(0,0,0,.3);overflow:hidden;background:#5a4635;box-shadow:inset 0 2px 6px rgba(0,0,0,.3);display:block;cursor:pointer}"
 "§ button{position:absolute;inset:0;margin:0;padding:0;border:0;border-radius:999px;font-size:0;color:transparent;cursor:pointer;transition:opacity .6s}"
 f"§ button[data-m=r]{{background:{U(cartoon.MODE_R2)} center/100% 100% no-repeat!important}}§ button[data-m=e]{{background:{U(cartoon.MODE_E2)} center/100% 100% no-repeat!important}}"
 "§ button svg,§ button span{display:none}"
 "§ button[aria-pressed=true]{opacity:1;z-index:1}§ button[aria-pressed=false]{opacity:0;z-index:2}"
 "§::before,§::after{content:'';position:absolute;z-index:3;top:3px;left:3px;width:28px;height:28px;border-radius:50%;pointer-events:none;filter:drop-shadow(0 2px 3px rgba(0,0,0,.4));transition:transform .6s cubic-bezier(.65,0,.3,1),opacity .5s;background:center/contain no-repeat}"
 f"§::before{{background:linear-gradient(110deg,transparent 35%,rgba(255,255,255,.8) 50%,transparent 65%) 160% 0/260% 100% no-repeat,{U(cartoon.KNOB_R)} center/contain no-repeat;animation:kshine 4.2s ease-in-out infinite}}§::after{{background:linear-gradient(110deg,transparent 35%,rgba(255,255,255,.8) 50%,transparent 65%) 160% 0/260% 100% no-repeat,{U(cartoon.KNOB_E)} center/contain no-repeat;opacity:0;animation:kshine 4.2s ease-in-out infinite}}"
 "§.e::before,§.e::after{transform:translateX(62px)}"
 "§.e::before{opacity:0}§.e::after{opacity:1}"
 "§:hover::before,§:hover::after{filter:drop-shadow(0 3px 5px rgba(0,0,0,.5)) brightness(1.06)}"
 "@media (max-width:560px){§{width:84px;height:30px}§::before,§::after{width:24px;height:24px}§.e::before,§.e::after{transform:translateX(54px)}}"
 ".modelbl{font:700 11.5px var(--f-body);letter-spacing:.14em;text-transform:uppercase;color:var(--mut);white-space:nowrap;margin-inline-start:8px}.modelbl.e{color:#e8a24a}.modelbl.r{color:var(--ink)}"
)
# Explorer mode in the editions: each rail tile becomes a hand-drawn sticker (white disc, thick ink outline, tilted, icon filled with the layer colour)
TILE_E = ("html[data-mode=e] .tile{background:#fff;background:color-mix(in srgb,var(--c) 38%,#fff);color:#3b2d52;border-radius:50%;border:2.5px solid #3b2d52;box-shadow:0 3px 0 rgba(59,45,82,.35);transform:rotate(-6deg);transition:transform .25s cubic-bezier(.3,1.5,.5,1)}"
 "html[data-mode=e] #rail button:nth-child(even) .tile,html[data-mode=e] #rail a:nth-child(even) .tile{transform:rotate(5deg)}"
 "html[data-mode=e] #rail button:hover .tile,html[data-mode=e] #rail a:hover .tile{transform:rotate(-12deg) scale(1.08)}"
 "html[data-mode=e] .tile>svg{width:27px;height:27px;stroke-width:2.2;filter:drop-shadow(1px 1px 0 rgba(255,255,255,.8))}"
 "html[data-mode=e] .tile::after{content:'';position:absolute;top:6px;left:9px;width:9px;height:5px;border-radius:50%;background:#fff;opacity:.9;transform:rotate(-30deg)}"
 "html[data-mode=e] .sbk{background:#ffd33d;border:2px solid #3b2d52;width:19px;height:19px;transform:rotate(6deg)}html[data-mode=e] .sbk svg{width:11px;height:11px;color:#3b2d52;fill:none}"
 "html[data-mode=e] .tile.sp{background:#fff3c4}")
LOGO_SHINE = ("@keyframes kshine{0%,62%{background-position:160% 0,center}100%{background-position:-60% 0,center}}"
 "@keyframes lglow{0%,100%{filter:none}4%{filter:brightness(1.18) drop-shadow(0 0 6px rgba(255,214,120,.9))}9%{filter:none}}"
 ".lgs .lg:not(.on):not(.lghome) svg{animation:lglow 10s ease-in-out infinite}"
 + ''.join(f".lgs .lg:nth-child({i}) svg{{animation-delay:{(i-1)*.5:.1f}s}}" for i in range(1, 9)))
def mode_css(ids):
    return ''.join(MODE_CANON.replace('§', A) for A in ids)
SWITCH_CSS = (mode_css(["#modes", "#hmodes", "#demo"]) + LOGO_SHINE +
 # light / dark: sky with clouds and a sun that slides right and becomes a moon over a starry night
 ".thm{position:relative;width:72px;height:34px;border-radius:999px;border:1px solid rgba(0,0,0,.25);padding:0;cursor:pointer;overflow:hidden;background:none;flex:none;box-shadow:inset 0 2px 6px rgba(0,0,0,.25)}"
 f".thm::before,.thm::after{{content:'';position:absolute;inset:0;background:{U(cartoon.DAY)} center/100% 100% no-repeat;transition:opacity .6s}}"
 f".thm::after{{background:{U(cartoon.NIGHT)} center/100% 100% no-repeat;opacity:0}}.thm[aria-pressed=true]::after{{opacity:1}}"
 ".thm i{position:absolute;z-index:2;top:3px;left:3px;width:28px;height:28px;border-radius:50%;transition:transform .6s cubic-bezier(.65,0,.3,1);filter:drop-shadow(0 2px 3px rgba(0,0,0,.35))}"
 f".thm i::before,.thm i::after{{content:'';position:absolute;inset:0;background:{U(cartoon.SUN)} center/contain no-repeat;transition:opacity .5s,transform .6s}}"
 f".thm i::after{{background:{U(cartoon.MOON)} center/contain no-repeat;opacity:0;transform:rotate(-90deg)}}"
 ".thm[aria-pressed=true] i{transform:translateX(38px)}html[dir=rtl] .thm[aria-pressed=true] i{transform:translateX(-38px)}.thm[aria-pressed=true] i::before{opacity:0;transform:rotate(90deg)}.thm[aria-pressed=true] i::after{opacity:1;transform:none}"
 "@media (max-width:560px){.thm{width:56px;height:30px}.thm i{width:24px;height:24px}.thm[aria-pressed=true] i{transform:translateX(26px)}html[dir=rtl] .thm[aria-pressed=true] i{transform:translateX(-26px)}}"
 "@media (prefers-reduced-motion:reduce){.thm i,#modes::before,#hmodes::before{transition:none}}")
KID_CSS = (SWITCH_CSS +
 ".seg button[data-m=e][aria-pressed=true]{color:#2b2340}"
 "html[data-mode=e] .chip,html[data-mode=e] .hchip{background:#fff;color:#3b2d52;border-color:#4a3350;box-shadow:0 2px 0 rgba(74,51,80,.35);font-weight:700}"
 "html[data-mode=e] .chip[aria-pressed=true]{background:var(--c);color:#fff;border-color:#4a3350}html[data-mode=e] .hchip,html[data-mode=e] .hchip b{color:#3b2d52!important;background:#fff!important}"
 + chipcss('.chip[data-k=K] i', 'data-k') + chipcss('.hchip[data-k=K] i', 'data-k') +
 "html[data-mode=e] .seg{background:#fff;border-color:#4a3350;box-shadow:0 2px 0 rgba(74,51,80,.35)}html[data-mode=e] .seg button{color:#4a3350;font-weight:700}html[data-mode=e] .seg button[aria-pressed=true]:not([data-m=e]){background:#4a3350;color:#fff}"
 "html[data-mode=e] .ob,html[data-mode=e] .lang,html[data-mode=e] #go,html[data-mode=e] .srch,html[data-mode=e] #q{background:#fff;color:#4a3350;border-color:#4a3350;box-shadow:0 2px 0 rgba(74,51,80,.35);font-weight:700}"
 "html[data-mode=e] .arail a i.ir{display:none}html[data-mode=e] .arail a i.ie{display:grid}"
 "html[data-mode=e] .ob.ic2 .ir{display:none}html[data-mode=e] .ob.ic2 .ie{display:inline-block;width:16px;height:16px}"
 f"html[data-mode=e] #hviews button[data-v=map]::before{{content:'';width:16px;height:16px;background:{cartoon.uri(cartoon.CHIP['map'])} center/contain no-repeat}}"
 f"html[data-mode=e] #hviews button[data-v=tl]::before{{content:'';width:16px;height:16px;background:{cartoon.uri(cartoon.CHIP['tl'])} center/contain no-repeat}}"
 f"html[data-mode=e] #hviews button[data-v=cmp]::before{{content:'';width:16px;height:16px;background:{cartoon.uri(cartoon.CHIP['cmp'])} center/contain no-repeat}}"
 "html[data-mode=e] #hviews button{display:inline-flex;align-items:center;gap:5px}"
 f"html[data-mode=e] #go::before{{content:'';width:16px;height:16px;background:{cartoon.uri(cartoon.CHIP['live'])} center/contain no-repeat;display:inline-block;vertical-align:-5px;margin-inline-end:4px}}"
 "html[data-mode=e] .rail .tile,html[data-mode=e] #rail button i,html[data-mode=e] .tile i{border-radius:50%;border:2px solid #4a3350;box-shadow:0 3px 0 rgba(74,51,80,.35)}"
 "html[data-mode=e] .deco{color:var(--mut)}")
EXPL_CSS = (KID_CSS + ".seg button svg{width:15px;height:15px;vertical-align:-3px;margin-inline-end:5px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}")
ICO_R = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 4.5h7a2.5 2.5 0 0 1 2.5 2.5v13.5a2 2 0 0 0-2-2h-7.5z" fill="#3f7cc0" stroke="#1d4f8a" stroke-width="1.4" stroke-linejoin="round"/><path d="M20.5 4.5h-7a2.5 2.5 0 0 0-2.5 2.5v13.5a2 2 0 0 1 2-2h7.5z" fill="#6aa6e8" stroke="#1d4f8a" stroke-width="1.4" stroke-linejoin="round"/><path d="M6 8.5h4M6 11.5h4M14 8.5h4M14 11.5h4" stroke="#eaf3ff" stroke-width="1.2" stroke-linecap="round"/><path d="M12 7v13.5" stroke="#1d4f8a" stroke-width="1.4"/></svg>'
ICO_E = '<svg viewBox="0 0 24 24" aria-hidden="true"><g stroke="#f4a823" stroke-width="2.2" stroke-linecap="round" fill="none"><path d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M4.8 4.8l2.1 2.1M17.1 17.1l2.1 2.1M4.8 19.2l2.1-2.1M17.1 6.9l2.1-2.1"/></g><circle cx="12" cy="12" r="4.6" fill="#ffd33d" stroke="#f4a823" stroke-width="1.6"/></svg>'

HOWSTEPS = [('Sources', 'Journals, heritage bodies, surveys, museums and news about these places are monitored.', 'المصادر', 'تُرصد المجلات العلمية وهيئات التراث والمسوح والمتاحف والأخبار عن هذه الأماكن.'),
 ('Regular check', 'Every week the agent looks for new papers and announcements.', 'فحص منتظم', 'كل أسبوع يبحث الوكيل عن أوراق وإعلانات جديدة.'),
 ('Read & extract', 'Each source is opened and read; place, dates, team and measurements are taken only from what it says.', 'قراءة واستخراج', 'يُفتح كل مصدر ويُقرأ؛ وتؤخذ الأماكن والتواريخ والفِرق والقياسات مما يقوله فقط.'),
 ('Write EN + AR', 'A record, an explorer title and a summary are written in both languages, with the reference kept.', 'كتابة بالعربية والإنجليزية', 'يُكتب سجل وعنوان استكشافي وملخص باللغتين مع الاحتفاظ بالمرجع.'),
 ('Human check', 'Nothing is published until a person reviews it.', 'مراجعة بشرية', 'لا يُنشر شيء قبل أن يراجعه إنسان.'),
 ('Publish', 'The map, timeline and stories update; AI connections stay labelled as untested ideas.', 'نشر', 'تُحدَّث الخريطة والخط الزمني والقصص؛ وتبقى الروابط الذكية مُعلَّمة كأفكار غير مختبَرة.')]
def pipe():
    n = len(HOWSTEPS); W = 880; xs = [60 + i * (W - 120) / (n - 1) for i in range(n)]
    g = ''
    for i in range(n - 1): g += f'<path class="lnk" d="M{xs[i]+26:.0f} 70 H{xs[i+1]-26:.0f}"/>'
    ic = ['M-9 -8h18v16h-18zM-5 -3h10M-5 2h10', 'M-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0M0 -5v5l4 3', 'M-7 -9h10l4 4v14h-14zM-3 0h6M-3 4h6', 'M-9 -7h18v14h-18zM-4 -2h8M-4 2h5', 'M-8 1l5 5 11-11', 'M-9 4l9-12 9 12zM-4 8h8']
    for i, (en, d, ar, da) in enumerate(HOWSTEPS):
        auto = i in (1, 2, 3, 5)
        g += (f'<g class="pulse" style="animation-delay:{i*.4:.1f}s"><circle class="ring{" auto" if auto else ""}" cx="{xs[i]:.0f}" cy="70" r="26"/>'
              f'<path d="{ic[i]}" transform="translate({xs[i]:.0f} 70)" fill="none" stroke="{"#c99a2e" if auto else "#2c6e72"}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>'
              f'<text class="st" x="{xs[i]:.0f}" y="118" data-i="hs{i}">{en}</text><text class="ss" x="{xs[i]:.0f}" y="134" data-i="hsk{i}">{"automatic" if auto else "human"}</text>')
    g += f'<circle r="6" fill="#c99a2e"><animateMotion dur="7s" repeatCount="indefinite" path="M{xs[0]:.0f} 70 H{xs[-1]:.0f}"/></circle>'
    return f'<svg viewBox="0 0 {W} 150" role="img" aria-label="How research reaches the map">{g}</svg>'

SUBSURFACE = {'bahrah-hydrothermal', 'dextral-slip-fault', 'wadi-batin-fault'}  # dated at depth, not an outcrop
def pipe_v():
    n = len(HOWSTEPS); H = 60 + (n - 1) * 86; x = 44
    g = f'<path class="lnk" d="M{x} 40 V{H-20}"/>'
    ic = ['M-9 -8h18v16h-18zM-5 -3h10M-5 2h10', 'M-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0M0 -5v5l4 3', 'M-7 -9h10l4 4v14h-14zM-3 0h6M-3 4h6', 'M-9 -7h18v14h-18zM-4 -2h8M-4 2h5', 'M-8 1l5 5 11-11', 'M-9 4l9-12 9 12zM-4 8h8']
    for i, (en, d, ar, da) in enumerate(HOWSTEPS):
        y = 40 + i * 86; auto = i in (1, 2, 3, 5)
        g += (f'<g class="pulse" style="animation-delay:{i*.4:.1f}s"><circle class="ring{" auto" if auto else ""}" cx="{x}" cy="{y}" r="24"/>'
              f'<path d="{ic[i]}" transform="translate({x} {y})" fill="none" stroke="{"#c99a2e" if auto else "#2c6e72"}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>'
              f'<text class="st" x="{x+40}" y="{y-4}" text-anchor="start" data-i="hs{i}">{en}</text><text class="ss" x="{x+40}" y="{y+14}" text-anchor="start" data-i="hsk{i}">{EN.get("hsk"+str(i), "")}</text>')
    g += f'<circle r="6" fill="#c99a2e"><animateMotion dur="7s" repeatCount="indefinite" path="M{x} 40 V{H-20}"/></circle>'
    return f'<svg class="pv" viewBox="0 0 420 {H}" role="img" aria-label="How research reaches the map">{g}</svg>'
def howflow():
    ic = ['<path d="M4 6h16v12H4zM8 10h8M8 14h5"/>', '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', '<path d="M6 3h9l4 4v14H6zM9 12h6M9 16h6"/>', '<path d="M4 6h16v12H4zM8 10h8M8 14h4"/><path d="M17 15l2 2 3-3" />', '<circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/><path d="M17 11l2 2 3-3"/>', '<path d="M3 11l9-7 9 7v9H3z"/><path d="M9 20v-6h6v6"/>']
    out = '<div class="flow"><svg class="spine" viewBox="0 0 60 100" preserveAspectRatio="none"><path d="M30 0V100"/><path class="f" d="M30 0V100"/></svg>'
    for i, (en, d, ar, da) in enumerate(HOWSTEPS):
        auto = i in (1, 2, 3, 5)
        out += (f'<div class="step{" auto" if auto else ""}"><div class="card"><b data-i="hs{i}">{en}</b><span data-i="hsd{i}">{d}</span><br><small data-i="hsk{i}">{EN["hsk"+str(i)]}</small></div>'
                f'<div class="node"><svg viewBox="0 0 24 24">{ic[i]}</svg></div></div>')
    return out + '</div>'
def growmap():
    W, Hh = map2.W, map2.H
    gc = ''.join(f'<path d="{MD["gcc"][cc]}" fill="var(--land)" stroke="var(--coast)" stroke-width="1.2"/>' for cc in ORDER)
    import random; rng = random.Random(11); pins = ''
    pts = []
    for cc in ORDER:
        for x in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']:
            if x.get('lat') and x.get('lng'): pts.append((x['lng'], x['lat'], x['c']))
    rng.shuffle(pts); COL = {'geological': 'var(--geo)', 'archaeological': 'var(--arch)', 'ecology': 'var(--eco)'}
    for i, (lng, lat, c) in enumerate(pts[:160]):
        px, py = map2.P(lng, lat); pins += f'<circle class="gp" cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{COL.get(c, "#bf2f7d")}" style="animation-delay:{i*.09:.2f}s"/>'
    x0, y0 = map2.P(33.5, 33.5); x1, y1 = map2.P(61.5, 11.5)
    return f'<svg class="gm" viewBox="{x0:.0f} {y0:.0f} {x1-x0:.0f} {y1-y0:.0f}" role="img" aria-label="The map growing"><rect x="{x0:.0f}" y="{y0:.0f}" width="{x1-x0:.0f}" height="{y1-y0:.0f}" rx="24" fill="var(--sea)"/>{gc}{pins}<circle class="gw" cx="{map2.P(50,27)[0]:.0f}" cy="{map2.P(50,27)[1]:.0f}" r="40" fill="none" stroke="#c99a2e" stroke-width="3"/></svg>'
SUBSURFACE_ = None
def gulf_stats():
    rows = {}
    for cc in ORDER:
        sites = json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']
        if cc == 'kw':
            AG = runpy.run_path('/tmp/w/ages.py')['G']
            for x in sites:
                if x['id'] in AG: x['t0'], x['t1'] = AG[x['id']]
        geo = [x for x in sites if x['c'] == 'geological' and x.get('t0') and x['id'] not in SUBSURFACE]
        arc = [x for x in sites if x['c'] == 'archaeological' and x.get('t0')]
        og = max(geo, key=lambda x: x['t0']); oa = max(arc, key=lambda x: x['t0'])
        if cc == 'kw': pa, whs = 12, 0
        else:
            pz = json.load(open(f'/tmp/w/gulf/{cc}/config.json'))['protected']; pa = sum(1 for p in pz if p['t'] in 'rmfg'); whs = sum(1 for p in pz if p['t'] == 'u')
        ecl = [x for x in sites if x['c'] == 'ecology']; tiers = {t: sum(1 for x in ecl if ecotier.tier(x) == t) for t in ecotier.ORDER}
        rarest = max(ecl, key=lambda x: (ecotier.ORDER.index(ecotier.tier(x)), len(x.get('refs', []))))
        rows[cc] = dict(n=80 if cc == 'kw' else len(sites), eco=len(ecl), og=og, oa=oa, pa=pa, whs=whs, tiers=tiers, rarest=rarest)
    return rows
def yrs(t, ar=False):
    if t >= 1e6:
        v = t / 1e6; v = f'{v:.1f}'.rstrip('0').rstrip('.') if v < 10 else f'{v:.0f}'
        return f'{v} million yrs'
    return f'{int(round(t, -2 if t >= 10000 else -1)):,} yrs'
def yrs2(t):
    if t >= 1e6:
        v = t / 1e6; v = f'{v:.1f}'.rstrip('0').rstrip('.') if v < 10 else f'{v:.0f}'
        return bi(f'{v} million yrs', f'{v} مليون سنة', False)
    n = f'{int(round(t, -2 if t >= 10000 else -1)):,}'
    return bi(f'{n} yrs', f'{n} سنة', False)
def table(R):
    hd = ''.join(f'<th{" class=n" if i else ""} data-i="hc{i+1}">{EN["hc"+str(i+1)]}</th>' for i in (0, 1, 2, 3, 4, 7, 5, 6))
    tr = ''
    for cc in ORDER:
        r = R[cc]
        tr += (f'<tr><td><a href="#{cc}" style="text-decoration:none"><b data-i="n.{cc}">{EN["n."+cc]}</b></a></td><td class="n">{r["n"]}</td>'
               f'<td><b>{yrs2(r["og"]["t0"])}</b><small>{bi(esc(r["og"]["n"]), esc(r["og"].get("na", r["og"]["n"])), False)}</small></td><td><b>{yrs2(r["oa"]["t0"])}</b><small>{bi(esc(r["oa"]["n"]), esc(r["oa"].get("na", r["oa"]["n"])), False)}</small></td>'
               f'<td class="n">{r["eco"]}</td><td><span class="tier t-{ecotier.tier(r["rarest"])}" data-i="t.{ecotier.tier(r["rarest"])}">{EN["t."+ecotier.tier(r["rarest"])]}</span><small>{bi(esc(r["rarest"]["n"]), esc(r["rarest"].get("na", r["rarest"]["n"])), False)}</small></td><td class="n">{r["pa"]}</td><td class="n">{r["whs"]}</td></tr>')
    return f'<table class="tbl"><thead><tr>{hd}</tr></thead><tbody>{tr}</tbody></table>'
def timeline(R):
    import math
    W = 900; L, Rm = 100, 30; y0 = 30
    lo, hi = math.log10(2000), math.log10(6e8)
    X = lambda t: L + (W - L - Rm) * (math.log10(max(t, 2000)) - lo) / (hi - lo)
    g = ''
    for t, lab in ((2000, '2,000 yrs'), (10000, '10,000'), (100000, '100,000'), (1e6, '1 Ma'), (1e7, '10 Ma'), (1e8, '100 Ma'), (6e8, '600 Ma')):
        g += f'<line x1="{X(t):.0f}" y1="{y0}" x2="{X(t):.0f}" y2="{y0+6*34}" stroke="#d5dcd6"/><text class="ax" x="{X(t):.0f}" y="{y0+6*34+16}">{lab}</text>'
    for i, cc in enumerate(ORDER):
        r = R[cc]; y = y0 + i * 34 + 17
        g += f'<text class="nm" x="4" y="{y+4}" data-i="n.{cc}">{EN["n."+cc]}</text><line x1="{L}" y1="{y}" x2="{W-Rm}" y2="{y}" stroke="#eef1ec" stroke-width="10" stroke-linecap="round"/>'
        g += f'<line x1="{X(r["oa"]["t0"]):.0f}" y1="{y}" x2="{X(r["og"]["t0"]):.0f}" y2="{y}" stroke="#d5dcd6" stroke-width="3"/>'
        g += f'<circle cx="{X(r["og"]["t0"]):.0f}" cy="{y}" r="7" fill="#5847b0"><title>{r["og"]["n"]}</title></circle><circle cx="{X(r["oa"]["t0"]):.0f}" cy="{y}" r="7" fill="#b4521c"><title>{r["oa"]["n"]}</title></circle>'
    g += f'<circle cx="{L}" cy="{y0-14}" r="5" fill="#5847b0"/><text class="ax" x="{L+54}" y="{y0-10}">oldest rock</text><circle cx="{L+120}" cy="{y0-14}" r="5" fill="#b4521c"/><text class="ax" x="{L+190}" y="{y0-10}">oldest human trace</text>'
    return f'<svg viewBox="0 0 {W} {y0+6*34+26}" role="img" aria-label="Timeline across six countries">{g}</svg>'
def cut(t, n): return t if len(t) <= n else t[:n-1].rstrip(' (،,') + '…'
def bi(en, ar, svg=True):
    if svg: return f'<tspan class="le">{en}</tspan><tspan class="la">\u202b{ar}\u202c</tspan>'
    return f'<span class="le">{en}</span><span class="la">{ar}</span>'
def _scale(R, key, lo, hi, bands, fmt, mob=False):
    import math
    W = 900 if not mob else 470; L, Rm = (150, 64) if not mob else (104, 40); y0 = 44; rh = 36 if not mob else 40
    fs = '' if not mob else ' style="font-size:14px"'; fs2 = '' if not mob else ' style="font-size:12.5px"'
    lo_, hi_ = math.log10(lo), math.log10(hi)
    X = lambda t: L + (W - L - Rm) * (hi_ - math.log10(min(max(t, lo), hi))) / (hi_ - lo_)   # oldest at the left, today at the right
    Hh = y0 + 6 * rh
    g = ''
    for k, t0, t1, col in bands:   # era / period columns behind the rows
        x1, x2 = X(t0), X(t1)
        kk = k + ('s' if mob else ''); base = 12.5 if mob else 10.5; est = len(EN[kk]) * base * .82
        f0 = base if est <= x2 - x1 - 8 else max(7, base * (x2 - x1 - 8) / est)
        g += f'<rect x="{x1:.0f}" y="{y0-6}" width="{x2-x1:.0f}" height="{Hh-y0+6}" fill="{col}" opacity=".16"/><rect x="{x1:.0f}" y="{y0-30}" width="{x2-x1:.0f}" height="20" rx="4" fill="{col}" opacity=".9"/><text class="er" x="{(x1+x2)/2:.0f}" y="{y0-16}" fill="#fff" data-i="{kk}" style="font-size:{f0:.1f}px;letter-spacing:{0 if f0 < base else .08}em">{EN[kk]}</text>'
    rows = sorted(ORDER, key=lambda c: -R[c][key]['t0'])
    for i, cc in enumerate(rows):
        r = R[cc][key]; y = y0 + i * rh + rh / 2; x = X(r['t0']); col = '#5847b0' if key == 'og' else '#b4521c'
        g += (f'<line x1="{L}" y1="{y:.0f}" x2="{W-Rm}" y2="{y:.0f}" stroke="#d5dcd6" stroke-width="1" stroke-dasharray="2 4"/>'
              f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{W-Rm}" y2="{y:.0f}" stroke="{col}" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
              f'<circle cx="{W-Rm}" cy="{y:.0f}" r="4" fill="{col}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{col}"/><text class="rk" x="{x:.0f}" y="{y+4:.0f}">{i+1}</text>'
              f'<a href="#{cc}" style="text-decoration:none"><text class="nm" x="8" y="{y-3:.0f}" data-i="n.{cc}"{fs}>{EN["n."+cc]}</text></a><text class="pl" x="8" y="{y+11:.0f}"{fs2}>{bi(esc(cut(r["n"], 26 if not mob else 18)), esc(cut(r.get("na", r["n"]), 24 if not mob else 16)))}</text>'
              f'<text class="vl" x="{x+14:.0f}" y="{y-7:.0f}"{fs}>{fmt(r["t0"])}</text>')
    ticks = [t for t in (1e9, 5e8, 2e8, 1e8, 5e7, 2e7, 1e7, 2e6, 1e6, 5e5, 2e5, 1e5, 5e4, 2e4, 1e4, 5e3) if lo <= t <= hi]
    if mob: ticks = ticks[::2]
    ticks = [t for t in ticks if X(t) < W - Rm - 34]
    for t in ticks: g += f'<line x1="{X(t):.0f}" y1="{Hh}" x2="{X(t):.0f}" y2="{Hh+5}" stroke="#9aa6a5"/><text class="ax" x="{X(t):.0f}" y="{Hh+18}"{fs2}>{fmt(t)}</text>'
    g += f'<line x1="{L}" y1="{Hh}" x2="{W-Rm}" y2="{Hh}" stroke="#9aa6a5"/><text class="ax" x="{W-Rm}" y="{Hh+18}" data-i="now"{fs2}>{EN["now"]}</text>'
    return f'<svg class="ltrsvg {"sc" if mob else ""}" viewBox="0 0 {W} {Hh+26}" role="img" aria-label="Ranked time scale">{g}</svg>'
def geo_scale(R, mob=False):
    f = lambda t: (lambda v: bi(v + ' Ma', v + ' مليون'))(f'{t/1e6:.0f}' if t >= 1e7 else f'{t/1e6:.1f}'.rstrip('0').rstrip('.'))
    return _scale(R, 'og', 1e7, 1e9, [('e1', 1e9, 541e6, '#6b4a8a'), ('e2', 541e6, 252e6, '#5a7fb5'), ('e3', 252e6, 66e6, '#4f9a7a'), ('e4', 66e6, 1e7, '#d9a24a')], f, mob)
def arch_scale(R, mob=False):
    f = lambda t: (lambda v: bi(v + ' M', v + ' مليون'))(f'{t/1e6:.1f}'.rstrip('0').rstrip('.')) if t >= 1e6 else ((lambda v: bi(v + ' k', v + ' ألف'))(f'{t/1e3:.0f}') if t >= 2e4 else f'{int(t):,}')
    return _scale(R, 'oa', 5e3, 2e6, [('p1', 2e6, 3e5, '#8a5a3c'), ('p2', 3e5, 45e3, '#b4521c'), ('p3', 45e3, 12e3, '#d98c5f'), ('p4', 12e3, 5e3, '#c99a2e')], f, mob)
sys.path.insert(0, '/tmp/w/logo')
import logo as LOGO
def flag_badge(cc, pf):
    r = 40
    return (f'<svg viewBox="-46 -46 92 92" aria-hidden="true"><defs><clipPath id="{pf}"><circle r="{r}"/></clipPath></defs><circle r="45" fill="#fff"/>'
            f'<g clip-path="url(#{pf})">{LOGO.FLAGS[cc]["svg"](r)}</g><circle r="{r}" fill="none" stroke="rgba(0,0,0,.18)" stroke-width="3"/></svg>')
def gulf_timeline(R):
    import math
    ALL = {}
    for cc in ORDER:
        sites = json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']
        if cc == 'kw':
            AG = runpy.run_path('/tmp/w/ages.py')['G']
            for x in sites:
                if x['id'] in AG: x['t0'], x['t1'] = AG[x['id']]
        ALL[cc] = sites
    USED = {cc: [] for cc in ORDER}
    def scale(kind, lo, hi, bands, ticks, perc, n):
        lo_, hi_ = math.log10(lo), math.log10(hi)
        X = lambda t: 100 * (hi_ - math.log10(min(max(t, lo), hi))) / (hi_ - lo_)
        rows = []
        for cc in ORDER:
            sites = ALL[cc]; byid = {x['id']: x for x in sites}
            first = byid[R[cc]['og' if kind == 'geological' else 'oa']['id']]
            pick = [first] + sorted([x for x in sites if x['c'] == kind and x.get('t0') and x is not first and x['id'] not in SUBSURFACE], key=lambda x: -len(x.get('refs', [])))[:n - 1]
            rows += [(cc, x) for x in pick]; USED[cc] += pick
        rows.sort(key=lambda r: -r[1]['t0'])
        hd = '<div class="eras">' + ''.join(f'<span style="left:{X(a):.2f}%;width:{X(b)-X(a):.2f}%;background:{c}" data-i="{k}">{EN[k]}</span>' for k, a, b, c in bands) + '</div>'
        hd += '<div class="ticks">' + ''.join(f'<span style="left:{X(t):.2f}%" data-i="{k}">{EN[k]}</span>' for t, k in ticks) + '</div>'
        grid = '<div class="grid">' + ''.join(f'<i style="left:{X(t):.2f}%"></i>' for t, k in ticks) + '</div>'
        body = ''; col = 'var(--geo)' if kind == 'geological' else 'var(--arch)'; last = None
        for cc, x in rows:
            x0, x1 = X(x['t0']), X(x.get('t1') or lo)
            for k, a, b, c in bands:   # era label row when the era changes
                if a >= x['t0'] > b and last != k:
                    body += f'<div class="era"><b data-i="{k}">{EN[k]}</b><div class="bw"><i style="left:{X(a):.2f}%;background:{c}"></i></div></div>'; last = k
            name = f'<b><span class="rn" data-en="{esc(x["n"])}" data-ar="{esc(x.get("na") or x["n"])}">{esc(x["n"])}</span><span class="en" data-en="{esc(x.get("te") or x["n"])}" data-ar="{esc(x.get("ta") or x.get("na") or x["n"])}">{esc(x.get("te") or x["n"])}</span></b>'
            body += (f'<a class="row" href="#{cc}/p={x["id"]}" style="--c:{col}" title="{esc(EN["n."+cc])}"><span class="nm"><span class="fg">{flag_badge(cc, "fb" + kind[:1] + cc + x["id"][:8])}</span>{name}</span>'
                     f'<span class="bw"><em{' class="l"' if x0 > 58 else ''} style="left:{x0:.2f}%">{yrs2(x["t0"])}</em><span class="bar" style="left:{x0:.2f}%;width:{max(x1-x0,1):.2f}%"></span><span class="dot" style="left:{x0:.2f}%"></span></span></a>')
        ck = 'cnG' if perc == 'geo' else 'cnA'
        return f'<div class="gtl {perc}"><div class="hd"><span class="corner" data-i="{ck}">{EN[ck]}</span>{hd}</div><div class="rows">{grid}{body}</div></div>'
    geo = scale('geological', 1e6, 1e9,
        [('e1', 1e9, 541e6, '#6b4a8a'), ('e2', 541e6, 252e6, '#5a7fb5'), ('e3', 252e6, 66e6, '#4f9a7a'), ('e4', 66e6, 1e6, '#d9a24a')],
        [(1e9, 'tk0'), (1e8, 'tk1'), (1e7, 'tk2'), (1e6, 'tk3')], 'geo', 3)
    arc = scale('archaeological', 100, 2e6,
        [('p1', 2e6, 3e5, '#8a5a3c'), ('p2', 3e5, 45e3, '#b4521c'), ('p3', 45e3, 12e3, '#d98c5f'), ('p4', 12e3, 5.3e3, '#c99a2e'), ('p5', 5.3e3, 3.2e3, '#a0763a'), ('p6', 3.2e3, 2.3e3, '#7d8c3a'), ('p7', 2.3e3, 1.4e3, '#5a7fb5'), ('p8', 1.4e3, 100, '#2c6e72')],
        [(1e6, 'tk3'), (1e5, 'tk4'), (1e4, 'tk5'), (1e3, 'tk6'), (100, 'tk7')], 'arc', 4)
    import re as _re
    import ecotime
    TR = {t: i for i, t in enumerate(ecotier.ORDER)}
    def ename(x):
        return f'<b><span class="rn" data-en="{esc(x["n"])}" data-ar="{esc(x.get("na") or x["n"])}">{esc(x["n"])}</span><span class="en" data-en="{esc(x.get("te") or x["n"])}" data-ar="{esc(x.get("ta") or x.get("na") or x["n"])}">{esc(x.get("te") or x["n"])}</span></b>'
    def erow(cc, x, bw, note=None, extra=''):
        tg = ecotier.tier(x)
        nt = f'<small class="enote" data-en="{esc(note[0])}" data-ar="{esc(note[1])}">{esc(note[0])}</small>' if note else ''
        return (f'<a class="row" href="#{cc}/p={x["id"]}" style="--c:var(--t-{tg})"><span class="nm"><span class="fg">{flag_badge(cc, "fbe" + cc + x["id"][:8])}</span><span class="nmc">{ename(x)}{nt}<span class="tier t-{tg}" data-i="t.{tg}">{EN["t."+tg]}</span>{extra}</span></span><span class="bw">{bw}</span></a>')
    ECO = {cc: [x for x in ALL[cc] if x['c'] == 'ecology'] for cc in ORDER}
    # 1 · every year: a calendar
    MON = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']; MONL = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    MONA = ['ينا', 'فبر', 'مار', 'أبر', 'ماي', 'يون', 'يول', 'أغس', 'سبت', 'أكت', 'نوف', 'ديس']
    MONLA = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر']
    Xm = lambda m: 100 * (m - 1) / 12
    hd = '<div class="eras">' + ''.join(f'<span style="left:{Xm(m):.2f}%;width:{100/12:.2f}%;background:{["#5a7fb5","#5a7fb5","#4f9a7a","#4f9a7a","#4f9a7a","#d9a24a","#d9a24a","#d9a24a","#c9733a","#c9733a","#c9733a","#5a7fb5"][m-1]}">{bi(MON[m-1], MONA[m-1], False)}</span>' for m in range(1, 13)) + '</div>'
    grid = '<div class="grid">' + ''.join(f'<i style="left:{Xm(m):.2f}%"></i>' for m in range(1, 13)) + '</div>'
    body = ''; rows = []
    for cc in ORDER:
        for x in ECO[cc]:
            if x['id'] in ecotime.SEASON: rows.append((cc, x, ecotime.SEASON[x['id']]))
    rows.sort(key=lambda r: (r[2][0][0] if r[2][0][0] > 2 or len(r[2][0]) < 5 else 0, -TR[ecotier.tier(r[1])]))
    for cc, x, (ms, en, ar) in rows:
        segs = []; run = [ms[0]]
        for a, b in zip(ms, ms[1:]):
            if b == a + 1: run.append(b)
            else: segs.append(run); run = [b]
        segs.append(run)
        bars = ''.join(f'<span class="bar" style="left:{Xm(sg[0]):.2f}%;width:{100*len(sg)/12:.2f}%"></span>' for sg in segs)
        u = ecotime.UNIQUE.get(x['id'])
        uq = f'<span class="uq" data-en="★ {esc(u[0])}" data-ar="★ {esc(u[1])}">★ {esc(u[0])}</span>' if u else ''
        body += erow(cc, x, bars + f'<em{' class="l"' if Xm(segs[0][0]) > 70 else ''} style="left:{Xm(segs[0][0]):.2f}%">{bi(MONL[ms[0]-1] + "–" + MONL[ms[-1]-1], MONLA[ms[0]-1] + "–" + MONLA[ms[-1]-1], False)}</em>', (en, ar), uq); USED[cc].append(x)
    eco_s = f'<h4 class="eh" data-i="esT">{EN["esT"]}</h4><div class="gtl eco cal"><div class="hd"><span class="corner" data-i="cnS">{EN["cnS"]}</span>{hd}</div><div class="rows">{grid}{body}</div></div>'
    # 2 · ancient living places: their own age
    import math
    lo_, hi_ = math.log10(100), math.log10(20000); Xa = lambda t: 100 * (hi_ - math.log10(t)) / (hi_ - lo_)
    hd = '<div class="ticks">' + ''.join(f'<span style="left:{Xa(t):.2f}%">{l}</span>' for t, l in ((20000, '20,000'), (10000, '10,000'), (1000, '1,000'), (100, bi('100 yrs', '100 سنة', False)))) + '</div>'
    grid = '<div class="grid">' + ''.join(f'<i style="left:{Xa(t):.2f}%"></i>' for t in (20000, 10000, 1000, 100)) + '</div>'
    body = ''; rows = []
    for cc in ORDER:
        for x in ECO[cc]:
            if x['id'] in ecotime.ANCIENT: rows.append((cc, x, ecotime.ANCIENT[x['id']]))
    rows.sort(key=lambda r: -r[2][0])
    for cc, x, (age, en, ar) in rows:
        body += erow(cc, x, f'<em{' class="l"' if Xa(age) > 70 else ''} style="left:{Xa(age):.2f}%">{bi(f"{age:,} yrs", f"{age:,} سنة", False)}</em><span class="bar" style="left:{Xa(age):.2f}%;width:{100-Xa(age):.2f}%"></span><span class="dot" style="left:{Xa(age):.2f}%"></span>', (en, ar)); USED[cc].append(x)
    eco_a = f'<h4 class="eh" data-i="eaT">{EN["eaT"]}</h4><div class="gtl eco"><div class="hd"><span class="corner" data-i="cnA">{EN["cnA"]}</span>{hd}</div><div class="rows">{grid}{body}</div></div>'
    # 3 · everything else: the year it was recorded or protected
    erows = [(cc, x) for cc in ORDER for x in ECO[cc] if x.get('t0') and x['id'] not in ecotime.SEASON and x['id'] not in ecotime.ANCIENT]
    for cc, x in erows: USED[cc].append(x)
    Y0, Y1 = 1940, 2026; Xe = lambda yr: 100 * (max(Y0, min(Y1, yr)) - Y0) / (Y1 - Y0)
    hd = '<div class="ticks">' + ''.join(f'<span style="left:{Xe(y):.2f}%">{y}</span>' for y in range(1940, 2027, 20)) + '</div>'
    grid = '<div class="grid">' + ''.join(f'<i style="left:{Xe(y):.2f}%"></i>' for y in range(1940, 2027, 10)) + '</div>'
    import re as _r2
    def ryear(x):
        m = _r2.search(r'(1[89]\d\d|20[0-2]\d)', x.get('dr') or '')
        return int(m.group(1)) if m else None
    _p = '/tmp/w/arfix/eco_dr_ar.json'; DRAR = json.load(open(_p, encoding='utf-8')) if os.path.exists(_p) else {}
    erows.sort(key=lambda r: (ryear(r[1]) or 9999, -TR[ecotier.tier(r[1])])); body = ''
    for cc, x in erows:
        yr = ryear(x)
        bw = (f'<em{' class="l"' if Xe(yr) > 85 else ''} style="left:{Xe(yr):.2f}%">{yr}</em><span class="bar" style="left:{Xe(yr):.2f}%;width:{100-Xe(yr):.2f}%;opacity:.3"></span><span class="dot" style="left:{Xe(yr):.2f}%"></span>') if yr else '<em style="right:0">—</em>'
        body += erow(cc, x, bw, (x.get('dr') or '', DRAR.get(x.get('dr') or '', '')))
    eco_r = f'<h4 class="eh" data-i="erT2">{EN["erT2"]}</h4><div class="gtl eco"><div class="hd"><span class="corner" data-i="cnY">{EN["cnY"]}</span>{hd}</div><div class="rows">{grid}{body}</div></div>'
    legend = '<div class="tleg">' + ''.join(f'<div><span class="tier t-{t}" data-i="t.{t}">{EN["t."+t]}</span><small data-i="td.{t}">{EN["td."+t]}</small></div>' for t in reversed(ecotier.ORDER)) + '</div>'
    eco = (f'<div class="seg esw" role="group" id="esub"><button type="button" data-e="a" aria-pressed="true" data-i="eaS">{EN["eaS"]}</button><button type="button" data-e="s" aria-pressed="false" data-i="esS">{EN["esS"]}</button><button type="button" data-e="r" aria-pressed="false" data-i="erS2">{EN["erS2"]}</button></div>'
           f'<div class="esub on" data-e="a">{eco_a}</div><div class="esub" data-e="s">{eco_s}</div><div class="esub" data-e="r">{eco_r}</div>{legend}')
    refs = f'<div class="refs">'
    for cc in ORDER:
        seen = set(); items = ''
        for x in USED[cc]:
            for r in x.get('refs', []):
                t = r if isinstance(r, str) else (r.get('label') or r.get('t') or r.get('title') or ''); u = '' if isinstance(r, str) else (r.get('url') or r.get('u') or '')
                if not u:
                    m = _re.search(r'https?://\S+', t)
                    if m: u = m.group(0).rstrip('.)')
                key = t.strip()[:80]
                if not key or key in seen: continue
                seen.add(key)
                items += f'<li>{esc(t)}{(" <a href=%s target=_blank rel=noopener>↗</a>" % esc(u)) if u else ""}<small><span class="rn">{esc(x["n"])}</span><span class="en">{esc(x.get("te") or x["n"])}</span></small></li>'
        refs += f'<h4>{flag_badge(cc, "rf" + cc)}<span data-i="n.{cc}">{EN["n."+cc]}</span></h4><ol>{items}</ol>'
    refs += '</div>'
    return (f'<div class="tlwrap"><div class="seg tsw" role="group" id="tlkind"><button type="button" data-k="geo" aria-pressed="true" data-i="cg">{EN["cg"]}</button><button type="button" data-k="arc" aria-pressed="false" data-i="ca">{EN["ca"]}</button><button type="button" data-k="eco" aria-pressed="false" data-i="eco">{EN["eco"]}</button></div><div class="tlk on" data-k="geo">{geo}</div><div class="tlk" data-k="arc">{arc}</div><div class="tlk" data-k="eco">{eco}</div></div>', refs)
def rarity_bars(R):
    mx = max(R[c]['eco'] for c in ORDER); out = '<div class="rbars">'
    for cc in ORDER:
        segs = ''.join(f'<i class="t-{t}" style="width:{R[cc]["tiers"][t]/mx*100:.2f}%" title="{R[cc]["tiers"][t]}">{R[cc]["tiers"][t] or ""}</i>' for t in reversed(ecotier.ORDER))
        out += f'<div class="rb"><span class="fg">{flag_badge(cc, "rb" + cc)}</span><b data-i="n.{cc}">{EN["n."+cc]}</b><span class="rbar">{segs}</span></div>'
    out += '<div class="rleg">' + ''.join(f'<span><i class="t-{t}"></i><span data-i="t.{t}">{EN["t."+t]}</span></span>' for t in reversed(ecotier.ORDER)) + '</div>'
    return out + '</div>'
def records(R):
    og = max(ORDER, key=lambda c: R[c]['og']['t0']); oa = max(ORDER, key=lambda c: R[c]['oa']['t0']); ec = max(ORDER, key=lambda c: R[c]['eco']); wh = max(ORDER, key=lambda c: R[c]['whs']); ex = max(ORDER, key=lambda c: R[c]['tiers']['exceptional'])
    def card(k, cc, b, sm): return f'<div><i data-i="{k}">{EN[k]}</i><b>{b}</b><span><span data-i="n.{cc}">{EN["n."+cc]}</span> · {sm}</span></div>'
    nm = lambda r: bi(esc(r['n']), esc(r.get('na') or r['n']), False)
    return (card('r1', og, nm(R[og]['og']), yrs2(R[og]['og']['t0'])) + card('r2', oa, nm(R[oa]['oa']), yrs2(R[oa]['oa']['t0'])) +
            card('r3', ec, bi(f'{R[ec]["eco"]} places', f'{R[ec]["eco"]} موقعًا', False), bi('ecology layer', 'طبقة البيئة', False)) +
            card('r5', ex, bi(f'{R[ex]["tiers"]["exceptional"]} places', f'{R[ex]["tiers"]["exceptional"]} مواقع', False), bi('Exceptional grade', 'درجة استثنائية', False)) +
            card('r4', wh, bi(f'{R[wh]["whs"]} sites', f'{R[wh]["whs"]} مواقع', False), bi('UNESCO World Heritage', 'التراث العالمي لليونسكو', False)))

# rename "AI speculation" to "AI hypotheses" in every edition (display text only; the data key stays 'speculative')
AIREN = [
 ("speculative:'AI speculation'", "speculative:'AI hypotheses'"), ("aiF:'AI speculation'", "aiF:'AI hypotheses'"), ("tAi:'AI speculation'", "tAi:'AI hypothesis'"),
 ("An AI speculation.", "An AI hypothesis."), ("Untested AI speculation", "Untested AI hypothesis"), ("AI-powered speculation", "AI-powered hypotheses"),
 ("Speculative / AI-Detected Features", "AI Hypotheses / AI-Detected Features"), ("AI speculations", "AI hypotheses"), ("AI speculation", "AI hypothesis"), ("AI Speculation", "AI Hypotheses"),
 ("تخمينات الذكاء الاصطناعي", "فرضيات الذكاء الاصطناعي"), ("تخمين بالذكاء الاصطناعي", "فرضية من الذكاء الاصطناعي"), ("تخمين مدعوم بالذكاء", "فرضيات مدعومة بالذكاء الاصطناعي"),
]
def patch_edition(cc):
    h = patch0(cc)
    for _a, _b in AIREN: h = h.replace(_a, _b)
    h = h.replace('const free=(bx,c)=>!placed.some(', 'const free=(bx,c)=>bx[0]>=vb[0]&&bx[2]<=vb[0]+vb[2]&&bx[1]>=vb[1]&&bx[3]<=vb[1]+vb[3]&&(bx[1]>vb[1]+225*u||(rtl?bx[0]>=vb[0]+60*u:bx[2]<=vb[0]+vb[2]-60*u))&&!placed.some(')  # keep map labels inside the map
    # map labels in Arabic: x is the label's left edge, so anchor at the left edge in RTL too
    h = h.replace('text-anchor="start" style="font-size:${fs}px;stroke-width:${3.2*u}px"', 'text-anchor="${rtl?\'end\':\'start\'}" style="font-size:${fs}px;stroke-width:${3.2*u}px"')
    h = h.replace('<style', '<style>html[dir=rtl] *,html[lang=ar] *{letter-spacing:0!important}#modes{flex:none!important;width:96px!important;height:34px!important}@media (max-width:560px){#modes{width:84px!important;height:30px!important}}body:has(#det.on) .legend{max-width:calc(100% - 476px);border-radius:16px}@media (max-width:760px){#tools{flex-wrap:wrap!important;overflow:visible!important;row-gap:8px!important}#tools .search{flex:1 1 150px!important;min-width:150px!important}#tools .search input{width:100%!important;min-width:0!important}}</style><style', 1)
    def rep(a, b, n=1):
        nonlocal h
        assert h.count(a) == n, (cc, a[:60], h.count(a)); h = h.replace(a, b)
    a = "function goCountry(k){parent.postMessage({layers:'open',cc:k},'*')}"
    b = ("function goCountry(k){try{setActive(k);var c=LGN[k];if(c){var ti=lang=='ar'?'طبقات '+c.ar:(c.t||'Layers of '+c.en);$('#t-title').textContent=ti;var s=$('#t-short');if(s)s.textContent=ti}}catch(e){}"
         "setTimeout(function(){parent.postMessage({layers:'open',cc:k},'*')},560)}")
    rep(a, b)
    # Directions: opens the phone's maps app at the place's recorded coordinates (not for AI hypotheses)
    rep("db.insertAdjacentHTML('afterbegin',spkBtn()+(sel?shareBtn(sel):''))",
        "db.insertAdjacentHTML('afterbegin',spkBtn()+(sel?shareBtn(sel)+dirBtn(sel):''))")
    h = h.replace('<style', '<script>function dirBtn(id){try{var s=D.sites.find(function(x){return x.id==id});'
        'if(!s||s.c==\'speculative\'||!isFinite(+s.lat)||!isFinite(+s.lng))return\'\';'
        'var ar=document.documentElement.lang==\'ar\';return \'<a class="spk dirs" target="_blank" rel="noopener" href="https://www.google.com/maps/dir/?api=1&amp;destination=\'+(+s.lat)+\',\'+(+s.lng)+\'">'
        '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 2.5 21.5 12 12 21.5 2.5 12Z"/><path d="M9 14v-2.5a1.5 1.5 0 0 1 1.5-1.5H15m-2-2 2 2-2 2"/></svg>'
        '<span>\'+(ar?\'الاتجاهات\':\'Directions\')+\'</span></a> \'}catch(e){return \'\'}}<\\/script>'
        '<style>a.spk.dirs{text-decoration:none}</style><style', 1)
    # timeline: era names only where they fit (else hover/tap title), and a gap so dots never touch the names column
    rep("${x1-x0>6?E(t.bands[i]):''}", "${x1-x0>2?E(t.bands[i]):''}")
    rep("el.innerHTML=h+'</div>'}", "el.innerHTML=h+'</div>';el.querySelectorAll('.bands b').forEach(b=>{b.style.overflow='hidden';b.style.whiteSpace='nowrap';if(b.scrollWidth>b.clientWidth+1)b.textContent=''})}")
    h = h.replace('<style', '<style>.trk{margin-inline-start:10px}.tlrow.item{height:auto!important;min-height:28px}.tlrow .lab{white-space:normal!important;display:-webkit-box!important;-webkit-line-clamp:2;-webkit-box-orient:vertical;line-height:1.25!important;padding-top:3px!important;padding-bottom:3px!important;text-overflow:clip!important}.tlrow.ms .lab{-webkit-line-clamp:3}</style><style', 1)
    # timeline: places older than the scale start (100 Myr) begin at the scale edge, not inside the names column
    rep("const s=r.s,sp=s.c=='speculative',x0=TX(r.t0),x1=TX(r.t1);", "const s=r.s,sp=s.c=='speculative',x0=Math.max(0,TX(r.t0)),x1=Math.max(0,TX(r.t1));")
    # no welcome pop-up: the Researcher/Explorer toggle is always in the top bar
    rep("welcomed=store.get('welcomed',false);", "welcomed=true;")
    rep("document.querySelector('[data-home]').addEventListener('click',()=>{parent.postMessage({layers:'home'},'*')});",
        "document.querySelector('[data-home]').addEventListener('click',function(){var b=this,row=b.parentNode;row.classList.add('going');b.classList.add('sel');setTimeout(function(){parent.postMessage({layers:'home'},'*')},520)});")
    h = h.replace('</style>', ".lgs.going .lg{opacity:.3;transition:opacity .3s,transform .4s}.lgs.going .lg.sel{opacity:1;transform:scale(1.35)}</style>", 1)
    # icons on the mode buttons + explorer palette hook
    rep("$('#b-e').textContent=t.e", "$('#b-e').innerHTML=" + json.dumps(ICO_E) + "+'<span>'+E(t.e)+'</span>'")
    rep("$('#b-r').textContent=t.r", "$('#b-r').innerHTML=" + json.dumps(ICO_R) + "+'<span>'+E(t.r)+'</span>'")
    rep("$('#tl').onclick=e=>{const b=e.target.closest('[data-id]');if(b)show(b.dataset.id)};",
        "window.backTL=null;function detBack(fn){let b=$('#detB');if(!b){b=document.createElement('button');b.id='detB';b.type='button';$('#detX').after(b)}b.textContent='← '+(lang=='ar'?'الخط الزمني':'Timeline');b.onclick=ev=>{ev.stopPropagation();const f=window.backTL;window.backTL=null;b.classList.remove('on');f&&f()};window.backTL=fn;b.classList.add('on')}window.detBack=detBack;"
        "$('#tl').onclick=e=>{const b=e.target.closest('[data-id]');if(b){show(b.dataset.id);detBack(()=>closeDet())}};")
    rep("function closeDet(){stopSpk();", "function closeDet(){stopSpk();{const b=document.getElementById('detB');if(b)b.classList.remove('on');window.backTL=null}")
    rep("function chrome(){stopSpk();", "function chrome(){stopSpk();document.documentElement.setAttribute('data-mode',mode);")
    h = h.replace('</style>', EXPL_CSS + TILE_E + '#hwb,#inst{display:none!important}#detB{display:none;position:absolute;z-index:6;top:10px;inset-inline-end:calc(min(440px,100%) - 10px);transform:translateX(100%);height:36px;padding:0 14px;border:0;border-radius:999px;background:rgba(20,20,20,.55);color:#fff;font:700 13px var(--f-body);box-shadow:0 0 0 2px rgba(255,255,255,.75),0 2px 8px rgba(0,0,0,.25);backdrop-filter:blur(4px);cursor:pointer}html[dir=rtl] #detB{transform:translateX(-100%)}#det.on~#detB.on{display:inline-flex;align-items:center}@media (max-width:760px){#detB{top:calc(32% + 10px);inset-inline-end:auto;inset-inline-start:10px;transform:none}html[dir=rtl] #detB{transform:none}}input,textarea,select{font-size:16px}html,body{overflow-x:hidden;max-width:100vw}</style>', 1)
    rep('<button class="lang" id="lang" lang="ar">عربي</button>', '<button class="thm" id="thm" type="button" aria-pressed="false" aria-label="Dark mode"><i></i></button><button class="lang" id="lang" lang="ar">عربي</button>')
    rep('<button data-m="e" aria-pressed="false" id="b-e"></button></div>', '<button data-m="e" aria-pressed="false" id="b-e"></button></div><span class="modelbl" id="modelbl"></span>')
    h = h.replace('<script>', '<script>(function(){try{var t=JSON.parse(localStorage.getItem("kge-theme"));if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t)}catch(e){}})();', 1)
    assert h.rstrip().endswith('</html>'), cc
    h = h.rstrip()[:-7] + '</html>'
    h = h.replace('</html>', '<script>(function(){var b=document.getElementById("thm"),m=document.getElementById("modes");function dark(){var t=document.documentElement.getAttribute("data-theme");return t?t==="dark":matchMedia("(prefers-color-scheme: dark)").matches}function paintT(){b.setAttribute("aria-pressed",dark()?"true":"false")}b.addEventListener("click",function(){var t=dark()?"light":"dark";document.documentElement.setAttribute("data-theme",t);try{localStorage.setItem("kge-theme",JSON.stringify(t))}catch(e){}paintT();try{parent.postMessage({layers:"theme",t:t},"*")}catch(e){}});paintT();if(m){new MutationObserver(function(){var e=m.querySelector("[data-m=e]");var on=e&&e.getAttribute("aria-pressed")==="true";m.classList.toggle("e",on);lbl()}).observe(m,{attributes:true,subtree:true,attributeFilter:["aria-pressed"]});var e0=m.querySelector("[data-m=e]");m.classList.toggle("e",e0&&e0.getAttribute("aria-pressed")==="true");lbl()}function lbl(){var l=document.getElementById("modelbl");if(!l)return;var on=m.classList.contains("e"),r=document.getElementById("b-r"),e=document.getElementById("b-e");l.textContent=(on?e:r).textContent;l.className="modelbl "+(on?"e":"r")}new MutationObserver(lbl).observe(document.getElementById("b-r"),{childList:true,subtree:true,characterData:true})})();<\\/script></html>', 1)
    h = h.replace('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">', '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,viewport-fit=cover">', 1)
    return h

def build(mode, fname):
    data = {cc: dict(zip(['n', 'k'], H.counts(cc))) for cc in ORDER}
    IDX = {}
    for cc in ORDER:
        for s in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']: IDX[s['id']] = cc
    total = sum(data[cc]['n'] for cc in ORDER)
    b64 = lambda f: base64.b64encode(open(f'{SITE}/{f}', 'rb').read()).decode()
    man = {'name': 'Layers · طبقات', 'short_name': 'Layers', 'start_url': BASE, 'scope': BASE, 'display': 'standalone', 'background_color': '#f7f8f5', 'theme_color': '#fbeedb',
           'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'}]}
    manifest = 'data:application/manifest+json;base64,' + base64.b64encode(json.dumps(man, ensure_ascii=False).encode()).decode()
    R = gulf_stats()
    GT = gulf_timeline(R)
    for i, (en, d, ar, da) in enumerate(HOWSTEPS): EN[f'hs{i}'] = en; AR[f'hs{i}'] = ar; EN[f'hsk{i}'] = 'automatic' if i in (1,2,3,5) else 'human'; AR[f'hsk{i}'] = 'تلقائي' if i in (1,2,3,5) else 'بشري'; EN[f'hsd{i}'] = d; AR[f'hsd{i}'] = da
    nst = nai = nref = 0
    for cc in ORDER:
        if cc == 'kw': nst += 17; nai += 11
        else:
            pth = f'/tmp/w/gulf/{cc}/stories.json'
            if os.path.exists(pth): J = json.load(open(pth)); nst += len(J['stories']); nai += len(J['spec'])
        for x in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']: nref += len(x.get('refs', []))
    howsteps = pipe_v() + '<p class="hcap" id="hcap" data-cycle="' + '|'.join(f'hsd{i}' for i in range(len(HOWSTEPS))) + '"><span data-i="hsd0">' + HOWSTEPS[0][1] + '</span></p>'
    tot = {'archaeological': 0, 'geological': 0, 'ecology': 0}
    for cc in ORDER:
        for x in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']:
            if x['c'] in tot: tot[x['c']] += 1
    hchips = (f'<p class="hpromo"><b data-i="hp1">{EN["hp1"]}</b> <span data-i="hp2">{EN["hp2"]}</span></p><div class="hstats">'
              f'<span class="hchip" tabindex="0" data-k="archaeological" style="--c:var(--arch)"><b>{tot["archaeological"]}</b><span data-i="sa1">{EN["sa1"]}</span><em class="tip" data-i="sa1t">{EN["sa1t"]}</em></span>'
              f'<span class="hchip" tabindex="0" data-k="geological" style="--c:var(--geo)"><b>{tot["geological"]}</b><span data-i="sg1">{EN["sg1"]}</span><em class="tip" data-i="sg1t">{EN["sg1t"]}</em></span>'
              f'<span class="hchip" tabindex="0" data-k="ecology" style="--c:var(--eco)"><b>{tot["ecology"]}</b><span data-i="se1">{EN["se1"]}</span><em class="tip" data-i="se1t">{EN["se1t"]}</em></span>'
              f'<span class="hchip" tabindex="0" data-k="speculative" style="--c:#bf2f7d"><b>{nai}</b><span data-i="sai1">{EN["sai1"]}</span><em class="tip" data-i="sai1t">{EN["sai1t"]}</em></span>'
              f'<span class="hchip" tabindex="0" data-k="stories" style="--c:var(--gold)"><b>{nst}</b><span data-i="sst1">{EN["sst1"]}</span><em class="tip" data-i="sst1t">{EN["sst1t"]}</em></span>'
              '</div>')
    RI = {'ra1': ('v:about', 'var(--sea)', '<circle cx="12" cy="12" r="9"/><path d="M12 8v4l3 2"/>'), 'ra2': ('v:map', 'var(--arch)', '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14"/>'),
          'ra3': ('v:cmp', 'var(--eco)', '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'), 'ra4': ('v:tl', 'var(--geo)', '<path d="M3 12h18M7 12v-4M12 12v4M17 12v-5"/><circle cx="7" cy="7" r="1.5"/><circle cx="12" cy="17" r="1.5"/><circle cx="17" cy="6" r="1.5"/>'), 'ra9': ('ah-ta', 'var(--arch)', '<path d="M4 20h16M6 20V9l6-5 6 5v11M10 20v-6h4v6"/>'),
          'ra5': ('ah-rec', '#bf2f7d', '<path d="M12 3l2.7 5.6 6.3.9-4.5 4.4 1 6.1L12 17l-5.5 3 1-6.1L3 9.5l6.3-.9z"/>'), 'ra6': ('v:how', 'var(--gold)', '<path d="M4 6h16M4 12h10M4 18h7"/><circle cx="18" cy="16" r="3"/>'),
          'ra7': ('inst', 'var(--ink)', '<path d="M12 3v12M7 10l5 5 5-5M4 19h16"/>'), 'ra8': ('intro', 'var(--coast)', '<path d="M5 4l14 8-14 8z"/>'), 'ra10': ('v:inno', '#bf2f7d', IC['spark']), 'ra11': ('v:ref', 'var(--coast)', IC['book'])}
    RO = ['ra2', 'ra4', 'ra3', 'ra10', 'ra6', 'ra11', 'ra8']
    tnav = ('<div class="seg" role="group" id="hviews"><button type="button" data-v="map" aria-pressed="true" data-i="vmap">' + EN['vmap'] + '</button><button type="button" data-v="tl" aria-pressed="false" data-i="vtl">' + EN['vtl'] + '</button><button type="button" data-v="cmp" aria-pressed="false" data-i="vcmp">' + EN['vcmp'] + '</button></div>'
            '<button class="stbtn" type="button" id="stbtn" aria-label="' + EN['stT'] + '"><span data-i="stT">' + EN['stT'] + '</span></button>'
            '<div class="seg" role="group" id="hmore"><button type="button" data-go="intro" data-i="ra8">' + EN['ra8'] + '</button><button type="button" data-v="inno" aria-pressed="false" data-i="ra10">' + EN['ra10'] + '</button><button type="button" data-v="how" aria-pressed="false" data-i="ra6">' + EN['ra6'] + '</button><button type="button" data-v="ref" aria-pressed="false" data-i="ra11">' + EN['ra11'] + '</button></div>')
    CK = {'ra2': 'map', 'ra4': 'tl', 'ra3': 'cmp', 'ra10': 'inno', 'ra6': 'how', 'ra11': 'about', 'ra8': 'intro'}
    arail = f'<div class="lb2" data-i="rl">{EN["rl"]}</div>' + ''.join(f'<a href="#" data-go="{RI[k][0]}" style="--c:{RI[k][1]}"><i class="ir"><svg viewBox="0 0 24 24">{RI[k][2]}</svg></i><i class="ie">{cartoon.ICONS[CK[k]]}</i><span data-i="{k}">{EN[k]}</span></a>' for k in RO)
    lbar = ''.join(f'<button class="lb" type="button" data-go="{cc}" data-cc="{cc}"><span class="i">{H.flag_logo(cc, "lb"+cc)}</span><span class="n" data-i="n.{cc}">{EN["n."+cc]}</span></button>' for cc in ORDER)
    flags = ''.join(f'<button type="button" data-go="{cc}" data-cc="{cc}" title="{EN["n."+cc]}" aria-label="{EN["n."+cc]}">{H.flag_logo(cc, "ab"+cc)}</button>' for cc in ORDER)
    html = open('/tmp/w/layers/hub5_tpl.html', encoding='utf-8').read()
    def sub(m):
        f, k = m.group(1), m.group(2)
        return EN[k] if f == '=' else f'<span data-i="{k}">{EN[k]}</span>'
    html = re.sub(r'\[\[([=]?)([a-zA-Z0-9_.]+)\]\]', sub, html)
    rep = {'__SCENE_LG__': scene(1600, 560), '__SCENE_SM__': scene(420, 480, True), '__ENGINE__': engine({'lgeo': tot['geological'], 'larch': tot['archaeological'], 'leco': tot['ecology'], 'o1': nai, 'o3': nst}), '__MAP_P__': mapc('p'), '__MAP_A__': mapc('a'),
           '__IHX__': '<svg class="ir" viewBox="0 0 24 24"><path d="M4 6h16M4 12h10M4 18h7"/><circle cx="18" cy="16" r="3"/></svg><i class="ie">' + cartoon.CHIP['how'] + '</i>', '__II__': '<svg class="ir" viewBox="0 0 24 24"><path d="M12 3v12M7 10l5 5 5-5M4 19h16"/></svg><i class="ie">' + cartoon.CHIP['inst'] + '</i>',
           '__LBAR__': lbar, '__HCHIPS__': hchips, '__ARAIL__': arail, '__TNAV__': tnav, '__PIPE__': pipe(), '__GROWMAP__': growmap(), '__TABLE__': table(R), '__RBARS__': rarity_bars(R), '__STORIES__': json.dumps(storyidx.story_index(ORDER), ensure_ascii=False).replace('<', '\\u003c'), '__STBG__': cartoon.uri(cartoon.STORY_BG), '__FLAGSJ__': json.dumps({cc: flag_badge(cc, 'sf' + cc) for cc in ORDER}), '__GTL__': GT[0], '__REFS__': GT[1], '__HWCSS__': open('/tmp/w/layers/hw_css.css', encoding='utf-8').read(), '__HWJS__': open('/tmp/w/layers/hw_code.js', encoding='utf-8').read(), '__GEOSCALE__': geo_scale(R, mode == 'mob'), '__ARCHSCALE__': arch_scale(R, mode == 'mob'), '__RECORDS__': records(R),  '__ICO_R__': ICO_R, '__ICO_E__': ICO_E, '__KIDCSS__': KID_CSS, '__INNO5__': inno5(), '__INNO17__': inno17(), '__NSTORIES__': str(nst), '__NAI__': str(nai), '__NREFS__': str(nref), '__FLAGS__': flags, '__HAND__': HAND, '__FY__': f'{map2.P(50, 26.5)[1] / map2.H:.4f}', '__MW__': str(map2.W), '__FOCUS__': '[%.1f,%.1f,%.1f,%.1f]' % (*map2.P(45.6, 31.2), *map2.P(59.6, 20.2)), '__MH__': str(map2.H),
           '__LOGO1__': H.plain_logo('l1'), '__LOGO2__': H.plain_logo('l2'), '__LOGO3__': H.plain_logo('l3'), '__LOGO4__': H.plain_logo('l4'),
           '__ART_G__': art('jal-az-zor'), '__ART_A__': art('failaka-island'), '__ART_E__': art('khor-sabiyah-marsh'),
           '__IDX__': json.dumps(IDX), '__TEXTS__': json.dumps({'en': EN, 'ar': AR}, ensure_ascii=False), '__BASE__': BASE, '__TOTAL__': str(total),
           '__MANIFEST__': manifest, '__KV__': KV, '__ARTCSS__': ARTCSS, '__MODE__': mode,
           '__CN__': json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in H.C.items()}, ensure_ascii=False)}
    for k, v in rep.items(): html = html.replace(k, v)
    left = re.findall(r'__[A-Z0-9_]+__', html); assert not left, left
    html = html.replace('<!--PAYLOAD-->', ''.join(f'<script type="text/plain" id="ed-{cc}">{patch_edition(cc)}</script>\n' for cc in ORDER))
    html = ar_apply(html)
    open(f'{OUT}/{fname}', 'w', encoding='utf-8').write(html)
    return total, os.path.getsize(f'{OUT}/{fname}')


# ---- Arabic editorial pass: exact, delimiter-bounded replacements from /tmp/w/arfix/ar_map.json
def ar_apply(html):
    p = '/tmp/w/arfix/ar_map.json'
    if not os.path.exists(p): return html
    M = dict(json.load(open(p, encoding='utf-8')))
    hits = set()
    def sub(m):
        a, body, b = m.group(1), m.group(2), m.group(3)
        core = body.strip()
        if core in M:
            hits.add(core); return a + body.replace(core, M[core]) + b
        return m.group(0)
    html = re.sub(r"(['\"`>])([^'\"`<>\n]*[\u0600-\u06FF][^'\"`<>\n]*)(['\"`<])", sub, html)
    print('arabic fixes', len(M), 'applied', len(hits))
    html = html.replace('fill:var(--ink)">SUN</text>', 'fill:var(--ink)">${document.documentElement.lang==\'ar\'?\'الأحد\':\'SUN\'}</text>')
    html = html.replace('الأتوم', 'الأطوم')
    return html

if __name__ == '__main__':
    print(build('pc', 'index.html')); print(build('mob', 'mobile.html'))
