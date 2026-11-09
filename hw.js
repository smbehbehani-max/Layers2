
const KW="M47.2 0.0L35.5 3.3L28.4 7.4L25.2 16.1L21.6 23.3L18.1 31.8L14.7 39.1L8.7 47.7L0.0 59.6L8.6 65.5L50.7 76.8L53.7 90.2L99.9 100.0L98.2 96.9L97.5 94.8L97.8 93.9L97.2 90.5L97.4 90.0L97.5 90.0L98.1 86.6L93.4 85.3L91.7 79.2L91.7 79.1L92.0 78.9L89.6 77.2L88.9 76.7L87.4 74.2L86.4 72.8L85.7 71.5L84.9 69.2L85.2 68.0L85.3 67.6L84.8 67.9L85.3 67.4L84.4 66.4L85.1 66.1L84.4 66.1L84.1 65.1L83.9 65.2L83.9 64.8L83.9 63.6L83.7 62.6L83.5 62.0L83.4 60.7L83.0 60.2L83.3 59.8L83.1 59.7L83.3 59.6L83.2 59.3L82.1 56.4L81.8 56.1L81.6 55.1L81.5 54.8L81.4 54.5L81.3 53.2L81.0 51.6L81.0 50.9L81.2 49.6L81.5 48.6L81.7 47.9L79.9 48.4L79.7 48.5L78.9 48.5L78.1 48.0L77.7 47.2L76.9 46.7L76.4 46.3L76.4 46.0L75.4 45.5L74.8 45.7L74.7 45.8L73.9 46.8L72.8 47.8L71.9 48.3L71.6 48.1L71.8 47.7L72.3 47.5L70.8 47.5L70.8 48.8L69.5 49.5L67.2 49.8L66.4 48.1L66.1 47.1L67.3 45.7L67.1 45.3L66.8 45.3L67.1 45.7L65.0 46.6L64.8 46.1L64.6 46.2L63.5 46.8L62.6 46.4L61.9 46.8L60.3 47.5L59.7 47.0L60.3 45.7L61.0 44.6L62.2 45.0L63.2 43.2L65.0 40.7L70.6 36.4L73.1 34.8L74.6 33.8L83.9 35.9L85.7 35.1L85.8 36.0L83.9 36.0L85.4 37.6L86.5 35.5L86.6 33.9L86.2 33.6L84.7 32.1L83.9 30.0L82.2 26.3L81.1 23.1L80.1 22.4L78.8 21.0L76.8 15.9L76.5 12.7L76.6 12.8L76.9 12.5L76.3 9.9L74.6 7.0L75.3 8.4L75.1 8.3L73.9 7.4L73.7 6.6ZM84.5 7.7L83.3 9.6L83.5 10.1L84.0 10.2L84.3 11.0L84.5 12.3L85.1 12.5L85.5 10.5L87.5 11.0L87.4 12.4L86.7 13.4L86.8 14.2L86.6 15.3L86.3 15.8L86.2 16.1L85.9 17.6L85.3 17.7L84.2 17.1L83.0 17.0L82.6 17.1L82.0 17.7L83.9 17.7L81.9 17.8L81.6 18.1L81.6 19.0L81.9 19.7L82.5 19.2L82.5 19.8L79.8 21.0L82.0 22.5L82.7 24.5L84.0 26.6L85.0 29.2L87.5 33.1L95.5 26.4L95.7 18.8L96.5 20.2L93.4 16.4L94.5 15.2L89.6 11.2Z";
const X=i=>92+i*136,Y=190;
const S=[
 {t:'Sources',s:'papers · news · PDFs · emails',who:'auto',ttl:'Research arrives from many places',
  txt:'Journals, news sites, field reports and the original PDF catalogue all describe these places. Researchers can also send their own stories by email from the Stories shelf.',
  ex:'<b>Example source:</b> Archeowieści, 2 Dec 2024: Kuwaiti-Polish team discovers figurine, local pottery, and environmental clues.'},
 {t:'Weekly check',s:'Sundays, 8:56 am',who:'auto',ttl:'Every Sunday, a search runs on its own',
  txt:'A scheduled task searches for anything new about the 74 places. It reads what is already queued, approved or rejected first, so it never suggests the same finding twice.',
  ex:'<b>Searches like:</b> “Bahra 1 excavation”, “Failaka temple”, “Kuwait mud volcanoes”, “Al-Ahmadi quarry Dammam Formation”.'},
 {t:'Read & extract',s:'place · date · coordinates',who:'auto',ttl:'Each source is opened and read',
  txt:'Facts are taken only from pages actually opened: the place, the dates, the team, the link, and coordinates when the source states them. The finding is matched to a place already on the map, or marked as a new place.',
  ex:'<b>Extracted:</b> Place → Bahra 1 · Published → Dec 2024 · Find → Ubaid-style clay head · Team → Kuwaiti-Polish mission.'},
 {t:'Write EN + AR',s:'summary · title · source',who:'auto',ttl:'A short summary in English and Arabic',
  txt:'It writes a plain two-to-three sentence summary and title in both languages, uses “Arabian Gulf”, and keeps the source link so anyone can check it.',
  ex:'<b>Title:</b> A unique clay head and the Gulf’s oldest pottery workshop at Bahra 1<br><b>العنوان:</b> رأس طيني فريد وأقدم ورشة فخار في الخليج في بحرة 1'},
 {t:'You review',s:'approve · reject',who:'you',ttl:'Nothing goes live without you',
  txt:'Drafts wait in a private queue under What’s new. You read each one with its source and press Approve or Reject. Viewers never see the queue.',
  ex:'<b>In the app:</b> What’s new <span style="background:var(--gold);color:#1a1205;border-radius:9px;padding:0 6px;font-weight:700">3</span> → Waiting for your review (3) → Approve.'},
 {t:'Live in the app',s:'What’s new · place card · map',who:'all',ttl:'Approved findings appear at once',
  txt:'Signed-in viewers see the finding immediately in What’s new and as “New research” on the place’s card. A new place with coordinates appears as a gold star on the map.',
  ex:'<b>Shown on:</b> Bahra 1 card → New research → link to the original source.'},
 {t:'Grows into a story',s:'title · story · cartoon',who:'you',ttl:'A new place can become a full entry',
  txt:'When you ask, Claude turns a new place into a complete entry: researcher record, Explorer title and story in both languages, a cartoon, an icon and a bar on the timeline. That is how the Al-Ahmadi quarry was added.',
  ex:'<b>Example:</b> Al-Ahmadi quarry → “The Window into Deep Time” · Eocene Dammam Formation · 48–34 million years ago.'}
];
const ns='http://www.w3.org/2000/svg';
function icon(i){const c='var(--ink)',g='var(--gold)',sea='var(--sea)',sand='var(--sand)';
 switch(i){
 case 0:return`<g class="ic"><rect x="-20" y="-22" width="30" height="38" rx="3" fill="${sand}" stroke="${c}" stroke-width="1.6" transform="rotate(-8)"/><rect x="-12" y="-24" width="30" height="38" rx="3" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><path d="M-6 -14h18M-6 -8h18M-6 -2h12" stroke="${c}" stroke-width="1.4"/><rect x="2" y="6" width="22" height="15" rx="2" fill="var(--panel)" stroke="${g}" stroke-width="1.8"/><path d="M2 7l11 8 11-8" fill="none" stroke="${g}" stroke-width="1.6"/></g>`;
 case 1:return`<g class="ic"><rect x="-22" y="-20" width="36" height="34" rx="4" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><rect x="-22" y="-20" width="36" height="9" rx="3" fill="${sea}"/><text x="-4" y="7" text-anchor="middle" style="font:700 11px var(--f-body);fill:var(--ink)">SUN</text><circle cx="13" cy="10" r="9" fill="var(--panel)" stroke="${g}" stroke-width="2.4"/><path d="M19 16l7 7" stroke="${g}" stroke-width="3" stroke-linecap="round"/></g>`;
 case 2:return`<g class="ic"><rect x="-16" y="-24" width="32" height="44" rx="3" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><rect x="-11" y="-16" width="22" height="5" fill="${g}" opacity=".7"/><path d="M-11 -6h22M-11 0h16" stroke="${c}" stroke-width="1.4"/><rect x="-11" y="6" width="18" height="5" fill="${g}" opacity=".7"/></g>
  <g class="chip"><rect x="-58" y="-74" width="116" height="20" rx="10"/><text x="0" y="-60" text-anchor="middle">29.6°N · 48.0°E</text></g>
  <g class="chip" style="transition-delay:.15s"><rect x="-46" y="38" width="92" height="20" rx="10"/><text x="0" y="52" text-anchor="middle">Dec 2024 · Bahra 1</text></g>`;
 case 3:return`<g class="ic"><rect x="-24" y="-22" width="48" height="40" rx="5" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><path d="M-18 -2q8-12 16-4t18-6v14h-34z" fill="${sand}" stroke="${c}" stroke-width="1.2"/><circle cx="12" cy="-12" r="4" fill="${g}"/><text x="-12" y="14" text-anchor="middle" style="font:700 9px var(--f-body);fill:var(--ink)">EN</text><text x="12" y="14" text-anchor="middle" style="font:700 10px var(--f-body);fill:var(--ink)">ع</text></g>`;
 case 4:return`<g class="ic"><circle cx="0" cy="-8" r="9" fill="var(--sand)" stroke="${c}" stroke-width="1.6"/><path d="M-16 18q2-16 16-16t16 16z" fill="var(--you)" opacity=".85" stroke="${c}" stroke-width="1.4"/></g>
  <g><rect class="okbtn" x="-40" y="34" width="36" height="18" rx="9" fill="var(--line)"/><path d="M-30 43l4 4 7-8" fill="none" stroke="#fff" stroke-width="2.2"/><rect x="4" y="34" width="36" height="18" rx="9" fill="var(--panel)" stroke="var(--line)" stroke-width="1.4"/><path d="M17 39l8 8M25 39l-8 8" stroke="var(--mut)" stroke-width="2"/></g>`;
 case 5:return`<g class="ic" transform="translate(-24 -26) scale(.5)"><path d="${KW}" fill="${sand}" stroke="var(--coast)" stroke-width="2.4"/></g><g class="pin"><path d="M2 -14c-6 0-10 4-10 9 0 7 10 15 10 15s10-8 10-15c0-5-4-9-10-9z" fill="${g}" stroke="${c}" stroke-width="1.4"/><circle cx="2" cy="-5" r="3" fill="var(--panel)"/></g>`;
 case 6:return`<g class="ic"><path d="M-24 -16c8-4 16-4 24 1v32c-8-5-16-5-24-1z" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><path d="M24 -16c-8-4-16-4-24 1v32c8-5 16-5 24-1z" fill="var(--panel)" stroke="${c}" stroke-width="1.6"/><path d="M-19 4q5-8 10-3t8-3" fill="none" stroke="${sea}" stroke-width="2"/><circle cx="12" cy="-4" r="4" fill="${g}"/><path d="M5 8h14M5 13h10" stroke="${c}" stroke-width="1.3"/></g>`;
 }}
