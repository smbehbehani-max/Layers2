import sys,os,json
sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=8918)
from playwright.sync_api import sync_playwright
R={};OUT='/tmp/w/layers/shots';U='http://127.0.0.1:8918/'
def fr(pg):
    for f in pg.frames:
        if f.name=='' and f!=pg.main_frame or f.parent_frame is pg.main_frame: return f
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,geolocation={'latitude':26.2,'longitude':50.55},permissions=['geolocation']); pg=ctx.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U,wait_until='load'); pg.wait_for_timeout(600); pg.screenshot(path=f'{OUT}/two-hero.png'); pg.screenshot(path=f'{OUT}/two-full.png',full_page=True)
    R['hub_overflow']=pg.evaluate('[document.documentElement.scrollWidth, innerWidth]')
    pg.click('.card[data-cc="bh"]'); pg.wait_for_timeout(1500); f=fr(pg)
    R['bh']=[pg.url, f.evaluate("document.querySelector('#t-title')?.textContent"), f.evaluate("D.sites.length"), f.evaluate("SHARE_BASE")]
    f.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/two-bh.png')
    sid=f.evaluate("D.sites[3].id"); f.evaluate(f"show('{sid}')"); pg.wait_for_timeout(400); R['hash_after_show']=pg.evaluate('location.hash'); R['bh_detail']=f.evaluate("document.querySelector('#det h2')?.textContent")
    f.evaluate('closeDet()'); pg.wait_for_timeout(200); R['hash_after_close']=pg.evaluate('location.hash')
    f.click('.lg[data-lg="om"]'); pg.wait_for_timeout(1500); f=fr(pg); R['om']=[pg.url, f.evaluate("document.querySelector('#t-title')?.textContent")]
    f.evaluate("welcomed=true;store.set('welcomed',true);render()"); f.click('[data-home]'); pg.wait_for_timeout(500); R['home']=[pg.url, pg.evaluate("document.body.classList.contains('open')")]
    pg.goto(U+'#kw/p=mud-volcano-z3'); pg.reload(wait_until='load'); pg.wait_for_timeout(2500); f=fr(pg); R['kw_deep']=[f.evaluate("document.querySelector('#det h2')?.textContent"), f.evaluate("STORIES.length"), f.evaluate("D.sites.length")]
    pg.screenshot(path=f'{OUT}/two-kw-deep.png')
    pg.goto(U+'#p=hegra'); pg.reload(wait_until='load'); pg.wait_for_timeout(2500); f=fr(pg); R['legacy_deep']=[pg.url, f.evaluate("document.querySelector('#det h2')?.textContent")]
    pg.goto(U+'#kw/stories'); pg.wait_for_timeout(2500); f=fr(pg); R['kw_stories']=f.evaluate("(()=>{const s=document.querySelector('#story');return s?!s.hidden:null})()")
    pg.goto(U+'#qa/live'); pg.wait_for_timeout(3000); f=fr(pg); R['qa_live']=f.evaluate("document.querySelector('#livep')?.innerText?.slice(0,60)")
    # share link built by the app
    R['share']=f.evaluate("SHARE_BASE+'#qa/p='+encodeURIComponent(D.sites[0].id)")
    # arabic persists into edition
    pg.goto(U); pg.reload(wait_until='load'); pg.wait_for_timeout(500); pg.click('#lang'); pg.wait_for_timeout(400); pg.screenshot(path=f'{OUT}/two-ar.png',full_page=True)
    pg.click('.card[data-cc="sa"]'); pg.wait_for_timeout(1500); f=fr(pg); R['sa_ar']=[f.evaluate("document.documentElement.dir"), f.evaluate("document.querySelector('#t-title')?.textContent")]
    f.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/two-sa-ar.png'); f.click('#lang')
    R['errors']=errs; ctx.close()
    ctx=b.new_context(viewport={'width':1280,'height':800}); pg=ctx.new_page(); pg.goto(U,wait_until='load'); pg.wait_for_timeout(600); pg.screenshot(path=f'{OUT}/two-desk.png',full_page=True); ctx.close(); b.close()
print(json.dumps(R,ensure_ascii=False,indent=1))
