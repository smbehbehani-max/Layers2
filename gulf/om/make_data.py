# Layers of Oman — researcher catalogue v0.1
import json
S = []
def add(**k): S.append(k)

add(id='bat-al-khutm-al-ayn', n='Bat, Al-Khutm and Al-Ayn', na='بات والخطم والعين', c='archaeological', s='Bronze Age towers and tombs · World Heritage', lat=23.2699, lng=56.7450,
    p='Hafit and Umm an-Nar periods', dr='3rd millennium BC', el='Towers about 20 m across', ic='mound', era='P', t0=5025, t1=4025,
    te='Towers with no doors', ta='أبراج بلا أبواب', se='Round stone buildings 20 m wide whose purpose is still unknown, and a hillside of beehive tombs', sa='مبانٍ حجرية دائرية بعرض 20 م لا يُعرف غرضها، وسفح من قبور كخلايا النحل',
    desc="A 3rd-millennium BC necropolis and settlement in Al Dhahirah: at Bat about 100 graves and circular buildings each about 20 m in diameter with no outside openings; at Al-Khutm, 2 km west, a rock tower of 20 m thought to be a fort; and at Al-Ayn, 22 km south-east, the best-preserved line of beehive tombs on a ridge. A Danish team under Karen Frifelt excavated in 1972 and found some 4,000 years of continuous occupation. Inscribed in 1988 under criteria (iii) and (iv), Oman's second World Heritage site.",
    sig="The most complete Bronze Age settlement and cemetery landscape of the 3rd millennium BC in the world, per UNESCO.",
    ex='Danish expedition (K. Frifelt) 1972; University of Pennsylvania Bat Archaeological Project 2007–2012',
    disc=['Circular towers 20 m across without doors', 'Beehive tombs of Al-Ayn'],
    refs=['Thornton, C. P., Cable, C. M. & Possehl, G. L. (2016). The Bronze Age Towers at Bat, Sultanate of Oman. University of Pennsylvania Press.', 'UNESCO World Heritage Centre. Archaeological Sites of Bat, Al-Khutm and Al-Ayn (ref. 434), inscribed 1988.'])

add(id='bahla-fort', n='Bahla Fort', na='قلعة بهلاء', c='archaeological', s='Mud-brick fortress of the Banu Nabhan · World Heritage', lat=22.9642, lng=57.3011,
    p='Islamic (Nabhani to Ya’ariba)', dr='12th – 18th century AD', el='Oasis wall about 13 km', ic='wall', era='H', t0=900, t1=250,
    te='A castle made of earth', ta='قلعة من تراب', se='A mud-brick fortress and a 13 km wall around an oasis famous for its potters', sa='قلعة من الطوب الطيني وسور بطول 13 كم حول واحة اشتهرت بخزّافيها',
    desc="A fortress of mud brick and straw at the foot of the Jebel Akhdar, believed to have been built between the 12th and 15th centuries by the Banu Nabhan, with the Al-Qasabah as its oldest part, the Bait al-Hadith of the Ya'ariba dynasty (1624–1743) and the 18th-century Bait al-Jabal. A wall of about 13 km, partly standing, encloses the oasis. Inscribed in 1987 as Oman's first World Heritage site, placed on the List in Danger from 1988 to 2004 because of decay of the unfired brick, and reopened in 2012 after a long restoration.",
    sig="The largest surviving earthen fortress of the Gulf and a lesson in how to conserve mud architecture.",
    ex='Ministry of Heritage and Tourism; ArCHIAM Centre management plan 2013',
    disc=['Three building phases from the 12th to the 18th century', 'Oasis wall of about 13 km'],
    refs=['UNESCO World Heritage Centre. Bahla Fort (ref. 433), inscribed 1987; State of Conservation report 2018.', 'ArCHIAM Centre (2013). Bahla Fort and Oasis heritage management plan.'])

