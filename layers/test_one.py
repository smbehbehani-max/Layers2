import sys,os,json
sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=8913)
from playwright.sync_api import sync_playwright
R={};OUT='/tmp/w/layers/shots';os.makedirs(OUT,exist_ok=True);U='http://127.0.0.1:8913/'
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,geolocation={'latitude':26.2,'longitude':50.55},permissions=['geolocation']); pg=ctx.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U,wait_until='load'); pg.wait_for_timeout(600); pg.screenshot(path=f'{OUT}/one-hero.png'); pg.screenshot(path=f'{OUT}/one-full.png',full_page=True)
    R['hub_overflow']=pg.evaluate('[document.documentElement.scrollWidth, innerWidth]')
    pg.click('.card[data-cc="bh"]'); pg.wait_for_timeout(1500)
    R['bh']=[pg.url, pg.evaluate("document.querySelector('#t-title')?.textContent"), pg.evaluate("typeof D!='undefined'&&D.sites.length")]
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/one-bh.png')
    sid=pg.evaluate("D.sites[3].id"); pg.evaluate(f"show('{sid}')"); pg.wait_for_timeout(400); R['bh_hash_after_show']=pg.evaluate('location.hash'); R['bh_detail']=pg.evaluate("document.querySelector('#det h2')?.textContent")
    R['share_url']=pg.evaluate("SHARE_BASE+'#bh/p='+encodeURIComponent(sel)")
    pg.evaluate('closeDet()'); pg.wait_for_timeout(200); R['hash_after_close']=pg.evaluate('location.hash')
    # switch country via header
    pg.click('.lg[data-lg="om"]'); pg.wait_for_timeout(2500); R['om']=[pg.url, pg.evaluate("document.querySelector('#t-title')?.textContent")]
    # home
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.click('[data-home]'); pg.wait_for_timeout(2000); R['home']=[pg.url, pg.evaluate("!!document.querySelector('#explore')")]
    # deep link to kuwait place + kuwait stories
    pg.goto(U+'#kw/p=mud-volcano-z3',wait_until='load'); pg.wait_for_timeout(2500); R['kw_deep']=[pg.evaluate("document.querySelector('#det h2')?.textContent"), pg.evaluate("typeof STORIES!='undefined'&&STORIES.length"), pg.evaluate("D.sites.length")]
    pg.screenshot(path=f'{OUT}/one-kw-deep.png')
    pg.goto(U+'#p=hegra'); pg.reload(wait_until='load'); pg.wait_for_timeout(2500); R['legacy_deep']=[pg.url, pg.evaluate("document.querySelector('#det h2')?.textContent")]
    pg.goto(U+'#kw/stories',wait_until='load'); pg.wait_for_timeout(2500); R['kw_stories']=pg.evaluate("(()=>{const s=document.querySelector('#story');return s?!s.hidden:null})()")
    # live
    pg.goto(U+'#qa/live'); pg.wait_for_timeout(3000); R['qa_live']=pg.evaluate("document.querySelector('#livep')?.innerText?.slice(0,80)")
    # arabic hub
    pg.goto(U,wait_until='load'); pg.wait_for_timeout(500); pg.click('#lang'); pg.wait_for_timeout(400); pg.screenshot(path=f'{OUT}/one-ar.png',full_page=True); R['ar']=pg.evaluate("[document.documentElement.dir, document.querySelector('#h2').textContent]"); pg.click('#lang')
    R['errors']=errs; ctx.close()
    ctx=b.new_context(viewport={'width':1280,'height':800}); pg=ctx.new_page(); pg.goto(U,wait_until='load'); pg.wait_for_timeout(600); pg.screenshot(path=f'{OUT}/one-desk.png',full_page=True); ctx.close(); b.close()
print(json.dumps(R,ensure_ascii=False,indent=1))
