"""Store screenshots: capture the app at each store size, then compose a caption band above each capture."""
import sys, os, shutil, json, time
sys.path.insert(0, '/tmp/w/video')
from srv import start
from playwright.sync_api import sync_playwright

SH = '/tmp/w/shots'                      # app copy with local fonts for rendering
if os.path.exists(SH): shutil.rmtree(SH)
shutil.copytree('/tmp/w/pwa2', SH)
os.symlink('/tmp/w/video/fonts', f'{SH}/fonts')
h = open(f'{SH}/index.html', encoding='utf-8').read()
i = h.find('<link rel="stylesheet" href="https://fonts.googleapis.com'); j = h.find('>', i) + 1
assert i > 0
h = h[:i] + '<link rel="stylesheet" href="fonts2.css">' + h[j:]
open(f'{SH}/index.html', 'w', encoding='utf-8').write(h)
open(f'{SH}/fonts2.css', 'w').write('''
@font-face{font-family:"Newsreader";src:url(fonts/Lora-Variable.ttf) format("truetype");font-weight:400 700;font-style:normal}
@font-face{font-family:"Newsreader";src:url(fonts/Lora-Italic-Variable.ttf) format("truetype");font-weight:400 700;font-style:italic}
@font-face{font-family:"Instrument Sans";src:url(fonts/Inter-Regular.otf);font-weight:400}
@font-face{font-family:"Instrument Sans";src:url(fonts/Inter-Medium.otf);font-weight:500}
@font-face{font-family:"Instrument Sans";src:url(fonts/Inter-SemiBold.otf);font-weight:600}
@font-face{font-family:"Instrument Sans";src:url(fonts/Inter-Bold.otf);font-weight:700}
@font-face{font-family:"Amiri";src:url(fonts/FreeSerif.ttf);font-weight:400 500;unicode-range:U+0600-06FF,U+0750-077F,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}
@font-face{font-family:"Amiri";src:url(fonts/FreeSerifBold.ttf);font-weight:600 800;unicode-range:U+0600-06FF,U+0750-077F,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}
@font-face{font-family:"Amiri";src:url(fonts/Lora-Variable.ttf) format("truetype");font-weight:400 700}
@font-face{font-family:"IBM Plex Sans Arabic";src:url(fonts/DejaVuSans.ttf);font-weight:400 500;unicode-range:U+0600-06FF,U+0750-077F,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}
@font-face{font-family:"IBM Plex Sans Arabic";src:url(fonts/DejaVuSans-Bold.ttf);font-weight:600 800;unicode-range:U+0600-06FF,U+0750-077F,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}
@font-face{font-family:"IBM Plex Sans Arabic";src:url(fonts/Inter-Regular.otf);font-weight:400}
@font-face{font-family:"IBM Plex Sans Arabic";src:url(fonts/Inter-Medium.otf);font-weight:500}
@font-face{font-family:"IBM Plex Sans Arabic";src:url(fonts/Inter-SemiBold.otf);font-weight:600}
''')
PORT = 8820; start(root=SH, port=PORT)
OUT = '/tmp/w/kit/screenshots'; RAW = '/tmp/w/kit/raw'
for d in (OUT, RAW): os.makedirs(d, exist_ok=True)

CAP = {'en': [
  ('80 places, from deep time to today', 'Geology, archaeology and ecology of Kuwait on one map'),
  ('Every place with its sources', 'Published research, references and field data'),
  ('Illustrated stories, true and imagined', 'Explorer mode turns science into stories'),
  ('Travel through 100 million years', 'A timeline from the Cretaceous to today'),
  ('AI connects the dots', 'Ideas worth testing, always marked as unproven'),
  ('Live directions to the nearest place', 'Distance and bearing as you walk')],
 'ar': [
  ('80 موقعًا من الزمن السحيق حتى اليوم', 'جيولوجيا الكويت وآثارها وبيئتها على خريطة واحدة'),
  ('كل موقع بمصادره', 'أبحاث منشورة ومراجع وبيانات ميدانية'),
  ('قصص مصوّرة، حقيقية ومتخيّلة', 'وضع المستكشف يحوّل العلم إلى حكايات'),
  ('رحلة عبر 100 مليون سنة', 'خط زمني من العصر الطباشيري حتى اليوم'),
  ('الذكاء الاصطناعي يربط النقاط', 'أفكار تستحق الاختبار، معلَّمة دائمًا كغير مثبتة'),
  ('إرشادات حيّة إلى أقرب موقع', 'المسافة والاتجاه وأنت تمشي')]}
NAMES = ['map', 'place', 'story', 'timeline', 'ai', 'live']
# (name, total W, total H, band H, device scale)
SIZES = [('iphone69', 1320, 2868, 540, 3), ('iphone-medium', 1206, 2622, 489, 3), ('play', 1080, 1920, 400, 3), ('ipad13', 2064, 2752, 520, 2)]
ONLY = os.environ.get('ONLY')
if ONLY: SIZES = [z for z in SIZES if z[0] == ONLY]

