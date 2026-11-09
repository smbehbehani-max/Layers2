from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1400,'height':1000}); pg.goto('file:///tmp/w/layers/scene_test.html'); pg.wait_for_timeout(5500); pg.screenshot(path='/tmp/w/layers/scene_test.png'); b.close()
