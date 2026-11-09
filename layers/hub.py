"""Builds the Layers front page (hub) -> /tmp/w/layers/site/index.html"""
import json, math, re, os
M = json.load(open('/tmp/w/layers/gulf_map.json'))
LOGOS = json.load(open('/tmp/w/logos_inline.json'))
BASE = 'https://smbehbehani-max.github.io/Layers2/docs/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
C = {
 'kw': dict(en='Kuwait', ar='الكويت', ten='Layers of Kuwait', tar='طبقات الكويت', pt=(47.75, 29.3), bd=(48.4, 31.0)),
 'sa': dict(en='Saudi Arabia', ar='السعودية', ten='Layers of Saudi Arabia', tar='طبقات السعودية', pt=(44.0, 24.0), bd=(44.0, 24.0)),
 'bh': dict(en='Bahrain', ar='البحرين', ten='Layers of Bahrain', tar='طبقات البحرين', pt=(50.55, 26.05), bd=(49.0, 27.2)),
 'qa': dict(en='Qatar', ar='قطر', ten='Layers of Qatar', tar='طبقات قطر', pt=(51.2, 25.35), bd=(52.5, 27.3)),
 'ae': dict(en='the UAE', ar='الإمارات', ten='Layers of the UAE', tar='طبقات الإمارات', pt=(54.4, 23.9), bd=(54.2, 23.3)),
 'om': dict(en='Oman', ar='عُمان', ten='Layers of Oman', tar='طبقات عُمان', pt=(56.6, 20.6), bd=(58.0, 19.9)),
}
def counts(cc):
    if cc == 'kw':
        d = json.load(open('/tmp/w/data2.json'))['sites']; n = 80
    else:
        d = json.load(open(f'/tmp/w/gulf/{cc}/data.json'))['sites']; n = len(d)
    k = {'archaeological': 0, 'geological': 0, 'ecology': 0}
    for s in d: k[s['c']] = k.get(s['c'], 0) + 1
    return n, k
def P(lng, lat):
    return ((lng * M['K'] - M['x0']) * M['S'], (-lat - M['y0']) * M['S'])
def plain_logo(pf):
    s = open('/tmp/w/logo/icon-plain.svg').read()
    for i in ['sky', 'sun', 'sq', 'fc', 'sh']:
        s = s.replace(f'id="{i}"', f'id="{pf}-{i}"').replace(f'url(#{i})', f'url(#{pf}-{i})')
    return s.replace('xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"', 'viewBox="0 0 1024 1024" aria-hidden="true"')
def flag_logo(cc, pf):
    s = LOGOS[cc].split('<svg class="v-sm"')[0]  # the v-on (small-badge) variant
    s = s.replace(f'lg{cc}n-', f'{pf}-').replace('class="v-on" ', '')
    return s
def build():
    W, H = M['w'], M['h']; VY0 = -70; VH = H + 70
    shapes = ''.join(f'<path class="cs" data-cc="{cc}" d="{M["paths"][cc]}"/>' for cc in ORDER)
    badges = ''; leaders = ''; cards = ''; DATA = {}
    for cc in ORDER:
        n, k = counts(cc); c = C[cc]; DATA[cc] = dict(n=n, **k)
        x, y = P(*c['pt']); bx, by = P(*c['bd'])
        if (bx, by) != (x, y):
            leaders += f'<line class="ld" x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/><circle class="ldp" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
        badges += f'''<a class="bd" href="{cc}.html" data-cc="{cc}" style="left:{bx/W*100:.2f}%;top:{(by-VY0)/VH*100:.2f}%"><span class="bdl">{flag_logo(cc, 'bd'+cc)}</span><span class="bdn" data-n="{cc}"></span><span class="bdc">{n}</span></a>'''
        cards += f'''<a class="card" href="{cc}.html" data-cc="{cc}"><span class="cl">{flag_logo(cc, 'cd'+cc)}</span><span class="ct"><b data-t="{cc}"></b><small><span data-s="{cc}"></span></small></span><span class="go" aria-hidden="true">›</span></a>'''
    html = TPL.replace('__SHAPES__', shapes).replace('__LEADERS__', leaders).replace('__BADGES__', badges).replace('__CARDS__', cards) \
        .replace('__W__', f'{W:.0f}').replace('__H__', f'{VH:.0f}').replace('__VY0__', f'{VY0:.0f}').replace('__WL__', ''.join(f'<text class="wl" id="wl{i+1}" x="{P(*g)[0]:.0f}" y="{P(*g)[1]:.0f}">{t}</text>' for i, (g, t) in enumerate([((50.9, 28.9), 'Arabian Gulf'), ((36.8, 21.0), 'Red Sea'), ((56.8, 16.9), 'Arabian Sea')]))).replace('__LOGO__', plain_logo('hub')).replace('__DATA__', json.dumps(DATA)) \
        .replace('__C__', json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in C.items()}, ensure_ascii=False)).replace('__BASE__', BASE)
    os.makedirs('/tmp/w/layers/site', exist_ok=True)
    open('/tmp/w/layers/site/index.html', 'w', encoding='utf-8').write(html)
    return DATA

