# Layers of Saudi Arabia — researcher catalogue v0.1
import json
S = []
def add(**k): S.append(k)

# ---------------- ARCHAEOLOGY ----------------
add(id='hegra', n='Hegra (Mada’in Salih)', na='الحِجر (مدائن صالح)', c='archaeological', s='Nabataean tomb city · World Heritage', lat=26.7917, lng=37.9542,
    p='Nabataean to Roman', dr='1st century BC – 2nd century AD', el='111 monumental tombs cut into sandstone', ic='wall', era='H', t0=2100, t1=1850,
    te='The southern city of the Nabataeans', ta='مدينة الأنباط الجنوبية', se='111 tombs carved into sandstone outcrops, with dated inscriptions from 1 BC to AD 74', sa='111 مقبرة منحوتة في نتوءات الحجر الرملي، بنقوش مؤرخة من 1 ق.م إلى 74 م',
    desc="The largest Nabataean site south of Petra: 111 monumental tombs cut into sandstone outcrops around a now-vanished city, 94 of them decorated, with dated inscriptions running from 1 BC to AD 74. Qasr al-Bint, the largest, is about 16 m high. Water came from wells and cisterns in the plain. Rome annexed the Nabataean kingdom in AD 106 and a Roman garrison is attested at Hegra. Inscribed in 2008 as Saudi Arabia's first World Heritage site; excavated by the Saudi-French Madâ'in Sâlih Archaeological Project since 2008.",
    sig="The best-preserved Nabataean tombs anywhere, and the only ones with a run of dated inscriptions.",
    ex='Saudi-French Madâ’in Sâlih Archaeological Project (L. Nehmé) 2008 onwards; Royal Commission for AlUla',
    disc=['Tombs dated by inscription from 1 BC to AD 74', 'Roman garrison after AD 106'],
    refs=['UNESCO World Heritage Centre. Hegra Archaeological Site (al-Hijr / Madā ͐ in Ṣāliḥ) (ref. 1293), inscribed 2008.', 'Nehmé, L. (ed.) (2015). Les tombeaux nabatéens de Hégra. Académie des Inscriptions et Belles-Lettres.'])

add(id='mustatils', n='Mustatils of the Nafud', na='مستطيلات النفود', c='archaeological', s='Neolithic stone monuments · AlUla–Khaybar', lat=25.70, lng=39.30,
    p='Neolithic', dr='c. 5300 – 5000 BC', el='Over 1,000 rectangles, 20 – 620 m long', ic='platform', era='P', t0=7300, t1=7000,
    te='A thousand rectangles in the desert', ta='ألف مستطيل في الصحراء', se='Stone enclosures up to 620 m long, built 7,000 years ago and holding cattle horns as offerings', sa='حظائر حجرية يصل طولها إلى 620 م، بُنيت قبل 7,000 عام وتضم قرون ماشية كقرابين',
    desc="Long rectangular stone structures, 20 to 620 m in length, found by the thousand across north-west Arabia from the Nafud to the lava fields of Khaybar: more than 1,000 are recorded over about 200,000 km². Excavation of a mustatil near AlUla found a chamber with cattle, sheep and gazelle horns placed as offerings around a standing stone, radiocarbon-dated to about 5300–5000 BC, making them among the oldest large-scale monuments in the world. Their builders were cattle herders of a wetter Arabia.",
    sig="Older than the pyramids and Stonehenge, and until 2021 almost unknown outside Arabia.",
    ex='Aerial Archaeology in the Kingdom of Saudi Arabia (University of Western Australia) and Royal Commission for AlUla, 2018 onwards',
    disc=['Cattle horns deposited around a standing stone', 'Radiocarbon dates of c. 5300–5000 BC'],
    refs=['Thomas, H., Kennedy, M. A., Dalton, M. et al. (2021). The mustatils: cult and monumentality in Neolithic north-western Arabia. Antiquity 95(381), 605–626.', 'Kennedy, M. A. et al. (2023). Cult, herding and pilgrimage in the Late Neolithic of north-west Arabia. PLOS ONE 18(3).'])

add(id='at-turaif', n='At-Turaif District, Diriyah', na='حي الطريف، الدرعية', c='archaeological', s='Najdi mud-brick capital · World Heritage', lat=24.7340, lng=46.5730,
    p='Islamic (First Saudi State)', dr='15th century – 1818', el='Salwa Palace and mud-brick city on Wadi Hanifah', ic='wall', era='H', t0=575, t1=208,
    te='A capital made of earth', ta='عاصمة من تراب', se='The mud-brick heart of the First Saudi State, on a bend of Wadi Hanifah', sa='قلب الدولة السعودية الأولى من الطوب الطيني، على منعطف وادي حنيفة',
    desc="A walled district of mud brick on the edge of Wadi Hanifah, settled in the 15th century and from 1727 the capital of the First Saudi State until an Ottoman-Egyptian siege took it in 1818. Salwa Palace, the Imam Mohammed bin Saud Mosque and houses of the Najdi style, with thick adobe walls, triangular openings and tamarisk roofs, survive. Inscribed in 2010 under criteria (iv), (v) and (vi) and restored as part of the Diriyah project.",
    sig="The finest surviving example of Najdi architecture and the birthplace of the Saudi state.",
    ex='Diriyah Gate Development Authority; Saudi Commission for Tourism and National Heritage',
    disc=['Najdi mud-brick style with triangular vents', 'Capital 1727–1818'],
    refs=['UNESCO World Heritage Centre. At-Turaif District in ad-Dir’iyah (ref. 1329), inscribed 2010.', 'Diriyah Gate Development Authority. At-Turaif UNESCO World Heritage Site.'])

