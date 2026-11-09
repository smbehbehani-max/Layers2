import sys, shutil, os
sys.path.insert(0, '/tmp/w/video'); from srv import start
from playwright.sync_api import sync_playwright
from PIL import Image
OUT = '/tmp/w/layers/site'
svg = open('/tmp/w/logo/icon-plain.svg').read()
open('/tmp/w/logo/icon-plain-square.svg', 'w').write(svg.replace('rx="228"', 'rx="0"'))
start('/tmp/w/logo', 8796)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, sz, src, alpha in (('icon-192', 192, 'icon-plain.svg', True), ('icon-512', 512, 'icon-plain.svg', True), ('apple-touch-icon', 180, 'icon-plain-square.svg', False), ('icon-maskable-512', 512, 'icon-plain-square.svg', False), ('appstore-icon-1024', 1024, 'icon-plain-square.svg', False)):
        q = b.new_page(viewport={'width': sz, 'height': sz}); q.set_content(f'<style>body{{margin:0;background:{"transparent" if alpha else "#fff"}}}</style><img src="http://127.0.0.1:8796/{src}" width="{sz}" height="{sz}">'); q.wait_for_timeout(300)
        q.screenshot(path=f'{OUT}/{name}.png', omit_background=alpha); q.close()
    b.close()
for name in ('apple-touch-icon', 'icon-maskable-512', 'appstore-icon-1024'):
    Image.open(f'{OUT}/{name}.png').convert('RGB').save(f'{OUT}/{name}.png')
shutil.move(f'{OUT}/appstore-icon-1024.png', '/tmp/w/layers/appstore-icon-1024.png')
