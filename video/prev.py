import sys, json; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start()
from playwright.sync_api import sync_playwright
O='/tmp/claude-0/-home-claude/c6b9363c-d753-5c3e-923c-9b3cb7539622/scratchpad/vid/'
times=[float(x) for x in sys.argv[1].split(',')]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720})
    logs=[];pg.on('console',lambda m:logs.append(m.type+': '+m.text) if m.type in('error','warning') else None);pg.on('pageerror',lambda e:logs.append('PAGEERR '+str(e)))
    pg.goto('http://127.0.0.1:8765/stage.html'); pg.wait_for_function('window.READY===true',timeout=30000)
    t=0.0; i=0
    for tt in times:
        while t<tt-1e-9:
            t=min(tt,round(t+0.1,4)); pg.evaluate(f'seek({t})')
        pg.screenshot(path=O+f'p{tt:05.1f}.png')
    print('clicks',pg.evaluate('CLICKS'))
    print('\n'.join(logs[:20]))
    b.close()
