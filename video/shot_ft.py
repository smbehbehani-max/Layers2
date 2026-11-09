import sys; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start()
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1100,'height':420})
    pg.goto('http://127.0.0.1:8765/fonttest.html'); pg.wait_for_timeout(600)
    pg.screenshot(path='/tmp/claude-0/-home-claude/c6b9363c-d753-5c3e-923c-9b3cb7539622/scratchpad/ft.png'); b.close()
