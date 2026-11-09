import sys; sys.path.insert(0,'/tmp/w/video'); cc=sys.argv[1]
from srv import start; start(root=f'/tmp/w/gulf/{cc}/site',port=8900+hash(cc)%40)
from playwright.sync_api import sync_playwright
import os
port=8900+hash(cc)%40
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':800}); pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(700)
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(300); os.makedirs(f'/tmp/w/gulf/{cc}/shots',exist_ok=True); pg.screenshot(path=f'/tmp/w/gulf/{cc}/shots/desktop.png'); b.close()