add(id='al-ahsa-oasis', n='Al-Ahsa Oasis', na='واحة الأحساء', c='archaeological', s='Largest oasis in the world · World Heritage', lat=25.4294, lng=49.6219,
    p='Neolithic to present', dr='c. 5000 BC – today', el='2.5 million date palms on 85 km²', ic='well', era='H', t0=7000, t1=0,
    te='Two and a half million palms', ta='مليونان ونصف من النخيل', se='Springs feed the largest oasis on Earth, farmed without a break since the Neolithic', sa='عيون تغذي أكبر واحة على الأرض، زُرعت دون انقطاع منذ العصر الحجري الحديث',
    desc="An oasis of about 85.4 km² in the Eastern Province with some 2.5 million date palms watered by more than 280 artesian springs from the Neogene aquifer. Twelve components, including gardens, canals, springs, Jawatha mosque and Qasr Ibrahim, record settlement from the Neolithic to the present. Inscribed in 2018 under criteria (iii), (iv) and (v) as the world's largest oasis.",
    sig="A cultural landscape that shows how people have farmed one spring-fed place for seven thousand years.",
    ex='Saudi Commission for Tourism and National Heritage; Al-Ahsa Municipality',
    disc=['More than 280 springs', 'Continuous farming since the Neolithic'],
    refs=['UNESCO World Heritage Centre. Al-Ahsa Oasis, an Evolving Cultural Landscape (ref. 1563), inscribed 2018.', 'Saudipedia. Al-Ahsa Oasis.'])

add(id='hail-rock-art', n='Rock Art of Jubbah and Shuwaymis', na='فنون صخرية في جبة والشويمس', c='archaeological', s='Ten thousand years of carvings · World Heritage', lat=28.0106, lng=40.9131,
    p='Neolithic to Islamic', dr='c. 8000 BC – 1st millennium AD', el='Petroglyphs above a vanished lake 20 km long', ic='eye', era='P', t0=10000, t1=1500,
    te='Pictures beside a lake that dried', ta='صور بجوار بحيرة جفّت', se='Life-size humans, cattle and lions carved over 10,000 years on cliffs that once overlooked a lake', sa='بشر وماشية وأسود بحجمها الطبيعي نُقشت على مدى 10,000 عام على جروف أطلّت يومًا على بحيرة',
    desc="Two clusters of petroglyphs in Ha'il: Jabal Umm Sinman at Jubbah, above the bed of a Holocene lake about 20 by 5 km, and Jabal al-Manjor and Raat at Shuwaymis. The oldest carvings, of life-size people and wild animals, date back about 10,000 years; later panels show cattle herding, horses, camels and Thamudic inscriptions. Inscribed in 2015 under criteria (i) and (iii).",
    sig="One of the largest and longest sequences of rock art in the world.",
    ex='Saudi Commission for Tourism and National Heritage; Palaeodeserts Project (Max Planck Institute)',
    disc=['Palaeolake 20 × 5 km at Jubbah', 'Carvings spanning 10,000 years'],
    refs=['UNESCO World Heritage Centre. Rock Art in the Hail Region of Saudi Arabia (ref. 1472), inscribed 2015.', 'Guagnin, M. et al. (2017). Rock art provides new evidence on the biogeography of kudu, wild dromedary, aurochs and African wild ass in the early and middle Holocene of north-western Arabia. Journal of Biogeography 44, 2071–2081.'])

add(id='al-faw', n='Qaryat al-Faw', na='قرية الفاو', c='archaeological', s='Capital of Kinda · World Heritage', lat=19.7649, lng=45.1634,
    p='Pre-Islamic', dr='4th century BC – c. AD 300', el='Walled town, market, temples and 17 wells', ic='caravan', era='H', t0=2350, t1=1700,
    te='The city at the edge of the Empty Quarter', ta='المدينة على حافة الربع الخالي', se='A caravan capital with wall paintings, a market and temples, found under the sand at Wadi al-Dawasir', sa='عاصمة قوافل بجدارياتها وسوقها ومعابدها، وُجدت تحت الرمل في وادي الدواسر',
    desc="The capital of the kingdom of Kinda on the caravan route between Yemen and the Gulf, at a gap in the Tuwaiq escarpment facing the Rub' al Khali. Excavated by King Saud University from 1972, it has a walled market, houses with wall paintings, five temples, tombs and 17 wells, with South Arabian inscriptions and bronzes. Inscribed on 27 July 2024 as the Cultural Landscape of Al-Faw Archaeological Area.",
    sig="The most complete pre-Islamic town in central Arabia and its first painted interiors.",
    ex='King Saud University (A. R. al-Ansary) 1972 onwards; Heritage Commission and Saudi-French mission',
    disc=['Wall paintings of a feasting man', '17 wells for a desert town'],
    refs=['UNESCO World Heritage Centre. Cultural Landscape of Al-Faw Archaeological Area (ref. 1712), inscribed 2024.', 'al-Ansary, A. R. (1982). Qaryat al-Fau: a portrait of pre-Islamic civilisation in Saudi Arabia. University of Riyadh.'])

