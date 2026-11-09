import sys; sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=int(sys.argv[1]))
from playwright.sync_api import sync_playwright
from PIL import Image
U=f'http://127.0.0.1:{sys.argv[1]}/'
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); pg=ctx.new_page()
    pg.goto(U+'mobile.html'); pg.wait_for_timeout(1200); pg.screenshot(path='shots/s7a.png')   # camel at start
    pg.wait_for_timeout(4500); pg.screenshot(path='shots/s7b.png')
    pg.evaluate("document.querySelector('#one').scrollIntoView()"); pg.wait_for_timeout(2600); pg.screenshot(path='shots/s7c.png')
    pg.evaluate("document.querySelector('#ai').scrollIntoView()"); pg.wait_for_timeout(1500); pg.screenshot(path='shots/s7d.png')
    pg.evaluate("document.querySelector('#why').scrollIntoView()"); pg.wait_for_timeout(1500); pg.screenshot(path='shots/s7e.png')
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300); pg.evaluate("document.querySelector('#cta').click()"); pg.wait_for_timeout(900); pg.screenshot(path='shots/s7f.png')
    pg.evaluate("document.querySelector('#hmodes button[data-m=e]').click()"); pg.wait_for_timeout(600); pg.screenshot(path='shots/s7g.png')
    pg.evaluate("document.querySelector('#ah-inno').scrollIntoView()"); pg.wait_for_timeout(600); pg.screenshot(path='shots/s7h.png')
    pg.evaluate("document.querySelector('#abar .fl button[data-go=kw]').click()"); pg.wait_for_timeout(5000); pg.screenshot(path='shots/s7i.png')
    ctx.close(); b.close()
ims=[Image.open(f'shots/s7{c}.png').resize((390,844)) for c in 'abcdefghi']
o=Image.new('RGB',(400*5-10,844*2+10),'white')
for i,x in enumerate(ims): o.paste(x,((i%5)*400,(i//5)*854))
o.save('shots/s7.png')
