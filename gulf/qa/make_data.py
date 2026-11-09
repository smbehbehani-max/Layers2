# Layers of Qatar — researcher catalogue v0.1
import json
S = []
def add(**k): S.append(k)

add(id='al-zubarah', n='Al Zubarah', na='الزبارة', c='archaeological', s='18th-century pearling town · World Heritage', lat=25.978, lng=51.030,
    p='Late Islamic', dr='1760s – early 20th century', el='60 ha · 2.5 km town wall', ic='wall', era='H', t0=266, t1=100,
    te='The town that pearls built', ta='المدينة التي بناها اللؤلؤ', se='A walled trading town of 6,000 to 9,000 people, burned in 1811 and buried by sand', sa='مدينة تجارية مسوّرة سكنها 6 إلى 9 آلاف إنسان، أُحرقت عام 1811 ودفنتها الرمال',
    desc="A pearling and trading town founded in the 1760s on the north-west coast, 85 km from Doha. The late 18th-century town wall forms a 2.5 km arc from shore to shore around a 60 ha site that may have held 6,000–9,000 people; a palatial compound of 110 × 100 m has nine courtyards. Forces loyal to the Sultan of Muscat burned the town in 1811, a later town covered about 20% of the area, and the site was abandoned by the early 20th century. Qal'at Murair, a fortified settlement inland, stayed occupied until Al Zubarah Fort was built in 1938. Inscribed on the World Heritage List on 22 June 2013, Qatar's first.",
    sig="The best-preserved example of an 18th–19th-century Gulf merchant town, with its street plan, souq, houses and fishing harbours intact under the sand.",
    ex='Qatar Museums with the University of Copenhagen (Qatar Islamic Archaeology and Heritage Project), 2009 onwards; Qatari excavations of the souq in the 1980s',
    disc=['2.5 km town wall from shore to shore', 'Palatial compound with nine courtyards', 'Qal\'at Murair and the 1938 fort'],
    refs=['Qatar Museums (2022). Al Zubarah Archaeological Site: visitor guide.', 'UNESCO World Heritage Centre. Al Zubarah Archaeological Site (ref. 1402rev), inscribed 2013.'])

add(id='al-jassasiya', n='Al Jassasiya Rock Carvings', na='نقوش الجساسية الصخرية', c='archaeological', s='Largest rock-art site in Qatar', lat=26.020, lng=51.385,
    p='Islamic (dates debated)', dr='Possibly 11th century AD onwards', el='c. 900 carvings on 580 numbered rocks', ic='boat', era='H', t0=1000, t1=200,
    te='Boats cut into the rock', ta='قوارب محفورة في الصخر', se='Rows of cup marks and 141 boats carved into a coastal ridge', sa='صفوف من الحفر الفنجانية و141 قاربًا محفورة في ضلع ساحلي',
    desc="About 900 carvings across 580 numbered sites on a low ridge 4.8 km south of Fuwairit, discovered in 1961 by a Danish team under Holger Kapel and recorded by Hans Kapel in 1974. Cup-and-ring marks are the most common motif, with animals (ostriches, turtles, fish) and boats: 124 plan drawings and 17 elevation drawings, the only recorded boat carvings in Qatar. Dating is debated: Facey (1987) put the earliest boat drawings at the 11th century AD on the evidence of rudders, Nayeem (1998) suggested the 3rd century BC, and a 2012 dating study found its oldest sample under 300 years old. Nearby habitation mounds hold pottery of the 10th–11th centuries.",
    sig="The richest open-air rock-art site on the Gulf coast, and a rare record of the dhows of the pearling age.",
    ex='Danish Archaeological Expedition (H. Kapel) 1961; H. Kapel 1974; de Cardi 1973–74',
    disc=['141 boat carvings in plan and elevation', 'Cup-and-ring marks in rows and rosettes'],
    refs=['Facey, W. (1987). The boat carvings at Jabal Al-Jussasiyah, northeast Qatar. Proceedings of the Seminar for Arabian Studies 17, 199–222.', 'Hassiba, R. et al. (2012). Determining the age of Qatari Jabal Jassasiyah petroglyphs. QScience Connect 4.', 'Kapel, H. (1983). Rock carvings at Jabel Jusasiyah, Qatar. Qatar National Museum Journal.'])