add(id='hima', n='Ḥimā Cultural Area', na='منطقة حمى الثقافية', c='archaeological', s='Rock art and ancient wells · World Heritage', lat=18.2505, lng=44.4515,
    p='Neolithic to Islamic', dr='c. 5000 BC – today', el='Bir Hima wells in use for 3,000 years', ic='well', era='P', t0=7000, t1=0,
    te='Seven thousand years of travellers', ta='سبعة آلاف عام من المسافرين', se='Rock art and inscriptions in many scripts beside wells that caravans still use', sa='فنون صخرية ونقوش بخطوط عدة بجوار آبار ما زالت القوافل تستخدمها',
    desc="A mountainous area north of Najran on one of Arabia's oldest caravan routes, with 34 rock-art sites carved over some 7,000 years: hunting, animals, plants and people, and inscriptions in Musnad, Thamudic, Greek and early Arabic. The Bir Hima wells have supplied travellers for about 3,000 years and still flow. Inscribed in 2021 under criterion (iii).",
    sig="A roadside archive of every script that passed through southern Arabia.",
    ex='Saudi Heritage Commission; Saudi-French Najran mission',
    disc=['Inscriptions in several scripts', 'Wells in continuous use'],
    refs=['UNESCO World Heritage Centre. Ḥimā Cultural Area (ref. 1619), inscribed 2021.', 'Heritage Commission, Saudi Arabia. Hima Cultural Area nomination file.'])

add(id='tarout-island', n='Tarout Island', na='جزيرة تاروت', c='archaeological', s='Dilmun-era island of Qatif', lat=26.571, lng=50.056,
    p='Ubaid to Islamic', dr='c. 5000 BC – today', el='Castle mound on 7,000 years of layers', ic='island', era='P', t0=7000, t1=0,
    te='Seven thousand years under one castle', ta='سبعة آلاف عام تحت قلعة واحدة', se='An island off Qatif settled since about 5000 BC, with a Dilmun past and a Portuguese fort', sa='جزيرة قبالة القطيف سُكنت منذ نحو 5000 ق.م، بماضٍ دلموني وحصن برتغالي',
    desc="An island about 6 km off Qatif, joined to it by causeways, inhabited since about 5000 BC. Pottery of c. 4500 and 3000 BC was excavated by a Danish team in 1968, tombs date to c. 2000 BC and a 94 cm stone statue of a man, probably Sumerian in style, is in the National Museum in Riyadh. The island was a centre of the Dilmun world; Tarout Castle stands on the mound, with a Portuguese fort of 1515–1521 nearby.",
    sig="The oldest continuously inhabited place on the Saudi Gulf coast.",
    ex='Danish expedition (G. Bibby) 1968; Saudi Department of Antiquities',
    disc=['Stone statue in Sumerian style', 'Ubaid pottery of c. 4500 BC'],
    refs=['Wikipedia contributors (2026). Tarout Island, citing Bibby, G. (1969) Looking for Dilmun.', 'Saudipedia. Tarout Island.'])

add(id='thaj', n='Thaj', na='ثاج', c='archaeological', s='Hellenistic walled city, possibly Gerrha', lat=26.868, lng=48.715,
    p='Hellenistic', dr='c. 300 BC – AD 300', el='Stone city wall and a gold funerary mask', ic='sword', era='H', t0=2300, t1=1700,
    te='The girl with the golden mask', ta='الفتاة ذات القناع الذهبي', se='A walled Hellenistic city 90 km inland from Jubail, where a child was buried with a mask of gold', sa='مدينة هلنستية مسوّرة على بُعد 90 كم من الجبيل، دُفنت فيها طفلة بقناع من الذهب',
    desc="A Hellenistic city about 90 km west of Jubail enclosed by a stone wall, settled from about 300 BC to AD 300 and possibly earlier; many scholars think it the site of Gerrha, the rich trading city Strabo described. A Danish mission (1968), a Saudi-British team (1983) and Saudi excavations from 2000 found houses, coins and, in a tomb, a young girl buried with a gold funerary mask, gloves and jewellery, now in the National Museum.",
    sig="The richest burial of pre-Islamic eastern Arabia and the best candidate for lost Gerrha.",
    ex='Danish expedition 1968; Saudi-UK 1983; Saudi Department of Antiquities 2000–2006; Saudi-French Thaj mission 2016 onwards',
    disc=['Gold funerary mask of a child', 'City wall of dressed stone'],
    refs=['Wikipedia contributors (2026). Thaj, citing Potts, D. T. (1990) The Arabian Gulf in Antiquity.', 'Asharq Al-Awsat (1 March 2017). Thaj: land of gold treasures in Saudi Arabia.'])