add(id='khor-rori-sumhuram', n='Khor Rori (Sumhuram)', na='خور روري (سمهرم)', c='archaeological', s='Frankincense port · World Heritage', lat=17.038, lng=54.433,
    p='Late pre-Islamic', dr='Late 1st century BC – 5th century AD', el='Walled town above a lagoon', ic='boat', era='H', t0=2050, t1=1550,
    te='The port of incense', ta='ميناء البخور', se='A walled port founded by the kings of Hadramawt to ship frankincense to Rome and India', sa='ميناء مسوّر أسسه ملوك حضرموت لشحن اللبان إلى روما والهند',
    desc="A fortified port on a lagoon east of Salalah, founded at the end of the 1st century BC by the kingdom of Hadramawt to control the Dhofar incense trade, and identified with the Moscha of classical texts. Inscriptions in the gate name the city Sumhuram; warehouses, a temple and houses lie within the walls. One of four components of the Land of Frankincense property (849.88 ha) inscribed in 2000 under criteria (iii) and (iv) and renamed in 2005.",
    sig="The best-preserved pre-Islamic port of the incense route, where South Arabian script meets Roman and Indian trade.",
    ex='American Foundation for the Study of Man 1952–53; Italian Mission to Oman (University of Pisa) 1997 onwards',
    disc=['Gate inscriptions naming Sumhuram', 'Warehouses for frankincense'],
    refs=['UNESCO World Heritage Centre. Land of Frankincense (ref. 1010), inscribed 2000.', 'Avanzini, A. (ed.) (2008). A Port in Arabia between Rome and the Indian Ocean (3rd C. BC – 5th C. AD): Khor Rori Report 2. L\'Erma di Bretschneider.'])

add(id='al-baleed', n='Al-Baleed (Zafar)', na='البليد (ظفار)', c='archaeological', s='Medieval port of Dhofar · World Heritage', lat=17.000, lng=54.120,
    p='Islamic', dr='c. 10th – 16th century AD', el='Port with citadel and grand mosque', ic='platform', era='H', t0=1050, t1=450,
    te='The city Marco Polo saw', ta='المدينة التي رآها ماركو بولو', se='A walled medieval port that sold frankincense and horses to China and India', sa='ميناء مسوّر من العصور الوسطى باع اللبان والخيول للصين والهند',
    desc="The ruins of the medieval city of Zafar on the Salalah shore: a walled port with a citadel and a grand mosque, visited by Ibn Battuta and recorded by Marco Polo's generation, which exported frankincense and Arabian horses across the Indian Ocean until its decline in the 16th century. It is a component of the Land of Frankincense World Heritage property and houses the Museum of the Frankincense Land.",
    sig="The medieval successor of Sumhuram and the last great port of the incense trade.",
    ex='Office of the Adviser to His Majesty for Cultural Affairs; German (DAI) and American missions',
    disc=['Citadel and grand mosque', 'Horse-export port of the Middle Ages'],
    refs=['UNESCO World Heritage Centre. Land of Frankincense (ref. 1010).', 'World Heritage Site community reviews, Land of Frankincense (worldheritagesite.org).'])

add(id='shisr-ubar', n='Shisr (Wubar)', na='شصر (وبار)', c='archaeological', s='Caravan oasis of the incense road', lat=18.260, lng=53.650,
    p='Pre-Islamic to Islamic', dr='By 300 BC – 16th century AD', el='Spring and collapsed fort at the desert edge', ic='caravan', era='H', t0=2325, t1=450,
    te='The city lost in the sands', ta='المدينة الضائعة في الرمال', se='A caravan fort over a spring, identified in the 1990s with the legendary Ubar', sa='حصن قوافل فوق عين، رُبط في التسعينيات بمدينة أوبار الأسطورية',
    desc="A spring and fortified caravan station on the edge of the Rub' al Khali north of Thumrait, part of the incense trade network by 300 BC. Identified in the early 1990s by Sir Ranulph Fiennes and a team of archaeologists as the legendary Ubar, an identification still debated; part of the fort collapsed into the sinkhole of its own spring. A component of the Land of Frankincense World Heritage property.",
    sig="The desert end of the incense road, where caravans watered before crossing to the Gulf.",
    ex='Trans-Arabia Expedition (N. Clapp, R. Fiennes, J. Zarins) 1990–1995',
    disc=['Fort collapsed into its spring sinkhole', 'Trade goods from 300 BC onward'],
    refs=['UNESCO World Heritage Centre. Land of Frankincense (ref. 1010).', 'Zarins, J. (2001). The Land of Incense: archaeological work in the Governorate of Dhofar. Sultan Qaboos University.'])

