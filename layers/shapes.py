import json, math
G=json.load(open('/tmp/nev/geojson/ne_10m_admin_0_countries.geojson'))
ISO={'KWT':'kw','SAU':'sa','BHR':'bh','QAT':'qa','ARE':'ae','OMN':'om'}
K=math.cos(math.radians(24))
def dp(pts,eps):
    if len(pts)<3:return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1];dx,dy=x2-x1,y2-y1;L=math.hypot(dx,dy) or 1e-9
    im,dm=0,-1
    for i in range(1,len(pts)-1):
        x,y=pts[i];d=abs(dy*x-dx*y+x2*y1-y2*x1)/L
        if d>dm:im,dm=i,d
    if dm>eps:
        a=dp(pts[:im+1],eps);b=dp(pts[im:],eps);return a[:-1]+b
    return [pts[0],pts[-1]]
out={}
for f in G['features']:
    p=f['properties'];iso=p.get('ISO_A3');adm=p.get('ADM0_A3')
    cc=ISO.get(iso) or ISO.get(adm)
    if not cc:continue
    g=f['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    rings=[]
    for poly in polys:
        for ring in poly[:1]:
            pts=[(x*K,-y) for x,y in ring]
            e=0.015 if cc in('kw','bh','qa') else 0.03;m=len(pts)//2
            s=dp(pts[:m+1],e)[:-1]+dp(pts[m:],e)
            if len(s)>=4:rings.append(s)
    out[cc]=rings
# bounds
xs=[x for r in out.values() for ring in r for x,y in ring];ys=[y for r in out.values() for ring in r for x,y in ring]
x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
print(x0,x1,y0,y1)
S=1000/(x1-x0)
paths={cc:''.join('M'+' L'.join(f'{(x-x0)*S:.1f} {(y-y0)*S:.1f}' for x,y in ring)+'Z' for ring in rings) for cc,rings in out.items()}
json.dump({'paths':paths,'w':1000,'h':(y1-y0)*S,'x0':x0,'y0':y0,'S':S,'K':K},open('gulf_map.json','w'))
print({k:len(v) for k,v in paths.items()},(y1-y0)*S)
