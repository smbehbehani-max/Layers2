"""Build a Layers edition for a Gulf country from the Kuwait template (tpl3.html).
usage: python3 edition.py <cc>   (reads /tmp/w/gulf/<cc>/config.json and data.json, writes /tmp/w/gulf/<cc>/site/)"""
import json, re, runpy, sys, os, shutil
cc = sys.argv[1]
D = f'/tmp/w/gulf/{cc}'
C = json.load(open(f'{D}/config.json', encoding='utf-8'))
data = json.load(open(f'{D}/data.json', encoding='utf-8'))
data.setdefault('stops', [])
for s in data['sites']:
    assert 't0' in s and 't1' in s and 'ic' in s and 'era' in s and s.get('te') and s.get('ta'), s['id']
    s.setdefault('refs', []); s.setdefault('disc', [])
    for k in ('conf', 'ev', 'an', 'val', 'ex', 'el', 'sig', 'dr', 'p', 'na', 'se', 'sa', 's'):
        s.setdefault(k, '')

# ---- country outline from Natural Earth 10m ----
ne = json.load(open('/tmp/nev/geojson/ne_10m_admin_0_countries.geojson'))
feat = [f for f in ne['features'] if f['properties'].get('ADM0_A3') == C['iso'] or f['properties'].get('ISO_A3') == C['iso']]
assert feat, C['iso']
geom = feat[0]['geometry']
polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
rings = []
for poly in polys:
    outer = poly[0]
    if 'bbox' in C:  # optional crop of far-away pieces
        x0, y0, x1, y1 = C['bbox']
        if not any(x0 <= p[0] <= x1 and y0 <= p[1] <= y1 for p in outer): continue
    rings.append([[round(p[0], 4), round(p[1], 4)] for p in outer])
