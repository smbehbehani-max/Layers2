import json, sys
ICONS=set('shell boat mound platform well jar caravan island sword flame wall cliff mudvolc quake fault steam sinkhole wood fossil dune salt wave river delta bird crab mangrove oil gazelle plant dolphin map trench eye'.split())
REQ=['id','n','na','c','s','lat','lng','p','dr','el','ic','era','t0','t1','te','ta','se','sa','desc','sig','ex','disc','refs']
for cc in sys.argv[1:]:
    cfg=json.load(open(f'{cc}/config.json')); x0,y0,x1,y1=cfg['bbox']
    d=json.load(open(f'{cc}/data.json')); ids={s['id'] for s in d['sites']}
    more=json.load(open(f'{cc}/more.json'))['sites']; added=0; bad=[]
    for s in more:
        miss=[k for k in REQ if k not in s or s[k] in ('',None,[])]
        if miss: bad.append((s.get('id'),'missing',miss)); continue
        if s['id'] in ids: bad.append((s['id'],'dup')); continue
        if s['c'] not in ('archaeological','geological','ecology'): bad.append((s['id'],'cat',s['c'])); continue
        if s['ic'] not in ICONS: bad.append((s['id'],'icon',s['ic'])); s['ic']='map'
        if s['era'] not in 'DPHN': bad.append((s['id'],'era',s['era'])); s['era']='?'
        if not (x0<=s['lng']<=x1 and y0<=s['lat']<=y1): bad.append((s['id'],'bbox',s['lat'],s['lng'])); continue
        if s['t0']<s['t1']: s['t0'],s['t1']=s['t1'],s['t0']
        if 'Persian' in json.dumps(s,ensure_ascii=False): bad.append((s['id'],'persian'))
        d['sites'].append({k:s[k] for k in REQ}); ids.add(s['id']); added+=1
    json.dump(d,open(f'{cc}/data.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
    print(cc,'added',added,'total',len(d['sites']),'issues',bad)