const st=document.getElementById('stations');
let trackD='M'+X(0)+' '+Y;for(let i=1;i<S.length;i++){const a=X(i-1),b=X(i);trackD+=` C${a+50} ${Y+(i%2?-46:46)} ${b-50} ${Y+(i%2?-46:46)} ${b} ${Y}`}
document.getElementById('track').setAttribute('d',trackD);
S.forEach((s,i)=>{const g=document.createElementNS(ns,'g');g.setAttribute('class','st');g.setAttribute('transform',`translate(${X(i)} ${Y})`);g.setAttribute('tabindex','0');g.setAttribute('role','button');g.setAttribute('aria-label',`Step ${i+1}: ${s.t}`);g.dataset.i=i;
 const col=s.who=='you'?'var(--you)':s.who=='all'?'var(--gold)':'var(--seaT)',wl=s.who=='you'?'YOU':s.who=='all'?'EVERYONE':'AUTOMATIC';
 g.innerHTML=`<circle class="ring" r="44"/>${icon(i)}<text class="who" y="-60" style="fill:${col}">${wl}</text><text class="lbl" y="76">${s.t}</text><text class="sub" y="93">${s.s}</text>`;
 if(i==2||i==4)g.querySelector('.who').setAttribute('y',i==2?'-84':'-60');
 st.appendChild(g)});