add(id='falaj-daris', n='Falaj Daris and the Aflaj of Oman', na='فلج دارس وأفلاج عُمان', c='archaeological', s='Living irrigation channels · World Heritage', lat=22.9833, lng=57.5333,
    p='Iron Age to present', dr='From c. AD 500 (tradition 5,000 years old)', el='Five inscribed aflaj; c. 3,000 still flowing', ic='river', era='H', t0=1500, t1=0,
    te='Water shared by the minute', ta='ماء يُقسَّم بالدقيقة', se='Underground channels up to 12 km long bring mountain water to oases, still divided by the stars', sa='قنوات تحت الأرض بطول 12 كم تجلب ماء الجبل إلى الواحات، وما زالت تُقسَّم بالنجوم',
    desc="Falaj Daris at Nizwa is the largest of five aflaj inscribed in 2006 (with Al-Khatmeen, Al-Malki, Al-Mayassar and Al-Jeela) under criterion (v). About 3,000 aflaj still function in Oman; the systems date from around AD 500 within a 5,000-year irrigation tradition. Daudi aflaj (23.5%) run underground up to 12 km and 50 m deep; ghaili aflaj (48.5%) are seasonal open channels; aini aflaj (28%) carry spring water, sometimes hot. Water is shared by timed turns under a management system that has survived for centuries.",
    sig="The most extensive living example of ancient water engineering in Arabia.",
    ex='Ministry of Agriculture, Fisheries and Water Resources (Aflaj inventory)',
    disc=['Daudi channels up to 12 km long', 'About 3,000 working aflaj'],
    refs=['UNESCO World Heritage Centre. Aflaj Irrigation Systems of Oman (ref. 1207), inscribed 2006.', 'Al-Ghafri, A. S. (2018). Overview about the aflaj of Oman. Proceedings of the International Symposium of Khettaras and Qanats.'])

add(id='qalhat', n='Ancient City of Qalhat', na='مدينة قلهات القديمة', c='archaeological', s='Hormuz-era port · World Heritage', lat=22.6994, lng=59.3694,
    p='Islamic', dr='11th – 16th century AD', el='About 24 ha within walls', ic='jar', era='H', t0=950, t1=450,
    te='The queen’s mosque', ta='مسجد الملكة', se='A port that Marco Polo and Ibn Battuta praised, ruled by a woman after 1311', sa='ميناء أثنى عليه ماركو بولو وابن بطوطة، حكمته امرأة بعد عام 1311',
    desc="The ruins of a walled port of more than 24 ha north of Sur, the second city of the Kingdom of Hormuz. Marco Polo called it Calatu in the 13th century and Ibn Battuta in the 14th praised its bazaars and a mosque built by Bibi Maryam, who ruled Qalhat and Hormuz after her husband Ayaz died in 1311–12; her mausoleum, now without its dome, is the main standing monument. The city declined as trade moved to Muscat, was taken by the Portuguese by 1507, and earthquakes on the Qalhat Fault are a plausible cause of its ruin. Inscribed in 2018.",
    sig="A rare intact medieval Indian Ocean port, abandoned early and never rebuilt.",
    ex='French Archaeological Mission at Qalhat (A. Rougeulle), 2008 onwards',
    disc=['Mausoleum of Bibi Maryam', 'City walls and water cisterns'],
    refs=['UNESCO World Heritage Centre. Ancient City of Qalhat (ref. 1537), inscribed 2018.', 'Rougeulle, A. (ed.) (2017). Qalhāt, Oman: a medieval port city. Archaeopress.'])

