import sys; sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=int(sys.argv[1]))
from playwright.sync_api import sync_playwright
from PIL import Image
U=f'http://127.0.0.1:{sys.argv[1]}/'
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U+'mobile.html#app'); pg.wait_for_timeout(1200); pg.screenshot(path='shots/s8a.png')
    pg.evaluate("document.querySelector('#hviews button[data-v=tl]').click()"); pg.wait_for_timeout(500); pg.screenshot(path='shots/s8b.png')
    pg.evaluate("document.querySelector('#hmodes button[data-m=e]').click()"); pg.wait_for_timeout(500); pg.screenshot(path='shots/s8c.png')
    pg.evaluate("document.querySelector('#hviews button[data-v=map]').click()"); pg.wait_for_timeout(500); pg.screenshot(path='shots/s8d.png')
    pg.evaluate("document.querySelector('#hviews button[data-v=cmp]').click()"); pg.wait_for_timeout(500); pg.screenshot(path='shots/s8e.png')
    pg.evaluate("document.querySelector('#abar .fl button[data-go=bh]').click()"); 
    for i,t in enumerate([450,700,1200]): pg.wait_for_timeout(t); pg.screenshot(path=f'shots/s8f{i}.png')
    pg.wait_for_timeout(3000); pg.screenshot(path='shots/s8g.png')
    ctx.close(); b.close()
print(errs)
ims=[Image.open(f'shots/s8{c}.png').resize((390,844)) for c in ['a','b','c','d','e','f0','f1','f2','g']]
o=Image.new('RGB',(400*5-10,844*2+10),'white')
for i,x in enumerate(ims): o.paste(x,((i%5)*400,(i//5)*854))
o.save('shots/s8.png')
