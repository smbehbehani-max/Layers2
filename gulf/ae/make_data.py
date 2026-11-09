# Layers of the UAE — researcher catalogue v0.1
import json
S = []
def add(**k): S.append(k)

add(id='hili', n='Hili Archaeological Park (Al Ain)', na='حديقة الهيلي الأثرية (العين)', c='archaeological', s='Bronze Age oasis village · World Heritage', lat=24.2929, lng=55.7899,
    p='Umm an-Nar to Iron Age', dr='c. 3000 – 300 BC', el='Grand Tomb 12 m across', ic='mound', era='P', t0=5025, t1=2325,
    te='The first farmers of the oasis', ta='أوائل مزارعي الواحة', se='Wheat, barley and dates were grown here 5,000 years ago beside a tomb for 600 people', sa='زُرع القمح والشعير والتمر هنا قبل 5,000 عام إلى جانب قبر لستمئة إنسان',
    desc="The Hili 8 settlement, dating to about 3000 BC, holds some of the earliest evidence of oasis agriculture in south-eastern Arabia (wheat, barley and date palm). The reconstructed Hili Grand Tomb of the Umm an-Nar culture is about 12 m in diameter and was originally about 4 m high; Tomb N, from the last two centuries of the 3rd millennium BC, held more than 600 burials. Aflaj irrigation channels dug in the first millennium BC are among the oldest known, and 3,000-year-old fingerprints of wall-builders were reported at Hili II in 2019. Part of the Cultural Sites of Al Ain, 17 locations inscribed in 2011 under criteria (iii), (iv) and (v), the UAE's first World Heritage property.",
    sig="The clearest evidence of how farming, tower tombs and falaj irrigation began in the oases of eastern Arabia.",
    ex='Danish, Iraqi and French missions from the 1960s; Department of Culture and Tourism – Abu Dhabi',
    disc=['Earliest oasis farming in south-east Arabia, c. 3000 BC', 'Tomb N with over 600 burials', 'Iron Age aflaj among the oldest known'],
    refs=['UNESCO World Heritage Centre. Cultural Sites of Al Ain (Hafit, Hili, Bidaa Bint Saud and Oases Areas), ref. 1343, inscribed 2011.', 'Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.', 'Potts, D. T. (2003). Archaeology of the United Arab Emirates. Trident Press.'])

add(id='jebel-hafeet-tombs', n='Jebel Hafeet Tombs', na='مدافن جبل حفيت', c='archaeological', s='Beehive tombs of the Hafit period', lat=24.0700, lng=55.7800,
    p='Hafit period (Early Bronze Age)', dr='c. 3200 – 2600 BC', el='More than 500 cairns on the foothills near Mezyad', ic='mound', era='P', t0=5225, t1=4625,
    te='Five hundred stone beehives', ta='خمسمئة خلية نحل من حجر', se='Tombs on the mountain foothills hold pottery carried from Mesopotamia 5,000 years ago', sa='قبور على سفوح الجبل تحوي فخارًا جُلب من بلاد الرافدين قبل 5,000 عام',
    desc="More than 500 stone cairns on the foothills of Jebel Hafeet near Mezyad, first discovered in 1950 and excavated from 1962 by the Danish expedition. They date to 3200–2600 BC and give their name to the Hafit period, the start of the Bronze Age in the UAE. Imported Mesopotamian pottery of Jemdet Nasr type, about 5,000 years old, shows contact with the cities of Iraq. Part of the Cultural Sites of Al Ain, inscribed in 2011.",
    sig="The earliest monumental tombs in the Emirates and the first evidence of long-distance trade with Mesopotamia.",
    ex='Danish Archaeological Expedition, 1962; Department of Culture and Tourism – Abu Dhabi',
    disc=['Over 500 beehive cairns', 'Jemdet Nasr pottery from Mesopotamia'],
    refs=['Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.', 'UNESCO World Heritage Centre. Cultural Sites of Al Ain, ref. 1343.'])