TPL = r'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Layers · طبقات</title>
<meta name="description" content="Layers: the geology, archaeology and ecology of the Arabian Gulf on one bilingual map. Choose a country to begin.">
<meta name="theme-color" content="#f7f8f5">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Layers"><meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="application-name" content="Layers">
<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="canonical" href="__BASE__">
<meta property="og:type" content="website"><meta property="og:site_name" content="Layers"><meta property="og:title" content="Layers · طبقات">
<meta property="og:description" content="The geology, archaeology and ecology of the Arabian Gulf on one bilingual map. Choose a country to begin."><meta property="og:url" content="__BASE__"><meta property="og:image" content="__BASE__og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Layers · طبقات"><meta name="twitter:image" content="__BASE__og.png">
<style>
:root{--sea:#2c6e72;--sea-2:#3f8286;--land:#ece3cf;--coast:#7b6a4c;--panel:#f7f8f5;--panel-2:#eef1ec;--ink:#1a2a2b;--mut:#5d6d6c;--line:#d5dcd6;--arch:#b4521c;--geo:#5847b0;--eco:#2c7a4c;--gold:#c99a2e;
 --f-disp:"Newsreader",Georgia,"Times New Roman",serif;--f-body:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--shadow:0 6px 24px rgba(10,40,42,.18)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--panel);color:var(--ink);font-family:var(--f-body);line-height:1.45;min-height:100vh;padding-bottom:env(safe-area-inset-bottom)}
