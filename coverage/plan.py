import json,math,collections,sys
sys.path.insert(0,'/tmp/w/coverage'); from regions import region,SEEDS
out={};Q={}
for cc in ['sa','om','ae','qa','bh']:
    S=[s for s in json.load(open(f'/tmp/w/gulf/{cc}/data.json',encoding='utf-8'))['sites'] if s['c']!='speculative']
    U=json.load(open(f'missing_units_{cc}.json',encoding='utf-8')); names=list(SEEDS[cc])
    def norm(r):
        r=(r or '').lower()
        for n in names:
            if n.lower().replace('al-','').replace('al ','').split()[0] in r: return n
    G={n:collections.Counter() for n in names}
    for s in S: G[region(cc,s)[0]][s['c']]+=1
    for u in U:
        n=norm(u.get('region'))
        if n: G[n][u['layer']]+=1
    short={n:max(0,6-sum(G[n].values())) for n in names}; sh=sum(short.values())
    lay=collections.Counter(s['c'] for s in S)+collections.Counter(u['layer'] for u in U); after=sum(lay.values())
    E=sh
    while True:
        N=after+E; nG=max(0,math.ceil(.25*N)-lay['geological']); nA=max(0,math.ceil(.38*N)-lay['archaeological'])
        if nG+nA<=E: break
        E+=1
    out[cc]=dict(now=len(S),musthave=len(U),after=after,extra=E,final=after+E,geo_extra=nG,arch_extra=nA,free=E-nG-nA,layers_final={'archaeological':lay['archaeological']+nA,'geological':lay['geological']+nG,'ecology':lay['ecology']})
    slots=['geological']*nG+['archaeological']*nA+['any']*(E-nG-nA)
    add={n:collections.Counter() for n in names}; tot=lambda n:sum(G[n].values())+sum(add[n].values())
    cap={'Ajman':6,'Umm Al Quwain':7}
    for n in names:
        while tot(n)<6 and slots:
            L=sorted(['geological','archaeological','any'],key=lambda L:(L not in slots, G[n][L]+add[n][L] if L!='any' else 99))[0]; slots.remove(L); add[n][L]+=1
    for L in list(slots):
        n=min([n for n in names if tot(n)<cap.get(n,99)],key=lambda n:(G[n][L]+add[n][L] if L!='any' else tot(n), tot(n)))
        add[n][L]+=1
    Q[cc]={n:{'now':dict(G[n]),'add':dict(add[n])} for n in names}
    print(cc,out[cc])
json.dump(out,open('plan2.json','w'),indent=1); json.dump(Q,open('quotas.json','w'),indent=1)
