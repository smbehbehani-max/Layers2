"""Assemble the single 'Layers' site: hub + six country editions -> /tmp/w/layers/site/"""
import os, re, shutil, json, subprocess, sys
sys.path.insert(0, '/tmp/w/layers')
import hub
OUT = '/tmp/w/layers/site'
BASE = 'https://smbehbehani-max.github.io/Layers2/'
VERSION = '2.0.0'
SRC = {'kw': '/tmp/w/pwa2', 'bh': '/tmp/w/gulf/bh/site', 'qa': '/tmp/w/gulf/qa/site', 'ae': '/tmp/w/gulf/ae/site', 'om': '/tmp/w/gulf/om/site', 'sa': '/tmp/w/gulf/sa/site'}
OLD = {'kw': 'Layers2', 'bh': 'Layers-Bahrain', 'qa': 'Layers-Qatar', 'ae': 'Layers-UAE', 'om': 'Layers-Oman', 'sa': 'Layers-Saudi'}
PLAIN = open('/tmp/w/logo/icon-plain.svg').read()
def plain_small():
    s = PLAIN
    for i in ['sky', 'sun', 'sq', 'fc', 'sh']:
        s = s.replace(f'id="{i}"', f'id="lghome-{i}"').replace(f'url(#{i})', f'url(#lghome-{i})')
    return s.replace('xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"', 'viewBox="0 0 1024 1024" aria-hidden="true"')
