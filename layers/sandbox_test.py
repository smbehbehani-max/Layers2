# simulate a sandboxed preview: load the single file inside <iframe sandbox="allow-scripts"> (opaque origin)
import sys; sys.path.insert(0,'/tmp/w/video'); from srv import start
start(root='/tmp/w/layers/one',port=8915)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); msgs=[]
    pg.on('console',lambda m: msgs.append(m.type+': '+m.text[:160]) if m.type=='error' else None)
    pg.set_content('<iframe id="f" sandbox="allow-scripts allow-same-origin" src="http://127.0.0.1:8915/index.html" style="width:390px;height:800px;border:0"></iframe>')
    pg.wait_for_timeout(2500); f=pg.frame_locator('#f'); fr=pg.frames[1]
    print('hub ok', fr.evaluate("!!document.querySelector('#explore')"))
    try:
        f.locator('.card[data-cc="bh"]').click(); pg.wait_for_timeout(2500)
        fr=[f for f in pg.frames if f.parent_frame and f.parent_frame!=pg.main_frame][0]; print('after click title:', fr.evaluate("document.querySelector('#t-title')?.textContent"))
    except Exception as e: print('ERR',str(e)[:300])
    print(msgs[:6])
    # opaque origin (no allow-same-origin)
    pg.set_content('<iframe id="f" sandbox="allow-scripts" src="http://127.0.0.1:8915/index.html" style="width:390px;height:800px;border:0"></iframe>')
    pg.wait_for_timeout(2500); f=pg.frame_locator('#f'); fr=pg.frames[1]; msgs.clear()
    try:
        f.locator('.card[data-cc="bh"]').click(); pg.wait_for_timeout(2500)
        fr=[f for f in pg.frames if f.parent_frame and f.parent_frame!=pg.main_frame][0]; print('opaque after click title:', fr.evaluate("document.querySelector('#t-title')?.textContent"))
    except Exception as e: print('ERR',str(e)[:300])
    print(msgs[:6]); b.close()
