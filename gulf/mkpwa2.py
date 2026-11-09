"""Standalone website folder for a Gulf edition: python3 mkpwa2.py <cc>"""
import os, sys, json, shutil, re
sys.path.insert(0, '/tmp/w/video')
cc = sys.argv[1]
D = f'/tmp/w/gulf/{cc}'; C = json.load(open(f'{D}/config.json', encoding='utf-8'))
OUT = f'{D}/site'; os.makedirs(OUT, exist_ok=True)
BASE, EN, AR, TEN, TAR = C['base'], C['en'], C['ar'], C['title_en'], C['title_ar']
data = json.load(open(f'{D}/data.json', encoding='utf-8')); N = len(data['sites'])
VERSION = C.get('version', '0.1.0')
h = open(f'{D}/app.html', encoding='utf-8').read()
assert h.count("const STANDALONE=false,") == 1
h = h.replace("const STANDALONE=false,", "const STANDALONE=true,").replace("APP_VERSION='1.1.0'", f"APP_VERSION='{VERSION}'")
assert h.startswith('<meta charset="utf-8">')
DESC = f"{EN}'s geology, archaeology and ecology on one bilingual map: {N} places with their sources, a timeline and live directions."
head = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#f7f8f5" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#121c1c" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Layers"><meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="application-name" content="{TEN}">
<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="canonical" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{TEN}"><meta property="og:title" content="{TEN} · {TAR}">
<meta property="og:description" content="{DESC}"><meta property="og:url" content="{BASE}"><meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TEN} · {TAR}"><meta name="twitter:description" content="{DESC}"><meta name="twitter:image" content="{BASE}og.png">
'''
h = head + h[len('<meta charset="utf-8">'):]
h = h.rstrip() + '''
<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').then(r=>{r.addEventListener('updatefound',()=>{const w=r.installing;if(!w)return;w.addEventListener('statechange',()=>{if(w.state=='installed'&&navigator.serviceWorker.controller&&typeof updToast=='function')updToast()})})}).catch(()=>{}));</script>
</html>
'''
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(h)
manifest = {"id": f"/{C['repo']}/", "name": TEN, "short_name": "Layers", "description": DESC, "start_url": "./", "scope": "./",
  "display": "standalone", "display_override": ["standalone", "minimal-ui"], "orientation": "any", "background_color": "#f7f8f5", "theme_color": "#f7f8f5",
  "lang": "en", "dir": "auto", "categories": ["education", "travel", "navigation"], "prefer_related_applications": False,
  "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}, {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
  "shortcuts": [{"name": "Go live", "short_name": "Go live", "url": "./#live", "icons": [{"src": "icon-192.png", "sizes": "192x192"}]}, {"name": "Timeline", "short_name": "Timeline", "url": "./#timeline", "icons": [{"src": "icon-192.png", "sizes": "192x192"}]}]}
json.dump(manifest, open(f'{OUT}/manifest.webmanifest', 'w'), indent=1, ensure_ascii=False)
sw = open('/tmp/w/pwa2/sw.js').read().replace("const C='layers-v5';", f"const C='layers-{cc}-v1';")
open(f'{OUT}/sw.js', 'w').write(sw)
# privacy page: the Kuwait one with names and links swapped
pv = open('/tmp/w/pwa2/privacy.html', encoding='utf-8').read()
pv = pv.replace('Layers of Kuwait', TEN).replace('طبقات الكويت', TAR).replace("Kuwait's geology, archaeology and ecology", f"{EN}'s geology, archaeology and ecology").replace('لجيولوجيا الكويت وآثارها وبيئتها', f'لجيولوجيا {AR} وآثارها وبيئتها').replace('github.com/smbehbehani-max/Layers2', f"github.com/smbehbehani-max/{C['repo']}").replace('23 October 2026', '7 November 2026').replace('23 أكتوبر 2026', '7 نوفمبر 2026')
open(f'{OUT}/privacy.html', 'w', encoding='utf-8').write(pv)
open(f'{OUT}/README.md', 'w', encoding='utf-8').write(f"# {TEN} · {TAR}\n\nBilingual map of {EN}'s geology, archaeology and ecology: {N} places with sources, a timeline and live directions. Part of Layers of the Gulf.\n\nLive site: {BASE}\n\nVersion {VERSION}.\n")
# icons from the logo generator
from srv import start
from playwright.sync_api import sync_playwright
from PIL import Image
svg = open(f'/tmp/w/logo/icon-{cc}.svg').read()
open(f'/tmp/w/logo/icon-{cc}-square.svg', 'w').write(svg.replace('rx="228"', 'rx="0"'))
start('/tmp/w/logo', 8795)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, sz, src, alpha in (('icon-192', 192, f'icon-{cc}.svg', True), ('icon-512', 512, f'icon-{cc}.svg', True), ('apple-touch-icon', 180, f'icon-{cc}-square.svg', False), ('icon-maskable-512', 512, f'icon-{cc}-square.svg', False), ('appstore-icon-1024', 1024, f'icon-{cc}-square.svg', False)):
        q = b.new_page(viewport={'width': sz, 'height': sz}); q.set_content(f'<style>body{{margin:0;background:{"transparent" if alpha else "#fff"}}}</style><img src="http://127.0.0.1:8795/{src}" width="{sz}" height="{sz}">'); q.wait_for_timeout(300)
        q.screenshot(path=f'{OUT}/{name}.png', omit_background=alpha); q.close()
    b.close()
for name in ('apple-touch-icon', 'icon-maskable-512', 'appstore-icon-1024'):
    im = Image.open(f'{OUT}/{name}.png').convert('RGB'); im.save(f'{OUT}/{name}.png')
shutil.move(f'{OUT}/appstore-icon-1024.png', f'{D}/appstore-icon-1024.png')
print('site ready', OUT, sorted(os.listdir(OUT)))
