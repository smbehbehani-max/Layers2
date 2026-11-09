import sys
"""Build the ready-to-host website folder from one/index.html and one/mobile.html.

Output: /tmp/w/layers/website/  (upload the whole folder to any static host)
"""
import os, re, shutil, json

SRC = '/tmp/w/layers/one'
ASSETS = '/tmp/w/layers/site'
OUT = '/tmp/w/layers/website'
OLD_BASE = "BASE='https://smbehbehani-max.github.io/Layers/'"
NEW_BASE = ("BASE=(/^https?:$/.test(location.protocol)?location.href.split(/[?#]/)[0]"
            ".replace(/(index|mobile)\\.html$/,''):'https://smbehbehani-max.github.io/Layers/')")
CC = {'kw': ('Kuwait', 'الكويت'), 'sa': ('Saudi Arabia', 'السعودية'), 'bh': ('Bahrain', 'البحرين'),
      'qa': ('Qatar', 'قطر'), 'ae': ('UAE', 'الإمارات'), 'om': ('Oman', 'عُمان')}

# phone <-> computer switch, placed first in <head> so it runs before the 11 MB page loads
TO_MOBILE = ("<script>(function(){try{if(/[?&]desktop=1/.test(location.search))return;"
             "if(matchMedia('(max-width:760px)').matches||(matchMedia('(pointer:coarse)').matches&&Math.min(screen.width,screen.height)<600))"
             "location.replace('mobile.html'+location.search+location.hash)}catch(e){}})()</script>")
TO_PC = ("<script>(function(){try{if(/[?&]mobile=1/.test(location.search))return;"
         "if(matchMedia('(min-width:1024px) and (pointer:fine)').matches)"
         "location.replace('./'+location.search+location.hash)}catch(e){}})()</script>")


def page(name, inject):
    h = open(os.path.join(SRC, name), encoding='utf-8').read()
    assert OLD_BASE in h, 'share base not found'
    h = h.replace(OLD_BASE, NEW_BASE)
    # register the offline worker on any https host, not only github.io
    h = h.replace("location.protocol=='https:'&&/github\\.io$/.test(location.hostname)", "location.protocol=='https:'")
    h = h.replace('<head><meta charset="utf-8">', '<head><meta charset="utf-8">' + inject, 1)
    h, n = re.subn(r'<link rel="manifest" href="data:[^"]*">', '<link rel="manifest" href="manifest.webmanifest">', h, count=1)
    assert n == 1, 'manifest link not found'
    h = split_editions(h)
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(h)


OPEN_OLD = "function openCC(cc,sub,minMs){var el=document.getElementById('ed-'+cc);if(!el||!CN[cc])return;"
OPEN_NEW = (OPEN_OLD +
    "if(el.dataset.src&&!el.textContent){if(el._ld)return;el._ld=1;document.body.classList.add('edload');"
    "edGet(el).then(function(){el._ld=0;document.body.classList.remove('edload');openCC(cc,sub,minMs)},"
    "function(){el._ld=0;document.body.classList.remove('edload')});return}")
# fetch an edition file once; also used to warm it when a finger or mouse reaches a country
LOADER = ("<script>function edGet(el){if(el.textContent)return Promise.resolve();if(!el._p)el._p=fetch(el.dataset.src)"
          ".then(function(r){if(!r.ok)throw new Error(r.status);return r.text()}).then(function(t){el.textContent=t},function(e){el._p=null;throw e});return el._p}"
          "['pointerover','touchstart','focusin'].forEach(function(ev){addEventListener(ev,function(e){var a=e.target.closest&&e.target.closest('[data-cc]');"
          "if(a){var el=document.getElementById('ed-'+a.getAttribute('data-cc'));if(el&&el.dataset.src)edGet(el).catch(function(){})}},{passive:true})});</script>"
          "<style>body.edload,body.edload *{cursor:progress!important}body.edload::after{content:'';position:fixed;left:0;top:0;height:3px;width:40%;z-index:99999;"
          "background:linear-gradient(90deg,transparent,#c99a2e,transparent);animation:edl 1s linear infinite}@keyframes edl{from{transform:translateX(-100%)}to{transform:translateX(250%)}}</style>")
