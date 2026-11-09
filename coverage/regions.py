# Approximate first-level region assignment: keyword in the record text first, otherwise nearest seed point.
import json, math, re
SEEDS = {
 'sa': {'Riyadh':[(24.71,46.68),(23.5,45.5),(21.5,46.5),(25.5,45.5),(20.5,45.5)], 'Makkah':[(21.42,39.83),(21.3,40.4),(22.5,39.2),(20.3,41.5),(21.0,42.3),(22.3,41.8)],
        'Madinah':[(24.47,39.61),(25.7,38.0),(24.1,38.06),(25.5,39.5),(26.6,37.9),(25.3,40.6)], 'Eastern Province':[(26.43,50.10),(25.38,49.59),(23.0,51.0),(20.5,51.5),(27.5,48.5),(28.4,46.2)],
        'Al-Qassim':[(26.33,43.97),(26.0,43.5),(26.6,42.8)], 'Hail':[(27.52,41.69),(27.0,40.5),(28.0,42.5)], 'Tabuk':[(28.38,36.57),(27.6,35.6),(29.0,35.5),(27.0,37.5),(28.0,37.5)],
        'Northern Borders':[(30.98,41.02),(30.5,42.5),(29.2,44.5),(31.5,39.0)], 'Al-Jawf':[(29.97,40.21),(31.3,37.4),(29.8,39.0),(28.8,40.5)], 'Jazan':[(16.89,42.55),(16.7,42.0),(17.3,43.0)],
        'Najran':[(17.49,44.13),(18.5,46.5),(17.8,48.5)], 'Asir':[(18.22,42.51),(19.0,43.2),(18.7,41.8),(19.9,44.0)], 'Al-Bahah':[(20.01,41.47),(19.85,41.3)]},
 'om': {'Muscat':[(23.59,58.4),(23.3,58.7)], 'Dhofar':[(17.02,54.09),(17.8,53.0),(18.5,53.8),(17.3,55.5)], 'Musandam':[(26.2,56.25),(25.6,56.3)], 'Al Buraimi':[(24.25,55.8),(23.7,55.6)],
        'Ad Dakhiliyah':[(22.93,57.53),(23.07,57.67),(22.5,57.3),(21.8,57.5)], 'North Al Batinah':[(24.35,56.7),(24.0,57.0),(24.9,56.3)], 'South Al Batinah':[(23.68,57.88),(23.39,57.42),(23.4,57.0)],
        'South Ash Sharqiyah':[(22.57,59.53),(22.0,59.6),(20.5,58.8),(21.5,59.2)], 'North Ash Sharqiyah':[(22.69,58.53),(22.2,58.6),(21.9,58.8)], 'Ad Dhahirah':[(23.22,56.51),(22.5,56.3),(23.6,56.0)],
        'Al Wusta':[(19.95,56.87),(19.6,57.7),(20.5,56.0),(18.9,56.5)]},
 'ae': {'Abu Dhabi':[(24.45,54.4),(24.2,55.75),(23.65,53.7),(23.1,53.6),(24.1,52.6),(24.3,54.6),(22.9,54.5),(24.4,55.4)], 'Dubai':[(25.2,55.27),(24.95,55.6),(24.8,55.3)],
        'Sharjah':[(25.35,55.4),(25.07,56.35),(25.34,56.35),(25.15,55.8),(25.0,55.7)], 'Ajman':[(25.4,55.48)], 'Umm Al Quwain':[(25.56,55.55),(25.45,55.75)],
        'Ras Al Khaimah':[(25.8,55.95),(25.95,56.1),(25.6,56.05)], 'Fujairah':[(25.12,56.33),(25.6,56.27),(25.35,56.2)]},
 'qa': {'Doha':[(25.29,51.53)], 'Al Rayyan':[(25.25,51.35),(24.95,51.1),(24.6,50.9)], 'Al Wakrah':[(25.17,51.6),(24.95,51.45),(24.65,51.3),(24.5,51.0)], 'Umm Salal':[(25.41,51.4)],
        'Al Khor':[(25.68,51.5),(25.6,51.3)], 'Al Shamal':[(26.1,51.2),(25.95,51.05)], 'Al Daayen':[(25.55,51.45)], 'Al Shahaniya':[(25.4,51.0),(25.4,50.8),(25.65,50.85),(25.1,50.85)]},
 'bh': {'Capital':[(26.22,50.58),(26.2,50.62)], 'Muharraq':[(26.25,50.61),(26.27,50.66),(26.3,50.6)], 'Northern':[(26.17,50.48),(26.2,50.5),(26.15,50.42)], 'Southern':[(25.95,50.55),(26.05,50.52),(25.8,50.6),(25.6,50.8),(26.0,50.62)]},
}
KEY = {'sa':{'Riyadh':['riyadh','kharj','dawadmi','diriyah','wadi al-dawasir','afif','tuwaiq'],'Makkah':['makkah','mecca','jeddah','taif','rabigh','thuwal','khulais'],'Madinah':['madinah','medina','alula','al-ula','hegra','khaybar','yanbu'],
       'Eastern Province':['eastern province','al-ahsa','al-hasa','hofuf','dammam','jubail','qatif','tarut','dhahran','khobar'],'Al-Qassim':['qassim','buraydah','unaizah'],'Hail':['hail','ha’il','jubbah','shuwaymis'],
       'Tabuk':['tabuk','duba','haql','neom','sharma','muwaylih','ifal','hisma','jabal al-lawz','umluj','al-wajh'],'Northern Borders':['northern borders','arar','rafha','turaif'],'Al-Jawf':['al-jawf','jawf','sakaka','dumat','domat','tabarjal'],
       'Jazan':['jazan','jizan','farasan','fifa'],'Najran':['najran','ukhdood','bir hima','hima','sharurah','rub'],'Asir':['asir','abha','khamis','rijal','soudah','tanomah','bisha'],'Al-Bahah':['al-bahah','al bahah','baha','mekhwa']}}
def km(a,b,c,d):
    p=math.radians;return 2*6371*math.asin(math.sqrt(math.sin(p(c-a)/2)**2+math.cos(p(a))*math.cos(p(c))*math.sin(p(d-b)/2)**2))
def region(cc, s):
    txt=(s.get('n','')+' '+s.get('s','')+' '+s.get('desc','')[:300]).lower()
    for r,ks in KEY.get(cc,{}).items():
        if any(k in txt for k in ks): return r, 'text'
    best=min(((km(s['lat'],s['lng'],a,b),r) for r,pts in SEEDS[cc].items() for a,b in pts))
    return best[1], 'nearest'
