# Layers of Bahrain — researcher catalogue v0.1 (facts from the sources listed in each record's refs)
import json
S = []
def add(**k): S.append(k)

# ---------------- ARCHAEOLOGY ----------------
add(id='qalat-al-bahrain', n="Qal'at al-Bahrain", na='قلعة البحرين', c='archaeological', s='Dilmun capital · World Heritage', lat=26.2336, lng=50.5206,
    p='Dilmun to Portuguese periods', dr='c. 2300 BC – 16th century AD', el='Tell 12 m high · 17.5 ha', ic='wall', era='P', t0=4325, t1=400,
    te='The city under the fort', ta='المدينة تحت القلعة', se='Seven layers of a capital, from Dilmun to the Portuguese', sa='سبع طبقات لعاصمة، من دلمون إلى البرتغاليين',
    desc="A 12 m high tell on the north coast, 6 km from Manama, with seven stratified occupation layers from about 2300 BC to the 16th century AD. Regarded as the capital of Dilmun, it holds a Dilmun palace with warehouses, a Kassite palace, residential quarters on 12 m wide streets, city walls and gates, and the Portuguese fort on top that gave the site its name. About 25% of the 17.5 ha site has been excavated. Inscribed on the UNESCO World Heritage List in 2005.",
    sig="The longest continuous archaeological sequence in the Gulf and the only Dilmun-period city excavated at scale. About 50 cuneiform tablets were found, three from the reign of the Kassite king Agum.",
    ex='Danish expedition (Geoffrey Bibby), 1954–1972; French CNRS team from the 1970s; Danish–Bahraini teams since 1987',
    disc=['Dilmun palace and warehouse complex of the late 3rd millennium BC', 'Kassite palace with cuneiform tablets of king Agum', 'City walls, gates and streets 12 m wide', 'Portuguese fort of the 16th century on the summit'],
    refs=['Kervran, M., Hiebert, F. T. & Rougeulle, A. (2005). Qal\'at al-Bahrain: a trading and military outpost, 3rd millennium B.C.–17th century A.D. Brepols.', 'Crawford, H. & Rice, M. (2000). Traces of Paradise: the archaeology of Bahrain 2500 BC–300 AD. I.B. Tauris.', 'UNESCO World Heritage Centre. Qal\'at al-Bahrain – Ancient Harbour and Capital of Dilmun (ref. 1192), inscribed 2005.'])

add(id='barbar-temple', n='Barbar Temple', na='معبد باربار', c='archaeological', s='Dilmun temple complex', lat=26.2262, lng=50.4840,
    p='Early Dilmun', dr='c. 3000 – 2000 BC', el='Three superimposed temples', ic='platform', era='P', t0=5025, t1=3900,
    te='The temple of sweet water', ta='معبد الماء العذب', se='Three temples built over a sacred spring to the god of fresh water', sa='ثلاثة معابد بُنيت فوق عين مقدسة لإله الماء العذب',
    desc="Three temples built one above the other at the village of Barbar. Temple I (c. 3000 BC) stood on a platform about 25 by 16–18 m of local stone; Temple II, about 500 years later, enlarged the terrace in limestone; Temple III (2100–2000 BC) was the largest and stayed in use into the early 2nd millennium BC. A natural spring filled a pool in a subterranean shrine, read as the abzu of Enki, god of wisdom and fresh water, with channels carrying water to fields and gardens. Limestone blocks are thought to have been quarried on Jidda Island and brought by boat.",
    sig="The clearest expression of Dilmun's water cult and one of the oldest temple sequences in the Gulf. The copper bull's head from Temple II is the emblem of the Bahrain National Museum.",
    ex='Danish expedition (P. V. Glob; H. Andersen and P. Mortensen), 1954–1962; work resumed 2004',
    disc=['Copper bull\'s head from Temple II', 'Subterranean spring shrine with stone-lined pool', 'Three construction phases spanning a thousand years'],
    refs=['Andersen, H. H. & Højlund, F. (2003). The Barbar Temples. Jutland Archaeological Society.', 'Højlund, F. (2005). New excavations at the Barbar Temple, Bahrain. Arabian Archaeology and Epigraphy 16.', 'Mortensen, P. (1971). On the date of the Barbar Temple in Bahrain. Artibus Asiae.', 'Al Halwachi, H. (2020). The copper bull\'s head at Barbar temple: chemical composition and casting alloy. Journal of Archaeological Science: Reports 32.'])

add(id='saar-settlement', n='Saar Settlement and Temple', na='مستوطنة سار ومعبدها', c='archaeological', s='Early Dilmun town', lat=26.1967, lng=50.4856,
    p='Early Dilmun', dr='c. 2050 – 1800 BC', el='c. 2.5 ha', ic='jar', era='P', t0=4075, t1=3825,
    te='A town that kept its seals', ta='بلدة احتفظت بأختامها', se='Several hundred stamp seals from the houses of one small Dilmun town', sa='مئات الأختام من بيوت بلدة دلمونية صغيرة',
    desc="A planned Early Dilmun town of about 2.5 ha west of Manama, with houses along streets and a temple believed to have marked the summer solstice. Found in a 1977 survey and excavated 1977–1979 under M. Ibrahim, then by the London–Bahrain Archaeological Expedition in 1990–1999. Finds include copper fishhooks, bitumen imported from Mesopotamia, pearl-oyster shell and seed pearls, and several hundred stamp seals, four or five in a single house; 48 more came from the adjoining burial ground.",
    sig="The most complete plan of an ordinary Dilmun town and the richest seal assemblage from domestic contexts anywhere in the Gulf.",
    ex='London–Bahrain Archaeological Expedition (R. Killick, J. Moon, H. Crawford), 1990–1999',
    disc=['Several hundred Early Dilmun stamp seals', 'Temple aligned to the summer solstice', 'Copper fishhooks and imported bitumen'],
    refs=['Crawford, H., Killick, R. & Moon, J. (eds.) (1997). The Dilmun Temple at Saar. Kegan Paul International.', 'Killick, R. & Moon, J. (eds.) (2005). The Early Dilmun Settlement at Saar. Archaeology International.', 'Crawford, H. (1997). The site of Saar: Dilmun reconsidered. Antiquity 71, 701–708.'])