for extra in C.get('extra_rings', []): rings.append(extra)
kw = json.dumps(rings, separators=(',', ':'))
# normalised 100x100 path for the How-it-works icon (largest ring only)
big = max(rings, key=len)
xs = [p[0] for p in big]; ys = [p[1] for p in big]
mx, Mx, my, My = min(xs), max(xs), min(ys), max(ys)
sc = 100 / max(Mx - mx, My - my)
hw = 'M' + 'L'.join(f'{(p[0]-mx)*sc:.1f} {(My-p[1])*sc:.1f}' for p in big[::max(1, len(big) // 160)]) + 'Z'

h = open('/tmp/w/tpl3.html', encoding='utf-8').read()

def rep(old, new, n=1):
    global h
    c = h.count(old)
    assert c == n, (c, old[:80])
    h = h.replace(old, new)

def block(start, end_pat, new):
    """replace from the line starting with `start` up to and including the first line matching end_pat."""
    global h
    i = h.index('\n' + start) + 1
    j = h.index(end_pat, i) + len(end_pat)
    h = h[:i] + new + h[j:]

# stories, AI stories, art: none in a first edition
block('const STORIES=[', '\n];', 'const STORIES=__STORIESJS__;')
h = h.replace('</style>', '__HIDECSS__</style>', 1)
block('const ROUTE=[', '].map(a=>({id:a[0],te:a[1],ta:a[2],le:a[3],la:a[4]}));', 'const ROUTE=' + json.dumps(C['route'], ensure_ascii=False) + '.map(a=>({id:a[0],te:a[1],ta:a[2],le:a[3],la:a[4]}));')
block('const PZ=[', '}];', 'const PZ=' + json.dumps(C.get('protected', []), ensure_ascii=False) + ';')
# map labels, city, latitude scale, graticule
block('const LABELS=[', '];', 'const LABELS=' + json.dumps(C['labels'], ensure_ascii=False) + ';')
rep("const cx=px(47.978),cy=py(29.369);", f"const cx=px({C['city'][0]}),cy=py({C['city'][1]});")
rep("const K=Math.cos(29.4*Math.PI/180),pad=.05;", f"const K=Math.cos({C['lat0']}*Math.PI/180),pad={C.get('pad', .05)};")
rep("+pad+.35,Y0=", f"+pad+{C.get('padr', .35)},Y0=")
rep("l=Math.ceil(X0*4)/4;l<=X1;l+=.25", f"l=Math.ceil(X0/{C['gstep']})*{C['gstep']};l<=X1;l+={C['gstep']}")
rep("l=Math.ceil(Y0*4)/4;l<=Y1;l+=.25", f"l=Math.ceil(Y0/{C['gstep']})*{C['gstep']};l<=Y1;l+={C['gstep']}")
rep("data-s=\"gx\">${l.toFixed(2)}°E", "data-s=\"gx\">${(+l.toFixed(3))}°E")
rep("data-s=\"gy\">${l.toFixed(2)}°N", "data-s=\"gy\">${(+l.toFixed(3))}°N")
# water/label strings: replace the whole water objects
for lang in ('en', 'ar'):
    m = re.search(r"water:\{[^}]*\}", h[h.index(f"\n{lang}:{{title:"):])
    h = h.replace(m.group(0), 'water:' + json.dumps(C['water'][lang], ensure_ascii=False), 1)
# timeline milestones stay; subtitles
rep("<title>Layers of Kuwait</title>", f"<title>{C['title_en']}</title>")
rep('aria-label="Map of Kuwait"', f'aria-label="Map of {C["en"]}"')
# names everywhere in UI strings (HW/INS/about/mail/soon/PZT)
h = h.replace('Layers of Kuwait', C['title_en']).replace('طبقات الكويت', C['title_ar'])
h = h.replace("back:'Back to Kuwait'", f"back:'Back to {C['en']}'").replace("back:'العودة إلى الكويت'", f"back:'العودة إلى {C['ar']}'")
rep("made:'Made in Kuwait'", f"made:'Made in {C['en']}'"); rep("made:'صُنع في الكويت'", f"made:'صُنع في {C['ar']}'")
rep("src:'Source: Environment Public Authority (Kuwait)'", f"src:'Source: {C['pa_source_en']}'")
m = re.search(r"src:'المصدر: [^']*'", h); h = h.replace(m.group(0), f"src:'المصدر: {C['pa_source_ar']}'", 1)
h = h.replace('Check with the Environment Public Authority before visiting', f"Check with {C['pa_auth_en']} before visiting").replace('Entry by permit from the Environment Public Authority', f"Entry by permit from {C['pa_auth_en']}")
# subtitle lines of the header and about text
for k, v in C['strings'].items():
    assert k in h, k[:60]
    h = h.replace(k, v)
# logos: this country active; Kuwait becomes an "available" link
h = h.replace('data-lg="kw" class="lg on"', 'data-lg="kw" class="lg"') if 'data-lg="kw" class="lg on"' in h else h
LGN_KW = "kw:{iso:'KWT',en:'Kuwait',t:'Layers of Kuwait',ar:'الكويت',url:'https://smbehbehani-max.github.io/Layers2/'}"
rep("const LGN={sa:", "const LGN={" + LGN_KW + ",sa:")
h = h.replace("const LGN={" + LGN_KW + ",sa:", "const LGN={" + LGN_KW + ",sa:")
# remove own country from LGN so clicking it does nothing special
h = re.sub(r",?%s:\{iso:'%s'[^}]*\}" % (cc, C['iso']), '', h, 1)
rep("const HWKW=\"__HWKW__\";", f"const HWKW=\"{hw}\";")
rep("const SHARE_BASE=STANDALONE?location.href.split(/[?#]/)[0]:'https://smbehbehani-max.github.io/Layers2/';",
    f"const SHARE_BASE=STANDALONE?location.href.split(/[?#]/)[0]:'{C['base']}';")
h = h.replace("https://smbehbehani-max.github.io/Layers2/", C['base'])
h = h.replace("github.com/smbehbehani-max/Layers2", "github.com/smbehbehani-max/" + C['repo'])

# ---- home country for the brand logic ----
rep("let actC='kw';const ORDER=['kw','sa','bh','qa','ae','om'];", f"const HOMEC='{cc}';let actC=HOMEC;const ORDER=['{cc}','kw','sa','bh','qa','ae','om'].filter((x,i,a)=>a.indexOf(x)==i);")
rep("function applyBrand(){if(actC=='kw')return;", "(function(){const row=$('#brandrow'),nav=row.querySelector('.lgs'),kb=row.querySelector('.lg[data-lg=\"kw\"]'),cb=row.querySelector('.lg[data-lg=\"'+HOMEC+'\"]');if(cb&&kb){row.insertBefore(cb,row.firstChild);nav.insertBefore(kb,nav.firstChild)}})();\nfunction applyBrand(){if(actC==HOMEC)return;")
rep(" if(k=='kw'){const t=L();", " if(k==HOMEC){const t=L();")
rep("function goHome(){closeSoon(true);setActive('kw');", "function goHome(){closeSoon(true);setActive(HOMEC);")
rep("if(!keep&&actC!='kw')setActive('kw')}", "if(!keep&&actC!=HOMEC)setActive(HOMEC)}")
rep("b.dataset.lg=='kw'?goHome():openSoon(b.dataset.lg)", "b.dataset.lg==HOMEC?goHome():openSoon(b.dataset.lg)")
rep("<h2>${E(lang=='ar'?'طبقات '+c.ar:c.t)}</h2><div class=\"soon-pill\">${E(T.soon)}</div><p>${E(T.p(lang=='ar'?c.ar:c.en))}</p>",
    "<h2>${E(lang=='ar'?'طبقات '+c.ar:c.t)}</h2>${c.url?`<div class=\"soon-pill\" style=\"background:var(--gold);color:#1a2a2b\">${E(T.avail)}</div><p>${E(T.pa(lang=='ar'?c.ar:c.en))}</p><a class=\"back\" style=\"display:inline-block;text-decoration:none;margin:0 6px 12px 0\" href=\"${c.url}\" target=\"_blank\" rel=\"noopener\">${E(T.open)}</a>`:`<div class=\"soon-pill\">${E(T.soon)}</div><p>${E(T.p(lang=='ar'?c.ar:c.en))}</p>`}")
rep("const SOONT={en:{soon:'Coming soon',", "const SOONT={en:{avail:'Available now',open:'Open Layers of Kuwait',pa:n=>`${n} is already mapped: 80 places with their sources, stories and a timeline.`,soon:'Coming soon',")
m2 = re.search(r"ar:\{soon:'[^']*',", h); h = h.replace(m2.group(0), m2.group(0).replace("ar:{", "ar:{avail:'متاح الآن',open:'افتح طبقات الكويت',pa:n=>`${n} مرسومة بالفعل: 80 موقعًا بمصادرها وقصصها وخط زمني.`,"), 1)
rep("function applyBrand(){if(actC==HOMEC)return;const c=LGN[actC];", "function applyBrand(){if(actC==HOMEC)return;const c=LGN[actC];")

open(f'{D}/_tpl.html', 'w', encoding='utf-8').write(h)

# ---- fill placeholders (same as build2) ----
SYMS = runpy.run_path('/tmp/w/icons.py')['SYMS']
SB = runpy.run_path('/tmp/w/gulf/stories_build.py')['build'](cc, data)   # adds speculative records to data
js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
hide = '#stb{display:none!important}.chip.ai{display:none!important}' if SB['stories'] == '[]' else ''
out = (h.replace('__STORIESJS__', SB['stories']).replace('__HIDECSS__', hide)
       .replace('__AISTORIES__', json.dumps(SB['ai'], ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')).replace('__STORYART__', json.dumps(SB['art'], ensure_ascii=False)).replace('__STORYDEFS__', SB['defs'])
       .replace('__ART__', json.dumps(SB['card'], ensure_ascii=False)).replace('__SYMBOLS__', SYMS).replace('__DATA__', js).replace('__KW__', kw)
       .replace('__GULF__', open('/tmp/w/gulf_shapes.json').read())
       .replace('__LOGO__', open('/tmp/w/logo_inline.svg').read().replace('__BRAND__', '<div class="brand"><h1><span id="t-title"></span><span id="t-short"></span></h1><span id="t-sub"></span></div>')))
assert '__' + 'HWKW__' not in out
# active logo: move the .on class to this country
out = out.replace('<button class="lg on" data-lg="kw"', '<button class="lg" data-lg="kw"')
out = out.replace(f'<button class="lg" data-lg="{cc}"', f'<button class="lg on" data-lg="{cc}"')
assert out.count('class="lg on"') == 1
open(f'{D}/app.html', 'w', encoding='utf-8').write(out)
print('built', f'{D}/app.html', len(out), 'sites', len(data['sites']), 'rings', len(rings))