add(id='faya-palaeolandscape', n='Faya Palaeolandscape', na='منظر الفاية القديم', c='archaeological', s='210,000 years of human presence · World Heritage', lat=25.120, lng=55.830,
    p='Palaeolithic to Neolithic', dr='c. 210,000 years ago onwards', el='18 archaeological layers', ic='eye', era='P', t0=210000, t1=5000,
    te='The desert that kept people alive', ta='الصحراء التي أبقت الناس أحياء', se='Eighteen layers of stone tools show humans returning here for 210,000 years', sa='ثماني عشرة طبقة من الأدوات الحجرية تُظهر عودة الإنسان إلى هنا طوال 210,000 عام',
    desc="A desert landscape of dunes, rocky outcrops and fossil remnants around Jebel Faya in central Sharjah, where 30 years of excavation by the Sharjah Archaeology Authority and international teams have uncovered 18 distinct layers of human activity spanning more than 210,000 years. A joint German–Emirati team led by Hans-Peter Uerpmann found handaxes, blades and points about 125,000 years old in 2011. Inscribed on the World Heritage List in 2025 as a cultural landscape, the first desert Palaeolithic site on the list and the only Arab-region site inscribed that year.",
    sig="A key site for how early humans crossed and survived Arabia during the wet and dry phases of the last 200,000 years.",
    ex='Sharjah Archaeology Authority with the University of Tübingen and other partners, 1990s onwards',
    disc=['Stone tools about 125,000 years old (2011)', '18 layers of occupation'],
    refs=['Current World Archaeology (2025). Faya Palaeolandscape becomes only site in the Arab world to be awarded UNESCO World Heritage status in 2025.', 'UNESCO World Heritage Centre. Faya Palaeolandscape, inscribed 2025.'])

add(id='mleiha', n='Mleiha', na='مليحة', c='archaeological', s='Capital of the kingdom of Uman · UNESCO tentative list', lat=25.1171, lng=55.8716,
    p='Late pre-Islamic', dr='c. 300 BC – 300 AD', el='Al-Husn fort 55 × 50 m', ic='caravan', era='H', t0=2325, t1=1725,
    te='A kingdom under the sand', ta='مملكة تحت الرمال', se='A trading capital with horse burials, a mint and amphorae from Rhodes', sa='عاصمة تجارية بمدافن خيول ودار سكّ وجرار من رودس',
    desc="A town east of Jebel Faya, about 50 km from Sharjah, occupied from roughly 300 BC to 300 AD as the centre of the kingdom of Uman, probably the Omana of classical sources. Remains include a fort (the al-Husn building, 55 × 50 m), a buttressed palace, tower tombs and houses with underground kitchens; finds include horse and hybrid-camel burials with a gold bridle, coins imitating Alexander's tetradrachm with a coin mould, the largest number of Rhodian amphorae in Arabia, and a 2016 bilingual Aramaic–Hasaitic tombstone naming the kingdom. A 1994 cemetery held 26 graves, 12 for camels. Abandoned after a violent attack in the 3rd century AD; submitted to the UNESCO Tentative List in 2023.",
    sig="The eponymous site of the late pre-Islamic period in south-east Arabia and proof of an Arabian kingdom trading with the Hellenistic world.",
    ex='Iraqi mission 1973; Belgian and French missions from the 1980s; Sharjah Archaeology Authority',
    disc=['Bilingual tombstone naming the kingdom of Uman (2016)', 'Horse burials with a gold bridle', 'Coin mould for Alexander-type tetradrachms'],
    refs=['UNESCO World Heritage Centre. Mleiha, late pre-Islamic center of a south-east Arabian kingdom. Tentative List ref. 6643 (2023).', 'Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.'])