add(id='al-khor-island', n='Al Khor Island (Purple Island)', na='جزيرة الخور (الجزيرة الأرجوانية)', c='archaeological', s='Kassite purple-dye workshop', lat=25.6928, lng=51.5489,
    p='Dilmun to Kassite', dr='c. 2000 – 1100 BC', el='1.67 km² · outcrop 8.5 m', ic='shell', era='P', t0=4025, t1=3125,
    te='Three million crushed shells', ta='ثلاثة ملايين صدفة مسحوقة', se='The oldest known purple-dye works, on an island of mangroves', sa='أقدم مصنع معروف للصبغة الأرجوانية، على جزيرة من القرم',
    desc="A 1.67 km² island in the bay of Al Khor, 50 km north of Doha, joined to the shore by a causeway at low water. Dilmun-period pottery (c. 2000–1750 BC) links it to Bahrain; in the Kassite period (c. 1400–1100 BC) it became a purple-dye works, with about 3,000,000 crushed murex shells (Hexaplex trunculus) and Kassite potsherds, claimed as the earliest known production of shellfish purple. Sasanian and late Islamic material shows later use. First studied systematically in 1976 by the French mission under Jacques Tixier, then by Carter and Killick. Avicennia mangroves line its east and south-east shores.",
    sig="The earliest industrial-scale purple-dye site known, tying Qatar to the Kassite kings of Babylon and Dilmun.",
    ex='Mission Archéologique Française à Qatar (J. Tixier) 1976; Carter & Killick (2014)',
    disc=['3,000,000 crushed murex shells', 'Kassite and Dilmun pottery'],
    refs=['Carter, R. & Killick, R. (2014). Al-Khor Island: investigating coastal exploitation in Bronze Age Qatar. Moonrise Press.', 'Magee, P. (2014). The Archaeology of Prehistoric Arabia. Cambridge University Press.'])

add(id='wadi-debayan', n='Wadi Debayan', na='وادي دبيان', c='archaeological', s='Oldest settlement in Qatar', lat=25.945, lng=51.045,
    p='Neolithic', dr='c. 7,500 – 4,500 years ago', el='North-west coast, approximate location', ic='well', era='P', t0=7500, t1=4500,
    te='The first campfires', ta='أولى نيران المخيم', se='People lived here 7,500 years ago, until something sudden ended it', sa='عاش الناس هنا قبل 7,500 عام، حتى أنهى ذلك حدث مفاجئ',
    desc="A Neolithic settlement on the north-west coast with occupation from about 7,500 years ago, excavated over three seasons to 2013 by the Qatar National Historic Environment Record project of the University of Birmingham and Qatar Museums (co-director Richard Cuttler). Flint scatters and pottery mark the earliest phase; settlement appears to have ended abruptly shortly after 4,500 years ago, possibly in a high-energy event such as a tsunami.",
    sig="Qatar's oldest known settlement, contemporary with the Ubaid-period villages of Kuwait and Saudi Arabia across the Gulf.",
    ex='QNHER project, University of Birmingham and Qatar Museums (R. Cuttler, P. Spencer), 2010–2013',
    disc=['Occupation from about 7,500 years ago', 'Abrupt end about 4,500 years ago'],
    refs=['Gulf Times (13 July 2013). Wadi Debayan offers detailed and rich story of human occupation.', 'Cuttler, R. et al. Qatar National Historic Environment Record project reports, University of Birmingham.'])