HOME_LABEL = {'en': 'Layers — all countries', 'ar': 'طبقات — كل الدول'}
def patch(cc, h):
    old = OLD[cc]
    # URLs
    h = h.replace(f'https://smbehbehani-max.github.io/{old}/og.png', f'{BASE}og-{cc}.png').replace(f'https://smbehbehani-max.github.io/{old}/', f'{BASE}{cc}.html')
    # the Kuwait app's old address can equal the new site address (both Layers2): ignore the new address in this check
    assert 'smbehbehani-max.github.io/' + old not in h.replace(BASE, ''), cc
    assert h.count("register('sw.js')") == 1, cc
    # brand row: other countries navigate, home button goes to hub
    assert h.count('openSoon(b.dataset.lg)') == 1, cc
    h = h.replace('openSoon(b.dataset.lg)', 'goCountry(b.dataset.lg)')
    nav = '<nav class="lgs" aria-label="Other Layers apps">'
    assert h.count(nav) == 1, cc
    h = h.replace(nav, nav + f'<button class="lg lghome" data-home="1" title="{HOME_LABEL["en"]}" aria-label="{HOME_LABEL["en"]}">{plain_small()}</button>')
    css = '.lg.lghome svg{display:block}.lg.lghome{margin-inline-end:4px;padding-inline-end:6px;border-inline-end:1px solid var(--line);border-radius:0}'
    h = h.replace('</style>', css + '</style>', 1)
    js = ("function goCountry(k){location.href=k+'.html'}"
          "document.querySelector('[data-home]').addEventListener('click',()=>{location.href='./'});"
          "(function(){const b=document.querySelector('[data-home]'),n=b.parentNode;if(n.firstChild!==b)n.insertBefore(b,n.firstChild)})();"
          "(function(){const b=document.querySelector('[data-home]');const f=()=>{const l=(typeof lang=='string'&&lang=='ar')?'ar':'en';b.title=b.ariaLabel=" + json.dumps(HOME_LABEL, ensure_ascii=False) + "[l]};f();const lb=document.querySelector('#lang');if(lb)lb.addEventListener('click',()=>setTimeout(f,0))})();")
    # place the JS right before the SW registration script (end of document)
    anchor = "<script>if('serviceWorker' in navigator)"
    assert h.count(anchor) == 1, cc
    h = h.replace(anchor, '<script>' + js + '</script>\n' + anchor)
    # version
    h = re.sub(r"APP_VERSION='[^']*'", f"APP_VERSION='{VERSION}'", h, count=1)
    return h

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    data = hub.build()
    for cc, src in SRC.items():
        h = open(f'{src}/index.html', encoding='utf-8').read()
        open(f'{OUT}/{cc}.html', 'w', encoding='utf-8').write(patch(cc, h))
        shutil.copy(f'{src}/og.png', f'{OUT}/og-{cc}.png')
    # root files
    man = {
        'id': '/Layers/', 'name': 'Layers · طبقات', 'short_name': 'Layers', 'description': 'Geology, archaeology and ecology of the Arabian Gulf, country by country, in Arabic and English.',
        'start_url': './', 'scope': './', 'display': 'standalone', 'orientation': 'any', 'background_color': '#f7f8f5', 'theme_color': '#f7f8f5', 'lang': 'en', 'dir': 'ltr',
        'categories': ['education', 'travel', 'navigation'],
        'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}, {'src': 'icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}],
        'shortcuts': [{'name': n, 'url': f'{cc}.html', 'icons': [{'src': 'icon-192.png', 'sizes': '192x192'}]} for cc, n in [('kw', 'Layers of Kuwait'), ('sa', 'Layers of Saudi Arabia'), ('bh', 'Layers of Bahrain'), ('qa', 'Layers of Qatar')]],
    }
    json.dump(man, open(f'{OUT}/manifest.webmanifest', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    pages = ['./', 'index.html'] + [f'{cc}.html' for cc in SRC] + ['privacy.html', 'manifest.webmanifest']
    sw = f"""const CACHE='layers-v{VERSION}';
const PAGES={json.dumps(pages)};
const ASSETS=['icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png'].concat({json.dumps([f'og-{cc}.png' for cc in SRC])});
self.addEventListener('install',e=>{{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS).then(()=>Promise.allSettled(PAGES.map(p=>c.add(p))))).then(()=>self.skipWaiting()))}});
self.addEventListener('activate',e=>{{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))}});
self.addEventListener('fetch',e=>{{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 const u=new URL(r.url);const page=r.mode==='navigate'||u.pathname.endsWith('/')||u.pathname.endsWith('.html');
 if(page){{e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp));return res}}).catch(()=>caches.match(r).then(m=>m||caches.match(u.pathname.endsWith('/')?u.pathname+'index.html':u.pathname.replace(/index\\.html$/,'')))))}}
 else{{e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{{const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp));return res}})))}}}});
"""
    open(f'{OUT}/sw.js', 'w').write(sw)
    # icons: plain camel (no flag)
    subprocess.run(['python3', '/tmp/w/layers/icons.py'], check=True)
    # privacy
    p = open('/tmp/w/pwa2/privacy.html', encoding='utf-8').read()
    p = p.replace('Layers of Kuwait', 'Layers').replace('طبقات الكويت', 'طبقات').replace('https://smbehbehani-max.github.io/Layers2/', BASE)
    open(f'{OUT}/privacy.html', 'w', encoding='utf-8').write(p)
    readme = f"""# Layers · طبقات

One bilingual (Arabic/English) map app for the geology, archaeology and ecology of the Arabian Gulf countries.

- `index.html` — front page: choose a country.
- `kw.html`, `sa.html`, `bh.html`, `qa.html`, `ae.html`, `om.html` — the country editions (Kuwait, Saudi Arabia, Bahrain, Qatar, UAE, Oman).
- `manifest.webmanifest`, `sw.js`, icons — one installable app (PWA) that works offline.

Live: {BASE}

Every place carries its sources. Illustrated stories and AI speculation (Kuwait edition) are marked as such.
"""
    open(f'{OUT}/README.md', 'w').write(readme)
    return data

if __name__ == '__main__':
    print(build())
    for root, ds, fs in os.walk(OUT):
        for f in fs: print(os.path.join(root, f).replace(OUT + '/', ''), os.path.getsize(os.path.join(root, f)))