add(id='ras-al-jinz-rj2', n='Ras al-Jinz Bronze Age Village (RJ-2)', na='قرية رأس الجنز من العصر البرونزي', c='archaeological', s='Fishing village in contact with the Indus', lat=22.410, lng=59.830,
    p='Bronze Age', dr='c. 2300 – 2000 BC', el='1 km² of remains · 100 sites · 350 graves', ic='boat', era='P', t0=4325, t1=4025,
    te='Fishermen who knew the Indus', ta='صيادون عرفوا السند', se='A village at the easternmost point of Arabia that traded with India 4,000 years ago', sa='قرية في أقصى شرق الجزيرة العربية تاجرت مع الهند قبل 4,000 عام',
    desc="Remains covering about 1 km² at the easternmost point of Arabia, 11 km south of Ras al Hadd, with 100 documented sites and some 350 graves on the mesa above Khawr Jarama. Occupation runs from the early Holocene to the Iron Age; steatite vessels date to about 2300 BC, an incense burner to 2200 BC and settlements to 2000 BC. A potsherd with a Harappan inscription found in 1982 shows contact with the Indus Valley, with bitumen, stamp seals, fish hooks, metal pins and an Indian ivory comb among the finds. On the UNESCO Tentative List with the turtle reserve (2013).",
    sig="Evidence that Oman's fishermen were part of the Bronze Age world linking Mesopotamia, the Gulf and the Indus.",
    ex='Joint Hadd Project (S. Cleuziou, M. Tosi), 1985–2000s',
    disc=['Harappan-inscribed potsherd (1982)', 'Indian ivory comb'],
    refs=['UNESCO World Heritage Centre. Ras al Had Turtle Reserve and the Heritage Site of Ras al Jinz, Tentative List ref. 5840 (2013).', 'Cleuziou, S. & Tosi, M. (2007). In the Shadow of the Ancestors: the prehistoric foundations of the early Arabian civilization in Oman. Ministry of Heritage and Culture.'])

# ---------------- GEOLOGY ----------------
add(id='semail-ophiolite', n='Semail Ophiolite', na='أفيوليت سمائل', c='geological', s='The world’s largest slice of ocean crust on land', lat=23.390, lng=57.830,
    p='Late Cretaceous', dr='Crust formed 96 – 94 million years ago; thrust onto Arabia soon after', el='550 km long · 150 km wide · over 10,000 km²', ic='fault', era='D', t0=96e6, t1=70e6,
    te='The sea floor that climbed onto the land', ta='قاع البحر الذي صعد إلى اليابسة', se='Oman’s dark mountains are a 550 km sheet of oceanic crust and mantle pushed over the continent', sa='جبال عُمان الداكنة صفيحة من قشرة المحيط ووشاحه بطول 550 كم دُفعت فوق القارة',
    desc="The Hajar Mountains are built largely of the Semail ophiolite, described as the world's largest and best-preserved thrust sheet of oceanic crust and upper mantle: more than 10,000 km², about 550 km long and 150 km wide. The crust formed 96–94 million years ago at a spreading centre above a north-east-dipping subduction zone and was emplaced onto the Arabian margin in the Late Cretaceous; its metamorphic sole formed at about 850 °C 95–93 million years ago, and eclogites at As Sifah record continental crust dragged 78–90 km down. The sequence, from arc lavas and pillow basalts through gabbros to more than 12 km of mantle harzburgite, can be walked across in a day in wadis such as Wadi Al Abyad.",
    sig="The reference ophiolite of the planet, where geologists go to see the ocean floor and the mantle at the surface.",
    ex='Oxford (M. Searle) and international teams; Oman Drilling Project 2017–2018',
    disc=['Mantle rock exposed at the surface', 'Eclogites from 78–90 km depth at As Sifah'],
    refs=['Searle, M. & Cox, J. Tectonic setting, origin, and obduction of the Oman ophiolite. Geological Society of America Bulletin 111(1), 104–122 (1999).'])