add(id='murwab', n='Murwab', na='مروب', c='archaeological', s='Abbasid village with the oldest fort', lat=25.8597, lng=51.0197,
    p='Early Islamic (Abbasid)', dr='c. 805 – 885 AD', el='250 houses · 2 mosques · 1 fort', ic='jar', era='H', t0=1220, t1=1140,
    te='A village of 250 houses', ta='قرية من 250 بيتًا', se='An Abbasid village that traded pearls for glazed pots from Basra and Samarra', sa='قرية عباسية قايضت اللؤلؤ بأوانٍ مزجّجة من البصرة وسامراء',
    desc="A 9th-century village 4 km from the west coast and 15 km north of Dukhan: 250 ruined houses, two mosques and a rectangular fort with a central courtyard and twelve rooms, the oldest known fort in Qatar. Of 6,948 potsherds, most date to 805–885 AD, with glazed wares from Susa, Basra or Samarra and no Chinese porcelain; at least 18% of the common pots had been repaired. Discovered by Geoffrey Bibby's Danish team in 1959, excavated by C. Hardy-Guilbert in 1984 and Alexandrine Guérin in 2009. Abandoned in the late 9th century as the Qarmatian revolt began.",
    sig="The clearest picture of early Islamic village life in Qatar, and evidence of pearl-for-pottery trade with Iraq.",
    ex='Danish expedition (G. Bibby) 1959; French missions 1984 and 2009',
    disc=['Oldest known fort in Qatar', '6,948 potsherds dated 805–885 AD'],
    refs=['Guérin, A. & Al-Naimi, F. (2010). Preliminary pottery study: Murwab horizon in progress, ninth century AD, Qatar. Proceedings of the Seminar for Arabian Studies 40.', 'Hardy-Guilbert, C. (1991). Dilmun and Qatar in the early Islamic period. In: The Heritage of Qatar.'])

add(id='barzan-towers', n='Barzan Towers', na='أبراج برزان', c='archaeological', s='Watchtowers of Umm Salal Mohammed', lat=25.4180, lng=51.4131,
    p='Modern', dr='Late 19th century; renovated 1910', el='16 m high', ic='wall', era='H', t0=140, t1=23,
    te='Towers that watched the moon', ta='أبراج راقبت القمر', se='Built to guard a rainwater valley, watch the sea and sight the Ramadan moon', sa='بُنيت لحراسة وادٍ لمياه الأمطار، ومراقبة البحر، ورؤية هلال رمضان',
    desc="Two watchtowers of coral rock and limestone with mud mortar, 16 m high with walls about 1 m thick at the base, on the low hill of Jebel Lusail at Umm Salal Mohammed, 15 km north of Doha and 10 km from the coast. Built in the late 19th century and renovated in 1910 by Sheikh Mohammed bin Jassim Al Thani, they guarded the rawda, a depression that collected rainwater, watched for Ottoman troops and approaching ships, and were used to sight the new moon of Ramadan. Restored in 2003 and now a museum.",
    sig="A rare surviving example of Qatar's pre-oil defensive architecture, tied to water rather than to a coast.",
    ex='Qatar Museums (restoration 2003)',
    disc=['Walls 1 m thick of coral rock and limestone', 'Rawda rainwater depression below the towers'],
    refs=['Hawker, R. (2008). Traditional Architecture of the Arabian Gulf. WIT Press.', 'Qatar Museums. Barzan Towers (qm.org.qa).'])

