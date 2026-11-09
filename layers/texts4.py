def texts(total):
    EN = {'lang': 'عربي', 'by': 'by GEOHERITAGE', 'tag1': 'Discover the Gulf Beyond the Ordinary.', 'c1': 'Explore the Gulf',
     'k2': 'What is LAYERS', 't2': 'One Landscape. Multiple Stories.', 'st1': 'Ecological', 'st2': 'Archaeological', 'st3': 'Geological',
     'g1': 'Geological', 'g2': 'Archaeological', 'g3': 'Ecological',
     'k3': 'Powered by', 'ai': 'Artificial Intelligence', 'aid': 'Connecting knowledge, interpreting relationships and revealing stories.',
     'tag2': 'A new way to experience the Gulf.', 'k4': 'Six countries', 't4': 'Explore the Gulf',
     'wl1': 'Arabian Gulf', 'wl2': 'Red Sea', 'wl3': 'Arabian Sea',
     'f1': 'GEO — geological and geographical. HERITAGE — what makes a place matter. LAYERS — how you explore it.',
     'priv': 'Privacy', 'made': 'Made in Kuwait', 'loading': 'Opening…'}
    AR = {'lang': 'English', 'by': 'من جيوهيريتيج', 'tag1': 'اكتشف الخليج بما يتجاوز المألوف.', 'c1': 'استكشف الخليج',
     'k2': 'ما هو «طبقات»', 't2': 'أرض واحدة. قصص متعددة.', 'st1': 'البيئة', 'st2': 'الآثار', 'st3': 'الجيولوجيا',
     'g1': 'جيولوجيا', 'g2': 'آثار', 'g3': 'بيئة',
     'k3': 'بقوة', 'ai': 'الذكاء الاصطناعي', 'aid': 'يربط المعرفة، ويفسّر العلاقات، ويكشف القصص.',
     'tag2': 'طريقة جديدة لتجربة الخليج.', 'k4': 'ست دول', 't4': 'استكشف الخليج',
     'wl1': 'الخليج العربي', 'wl2': 'البحر الأحمر', 'wl3': 'بحر العرب',
     'f1': 'جيو — الجيولوجيا والجغرافيا. التراث — ما يجعل المكان مهمًا. طبقات — طريقك لاستكشافه.',
     'priv': 'الخصوصية', 'made': 'صُنع في الكويت', 'loading': 'جارٍ الفتح…'}
    for cc in ORDER:
        c = H.C[cc]; EN['c.' + cc] = c['en'].replace('the UAE', 'UAE'); AR['c.' + cc] = c['ar']
    return EN, AR