add(id='jebel-buhais', n='Jebel Buhais Necropolis', na='مقبرة جبل البحيص', c='archaeological', s='Neolithic herders’ cemetery', lat=25.0170, lng=55.7947,
    p='Neolithic to Iron Age', dr='c. 5000 – 4000 BC (BHS 18)', el='Limestone outcrop 340 m', ic='shell', era='P', t0=7025, t1=6025,
    te='Winter camp of the herders', ta='مخيم الرعاة الشتوي', se='Nomadic herders buried their dead here for a thousand years', sa='دفن الرعاة الرُّحّل موتاهم هنا ألف عام',
    desc="A limestone outcrop 48 km south-east of Sharjah city, rising to about 340 m, on the ridge that runs from Madam to Mleiha. The Neolithic cemetery BHS 18, dated by radiocarbon to about 5000–4000 BC, is one of the key Neolithic sites of southern Arabia; its burials are read as those of nomadic herders who came inland for the winter, and the whole site has yielded the complete remains of about 600 individuals. Hafit-period beehive graves, a unique clover-shaped Wadi Suq tomb (BHS 66), Iron Age burials and an Iron Age fort lie on the same mountain. Excavated by Iraqi, French, Spanish and, from 1995, University of Tübingen teams (ten seasons at BHS 18, 1996–2005).",
    sig="The largest Neolithic cemetery in the region, with the best evidence for the health, diet and movements of Arabia's first herders.",
    ex='University of Tübingen (H.-P. Uerpmann) with the Sharjah Directorate of Antiquities, 1995–2005',
    disc=['About 600 individuals recovered', 'Unique clover-shaped tomb BHS 66'],
    refs=['Uerpmann, H.-P., Uerpmann, M. & Jasim, S. A. (2006). Funeral Monuments and Human Remains from Jebel al-Buhais. Department of Culture and Information, Sharjah.', 'Jasim, S. A. (2012). The Necropolis of Jebel al-Buhais. Sharjah.'])

add(id='saruq-al-hadid', n='Saruq Al-Hadid', na='ساروق الحديد', c='archaeological', s='Iron Age metal-working and ritual site', lat=24.650, lng=55.350,
    p='Iron Age II', dr='c. 1200 – 800 BC', el='Dune field at the edge of the Empty Quarter', ic='flame', era='P', t0=3225, t1=2825,
    te='Snakes of copper in the dunes', ta='أفاعٍ من نحاس في الكثبان', se='Smelting slag, arrowheads and copper snakes buried far from any ore', sa='خبث صهر ورؤوس سهام وأفاعٍ نحاسية مدفونة بعيدًا عن أي خام',
    desc="A site in the dunes of the Rub' al-Khali margin south of Dubai, excavated since 2002 by Jordanian, Australian, Spanish and Polish teams. Slag, ore nodules, crucibles and metallurgical tools show copper smelting and probably manufacture in Iron Age II, although no furnaces or moulds have yet been found; many copper arrowheads, axes and daggers were collected. The ritualised scattering of objects, with copper snakes, human figurines and soft-stone and alabaster vessels, suggests a ceremonial role. Location approximate.",
    sig="A unique combination of industry and ritual in a place with no water or ore, still unexplained.",
    ex='Dubai Municipality Architectural Heritage Department with Spanish (Sanisera), Australian (UNSW) and Polish (PCMA) teams, 2002 onwards',
    disc=['Copper snakes and figurines', 'Slag and crucibles without furnaces'],
    refs=['Contreras Rodrigo, F. et al. (2017). Excavations in Area 2A at Sarūq al-Ḥadīd: Iron Age II evidence of copper production and ceremonial activities. Proceedings of the Seminar for Arabian Studies 47, 57–67.'])