add(id='ain-umm-sujoor', n='Ain Umm es-Sujur (Diraz)', na='عين أم السجور', c='archaeological', s='Dilmun spring and well shrine', lat=26.2218, lng=50.4701,
    p='Early Dilmun', dr='3rd millennium BC', el='Oval hollow c. 60 × 30 m', ic='well', era='P', t0=4525, t1=3525,
    te='The well that was a temple', ta='البئر التي كانت معبدًا', se='Stone-built wells at a spring, treated as holy places', sa='آبار مبنية بالحجر عند عين، عوملت كأماكن مقدسة',
    desc="A spring site in Diraz whose name means 'mother of the spring of overflowing waters'. An oval hollow about 60 by 30 m holds stone-built wells dated to the 3rd millennium BC, with rooms and ovens added later on the south side. First dug by the Danish expedition in 1954; a Rikkyo University (Japan) team in the 1990s identified three wells and was the first to interpret them as holy places. The northern well is known as the water temple.",
    sig="Links the Dilmun water cult of Barbar to the island's spring line; one of the few shrines built directly on a spring.",
    ex='Danish expedition 1954; Rikkyo University expedition, 1990s',
    disc=['Three stone-lined wells of the 3rd millennium BC', 'Later rooms and ovens on the southern side'],
    refs=['Matsumoto, K. & Oguchi, K. (2001). Expeditions and discoveries in West Asia by Japanese archaeologists. Orient 36(1), 7–33.', 'Bibby, G. (1969). Looking for Dilmun. Knopf.'])

add(id='aali-royal-mounds', n="A'ali Royal Mounds", na='تلال عالي الملكية', c='archaeological', s='Royal tumuli of Early Dilmun · World Heritage', lat=26.1497, lng=50.5128,
    p='Early Dilmun', dr='c. 2050 – 1750 BC', el='Up to 50 m across and 12 m high', ic='mound', era='P', t0=4075, t1=3775,
    te='Where the kings of Dilmun lie', ta='حيث يرقد ملوك دلمون', se='Seventeen giant mounds in one village, the tombs of Dilmun’s first kings', sa='سبعة عشر تلًا عملاقًا في قرية واحدة، مدافن أوائل ملوك دلمون',
    desc="Seventeen royal mounds (13 single and two pairs) in the village of A'ali, up to 50 m in diameter and 12 m high, built between about 2050 and 1750 BC when Dilmun was ruled by kings. Chieftain mounds of 13–26 m lie around them. Three cuneiform inscriptions were found in Mound 8. The royal mounds form 15 of the 21 components of the Dilmun Burial Mounds World Heritage property inscribed in 2019.",
    sig="The earliest monumental royal tombs in Eastern Arabia and the main evidence for the emergence of kingship in Dilmun.",
    ex='Bahrain Authority for Culture and Antiquities with Moesgaard Museum (S. T. Laursen), 2010s',
    disc=['Royal mounds up to 50 m wide and 12 m high', 'Cuneiform inscriptions from Mound 8', 'Chieftain mounds of 13–26 m diameter'],
    refs=['Laursen, S. T. (2017). The Royal Mounds of A\'ali in Bahrain: the emergence of kingship in Early Dilmun. Aarhus University Press.', 'Bahrain Authority for Culture and Antiquities. Typology of Dilmun burial mounds (culture.gov.bh).', 'UNESCO World Heritage Centre. Dilmun Burial Mounds (ref. 1542), inscribed 2019.'])

add(id='hamad-town-moundfields', n='Hamad Town and Janabiyah Mound Fields', na='حقول تلال مدينة حمد والجنبية', c='archaeological', s='Dilmun burial mound fields · World Heritage', lat=26.1180, lng=50.4950,
    p='Early Dilmun', dr='c. 2200 – 1750 BC', el='Fields of some dozen to several thousand tumuli', ic='mound', era='P', t0=4225, t1=3775,
    te='A landscape of the dead', ta='مشهد للموتى', se='Tens of thousands of small mounds once covered the north of the island', sa='عشرات الآلاف من التلال الصغيرة غطّت يومًا شمال الجزيرة',
    desc="Mound fields west and south of A'ali that make up six of the 21 components of the Dilmun Burial Mounds property, about 11,774 mounds in all. Early Type mounds (c. 2200–2050 BC) average 2.5 m across and under 1.5 m high; about 1,000 survive of an estimated 17,000. Late Type mounds (c. 2050–1750 BC) are 6–11 m across and 2–3 m high; mapping suggested 58,000 once existed, with about 13,500 remaining. Each mound covers a central stone chamber inside a low ring wall; Janabiyah and Madinat Hamad 2 hold mounds with subsidiary burials.",
    sig="One of the densest Bronze Age cemetery landscapes known anywhere, and a record of how a whole island population buried its dead for four centuries.",
    ex='Danish excavations from 1954; Bahrain National Museum survey and mapping projects',
    disc=['Early Type mounds of 2.5 m average diameter', 'Late Type mounds 6–11 m across with ring walls', 'Mounds with subsidiary burials at Janabiyah'],
    refs=['Højlund, F. (2007). The Burial Mounds of Bahrain: social complexity in Early Dilmun. Jutland Archaeological Society.', 'Bahrain Authority for Culture and Antiquities. Typology of Dilmun burial mounds (culture.gov.bh).', 'UNESCO World Heritage Centre. Dilmun Burial Mounds (ref. 1542), inscribed 2019.'])