add(id='zekreet-mesas', n='Zekreet Peninsula and Mushroom Rocks', na='شبه جزيرة زكريت وصخور الفطر', c='geological', s='Eroded Eocene mesas', lat=25.520, lng=50.860,
    p='Eocene (Dammam Formation)', dr='Rocks c. 48 – 40 million years old', el='Abarug member: 2 m limestone over 10 m marl', ic='cliff', era='D', t0=48e6, t1=0,
    te='Tables and mushrooms of stone', ta='طاولات وفطر من حجر', se='Wind and salt carved mesas and mushroom rocks from a layered Eocene sea floor', sa='نحتت الرياح والملح موائد وصخور فطر من قاع بحر إيوسيني مطبّق',
    desc="A peninsula north of Dukhan on the west coast, defined by the half-moon Bay of Zekreet and lying inside the Al Reem Biosphere Reserve. Foothills, mesas and gypsum plateaux are carved from the Abarug member of the Eocene Dammam Formation: an upper 2 m of dull dolomitic limestone over 10 m of brightly coloured dolomitic marl, so that the resistant cap protects pillars and mushroom rocks as the soft marl erodes. Ostriches, gazelles and reintroduced oryx roam the Ras Abrouq headland, and flamingos feed in the bay. Richard Serra's East-West/West-East steel plates stand in a valley here. Tourism has caused litter and vegetation damage.",
    sig="Qatar's most striking natural landscape and a clear lesson in differential erosion of the Eocene sea floor.",
    ex='Qatar Natural History Group; UNESCO Doha (Al Reem studies)',
    disc=['Hard 2 m limestone cap over soft 10 m marl', 'Mesas, pillars and mushroom rocks'],
    refs=['Leblanc, J. (2008). A fossil hunting guide to the Tertiary formations of Qatar.', 'Richtzenhain, M. et al. (2008). Towards environmentally friendly tourism in Arabian biosphere reserves: case study Al Reem, Qatar. UNESCO Doha.'])

add(id='dukhan-field', n='Dukhan Anticline and Oil Field', na='طيّة دخان وحقل النفط', c='geological', s='Qatar’s first oil, 1940', lat=25.420, lng=50.780,
    p='Jurassic reservoirs under an Eocene fold', dr='Discovered January 1940', el='Anticline 80 km long · well 1,733 m deep', ic='oil', era='N', t0=88, t1=0,
    te='The hill of smoke', ta='تل الدخان', se='An 80 km fold at the surface led drillers to Jurassic oil 1,733 m down', sa='طيّة بطول 80 كم على السطح قادت الحفّارين إلى نفط جوراسي على عمق 1,733 م',
    desc="A north–south anticline about 80 km long and up to 8 km wide on the west coast, whose Middle Eocene limestone limbs dip 2–10° with about 90 m of surface closure; the hazy hills were called Jabal Dukhan, the hill of smoke. Dukhan No. 1 was spudded in October 1938 and completed in January 1940 at 1,733 m, flowing about 4,480 barrels a day from Upper Jurassic limestone (the Zekrit Formation, equivalent to the Arab Formation) rather than the expected Cretaceous. The first cargo, 80,000 tons, left Umm Said on 31 December 1949. Non-associated gas was found in the Permian Khuff Formation at about 3,000 m in 1959–60, with production from 1978.",
    sig="The structure that made modern Qatar, and a textbook case of surface geology pointing to deep oil.",
    ex='Petroleum Development (Qatar) Ltd, 1938–1940; QatarEnergy',
    disc=['Discovery well completed January 1940 at 1,733 m', 'Khuff gas at 3,000 m, 1959–60'],
    refs=['Sorkhabi, R. (2010). The Qatar oil discoveries. GEO ExPro.'])

add(id='qatar-arch', n='The Qatar Arch', na='قوس قطر', c='geological', s='The fold that lifted the peninsula', lat=24.930, lng=51.040,
    p='Eocene to Pleistocene', dr='Rocks 56 million years old to recent', el='Highest point 103 m (south-west)', ic='fault', era='D', t0=56e6, t1=0,
    te='Why Qatar is above the sea', ta='لماذا قطر فوق البحر', se='A long, gentle arch of the Arabian plate holds the whole peninsula out of the water', sa='قوس طويل لطيف في الصفيحة العربية يرفع شبه الجزيرة كلها فوق الماء',
    desc="Qatar sits on the eastern stable shelf of the Arabian Plate, lifted by the Qatar–South Fars Arch, a regional NNE–SSW anticline bounded to the north by the Zagros belt. The surface is mostly Lower Eocene to Pleistocene limestone and dolostone with marl, shale, clay and gypsum, plus Upper Miocene–Pliocene gravels and conglomerates; the highest point is 103 m in the south-west, and aeolian dunes cover about 12% of the country. The same arch carries the Dukhan field and the offshore North Field.",
    sig="The single structure that explains Qatar's existence, its flatness, its caves and its hydrocarbons.",
    ex='Al-Awah & Matter (2023); Qatar geological surveys',
    disc=['Peninsula lifted on a NNE–SSW arch', 'Dunes on 12% of the land'],
    refs=['Al-Awah, H. & Matter, W. S. (2023). Physicochemical characterization and origin of aeolian sand dunes in southeastern Qatar. Advances in Geosciences 63, 1–13.'])