add(id='jubail-church', n='Jubail Church', na='كنيسة الجبيل', c='archaeological', s='Church of the East, 4th–7th century', lat=27.03, lng=49.60,
    p='Late pre-Islamic / early Islamic', dr='4th – 7th century AD', el='Nave, sanctuary and two carved crosses', ic='platform', era='H', t0=1650, t1=1350,
    te='A church found at a picnic', ta='كنيسة وُجدت في نزهة', se='Picnickers found a buried church in 1986; its carved crosses still mark the doorway', sa='عثر متنزهون على كنيسة مدفونة عام 1986؛ وما زالت صلبانها المنحوتة تعلّم المدخل',
    desc="A church of the Church of the East near Jubail, found by picnickers in 1986 and excavated by the Saudi Department of Antiquities in 1987. Two crosses are carved either side of the doorway between nave and sanctuary. Its date is debated between the 4th and 7th centuries; it belongs to the chain of Christian communities along the Gulf known from Sir Bani Yas, Kharg and Failaka. The site is fenced and the excavation unpublished.",
    sig="Evidence of the Christian communities of the Gulf coast before Islam.",
    ex='Saudi Department of Antiquities 1987',
    disc=['Two carved crosses in situ', 'Found by chance in 1986'],
    refs=['Wikipedia contributors (2026). Jubail Church.', 'Langfeldt, J. A. (1994). Recently discovered early Christian monuments in northeastern Arabia. Arabian Archaeology and Epigraphy 5, 32–60.'])

add(id='dadan-jabal-ikmah', n='Dadan and Jabal Ikmah', na='دادان وجبل عكمة', c='archaeological', s='Lihyanite capital and open-air library', lat=26.65, lng=37.93,
    p='Dadanite – Lihyanite', dr='c. 800 – 100 BC', el='450 inscriptions on one canyon', ic='eye', era='H', t0=2800, t1=2100,
    te='A library carved in a canyon', ta='مكتبة منقوشة في وادٍ', se='The capital of Dadan and Lihyan, and a canyon with 450 inscriptions in old Arabian scripts', sa='عاصمة دادان ولحيان، ووادٍ فيه 450 نقشًا بالخطوط العربية القديمة',
    desc="Dadan, in the AlUla valley, was the capital of the Dadanite and then Lihyanite kingdoms of the 1st millennium BC: a town below a cliff of tombs, some guarded by carved lions, and a sanctuary with statues of kings. Nearby Jabal Ikmah holds about 450 inscriptions in Dadanitic, an ancient North Arabian script, most from the second half of the 1st millennium BC, recording rituals, taxes and names. Jabal Ikmah joined UNESCO's Memory of the World Register in May 2023.",
    sig="The largest concentration of Dadanitic texts, a step on the road to Arabic.",
    ex='King Saud University 2004 onwards; Royal Commission for AlUla with French CNRS mission',
    disc=['Lion tombs of Dadan', '450 inscriptions on Jabal Ikmah'],
    refs=['Arab News (24 May 2023). AlUla’s Jabal Ikmah listed on UNESCO’s Memory of the World Register.', 'Royal Commission for AlUla. Dadan and Jabal Ikmah heritage sites.'])

add(id='historic-jeddah', n='Historic Jeddah (Al-Balad)', na='جدة التاريخية (البلد)', c='archaeological', s='Coral-stone port · World Heritage', lat=21.4858, lng=39.1875,
    p='Islamic', dr='7th century – today', el='Tower houses of coral stone with wooden rawashin', ic='boat', era='H', t0=1380, t1=0,
    te='A city built from the reef', ta='مدينة بُنيت من الشعاب', se='The port of Makkah since the 7th century, its tall houses built of coral stone and screened in wood', sa='ميناء مكة منذ القرن السابع، بيوته العالية من حجر المرجان ومزيّنة بالرواشين',
    desc="The old walled town of Jeddah, made the port of Makkah by Caliph Uthman in the 7th century, grew rich on pilgrim and Indian Ocean trade. Its tower houses are built of coral stone quarried from the Red Sea reef and faced with large wooden rawashin, with mosques, ribats and suqs between them. About a third of the original walled city is inscribed (2014, criteria ii, iv, vi); the Ministry of Culture began a large restoration in 2021.",
    sig="The last Red Sea merchant town still standing in coral stone.",
    ex='Ministry of Culture, Jeddah Historic District Program',
    disc=['Houses of reef coral', 'Port of Makkah since the 7th century'],
    refs=['UNESCO World Heritage Centre. Historic Jeddah, the Gate to Makkah (ref. 1361), inscribed 2014.', 'Jeddah Historic District Program. Explore Historic Jeddah.'])