add(id='marawah-village', n='Marawah Island Stone Age Village', na='قرية مروح من العصر الحجري', c='archaeological', s='Oldest stone houses in the Gulf', lat=24.280, lng=53.300,
    p='Neolithic', dr='c. 8,000 – 7,500 years ago', el='Island inside the Marawah Marine Biosphere Reserve', ic='shell', era='P', t0=8000, t1=7000,
    te='The oldest pearl', ta='أقدم لؤلؤة', se='An 8,000-year-old village with stone houses, burials and a pearl less than a centimetre long', sa='قرية عمرها 8,000 عام ببيوت حجرية ومدافن ولؤلؤة أقصر من سنتيمتر',
    desc="Excavations by the Abu Dhabi Islands Archaeological Survey began in March 1998 on Marawah Island and revealed a Stone Age village: fireplaces of Late Stone Age hunters, then stone houses about 7,500 years old, the earliest permanent stone buildings found in the Arabian Gulf, with burials inside former homes, tools, jewellery and fishing gear. Two more settlements, MR I and MR II, lie nearby. In 2019 a natural pearl less than a centimetre long, dated to 5800–5600 BC, was found, the oldest known anywhere, pushing pearling back nearly 8,000 years.",
    sig="The oldest architecture and the oldest pearl of the Gulf, on one small island.",
    ex='Abu Dhabi Islands Archaeological Survey (ADIAS) 1998–2004; Department of Culture and Tourism – Abu Dhabi',
    disc=['Stone houses about 7,500 years old', 'Pearl dated 5800–5600 BC (2019)'],
    refs=['The National (6 March 2026). Timeframe: when Abu Dhabi\'s 8,000-year-old village was first unearthed.', 'Beech, M. et al. Marawah excavation reports, Department of Culture and Tourism – Abu Dhabi.'])

add(id='sir-bani-yas-monastery', n='Sir Bani Yas Monastery', na='دير صير بني ياس', c='archaeological', s='Church of the East monastery', lat=24.330, lng=52.650,
    p='Late pre-Islamic to early Islamic', dr='c. 600 – 750 AD', el='East coast of Sir Bani Yas Island', ic='platform', era='H', t0=1425, t1=1275,
    te='Monks on the island', ta='رهبان على الجزيرة', se='A 1,400-year-old church and monastery that traded with its Muslim neighbours', sa='كنيسة ودير عمرهما 1,400 عام تاجرا مع جيرانهما المسلمين',
    desc="A church and monastery on the eastern coast of Sir Bani Yas Island, about 200 km from Abu Dhabi, found in 1992 and at first not recognised as religious. About 1,400 years old, it has dormitories, a kitchen, cells and burials, with more buildings found in 2014 to the west, south-west and north. Finds include Christian crosses and a decorative frieze now in the Louvre Abu Dhabi, and evidence that the monks kept cattle and fished and traded with Muslim neighbours in the 7th and 8th centuries. Opened to the public in 2019; the island also holds the Arabian Wildlife Park.",
    sig="The only known Christian monastery in the UAE and a rare window on the Gulf at the dawn of Islam.",
    ex='Abu Dhabi Islands Archaeological Survey (G. King) 1992–1996; Department of Culture and Tourism – Abu Dhabi (P. Magee) 2014',
    disc=['Church with plaster crosses and frieze', 'Expansion found in 2014'],
    refs=['Euronews (27 September 2019). Sir Bani Yas church and monastery: UAE\'s oldest Christian site opens to the public.', 'King, G. R. D. (1997). A Nestorian monastic settlement on the island of Sir Bani Yas, Abu Dhabi. Bulletin of SOAS 60(2).'])

add(id='ed-dur', n='Ed-Dur', na='الدور', c='archaeological', s='Hellenistic-period city and temple', lat=25.590, lng=55.630,
    p='Late pre-Islamic', dr='1st century BC – 2nd century AD', el='Umm Al Quwain coast', ic='platform', era='H', t0=2075, t1=1825,
    te='A temple to the sun', ta='معبد للشمس', se='A coastal city whose temple named the sun god Shams in Aramaic', sa='مدينة ساحلية سمّى معبدها إله الشمس «شمس» بالآرامية',
    desc="One of the largest pre-Islamic sites in the Emirates, on the coast of Umm Al Quwain, partly excavated by an Iraqi mission in 1974 and by European missions from 1987. It belongs to the second phase of the Hellenistic period in the region; a Belgian team found a temple with three altars and an Aramaic inscription naming the solar deity Shams, together with imported glass and coins.",
    sig="The main port of the Gulf coast in the early centuries AD, linking Mleiha inland to the Roman and Parthian world.",
    ex='Iraqi mission 1974; Belgian, British, Danish and French missions 1987–1995',
    disc=['Temple of Shams with Aramaic inscription', 'Three altars'],
    refs=['Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.', 'Potts, D. T. (2003). Archaeology of the United Arab Emirates. Trident Press.'])

