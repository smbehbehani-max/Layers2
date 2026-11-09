import json,re,runpy,sys
sys.path.insert(0,'/tmp/w')
SYMS=runpy.run_path('/tmp/w/icons.py')['SYMS']
d=json.load(open('/tmp/w/data2.json'))
AG=runpy.run_path('/tmp/w/ages.py')['G']
SPM=runpy.run_path('/tmp/w/spec.py'); A3=runpy.run_path('/tmp/w/story_art3.py')
P=lambda en,ar:{'en':en,'ar':ar}

# ---- AI speculation layer: enrich the 5 shape-based records, add the cross-category ones, build their stories
byid={s['id']:s for s in d['sites']}
AISTORIES=[]
for sp in SPM['SPEC']:
    sid=sp['id']
    if sp.get('new'):
        rec=dict(id=sid,n=sp['n'],c='speculative',s=sp['s'],lat=sp['lat'],lng=sp['lng'],p=sp['p'],dr=sp['dr'],el='',desc=sp['desc'],
                 sig=sp['sig'],ex='',conf='',ev=sp['ev'],an=sp['an'],val=sp['val'],disc=sp['dlist'],refs=sp['refs'],ic='spark',era='?',
                 te=sp['te'],ta=sp['ta'],se=sp['se'],sa=sp['sa'],na=sp['na'])
        d['sites'].append(rec); byid[sid]=rec; AG[sid]=sp['ages']
    else:
        rec=byid[sid]
        rec['an']=rec['an'].rstrip()+sp['an_add']
        refs=[r for r in rec['refs'] if 'AI Analysis' not in r]
        refs=[r.replace('Rutkowski, J. & Kiersnowski','Rutkowski, Ł. & Kiersnowski') for r in refs]
        rec['refs']=refs+[r for r in sp['addrefs'] if r not in refs]
    rec['conf']='Untested AI speculation (shape seen on satellite imagery)' if sp['bas']=='shape' else 'Untested AI speculation (connection between published records)'
    key=sp['key']; st=sp['story']
    rec['spec']=dict(bas=sp['bas'],key=key,sty='ai-'+key,spot=sp['spot'],lk=sp['lk'],pred=sp['pred'],test=sp['test'],wrong=sp['wrong'])
    AISTORIES.append(dict(id='ai-'+key,kind='ai',disc=sp['disc'],cover=f'x-{key}-0',color='#7b3fb8',sites=[sid],mapSite=sid,
        title=st['title'],tag=st['tag'],refs=[{'label':r,'url':SPM['U'].get(r,'')} for r in st['refs']],
        pages=[{'art':f'x-{key}-0','cover':1},
               {'art':f'x-{key}-1','h':P('The clue','الدليل'),'p':st['p1']},
               {'art':f'x-{key}-2','h':st['h2'],'p':st['p2']},
               {'cmap':sid,'h':P('Connecting the dots','صِل النقاط'),'p':st['p3']},
               {'art':f'x-{key}-4','h':P('The prediction','التوقّع'),'pred':sid}]))
for sp in SPM['SPEC']:
    for l in sp['lk']: assert l[0] in byid, (sp['id'],l[0])

for s in d['sites']:
    s['t0'],s['t1']=AG[s['id']]
    for k in ['ad']: s.pop(k,None)
js=json.dumps(d,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
kw=open('/tmp/w/kw_rings.json').read()
ART=runpy.run_path('/tmp/w/art.py')['ART']
_w=lambda body:f'<svg viewBox="0 0 400 220" aria-hidden="true">{body}</svg>'
for _m in ('art_a','art_g','art_e'):
    for _k,_v in runpy.run_path(f'/tmp/w/{_m}.py')['A'].items(): ART[_k]=_w(_v)
SM=runpy.run_path('/tmp/w/story_art.py')
SM['ART'].update(runpy.run_path('/tmp/w/story_art2.py')['ART'])
SM['ART'].update(A3['ART'])
aij=json.dumps(AISTORIES,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
h=open('/tmp/w/tpl2.html',encoding='utf-8').read().replace('__AISTORIES__',aij).replace('__STORYART__',json.dumps(SM['ART'],ensure_ascii=False)).replace('__STORYDEFS__',SM['DEFS']+A3['DEFS']).replace('__ART__',json.dumps(ART,ensure_ascii=False)).replace('__SYMBOLS__',SYMS).replace('__DATA__',js).replace('__KW__',kw).replace('__GULF__',open('/tmp/w/gulf_shapes.json').read()).replace('__LOGO__',open('/tmp/w/logo_inline.svg').read().replace('__BRAND__','<div class="brand"><h1><span id="t-title"></span><span id="t-short"></span></h1><span id="t-sub"></span></div>')).replace('__HWKW__',open('/tmp/w/kwpath.txt').read())
open('/mnt/user-data/outputs/kuwait-geoheritage-explorer.html','w').write(h)
open('/tmp/w/chk.js','w').write(re.search(r'<script>(.*)</script>',h,re.S).group(1))
used={s['ic'] for s in d['sites']}; G=runpy.run_path('/tmp/w/icons.py')['G']
print(len(h),'sites',len(d['sites']),'missing glyphs',used-set(G),'art',len(ART),'missing art',[s['id'] for s in d['sites'] if s['id'] not in ART and 'spec' not in s])
