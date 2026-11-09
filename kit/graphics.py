"""Store icons, Open Graph image and Google Play feature graphic."""
import sys, os
sys.path.insert(0, '/tmp/w/video')
from srv import start
from playwright.sync_api import sync_playwright
from PIL import Image
OUT = '/tmp/w/kit'
PORT = 8821; start(root='/tmp/w/logo', port=PORT)

def card(W, H, feature=False):
    s = W / 1200
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:"Lora";src:url(file:///tmp/w/video/fonts/Lora-Variable.ttf);font-weight:400 700}}
@font-face{{font-family:"Lora";src:url(file:///tmp/w/video/fonts/Lora-Italic-Variable.ttf);font-weight:400 700;font-style:italic}}
@font-face{{font-family:"Inter";src:url(file:///tmp/w/video/fonts/Inter-Medium.otf)}}
@font-face{{font-family:"FS";src:url(file:///tmp/w/video/fonts/FreeSerifBold.ttf)}}
@font-face{{font-family:"DV";src:url(file:///tmp/w/video/fonts/DejaVuSans.ttf)}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}}
.bg{{position:absolute;inset:0;background:radial-gradient(120% 95% at 72% 45%,#1f5a5e 0%,#123a3e 48%,#0a2023 100%)}}
.grid{{position:absolute;inset:0;opacity:.07;background-image:linear-gradient(#ece3cf 1px,transparent 1px),linear-gradient(90deg,#ece3cf 1px,transparent 1px);background-size:{int(80*s)}px {int(80*s)}px}}
.ic{{position:absolute;left:{int(70*s)}px;top:50%;transform:translateY(-50%);width:{int(300*s)}px;height:{int(300*s)}px;filter:drop-shadow(0 {int(18*s)}px {int(40*s)}px rgba(0,0,0,.45))}}
.tx{{position:absolute;left:{int(420*s)}px;top:50%;transform:translateY(-50%);color:#fff;width:{int(740*s)}px}}
.ar{{font:700 {int(64*s)}px/1.25 "FS",serif;direction:rtl;text-align:left}}
.en{{font:600 {int(78*s)}px/1.05 "Lora",serif;letter-spacing:-.01em;margin-top:{int(2*s)}px}}
.rule{{width:{int(120*s)}px;height:{int(4*s)}px;border-radius:3px;background:linear-gradient(115deg,#ff4fd8,#ffcf3f 32%,#2fe0c0 64%,#5b7cff);margin:{int(20*s)}px 0 {int(16*s)}px}}
.tag{{font:{int(26*s)}px/1.4 "Inter",sans-serif;color:rgba(246,236,217,.9)}}
.tag .a{{font-family:"DV",sans-serif;direction:rtl;display:block;font-size:{int(24*s)}px;margin-top:{int(4*s)}px}}
.chips{{display:flex;gap:{int(10*s)}px;margin-top:{int(22*s)}px}}
.chip{{font:600 {int(19*s)}px/1 "Inter",sans-serif;color:#fff;padding:{int(10*s)}px {int(14*s)}px;border-radius:99px;background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16);display:flex;gap:{int(8*s)}px;align-items:center}}
.chip i{{width:{int(10*s)}px;height:{int(10*s)}px;border-radius:50%}}
</style><div class="bg"></div><div class="grid"></div>
<img class="ic" src="http://127.0.0.1:{PORT}/icon-kw.svg">
<div class="tx"><div class="ar">طبقات الكويت</div><div class="en">Layers of Kuwait</div><div class="rule"></div>
<div class="tag">Geology, archaeology and ecology of Kuwait on one bilingual map<span class="a">جيولوجيا الكويت وآثارها وبيئتها على خريطة واحدة بلغتين</span></div>
<div class="chips"><div class="chip"><i style="background:#e08a4f"></i>80 places</div><div class="chip"><i style="background:#e2b850"></i>Illustrated stories</div><div class="chip"><i style="background:linear-gradient(115deg,#ff4fd8,#ffcf3f,#2fe0c0,#5b7cff)"></i>AI connections</div>{'' if feature else '<div class="chip"><i style="background:#62c98e"></i>Works offline</div>'}</div></div>'''

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for name, W, H, feat in (('og', 1200, 630, False), ('play-feature-graphic-1024x500', 1024, 500, True)):
        open('/tmp/w/kit/_g.html', 'w', encoding='utf-8').write(card(W, H, feat))
        pg.set_viewport_size({'width': W, 'height': H}); pg.goto('file:///tmp/w/kit/_g.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'{OUT}/{name}.png')
    # icons: full-bleed square for the stores
    for sz, name in ((1024, 'appstore-icon-1024'), (512, 'play-icon-512')):
        q = b.new_page(viewport={'width': sz, 'height': sz})
        q.set_content(f'<style>body{{margin:0}}</style><img src="http://127.0.0.1:{PORT}/icon-kw-square.svg" width="{sz}" height="{sz}">'); q.wait_for_timeout(400)
        q.screenshot(path=f'{OUT}/{name}.png'); q.close()
    b.close()
for name in ('appstore-icon-1024', 'play-icon-512', 'og', 'play-feature-graphic-1024x500'):
    im = Image.open(f'{OUT}/{name}.png').convert('RGB'); im.save(f'{OUT}/{name}.png'); print(name, im.size, im.mode)
