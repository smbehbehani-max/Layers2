import sys; sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=int(sys.argv[1]))
from playwright.sync_api import sync_playwright
from PIL import Image
U=f'http://127.0.0.1:{sys.argv[1]}/'
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,kw in (('m',dict(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)),('p',dict(viewport={'width':1280,'height':800}))):
        ctx=b.new_context(**kw); pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(U+('mobile.html' if name=='m' else 'index.html')); pg.wait_for_timeout(4200); pg.screenshot(path=f'shots/v5{name}1.png')
        pg.evaluate("document.querySelector('#one').scrollIntoView()"); pg.wait_for_timeout(4300); pg.screenshot(path=f'shots/v5{name}2.png')
        pg.wait_for_timeout(6000); pg.screenshot(path=f'shots/v5{name}2b.png')
        pg.evaluate("document.querySelector('#ai').scrollIntoView()"); pg.wait_for_timeout(1500); pg.screenshot(path=f'shots/v5{name}3.png')
        pg.evaluate("document.querySelector('#explore').scrollIntoView()"); pg.wait_for_timeout(1200); pg.screenshot(path=f'shots/v5{name}4.png')
        pg.evaluate("location.hash='#app'"); pg.wait_for_timeout(800); pg.screenshot(path=f'shots/v5{name}5.png')
        ctx.close()
    b.close()
print('errors',errs)
for name,sz in (('m',(390,844)),('p',(640,400))):
    ims=[Image.open(f'shots/v5{name}{i}.png').resize(sz) for i in ['1','2','2b','3','4','5']]
    o=Image.new('RGB',(sz[0]*3+20,sz[1]*2+10),'white')
    for i,x in enumerate(ims): o.paste(x,((i%3)*(sz[0]+10),(i//3)*(sz[1]+10)))
    o.save(f'shots/v5{name}.png')
