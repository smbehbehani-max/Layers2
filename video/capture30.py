import sys, os, time, json; sys.path.insert(0,'/tmp/w/video')
from srv import start
port=int(os.environ['PORT']); s=start(port=port)
from playwright.sync_api import sync_playwright
FPS=30; V0=float(os.environ['V0']); V1=float(os.environ['V1'])
OUT='/tmp/w/video/frames30'; os.makedirs(OUT,exist_ok=True)
SEG=[(0,5,0),(5,10,7.8),(10,12.5,12.8),(12.5,16.25,28.3),(16.25,20,41.3),(20,22.5,48.3),(22.5,30,52.4)]
def warp(v):
    for a,b,s0 in SEG:
        if a<=v<b: return s0+(v-a)
    return SEG[-1][2]+(v-SEG[-1][0])
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1.5)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(f'http://127.0.0.1:{port}/stage30.html'); pg.wait_for_function('window.READY===true',timeout=60000)
    n=int(round(30*FPS)); t0=time.time()
    for i in range(n):
        v=i/FPS
        if v>=V1-1e-9: break
        pg.evaluate(f'seek({warp(v):.5f})')
        if v>=V0-1e-9: pg.screenshot(path=f'{OUT}/f{i:05d}.jpg',type='jpeg',quality=93)
        if i%60==0: print(f'frame {i} v={v:.1f} elapsed {time.time()-t0:.0f}s',flush=True)
    if V1>=30: json.dump(pg.evaluate('CLICKS'),open('/tmp/w/video/clicks30_src.json','w'))
    print('done errors:',errs[:5],flush=True)
    b.close()