add(id='shakhura-necropolis', n='Shakhura Necropolis', na='مدافن الشاخورة', c='archaeological', s='Tylos-period burial mound', lat=26.2010, lng=50.5240,
    p='Tylos (Hellenistic to Parthian)', dr='3rd century BC – 4th century AD', el='Main mound c. 80 m long', ic='jar', era='H', t0=2275, t1=1625,
    te='Feasts for the dead', ta='ولائم للموتى', se='Ninety graves in one mound, and the ashes of funeral banquets', sa='تسعون قبرًا في تل واحد، ورماد ولائم الجنازة',
    desc="A burial mound about 80 m long in the village of Shakhura, used from the 3rd century BC to the 4th century AD, when Bahrain was known as Tylos. Excavations led by Captain Robert Higham in the 1960s found 90 graves, the earliest at the centre and later ones added in arcs, with Roman and Parthian artefacts including an intact ribbed glass bowl now in the British Museum. A 2008 excavation found an ash layer with glazed pottery, fish and animal bones, read as the remains of funeral banquets. The mound was largely demolished in the 1990s.",
    sig="A key site for the Tylos period, when the island traded with the Hellenistic and Parthian worlds.",
    ex='R. Higham, 1960s; Bahrain National Museum, 2008',
    disc=['Intact ribbed glass bowl of Roman date', 'Ash layer with food remains from funeral banquets'],
    refs=['Crawford, H. & Rice, M. (2000). Traces of Paradise: the archaeology of Bahrain 2500 BC–300 AD. I.B. Tauris.', 'Salles, J.-F. & Lombard, P. (eds.). Les fouilles françaises de Abu Saiba: données nouvelles sur la phase Tylos de Bahreïn. Proceedings of the Seminar for Arabian Studies.'])

add(id='khamis-mosque', n='Al-Khamis Mosque', na='مسجد الخميس', c='archaeological', s='Early Islamic mosque with twin minarets', lat=26.2083, lng=50.5483,
    p='Islamic (Uyunid to Usfurid)', dr='11th – 15th century AD (traditionally 692 AD)', el='Building 22.8 × 20 m', ic='platform', era='H', t0=950, t1=550,
    te='Two minarets, two centuries apart', ta='مئذنتان بينهما قرنان', se='The oldest standing mosque in Bahrain, rebuilt twice', sa='أقدم مسجد قائم في البحرين، أُعيد بناؤه مرتين',
    desc="Traditionally founded in 692 AD, but an inscription points to an 11th-century foundation under the Uyunids, when it had one minaret; the second minaret was added about two centuries later under the Usfurids. The mosque was rebuilt in the 14th and 15th centuries: an early prayer hall with a flat roof on wooden columns, and a later section on arches and masonry piers dated to 1339. A 12th-century limestone mihrab slab carrying Qur'anic verses was found during restoration. Recent excavations by the Early Islamic Bahrain Project place it within Bilad al-Qadim, the main centre of settlement in the 11th–13th centuries.",
    sig="The principal surviving monument of medieval Bahrain and the anchor of the Bilad al-Qadim heritage trail.",
    ex='Early Islamic Bahrain Project (T. Insoll, University of Exeter) with the Bahrain Authority for Culture and Antiquities',
    disc=['12th-century mihrab slab with Qur\'anic inscription', 'Prayer hall section dated 1339'],
    refs=['Insoll, T., Almahari, S., MacLean, R. et al. (2016). Bilad al-Qadim revisited: recent archaeological research at the Al-Khamis Mosque, Ain Abu Zaydan and Abu Anbra, Bahrain. Arabian Archaeology and Epigraphy.', 'Petersen, A. (1996). Dictionary of Islamic Architecture. Routledge.'])

add(id='bilad-al-qadim', n='Bilad al-Qadim', na='بلاد القديم', c='archaeological', s='Medieval Islamic settlement', lat=26.2110, lng=50.5530,
    p='Islamic', dr='11th – 13th century AD', el='North-east of Awal island', ic='map', era='H', t0=975, t1=725,
    te='The old town', ta='البلد القديم', se='The main town of the island when Manama did not yet exist', sa='البلدة الرئيسية في الجزيرة قبل أن توجد المنامة',
    desc="An area of Islamic-period settlement in the north-east of the main island, the main centre of settlement in the 11th–13th centuries AD, named 'the old town' after Manama grew beside it. Excavations by the Anglo-Bahraini Early Islamic Bahrain Project at the Al-Khamis Mosque, the spring of Ain Abu Zaydan and the Abu Anbra cemetery have traced houses, water systems and burials of the medieval town.",
    sig="The only medieval Islamic town in the Gulf islands studied over two decades of excavation; a bridge between Dilmun-era springs and the modern capital.",
    ex='Early Islamic Bahrain Project (University of Manchester, then Exeter; T. Insoll), 2001 onwards',
    disc=['Medieval houses and water channels at Ain Abu Zaydan', 'Abu Anbra cemetery'],
    refs=['Insoll, T. (2005). The Land of Enki in the Islamic Era: pearls, palms and religious identity in Bahrain. Kegan Paul.', 'Insoll, T., Almahari, S., MacLean, R. et al. (2016). Bilad al-Qadim revisited. Arabian Archaeology and Epigraphy.'])