[lang=ar],html[dir=rtl] body{font-family:"Noto Naskh Arabic","Geeza Pro","Segeo UI",system-ui,sans-serif}
header{display:flex;align-items:center;gap:12px;padding:14px 16px 8px;max-width:1100px;margin:0 auto}
.logo{width:58px;height:58px;flex:none;filter:drop-shadow(0 1px 2px rgba(58,29,16,.28))}.logo svg{width:100%;height:100%;display:block}
.brand{flex:1;min-width:0}.brand h1{font:600 26px/1.05 var(--f-disp);margin:0;letter-spacing:-.01em}.brand h1 small{font:inherit;font-size:20px;color:var(--mut);margin-inline-start:8px}
.brand p{margin:3px 0 0;color:var(--mut);font-size:13.5px}
#lang{border:1px solid var(--line);background:#fff;border-radius:999px;padding:7px 13px;font:600 14px var(--f-body);cursor:pointer;color:var(--ink)}
#lang:hover{background:var(--panel-2)}
main{max-width:1100px;margin:0 auto;padding:4px 16px 32px}
.hero{position:relative;margin:0 auto;background:var(--sea);border-radius:18px;overflow:hidden;box-shadow:var(--shadow);aspect-ratio:__W__/__H__;max-height:62vh}
.hero svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.cs{fill:var(--land);stroke:var(--land);stroke-width:1.4;vector-effect:non-scaling-stroke;transition:fill .2s,stroke .2s;cursor:pointer}
.cs.hi,.cs:hover{fill:#f8f1dd;stroke:#f8f1dd}
.ld{stroke:rgba(255,250,240,.7);stroke-width:1.5;stroke-dasharray:4 4;vector-effect:non-scaling-stroke}.ldp{fill:#fffaf0}
.gr{stroke:rgba(255,255,255,.08);stroke-width:1;vector-effect:non-scaling-stroke}
.wl{fill:var(--land);opacity:.75;font-family:var(--f-disp);font-style:italic;text-anchor:middle;letter-spacing:.06em;font-size:30px}
.bd{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:2px;text-decoration:none;color:#fffaf0;transition:transform .15s}
.bd:hover,.bd:focus-visible{transform:translate(-50%,-50%) scale(1.06);outline:none}
.bdl{width:44px;height:44px;display:block;filter:drop-shadow(0 2px 4px rgba(10,40,42,.4))}.bdl svg{width:100%;height:100%;display:block}
.bdn{font:600 12.5px var(--f-body);text-shadow:0 1px 2px rgba(0,0,0,.45);white-space:nowrap}
.bdc{font:600 11px var(--f-body);background:rgba(255,250,240,.92);color:var(--ink);border-radius:999px;padding:1px 7px;line-height:1.5}
.hint{text-align:center;color:var(--mut);font-size:13.5px;margin:12px 0 6px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px;margin-top:10px}
.card{display:flex;align-items:center;gap:12px;padding:10px 12px;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:var(--ink);transition:transform .15s,box-shadow .15s}
.card:hover,.card.hi{transform:translateY(-1px);box-shadow:var(--shadow);border-color:#c5cfc8}
.cl{width:52px;height:52px;flex:none}.cl svg{width:100%;height:100%;display:block}
.ct{flex:1;min-width:0}.ct b{display:block;font:600 17px var(--f-disp)}.ct small{color:var(--mut);font-size:13px}
.go{font-size:26px;color:var(--mut);line-height:1}
html[dir=rtl] .go{transform:scaleX(-1)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;justify-content:center;margin:14px 0 0;color:var(--mut);font-size:13px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-inline-end:5px;vertical-align:1px}
footer{max-width:1100px;margin:0 auto;padding:8px 16px 28px;color:var(--mut);font-size:13px;text-align:center}
footer a{color:var(--sea);text-decoration:none}footer a:hover{text-decoration:underline}
footer p{margin:6px 0}
@media (max-width:520px){.brand h1{font-size:23px}.brand h1 small{font-size:17px}.bdl{width:34px;height:34px}.bdn,.bdc{display:none}.wl{font-size:34px}.hero{border-radius:14px}}
@media (min-width:900px){header{padding-top:22px}.logo{width:68px;height:68px}.brand h1{font-size:32px}}
.toast{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);background:var(--ink);color:#fff;padding:10px 16px;border-radius:999px;font-size:14px;display:none;z-index:9}
.toast button{margin-inline-start:10px;background:#fff;color:var(--ink);border:0;border-radius:999px;padding:4px 10px;font-weight:600;cursor:pointer}
</style></head>
<body>
<header>
 <div class="logo">__LOGO__</div>
 <div class="brand"><h1><span id="t">Layers</span><small id="t2">طبقات</small></h1><p id="sub"></p></div>
 <button id="lang" aria-label="العربية">عربي</button>
</header>
<main>
 <div class="hero" id="hero">
  <svg viewBox="0 __VY0__ __W__ __H__" preserveAspectRatio="xMidYMid meet" aria-label="Map of the Arabian Gulf countries" role="img"><defs><filter id="lsh" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0b2a2c" flood-opacity=".35"/></filter></defs>
   <g filter="url(#lsh)">__SHAPES__</g>
   __WL__
   <g>__LEADERS__</g>
  </svg>
  __BADGES__
 </div>
 <p class="hint" id="hint"></p>
 <div class="cards" id="cards">__CARDS__</div>
 <div class="legend" id="legend"></div>
</main>
<footer>
 <p id="f1"></p>
 <p><a href="privacy.html" id="fp"></a> · <a href="https://github.com/smbehbehani-max/Layers" rel="noopener" target="_blank">GitHub</a> · <span id="fm"></span></p>
</footer>
<div class="toast" id="toast"></div>
<script>
const DATA=__DATA__,CN=__C__,ORDER=['kw','sa','bh','qa','ae','om'];
const T={en:{sub:'Geology, archaeology and ecology of the Arabian Gulf',hint:'Choose a country to open its layers.',places:n=>`${n} places`,arch:'archaeology',geo:'geology',eco:'ecology',
  f1:'Every place carries its sources. Facts are taken from published research, heritage bodies and official reports; illustrated stories and AI speculation are marked as such.',
  priv:'Privacy',made:'Made in Kuwait',lang:'عربي',legend:[['arch','Archaeological'],['geo','Geological'],['eco','Ecology']],wl:['Arabian Gulf','Red Sea','Arabian Sea'],upd:'A new version is ready.',reload:'Reload'},
 ar:{sub:'جيولوجيا الخليج العربي وآثاره وبيئته',hint:'اختر دولة لفتح طبقاتها.',places:n=>`${n} موقعًا`,arch:'آثار',geo:'جيولوجيا',eco:'بيئة',
  f1:'كل موقع يحمل مصادره. الحقائق مأخوذة من أبحاث منشورة وهيئات التراث والتقارير الرسمية؛ والقصص المصوّرة والتخمينات الذكية مميّزة بوضوح.',
  priv:'الخصوصية',made:'صُنع في الكويت',lang:'English',legend:[['arch','آثار'],['geo','جيولوجيا'],['eco','بيئة']],wl:['الخليج العربي','البحر الأحمر','بحر العرب'],upd:'نسخة جديدة جاهزة.',reload:'تحديث'}};
const store={get(k,d){try{const v=localStorage.getItem('kge-'+k);return v==null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('kge-'+k,JSON.stringify(v))}catch(e){}}};
let lang=store.get('lang','en');if(lang!='ar')lang='en';
const $=s=>document.querySelector(s);
function render(){const t=T[lang],ar=lang=='ar';document.documentElement.lang=lang;document.documentElement.dir=ar?'rtl':'ltr';
 $('#t').textContent=ar?'طبقات':'Layers';$('#t2').textContent=ar?'Layers':'طبقات';$('#sub').textContent=t.sub;$('#hint').textContent=t.hint;$('#lang').textContent=t.lang;
 $('#f1').textContent=t.f1;$('#fp').textContent=t.priv;$('#fm').textContent=t.made;
 ['#wl1','#wl2','#wl3'].forEach((s,i)=>$(s).textContent=t.wl[i]);
 $('#legend').innerHTML=t.legend.map(([k,l])=>`<span><i style="background:var(--${k})"></i>${l}</span>`).join('');
 ORDER.forEach(cc=>{const d=DATA[cc],c=CN[cc];document.querySelector(`[data-n="${cc}"]`).textContent=ar?c.ar:c.en;document.querySelector(`[data-t="${cc}"]`).textContent=ar?c.tar:c.ten;
  document.querySelector(`[data-s="${cc}"]`).textContent=`${t.places(d.n)} · ${d.archaeological} ${t.arch} · ${d.geological} ${t.geo} · ${d.ecology} ${t.eco}`});
 document.title=ar?'طبقات · Layers':'Layers · طبقات'}
$('#lang').addEventListener('click',()=>{lang=lang=='ar'?'en':'ar';store.set('lang',lang);render()});
// hover links map shape <-> card
document.querySelectorAll('.cs').forEach(p=>{const cc=p.dataset.cc;p.addEventListener('click',()=>location.href=cc+'.html');
 p.addEventListener('mouseenter',()=>document.querySelector(`.card[data-cc="${cc}"]`).classList.add('hi'));p.addEventListener('mouseleave',()=>document.querySelector(`.card[data-cc="${cc}"]`).classList.remove('hi'))});
document.querySelectorAll('.card,.bd').forEach(a=>{const cc=a.dataset.cc;a.addEventListener('mouseenter',()=>document.querySelector(`.cs[data-cc="${cc}"]`).classList.add('hi'));a.addEventListener('mouseleave',()=>document.querySelector(`.cs[data-cc="${cc}"]`).classList.remove('hi'))});
render();
function updToast(){const t=T[lang],el=$('#toast');el.innerHTML=`${t.upd}<button>${t.reload}</button>`;el.style.display='block';el.querySelector('button').onclick=()=>location.reload()}
if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').then(r=>{r.addEventListener('updatefound',()=>{const w=r.installing;if(!w)return;w.addEventListener('statechange',()=>{if(w.state=='installed'&&navigator.serviceWorker.controller)updToast()})})}).catch(()=>{}));
</script>
</body></html>
'''
if __name__ == '__main__':
    print(build())
