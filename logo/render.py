import sys; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start('/tmp/w/logo',8790)
from playwright.sync_api import sync_playwright
O='/mnt/user-data/outputs/'
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1600,'height':1200});pg.goto('http://127.0.0.1:8790/sheet.html');pg.wait_for_timeout(800)
    pg.locator('#lock').screenshot(path=O+'layers-kuwait-logo-lockup.png');pg.locator('#fam').screenshot(path='/tmp/w/logo/family.png')
    for sz in (1024,512,180,64):
        q=b.new_page(viewport={'width':sz,'height':sz});q.goto('http://127.0.0.1:8790/sheet.html');q.set_content(f'<style>body{{margin:0}}</style><img src="http://127.0.0.1:8790/icon-kw.svg" width="{sz}" height="{sz}">');q.wait_for_timeout(300)
        q.screenshot(path=(O if sz in(1024,512) else '/tmp/w/logo/')+f'layers-kuwait-icon-{sz}.png',omit_background=True)
    b.close()