add(id='umm-jirsan', n='Umm Jirsan Lava Tube', na='كهف أم جرسان', c='archaeological', s='Herders’ shelter in a lava tube', lat=25.586, lng=39.754,
    p='Neolithic to Bronze Age', dr='c. 8000 – 5000 BC and later', el='1.5 km of underground passage', ic='flame', era='P', t0=10000, t1=4000,
    te='People who lived in a lava tube', ta='أناس عاشوا في أنبوب بركاني', se='The first excavated lava tube in Arabia sheltered herders for thousands of years', sa='أول أنبوب بركاني يُنقَّب في الجزيرة العربية آوى الرعاة آلاف السنين',
    desc="A lava tube about 1.5 km long in the Harrat Khaybar lava field, the first in Arabia to be excavated. Stone tools, animal bones and charcoal show repeated use from about 10,000 to 7,000 years ago and into the Bronze Age by groups herding cattle, sheep and goats; rock art at the entrance shows herding and dogs, and human remains record diets that gained fruit and cereals when oasis farming arrived. Published in PLOS ONE in 2024.",
    sig="The first proof that people used Arabia's lava caves as shelters on the move.",
    ex='Max Planck Institute of Geoanthropology, Heritage Commission and Saudi Geological Survey (Stewart et al.)',
    disc=['Occupation from 10,000 years ago', 'Rock art of herders with dogs'],
    refs=['Stewart, M., Andrieux, E., Blinkhorn, J. et al. (2024). First evidence for human occupation of a lava tube in Arabia. PLOS ONE 19(4).', 'Max Planck Institute of Geoanthropology (2024). Archaeological insights from the first lava tube excavation in Arabia.'])

# ---------------- GEOLOGY ----------------
add(id='edge-of-the-world', n='Edge of the World (Jebel Fihrayn)', na='حافة العالم (جبل فهرين)', c='geological', s='Tuwaiq escarpment of Jurassic limestone', lat=24.95, lng=45.99,
    p='Middle Jurassic', dr='c. 165 million years ago', el='Cliffs about 300 m above an ancient sea bed', ic='cliff', era='D', t0=165000000, t1=160000000,
    te='A reef 800 km long', ta='شعاب بطول 800 كم', se='The Tuwaiq escarpment is Jurassic sea floor, lifted and cut into cliffs that run 800 km', sa='جرف طويق قاع بحر جوراسي، رُفع وقُطع إلى جروف تمتد 800 كم',
    desc="The Tuwaiq escarpment runs some 800 km through Najd from Qassim to Wadi al-Dawasir, a wall of Middle Jurassic Tuwaiq Mountain limestone up to 600 m high laid down in a shallow sea with coral bioherms. At Jebel Fihrayn, about 100 km north-west of Riyadh, the cliff stands 1,131 m above sea level and drops about 300 m to the plain, with the view that earned it the name Edge of the World. The same limestone holds Callovian corals and, at depth, the reservoirs of the Arab Formation.",
    sig="The spine of central Arabia and the outcrop of the rocks that hold its oil.",
    ex='Saudi Geological Survey; King Saud University geology',
    disc=['Jurassic corals in the limestone', 'Escarpment of 800 km'],
    refs=['Wikipedia contributors (2026). Tuwaiq, citing Powers, R. W. et al. (1966) Geology of the Arabian Peninsula: sedimentary geology of Saudi Arabia, USGS Professional Paper 560-D.', 'El-Sorogy, A. S. et al. (2016). Callovian colonial corals from the Tuwaiq Mountain Limestone of Saudi Arabia. Journal of African Earth Sciences.'])

add(id='harrat-rahat', n='Harrat Rahat and the 1256 Eruption', na='حرة رهط وثوران 1256', c='geological', s='Lava field that reached Madinah', lat=24.30, lng=39.78,
    p='Quaternary volcanism', dr='1256 AD (last eruption)', el='Lava flow 23 km long, 4 km short of the city', ic='flame', era='H', t0=770, t1=770,
    te='The night the lava came to Madinah', ta='ليلة وصلت الحمم إلى المدينة', se='In 1256 a fissure opened and lava flowed 23 km, stopping 4 km from Madinah', sa='في 1256 انشقّ الأرض وسالت الحمم 23 كم، وتوقفت على بُعد 4 كم من المدينة',
    desc="The largest lava field in Saudi Arabia, stretching about 300 km south of Madinah and rising to 1,744 m. In 1256 AD (654 AH) an eruption on its northern edge lasted 52 days, poured out about 0.5 km³ of basalt in a flow 23 km long that stopped 4 km from Madinah, and was recorded by the city's chroniclers; an earlier eruption is dated to AD 641. Earthquake swarms in 1999 and 2009 (at Harrat Lunayyir) show the fields are not extinct.",
    sig="The best-documented historic eruption in Arabia, written down by eyewitnesses.",
    ex='Saudi Geological Survey; Camp & Roobol (USGS) 1989',
    disc=['52-day eruption of 1256 AD', 'Flow stopped 4 km from the city'],
    refs=['Camp, V. E. & Roobol, M. J. (1989). The Arabian continental alkali basalt province: Part I. Evolution of Harrat Rahat, Kingdom of Saudi Arabia. GSA Bulletin 101, 71–95.', 'Saudi Geological Survey. Harrat Rahat volcanic field.'])