add(id='dahl-al-misfir', n='Dahl Al Misfir Cave', na='دحل المسفر', c='geological', s='Gypsum cave that glows', lat=25.250, lng=51.210,
    p='Quaternary karst in Eocene rock', dr='Limestone 40 – 50 million years old; cave younger', el='40 m deep · entrance 12 × 4.5 m', ic='sinkhole', era='D', t0=2.58e6, t1=0,
    te='The cave that glows', ta='الكهف الذي يتوهج', se='Fibrous gypsum crystals light a 40 m sinkhole in the central desert', sa='بلورات جبس ليفية تضيء دحلًا بعمق 40 م في الصحراء الوسطى',
    desc="A sinkhole cave about 40 km south-west of Doha near Rawdat Rashid, 40 m deep (at least 100 m by one account) with an entrance of about 12 × 4.5 m. Its fibrous gypsum crystals, derived from the Lower Dammam and Rus Formations, give the interior a faint phosphorescent glow; the surrounding Eocene limestone is 40–50 million years old and the cave formed later by dissolution, part of the Middle Pleistocene karst of Qatar. Fenced, free to enter and rehabilitated in 2022 with paths and a cave map.",
    sig="The deepest accessible dahl in Qatar and the best place to see the gypsum that underlies the peninsula.",
    ex='Ministry of Environment and Climate Change (rehabilitation 2022)',
    disc=['Fibrous gypsum with a phosphorescent glow', 'Middle Pleistocene karst formation'],
    refs=['Sadiq, A. M. & Nasir, S. J. (2002). Middle Pleistocene karst evolution in the State of Qatar, Arabian Gulf. Journal of Cave and Karst Studies 64(2), 132–139.'])

add(id='mesaieed-dunes', n='Mesaieed Dunes and Khor Al Adaid Sands', na='كثبان مسيعيد ورمال خور العديد', c='geological', s='Mobile dunes marching to the sea', lat=24.900, lng=51.400,
    p='Holocene', dr='Active today; sand supply nearly exhausted', el='Barchans and parabolic dunes', ic='dune', era='D', t0=11700, t1=0,
    te='Dunes on their last journey', ta='كثبان في رحلتها الأخيرة', se='Wind drives the sand south-east into the Inland Sea, and no new sand arrives', sa='تدفع الريح الرمال جنوبًا شرقًا إلى البحر الداخلي، ولا تصل رمال جديدة',
    desc="Mobile barchan and parabolic dunes south of Mesaieed, driven by the north-north-westerly shamal toward the Inland Sea and eastern Saudi Arabia. Vegetation cover is 0–1%, far below the 8% that normally checks wind erosion, and the sand supply is described as limited to exhausted: at current rates the dunes could be gone in roughly 500–1,500 years. Dunes cover about 12% of Qatar and are best developed here in the south.",
    sig="A dune field with an expiry date, and the sand that gives Khor Al Adaid its spectacle.",
    ex='UNESCO Doha (B. Boer); Al-Awah & Matter (2023)',
    disc=['Vegetation cover 0–1%', 'Sand supply limited to exhausted'],
    refs=['James, B. (2011). Dunes: shifting sands of time. Gulf Times, 13 March 2011.', 'Al-Awah, H. & Matter, W. S. (2023). Physicochemical characterization and origin of aeolian sand dunes in southeastern Qatar. Advances in Geosciences 63.'])

