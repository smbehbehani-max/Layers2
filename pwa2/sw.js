const C='layers-v5';
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