def prep(pg, lang, mode):
    pg.evaluate(f"""(()=>{{welcomed=true;store.set('welcomed',true);
      if(typeof closeStory=='function')closeStory();if(typeof closeSheet=='function')closeSheet();closeDet();if(live.on)stopLive();
      if(view!='map')switchView('map');
      if(lang!='{lang}'){{lang='{lang}';store.set('lang',lang)}} mode='{mode}';store.set('mode',mode);chrome();vb=home.slice();setVB();}})()""")
    pg.wait_for_timeout(250)

STATES = [
  ('r', ""),
  ('r', "show('bahra-1');setTimeout(()=>{const d=document.querySelector('#det'),el=d.querySelector('ul.refs');if(el)d.scrollTop=el.offsetTop-110},150)"),
  ('e', "openStory('bahrah')"),
  ('e', "switchView('tl');setTimeout(()=>{const t=document.querySelector('#tl');t.scrollTop=140},100)"),
  ('e', "document.querySelector('#zl').click();show('spec-bahra-quake')"),
  ('r', "startLive()"),
]

with sync_playwright() as p:
    b = p.chromium.launch()
    for sname, W, H, BH, dsf in SIZES:
        lw, lh = W // dsf, (H - BH) // dsf
        for lang in ('en', 'ar'):
            ctx = b.new_context(viewport={'width': lw, 'height': lh}, device_scale_factor=dsf, is_mobile=sname != 'ipad13', has_touch=True,
                                geolocation={'latitude': 29.386, 'longitude': 47.74}, permissions=['geolocation'], locale='en-US')
            pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f'http://127.0.0.1:{PORT}/index.html', wait_until='load'); pg.wait_for_timeout(600)
            pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
            for k, (mode, js) in enumerate(STATES):
                prep(pg, lang, mode)
                if js: pg.evaluate(js)
                pg.wait_for_timeout(1600 if k == 5 else 500)
                raw = f'{RAW}/{sname}-{lang}-{k+1}-{NAMES[k]}.png'
                pg.screenshot(path=raw)
            ctx.close()
            print(sname, lang, 'errors', errs[:3], flush=True)
    # compose
    page = b.new_page()
    for sname, W, H, BH, dsf in SIZES:
        for lang in ('en', 'ar'):
            for k in range(6):
                raw = f'{RAW}/{sname}-{lang}-{k+1}-{NAMES[k]}.png'
                t, sub = CAP[lang][k]
                rtl = lang == 'ar'
                tf = '"FS",serif' if rtl else '"Lora",serif'
                sf = '"DV",sans-serif' if rtl else '"Inter",sans-serif'
                sc = W / 1320
                html = f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:"Lora";src:url(file:///tmp/w/video/fonts/Lora-Italic-Variable.ttf);font-weight:400 700;font-style:italic}}
@font-face{{font-family:"Lora";src:url(file:///tmp/w/video/fonts/Lora-Variable.ttf);font-weight:400 700}}
@font-face{{font-family:"Inter";src:url(file:///tmp/w/video/fonts/Inter-Medium.otf)}}
@font-face{{font-family:"FS";src:url(file:///tmp/w/video/fonts/FreeSerifBold.ttf)}}
@font-face{{font-family:"DV";src:url(file:///tmp/w/video/fonts/DejaVuSans.ttf)}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#0c2629}}
.band{{position:absolute;left:0;top:0;width:{W}px;height:{BH}px;background:radial-gradient(120% 95% at 72% 45%,#1f5a5e 0%,#123a3e 48%,#0a2023 100%);color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 {int(70*sc)}px;box-sizing:border-box;direction:{'rtl' if rtl else 'ltr'}}}
.band::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:{int(6*sc)}px;background:linear-gradient(115deg,#ff4fd8,#ffcf3f 32%,#2fe0c0 64%,#5b7cff)}}
h1{{margin:0;font:{'700' if rtl else 'italic 600'} {int(86*sc)}px/1.22 {tf};text-wrap:balance;letter-spacing:{0 if rtl else '-0.01em'}}}
p{{margin:{int(18*sc)}px 0 0;font:{int(38*sc)}px/1.35 {sf};color:rgba(246,236,217,.88);text-wrap:balance}}
img{{position:absolute;left:0;top:{BH}px;width:{W}px;height:{H-BH}px;object-fit:cover;object-position:top}}
</style><div class="band"><h1>{t}</h1><p>{sub}</p></div><img src="file://{raw}">'''
                tmp = f'/tmp/w/kit/_c.html'; open(tmp, 'w', encoding='utf-8').write(html)
                page.set_viewport_size({'width': W, 'height': H}); page.goto('file://' + tmp); page.wait_for_timeout(250)
                page.screenshot(path=f'{OUT}/{sname}-{lang}-{k+1}-{NAMES[k]}.png', clip={'x': 0, 'y': 0, 'width': W, 'height': H})
    b.close()
print('done')