add(id='al-wahbah-crater', n='Al Wahbah Crater', na='فوهة الوعبة', c='geological', s='Maar crater of Harrat Kishb', lat=22.90, lng=41.14,
    p='Pleistocene', dr='c. 1.1 million years ago', el='2.2 km wide, 250 m deep, salt floor', ic='mudvolc', era='D', t0=1147000, t1=1147000,
    te='A bowl blown out by steam', ta='حفرة نسفها البخار', se='Rising magma met groundwater and blew a crater 2 km across; salt now floors it', sa='التقت الصهارة الصاعدة بالمياه الجوفية فنسفت فوهة بعرض 2 كم؛ يغطي قاعها الملح اليوم',
    desc="A maar about 2.2 km across and 250 m deep in the Harrat Kishb lava field between Taif and Madinah, formed when basaltic magma met groundwater and exploded through steam. Its floor is a white pan of sodium phosphate and salt crystals; its walls expose the layered tuff and the older lavas. Dated to about 1.15 million years. Once thought a meteorite crater, it is now a popular hike with a trail to the floor.",
    sig="The largest and clearest maar crater in Arabia.",
    ex='Saudi Geological Survey; King Abdulaziz University',
    disc=['Phreatomagmatic origin confirmed', 'Salt floor 250 m down'],
    refs=['Abdel Wahab, A., Abul-Maaty, M., Stuart, F. M. et al. (2014). Volcanic history of Al Wahbah maar, Saudi Arabia. Journal of African Earth Sciences 92, 1–13.', 'Saudi Geological Survey. Al Wahbah Crater.'])

add(id='wabar-craters', n='Wabar Craters', na='فوهات وبار', c='geological', s='Iron meteorite impact in the Rub’ al Khali', lat=21.5025, lng=50.4742,
    p='Recent', dr='Within the last few centuries', el='Three craters, the largest 116 m', ic='quake', era='H', t0=300, t1=150,
    te='The place of iron', ta='أرض الحديد', se='An iron meteorite of more than 3,500 tonnes struck the dunes and left glass and craters that Philby found in 1932', sa='نيزك حديدي يزيد على 3,500 طن ضرب الكثبان وخلّف زجاجًا وفوهات وجدها فيلبي عام 1932',
    desc="A group of impact craters, the largest about 116 m across, in the sands of the Rub' al Khali, reached by H. St John Philby on 2 February 1932 while searching for the lost city of Ubar; the Bedouin called it Al Hadida, the place of iron. An iron meteorite estimated at more than 3,500 tonnes exploded on impact, leaving black glass pellets, bleached impactite with coesite and iron fragments including the 2.2-tonne Camel's Hump now in Riyadh. Thermoluminescence dating puts the fall within the last 250 years or so; the dunes are burying the craters.",
    sig="One of the few impact sites on Earth preserved in sand, and among the youngest.",
    ex='Philby 1932; Zahid–USGS expeditions (J. C. Wynn, E. M. Shoemaker) 1994–95',
    disc=['Impact glass and coesite', 'Age under 250 years'],
    refs=['Wynn, J. C. & Shoemaker, E. M. (1998). The day the sands caught fire. Scientific American 279(5), 64–71.', 'Prescott, J. R., Robertson, G. B., Shoemaker, C., Shoemaker, E. M. & Wynn, J. (2004). Luminescence dating of the Wabar meteorite craters, Saudi Arabia. Journal of Geophysical Research 109.'])

add(id='dammam-no-7', n='Dammam Well No. 7 (Prosperity Well)', na='بئر الدمام رقم 7 (بئر الخير)', c='geological', s='Where Saudi oil was found, 1938', lat=26.3211, lng=50.1278,
    p='Jurassic reservoir (Arab Formation)', dr='3 March 1938', el='Oil struck at 1,440 m', ic='oil', era='N', t0=88, t1=44,
    te='The well that would not give up', ta='البئر التي لم تستسلم', se='After six dry wells, No. 7 found oil at 1,440 m in the Arab Formation and flowed for 44 years', sa='بعد ست آبار جافة، وجدت البئر رقم 7 النفط على عمق 1,440 م في تكوين العرب وتدفقت 44 عامًا',
    desc="On the Dammam Dome, the first six wells drilled by CASOC from 1935 found little. On 3 March 1938 well No. 7, deepened on the advice of geologist Max Steineke, struck oil at 1,440 m in the Jurassic Arab Formation and flowed at over 1,500 barrels a day. It produced about 32 million barrels until it was shut in 1982, and is preserved as a monument in Dhahran. The dome is a salt-cored anticline, the same structure that holds Bahrain's and Qatar's fields.",
    sig="The well that started the Saudi oil industry.",
    ex='Saudi Aramco; Saudi Geological Survey',
    disc=['Oil at 1,440 m in the Arab Formation', '32 million barrels over 44 years'],
    refs=['Saudi Aramco. Dammam No. 7: the Prosperity Well.', 'Wikipedia contributors (2026). Dammam No. 7, citing Aramco World and Steineke, M. (1938) report to CASOC.'])

