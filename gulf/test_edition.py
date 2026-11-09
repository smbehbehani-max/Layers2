import sys, os, json
sys.path.insert(0, '/tmp/w/video')
from srv import start
cc = sys.argv[1]; PORT = 8840 + hash(cc) % 50
SH = f'/tmp/w/gulf/{cc}/site'
start(root=SH, port=PORT)
from playwright.sync_api import sync_playwright
OUT = f'/tmp/w/gulf/{cc}/shots'; os.makedirs(OUT, exist_ok=True)
R = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True,
                        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
                        geolocation={'latitude': 26.2, 'longitude': 50.55}, permissions=['geolocation'])
    pg = ctx.new_page(); errs = []; cons = []
    pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: cons.append(m.text) if m.type == 'error' else None)
    pg.goto(f'http://127.0.0.1:{PORT}/index.html', wait_until='load'); pg.wait_for_timeout(800)
    R['title'] = pg.title(); R['header'] = pg.evaluate("[document.querySelector('#t-title').textContent, document.querySelector('#t-sub').textContent]")
    R['active_logo'] = pg.evaluate("document.querySelector('.lg.on').dataset.lg + ' first=' + document.querySelector('#brandrow .lg').dataset.lg")
    R['rail'] = pg.evaluate("document.querySelectorAll('#rail .ri').length"); R['overflow'] = pg.evaluate('[document.documentElement.scrollWidth, innerWidth]')
    pg.screenshot(path=f'{OUT}/01-home.png')
    pg.evaluate("welcomed=true;store.set('welcomed',true);render()"); pg.wait_for_timeout(200)
    pg.screenshot(path=f'{OUT}/02-map.png')
    sid = pg.evaluate("D.sites[0].id"); pg.evaluate(f"show('{sid}')"); pg.wait_for_timeout(400)
    R['detail'] = pg.evaluate("document.querySelector('#det h2')?.textContent"); pg.screenshot(path=f'{OUT}/03-detail.png')
    pg.evaluate("(()=>{const d=document.querySelector('#det'),el=d.querySelector('ul.refs');if(el)d.scrollTop=el.offsetTop-100})()"); pg.wait_for_timeout(200)
    pg.screenshot(path=f'{OUT}/04-refs.png'); pg.evaluate('closeDet()')
    pg.evaluate("document.querySelector('#v-tl').click()"); pg.wait_for_timeout(400); pg.screenshot(path=f'{OUT}/05-timeline.png')
    R['tl_bars'] = pg.evaluate("document.querySelectorAll('#tl .bar, #tl .tb, #tl rect').length")
    pg.evaluate("document.querySelector('#v-map').click()")
    # explorer
    pg.evaluate("mode='e';store.set('mode','e');chrome();render()"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/06-explorer.png')
    pg.evaluate("chapter(0)"); pg.wait_for_timeout(500); R['chapter0'] = pg.evaluate("document.querySelector('#det h2')?.textContent"); pg.screenshot(path=f'{OUT}/07-expedition.png')
    pg.evaluate('closeDet()')
    R['stories_btn'] = pg.evaluate("(()=>{const b=document.querySelector('#stb');return b?[!b.hidden, getComputedStyle(b).display]:null})()")
    pg.evaluate("document.querySelector('#stb')&&document.querySelector('#stb').click()"); pg.wait_for_timeout(400); R['shelf'] = pg.evaluate("(()=>{const s=document.querySelector('#story');return s?[!s.hidden, s.innerText.slice(0,120)]:null})()"); pg.screenshot(path=f'{OUT}/08-shelf.png')
    pg.evaluate("typeof closeStory=='function'&&closeStory()")
    # arabic
    pg.evaluate("mode='r';store.set('mode','r');chrome();render()"); pg.click('#lang'); pg.wait_for_timeout(500); pg.screenshot(path=f'{OUT}/09-arabic.png')
    R['ar_header'] = pg.evaluate("[document.querySelector('#t-title').textContent, document.querySelector('#t-sub').textContent]")
    pg.evaluate(f"show('{sid}')"); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/10-arabic-detail.png'); pg.evaluate('closeDet()'); pg.click('#lang')
    # live
    pg.click('#live'); pg.wait_for_timeout(1500); R['live'] = pg.evaluate("document.querySelector('#livep')?.innerText"); pg.screenshot(path=f'{OUT}/11-live.png'); pg.evaluate('stopLive()')
    # coming soon kuwait link + how + about
    pg.evaluate("openSoon('kw')"); pg.wait_for_timeout(600); R['soon_kw'] = pg.evaluate("document.querySelector('#soon')?.innerText.slice(0,200)"); pg.screenshot(path=f'{OUT}/12-kuwait-link.png'); pg.evaluate('closeSoon()')
    pg.evaluate("openSoon(cc=='qa'?'om':'qa')".replace('cc',repr(cc))); pg.wait_for_timeout(600); pg.screenshot(path=f'{OUT}/13-soon-qa.png'); pg.evaluate('closeSoon()')
    pg.evaluate('openHow()'); pg.wait_for_timeout(500); R['how'] = pg.evaluate("document.querySelector('#how h2, #how h1')?.textContent"); pg.screenshot(path=f'{OUT}/14-how.png'); pg.evaluate('closeHow()')
    pg.evaluate('openAbout()'); pg.wait_for_timeout(300); R['about'] = pg.evaluate("document.querySelector('#sheet')?.innerText.slice(0,160)"); pg.evaluate('closeSheet()')
    # protected layer
    R['pz'] = pg.evaluate("typeof PZ!='undefined' && PZ.length")
    pg.evaluate("location.hash='#p='+D.sites[5].id"); pg.wait_for_timeout(400); R['deeplink'] = pg.evaluate("document.querySelector('#det h2')?.textContent")
    R['errors'] = errs; R['console'] = cons[:5]
    ctx.close(); b.close()
print(json.dumps(R, ensure_ascii=False, indent=1))
