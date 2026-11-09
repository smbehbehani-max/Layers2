# Builds the standalone website / PWA folder from the app build: /tmp/w/out3.html -> /tmp/w/pwa2/
import os, shutil, json
SRC = '/tmp/w/out3.html'
OUT = '/tmp/w/pwa2'
BASE = 'https://smbehbehani-max.github.io/Layers2/'
VERSION = '1.1.0'
os.makedirs(OUT, exist_ok=True)
h = open(SRC, encoding='utf-8').read()
assert h.count("const STANDALONE=false,") == 1
h = h.replace("const STANDALONE=false,", "const STANDALONE=true,")
assert h.startswith('<meta charset="utf-8">')
DESC_EN = "Kuwait's geology, archaeology and ecology on one bilingual map: 80 places with sources, illustrated stories, a 100-million-year timeline and live directions."
head = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC_EN}">
<meta name="theme-color" content="#f7f8f5" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#121c1c" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Layers"><meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="application-name" content="Layers of Kuwait">
<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="canonical" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Layers of Kuwait"><meta property="og:title" content="Layers of Kuwait · طبقات الكويت">
<meta property="og:description" content="{DESC_EN}"><meta property="og:url" content="{BASE}"><meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US"><meta property="og:locale:alternate" content="ar_KW">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Layers of Kuwait · طبقات الكويت"><meta name="twitter:description" content="{DESC_EN}"><meta name="twitter:image" content="{BASE}og.png">
'''
h = head + h[len('<meta charset="utf-8">'):]
# body/head split: the app build has no <body>; browsers handle it, but give the service worker registration a proper home at the end
h = h.rstrip() + '''
<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').then(r=>{r.addEventListener('updatefound',()=>{const w=r.installing;if(!w)return;w.addEventListener('statechange',()=>{if(w.state=='installed'&&navigator.serviceWorker.controller&&typeof updToast=='function')updToast()})})}).catch(()=>{}));</script>
</html>
'''
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(h)

manifest = {
  "id": "/Layers2/",
  "name": "Layers of Kuwait",
  "short_name": "Layers",
  "description": DESC_EN,
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "display_override": ["standalone", "minimal-ui"],
  "orientation": "any",
  "background_color": "#f7f8f5",
  "theme_color": "#f7f8f5",
  "lang": "en",
  "dir": "auto",
  "categories": ["education", "travel", "navigation"],
  "prefer_related_applications": False,
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
    {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
  ],
  "screenshots": [
    {"src": "shot-en-1.jpg", "sizes": "1080x1920", "type": "image/jpeg", "form_factor": "narrow", "label": "80 places on one map"},
    {"src": "shot-en-2.jpg", "sizes": "1080x1920", "type": "image/jpeg", "form_factor": "narrow", "label": "Every place with its sources"},
    {"src": "shot-en-3.jpg", "sizes": "1080x1920", "type": "image/jpeg", "form_factor": "narrow", "label": "Illustrated stories"},
    {"src": "shot-ar-1.jpg", "sizes": "1080x1920", "type": "image/jpeg", "form_factor": "narrow", "label": "بالعربية والإنجليزية"}
  ],
  "shortcuts": [
    {"name": "Go live", "short_name": "Go live", "description": "Directions to the nearest place", "url": "./#live", "icons": [{"src": "icon-192.png", "sizes": "192x192"}]},
    {"name": "Stories", "short_name": "Stories", "description": "Illustrated stories", "url": "./#stories", "icons": [{"src": "icon-192.png", "sizes": "192x192"}]},
    {"name": "Timeline", "short_name": "Timeline", "description": "100 million years", "url": "./#timeline", "icons": [{"src": "icon-192.png", "sizes": "192x192"}]}
  ]
}
json.dump(manifest, open(f'{OUT}/manifest.webmanifest', 'w'), indent=1, ensure_ascii=False)

sw = r'''const C='layers-v5';
const CORE=['./','index.html','manifest.webmanifest','privacy.html','icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;
 const same=new URL(r.url).origin===location.origin;
 if(r.mode==='navigate'||(same&&/index\.html$/.test(r.url))){
  // the app itself: network first so a new version shows on the next open, cache if offline
  e.respondWith(fetch(r).then(x=>{const cp=x.clone();caches.open(C).then(c=>{c.put(r,cp);c.put('index.html',x.clone())});return x}).catch(()=>caches.match(r).then(m=>m||caches.match('index.html'))));return}
 // everything else (icons, privacy page, fonts): cache first, refresh in the background
 e.respondWith(caches.match(r).then(m=>{const f=fetch(r).then(x=>{if(x&&(x.ok||x.type==='opaque'))caches.open(C).then(c=>c.put(r,x.clone()));return x}).catch(()=>m);return m||f}))});