add(id='shaybah-dunes', n='Shaybah Dunes', na='كثبان شيبة', c='geological', s='Dunes 300 m high over an oil field', lat=22.52, lng=53.96,
    p='Quaternary sands over Jurassic reservoir', dr='Last 1 million years (dunes); 1968 discovery', el='Linear dunes up to 333 m, sabkha floors', ic='dune', era='N', t0=58, t1=0,
    te='Sand a hundred storeys high', ta='رمال بارتفاع مئة طابق', se='Red dunes 300 m tall in the Empty Quarter, with an oil field found in 1968 beneath them', sa='كثبان حمراء بارتفاع 300 م في الربع الخالي، تحتها حقل نفط اكتُشف عام 1968',
    desc="In the north-east of the Rub' al Khali, about 800 km south of Dhahran, long red dunes rise up to 333 m above floors of sabkha; they belong to the largest continuous sand sea on Earth. Oil was found beneath them by the Shaybah-1 well in 1968, and the field, with about 14 billion barrels of proved reserves, was developed in 1995–98 and reached 1 million barrels a day in 2016. A 637 km² wildlife sanctuary around the plant holds more than 40 Arabian oryx and 70 sand gazelles.",
    sig="The tallest dunes of Arabia, and a working oil field in the emptiest place on Earth.",
    ex='Saudi Aramco; Saudi Geological Survey (Rub’ al Khali sands)',
    disc=['Dunes up to 333 m', 'Sanctuary of 637 km²'],
    refs=['Saudipedia. Shaybah Oil Field.', 'Saudi Aramco. Shaybah: an oasis in the Empty Quarter.'])

# ---------------- ECOLOGY ----------------
add(id='uruq-bani-maarid', n='‘Uruq Bani Ma’arid', na='عروق بني معارض', c='ecology', s='Oryx reserve on the Empty Quarter · World Heritage', lat=19.50, lng=45.90,
    p='Living desert', dr='Protected since 1994 · World Heritage 2023', el='12,750 km² of dunes and escarpment', ic='gazelle', era='N', t0=32, t1=0,
    te='Where the oryx came home', ta='حيث عاد المها', se='The Arabian oryx, extinct in the wild in 1972, was released here in 1995 and now breeds free', sa='المها العربي، الذي انقرض في البرية عام 1972، أُطلق هنا عام 1995 ويتكاثر حرًا اليوم',
    desc="A reserve of 12,750 km² on the western edge of the Rub' al Khali, where the Tuwaiq escarpment meets the sand sea. Protected in 1994, it received the first Arabian oryx released back into the wild in 1995 after the species had been lost from the wild in 1972; it also holds sand gazelle, mountain gazelle, Nubian ibex and about 120 plant species. Inscribed in September 2023 as Saudi Arabia's first natural World Heritage site under criteria (vii) and (ix).",
    sig="The largest oryx reintroduction in the world and the first natural World Heritage site of the kingdom.",
    ex='National Center for Wildlife; formerly NCWCD',
    disc=['Oryx reintroduced from 1995', '120 plant species in the sand'],
    refs=['UNESCO World Heritage Centre. ‘Uruq Bani Ma’arid (ref. 1699), inscribed 2023.', 'National Center for Wildlife, Saudi Arabia. Uruq Bani Ma’arid Protected Area.'])

add(id='farasan-islands', n='Farasan Islands', na='جزر فرسان', c='ecology', s='Red Sea archipelago · Biosphere Reserve', lat=16.70, lng=42.00,
    p='Living reef and islands', dr='Protected 1989 · Biosphere Reserve 2021', el='More than 84 islands, 5,408 km²', ic='island', era='N', t0=37, t1=0,
    te='Gazelles on a coral island', ta='غزلان على جزيرة مرجانية', se='Eighty-four islands of raised reef, home to Saudi Arabia’s largest gazelle herd, mangroves and nesting seabirds', sa='أربع وثمانون جزيرة من شعاب مرفوعة، موطن أكبر قطيع غزلان في السعودية، والقرم والطيور البحرية',
    desc="An archipelago of more than 84 islands about 42 km off Jazan, built of uplifted coral limestone that stands 10–20 m and locally 75 m above the sea. Protected in 1989 and Saudi Arabia's first UNESCO Biosphere Reserve in September 2021, the 5,408 km² reserve is 90 percent marine: coral reefs, seagrass, three of the Red Sea's thirteen red-mangrove stands, dugong, green and hawksbill turtles, and nesting pink-backed pelicans, sooty falcons and crab-plovers. The islands carry the largest population of the Farasan (idmi) gazelle.",
    sig="The richest island ecosystem of the Saudi Red Sea.",
    ex='National Center for Wildlife; Khaled bin Sultan Living Oceans Foundation surveys 2006',
    disc=['Largest gazelle population in the kingdom', 'Uplifted coral islands'],
    refs=['UN Saudi Arabia (2021). Juzur Farasan: first Biosphere Reserve in KSA.', 'Saudipedia. Farasan Islands Marine Reserve.'])

