import json,re,math,collections
def km(a,b,c,d):
    p=math.radians;return 2*6371*math.asin(math.sqrt(math.sin(p(c-a)/2)**2+math.cos(p(a))*math.cos(p(c))*math.sin(p(d-b)/2)**2))
def prop(m):
    d=m.get('designation') or ''
    if m['group'] in ('WHS','Tentative'):
        r=re.search(r'(?:ref\.?|ID|no\.?)\s*(\d{3,4})',d) or re.search(r'\b(\d{3,4})(?:rev|bis|ter)?-\d{3}',d) or re.search(r'component[^()]*? of ([^,;()]+)',d)
        if r: return m['group']+':'+r.group(1).strip().lower()
    if re.search(r'geopark',d,re.I) and m['group']=='Geosite':
        g=re.search(r'(Salma|North Riyadh|Thadiq|Al Hajar|Hajar)',d,re.I); return 'GP:'+(g.group(1).lower() if g else 'x')
    return 'S:'+m['name'].lower()
def units(cc):
    M=[m for m in json.load(open(f'/tmp/w/coverage/musthave_{cc}.json',encoding='utf-8')) if m.get('confidence')!='low']
    P=collections.defaultdict(list)
    for m in M: P[prop(m)].append(m)
    out=[]
    for k,rows in P.items():
        have=[r for r in rows if r.get('in_app') not in (None,'None','')]
        if k.startswith('GP:'):
            need=max(0,5-len(have)); miss=[r for r in rows if r not in have][:need]
            out+= [dict(r,_unit=k,_why='geopark flagship geosite') for r in miss]; continue
        if k.startswith('S:'):
            if not have: out.append(dict(rows[0],_unit=k,_why='designated site'))
            continue
        # serial property
        if not have and not k.startswith('WHS'):
            # Tentative entry with nothing in app: one spot per region
            seen=set()
            for r in rows:
                if r.get('region') not in seen: seen.add(r.get('region')); out.append(dict(r,_unit=k,_why='tentative entry (one spot per region)'))
            continue
        kept=[r for r in have if r.get('lat')]
        for r in rows:
            if r in have: continue
            if k.startswith('WHS'):
                if r.get('lat') and all(km(r['lat'],r['lng'],q['lat'],q['lng'])>=5 for q in kept):
                    out.append(dict(r,_unit=k,_why='World Heritage component ≥5 km from others')); kept.append(r)
                elif not have and not out or (not r.get('lat') and not have):
                    out.append(dict(r,_unit=k,_why='World Heritage property'))
            else:
                if r.get('region') not in {q.get('region') for q in have}|{q.get('region') for q in out if q['_unit']==k}:
                    out.append(dict(r,_unit=k,_why='tentative component in a new region'))
    return out