add(id='jebel-shams', n='Jebel Shams and Wadi Nakhr', na='جبل شمس ووادي نخر', c='geological', s='Oman’s highest peak and its Grand Canyon', lat=23.237, lng=57.264,
    p='Permian to Cretaceous', dr='Limestone laid down 270 – 90 million years ago', el='3,010 m · canyon 1,000 m deep', ic='cliff', era='D', t0=270e6, t1=90e6,
    te='Three thousand metres of sea floor', ta='ثلاثة آلاف متر من قاع البحر', se='A canyon a kilometre deep cuts through the whole Hajar Supergroup', sa='أخدود بعمق كيلومتر يشق مجموعة الحجر الكبرى بأكملها',
    desc="At 3,010 m Jebel Shams is the highest point of the Jebel Akhdar and of Oman, in a range about 700 km long. Wadi Nakhr, the 'Grand Canyon of Arabia', is 12 km long, over 1 km wide at the viewpoint and more than 1,000 m deep, cutting through about 3,000 m of the Hajar Supergroup, shallow-marine limestone deposited from the Late Permian to the Late Cretaceous: Jurassic Sahtan oolitic limestone, Lower Cretaceous Kahmah limestone and marl, and the mid-Cretaceous Natih limestone over Nahr Umr shale, the same reservoir rocks that hold Oman's oil.",
    sig="The clearest exposure of the rocks beneath Arabia's oil fields, visible from a single viewpoint.",
    ex='Petroleum Development Oman geological surveys; GeoExpro (Whaley 2018)',
    disc=['Canyon over 1,000 m deep', 'Entire Hajar Supergroup exposed'],
    refs=['Whaley, J. (2018). The Grand Canyon of the Middle East. GEO ExPro, 3 December 2018.'])

add(id='majlis-al-jinn', n='Majlis al Jinn', na='مجلس الجن', c='geological', s='One of the largest cave chambers on Earth', lat=22.880, lng=59.090,
    p='Quaternary karst in Eocene rock', dr='Chamber in Middle Eocene Dammam limestone', el='310 × 225 m · 120 m high · 1,380 m a.s.l.', ic='sinkhole', era='D', t0=2.58e6, t1=0,
    te='The meeting place of the spirits', ta='مجلس الجن', se='A chamber big enough to hold ten jumbo jets, entered only by rope through holes in its roof', sa='قاعة تتسع لعشر طائرات جامبو، لا تُدخل إلا بالحبل عبر فتحات في سقفها',
    desc="A single chamber about 310 m long, 225 m wide and 120 m high, with a floor of 58,000 m² and a volume of about 4 million m³, beneath the Selma Plateau at 1,380 m, 100 km south-east of Muscat. Formed in fossiliferous marly limestone of the Middle Eocene Dammam Formation under a roof only 40 m thick, it is entered by free descent through three ceiling holes (Cheryl's Drop 158 m, Asterisk 140 m, First Drop 118 m). Discovered in June 1983 by Don Davison and Cheryl Jones and surveyed in 1985, when it ranked second in the world by volume; it has been closed by the government since 2008.",
    sig="A world-ranking cave chamber, and the same Dammam Formation that forms the aquifer of Bahrain and Qatar.",
    ex='Public Authority for Water Resources (survey 1985)',
    disc=['Volume about 4,000,000 m³', 'Entrance drops up to 158 m'],
    refs=['Public Authority for Water Resources, Oman (1985). Report PAWR 85-20.', 'Davison, W. D. (1990). Meeting place of the spirits. Aramco World, Sept–Oct 1990.'])

add(id='sharqiya-sands', n='Sharqiya (Wahiba) Sands', na='رمال الشرقية (الوهيبة)', c='geological', s='A sand sea 180 km long', lat=22.300, lng=58.800,
    p='Quaternary', dr='Dunes formed after the last ice age', el='12,500 km² · dunes to 100 m', ic='dune', era='D', t0=11700, t1=0,
    te='Dunes on a cemented floor', ta='كثبان على أرضية متحجرة', se='Living dunes 100 m high rest on an older desert turned to stone', sa='كثبان حيّة بارتفاع 100 م تستقر فوق صحراء أقدم تحوّلت إلى حجر',
    desc="A dune field of about 12,500 km², 180 km north–south and 80 km east–west, whose northern dunes rise to 100 m and rest on an older layer of cemented carbonate sand. The 1986 Royal Geographical Society expedition recorded 16,000 invertebrates, 200 other animal species and 150 native plants, including ghaf (Prosopis cineraria) woodland; Bedouin of the Al Wahiba and other tribes still gather at the Al-Huyawah oasis for the date harvest.",
    sig="One of the best-studied sand seas in the world and the type example of a dune field in the monsoon belt.",
    ex='Royal Geographical Society Oman Wahiba Sands Project, 1985–1987',
    disc=['Cemented sand beneath the living dunes', '16,000 invertebrates recorded in 1986'],
    refs=['Dutton, R. W. (ed.) (1988). The Scientific Results of the Royal Geographical Society\'s Oman Wahiba Sands Project 1985–1987. Journal of Oman Studies Special Report 3.', 'Pease, P. P. et al. (1999). Mineralogical characterization and transport pathways of dune sand using Landsat TM data, Wahiba Sand Sea. Geomorphology.'])