add(id='khor-al-adaid', n='Khor Al Adaid (Inland Sea)', na='خور العديد', c='ecology', s='Tidal inland sea · UNESCO tentative list', lat=24.714, lng=51.415,
    p='Living today', dr='On the Tentative List since 2008', el='Lagoon 15 km × 12 km · channel 10 km', ic='delta', era='N', t0=30, t1=0,
    te='Where the desert meets the sea', ta='حيث تلتقي الصحراء بالبحر', se='A tidal lagoon with no equal, ringed by dunes that spill into the water', sa='بحيرة مدّية لا نظير لها، تحيط بها كثبان تنهال في الماء',
    desc="A tidal embayment in the south-east about 15 km north–south and up to 12 km east–west, linked to the Gulf by a channel of about 10 km, submitted to UNESCO's Tentative List on 18 March 2008 under natural criteria (vii) and (viii). Barchan and parabolic dunes reach and spill into the sea; inland and coastal sabkhas prograde seaward under the shamal, salt hummocks record Holocene sea-level change, and dolomite precipitates beneath the surface. Dugongs, turtles, corals and seagrass live in the lagoon, ospreys nest on islets, migrant waterfowl winter here, and Arabian gazelles use the shore.",
    sig="The only lagoon system of its kind, where active dunes, sabkhas and a tidal sea meet in one protected landscape.",
    ex='Ministry of Environment and Climate Change; UNESCO Tentative List ref. 5317',
    disc=['Dunes spilling directly into tidal water', 'Dolomite forming today beneath the sabkha'],
    refs=['UNESCO World Heritage Centre. Khor Al-Adaid natural reserve, Tentative List ref. 5317 (2008).'])

add(id='al-reem-reserve', n='Al Reem Biosphere Reserve', na='محمية الريم', c='ecology', s='UNESCO biosphere reserve', lat=25.75, lng=51.00,
    p='Living today', dr='Established 2005; UNESCO 2007', el='120,000 ha, about 10% of Qatar', ic='gazelle', era='N', t0=21, t1=0,
    te='A tenth of the country, kept wild', ta='عُشر البلاد، حُفظ بريًا', se='Oryx and gazelle on the limestone plains of the north-west', sa='المها والغزال على سهول الشمال الغربي الجيرية',
    desc="A semi-arid reserve of 120,000 ha in the north-west, about 65 km from Doha, established in 2005 and recognised by UNESCO's Man and the Biosphere programme in 2007. It is an inhabited landscape of limestone plains, mesas and coast, including the Zekreet peninsula and Ras Abrouq, with Arabian oryx and gazelles among its wildlife and vegetation valued by local communities.",
    sig="One of 24 UNESCO biosphere reserves in the Middle East and the frame for Qatar's wildlife reintroductions.",
    ex='Ministry of Environment and Climate Change; UNESCO MAB',
    disc=['120,000 ha, 10% of the land area', 'Arabian oryx and gazelle'],
    refs=['UNESCO MAB Biosphere Reserves Directory. Al-Reem (Qatar).', 'Sillitoe, P., Alshawi, A. A. & Al-Amir Hassan, A. K. (2010). Challenges to conservation: land use change and local participation in the Al Reem Biosphere Reserve, west Qatar. Journal of Ethnobiology and Ethnomedicine 6, 28.'])