add(id='arad-fort', n='Arad Fort', na='قلعة عراد', c='archaeological', s='Islamic coastal fort', lat=26.2525, lng=50.6275,
    p='Late Islamic', dr='Late 15th – early 16th century AD', el='Square plan with four round towers', ic='wall', era='H', t0=530, t1=200,
    te='The fort on its own island', ta='القلعة على جزيرتها', se='A square fort that once stood on an islet, now joined to Muharraq', sa='قلعة مربعة كانت على جزيرة صغيرة، التحمت اليوم بالمحرق',
    desc="A square fort with a cylindrical tower at each corner, built in the late 15th or early 16th century, before the Portuguese occupation of 1622; a Portuguese map of about 1635 shows it under siege with inner and outer walls. A trench once filled from wells surrounded it, and nose-shaped openings for marksmen pierce the upper walls. Restored in 1984–1987 under architect Archie Walls using sea stone, lime, sand and palm trunks, without cement. The fort stood on a separate islet before land reclamation joined it to Muharraq.",
    sig="The best-preserved Islamic-period fort in Bahrain and a model restoration in traditional materials.",
    ex='Restoration by A. G. Walls, Directorate of Tourism and Archaeology, 1984–1987',
    disc=['Portuguese siege map of c. 1635', 'Restoration without cement, 1984–1987'],
    refs=['Walls, A. G. (1987). Arad Fort, Bahrain: its restoration, its history and defences. Directorate of Tourism and Archaeology, Bahrain.', 'Walls, A. G. (2004). Arabian mud brick technology: some thoughts after the Bam earthquake. Construction History Society Newsletter 69, 11–19.'])

add(id='riffa-fort', n='Riffa Fort', na='قلعة الرفاع', c='archaeological', s='19th-century fort on the escarpment', lat=26.1152, lng=50.5565,
    p='Modern', dr='Rebuilt 1812 – 1818', el='On the cliff over the Hunanaiya valley', ic='wall', era='H', t0=320, t1=200,
    te='A house on the cliff', ta='بيت على الجرف', se='Rebuilt in 1812 on an older foundation, home of the ruling family', sa='أُعيد بناؤها عام 1812 على أساس أقدم، وكانت مسكن الأسرة الحاكمة',
    desc="A fort on the cliff between East and West Riffa, first built in the early 18th century by Fareer bin Rahhal and rebuilt on its foundations in 1812–1818 by Sheikh Salman bin Ahmed Al Fateh Al Khalifa, who used it as a residence. Sheikh Isa bin Ali Al Khalifa, ruler from 1869 to 1932, was born here. The fort was restored in 1993 and overlooks the desert valley cut into the island's interior escarpment.",
    sig="Marks the move of the ruling family's seat inland in the early 19th century and sits on the island's geological rim.",
    ex='Bahrain Authority for Culture and Antiquities (restoration 1993)',
    disc=['Early 18th-century foundation beneath the 1812 fort', 'Birthplace of Sheikh Isa bin Ali Al Khalifa'],
    refs=['Bahrain Authority for Culture and Antiquities. Sheikh Salman bin Ahmed Al Fateh Fort (bahrain.com).', 'Bahrain News Agency. قلعة الرفاع بنيت عام 1812م.'])

add(id='pearling-path', n='Pearling Path and Bu Maher Fort', na='طريق اللؤلؤ وقلعة بو ماهر', c='archaeological', s='Pearling heritage · World Heritage', lat=26.2413, lng=50.6135,
    p='Pearling economy', dr='2nd century AD – 1930s', el='3.5 km trail · 17 buildings · 3 oyster beds', ic='boat', era='H', t0=1900, t1=90,
    te='The road to the oyster beds', ta='الطريق إلى مغاصات اللؤلؤ', se='Seventeen houses, a fort and three oyster beds that made an island economy', sa='سبعة عشر بيتًا وقلعة وثلاث مغاصات صنعت اقتصاد جزيرة',
    desc="A 3.5 km path through Muharraq linking 17 historic buildings, from the seafront Bu Maher fort on the island's southern tip to the Siyadi complex, together with three oyster beds in the northern waters. Pearl diving in the Gulf is mentioned in Assyrian texts of about 2000 BC; the economy that these buildings record ran from the 2nd century to the 1930s, with a golden age from the 1850s to 1930, before oil was found in 1932 and cultured pearls ended the trade. Inscribed on the World Heritage List on 30 June 2012.",
    sig="The last complete example of the cultural tradition of pearling that shaped the Gulf for two millennia.",
    ex='Bahrain Authority for Culture and Antiquities; Pearling Path visitor centre (Aga Khan Award 2019)',
    disc=['Bu Maher fort at the departure point of the pearling fleet', 'Three oyster beds (hayrat) in the northern waters'],
    refs=['UNESCO World Heritage Centre. Pearling, Testimony of an Island Economy (ref. 1364rev), inscribed 2012.', 'Faroughy, A. (1951). The Bahrein Islands (750–1951). Verry, Fisher & Co.'])

