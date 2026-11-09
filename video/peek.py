import sys; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start()
from playwright.sync_api import sync_playwright
O='/tmp/claude-0/-home-claude/c6b9363c-d753-5c3e-923c-9b3cb7539622/scratchpad/vid/'
import os; os.makedirs(O,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://127.0.0.1:8765/app.html'); pg.wait_for_timeout(700)
    pg.click('.opt[data-w=r]'); pg.wait_for_timeout(200)
    pg.click('#modes button[data-m=e]'); pg.wait_for_timeout(200)
    pg.evaluate("switchView('tl')"); pg.wait_for_timeout(300); pg.screenshot(path=O+'tl.png')
    pg.evaluate("switchView('map')"); pg.evaluate("show('bahra-1')"); pg.wait_for_timeout(400); pg.screenshot(path=O+'e-bahra.png')
    pg.evaluate("openShelf()"); pg.wait_for_timeout(300); pg.screenshot(path=O+'shelf.png')
    pg.evaluate("openStory('bahrah')"); pg.wait_for_timeout(300); pg.screenshot(path=O+'st0.png')
    pg.click('#story .pri'); pg.wait_for_timeout(300); pg.screenshot(path=O+'st1.png')
    pg.evaluate("closeStory();closeDet()"); pg.click('#zl'); pg.evaluate("show('spec-bahra-quake')"); pg.wait_for_timeout(400); pg.screenshot(path=O+'e-ai.png')
    print(errs, pg.evaluate("[home, vb, typeof LP, typeof px]"))
    b.close()