add(id='al-shaheen-whale-sharks', n='Al Shaheen Whale Shark Aggregation', na='تجمّع قرش الحوت في الشاهين', c='ecology', s='One of the largest whale shark gatherings', lat=26.600, lng=51.900,
    p='Living today', dr='Surveyed 2011 onwards; May – August peak', el='90 km offshore · 60 m water', ic='dolphin', era='N', t0=20, t1=0,
    te='A hundred giants in one square kilometre', ta='مئة عملاق في كيلومتر مربع واحد', se='Whale sharks gather around oil platforms to feed on tuna eggs', sa='تتجمع أقراش الحوت حول منصات النفط لتأكل بيض التونة',
    desc="Around the Al Shaheen oil field about 90 km offshore in 60 m of water, whale sharks gather from April to September with a peak from May to August. In 2011 densities reached 100 sharks per km², about 100 were counted on 9 July, 178 in June, and groups of 40 were seen from the platforms; the sharks averaged 6.9 m long and most were male. They feed at the surface on fish eggs identified by DNA as mackerel tuna, which spawn around the platforms as if around fish-aggregating devices.",
    sig="One of the largest whale shark aggregations known anywhere, created by an unexpected link between oil platforms and spawning tuna.",
    ex='Qatar Ministry of Environment, Maersk Oil Research and Technology Centre (Robinson et al. 2013)',
    disc=['Up to 100 sharks per km²', 'Feeding on mackerel tuna eggs'],
    refs=['Robinson, D. P., Jaidah, M. Y., Jabado, R. W. et al. (2013). Whale sharks, Rhincodon typus, aggregate around offshore platforms in Qatari waters of the Arabian Gulf to feed on fish spawn. PLoS ONE 8(3), e58255.'])

add(id='fuwairit-turtles', n='Fuwairit Turtle Beach', na='شاطئ فويرط للسلاحف', c='ecology', s='Hawksbill nesting beach', lat=26.030, lng=51.370,
    p='Living today', dr='Protected nesting season March – July', el='Designated nesting site since 2020', ic='wave', era='N', t0=23, t1=0,
    te='Where the hawksbills come home', ta='حيث تعود سلاحف منقار الصقر', se='219 turtles nested in 2025 and 8,213 hatchlings reached the sea', sa='عشّشت 219 سلحفاة عام 2025 ووصل 8,213 فرخًا إلى البحر',
    desc="The main hawksbill turtle nesting beach of Qatar, designated in 2020 and closed to the public each nesting season from the end of March to July. In 2025, 219 turtles nested on eight beaches (Fuwairit, Ras Rakan, Ras Laffan, Sharawa, Umm Tais, Al Ghariyah, Al Maroona and Al Khor), nests were relocated to Fuwairit and Ras Laffan, and 8,213 hatchlings were released; more than 60,000 hatchlings have been released in five years. The Hawksbill Turtle Conservation Project has run since 2003 with QatarEnergy and Qatar University's Environmental Science Centre.",
    sig="The northern Gulf's most important hawksbill rookery, in one of the hottest nesting environments on Earth.",
    ex='Ministry of Environment and Climate Change, QatarEnergy, Qatar University ESC',
    disc=['219 nesting turtles in 2025', '8,213 hatchlings released in 2025'],
    refs=['Gulf Times (2025). 2025 nesting season for hawksbill turtles ends.', 'Chatting, M. et al. Nesting ecology of hawksbill turtles, Eretmochelys imbricata, in an extreme environmental setting. Qatar University / Bangor University.'])

add(id='al-thakhira-mangroves', n='Al Thakhira Mangrove Reserve', na='محمية قرم الذخيرة', c='ecology', s='Largest mangrove forest in Qatar', lat=25.730, lng=51.550,
    p='Living today', dr='Qatar’s mangroves total about 14 km²', el='Over 7 km² in the reserve', ic='mangrove', era='N', t0=30, t1=0,
    te='Half of Qatar’s mangroves', ta='نصف قرم قطر', se='A grey-green forest in the tide, storing carbon and sheltering fish', sa='غابة رمادية خضراء في المدّ، تخزّن الكربون وتؤوي الأسماك',
    desc="The largest mangrove habitat in Qatar, north of Al Khor on the east coast: more than 7 km² of the country's roughly 14 km² of mangroves lie inside the Al Thakhira Reserve, with other stands at Al Khor, Al Wakra, Mesaieed, Al Alia Island, Fuwairit, Al Ruwais, Al Arish and Al Jamil. The Ministry of Environment runs afforestation and restoration programmes based on studies of tide, soil and salinity, citing a global estimate of about 3,754 tonnes of CO₂ stored per hectare including soils.",
    sig="A nursery for fish and a carbon store on a coast that has lost most of its natural shoreline.",
    ex='Ministry of Environment and Climate Change',
    disc=['Over 7 km² of mangrove in one reserve', 'Restoration planting monitored for survival'],
    refs=['Qatar Tribune (26 July 2026). Qatar\'s mangrove forests span 14 sq km as ministry strengthens conservation drive.'])