add(id='umm-an-nar-island', n='Umm an-Nar Island', na='جزيرة أم النار', c='archaeological', s='Type site of the Umm an-Nar culture', lat=24.440, lng=54.500,
    p='Umm an-Nar period', dr='c. 2700 – 2000 BC', el='50 above-ground tombs', ic='mound', era='P', t0=4725, t1=4025,
    te='The island that named an age', ta='الجزيرة التي سمّت عصرًا', se='Fifty round tombs excavated by the Danes in 1959 gave a whole culture its name', sa='خمسون قبرًا دائريًا نقّبها الدنماركيون عام 1959 أعطت ثقافة كاملة اسمها',
    desc="A small island beside Abu Dhabi where a Danish expedition in 1959 excavated a cemetery of 50 above-ground circular tombs and a settlement of fishers and traders. The finds defined the Umm an-Nar period (2700–2000 BC), when the coast traded copper, pearls and pottery with Mesopotamia and the Indus. The island is now inside an industrial area and not open to visitors.",
    sig="The reference site for the Bronze Age of the Emirates and Oman.",
    ex='Danish Archaeological Expedition (P. V. Glob, G. Bibby), 1959–1965',
    disc=['50 circular tombs', 'Settlement of the 3rd millennium BC'],
    refs=['Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.', 'Frifelt, K. (1991). The Island of Umm an-Nar. Jutland Archaeological Society.'])

add(id='julfar-kush', n='Julfar (Kush and Shimal)', na='جلفار (كوش والشمل)', c='archaeological', s='Medieval port of Ras Al Khaimah', lat=25.850, lng=56.000,
    p='Islamic', dr='13th – 17th century AD', el='Shimal plain, Ras Al Khaimah', ic='jar', era='H', t0=775, t1=375,
    te='The port of Chinese porcelain', ta='ميناء الخزف الصيني', se='A trading town that shipped pearls and horses and imported porcelain from China', sa='بلدة تجارية شحنت اللؤلؤ والخيول واستوردت الخزف من الصين',
    desc="The medieval port of Julfar, prominent in trade by the early 14th century and described by Duarte Barbosa in 1517, is now placed at Kush in the Shimal plain north of Ras Al Khaimah city; its oldest remains date to the 13th century. Excavations uncovered Chinese and East Asian porcelain among the houses of a town that traded pearls and horses across the Indian Ocean. Location approximate.",
    sig="The Emirates' main link to the Indian Ocean trade of the Middle Ages, and the home port of the navigator Ahmad ibn Majid.",
    ex='British (Kennet), Japanese, French and German missions, 1970s–1990s',
    disc=['Chinese porcelain in a 14th-century port', 'Town remains from the 13th century'],
    refs=['Emirates Natural History Group (2011). The United Arab Emirates throughout the ages.', 'Kennet, D. (2004). Sasanian and Islamic Pottery from Ras al-Khaimah. Archaeopress.'])

# ---------------- GEOLOGY ----------------
add(id='jebel-hafeet', n='Jebel Hafeet', na='جبل حفيت', c='geological', s='Folded Eocene mountain', lat=24.0586, lng=55.7775,
    p='Eocene to Miocene', dr='Rocks 56 – 16 million years old; folded 28 – 15 million years ago', el='1,249 m · 26 km long', ic='cliff', era='D', t0=56e6, t1=15e6,
    te='The mountain that leans', ta='الجبل المائل', se='A 26 km fold with one side tipped over, hot springs at its foot', sa='طيّة بطول 26 كم انقلب أحد جانبيها، وينابيع حارة عند قدمها',
    desc="An isolated mountain of 1,249 m on the UAE–Oman border near Al Ain, 26 km long and 4–5 km wide, trending NNW–SSE. It is an asymmetric anticline of shallow-marine limestone, marl and evaporite with corals, foraminifera and bryozoa, ranging from early Eocene in the core to early Miocene on the flanks; the west limb dips about 30° and the east limb is overturned at about 70°, probably over a backthrust, with folding dated to the late Oligocene to middle Miocene. Hot springs of about 40 °C at Green Mubazzarah come from water circulating 2 km down through faults beneath the fold. Caves reach at least 150 m. About 500 Hafit-period tombs lie on its foothills.",
    sig="The UAE's best-exposed anticline, the source of Al Ain's hot springs and the backdrop to its oldest tombs.",
    ex='Geological surveys of the UAE (Ministry of Energy / British Geological Survey)',
    disc=['East limb overturned at 70°', 'Hot springs at 40 °C'],
    refs=['Wikipedia contributors (2026). Jebel Hafeet, citing geological surveys of the Al Ain area.', 'Searle, M. P. & Ali, M. Y. (2009). Structural and tectonic evolution of the Jabal Sumeini–Al Ain–Buraimi region. GeoArabia 14(1).'])