# ---------------- ECOLOGY ----------------
add(id='ras-al-had-turtles', n='Ras al Hadd Turtle Reserve', na='محمية السلاحف في رأس الحد', c='ecology', s='Green turtle rookery', lat=22.520, lng=59.780,
    p='Living today', dr='Reserve since 23 April 1996', el='120 km² · 45 km of coast', ic='wave', era='N', t0=30, t1=0,
    te='Twenty thousand turtles come home', ta='عشرون ألف سلحفاة تعود', se='Most of Oman’s green turtles nest on one 45 km stretch of beach', sa='تعشّش معظم سلاحف عُمان الخضراء على شريط شاطئ واحد بطول 45 كم',
    desc="A 120 km² reserve declared on 23 April 1996 covering about 45 km of coast from Khawr Jarama to Ras Ruwais, with two lagoons, mangrove and coral at Khawr Jarama, about 130 bird species and the white stork on migration. About 20,000 green turtles nest on more than 275 beaches along Oman's coast and most nest within this reserve; 14 rangers and a visitor centre at Ras al-Jinz manage night viewing. On the UNESCO Tentative List since 2013 together with the Bronze Age site.",
    sig="One of the largest green turtle nesting grounds in the Indian Ocean.",
    ex='Environment Authority, Oman; Ras al-Jinz Scientific and Visitor Centre',
    disc=['About 20,000 nesting green turtles', '45 km protected coastline'],
    refs=['UNESCO World Heritage Centre. Ras al Had Turtle Reserve and the Heritage Site of Ras al Jinz, Tentative List ref. 5840 (2013).'])

add(id='masirah-loggerheads', n='Masirah Island Loggerheads', na='سلاحف مصيرة ضخمة الرأس', c='ecology', s='Globally important loggerhead rookery', lat=20.450, lng=58.780,
    p='Living today', dr='Monitored 1977 – 2019', el='83 km of nesting beach', ic='wave', era='N', t0=49, t1=0,
    te='A decline inside one lifetime', ta='تراجع في عمر جيل واحد', se='From 20,000–40,000 females a year to about 10,000, mostly lost to fishing nets', sa='من 20 إلى 40 ألف أنثى في السنة إلى نحو 10 آلاف، فُقد معظمها في شباك الصيد',
    desc="Masirah Island's 83 km of beaches hold one of the world's most important loggerhead turtle rookeries. Nesting females were estimated at 20,000–40,000 a year in 1977–1986 but at 10,223–11,500 in 2008–2016 (about 55,000 nests a year); track counts on the index beaches fell 79% between 1985–1996 and 2008–2016, within a single turtle generation of about 47 years, and density fell further by 2019. Bycatch is the most likely cause: community surveys in 2013 estimated 1,640–1,770 loggerheads a year caught in artisanal gillnets. Demersal trawling has been illegal in Oman since 2011.",
    sig="A warning from the Indian Ocean's largest loggerhead population, measured over forty years.",
    ex='Environment Authority, Oman with Five Oceans Environmental Services (Willson et al. 2020)',
    disc=['79% decline in nesting tracks', '1,640–1,770 turtles a year in gillnets'],
    refs=['Willson, A., Witherington, B., Baldwin, R., Tiwari, M., Al Sariri, T., Al Kiyumi, A. et al. (2020). Evaluating the long-term trend and management of a globally important loggerhead population nesting on Masirah Island, Sultanate of Oman. Frontiers in Marine Science 7, 666.'])

