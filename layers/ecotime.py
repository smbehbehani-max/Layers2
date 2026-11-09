"""How each living place relates to time, taken from its own record:
SEASON — a yearly event (months stated in the record); ANCIENT — the living thing or ecosystem itself is old (age stated in the record);
everything else is placed by the year it was recorded or protected."""
W = (11, 12, 1, 2, 3)   # 'winter' in the records
SEASON = {
 'iris-playa-meadow': ((2, 3, 4), 'Spring bloom', 'تفتّح الربيع'),
 'khareef-wadi-darbat': ((6, 7, 8, 9), 'Khareef monsoon forest', 'غابة الخريف الموسمية'),
 'jabal-samhan': ((6, 7, 8, 9), 'Khareef fog woodland', 'غابات ضباب الخريف'),
 'al-shaheen-whale-sharks': ((4, 5, 6, 7, 8, 9), 'Whale sharks gather', 'تجمّع أسماك القرش الحوتي'),
 'fuwairit-turtles': ((3, 4, 5, 6, 7), 'Hawksbill nesting', 'تعشيش السلاحف صقرية المنقار'),
 'umm-tais-national-park': ((3, 4, 5, 6, 7), 'Hawksbill nesting', 'تعشيش السلاحف صقرية المنقار'),
 'dimaniyat-islands': ((6, 7, 8), 'Seabirds nest', 'تعشيش الطيور البحرية'),
 'al-wathba-wetland': ((12, 1, 2, 3, 4), 'Flamingos breed', 'تكاثر الفلامنغو'),
 'ras-al-khor': (W, 'Flamingos winter', 'شتاء الفلامنغو'),
 'tubli-bay': (W, 'Wintering waterbirds', 'الطيور المائية الشاتية'),
 'hawar-islands': (W, 'Flamingos and gulls winter', 'شتاء الفلامنغو والنوارس'),
 'maqabah-hypocolius': (W, 'Hypocolius winter roost', 'مبيت الهيبوكوليس الشتوي'),
 'barr-al-hikman': (W, 'Arctic shorebirds winter', 'شتاء طيور الشاطئ القطبية'),
 'khor-al-beidah': (W, 'Wintering shorebirds', 'طيور الشاطئ الشاتية'),
 'khor-al-adaid': (W, 'Migrant waterfowl winter', 'شتاء الطيور المهاجرة'),
 'gulf-of-salwa-dugongs': ((12, 1, 2, 3), 'Dugong herds gather', 'تجمّع قطعان الأطوم'),
 'qatar-dugongs': ((12, 1, 2), 'Dugong herds gather', 'تجمّع قطعان الأطوم'),
}
ANCIENT = {   # years, what the age refers to (from the record's own date field)
 'tree-of-life': (444, 'A single mesquite tree, planted c. 1582', 'شجرة غاف واحدة، زُرعت نحو 1582'),
 'wadi-dawkah': (2000, 'Frankincense harvested here for over 2,000 years', 'يُحصد اللبان هنا منذ أكثر من 2,000 عام'),
 'khor-sabiyah-marsh': (6000, 'A salt marsh about 6,000 years old', 'سبخة ملحية عمرها نحو 6,000 عام'),
 'jahra-freshwater-lens': (10000, 'A freshwater lens about 10,000 years old', 'عدسة مياه عذبة عمرها نحو 10,000 عام'),
}

# what makes a seasonal event unique — quoted from each record's own "significance" line
UNIQUE = {
 'khareef-wadi-darbat': ('The only monsoon forest of the Arabian Peninsula', 'غابة الرياح الموسمية الوحيدة في شبه الجزيرة العربية'),
 'jabal-samhan': ('Arabia\'s monsoon fog woodland', 'غابة ضباب الرياح الموسمية في الجزيرة العربية'),
 'al-shaheen-whale-sharks': ('One of the largest whale shark gatherings on Earth', 'من أكبر تجمعات القرش الحوتي على الأرض'),
 'al-wathba-wetland': ('The Gulf\'s first regular flamingo breeding site', 'أول موقع منتظم لتكاثر الفلامنغو في الخليج'),
 'barr-al-hikman': ('The Middle East\'s most significant wintering wetland', 'أهم أرض رطبة للتشتية في الشرق الأوسط'),
 'hawar-islands': ('The world\'s largest Socotra cormorant colony', 'أكبر مستعمرة لغاق سقطرى في العالم'),
 'fuwairit-turtles': ('The northern Gulf\'s most important hawksbill rookery', 'أهم موقع تعشيش للسلاحف صقرية المنقار في شمال الخليج'),
 'gulf-of-salwa-dugongs': ('The world\'s second-largest dugong population', 'ثاني أكبر تجمع للأطوم في العالم'),
}
