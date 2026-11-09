/* ---------- research updates (db) ---------- */
const UT={en:{btn:'What’s new',title:'What’s new',sub:'New research about these places, checked before it appears here.',none:'No new research yet. New findings appear here after review.',
  pend:'Waiting for your review',pendP:'Only you can see these. Approve to show them to everyone, or reject to hide them.',approve:'Approve',reject:'Reject',
  newPlace:'New place',update:'New research',source:'Source',found:'Found',onMap:'Show on the map',siteLink:'Open the place',offline:'Updates load for signed-in viewers.',
  cardH:'New research'},
 ar:{btn:'الجديد',title:'الجديد',sub:'أبحاث جديدة عن هذه المواقع، تُراجع قبل أن تظهر هنا.',none:'لا توجد أبحاث جديدة بعد. تظهر الاكتشافات الجديدة هنا بعد المراجعة.',
  pend:'بانتظار مراجعتك',pendP:'أنت وحدك ترى هذه. وافق لعرضها للجميع، أو ارفض لإخفائها.',approve:'موافقة',reject:'رفض',
  newPlace:'موقع جديد',update:'بحث جديد',source:'المصدر',found:'تاريخ الرصد',onMap:'اعرضه على الخريطة',siteLink:'افتح الموقع',offline:'تظهر التحديثات للمستخدمين المسجّلين.',
  cardH:'بحث جديد'}};
let DB=null,USR=null,isAdmin=false,UPD=[],PEND=[];
const uT=()=>UT[lang];
const uTitle=u=>(lang=='ar'&&u.title_ar)||u.title_en||u.title_ar||'';
const uSum=u=>(lang=='ar'&&u.summary_ar)||u.summary_en||u.summary_ar||'';
function updBtn(){const b=$('#upd');if(!b)return;const n=UPD.length,p=PEND.length;b.hidden=!(DB&&(n||isAdmin));
 b.innerHTML=`${E(uT().btn)}${p?`<span class="ubadge">${p}</span>`:''}`}
function updCard(u,pending){const t=uT(),s=u.site&&D.sites.find(x=>x.id==u.site);
 return`<article class="ucard${pending?' pend':''}"><div class="uk">${E(u.kind=='new'?t.newPlace:t.update)}${s?` · ${E(ttl(s))}`:''}${u.year?` · ${E(u.year)}`:''}</div><h4>${E(uTitle(u))}</h4><p>${E(uSum(u))}</p>
 ${u.source_title?`<p class="usrc"><b>${E(t.source)}:</b> ${u.source_url?`<a href="${E(u.source_url)}" target="_blank" rel="noopener">${E(u.source_title)}</a>`:E(u.source_title)}</p>`:''}
 <div class="uact">${s?`<button data-uopen="${E(s.id)}">${E(t.siteLink)}</button>`:''}${u.lat!=null&&u.lng!=null&&!s?`<button data-umap="${E(u._id)}">${E(t.onMap)}</button>`:''}
 ${pending?`<button class="ok" data-uok="${E(u._id)}">${E(t.approve)}</button><button class="no" data-uno="${E(u._id)}">${E(t.reject)}</button>`:''}</div></article>`}
function openUpdates(){const t=uT();sel=null;chap=-1;
 let h=`<div class="dh" style="--c:var(--gold)"><button class="x" aria-label="${E(L().close)}">×</button><div class="big">${glyph('map')}</div><div class="kick">${E(t.sub)}</div><h2>${E(t.title)}</h2></div><div class="db">`;
 if(isAdmin&&PEND.length)h+=`<h3>${E(t.pend)} (${PEND.length})</h3><p class="note">${E(t.pendP)}</p>${PEND.map(u=>updCard(u,1)).join('')}<h3>${E(t.title)}</h3>`;
 h+=UPD.length?UPD.map(u=>updCard(u,0)).join(''):`<p class="note">${E(t.none)}</p>`;
 $('#det').innerHTML=h+'</div>';openDet();render()}
function siteUpdates(id){return UPD.filter(u=>u.site==id)}
function updSiteBlock(id){const us=siteUpdates(id);if(!us.length)return'';const t=uT();
 return`<div class="usite"><h3>${E(t.cardH)}</h3>${us.map(u=>`<div><b>${E(uTitle(u))}</b><p>${E(uSum(u))}</p>${u.source_url?`<a href="${E(u.source_url)}" target="_blank" rel="noopener">${E(u.source_title||t.source)}</a>`:''}</div>`).join('')}</div>`}
async function decide(id,ok){const u=PEND.find(x=>x._id==id);if(!u||!DB)return;const body={...u};delete body._id;
 try{if(ok){body.status='approved';body.approved_at=new Date().toISOString();await DB.collection('approved').doc(id).set(body)}
  else{await DB.collection('rejected').doc(id).set({title_en:body.title_en||'',source_url:body.source_url||'',source_title:body.source_title||'',rejected_at:new Date().toISOString()})}
  await DB.collection('pending').doc(id).delete()}catch(e){alertBox(e&&e.code)}}
function alertBox(code){const n=document.createElement('div');n.className='toast';n.textContent=lang=='ar'?'تعذّر الحفظ. حاول مرة أخرى.':'Could not save. Try again.';document.body.appendChild(n);setTimeout(()=>n.remove(),3500)}
function updPoints(u){if(!DB)return'';return UPD.filter(x=>x.kind=='new'&&!x.site&&x.lat!=null&&x.lng!=null).map(x=>`<path class="upt" data-uid="${E(x._id)}" transform="translate(${px(x.lng)} ${py(x.lat)}) scale(${u})" d="M0,-9 L2.6,-3 L9,-2.8 L4,1.4 L5.6,8 L0,4.4 L-5.6,8 L-4,1.4 L-9,-2.8 L-2.6,-3Z"/>`).join('')}
(async()=>{try{const [db,us]=await Promise.all([claude.use('db'),claude.use('user')]);USR=us;if(!db)return;DB=db;isAdmin=us?await us.canEdit():false;
 const map=snap=>snap.docs.map(d=>({...d.data(),_id:d.id}));
 DB.collection('approved').orderBy('found','desc').limit(300).onSnapshot(s=>{UPD=map(s);updBtn();if($('#det').dataset.v=='upd')openUpdates();render()},()=>{});
 if(isAdmin)DB.collection('pending').orderBy('found','desc').limit(200).onSnapshot(s=>{PEND=map(s);updBtn();if($('#det').dataset.v=='upd')openUpdates()},()=>{});
 updBtn()}catch(e){}})();
$('#upd').onclick=()=>{openUpdates();$('#det').dataset.v='upd'};