# ---------------- GEOLOGY ----------------
add(id='jebel-dukhan', n='Jebel Dukhan', na='جبل الدخان', c='geological', s='Crest of the Bahrain anticline', lat=26.0333, lng=50.5500,
    p='Eocene', dr='c. 56 – 34 million years ago', el='134.1 m, the island\'s highest point', ic='cliff', era='D', t0=56e6, t1=34e6,
    te='The mountain of smoke', ta='جبل الدخان', se='The highest point of a slow dome of Eocene limestone', sa='أعلى نقطة في قبة بطيئة من حجر الإيوسين الجيري',
    desc="The island's highest point at 134.1 m, near its geographic centre, on the axis of the north–south Bahrain anticline. The fold is simple, with no surface faults; subsurface faults are normal tension faults with throws usually under 15 m. The core exposes the lower Eocene Rus Formation (about 67 m thick, chalky dolomitic limestone with chert and anhydrite), overlain by the Dammam Formation, whose rimrock of Eocene limestone encircles the central basin in cliffs more than 30 m high. Bahrain's first oil well was drilled at its foot in 1932.",
    sig="The structural heart of Bahrain: the anticline that traps the island's oil and gas and lifts its oldest rocks to the surface.",
    ex='U.S. Geological Survey / Bahrain Petroleum Company (Willis 1967)',
    disc=['Rus Formation: 67 m of chalky limestone with anhydrite', 'Dammam rimrock cliffs over 30 m high', 'Anticline without surface faults'],
    refs=['Willis, R. P. (1967). Geology of the Arabian Peninsula: Bahrain. U.S. Geological Survey Professional Paper 560-E.'])

add(id='first-oil-well', n='First Oil Well and the Bahrain Field', na='أول بئر نفط وحقل البحرين', c='geological', s='Oil discovery of 1932', lat=26.0394, lng=50.5480,
    p='Petroleum geology', dr='1931 – present', el='Reservoirs 380 – 2,000 m deep', ic='oil', era='N', t0=95, t1=0,
    te='Where the Gulf’s oil age began', ta='حيث بدأ عصر النفط في الخليج', se='Oil first spurted below Jebel Dukhan on 16 October 1931', sa='تدفق النفط أول مرة أسفل جبل الدخان في 16 أكتوبر 1931',
    desc="Well No. 1 below Jebel Dukhan, where oil first spurted on 16 October 1931 and flowed from 2 June 1932: the first oil found on the Arabian side of the Gulf. Frank Holmes had won a concession in 1925 after first finding fresh water for the ruler; the Bahrain Petroleum Company (Bapco) was set up in 1929 by Standard Oil of California. The Awali (now Bahrain) field covers about 400 km², roughly 80% of the main island, with oil reservoirs between 380 and 2,000 m and gas to nearly 4,000 m. Output peaked at about 80,000 barrels a day in 1971; gas was found in 1948 and the offshore Abu Safah field in 1963.",
    sig="The discovery that started the Gulf oil industry, drilled on the anticline that geology had already revealed at the surface.",
    ex='Bahrain Petroleum Company (Bapco), nationalised 1980',
    disc=['First oil on the Arabian side of the Gulf, 1931–1932', 'Field of 400 km² under 80% of the island'],
    refs=['Archer, S. (2012). Bahrain: 80 years and still producing. GEO ExPro.', 'Vassiliou, M. (2009). Historical Dictionary of the Petroleum Industry. Scarecrow Press.'])

add(id='interior-basin', n='Interior Basin and Rimrock Escarpment', na='الحوض الداخلي والجرف الحلقي', c='geological', s='Eroded core of the anticline', lat=26.0700, lng=50.5200,
    p='Eocene to Quaternary', dr='Rocks 56 – 34 million years old; landform Quaternary', el='Cliffs over 30 m', ic='cliff', era='D', t0=2.58e6, t1=0,
    te='The bowl in the middle of the island', ta='الحوض في قلب الجزيرة', se='A ring of limestone cliffs around a hollow where the dome was eaten away', sa='حلقة من الجروف الجيرية حول تجويف أُكلت فيه القبة',
    desc="A closed basin in the centre of the island, ringed by a rimrock of Eocene Dammam limestone standing in cliffs more than 30 m high. Erosion cut through the crest of the Bahrain anticline, removing the younger beds and exposing the Rus Formation inside the ring; the basin is the only place with meaningful local recharge of groundwater. The Dammam Formation has four members here: the 'shark's-tooth shale' (9–15 m), a brown crystalline limestone (about 33 m), an orange marl (6–20 m) and a white limestone (6–62 m).",
    sig="A textbook breached anticline, and the landscape that explains Bahrain's springs, quarries and oil in one view.",
    ex='U.S. Geological Survey (Willis 1967)',
    disc=['Breached anticline with inward-facing cliffs', 'Four members of the Dammam Formation exposed'],
    refs=['Willis, R. P. (1967). Geology of the Arabian Peninsula: Bahrain. U.S. Geological Survey Professional Paper 560-E.'])

