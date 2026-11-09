const CACHE='layers-web-202611092140';
const CORE=['./','index.html','mobile.html','privacy.html','manifest.webmanifest','icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png'];
const LATER=['kw','sa','bh','qa','ae','om'].map(c=>'ed-'+c+'.html');
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>Promise.allSettled(CORE.map(p=>c.add(p)))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{caches.open(CACHE).then(c=>Promise.allSettled(LATER.map(p=>c.match(p).then(m=>m||c.add(p)))));e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 e.respondWith(fetch(r).then(res=>{if(res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp))}return res}).catch(()=>caches.match(r,{ignoreSearch:true}).then(m=>m||caches.match('./'))))});
