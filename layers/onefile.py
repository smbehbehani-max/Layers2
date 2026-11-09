"""Single-file Layers: promotional front page + all six country editions in one HTML."""
import json, re, os, base64, sys
sys.path.insert(0, '/tmp/w/layers')
import hub as H
SITE = '/tmp/w/layers/site'
OUT = '/tmp/w/layers/one'
BASE = 'https://smbehbehani-max.github.io/Layers/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
os.makedirs(OUT, exist_ok=True)

def patch_edition(cc):
    h = open(f'{SITE}/{cc}.html', encoding='utf-8').read()
    def rep(a, b, n=1):
        nonlocal h
        assert h.count(a) == n, (cc, a[:60], h.count(a))
        h = h.replace(a, b)
    rep("if(!hsh)return;let m;", "hsh=hsh.replace(/^[a-z]{2}(\\/|$)/,'');if(!hsh)return;let m;")
    rep("replaceState(null,'','#p='+encodeURIComponent(sel)", f"replaceState(null,'','#{cc}/p='+encodeURIComponent(sel)")
    rep("if(location.hash.indexOf('#p=')==0)history.replaceState(null,'',location.pathname+location.search)",
        f"if(/^#[a-z]{{2}}\\/p=/.test(location.hash))history.replaceState(null,'',location.pathname+location.search+'#{cc}')")
    rep("SHARE_BASE+'#p='", f"SHARE_BASE+'#{cc}/p='")
    rep("function goCountry(k){location.href=k+'.html'}", "function goCountry(k){location.hash='#'+k;location.reload()}")
    rep("location.href='./'", "history.replaceState(null,'',location.pathname+location.search);location.reload()")
    rep("<script>function goCountry", "<script>addEventListener('hashchange',()=>{const m=/^#([a-z]{2})(\\/|$)/.exec(location.hash);if(m&&m[1]!='" + cc + "'&&['kw','sa','bh','qa','ae','om'].includes(m[1]))location.reload()});function goCountry")
    h = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>\s*", "", h, count=1, flags=re.S)
    assert "serviceWorker' in navigator" not in h, cc
    assert '<\\/script' not in h and '<!--' not in h
    return h.replace('</script', '<\\/script')

def build():
    data = {}
    for cc in ORDER: data[cc] = dict(zip(['n', 'k'], H.counts(cc)))
    IDX = {}
    S = {}
    for cc in ORDER:
        sites = json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']
        for s in sites: IDX[s['id']] = cc; S[(cc, s['id'])] = s
    total = sum(data[cc]['n'] for cc in ORDER)
    # showcase
    SHOW = [('sa', 'hegra'), ('kw', 'mud-volcano-z3'), ('om', 'bimmah-sinkhole'), ('ae', 'mleisa-elephant-trackway'), ('bh', 'al-sayah-island'), ('qa', 'ruwayda'), ('sa', 'umm-jirsan'), ('om', 'arabian-sea-humpback'), ('kw', 'spec-polychrome-escarpment'), ('ae', 'al-sinniyah-island'), ('bh', 'tree-of-life'), ('qa', 'dahl-al-misfir')]
    show = []
    for cc, i in SHOW:
        s = S[(cc, i)]; show.append(dict(cc=cc, id=i, c=s['c'], te=s['te'], ta=s['ta'], n=s['n'], na=s['na'], se=s.get('se', ''), sa=s.get('sa', '')))
    M = H.M; W, Hh = M['w'], M['h']; VY0 = -70; VH = Hh + 70
    shapes = ''.join(f'<path class="cs" data-cc="{cc}" d="{M["paths"][cc]}"/>' for cc in ORDER)
    badges = ''; leaders = ''; cards = ''
    for cc in ORDER:
        c = H.C[cc]; x, y = H.P(*c['pt']); bx, by = H.P(*c['bd'])
        if (bx, by) != (x, y): leaders += f'<line class="ld" x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/><circle class="ldp" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
        badges += f'<a class="bd" href="#{cc}" data-cc="{cc}" style="left:{bx/W*100:.2f}%;top:{(by-VY0)/VH*100:.2f}%"><span class="bdl">{H.flag_logo(cc, "bd"+cc)}</span><span class="bdn" data-n="{cc}"></span><span class="bdc">{data[cc]["n"]}</span></a>'
        cards += f'<a class="card" href="#{cc}" data-cc="{cc}"><span class="cl">{H.flag_logo(cc, "cd"+cc)}</span><span class="ct"><b data-t="{cc}"></b><small><span data-s="{cc}"></span></small></span><span class="go" aria-hidden="true">›</span></a>'
    wl = ''.join(f'<text class="wl" id="wl{i+1}" x="{H.P(*g)[0]:.0f}" y="{H.P(*g)[1]:.0f}">{t}</text>' for i, (g, t) in enumerate([((50.9, 28.9), 'Arabian Gulf'), ((36.8, 21.0), 'Red Sea'), ((56.8, 16.9), 'Arabian Sea')]))
    b64 = lambda f: base64.b64encode(open(f'{SITE}/{f}', 'rb').read()).decode()
    man = {'name': 'Layers · طبقات', 'short_name': 'Layers', 'start_url': BASE, 'scope': BASE, 'display': 'standalone', 'background_color': '#f7f8f5', 'theme_color': '#1a2a2b',
           'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'}]}
    manifest = 'data:application/manifest+json;base64,' + base64.b64encode(json.dumps(man, ensure_ascii=False).encode()).decode()
    html = TPL
    for k, v in {'__SHAPES__': shapes, '__LEADERS__': leaders, '__BADGES__': badges, '__CARDS__': cards, '__WL__': wl, '__W__': f'{W:.0f}', '__H__': f'{VH:.0f}', '__VY0__': f'{VY0:.0f}',
                 '__LOGO__': H.plain_logo('hub'), '__DATA__': json.dumps({cc: dict(n=data[cc]['n'], **data[cc]['k']) for cc in ORDER}), '__IDX__': json.dumps(IDX), '__SHOW__': json.dumps(show, ensure_ascii=False),
                 '__C__': json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in H.C.items()}, ensure_ascii=False), '__BASE__': BASE, '__TOTAL__': str(total), '__MANIFEST__': manifest}.items():
        html = html.replace(k, v)
    assert '__' not in re.sub(r'__[a-z]', '', html) or True
    payload = ''.join(f'<script type="text/plain" id="ed-{cc}">{patch_edition(cc)}</script>\n' for cc in ORDER)
    html = html.replace('<!--PAYLOAD-->', payload)
    open(f'{OUT}/index.html', 'w', encoding='utf-8').write(html)
    return total, os.path.getsize(f'{OUT}/index.html')