add(id='sharks-tooth-shale', n="Shark's-Tooth Shale", na='طفل أسنان القرش', c='geological', s='Fossil bed of the Dammam Formation', lat=26.0550, lng=50.5700,
    p='Lower to middle Eocene', dr='c. 50 million years ago', el='9 – 15 m thick', ic='fossil', era='D', t0=50e6, t1=45e6,
    te='Teeth from a vanished sea', ta='أسنان من بحر زال', se='A grey shale full of shark teeth, laid down when Bahrain was sea floor', sa='طفل رمادي مليء بأسنان القرش، ترسّب حين كانت البحرين قاع بحر',
    desc="The lowest member of the Dammam Formation on Bahrain: 9.1–15.2 m of grey to yellow shale and marl named for its abundant fossil shark teeth, exposed on the inner slopes of the rimrock. It records the shallow Eocene sea that covered the region about 50 million years ago, before the Tertiary limestones were uplifted on the anticline.",
    sig="The island's most accessible fossil bed and a marker horizon used to map the whole Dammam Formation across eastern Arabia.",
    ex='U.S. Geological Survey (Willis 1967)',
    disc=['Fossil shark teeth in a 9–15 m marl and shale bed'],
    refs=['Willis, R. P. (1967). Geology of the Arabian Peninsula: Bahrain. U.S. Geological Survey Professional Paper 560-E.'])

add(id='dammam-aquifer-springs', n='Dammam Aquifer and the Springs', na='خزان الدمام والعيون', c='geological', s='Artesian springs of the land of two seas', lat=26.1960, lng=50.5560,
    p='Holocene to present', dr='Springs used for over 4,000 years', el='Ain Adhari, Adhari Park', ic='river', era='N', t0=4525, t1=0,
    te='The water that made Bahrain', ta='الماء الذي صنع البحرين', se='Fresh water from Saudi Arabia rises through the island’s limestone', sa='ماء عذب من السعودية يصعد عبر حجر الجزيرة الجيري',
    desc="Bahrain's springs rise from the Dammam Formation's Khobar and Alat limestones, recharged where the beds outcrop in Saudi Arabia; the Khobar member supplies over 75% of groundwater. Ain Adhari, south-west of Manama, was described as a river of fast water about three metres wide feeding the date groves. Abstraction from the Dammam rose from about 63 million m³ in 1952 to 188 million m³ in 2001, about 68% above the estimated inflow of 112 million m³, and the saline front advanced 60–139 m a year; most springs, including Adhari, no longer flow naturally and almost 70% of usable groundwater has been lost or salinised.",
    sig="The hydrogeology behind Dilmun's temples, the medieval towns and the island's name, and a warning written in salt.",
    ex='Bahrain Ministry of Works; University of Plymouth (Al-Noaimi 2004)',
    disc=['Khobar limestone yields over 75% of groundwater', 'Abstraction 68% above inflow by 2001', 'Saline front moving 60–139 m per year'],
    refs=['Al-Noaimi, M. A. (2004). Development of water resources in Bahrain: a combined approach of supply–demand analysis. PhD thesis, University of Plymouth.', 'Willis, R. P. (1967). Geology of the Arabian Peninsula: Bahrain. USGS Professional Paper 560-E.', 'News of Bahrain. The land of two seas: the freshwater springs that made Bahrain.'])

add(id='submarine-springs', n='Submarine Freshwater Springs', na='العيون البحرية', c='geological', s='Fresh water rising from the sea floor', lat=26.3000, lng=50.6400,
    p='Holocene to present', dr='Recorded 1829 – 20th century', el='About 3 fathoms (5.5 m) depth', ic='wave', era='N', t0=4525, t1=0,
    te='Sweet water under salt', ta='ماء عذب تحت الملح', se='Divers filled goatskins from springs on the sea bed, especially off Muharraq', sa='غاصوا ليملأوا القِرب من عيون في قاع البحر، خصوصًا قبالة المحرق',
    desc="Fresh water from the same Eocene aquifer that feeds the land springs also rises through the sea floor around the islands, most numerously off Muharraq. An 1829 British traveller described a spring in about three fathoms of water; divers fitted a jar over the spring mouth and filled goatskin bags, and pearling crews used the springs to take on water at sea. The phenomenon is the origin of the name 'Bahrain', the two seas of salt and sweet water. Location shown is approximate.",
    sig="A rare hydrogeological phenomenon that shaped a pearling economy and a country's name.",
    ex='Historical accounts (1829; early 20th-century British gazetteer)',
    disc=['Springs in about 5 m of water off Muharraq', 'Goatskin bags filled by divers for pearling fleets'],
    refs=['News of Bahrain. The land of two seas: the freshwater springs that made Bahrain.', 'Al-Noaimi, M. A. (2004). Development of water resources in Bahrain. PhD thesis, University of Plymouth.'])

add(id='ras-al-barr-sabkha', n='Ras al-Barr Sabkha', na='سبخة رأس البر', c='geological', s='Coastal salt flats of the south', lat=25.8300, lng=50.5500,
    p='Holocene', dr='Last few thousand years', el='Sea level, southern tip', ic='salt', era='D', t0=6000, t1=0,
    te='Where the island turns to salt', ta='حيث تتحول الجزيرة إلى ملح', se='Beach sands and salt crusts on the island’s quiet southern tip', sa='رمال شاطئية وقشور ملح على طرف الجزيرة الجنوبي الهادئ',
    desc="Recent beach sands and sabkha (salt-flat) deposits concentrated at Ra's al Jaza'ir and Ra's al Barr in the south and south-west of the island, where the land is low and the Eocene aquifers carry water too saline for use. The sabkha surface forms as sea water and brine evaporate in the capillary zone, leaving gypsum and halite crusts; the sand gazelle and migrating waders use the surrounding flats.",
    sig="The modern end of Bahrain's story: evaporite forming today on the same island whose Eocene rocks hold anhydrite from an older sea.",
    ex='U.S. Geological Survey (Willis 1967)',
    disc=['Sabkha and beach deposits at Ras al Jazayir and Ras al Barr'],
    refs=['Willis, R. P. (1967). Geology of the Arabian Peninsula: Bahrain. U.S. Geological Survey Professional Paper 560-E.'])