add(id='buhais-geology-park', n='Buhais Geology Park', na='حديقة البحيص الجيولوجية', c='geological', s='Cretaceous sea floor on show', lat=25.030, lng=55.780,
    p='Cretaceous', dr='Rocks at least 93 million years old', el='Opened 21 January 2020', ic='fossil', era='D', t0=93e6, t1=66e6,
    te='Fossils from before the mountains', ta='أحافير من قبل الجبال', se='Ammonites and sea urchins from a sea that covered Sharjah 93 million years ago', sa='أمونيتات وقنافذ بحر من بحر غطّى الشارقة قبل 93 مليون عام',
    desc="A visitor park opened on 21 January 2020 on the limestone ridge of Jebel Buhais, displaying fossils and features dating back at least 93 million years to the Cretaceous, when the area lay beneath a shallow sea before the Hajar Mountains rose. The ridge runs almost continuously from Madam to Mleiha and also carries the Neolithic to Iron Age cemeteries of Jebel Buhais.",
    sig="The easiest place in the UAE to see the marine rocks that predate the ophiolite and the mountains.",
    ex='Sharjah Environment and Protected Areas Authority',
    disc=['Cretaceous fossils at least 93 million years old'],
    refs=['Sharjah Environment and Protected Areas Authority. Buhais Geology Park.', 'Wikipedia contributors (2026). Jebel Buhais.'])

add(id='moreeb-dune', n='Moreeb Dune (Liwa)', na='تل مرعب (ليوا)', c='geological', s='Tallest dune in the UAE', lat=22.990, lng=53.780,
    p='Quaternary', dr='Active today', el='About 300 m high · slip face 50°', ic='dune', era='D', t0=11700, t1=0,
    te='A wall of sand', ta='جدار من رمل', se='A 300 m dune at the edge of the Empty Quarter, 1.6 km long', sa='كثيب بارتفاع 300 م على حافة الربع الخالي، طوله 1.6 كم',
    desc="A dune about 300 m high and 1,600 m long with a slip face reported at 50°, about 25 km south of Liwa Oasis and 250 km from Abu Dhabi, at the northern edge of the Rub' al Khali (Empty Quarter). The tallest dune in the UAE, it hosts the Liwa Moreeb Dune Festival of hill-climb racing. The dunes of Liwa are the end of a sand sea that stretches across southern Arabia.",
    sig="The UAE's doorway to the largest sand desert on Earth.",
    ex='Abu Dhabi Department of Culture and Tourism (Liwa festival)',
    disc=['About 300 m high', 'Slip face about 50°'],
    refs=['Wikipedia contributors (2026). Moreeb Dune, citing Liwa Sports Club and Visit Abu Dhabi.'])

