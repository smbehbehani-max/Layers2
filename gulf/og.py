import sys,json; sys.path.insert(0,'/tmp/w/video'); sys.path.insert(0,'/tmp/w/kit')
cc=sys.argv[1]; C=json.load(open(f'/tmp/w/gulf/{cc}/config.json',encoding='utf-8'))
N=len(json.load(open(f'/tmp/w/gulf/{cc}/data.json',encoding='utf-8'))['sites'])
src=open('/tmp/w/kit/graphics.py').read()
src=src.split("with sync_playwright() as p:")[0]   # reuse card() only
ns={}; exec(src,ns)
html=ns['card'](1200,630,False).replace('icon-kw.svg',f'icon-{cc}.svg').replace('طبقات الكويت',C['title_ar']).replace('Layers of Kuwait',C['title_en']).replace('Geology, archaeology and ecology of Kuwait',f"Geology, archaeology and ecology of {C['en']}").replace('جيولوجيا الكويت وآثارها وبيئتها',f"جيولوجيا {C['ar']} وآثارها وبيئتها").replace('80 places',f'{N} places').replace('<div class="chip"><i style="background:#e2b850"></i>Illustrated stories</div>','<div class="chip"><i style="background:#e2b850"></i>Timeline</div>').replace('<div class="chip"><i style="background:linear-gradient(115deg,#ff4fd8,#ffcf3f,#2fe0c0,#5b7cff)"></i>AI connections</div>','<div class="chip"><i style="background:#2fe0c0"></i>Live directions</div>')
open(f'/tmp/w/gulf/{cc}/_og.html','w',encoding='utf-8').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1200,'height':630}); pg.goto(f'file:///tmp/w/gulf/{cc}/_og.html'); pg.wait_for_timeout(600); pg.screenshot(path=f'/tmp/w/gulf/{cc}/site/og.png'); b.close()
from PIL import Image; Image.open(f'/tmp/w/gulf/{cc}/site/og.png').convert('RGB').save(f'/tmp/w/gulf/{cc}/site/og.png'); print('og ok')
