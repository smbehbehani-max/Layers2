from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch()
    errs=[]
    def run(name,vw,vh,steps,dark=False,store=None):
        ctx=b.new_context(viewport={'width':vw,'height':vh},color_scheme='dark' if dark else 'light')
        pg=ctx.new_page();pg.on('pageerror',lambda e:errs.append(name+': '+str(e)))
        pg.goto('file:///mnt/user-data/outputs/kuwait-geoheritage-explorer.html')
        if store:
            pg.evaluate("s=>{for(const k in s)localStorage.setItem('kge-'+k,JSON.stringify(s[k]))}",store);pg.reload()
        pg.wait_for_timeout(700)
        for st in steps:
            if st[0]=='click': pg.locator(st[1]).first.click()
            pg.wait_for_timeout(450)
        pg.screenshot(path=name+'.png');ctx.close()
    run('d1',1280,800,[])
    run('d2',1280,800,[('click','[data-w=e]'),('click','#rail .ri >> nth=1')])
    run('m1',390,800,[],store={'welcomed':True,'mode':'e','lang':'ar'})
    run('m2',390,800,[('click','#go'),('click','[data-nav="1"]')],store={'welcomed':True,'mode':'e','lang':'ar'},dark=True)
    run('d3',1280,800,[('click','#rail .ri >> nth=0')],store={'welcomed':True,'mode':'r','lang':'ar'},dark=True)
    print('ERR',errs)
    b.close()