# ---------------- ECOLOGY ----------------
add(id='wadi-wurayah', n='Wadi Wurayah National Park', na='حديقة وادي الوريعة الوطنية', c='ecology', s='Mountain park on ancient ocean crust · World Heritage 2026', lat=25.400, lng=56.250,
    p='Living today', dr='National park 2009 · World Heritage 2026', el='225 km² · 300 springs · 60 streams', ic='river', era='N', t0=17, t1=0,
    te='Water in the mountains of the sea floor', ta='ماء في جبال قاع البحر', se='Springs and tahr on rocks that were once ocean crust, 90 million years old', sa='ينابيع ووعول على صخور كانت يومًا قشرة محيط عمرها 90 مليون عام',
    desc="A 225 km² park in the Hajar Mountains of Fujairah with more than 300 springs and 60 streams, designated the UAE's first mountain protected area in 2009 and inscribed on the World Heritage List at the 2026 session in Busan as the country's first natural site. Its rocks are ophiolite, fragments of oceanic crust about 90 million years old considered among the best preserved in the world. Surveys since 2006 have recorded 1,099 species, including the endangered Arabian tahr (one of its three remaining habitats), the Arabian caracal rediscovered in 2025, Blanford's fox and a dragonfly once thought extinct.",
    sig="The UAE's richest mountain ecosystem and its first natural World Heritage site, on a slice of the ocean floor.",
    ex='Fujairah Environment Authority with Emirates Nature–WWF, 2006 onwards',
    disc=['1,099 species recorded', 'Arabian caracal rediscovered 2025', 'Ophiolite about 90 million years old'],
    refs=['Scene Traveller (26 July 2026). Wadi Wurayah becomes UAE\'s first UNESCO natural World Heritage site.', 'Ramsar Sites Information Service. Wadi Wurayah National Park (site 1932), designated 2010.'])

add(id='al-wathba-wetland', n='Al Wathba Wetland Reserve', na='محمية الوثبة للأراضي الرطبة', c='ecology', s='Flamingo breeding wetland · Ramsar', lat=24.260, lng=54.750,
    p='Living today', dr='Reserve 1998 · Ramsar 2013', el='5 km²', ic='bird', era='N', t0=28, t1=0,
    te='Where flamingos chose to nest', ta='حيث اختار الفلامنغو أن يعشّش', se='Up to 3,600 flamingos on lakes fed by treated city water', sa='حتى 3,600 طائر فلامنغو على بحيرات تغذّيها مياه المدينة المعالجة',
    desc="A 5 km² wetland of lakes and sabkha south-east of Abu Dhabi city, declared a reserve in 1998 and the emirate's first Ramsar site in 2013, with water levels partly maintained by tertiary-treated wastewater. Greater flamingos first bred successfully in December 1998, fledging 10 young in April 1999, and have bred every year since 2011; January counts in 2013–2018 ranged from 2,500 to 3,600 birds. Recorded diversity: 236 bird, 39 plant, 15 reptile, 10 mammal and 354 invertebrate species, about 21% of the emirate's terrestrial species. Visitors rose from 2,560 in 2014–15 to 5,780 in 2017–18.",
    sig="The first regular flamingo breeding site in the Gulf states and a model of a wetland made with recycled water.",
    ex='Environment Agency – Abu Dhabi',
    disc=['First flamingo breeding, December 1998', '354 invertebrate species'],
    refs=['Campbell, O., Javed, S., Al Dhaheri, S. et al. (2018). Al Wathba Wetland Reserve, Abu Dhabi emirate: successful mixing of birds and people. Sandgrouse Supplement 4.', 'Ramsar Sites Information Service. Al Wathba Wetland Reserve (site 2142).'])

add(id='ras-al-khor', n='Ras Al Khor Wildlife Sanctuary', na='محمية رأس الخور', c='ecology', s='Flamingos at the end of Dubai Creek · Ramsar', lat=25.1917, lng=55.3219,
    p='Living today', dr='Ramsar site since 29 August 2007', el='620 ha', ic='bird', era='N', t0=19, t1=0,
    te='Flamingos among the towers', ta='فلامنغو بين الأبراج', se='Twenty thousand waterbirds winter in a lagoon ringed by the city', sa='عشرون ألف طائر مائي تشتو في بحيرة تحيط بها المدينة',
    desc="A 620 ha sanctuary of mangrove, lagoon, intertidal mud and sand flats and saline flats at the end of the 14 km Dubai Creek, designated a Ramsar site on 29 August 2007. More than 20,000 waterbirds of 67 species winter here, including more than 3,000 greater flamingos; more than 1% of the regional population of broad-billed sandpipers passes through, and the threatened sociable lapwing and greater spotted eagle occur. Over 450 animal and 47 plant species are recorded, and about 10,000 people visit each year.",
    sig="A wetland of international importance surviving inside one of the fastest-growing cities on Earth.",
    ex='Dubai Municipality (Environment Department)',
    disc=['More than 20,000 wintering waterbirds', 'More than 3,000 greater flamingos'],
    refs=['Ramsar Sites Information Service. Ras Al Khor Wildlife Sanctuary (site 1715), designated 2007.'])

