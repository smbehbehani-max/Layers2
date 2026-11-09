const CACHE='layers-one-v2.0.0';
const PAGES0=["./", "index.html", "kw.html", "bh.html", "qa.html", "ae.html", "om.html", "sa.html", "privacy.html", "manifest.webmanifest"];
const PAGES=['./','index.html','privacy.html','manifest.webmanifest'];const ASSETS=['icon-192.png','icon-512.png','icon-maskable-512.png','apple-touch-icon.png'].concat(["og-kw.png", "og-bh.png", "og-qa.png", "og-ae.png", "og-om.png", "og-sa.png"]);
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS).then(()=>Promise.allSettled(PAGES.map(p=>c.add(p))))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
 const u=new URL(r.url);const page=r.mode==='navigate'||u.pathname.endsWith('/')||u.pathname.endsWith('.html');
 if(page){e.respondWith(fetch(r).then(res=>{const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp));return res}).catch(()=>caches.match(r).then(m=>m||caches.match(u.pathname.endsWith('/')?u.pathname+'index.html':u.pathname.replace(/index\.html$/,'')))))}
 else{e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp));return res})))}});
