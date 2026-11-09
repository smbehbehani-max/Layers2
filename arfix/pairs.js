const AR=/[؀-ۿ]/;const fs=require('fs');
const pairs=new Map(), lone=new Map();
function add(en,ar,ctx){ if(typeof ar!=='string'||!AR.test(ar))return; if(!pairs.has(ar))pairs.set(ar,{en:typeof en==='string'?en:'',ar,ctx}); }
function pair(en,ar,ctx){ if(typeof ar==='string'){add(en,ar,ctx);return}
 if(Array.isArray(ar)){ar.forEach((x,i)=>pair(Array.isArray(en)?en[i]:undefined,x,ctx));return}
 if(ar&&typeof ar==='object'){for(const k in ar)pair(en&&typeof en==='object'?en[k]:undefined,ar[k],ctx+'.'+k)} }
function walk(o,ctx,seen){ if(!o||typeof o!=='object'||seen.has(o))return; seen.add(o);
 if('en' in o&&'ar' in o){pair(o.en,o.ar,ctx);}
 for(const [a,b] of [['n','na'],['te','ta'],['se','sa'],['t','ta'],['title','titleAr'],['en','ar']]) if(typeof o[b]==='string') add(o[a],o[b],ctx+'.'+b);
 if(Array.isArray(o)) for(let i=1;i<o.length;i++){ if(typeof o[i]==='string'&&AR.test(o[i])&&typeof o[i-1]==='string'&&!AR.test(o[i-1])) add(o[i-1],o[i],ctx+'['+i+']') }
 for(const k in o){ if(k==='en'||k==='ar')continue; const v=o[k]; if(typeof v==='string'){ if(AR.test(v)&&!pairs.has(v)) lone.set(v,ctx+'.'+k)} else walk(v,ctx+'.'+k,seen)} }
for(const c of ['hub','kw','sa','om','ae','qa','bh']){const O=require('./c_'+c+'.js');for(const k in O)walk(O[k],c+':'+k,new Set())}
for(const k of pairs.keys())lone.delete(k);
fs.writeFileSync('pairs.json',JSON.stringify([...pairs.values()],null,0));
fs.writeFileSync('lone.json',JSON.stringify([...lone].map(([ar,ctx])=>({ar,ctx}))));
console.log('pairs',pairs.size,'lone',lone.size, [...pairs.values()].reduce((a,p)=>a+p.ar.length,0));