add(id='khor-kalba', n='Khor Kalba Mangroves (Al Qurm)', na='قرم خور كلباء', c='ecology', s='Oldest mangrove woodland in the region · Ramsar', lat=24.9981, lng=56.3625,
    p='Living today', dr='Ramsar site since 10 March 2013', el='1,494 ha', ic='mangrove', era='N', t0=30, t1=0,
    te='The kingfisher’s only home', ta='بيت الرفراف الوحيد', se='Tall old mangroves where a kingfisher found nowhere else in the world breeds', sa='قرم عالٍ عتيق يتكاثر فيه رفراف لا يوجد في أي مكان آخر في العالم',
    desc="A 1,494 ha protected area on the Gulf of Oman coast of Sharjah near the Oman border, listed under Ramsar on 10 March 2013. Its Avicennia marina trees are the tallest and the most extensive mature mangrove woodland in the biogeographic region. The Kalba white-collared kingfisher (Todiramphus chloris kalbaensis), an endemic subspecies, breeds almost exclusively here; Sykes's warbler has one of its two regional breeding sites; hawksbill and green turtles enter the creeks at high tide to feed. Habitats also include beach, tidal channels, salt marsh and Acacia woodland.",
    sig="A relict mangrove forest that holds a bird found nowhere else on Earth.",
    ex='Sharjah Environment and Protected Areas Authority',
    disc=['Endemic Kalba kingfisher subspecies', 'Tallest mangroves in the region'],
    refs=['Ramsar Sites Information Service. Mangrove and Al Hafeya Protected Area in Khor Kalba (site 2125), designated 2013.'])

add(id='bu-tinah-dugongs', n='Marawah Marine Biosphere Reserve and Bu Tinah', na='محمية مروح البحرية وبو طينة', c='ecology', s='Densest dugong population in the world', lat=24.600, lng=53.080,
    p='Living today', dr='UNESCO biosphere reserve 2007', el='Shallow seagrass banks west of Abu Dhabi', ic='dolphin', era='N', t0=27, t1=0,
    te='Three thousand sea cows', ta='ثلاثة آلاف بقرة بحر', se='Abu Dhabi’s seagrass holds the second-largest dugong population after Australia', sa='تحتضن أعشاب أبوظبي البحرية ثاني أكبر تجمّع للأطوم بعد أستراليا',
    desc="The UAE's first UNESCO biosphere reserve, recognised in 2007, covering seagrass beds, coral reefs and mangroves around Marawah Island west of Abu Dhabi, with four turtle species and 70 fish species. The Environment Agency – Abu Dhabi protects about 3,000 dugongs, mostly in Marawah and the Al Yasat protected area, the largest population after Australia; Bu Tinah, inside the reserve, is described as the densest dugong population in the world. Dugongs have been studied here since 1999 by aerial survey, satellite tagging and genetics; threats are abandoned nets, habitat loss, pollution and boat strikes.",
    sig="The most important dugong habitat outside Australia.",
    ex='Environment Agency – Abu Dhabi, 1999 onwards',
    disc=['About 3,000 dugongs in Abu Dhabi waters', 'Bu Tinah: densest dugong population known'],
    refs=['Environment Agency – Abu Dhabi. Dugong (Dugong dugon) species page.', 'Gulf News (2 November 2007). Marawah is UAE\'s first biosphere reserve.'])

D = {'sites': S, 'stops': []}
json.dump(D, open('/tmp/w/gulf/ae/data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