'''
open(f'{OUT}/sw.js', 'w').write(sw)

privacy = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Privacy policy · Layers of Kuwait</title>
<meta name="description" content="Privacy policy for the Layers of Kuwait app and website.">
<link rel="icon" href="icon-192.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>
:root{{--panel:#f7f8f5;--ink:#1a2a2b;--mut:#5d6d6c;--line:#d5dcd6;--sea:#2c6e72;--gold:#c99a2e}}
@media (prefers-color-scheme:dark){{:root{{--panel:#121c1c;--ink:#e6ecea;--mut:#93a5a2;--line:#273534;--sea:#7cc6c9;color-scheme:dark}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--panel);color:var(--ink);font:16px/1.6 "Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;padding:max(16px,env(safe-area-inset-top)) max(16px,env(safe-area-inset-right)) max(32px,env(safe-area-inset-bottom)) max(16px,env(safe-area-inset-left))}}
main{{max-width:720px;margin:0 auto}}h1{{font:700 30px/1.2 Georgia,"Times New Roman",serif;margin:12px 0 4px}}h2{{font-size:20px;margin:26px 0 6px}}p,li{{margin:0 0 10px}}
.meta{{color:var(--mut);font-size:14px}}a{{color:var(--sea)}}
.lang{{display:flex;gap:8px;margin:14px 0 20px}}.lang button{{border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:99px;padding:6px 14px;font:600 14px inherit;cursor:pointer}}.lang button[aria-pressed=true]{{background:var(--ink);color:var(--panel);border-color:var(--ink)}}
[lang=ar]{{direction:rtl;font-family:"IBM Plex Sans Arabic","Noto Sans Arabic",system-ui,sans-serif}}[lang=ar] h1{{font-family:"Amiri","Noto Naskh Arabic",serif}}
.back{{display:inline-block;margin-top:24px;color:var(--sea);font-weight:600}}
</style></head>
<body><main>
<div class="lang"><button id="b-en" aria-pressed="true">English</button><button id="b-ar" aria-pressed="false" lang="ar">عربي</button></div>
<section id="en">
<h1>Privacy policy</h1>
<p class="meta">Layers of Kuwait · website and apps · effective 23 October 2026</p>
<p>Layers of Kuwait is a map of Kuwait's geology, archaeology and ecology. It is designed so that it keeps no information about you.</p>
<h2>What the app collects</h2>
<p>Nothing. The app has no accounts, no sign-in, no analytics, no advertising and no tracking. It does not send any information about you to us or to anyone else.</p>
<h2>Location</h2>
<p>When you turn on <b>Go live</b>, the app asks your phone for your location so it can show your position on the map and the distance and direction to the nearest place. This happens entirely on your device. Your location is never stored and never transmitted. Turn Go live off, or decline the permission, and the app works normally without it.</p>
<h2>Read aloud</h2>
<p>The <b>Listen</b> button uses the speech voices built into your phone or browser. The text is spoken on your device; nothing is sent to us.</p>
<h2>Settings saved on your device</h2>
<p>The app remembers your language, your chosen mode (Explorer or Researcher) and the places you have opened in Explorer mode. These are stored only in your browser or phone storage and can be cleared at any time by clearing the site data or deleting the app.</p>
<h2>Third parties</h2>
<p>The website is hosted on GitHub Pages, and typefaces are loaded from Google Fonts. Like any web server, these services may record standard technical details of a request, such as an IP address, under their own privacy policies: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub</a> and <a href="https://developers.google.com/fonts/faq/privacy" rel="noopener">Google Fonts</a>. We do not receive this information. Links to research papers and other websites open in your browser and are governed by those sites' policies.</p>
<h2>Children</h2>
<p>The app is suitable for all ages and collects no personal information from anyone.</p>
<h2>Changes</h2>
<p>If this policy changes, the new version will be published at this address with a new effective date.</p>
<h2>Contact</h2>
<p>Questions about this policy can be sent through the project page: <a href="https://github.com/smbehbehani-max/Layers2" rel="noopener">github.com/smbehbehani-max/Layers2</a>.</p>
<a class="back" href="./">← Back to the app</a>
</section>
<section id="ar" lang="ar" hidden>
<h1>سياسة الخصوصية</h1>
<p class="meta">طبقات الكويت · الموقع الإلكتروني والتطبيقات · سارية من 23 أكتوبر 2026</p>
<p>طبقات الكويت خريطة لجيولوجيا الكويت وآثارها وبيئتها، صُمّمت بحيث لا تحتفظ بأي معلومات عنك.</p>
<h2>ما يجمعه التطبيق</h2>
<p>لا شيء. لا حسابات في التطبيق ولا تسجيل دخول ولا تحليلات ولا إعلانات ولا تتبّع. ولا يرسل أي معلومات عنك إلينا أو إلى أي جهة أخرى.</p>
<h2>الموقع الجغرافي</h2>
<p>عند تشغيل <b>مباشر</b> يطلب التطبيق من هاتفك موقعك ليعرض مكانك على الخريطة والمسافة والاتجاه إلى أقرب موقع. يجري ذلك كله على جهازك. لا يُخزَّن موقعك ولا يُرسل أبدًا. أوقف «مباشر» أو ارفض الإذن، وسيعمل التطبيق كالمعتاد من دونه.</p>
<h2>القراءة بصوت عالٍ</h2>
<p>يستخدم زر <b>استمع</b> أصوات النطق المدمجة في هاتفك أو متصفحك. يُنطق النص على جهازك، ولا يُرسل شيء إلينا.</p>
<h2>الإعدادات المحفوظة على جهازك</h2>
<p>يتذكر التطبيق لغتك والوضع الذي اخترته (مستكشف أو باحث) والمواقع التي فتحتها في وضع المستكشف. تُخزَّن هذه فقط في متصفحك أو ذاكرة هاتفك، ويمكن مسحها في أي وقت بمسح بيانات الموقع أو حذف التطبيق.</p>
<h2>الأطراف الأخرى</h2>
<p>يُستضاف الموقع على GitHub Pages، وتُحمَّل الخطوط من Google Fonts. وكأي خادم ويب، قد تسجّل هاتان الخدمتان تفاصيل تقنية معتادة للطلب مثل عنوان IP وفق سياسة الخصوصية الخاصة بكل منهما: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub</a> و<a href="https://developers.google.com/fonts/faq/privacy" rel="noopener">Google Fonts</a>. ولا نتلقى نحن هذه المعلومات. وتُفتح روابط الأوراق العلمية والمواقع الأخرى في متصفحك وتخضع لسياسات تلك المواقع.</p>
<h2>الأطفال</h2>
<p>التطبيق مناسب لجميع الأعمار ولا يجمع أي معلومات شخصية من أحد.</p>
<h2>التغييرات</h2>
<p>إذا تغيّرت هذه السياسة، تُنشر النسخة الجديدة على هذا العنوان بتاريخ سريان جديد.</p>
<h2>التواصل</h2>
<p>يمكن إرسال الأسئلة حول هذه السياسة عبر صفحة المشروع: <a href="https://github.com/smbehbehani-max/Layers2" rel="noopener">github.com/smbehbehani-max/Layers2</a>.</p>
<a class="back" href="./">→ العودة إلى التطبيق</a>
</section>
</main>
<script>
const pick=l=>{{document.getElementById('en').hidden=l!='en';document.getElementById('ar').hidden=l!='ar';document.getElementById('b-en').setAttribute('aria-pressed',l=='en');document.getElementById('b-ar').setAttribute('aria-pressed',l=='ar');document.documentElement.lang=l;document.title=(l=='ar'?'سياسة الخصوصية':'Privacy policy')+' · Layers of Kuwait'}};
document.getElementById('b-en').onclick=()=>pick('en');document.getElementById('b-ar').onclick=()=>pick('ar');
try{{if(location.hash=='#ar'||JSON.parse(localStorage.getItem('kge-lang'))=='ar')pick('ar')}}catch(e){{}}
</script>
</body></html>
'''
open(f'{OUT}/privacy.html', 'w', encoding='utf-8').write(privacy)

for f in ['apple-touch-icon.png', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', '.nojekyll']:
    shutil.copy(f'/tmp/w/pwa/{f}', f'{OUT}/{f}')
readme = f'''# Layers of Kuwait · طبقات الكويت

Bilingual map of Kuwait's geology, archaeology and ecology: 80 places with sources, illustrated stories, a 100-million-year timeline, AI connections marked as untested ideas, read-aloud and live directions.

Live site: {BASE}

Version {VERSION}. Files in this folder are the complete website and installable app (PWA):
index.html (the app) · manifest.webmanifest · sw.js (offline cache) · privacy.html · og.png (link preview) · icons · shot-*.jpg (install screenshots)
'''
open(f'{OUT}/README.md', 'w').write(readme)
print('built', OUT, len(h))
