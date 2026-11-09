const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:1600}});
await p.goto('file:///tmp/w/logo/award/logo.html');await p.waitForTimeout(800);
await p.locator('#sq').screenshot({path:'/mnt/user-data/outputs/GeoHeritage-logo-square.png'});
await p.locator('#hz').screenshot({path:'/mnt/user-data/outputs/GeoHeritage-logo-wide.png'});await b.close()})();
