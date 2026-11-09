import sys, os, time, json; sys.path.insert(0,'/tmp/w/video')
from srv import start; s=start(port=int(os.environ.get('PORT','8766')))
from playwright.sync_api import sync_playwright
FPS=30; DUR=float(os.environ.get('DUR','60')); START=float(os.environ.get('START','0'))
OUT=os.environ.get('OUT','/tmp/w/video/frames'); os.makedirs(OUT,exist_ok=True)
port=os.environ.get('PORT','8766')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1.5)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(f'http://127.0.0.1:{port}/stage.html'); pg.wait_for_function('window.READY===true',timeout=60000)
    n=int(round(DUR*FPS)); t0=time.time()
    for i in range(n):
        t=i/FPS
        pg.evaluate(f'seek({t:.5f})')
        if t>=START-1e-9: pg.screenshot(path=f'{OUT}/f{i:05d}.jpg',type='jpeg',quality=93)
        if i%60==0: print(f'frame {i}/{n} t={t:.1f}s elapsed {time.time()-t0:.0f}s',flush=True)
    json.dump(pg.evaluate('CLICKS'),open(os.environ.get('CLK','/tmp/w/video/clicks.json'),'w'))
    print('done',n,'frames in',round(time.time()-t0),'s; errors:',errs[:5],flush=True)
    b.close()
