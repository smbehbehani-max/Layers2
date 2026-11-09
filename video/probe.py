import sys; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start()
from playwright.sync_api import sync_playwright
O='/tmp/claude-0/-home-claude/c6b9363c-d753-5c3e-923c-9b3cb7539622/scratchpad/vid/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720})
    pg.goto('http://127.0.0.1:8765/stage.html'); pg.wait_for_function('window.READY===true',timeout=30000)
    t=0
    while t<41.7: t=round(t+0.1,3); pg.evaluate(f'seek({t})')
    print(pg.evaluate("[E('allLinks'), E('document.querySelectorAll(\".cline\").length'), E('view'), E('vb'), E('document.querySelector(\"#zl\").getAttribute(\"aria-pressed\")')]"))
    pg.screenshot(path=O+'probe.png')
    b.close()