add(id='jabal-samhan', n='Jabal Samhan Nature Reserve', na='محمية جبل سمحان', c='ecology', s='Stronghold of the Arabian leopard', lat=17.516, lng=54.940,
    p='Living today', dr='Royal Decree 48/97', el='About 4,500 km²', ic='gazelle', era='N', t0=29, t1=0,
    te='The last leopards', ta='آخر النمور', se='A 4,500 km² escarpment above Dhofar where the Arabian leopard still breeds', sa='جرف بمساحة 4,500 كم² فوق ظفار ما زال النمر العربي يتكاثر فيه',
    desc="A reserve of about 4,500 km² on the Jabal Samhan escarpment of Dhofar, established by Royal Decree 48/97, where camera-trap surveys confirmed a persisting population of the critically endangered Arabian leopard and a mother with cub was recorded in 2022. It also holds Arabian wolf, striped hyena, Arabian gazelle, Nubian ibex, rock hyrax, honey badger and red fox, with frankincense, wild fig, wild olive and acacia on its slopes and the monsoon fog of the khareef on its seaward face.",
    sig="The most important site on Earth for the Arabian leopard, with fewer than 200 left in the wild.",
    ex='Office for Conservation of the Environment, Diwan of Royal Court (J. A. Spalton)',
    disc=['Arabian leopard breeding confirmed', 'Nubian ibex and striped hyena'],
    refs=['Spalton, J. A., Al Hikmani, H. M., Willis, D. & Said, A. S. B. (2006). Critically endangered Arabian leopards Panthera pardus nimr persist in the Jabal Samhan Nature Reserve, Oman. Oryx 40(3), 287–294.', 'Oman Observer (17 August 2026). Jabal Samhan Nature Reserve protects rich biodiversity in Dhofar.'])

add(id='dimaniyat-islands', n='Dimaniyat Islands Nature Reserve', na='محمية جزر الديمانيات', c='ecology', s='Coral islands off Muscat', lat=23.850, lng=58.100,
    p='Living today', dr='Reserve since 3 April 1996', el='Nine islands, 16–18 km offshore', ic='crab', era='N', t0=30, t1=0,
    te='Nine islands of birds and turtles', ta='تسع جزر من الطيور والسلاحف', se='Hawksbills, tropicbirds and corals on an archipelago reached only by boat', sa='سلاحف منقار الصقر وطيور الاستوائي ومرجان على أرخبيل لا يُبلغ إلا بالقارب',
    desc="Nine islands 16–18 km off the Batinah coast, declared a nature reserve on 3 April 1996 and submitted to the UNESCO Tentative List in 2013 under natural criterion (x). Some 250–300 hawksbill turtles nest each year and green turtles feed in the shallows; thousands of seabirds nest in summer, including red-billed tropicbird, osprey, roseate, white-cheeked, bridled and sooty terns and common noddy, over a multitude of coral species; humpback whales and dolphins pass offshore. Four rangers guard the islands and landing is restricted in the nesting season.",
    sig="Oman's main hawksbill rookery and the richest coral site near the capital.",
    ex='Environment Authority, Oman; Environment Society of Oman',
    disc=['250–300 hawksbill nests a year', 'Seven seabird species breeding'],
    refs=['UNESCO World Heritage Centre. Al Dimaniyat Islands Nature Reserve, Tentative List ref. 5839 (2013).'])