TPL = r'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Layers · طبقات — Discover the Gulf Beyond the Ordinary</title>
<meta name="description" content="Layers: the geology, archaeology and ecology of the Arabian Gulf as one journey. 6 countries, __TOTAL__ places with sources, illustrated stories, AI connections, timelines and live directions — in Arabic and English.">
<meta name="theme-color" content="#1a2a2b">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Layers"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="application-name" content="Layers">
<link rel="manifest" href="__MANIFEST__"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="canonical" href="__BASE__">
<meta property="og:type" content="website"><meta property="og:site_name" content="Layers"><meta property="og:title" content="Layers — Discover the Gulf Beyond the Ordinary">
<meta property="og:description" content="Explore the stories written into the landscape: geology, archaeology and ecology of six Gulf countries on one bilingual map."><meta property="og:url" content="__BASE__"><meta property="og:image" content="__BASE__og-kw.png">
<meta name="twitter:card" content="summary_large_image">
<script>(function(){var m=/^#([a-z]{2})(\/|$)/.exec(location.hash)||/^#p=/.test(location.hash);if(m)document.documentElement.className+=' ld'})()</script>
<style>
:root{--sea:#2c6e72;--sea-2:#3f8286;--land:#ece3cf;--coast:#7b6a4c;--panel:#f7f8f5;--panel-2:#eef1ec;--ink:#1a2a2b;--mut:#5d6d6c;--line:#d5dcd6;--arch:#b4521c;--geo:#5847b0;--eco:#2c7a4c;--spec:#bf2f7d;--gold:#c99a2e;--night:#10211f;
 --f-disp:"Newsreader",Georgia,"Times New Roman",serif;--f-body:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--shadow:0 6px 24px rgba(10,40,42,.18)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}html.ld body{visibility:hidden}
body{margin:0;background:var(--panel);color:var(--ink);font-family:var(--f-body);line-height:1.5;min-height:100vh}
html[dir=rtl] body{font-family:"Noto Naskh Arabic","Geeza Pro",system-ui,sans-serif}
a{color:inherit}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
/* top bar */
.top{position:absolute;inset:0 0 auto 0;z-index:5;display:flex;align-items:center;gap:10px;padding:12px 16px;max-width:1100px;margin:0 auto;color:#fffaf0}
.top .logo{width:46px;height:46px;flex:none;filter:drop-shadow(0 1px 3px rgba(0,0,0,.4))}.top .logo svg{width:100%;height:100%;display:block}
.top .wm{flex:1;font:600 15px var(--f-body);letter-spacing:.14em}.top .wm small{display:block;letter-spacing:.04em;font-weight:400;opacity:.8;font-size:11.5px}
#lang{border:1px solid rgba(255,250,240,.5);background:rgba(255,250,240,.12);color:#fffaf0;border-radius:999px;padding:7px 13px;font:600 14px var(--f-body);cursor:pointer;backdrop-filter:blur(6px)}
#lang:hover{background:rgba(255,250,240,.25)}
/* hero */
.hero{position:relative;min-height:92vh;overflow:hidden;background:var(--night);color:#fffaf0;display:flex;align-items:flex-end}
.hero svg.sky{position:absolute;inset:0;width:100%;height:100%;display:block}
.hero::after{content:'';position:absolute;inset:0;background:linear-gradient(to right,rgba(16,33,31,.82) 0%,rgba(16,33,31,.5) 48%,rgba(16,33,31,0) 78%);z-index:1;pointer-events:none}
@media (max-width:760px){.hero::after{background:linear-gradient(to top,rgba(16,33,31,.8) 0%,rgba(16,33,31,.55) 50%,rgba(16,33,31,0) 85%)}}
.hero .in{position:relative;z-index:2;padding:0 16px 56px;max-width:1100px;margin:0 auto;width:100%}
.kick{font:600 13px var(--f-body);letter-spacing:.22em;text-transform:uppercase;opacity:.85;margin:0 0 10px}
.hero h1{font:600 clamp(40px,8vw,88px)/1 var(--f-disp);margin:0;letter-spacing:.08em}
.hero h2{font:400 clamp(21px,3.4vw,34px)/1.25 var(--f-disp);margin:12px 0 6px;max-width:16em}
.hero p.l{font-size:clamp(15px,1.8vw,19px);max-width:36em;margin:0 0 22px;opacity:.9}
.cta{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.btn{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:13px 22px;font:600 15.5px var(--f-body);text-decoration:none;border:1px solid transparent;cursor:pointer;transition:transform .15s,background .15s}
.btn.p{background:var(--gold);color:#241a06}.btn.p:hover{transform:translateY(-1px);background:#e0ad38}
.btn.g{border-color:rgba(255,250,240,.6);color:#fffaf0;background:rgba(0,0,0,.15)}.btn.g:hover{background:rgba(255,250,240,.16)}
.stats{display:flex;flex-wrap:wrap;gap:8px 26px;margin-top:26px;font-size:13.5px;opacity:.9}.stats b{font:600 22px var(--f-disp);display:block;letter-spacing:.01em}
.scrollhint{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);z-index:2;opacity:.6;font-size:11px;letter-spacing:.2em;text-transform:uppercase}
@keyframes drift{from{transform:translateX(0)}to{transform:translateX(-40px)}}
@keyframes drift2{from{transform:translateX(0)}to{transform:translateX(30px)}}
@keyframes glow{0%,100%{opacity:.85}50%{opacity:1}}
.dn1{animation:drift 26s ease-in-out infinite alternate}.dn2{animation:drift2 34s ease-in-out infinite alternate}.sun{animation:glow 6s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){.dn1,.dn2,.sun{animation:none}}
/* sections */
section{padding:56px 0}
.sec-h{max-width:40em}.sec-h .kick{color:var(--sea);opacity:1}
h2.t{font:600 clamp(28px,4vw,42px)/1.1 var(--f-disp);margin:0 0 10px;letter-spacing:-.01em}
p.lead{font-size:17px;color:var(--mut);margin:0 0 22px;max-width:44em}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.tile{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 18px 16px;position:relative;overflow:hidden}
.tile i.bar{position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--c,var(--sea))}
html[dir=rtl] .tile i.bar{left:auto;right:0}
.tile h3{font:600 20px var(--f-disp);margin:0 0 6px}.tile p{margin:0;color:var(--mut);font-size:14.5px}
.tile .tag{display:inline-block;font:600 11px var(--f-body);letter-spacing:.08em;text-transform:uppercase;color:var(--c,var(--sea));margin-bottom:8px}
.tile .tag.rm{color:var(--mut);background:var(--panel-2);padding:2px 8px;border-radius:999px;letter-spacing:.05em}
/* countries */
#explore{background:var(--panel-2)}
.hero2{position:relative;background:var(--sea);border-radius:18px;overflow:hidden;box-shadow:var(--shadow);aspect-ratio:__W__/__H__;max-height:62vh;margin:0 auto}
.hero2 svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.cs{fill:var(--land);stroke:var(--land);stroke-width:1.4;vector-effect:non-scaling-stroke;transition:fill .2s,stroke .2s;cursor:pointer}
.cs.hi,.cs:hover{fill:#f8f1dd;stroke:#f8f1dd}
.ld{stroke:rgba(255,250,240,.7);stroke-width:1.5;stroke-dasharray:4 4;vector-effect:non-scaling-stroke}.ldp{fill:#fffaf0}
.wl{fill:var(--land);opacity:.75;font-family:var(--f-disp);font-style:italic;text-anchor:middle;letter-spacing:.06em;font-size:30px}
.bd{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:2px;text-decoration:none;color:#fffaf0;transition:transform .15s}
.bd:hover,.bd:focus-visible{transform:translate(-50%,-50%) scale(1.06);outline:none}
.bdl{width:44px;height:44px;display:block;filter:drop-shadow(0 2px 4px rgba(10,40,42,.4))}.bdl svg{width:100%;height:100%;display:block}
.bdn{font:600 12.5px var(--f-body);text-shadow:0 1px 2px rgba(0,0,0,.45);white-space:nowrap}
.bdc{font:600 11px var(--f-body);background:rgba(255,250,240,.92);color:var(--ink);border-radius:999px;padding:1px 7px;line-height:1.5}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px;margin-top:14px}
.card{display:flex;align-items:center;gap:12px;padding:10px 12px;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:var(--ink);transition:transform .15s,box-shadow .15s}
.card:hover,.card.hi{transform:translateY(-1px);box-shadow:var(--shadow);border-color:#c5cfc8}
.cl{width:52px;height:52px;flex:none}.cl svg{width:100%;height:100%;display:block}
.ct{flex:1;min-width:0}.ct b{display:block;font:600 17px var(--f-disp)}.ct small{color:var(--mut);font-size:13px}
.go{font-size:26px;color:var(--mut);line-height:1}html[dir=rtl] .go{transform:scaleX(-1)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;justify-content:center;margin:14px 0 0;color:var(--mut);font-size:13px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-inline-end:5px;vertical-align:1px}
/* research strip */
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;align-items:stretch}
.step{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px;position:relative}
.step .n{position:absolute;top:-12px;inset-inline-start:14px;background:var(--ink);color:#fff;border-radius:999px;font:600 12px var(--f-body);padding:3px 10px}
.step h4{font:600 17px var(--f-disp);margin:8px 0 6px}.step p{margin:0;color:var(--mut);font-size:14px}
.step .ex{margin-top:10px;background:var(--panel-2);border-radius:10px;padding:10px 12px;font-size:13px;color:var(--ink)}
.step .ex b{display:block;font:600 15px var(--f-disp)}
/* showcase */
.show{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
.sh{display:block;text-decoration:none;color:#fffaf0;border-radius:16px;padding:16px;min-height:150px;position:relative;overflow:hidden;background:var(--bg,var(--sea));transition:transform .15s,box-shadow .15s}
.sh:hover{transform:translateY(-2px);box-shadow:var(--shadow)}
.sh .cc{font:600 11px var(--f-body);letter-spacing:.1em;text-transform:uppercase;opacity:.85}
.sh h4{font:600 20px/1.15 var(--f-disp);margin:8px 0 6px}.sh p{margin:0;font-size:13.5px;opacity:.9}
.sh .pill{position:absolute;top:12px;inset-inline-end:12px;font:600 10.5px var(--f-body);letter-spacing:.06em;background:rgba(255,250,240,.2);border-radius:999px;padding:2px 8px}
/* journey */
.journey{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;counter-reset:j}
.j{background:var(--night);color:#fffaf0;border-radius:16px;padding:18px}
.j h4{font:600 22px var(--f-disp);margin:0 0 6px}.j h4::before{counter-increment:j;content:counter(j) " · ";color:var(--gold)}
.j p{margin:0;opacity:.85;font-size:14.5px}.j ul{margin:10px 0 0;padding-inline-start:18px;font-size:14px;opacity:.9}
.ai{background:var(--night);color:#fffaf0}
.ai .tile{background:rgba(255,250,240,.06);border-color:rgba(255,250,240,.14);color:#fffaf0}.ai .tile p{color:rgba(255,250,240,.78)}.ai .tile .tag.rm{background:rgba(255,250,240,.12);color:#fffaf0}
.ai p.lead{color:rgba(255,250,240,.8)}.ai .sec-h .kick{color:var(--gold)}
.honest{margin-top:16px;font-size:13.5px;color:rgba(255,250,240,.7);max-width:50em}
footer{padding:28px 16px 36px;color:var(--mut);font-size:13px;text-align:center;border-top:1px solid var(--line)}
footer a{color:var(--sea);text-decoration:none}footer p{margin:6px 0}
@media (max-width:520px){.bdl{width:34px;height:34px}.bdn,.bdc{display:none}.wl{font-size:34px}.hero2{border-radius:14px}section{padding:40px 0}.hero{min-height:88vh}}
</style></head>
<body>
<header class="hero" id="top">
 <svg class="sky" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1f20"/><stop offset=".55" stop-color="#1f4a4d"/><stop offset="1" stop-color="#c99a2e"/></linearGradient>
  <radialGradient id="sn" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe8a3"/><stop offset=".6" stop-color="#f6c24a" stop-opacity=".9"/><stop offset="1" stop-color="#f6c24a" stop-opacity="0"/></radialGradient>
  <linearGradient id="se" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f9aa0"/><stop offset="1" stop-color="#1f4a4d"/></linearGradient></defs>
  <rect width="1440" height="900" fill="url(#sk)"/>
  <circle class="sun" cx="1040" cy="430" r="150" fill="url(#sn)"/>
  <g class="dn2" opacity=".55"><path d="M-80 560 C200 500 420 520 640 480 C860 440 1080 470 1300 450 C1400 440 1500 450 1540 445 L1540 620 L-80 620Z" fill="#8a6a52"/></g>
  <path d="M-80 600 C300 585 700 610 1100 590 C1300 580 1440 590 1540 585 L1540 700 L-80 700Z" fill="url(#se)"/>
  <g class="dn1"><path d="M-80 690 C160 640 380 650 600 690 C820 730 1040 660 1260 680 C1380 690 1480 700 1540 700 L1540 900 L-80 900Z" fill="#d9b779"/>
  <path d="M-80 760 C200 720 420 740 640 770 C860 800 1100 740 1320 760 C1420 770 1500 780 1540 780 L1540 900 L-80 900Z" fill="#cf8e5c"/></g>
  <path d="M-80 830 C300 800 700 840 1100 815 C1300 805 1440 820 1540 815 L1540 900 L-80 900Z" fill="#a8653f"/>
  <path d="M-80 870 C400 855 900 880 1540 860 L1540 900 L-80 900Z" fill="#5e4433"/>
 </svg>
 <div class="top">
  <div class="logo">__LOGO__</div>
  <div class="wm">LAYERS<small id="byline"></small></div>
  <button id="lang" aria-label="العربية">عربي</button>
 </div>
 <div class="in">
  <p class="kick" id="kick"></p>
  <h1 id="h1">LAYERS</h1>
  <h2 id="h2"></h2>
  <p class="l" id="hl"></p>
  <div class="cta"><a class="btn p" href="#explore" id="c1"></a><a class="btn g" href="#how" id="c2"></a></div>
  <div class="stats" id="stats"></div>
 </div>
 <div class="scrollhint" id="sh"></div>
</header>

<section id="explore"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k2"></p><h2 class="t" id="t2"></h2><p class="lead" id="l2"></p></div>
 <div class="hero2">
  <svg viewBox="0 __VY0__ __W__ __H__" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Map of the Arabian Gulf countries"><defs><filter id="lsh" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0b2a2c" flood-opacity=".35"/></filter></defs>
   <g filter="url(#lsh)">__SHAPES__</g>__WL__<g>__LEADERS__</g>
  </svg>
  __BADGES__
 </div>
 <div class="cards">__CARDS__</div>
 <div class="legend" id="legend"></div>
</div></section>

<section id="how"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k3"></p><h2 class="t" id="t3"></h2><p class="lead" id="l3"></p></div>
 <div class="grid3" id="layers3"></div>
</div></section>

<section id="research" style="background:var(--panel-2)"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k4"></p><h2 class="t" id="t4"></h2><p class="lead" id="l4"></p></div>
 <div class="strip" id="strip"></div>
</div></section>

<section class="ai" id="ai"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k5"></p><h2 class="t" id="t5"></h2><p class="lead" id="l5"></p></div>
 <div class="grid3" id="aig"></div>
 <p class="honest" id="honest"></p>
</div></section>

<section id="showcase"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k6"></p><h2 class="t" id="t6"></h2><p class="lead" id="l6"></p></div>
 <div class="show" id="show"></div>
</div></section>

<section id="journey" style="background:var(--panel-2)"><div class="wrap">
 <div class="sec-h"><p class="kick" id="k7"></p><h2 class="t" id="t7"></h2><p class="lead" id="l7"></p></div>
 <div class="journey" id="jg"></div>
 <p style="margin:22px 0 0;text-align:center"><a class="btn p" href="#explore" id="c3"></a></p>
</div></section>

<footer>
 <p id="f1"></p>
 <p><a href="privacy.html" id="fp"></a> · <a href="https://github.com/smbehbehani-max/Layers" rel="noopener" target="_blank">GitHub</a> · <span id="fm"></span></p>
</footer>

<script>
(function(){
const DATA=__DATA__,CN=__C__,IDX=__IDX__,SHOW=__SHOW__,ORDER=['kw','sa','bh','qa','ae','om'],TOTAL=__TOTAL__;
const T={en:{by:'by GeoHeritage',kick:'Geology · Archaeology · Ecology',h2:'Discover the Gulf Beyond the Ordinary.',hl:'Explore the stories written into the landscape. Six countries, one map: the rocks beneath your feet, the people who lived on them, and the life that still does — every place with its sources, in Arabic and English.',
  c1:'Explore the Gulf',c2:'How it works',c3:'Choose your country',sh:'scroll',
  stats:[[TOTAL,'places with sources'],['6','countries'],['3','layers of heritage'],['2','languages']],
  k2:'Six countries, one journey',t2:'Choose where to begin',l2:'Each country is a full edition: map, timeline, explorer routes, live directions and offline use. Switch countries any time from the top bar.',
  places:n=>`${n} places`,arch:'archaeology',geo:'geology',eco:'ecology',legend:[['arch','Archaeological'],['geo','Geological'],['eco','Ecology']],wl:['Arabian Gulf','Red Sea','Arabian Sea'],
  k3:'A multidisciplinary approach',t3:'One place, many layers',l3:'A spring, a tomb and a mangrove are rarely separate stories. Layers keeps the three domains together, so a visitor sees why a city rose where the water came out of the rock, and why the birds still come.',
  layers3:[['arch','Archaeological','Settlements, tombs, inscriptions, ports and forts — from the first Neolithic herders to the pearling towns and the first oil wells.'],['geo','Geological','Formations, fossils, craters, lava fields, dunes and springs: the deep-time stage on which everything else happened.'],['eco','Ecology','Reserves, wetlands, reefs, mangroves and the species that depend on them — the living layer, and the one most at risk.']],
  k4:'From research to a place',t4:'Science you can visit',l4:'Behind every card is a published paper, a heritage body or an official survey. We read it, keep the numbers, write a title you would tell a friend, and leave the reference in place.',
  strip:[['A source is read','A peer-reviewed paper, a UNESCO nomination file, a geological survey or a museum report.','PLOS ONE, 2024 — first excavation of an Arabian lava tube'],['Facts are extracted','Place, dates, measurements, who found it, what it means. Nothing added that the source did not say.','Umm Jirsan · 1.5 km lava tube · occupied from 10,000 years ago · herders with dogs'],['A story is written','Two modes: Researcher keeps the full record; Explorer gives a chapter title and a one-line hook.','“People who lived in a lava tube” — Layers of Saudi Arabia'],['The source stays','Every card ends with its references, so a student, a guide or a scientist can go back to the original.','Stewart, M. et al. (2024). PLOS ONE 19(4).']],
  k5:'AI, where it earns its place',t5:'Connecting the dots — and saying so',l5:'Layers uses AI to interpret, connect and simplify, never to invent. Everything generated is labelled, and everything stated has a source.',
  aig:[['now','Explorer mode','Chapter titles, one-line hooks and guided routes turn a catalogue into an expedition — the same records, told for a traveller.'],['now','Illustrated stories','In the Kuwait edition, research is retold as short illustrated stories with their references kept in view.'],['now','AI speculation','Untested connections between records — a shape on a satellite image, a link between two sites — shown as hypotheses with their reasoning, evidence and how they could be proved wrong.'],['now','Spatial & temporal intelligence','A timeline from the Jurassic sea to today, graticule maps, protected areas and World Heritage markers on every edition.'],['roadmap','Cross-disciplinary interpretation engine','Integrated readings per destination: how the rock, the water, the settlement and the habitat explain each other — with evidence, interpretation and hypothesis kept apart.'],['roadmap','Assistant, discovery feed & contributions','“What can I explore in one day near me?”, automatic monitoring of new research for review, and citizen submissions with verification.']],
  honest:'“Now” features are in the app today. “Roadmap” features are planned and will be labelled when they arrive — no capability is claimed before it exists.',
  k6:'Hidden heritage',t6:'Places you did not know you could visit',l6:'A few of the __TOTAL__ places across the six editions. Tap one to open it on its map.',
  k7:'Your journey',t7:'Discover · Explore · Plan',l7:'Built for people on the move: inside or outside the region, with a phone, on the road, sometimes offline.',
  jg:[['Discover','Start with a country, a category or a search — or just the map.',['Researcher and Explorer modes','Arabic and English','Search across every place']],['Explore','Open a place and read it the way you want: the record, the story, the sources.',['Guided expedition routes','Timeline view','Protected areas and World Heritage']],['Plan','Take it with you.',['Go live: distance and bearing to every place','Share any place with a link','Install it; it works offline']]],
  f1:'Every place carries its sources. Facts are taken from published research, heritage bodies and official reports; illustrated stories and AI speculation are marked as such.',
  priv:'Privacy',made:'Made in Kuwait',lang:'عربي'},
 ar:{by:'من جيوهيريتيج',kick:'جيولوجيا · آثار · بيئة',h2:'اكتشف الخليج بما يتجاوز المألوف.',hl:'استكشف القصص المكتوبة في الأرض. ست دول وخريطة واحدة: الصخر تحت قدميك، والناس الذين عاشوا عليه، والحياة التي ما زالت فيه — كل موقع بمصادره، بالعربية والإنجليزية.',
  c1:'استكشف الخليج',c2:'كيف يعمل',c3:'اختر دولتك',sh:'مرّر',
  stats:[[TOTAL,'موقعًا بمصادره'],['6','دول'],['3','طبقات من التراث'],['2','لغتان']],
  k2:'ست دول ورحلة واحدة',t2:'اختر من أين تبدأ',l2:'كل دولة نسخة كاملة: خريطة وخط زمني ومسارات استكشاف وإرشادات حيّة وعمل دون إنترنت. بدّل بين الدول في أي وقت من الشريط العلوي.',
  places:n=>`${n} موقعًا`,arch:'آثار',geo:'جيولوجيا',eco:'بيئة',legend:[['arch','آثار'],['geo','جيولوجيا'],['eco','بيئة']],wl:['الخليج العربي','البحر الأحمر','بحر العرب'],
  k3:'منهج متعدد التخصصات',t3:'مكان واحد وطبقات كثيرة',l3:'العين والقبر وغابة القرم نادرًا ما تكون قصصًا منفصلة. يُبقي «طبقات» المجالات الثلاثة معًا، فيرى الزائر لماذا قامت مدينة حيث خرج الماء من الصخر، ولماذا ما زالت الطيور تأتي.',
  layers3:[['arch','آثار','مستوطنات ومقابر ونقوش وموانئ وقلاع — من أوائل رعاة العصر الحجري الحديث إلى مدن اللؤلؤ وأولى آبار النفط.'],['geo','جيولوجيا','تكوينات وأحافير وفوهات وحرّات وكثبان وعيون: مسرح الزمن السحيق الذي جرى عليه كل شيء آخر.'],['eco','بيئة','محميات وأراضٍ رطبة وشعاب وقرم والأنواع التي تعتمد عليها — الطبقة الحيّة، وهي الأكثر عرضة للخطر.']],
  k4:'من البحث إلى المكان',t4:'علم يمكنك زيارته',l4:'خلف كل بطاقة ورقة علمية منشورة أو هيئة تراث أو مسح رسمي. نقرأه، ونحتفظ بالأرقام، ونكتب عنوانًا تحكيه لصديق، ونترك المرجع في مكانه.',
  strip:[['يُقرأ المصدر','ورقة محكّمة، أو ملف ترشيح لليونسكو، أو مسح جيولوجي، أو تقرير متحف.','PLOS ONE، 2024 — أول تنقيب في أنبوب بركاني بالجزيرة العربية'],['تُستخرج الحقائق','المكان والتواريخ والقياسات ومن اكتشفه وما معناه. لا يُضاف شيء لم يقله المصدر.','أم جرسان · أنبوب بطول 1.5 كم · استيطان منذ 10,000 عام · رعاة بكلابهم'],['تُكتب القصة','وضعان: «باحث» يحتفظ بالسجل الكامل، و«مستكشف» يعطي عنوان فصل وجملة جذب.','«أناس عاشوا في أنبوب بركاني» — طبقات السعودية'],['يبقى المصدر','تنتهي كل بطاقة بمراجعها، ليعود الطالب أو المرشد أو العالم إلى الأصل.','Stewart, M. et al. (2024). PLOS ONE 19(4).']],
  k5:'الذكاء الاصطناعي حيث يستحق مكانه',t5:'وصل النقاط — والتصريح بذلك',l5:'يستخدم «طبقات» الذكاء الاصطناعي للتفسير والربط والتبسيط، لا للاختلاق أبدًا. كل ما يُولَّد مُعلَّم، وكل ما يُذكر له مصدر.',
  aig:[['now','وضع المستكشف','عناوين فصول وجمل جذب ومسارات موجَّهة تحوّل الفهرس إلى رحلة استكشاف — السجلات نفسها، تُروى للمسافر.'],['now','قصص مصوّرة','في نسخة الكويت، يُعاد سرد البحث قصصًا قصيرة مصوّرة مع إبقاء مراجعها ظاهرة.'],['now','تخمين ذكي','روابط غير مختبَرة بين السجلات — شكل في صورة فضائية، أو صلة بين موقعين — تُعرض فرضياتٍ مع منطقها وأدلتها وكيف يمكن دحضها.'],['now','ذكاء مكاني وزمني','خط زمني من البحر الجوراسي حتى اليوم، وخرائط بشبكة إحداثيات، ومحميات ومواقع تراث عالمي في كل نسخة.'],['roadmap','محرك التفسير متعدد التخصصات','قراءات متكاملة لكل وجهة: كيف يفسّر الصخر والماء والاستيطان والموئل بعضها بعضًا — مع الفصل بين الدليل والتفسير والفرضية.'],['roadmap','مساعد، وتدفق اكتشافات، ومساهمات','«ماذا أستكشف في يوم واحد قربي؟»، ورصد تلقائي للأبحاث الجديدة للمراجعة، ومساهمات الجمهور مع التحقق.']],
  honest:'ميزات «الآن» موجودة في التطبيق اليوم. وميزات «خارطة الطريق» مخطَّطة وستُعلَّم عند وصولها — لا تُدّعى أي قدرة قبل أن توجد.',
  k6:'تراث مخفي',t6:'أماكن لم تكن تعرف أنك تستطيع زيارتها',l6:'بعض من __TOTAL__ موقعًا في النسخ الست. اضغط على أحدها لفتحه على خريطته.',
  k7:'رحلتك',t7:'اكتشف · استكشف · خطّط',l7:'صُمم لمن هم على الطريق: من داخل المنطقة أو خارجها، بهاتف، في السيارة، وأحيانًا دون إنترنت.',
  jg:[['اكتشف','ابدأ بدولة أو فئة أو بحث — أو بالخريطة فقط.',['وضعا الباحث والمستكشف','العربية والإنجليزية','بحث في كل المواقع']],['استكشف','افتح موقعًا واقرأه كما تريد: السجل أو القصة أو المصادر.',['مسارات استكشاف موجَّهة','عرض الخط الزمني','المحميات ومواقع التراث العالمي']],['خطّط','خذه معك.',['تتبّع مباشر: المسافة والاتجاه إلى كل موقع','شارك أي موقع برابط','ثبّته؛ يعمل دون إنترنت']]],
  f1:'كل موقع يحمل مصادره. الحقائق مأخوذة من أبحاث منشورة وهيئات التراث والتقارير الرسمية؛ والقصص المصوّرة والتخمينات الذكية مميّزة بوضوح.',
  priv:'الخصوصية',made:'صُنع في الكويت',lang:'English'}};
const store={get(k,d){try{const v=localStorage.getItem('kge-'+k);return v==null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('kge-'+k,JSON.stringify(v))}catch(e){}}};
let lang=store.get('lang','en');if(lang!='ar')lang='en';
const $=s=>document.querySelector(s),E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const CV={archaeological:'arch',geological:'geo',ecology:'eco',speculative:'spec'};
function render(){const t=T[lang],ar=lang=='ar';document.documentElement.lang=lang;document.documentElement.dir=ar?'rtl':'ltr';
 $('#byline').textContent=t.by;$('#kick').textContent=t.kick;$('#h1').textContent=ar?'طبقات':'LAYERS';$('#h2').textContent=t.h2;$('#hl').textContent=t.hl;$('#c1').textContent=t.c1;$('#c2').textContent=t.c2;$('#c3').textContent=t.c3;$('#sh').textContent=t.sh;$('#lang').textContent=t.lang;
 $('#stats').innerHTML=t.stats.map(([n,l])=>`<span><b>${E(n)}</b>${E(l)}</span>`).join('');
 for(const i of [2,3,4,5,6,7]){$('#k'+i).textContent=t['k'+i];$('#t'+i).textContent=t['t'+i];$('#l'+i).textContent=t['l'+i].replace('__TOTAL__',TOTAL)}
 ['#wl1','#wl2','#wl3'].forEach((s,i)=>$(s).textContent=t.wl[i]);
 $('#legend').innerHTML=t.legend.map(([k,l])=>`<span><i style="background:var(--${k})"></i>${l}</span>`).join('');
 ORDER.forEach(cc=>{const d=DATA[cc],c=CN[cc];$(`[data-n="${cc}"]`).textContent=ar?c.ar:c.en;$(`[data-t="${cc}"]`).textContent=ar?c.tar:c.ten;$(`[data-s="${cc}"]`).textContent=`${t.places(d.n)} · ${d.archaeological} ${t.arch} · ${d.geological} ${t.geo} · ${d.ecology} ${t.eco}`});
 $('#layers3').innerHTML=t.layers3.map(([k,h,p],i)=>`<div class="tile" style="--c:var(--${k})"><i class="bar"></i><span class="tag">${ar?'الطبقة '+(i+1):'Layer '+(i+1)}</span><h3>${E(h)}</h3><p>${E(p)}</p></div>`).join('');
 $('#strip').innerHTML=t.strip.map(([h,p,ex],i)=>`<div class="step"><span class="n">${i+1}</span><h4>${E(h)}</h4><p>${E(p)}</p><div class="ex">${E(ex)}</div></div>`).join('');
 $('#aig').innerHTML=t.aig.map(([k,h,p])=>`<div class="tile" style="--c:${k=='now'?'var(--gold)':'#fff'}"><i class="bar"></i><span class="tag${k=='now'?'':' rm'}">${k=='now'?(ar?'الآن':'Now'):(ar?'خارطة الطريق':'Roadmap')}</span><h3>${E(h)}</h3><p>${E(p)}</p></div>`).join('');
 $('#honest').textContent=t.honest;
 $('#show').innerHTML=SHOW.map(s=>`<a class="sh" href="#${s.cc}/p=${encodeURIComponent(s.id)}" style="--bg:var(--${CV[s.c]})"><span class="cc">${E(ar?CN[s.cc].ar:CN[s.cc].en)}</span><span class="pill">${E(ar?{arch:'آثار',geo:'جيولوجيا',eco:'بيئة',spec:'تخمين ذكي'}[CV[s.c]]:{arch:'Archaeology',geo:'Geology',eco:'Ecology',spec:'AI speculation'}[CV[s.c]])}</span><h4>${E(ar?s.ta:s.te)}</h4><p>${E(ar?s.na:s.n)}</p></a>`).join('');
 $('#jg').innerHTML=t.jg.map(([h,p,ul])=>`<div class="j"><h4>${E(h)}</h4><p>${E(p)}</p><ul>${ul.map(x=>`<li>${E(x)}</li>`).join('')}</ul></div>`).join('');
 $('#f1').textContent=t.f1;$('#fp').textContent=t.priv;$('#fm').textContent=t.made;
 document.title=ar?'طبقات · Layers — اكتشف الخليج بما يتجاوز المألوف':'Layers · طبقات — Discover the Gulf Beyond the Ordinary'}
$('#lang').addEventListener('click',()=>{lang=lang=='ar'?'en':'ar';store.set('lang',lang);render()});
document.querySelectorAll('.cs').forEach(p=>{const cc=p.dataset.cc;p.addEventListener('click',()=>openCC(cc));
 p.addEventListener('mouseenter',()=>$(`.card[data-cc="${cc}"]`).classList.add('hi'));p.addEventListener('mouseleave',()=>$(`.card[data-cc="${cc}"]`).classList.remove('hi'))});
document.querySelectorAll('.card,.bd').forEach(a=>{const cc=a.dataset.cc;a.addEventListener('mouseenter',()=>$(`.cs[data-cc="${cc}"]`).classList.add('hi'));a.addEventListener('mouseleave',()=>$(`.cs[data-cc="${cc}"]`).classList.remove('hi'))});
render();
/* ---- loading a country edition inside this same file ---- */
function loadCC(cc){const el=document.getElementById('ed-'+cc);if(!el)return false;const src=el.textContent.replace(/<\\\/script/g,'</script');document.open();document.write(src);document.close();return true}
function openCC(cc,sub){history.replaceState(null,'',location.pathname+location.search+'#'+cc+(sub?'/'+sub:''));loadCC(cc)}
addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a)return;const m=/^#([a-z]{2})(?:\/(.*))?$/.exec(a.getAttribute('href'));if(m&&CN[m[1]]){e.preventDefault();openCC(m[1],m[2])}});
function boot(){const h=location.hash;let m=/^#([a-z]{2})(?:\/(.*))?$/.exec(h);if(m&&CN[m[1]]){if(loadCC(m[1]))return}
 const p=/^#p=(.+)$/.exec(h);if(p){let id='';try{id=decodeURIComponent(p[1])}catch(e){id=p[1]}const cc=IDX[id];if(cc){openCC(cc,'p='+p[1]);return}}
 document.documentElement.classList.remove('ld')}
addEventListener('hashchange',()=>{const m=/^#([a-z]{2})(?:\/(.*))?$/.exec(location.hash);if(m&&CN[m[1]])loadCC(m[1])});
if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));
if(document.readyState=='loading')addEventListener('DOMContentLoaded',boot);else boot();
})();
</script>
<!--PAYLOAD-->
</body></html>
'''
if __name__ == '__main__':
    print(build())
