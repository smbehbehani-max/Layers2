# usage: python3 ingest.py <cc> <file.json> [--apply]
import json,sys,math,re
cc,f=sys.argv[1],sys.argv[2]; apply='--apply' in sys.argv
ICONS=set('shell boat mound platform well jar caravan island sword flame wall cliff mudvolc quake fault steam sinkhole wood fossil dune salt wave river delta bird crab mangrove oil gazelle plant dolphin map trench eye'.split())
BB={'sa':(16,32.5,34,56),'om':(16.5,26.6,51.9,60),'ae':(22.5,26.3,51.4,56.5),'qa':(24.4,26.3,50.6,51.8),'bh':(25.5,27.0,50.3,51.0)}
REQ='id n na c ic era s lat lng p dr el t0 t1 te ta se sa desc sig ex disc refs conf'.split()
P=f'/tmp/w/gulf/{cc}/data.json'; D=json.load(open(P,encoding='utf-8'))
km=lambda a,b,c,d:2*6371*math.asin(math.sqrt(math.sin(math.radians(c-a)/2)**2+math.cos(math.radians(a))*math.cos(math.radians(c))*math.sin(math.radians(d-b)/2)**2))
N=json.load(open(f,encoding='utf-8')); ok=[]; ids={s['id'] for s in D['sites']}
for r in N:
    pb=[k for k in REQ if k not in r or r[k] in (None,'') and k not in ('conf','el')]
    if pb: print('SKIP missing',r.get('id'),pb); continue
    if r['ic'] not in ICONS: print('fix icon',r['id'],r['ic']); r['ic']={'archaeological':'wall','geological':'cliff','ecology':'plant'}[r['c']]
    if r['c'] not in ('archaeological','geological','ecology') or r['era'] not in 'DPHN': print('SKIP bad c/era',r['id']); continue
    la,lo=float(r['lat']),float(r['lng']); b=BB[cc]
    if not(b[0]<=la<=b[1] and b[2]<=lo<=b[3]): print('SKIP out of country',r['id'],la,lo); continue
    if r['id'] in ids: print('SKIP id exists',r['id']); continue
    near=[(round(km(la,lo,s['lat'],s['lng']),2),s['id']) for s in D['sites'] if km(la,lo,s['lat'],s['lng'])<1.0]
    if near: print('CHECK near',r['id'],near)
    r['t0'],r['t1']=float(r['t0']),float(r['t1'])
    if r['t0']<r['t1']: r['t0'],r['t1']=r['t1'],r['t0']
    for k in ('na','ta','sa'):
        r[k]=r[k].replace('"','«').replace("'",'’')
    ok.append(r); ids.add(r['id'])
print(cc,'valid',len(ok),'of',len(N))
if apply:
    import shutil; shutil.copy(P,P+'.bak-ingest')
    D['sites'].extend(ok); json.dump(D,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('applied; total',len(D['sites']))