add(id='oryx-sanctuary', n='Al Wusta Wildlife Reserve (former Arabian Oryx Sanctuary)', na='محمية الوسطى (محمية المها العربي سابقًا)', c='ecology', s='Where the oryx returned, and the listing was lost', lat=19.950, lng=57.100,
    p='Living today', dr='World Heritage 1994 – 2007', el='Jiddat al-Harasis gravel plain', ic='gazelle', era='N', t0=44, t1=0,
    te='A lesson written in oryx', ta='درس مكتوب بالمها', se='The first site ever removed from the World Heritage List, after the herd fell from 450 to 65', sa='أول موقع يُحذف من قائمة التراث العالمي، بعد أن تراجع القطيع من 450 إلى 65',
    desc="The gravel plain of Jiddat al-Harasis where Arabian oryx bred in captivity were returned to the wild from 1982, inscribed as a World Heritage site in 1994. Poaching and habitat degradation cut the free herd from about 450 in 1996 to 65 by 2007, with about four breeding pairs, and after Oman reduced the protected area by 90% to allow hydrocarbon prospecting the World Heritage Committee removed the site on 28 June 2007, the first deletion in the List's history. Oryx are now kept in fenced enclosures in what is today the Al Wusta Wildlife Reserve.",
    sig="A global landmark in conservation history, both for the oryx's return and for its loss.",
    ex='Office for Conservation of the Environment, Diwan of Royal Court',
    disc=['Oryx reintroduced from 1982', 'Delisted by UNESCO in 2007'],
    refs=['UNESCO World Heritage Centre (2007). Oman\'s Arabian Oryx Sanctuary: first site ever to be deleted from UNESCO\'s World Heritage List. News, 28 June 2007.', 'Spalton, J. A., Lawrence, M. W. & Brend, S. A. (1999). Arabian oryx reintroduction in Oman: successes and setbacks. Oryx 33(2).'])

add(id='wadi-dawkah', n='Wadi Dawkah Frankincense Park', na='منتزه وادي دوكة للبان', c='ecology', s='Frankincense trees · World Heritage', lat=17.330, lng=54.070,
    p='Living today', dr='Harvested for over 2,000 years', el='Boswellia sacra woodland north of Salalah', ic='plant', era='N', t0=2300, t1=0,
    te='The trees that perfumed the ancient world', ta='الأشجار التي عطّرت العالم القديم', se='Boswellia sacra still bleeds resin in a protected valley 45 minutes from Salalah', sa='ما زالت شجرة اللبان تنزف صمغها في وادٍ محميّ على بعد 45 دقيقة من صلالة',
    desc="A natural woodland of Boswellia sacra, the frankincense tree, in a dry valley about 45 minutes' drive north of Salalah, where resin is still tapped by cutting the bark as it was for the incense trade of Sumhuram and Zafar. The park is one of the four components of the Land of Frankincense World Heritage property inscribed in 2000.",
    sig="The living source of the trade that built the ports of Dhofar.",
    ex='Ministry of Heritage and Tourism; Office of the Adviser for Cultural Affairs',
    disc=['Resin tapped by cutting the bark', 'Component of a World Heritage property'],
    refs=['UNESCO World Heritage Centre. Land of Frankincense (ref. 1010), inscribed 2000.'])

add(id='khareef-wadi-darbat', n='Khareef and Wadi Darbat', na='الخريف ووادي دربات', c='ecology', s='The monsoon that greens Dhofar', lat=17.110, lng=54.450,
    p='Living today', dr='Late June – September each year', el='Dhofar escarpment, 50 minutes from Salalah', ic='river', era='N', t0=30, t1=0,
    te='Arabia’s green season', ta='موسم الخضرة في الجزيرة العربية', se='Fog from the Indian Ocean turns the mountains green and fills the waterfalls of Wadi Darbat', sa='ضباب من المحيط الهندي يخضّر الجبال ويملأ شلالات وادي دربات',
    desc="From late June to September the south-west monsoon wraps the Dhofar mountains in fog and drizzle, with the landscape greenest from mid-July to the end of August; temperatures drop while the rest of Arabia is at about 43 °C. Wadi Darbat, about 50 minutes from Salalah, fills with waterfalls, lakes and grazing camels, and the escarpment's woodland of figs, olives and frankincense depends on this fog. The season draws thousands of visitors to Salalah each year.",
    sig="The only monsoon forest ecosystem of the Arabian Peninsula.",
    ex='Environment Authority, Oman; Oman Meteorology',
    disc=['Fog-fed woodland on the escarpment', 'Peak greenery mid-July to late August'],
    refs=['Hasan, D. (2023). Everything you need to know about travelling to Salalah during khareef season. The National, 20 July 2023.', 'Oman Observer (2026). Early rains signal start of Dhofar\'s khareef season.'])

D = {'sites': S, 'stops': []}
json.dump(D, open('/tmp/w/gulf/om/data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