add(id='qatar-dugongs', n='Dugongs of Western Qatar', na='أطوم غرب قطر', c='ecology', s='Record herds on the seagrass', lat=25.600, lng=50.750,
    p='Living today', dr='Surveys 2015 – 2016', el='Waters under 10 m deep', ic='dolphin', era='N', t0=12, t1=0,
    te='Five hundred in a square kilometre', ta='خمسمئة في كيلومتر مربع', se='The largest dugong herds outside Australia graze off the west coast', sa='أكبر قطعان الأطوم خارج أستراليا ترعى قبالة الساحل الغربي',
    desc="In the shallow seagrass waters off west and north-west Qatar, helicopter surveys in late 2015 and early 2016 counted 508 dugongs within an area under 1 km², with cow–calf pairs 9.9% of the group, and two foraging herds of 226 and 166 in December 2015. The waters between Qatar and Bahrain form an Important Marine Mammal Area of 10,676 km² holding the world's second-largest dugong population; winter surveys in 2004 had recorded groups of 577 and 97.",
    sig="The clearest evidence that the Gulf's dugong population persists at the size first recorded in the 1980s.",
    ex='Marshall et al. (2018); Preen (2004)',
    disc=['508 dugongs in under 1 km²', 'Herds of 226 and 166 in December 2015'],
    refs=['Marshall, C. D. et al. (2018). Large dugong aggregations persist in coastal Qatar. Marine Mammal Science 34(4), 1154–1163.', 'Preen, A. (2004). Distribution, abundance and conservation status of dugongs and dolphins in the southern and western Arabian Gulf. Biological Conservation 118, 205–218.'])

add(id='al-wajbah-fort', n='Al Wajbah Fort', na='قلعة الوجبة', c='archaeological', s='Fort of the 1893 battle', lat=25.3017, lng=51.3941,
    p='Modern', dr='Late 18th – 19th century', el='15 km west of Doha', ic='sword', era='H', t0=230, t1=133,
    te='The day the Ottomans turned back', ta='يوم تراجع العثمانيون', se='A small square fort where Sheikh Jassim’s men defeated an Ottoman force in 1893', sa='قلعة مربعة صغيرة هزم فيها رجال الشيخ جاسم قوة عثمانية عام 1893',
    desc="A fort in Al Wajbah, about 15 km west of Doha, thought to date from the late 18th or 19th century. In 1893, after Sheikh Jassim bin Mohammed Al Thani stopped paying taxes to the Ottomans, a contingent sent against him was defeated here and retreated to Doha, three hours away; the battle is remembered as the founding moment of modern Qatar. Restored to its original state in 1990 by the Museums and Archaeology Department, which removed later alterations.",
    sig="The site of the battle that secured Al Thani rule and the independence of the peninsula from Ottoman control.",
    ex='National Council for Culture, Arts and Heritage (restoration 1990)',
    disc=['Battle of Al Wajbah, 1893', 'Restored to original form in 1990'],
    refs=['Al-Kholaifi, M. J. (2006). Traditional Architecture in Qatar. pp. 39–41.', 'Qatar News Agency (18 November 2022). Al Wajbah Fort: a landmark in Qatar\'s history and present.'])

D = {'sites': S, 'stops': []}
json.dump(D, open('/tmp/w/gulf/qa/data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
