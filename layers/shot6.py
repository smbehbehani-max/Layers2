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
        pg.goto(U+('mobile.html' if name=='m' else 'index.html')); pg.wait_for_timeout(5500); pg.screenshot(path=f'shots/v6{name}1.png')
        pg.evaluate("document.querySelector('#explore').scrollIntoView()"); pg.wait_for_timeout(1200); pg.screenshot(path=f'shots/v6{name}4.png')
        pg.evaluate("location.hash='#app'"); pg.wait_for_timeout(800); pg.screenshot(path=f'shots/v6{name}5.png')
        pg.evaluate("document.querySelector('#ah-tl').scrollIntoView()"); pg.wait_for_timeout(600); pg.screenshot(path=f'shots/v6{name}6.png')
        pg.evaluate("document.querySelector('#ah-ta').scrollIntoView()"); pg.wait_for_timeout(600); pg.screenshot(path=f'shots/v6{name}7.png')
        # open a country from the home flags: the toggle animates, no curtain
        pg.evaluate("document.querySelector('#abar .fl button[data-go=qa]').click()"); pg.wait_for_timeout(250); pg.screenshot(path=f'shots/v6{name}8.png')
        pg.wait_for_timeout(3500); pg.screenshot(path=f'shots/v6{name}9.png')
        print(name, 'curtain' , pg.evaluate("!!document.querySelector('#curtain')"), 'open', pg.evaluate("document.body.className"), pg.evaluate("location.hash"))
        ctx.close()
    b.close()
print('errors',errs)
for name,sz in (('m',(390,844)),('p',(640,400))):
    ims=[Image.open(f'shots/v6{name}{i}.png').resize(sz) for i in ['1','4','5','6','7','8','9']]
    o=Image.new('RGB',(sz[0]*4+30,sz[1]*2+10),'white')
    for i,x in enumerate(ims): o.paste(x,((i%4)*(sz[0]+10),(i//4)*(sz[1]+10)))
    o.save(f'shots/v6{name}.png')