# ---------------- ECOLOGY ----------------
add(id='hawar-islands', n='Hawar Islands', na='جزر حوار', c='ecology', s='Ramsar site · Socotra cormorant colony', lat=25.6667, lng=50.8333,
    p='Living today', dr='Ramsar site since 1997', el='5,200 ha · 16 main islands', ic='bird', era='N', t0=30, t1=0,
    te='Islands of a hundred thousand birds', ta='جزر مئة ألف طائر', se='The world’s largest breeding colony of Socotra cormorants, with dugongs and gazelles', sa='أكبر مستعمرة تكاثر لغراب البحر السوقطري في العالم، مع الأطوم والغزلان',
    desc="An archipelago of 16 main desert islands (36 in all) about 19 km south-east of the main island, with a highest point of 22 m; Hawar itself is over 41 km². Designated a Ramsar wetland of 5,200 ha on 27 October 1997 and a national protected area with access restricted by the coast guard. In 1992, 200,000–300,000 adult Socotra cormorants were recorded, the largest known breeding concentration in the world; greater flamingos and gulls winter in numbers, dugongs and sea turtles feed on the seagrass beds, and reintroduced Arabian oryx and sand gazelle live on the main island.",
    sig="One of the most important seabird sites in the Middle East and the only part of Bahrain in near-pristine condition.",
    ex='Hawar Islands Protected Area Management Plan (2003); BirdLife International',
    disc=['200,000–300,000 Socotra cormorants counted in 1992', 'Ramsar site no. 920, 5,200 ha', 'Reintroduced oryx and gazelle'],
    refs=['Ramsar Sites Information Service. Hawar Islands (site 920), designated 1997.', 'BirdLife International (2024). Important Bird Area factsheet: Hawar Islands.', 'IUCN (2004). Evaluation of the Hawar Islands World Heritage nomination.'])

add(id='tubli-bay', n='Tubli Bay and Ras Sanad Mangroves', na='خليج توبلي وقرم رأس سند', c='ecology', s='Ramsar site · last mangroves', lat=26.1732, lng=50.5722,
    p='Living today', dr='Protected by Royal Decree 2006', el='1,350 ha', ic='mangrove', era='N', t0=30, t1=0,
    te='The last mangroves', ta='آخر أشجار القرم', se='A shrinking bay that still feeds thousands of wintering shorebirds', sa='خليج يتقلص لكنه ما زال يطعم آلاف الطيور الشاطئية الشاتية',
    desc="A shallow bay of 1,350 ha between Manama and Sitra, protected by Royal Decree in 2006 and listed as a Ramsar wetland. The Avicennia marina stand at Ras Sanad in its south-west corner is Bahrain's last natural mangrove and a wildlife reserve. It is the country's most important site for migrating and wintering waterbirds, with counts of 2,000 black-headed gulls, 1,000 little stints, 300 ringed plovers and 250 ruddy turnstones. Since 1975 most of the original mangrove, intertidal and date-palm habitats have been lost to reclamation, roads and sewage, especially on the northern shore.",
    sig="A living remnant of the mangrove coast that once lined the island, and a measure of what reclamation costs.",
    ex='Supreme Council for Environment; BirdLife International (Key Biodiversity Area 8017)',
    disc=['Last natural Avicennia mangrove in Bahrain', 'Counts of up to 2,000 black-headed gulls'],
    refs=['BirdLife International. Key Biodiversity Area factsheet: Tubli Bay (KBA 8017).', 'Ramsar Sites Information Service. Tubli Bay (site 921).'])

add(id='al-areen', n='Al Areen Wildlife Park and Reserve', na='محمية العرين', c='ecology', s='Captive-breeding reserve for Arabian wildlife', lat=26.0156, lng=50.4956,
    p='Living today', dr='Founded 1976', el='8 km² in two halves', ic='gazelle', era='N', t0=50, t1=0,
    te='Where the oryx came back', ta='حيث عاد المها', se='A fenced reserve that bred the Arabian oryx and gazelle for release on Hawar', sa='محمية مسيّجة ربّت المها العربي والغزال لإطلاقهما في حوار',
    desc="A fenced desert reserve of about 8 km² at Sakhir on the west side of the island, founded in 1976 and divided into a public park and a protected reserve with two surface reservoirs. It holds indigenous plants and animals plus exotic species from Africa and Asia, with 82 bird species and more than 45 animal species recorded; its flagship animals are the Arabian oryx, once extinct in the wild, and the reem (sand) gazelle. Oryx and gazelle bred here were reintroduced to the Hawar Islands.",
    sig="The source population for Bahrain's reintroduced large mammals and its main environmental education site.",
    ex='Supreme Council for Environment / Al Areen Wildlife Park',
    disc=['Arabian oryx breeding herd', 'Oryx and gazelle reintroduced to Hawar'],
    refs=['Bahrain Clearing-House Mechanism (CBD). Al-Areen Wildlife Park and Reserve.', 'Oxford Business Group (2011). The Report: Bahrain 2011.'])

