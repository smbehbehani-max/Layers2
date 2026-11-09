import sys,os,json
sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/site',port=8912)
from playwright.sync_api import sync_playwright
R={};OUT='/tmp/w/layers/shots';os.makedirs(OUT,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); pg=ctx.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://127.0.0.1:8912/',wait_until='load'); pg.wait_for_timeout(400)
    pg.click('.card[data-cc="bh"]'); pg.wait_for_load_state('load'); pg.wait_for_timeout(800)
    R['bh_url']=pg.url;assert pg.url.endswith('bh.html'),pg.url; R['bh_title']=pg.evaluate("document.querySelector('#t-title').textContent"); R['home_btn']=pg.evaluate("!!document.querySelector('[data-home]')")
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/ed-bh.png')
    pg.click('.lg[data-lg="om"]'); pg.wait_for_load_state('load'); pg.wait_for_timeout(800); R['om_url']=pg.url; R['om_title']=pg.evaluate("document.querySelector('#t-title').textContent")
    pg.click('.lg[data-lg="kw"]'); pg.wait_for_load_state('load'); pg.wait_for_timeout(1200); R['kw_url']=pg.url; R['kw_title']=pg.evaluate("document.querySelector('#t-title').textContent")
    R['kw_stories']=pg.evaluate("(()=>{const b=document.querySelector('#stb');return b?getComputedStyle(b).display:null})()")
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/ed-kw.png')
    pg.click('[data-home]'); pg.wait_for_load_state('load'); pg.wait_for_timeout(400); R['home_url']=pg.url;assert pg.url.endswith('/'),pg.url
    # arabic persists across pages
    pg.click('#lang'); pg.wait_for_timeout(200); pg.click('.card[data-cc="sa"]'); pg.wait_for_load_state('load'); pg.wait_for_timeout(800)
    R['sa_ar']=pg.evaluate("[document.documentElement.dir, document.querySelector('#t-title').textContent, document.querySelector('[data-home]').title]")
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/ed-sa-ar.png')
    pg.click('#lang'); pg.wait_for_timeout(200)
    R['sw']=pg.evaluate("navigator.serviceWorker.getRegistrations().then(r=>r.map(x=>x.scope))")
    R['share']=pg.evaluate("typeof SHARE_BASE=='string'?SHARE_BASE:null")
    R['about']=pg.evaluate("(()=>{openAbout();const s=document.querySelector('#sheet').innerText;closeSheet();return s.slice(0,400)})()")
    R['privacy_link']=pg.evaluate("[...document.querySelectorAll('a')].map(a=>a.getAttribute('href')).filter(h=>h&&h.includes('privacy'))")
    R['errors']=errs; ctx.close(); b.close()
print(json.dumps(R,ensure_ascii=False,indent=1))