WRITTEN = set()


def split_editions(h):
    """Move each country edition out of the page into ed-<cc>.html, loaded only when that country is opened."""
    assert OPEN_OLD in h, 'openCC not found'
    h = h.replace(OPEN_OLD, OPEN_NEW, 1)
    def cut(m):
        cc, body = m.group(1), m.group(2)
        page = body.replace('<\\/script', '</script')
        f = os.path.join(OUT, f'ed-{cc}.html')
        if cc in WRITTEN:
            assert open(f, encoding='utf-8').read() == page, f'edition {cc} differs between pc and phone'
        else:
            open(f, 'w', encoding='utf-8').write(page); WRITTEN.add(cc)
        return f'<script type="text/plain" id="ed-{cc}" data-src="ed-{cc}.html"></script>'
    h, n = re.subn(r'<script type="text/plain" id="ed-([a-z]{2})">(.*?)</script>', cut, h, flags=re.S)
    assert n == 6, f'expected 6 editions, found {n}'
    return h.replace('</head>', LOADER + '</head>', 1)


def share_page(cc):
    en, ar = CC[cc]
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Layers of {en} · LAYERS by GEOHERITAGE</title>
<meta name="description" content="The geology, archaeology and ecology of {en} on one bilingual map. طبقات {ar}: الجيولوجيا والآثار والبيئة على خريطة واحدة.">
<meta property="og:title" content="Layers of {en} · طبقات {ar}">
<meta property="og:description" content="Geology, archaeology and ecology on one bilingual map.">
<meta property="og:image" content="og-{cc}.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="icon-192.png">
<script>(function(){{var h=location.hash.replace(/^#/,'');location.replace('./#{cc}'+(h?'/'+h:''))}})()</script>
</head><body style="font-family:system-ui;padding:24px"><a href="./#{cc}">Open Layers of {en} · افتح طبقات {ar}</a></body></html>
'''


SW = '''const CACHE='layers-web-%s';
const CORE=['./','index.html','mobile.html','privacy.html','manifest.webmanifest','icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png'];
const LATER=['kw','sa','bh','qa','ae','om'].map(c=>'ed-'+c+'.html');
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>Promise.allSettled(CORE.map(p=>c.add(p)))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{caches.open(CACHE).then(c=>Promise.allSettled(LATER.map(p=>c.match(p).then(m=>m||c.add(p)))));e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 e.respondWith(fetch(r).then(res=>{if(res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp))}return res}).catch(()=>caches.match(r,{ignoreSearch:true}).then(m=>m||caches.match('./'))))});
'''


def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    page('index.html', TO_MOBILE)
    page('mobile.html', TO_PC)
    for f in ['apple-touch-icon.png', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'privacy.html'] + [f'og-{c}.png' for c in CC]:
        shutil.copy(os.path.join(ASSETS, f), OUT)
    for c in CC:
        open(os.path.join(OUT, f'{c}.html'), 'w', encoding='utf-8').write(share_page(c))
    m = json.load(open('/tmp/w/layers/one-extras/manifest.webmanifest', encoding='utf-8'))
    m['id'] = './'; m['name'] = 'LAYERS by GEOHERITAGE · طبقات'
    m['shortcuts'] = [{'name': f'Layers of {CC[c][0]}', 'url': f'./#{c}', 'icons': [{'src': 'icon-192.png', 'sizes': '192x192'}]} for c in CC]
    json.dump(m, open(os.path.join(OUT, 'manifest.webmanifest'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    import time
    open(os.path.join(OUT, 'sw.js'), 'w').write(SW % time.strftime('%Y%m%d%H%M'))
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n')
    open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(
        '<!doctype html><meta charset="utf-8"><title>Layers</title><script>location.replace("./")</script><a href="./">Layers</a>')
    shutil.copy('/tmp/w/layers/website_README.md', os.path.join(OUT, 'README.md'))
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)))


if __name__ == '__main__':
    main()
    import make_places; make_places.SITE = (sys.argv[1] if len(sys.argv) > 1 else make_places.SITE).rstrip('/') + '/'; make_places.main()