const pathEl=document.getElementById('track'),onEl=document.getElementById('trackOn'),pk=document.getElementById('packet');
const stopsLen=[0];{let acc=0;const tmp=document.createElementNS(ns,'path');document.getElementById('flow').appendChild(tmp);for(let i=1;i<S.length;i++){tmp.setAttribute('d',trackD.split(' C').slice(0,i+1).join(' C'));stopsLen.push(tmp.getTotalLength())}tmp.remove()}
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
let cur=0,playing=!reduce,timer=null,anim=null;
const dots=document.getElementById('dots');dots.innerHTML=S.map(()=>'<i></i>').join('');
function setPacket(len){const p=pathEl.getPointAtLength(len);pk.setAttribute('cx',p.x);pk.setAttribute('cy',p.y);onEl.setAttribute('d',trackD);onEl.style.strokeDasharray=`${len} 99999`}
function show(i,animate){const from=stopsLen[cur],to=stopsLen[i];cur=i;
 document.querySelectorAll('.st').forEach((g,k)=>{g.classList.toggle('on',k==i);g.classList.toggle('done',k<i)});
 dots.querySelectorAll('i').forEach((d,k)=>d.classList.toggle('on',k<=i));
 const s=S[i];document.getElementById('num').textContent=i+1;document.getElementById('ttl').textContent=s.ttl;document.getElementById('txt').textContent=s.txt;document.getElementById('ex').innerHTML=s.ex;
 const tg=document.getElementById('tag');tg.className='tag '+(s.who=='you'?'you':'auto');tg.textContent=s.who=='you'?(i==6?'When you ask':'Your step'):s.who=='all'?'For everyone':'Automatic';
 const bx=document.querySelector('.svgbox');if(bx.scrollWidth>bx.clientWidth){const sc=bx.scrollWidth/1000;bx.scrollTo({left:Math.max(0,X(i)*sc-bx.clientWidth/2),behavior:reduce||!animate?'auto':'smooth'})}
 cancelAnimationFrame(anim);
 if(!animate||reduce){setPacket(to);return}
 const t0=performance.now(),dur=900;const step=t=>{const k=Math.min(1,(t-t0)/dur),e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;setPacket(from+(to-from)*e);if(k<1)anim=requestAnimationFrame(step)};anim=requestAnimationFrame(step)}
function tick(){timer=setTimeout(()=>{show((cur+1)%S.length,cur+1<S.length);if(playing)tick()},cur==S.length-1?4200:3600)}
function setPlay(p){playing=p;document.getElementById('play').textContent=p?'Pause':'Play';clearTimeout(timer);if(p)tick()}
document.getElementById('play').onclick=()=>setPlay(!playing);
document.getElementById('next').onclick=()=>{setPlay(false);show((cur+1)%S.length,true)};
document.getElementById('prev').onclick=()=>{setPlay(false);show((cur+S.length-1)%S.length,true)};
st.addEventListener('click',e=>{const g=e.target.closest('.st');if(g){setPlay(false);show(+g.dataset.i,true)}});
st.addEventListener('keydown',e=>{if((e.key=='Enter'||e.key==' ')&&e.target.dataset.i){e.preventDefault();setPlay(false);show(+e.target.dataset.i,true)}});
show(0,false);setPlay(playing);