add(id='jubail-marine-sanctuary', n='Jubail Marine Wildlife Sanctuary', na='محمية الجبيل البحرية', c='ecology', s='Seagrass, dugong and flamingos on the Gulf', lat=27.083, lng=49.617,
    p='Living coast', dr='Established 1990s after the 1991 oil spill', el='About 2,410 km² of bays and islands', ic='dolphin', era='N', t0=35, t1=0,
    te='A coast that healed', ta='ساحل تعافى', se='Hit by the 1991 oil spill, the bays north of Jubail were protected and now hold dugong, turtles and a flamingo colony', sa='بعد تسرب النفط عام 1991، حُميت الخلجان شمال الجبيل وتضم اليوم الأتوم والسلاحف ومستعمرة فلامنغو',
    desc="A protected area of about 2,410 km² of shallow bays, islands and sabkha between Jubail and the Kuwaiti border, the coast most heavily oiled by the 1991 Gulf War spill. Set up by the NCWCD in the early 1990s, it protects seagrass meadows, coral patches, mangroves and mudflats used by several hundred dugong, green and hawksbill turtles, dolphins and a breeding colony of greater flamingos; the Sabkhat al-Fasl lagoons nearby are a Key Biodiversity Area for waterbirds.",
    sig="The main recovery site for the Gulf coast after the largest oil spill in history.",
    ex='National Center for Wildlife; Royal Commission for Jubail; EU-Gulf War damage assessment 1992',
    disc=['Several hundred dugong', 'Flamingo breeding colony'],
    refs=['Protected Planet. Jubail Marine Wildlife Sanctuary (WDPA 61786).', 'Krupp, F. & Abuzinada, A. H. (eds.) (1996). A Marine Wildlife Sanctuary for the Arabian Gulf: environmental research and conservation following the 1991 Gulf War oil spill. NCWCD and Senckenberg.'])

add(id='raydah-juniper', n='Raydah Reserve and the Asir Junipers', na='محمية ريدة وعرعر عسير', c='ecology', s='Cloud forest of Arabia', lat=18.20, lng=42.40,
    p='Living forest', dr='Protected since 1989', el='Escarpment from 2,800 m to 1,350 m', ic='wood', era='N', t0=37, t1=0,
    te='A forest in the clouds', ta='غابة في السحاب', se='Juniper woods between 2,500 and 3,000 m hold the Asir magpie, found nowhere else on Earth', sa='غابات العرعر بين 2,500 و3,000 م تضم عقعق عسير الذي لا يوجد في أي مكان آخر على الأرض',
    desc="About 1,200 ha of the Asir escarpment west of Abha, falling from about 2,800 m to Wadi Jaw at 1,350 m, protected since 1989 for the densest juniper woodland in the kingdom. The junipers grow between 2,500 and 3,000 m where monsoon cloud brings moisture, and shelter most of Arabia's endemic birds, including the Asir magpie, estimated at only about 135 pairs. Drought, grazing and development threaten the trees; Soudah Development has planted some 165,000 native trees in the highlands.",
    sig="The only cloud forest of the Arabian Peninsula and the home of its rarest bird.",
    ex='National Center for Wildlife; Asir National Park; National Center for Vegetation Cover',
    disc=['Asir magpie, c. 135 pairs', 'Junipers up to 255 years old'],
    refs=['Birds of Saudi Arabia (J. Babbington). Arabian endemics and the Raydah Protected Area.', 'Arab News (16 May 2025). How Saudi Arabia is safeguarding biodiversity by restoring its ancient juniper forests.'])

add(id='al-wajh-lagoon', n='Al Wajh Lagoon', na='بحيرة الوجه', c='ecology', s='Red Sea reef lagoon of 92 islands', lat=25.60, lng=36.80,
    p='Living reef', dr='Marine spatial plan 2020', el='2,081 km² lagoon, 92 islands', ic='wave', era='N', t0=6, t1=0,
    te='Ninety-two islands, nine untouched', ta='اثنتان وتسعون جزيرة، تسع منها بلا مساس', se='A reef lagoon planned so that 58 percent is conserved and development covers 5 percent', sa='بحيرة شعابية خُطط لها بحيث يُحفظ 58% منها ولا يتجاوز العمران 5%',
    desc="A lagoon of 2,081 km² enclosed by a barrier reef on the northern Red Sea coast, with 92 islands, coral reefs, seagrass beds and mangroves and species of global conservation concern. In 2020 KAUST scientists led by Carlos Duarte published a marine spatial plan for the Red Sea Project here that conserves 58 percent of the marine area and limits development to about 5 percent, aiming for a 30 percent net conservation gain. The reef corals of the northern Red Sea are among the most heat-tolerant known.",
    sig="A test of whether tourism can be built around a reef without losing it.",
    ex='KAUST Red Sea Research Center; Red Sea Global',
    disc=['Marine plan conserving 58% of the lagoon', 'Corals tolerant of heat'],
    refs=['Chalastani, V. I., Manetos, P., Al-Suwailem, A. M. et al. (2020). Reconciling tourism development and conservation outcomes through marine spatial planning for a Saudi Giga-Project in the Red Sea. Frontiers in Marine Science 7, 168.', 'KAUST News (15 April 2020). Scientific paper details marine spatial planning at Red Sea Project.'])

D = {'sites': S, 'stops': []}
json.dump(D, open('/tmp/w/gulf/sa/data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