add(id='fasht-al-adhm', n='Fasht Al Adhm Coral Reef', na='فشت العظم', c='ecology', s='Largest coral platform of Bahrain', lat=26.2500, lng=50.8000,
    p='Living today', dr='Bleaching 1996, 1998, 2017', el='c. 200 km² reef area', ic='crab', era='N', t0=30, t1=0,
    te='A reef at the edge of endurance', ta='شعاب على حافة الاحتمال', se='Corals here survive 37 °C summers, then lose almost everything in a bad year', sa='تصمد الشعاب هنا أمام صيف بحرارة 37 درجة، ثم تخسر كل شيء تقريبًا في سنة سيئة',
    desc="A reef platform of about 200 km² east of the main island; Bahrain's reef areas (fashts) total about 850 km², more than its land area. In the 1980s about 30 coral species were recorded, with Acropora cover of 50–90% in 1988; mass bleaching in 1996 (37.7 °C) and 1998 (38 °C) hit Bahrain harder than any other Gulf country, and the 2017 event, above 34 °C from July to October, cut nearshore hard-coral cover from 13.6% to 1.4%. The survivors are massive Platygyra, Favia and Porites; branching corals are essentially gone, and the nearshore carbonate budget has fallen to near zero.",
    sig="Among the world's most heat-tolerant reefs, and a front line of climate change in the Gulf.",
    ex='AlMealla, Edullantes & Hepburn, University of Essex / Bahrain (2024)',
    disc=['Coral cover 50–90% in 1988, over 90% lost within years', 'Nearshore hard coral down to 1.4% after 2017'],
    refs=['AlMealla, R. K., Edullantes, B. & Hepburn, L. J. (2024). Bleaching threatens positive carbonate budgets on Bahraini reefs. Marine Biology 171, 39.'])

add(id='gulf-of-salwa-dugongs', n='Dugongs of the Gulf of Salwa', na='أطوم خليج سلوى', c='ecology', s='Second-largest dugong population', lat=25.7500, lng=50.7200,
    p='Living today', dr='Surveys 1986 – 2016', el='Waters under 10 m deep', ic='dolphin', era='N', t0=40, t1=0,
    te='The sea cows of the shallows', ta='أبقار البحر في الضحال', se='Herds of several hundred dugongs graze the seagrass between Bahrain and Qatar', sa='قطعان من مئات الأطوم ترعى الأعشاب البحرية بين البحرين وقطر',
    desc="The shallow waters south of Bahrain, mostly under 10 m deep with extensive Halodule and Halophila seagrass, hold the world's second-largest dugong population after Australia. A herd of 674 was counted in March 1986, with calves 15.7% of the group; winter surveys in 2004 recorded groups of 577 and 97 between Bahrain and Qatar, and 508 animals were counted in under 1 km² in 2015–2016. Bahrain surveys in 2006 gave estimates similar to those of twenty years earlier. The area is an Important Marine Mammal Area of 10,676 km² that also holds humpback and bottlenose dolphins and finless porpoises.",
    sig="A globally important population of a vulnerable species, dependent on the same seagrass that feeds Hawar's turtles.",
    ex='Preen (1989, 2004); Hodgson (2009); Marshall et al. (2018)',
    disc=['Herd of 674 dugongs counted in 1986', '508 animals in under 1 km² in 2015–2016'],
    refs=['Preen, A. (2004). Distribution, abundance and conservation status of dugongs and dolphins in the southern and western Arabian Gulf. Biological Conservation 118, 205–218.', 'Marshall, C. D. et al. (2018). Large dugong aggregations persist in coastal Qatar. Marine Mammal Science 34(4), 1154–1163.', 'IUCN Marine Mammal Protected Areas Task Force. Gulf of Salwa IMMA factsheet.'])

add(id='tree-of-life', n='Tree of Life', na='شجرة الحياة', c='ecology', s='Lone mesquite in the southern desert', lat=25.9941, lng=50.5832,
    p='Living today', dr='Planted c. 1582', el='9.75 m tall · 6 km from Jebel Dukhan', ic='plant', era='N', t0=444, t1=0,
    te='The tree with no spring', ta='الشجرة بلا عين', se='A 400-year-old tree alive in bare desert, its water still unexplained', sa='شجرة عمرها 400 عام حيّة في صحراء جرداء، وماؤها ما زال لغزًا',
    desc="A Prosopis (mesquite) tree 9.75 m tall standing alone on a low hill about 6 km from Jebel Dukhan and 40 km from Manama. A 1990s soil and tree-ring study dated its planting to 1582. Its roots may reach 50 m down to groundwater, though no spring is visible; other explanations invoke moisture held in the sand. Archaeologists in October 2010 unearthed 500-year-old pottery and other artefacts beside it, and about 65,000 people visit each year.",
    sig="A living test of the island's hidden water, and the most visited natural site in Bahrain.",
    ex='Bahrain Authority for Culture and Antiquities (2010 excavation)',
    disc=['Planting dated to 1582 by tree-ring and soil analysis', '500-year-old pottery found beside the tree in 2010'],
    refs=['Mancuso, S. (2020). The Incredible Journey of Plants. Other Press.', 'Toumi, H. (2009). Bahrain\'s Tree of Life ranks high on Seven Wonders list. Gulf News.'])

D = {'sites': S, 'stops': []}
json.dump(D, open('/tmp/w/gulf/bh/data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
