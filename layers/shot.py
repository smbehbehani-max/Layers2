import sys,os
sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/site',port=8911)
from playwright.sync_api import sync_playwright
url=sys.argv[1] if len(sys.argv)>1 else 'index.html'; out=sys.argv[2] if len(sys.argv)>2 else '/tmp/w/layers/shots/hub'
os.makedirs('/tmp/w/layers/shots',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); errs=[]
    for name,vp,mob in (('phone',{'width':390,'height':844},True),('desk',{'width':1280,'height':800},False)):
        ctx=b.new_context(viewport=vp,device_scale_factor=2 if mob else 1,is_mobile=mob,has_touch=mob); pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(f'http://127.0.0.1:8911/{url}',wait_until='load'); pg.wait_for_timeout(600); pg.screenshot(path=f'{out}-{name}.png',full_page=True)
        if name=='phone' and 'index' in url:
            pg.click('#lang'); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}-phone-ar.png',full_page=True); pg.click('#lang')
        ctx.close()
    b.close(); print('errors',errs)
