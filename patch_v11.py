# Applies the v1.1 enhancements to the template: tpl2.html -> tpl3.html
import re
src = open('/tmp/w/tpl2.html', encoding='utf-8').read()
h = src

def rep(old, new, n=1):
    global h
    c = h.count(old)
    assert c == n, (c, old[:90])
    h = h.replace(old, new)

# ---------- 0. flags ----------
rep("const D=__DATA__,KW=__KW__,ART=__ART__;",
    "const STANDALONE=false,APP_VERSION='1.1.0';\nconst D=__DATA__,KW=__KW__,ART=__ART__;\nconst SHARE_BASE=STANDALONE?location.href.split(/[?#]/)[0]:'https://smbehbehani-max.github.io/Layers2/';")

# ---------- 1. visible search ----------
rep('<input type="hidden" id="q">',
    '<label class="search"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4-4"/></svg><input type="search" id="q" autocomplete="off" autocorrect="off" enterkeyhint="search"></label>')
rep('.search input{width:200px;padding:8px 12px 8px 32px;',
    '.search input{width:200px;padding:8px 12px;padding-inline-start:32px;-webkit-appearance:none;appearance:none;')
rep('.tools>.live{order:-2}#views{order:-1}', '.tools>.live{order:-3}.tools>.search{order:-2}#views{order:-1}')
rep("$('#lang').textContent=t.lang;$('#lang').lang=lang=='ar'?'en':'ar';",
    "$('#lang').textContent=t.lang;$('#lang').lang=lang=='ar'?'en':'ar';{const qi=$('#q');if(qi){qi.placeholder=t.search;qi.setAttribute('aria-label',t.search)}const ib=$('#inst');if(ib)ib.textContent=INS[lang].btn;if(typeof instUI=='function')instUI()}")
rep("$('#q').oninput=e=>{q=e.target.value.trim().toLowerCase();render()};",
    "$('#q').oninput=e=>{q=e.target.value.trim().toLowerCase();render()};$('#q').onkeydown=e=>{if(e.key=='Enter')e.target.blur()};")

# ---------- 2. strings ----------
rep("welT:'How would you like to explore?',", "share:'Share',copied:'Link copied',welT:'How would you like to explore?',")
rep("welT:'كيف تحب أن تستكشف؟',", "share:'مشاركة',copied:'تم نسخ الرابط',welT:'كيف تحب أن تستكشف؟',")

# ---------- 3. share button + deep links ----------
rep("if(db&&!db.querySelector('.spk'))db.insertAdjacentHTML('afterbegin',spkBtn());",
    "if(db&&!db.querySelector('.spk'))db.insertAdjacentHTML('afterbegin',spkBtn()+(sel?shareBtn(sel):''));if(sel)try{history.replaceState(null,'','#p='+encodeURIComponent(sel))}catch(e){}")
rep("function closeDet(){stopSpk();$('#det').classList.remove('on');sel=null;chap=-1;render()}",
    "function closeDet(){stopSpk();$('#det').classList.remove('on');sel=null;chap=-1;render();try{if(location.hash.indexOf('#p=')==0)history.replaceState(null,'',location.pathname+location.search)}catch(e){}}\n"
    "function shareBtn(id){return`<button class=\"spk share\" data-share=\"${id}\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><g class=\"w\" fill=\"none\"><circle cx=\"18\" cy=\"5\" r=\"2.6\"/><circle cx=\"6\" cy=\"12\" r=\"2.6\"/><circle cx=\"18\" cy=\"19\" r=\"2.6\"/><path d=\"M8.3 13.4l7.4 4.3M15.7 6.3L8.3 10.6\"/></g></svg><span>${E(L().share)}</span></button> `}\n"
    "function shareSite(id){const s=D.sites.find(x=>x.id==id);if(!s)return;const url=SHARE_BASE+'#p='+encodeURIComponent(id),title=ttl(s)+' · '+L().title,text=(mode=='e'?(lang=='ar'?s.sa:s.se):s.s)||'';\n"
    " if(navigator.share){navigator.share({title,text,url}).catch(()=>{})}else if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(url).then(()=>toast(L().copied),()=>prompt(L().share,url))}else prompt(L().share,url)}")
rep(" if(b.classList.contains('x'))return closeDet();\n",
    " if(b.classList.contains('x'))return closeDet();if(b.dataset.share)return shareSite(b.dataset.share);\n")
rep(".spk.golive{background:#2f7bf6;",
    ".spk.share{margin-inline-start:4px}.spk.share svg .w{fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}\n.spk.golive{background:#2f7bf6;")

# ---------- 4. tap targets on phones ----------
rep(".lg svg{width:22px;height:22px}.lg.on svg{width:36px;height:36px}",
    ".lg svg{width:22px;height:22px}.lg.on svg{width:36px;height:36px}.lg{padding:7px;margin:-7px}.lg.on{padding:2px;margin:-2px}")

# ---------- 5. welcome card can be dismissed ----------
rep("if(!welcomed)h+=`<div class=\"card welcome\"><h2>${E(L().welT)}</h2>",
    "if(!welcomed)h+=`<div class=\"card welcome\"><button class=\"wx\" data-w=\"${mode}\" aria-label=\"${E(L().close)}\">×</button><h2>${E(L().welT)}</h2>")
rep(".welcome h2{margin:0 0 4px;",
    ".card.welcome{position:relative}.welcome .wx{position:absolute;top:2px;inset-inline-end:2px;border:0;background:transparent;color:var(--mut);font-size:22px;line-height:1;padding:6px 10px;cursor:pointer;border-radius:8px}.welcome .wx:hover{color:var(--ink)}\n.welcome h2{margin:0 0 4px;padding-inline-end:26px;")

# ---------- 6. install button + sheet container ----------
rep('<button class="act ghost" id="hwb"></button>',
    '<button class="act ghost" id="hwb"></button><button class="act ghost" id="inst" hidden></button>')
rep('<div id="soon" class="soon" hidden role="dialog" aria-modal="true"></div>',
    '<div id="soon" class="soon" hidden role="dialog" aria-modal="true"></div>\n<div id="sheet" class="soon" hidden role="dialog" aria-modal="true"></div>')

# ---------- 7. How-it-works footer (About & privacy) ----------
rep(" <div class=\"hw-strip\">${t.strip.map(s=>`<div><div class=\"k ${s[0]}\">${E(s[1])}</div><h4>${E(s[2])}</h4><p>${E(s[3])}</p></div>`).join('')}</div></div>`;",
    " <div class=\"hw-strip\">${t.strip.map(s=>`<div><div class=\"k ${s[0]}\">${E(s[1])}</div><h4>${E(s[2])}</h4><p>${E(s[3])}</p></div>`).join('')}</div><div class=\"hw-foot\"><button class=\"lnk\" id=\"hw-about\">${E(INS[lang].about)}</button><span>· v${APP_VERSION}</span></div></div>`;")
rep(" if(b.classList.contains('hw-x'))return closeHow();if(b.id=='hw-play')return hwSetPlay(!hwPlay);",
    " if(b.classList.contains('hw-x'))return closeHow();if(b.id=='hw-about')return openAbout();if(b.id=='hw-play')return hwSetPlay(!hwPlay);")
rep(".soon-in .x{color:var(--ink);background:rgba(0,0,0,.07)}",
    ".soon-in .x{color:var(--ink);background:rgba(0,0,0,.07)}\n"
    ".hw-foot{margin-top:14px;display:flex;gap:8px;align-items:center;justify-content:center;color:var(--mut);font-size:13px}.hw-foot .lnk{border:0;background:none;color:var(--seaT);font:inherit;font-weight:600;text-decoration:underline;cursor:pointer;padding:4px}\n"
    ".soon-in ol{text-align:start;margin:0 0 14px;padding-inline-start:22px;line-height:1.55}.soon-in ol li{margin:0 0 6px}.soon-in .note{font-size:13px;color:var(--mut);margin:0 0 14px}.soon-in .lnks{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin:0 0 16px}.soon-in .lnks a{color:var(--seaT);font-weight:600}\n"
    ".sheet-ic{display:inline-block;width:20px;height:20px;vertical-align:-5px;margin:0 3px}.sheet-ic path,.sheet-ic rect{fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}\n"
    ".toast.updt{display:flex;gap:12px;align-items:center;z-index:90;bottom:max(16px,env(safe-area-inset-bottom,0px))}.toast.updt button{border:0;border-radius:99px;padding:6px 12px;background:var(--gold);color:#1a2a2b;font:600 13px var(--f-body);cursor:pointer}")

# ---------- 8. standalone text for How it works + install/about strings + logic ----------
INS = r"""
/* ---------- install, about, update, routes (v1.1) ---------- */
const INS={en:{btn:'Install app',t:'Install Layers of Kuwait',p:'Add it to your Home Screen to open it like an app: full screen, and it works without a connection.',
 ios:['Tap the <b>Share</b> button <svg class="sheet-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M8 7l4-4 4 4"/><path d="M5 11v8a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-8"/></svg> at the bottom of Safari','Scroll down and tap <b>Add to Home Screen</b> <svg class="sheet-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/></svg>','Tap <b>Add</b> at the top right'],
 iosNote:'If this page opened inside another app, open it in Safari first.',ok:'Done',upd:'A new version is ready.',reload:'Reload',about:'About & privacy',
 aT:'About Layers of Kuwait',aP1:'Layers of Kuwait maps the geology, archaeology and ecology of Kuwait: 80 places with their sources, illustrated stories, a 100-million-year timeline and live directions, in Arabic and English.',
 aP2:'Every record cites published research. AI connections are marked as untested ideas, never as findings.',
 aP3:'The app keeps nothing about you. Your location is used on your phone only while Go live is on and is never sent anywhere. Settings are saved on your device only.',
 privacy:'Privacy policy',site:'Website',made:'Made in Kuwait',version:'Version'},
 ar:{btn:'تثبيت التطبيق',t:'ثبّت طبقات الكويت',p:'أضفه إلى الشاشة الرئيسية ليفتح كتطبيق: بملء الشاشة، ويعمل دون اتصال.',
 ios:['اضغط زر <b>المشاركة</b> <svg class="sheet-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M8 7l4-4 4 4"/><path d="M5 11v8a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-8"/></svg> أسفل سفاري','مرّر للأسفل واضغط <b>إضافة إلى الشاشة الرئيسية</b> <svg class="sheet-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/></svg>','اضغط <b>إضافة</b> في الأعلى'],
 iosNote:'إذا فُتحت هذه الصفحة داخل تطبيق آخر، افتحها في سفاري أولًا.',ok:'تم',upd:'نسخة جديدة جاهزة.',reload:'إعادة التحميل',about:'حول التطبيق والخصوصية',
 aT:'حول طبقات الكويت',aP1:'يرسم تطبيق طبقات الكويت جيولوجيا الكويت وآثارها وبيئتها: 80 موقعًا بمصادرها، وقصص مصوّرة، وخط زمني يمتد 100 مليون سنة، وإرشادات حيّة، بالعربية والإنجليزية.',
 aP2:'كل سجل يستند إلى أبحاث منشورة. وتُعلَّم روابط الذكاء الاصطناعي كأفكار غير مختبرة، لا كاكتشافات.',
 aP3:'لا يحتفظ التطبيق بأي شيء عنك. يُستخدم موقعك على هاتفك فقط أثناء تشغيل «مباشر» ولا يُرسل إلى أي جهة. وتُحفظ الإعدادات على جهازك فقط.',
 privacy:'سياسة الخصوصية',site:'الموقع الإلكتروني',made:'صُنع في الكويت',version:'الإصدار'}};
const HW2={en:{sub:'From a new paper to a story on the map: how research is found, checked and published to the app.',
 strip:[['auto','RESEARCH · ONGOING','Search, read, draft','New papers, news and field reports about these places are gathered and read, and a short bilingual summary is drafted with a link to its source.'],
  ['you','AUTHOR · EVERY UPDATE','Check and approve','Nothing is published until the author has read the source and approved the summary. Rejected items are not suggested again.'],
  ['all','EVERYONE · NEXT UPDATE','Live in the app','Approved findings reach the app in its next update: on the place’s card and on the map. A new place can grow into a full entry with a story and a cartoon.']],
 steps:[['Sources','papers · news · PDFs','Research arrives from many places','Journals, news sites, field reports and the original PDF catalogue all describe these places. Researchers can also send their own stories by email from the Stories shelf.','<b>Example source:</b> Archeowieści, 2 Dec 2024: Kuwaiti-Polish team discovers figurine, local pottery, and environmental clues.'],
 ['Regular check','new papers · news','A search for anything new','Searches run regularly for new work on these places. Anything already queued, approved or rejected is skipped, so the same finding is never suggested twice.','<b>Searches like:</b> “Bahra 1 excavation”, “Failaka temple”, “Kuwait mud volcanoes”, “Al-Ahmadi quarry Dammam Formation”.'],
 ['Read & extract','place · date · coordinates','Each source is opened and read','Facts come only from pages actually opened: the place, the dates, the team, the link, and coordinates when the source states them. The finding is matched to a place on the map, or marked as a new place.','<b>Extracted:</b> Place → Bahra 1 · Published → Dec 2024 · Find → Ubaid-style clay head · Team → Kuwaiti-Polish mission.'],
 ['Write EN + AR','summary · title · source','A short summary in English and Arabic','A plain two-to-three sentence summary and title are written in both languages, using “Arabian Gulf”, with the source link kept so anyone can check it.','<b>Title:</b> A unique clay head and the Gulf’s oldest pottery workshop at Bahra 1<br><b>العنوان:</b> رأس طيني فريد وأقدم ورشة فخار في الخليج في بحرة 1'],
 ['Author reviews','approve · reject','Nothing goes live without the author','Each draft is read together with its source and approved or rejected by the author before it reaches anyone.','<b>Checked:</b> the source opens, the place matches, the dates agree → Approve.'],
 ['Live in the app','update · card · map','Approved findings appear in the next update','Approved findings appear as “New research” on the place’s card, with the link to the original source. A new place with coordinates appears as a gold star on the map.','<b>Shown on:</b> Bahra 1 card → New research → link to the original source.'],
 ['Grows into a story','title · story · cartoon','A new place can become a full entry','A new place can become a complete entry: researcher record, Explorer title and story in both languages, a cartoon, an icon and a bar on the timeline. That is how the Al-Ahmadi quarry was added.','<b>Example:</b> Al-Ahmadi quarry → “The Window into Deep Time” · Eocene Dammam Formation · 48–34 million years ago.']]},
 ar:{sub:'من ورقة علمية جديدة إلى قصة على الخريطة: كيف يُعثر على الأبحاث وتُراجع وتُنشر في التطبيق.',
 strip:[['auto','بحث · مستمر','بحث وقراءة وصياغة','تُجمع الأوراق الجديدة والأخبار والتقارير الميدانية حول هذه المواقع وتُقرأ، ويُصاغ ملخص قصير بلغتين مع رابط مصدره.'],
  ['you','المؤلف · مع كل تحديث','مراجعة وموافقة','لا يُنشر شيء قبل أن يقرأ المؤلف المصدر ويوافق على الملخص. وما رُفض لا يُقترح مرة أخرى.'],
  ['all','الجميع · في التحديث التالي','مباشرة في التطبيق','تصل الاكتشافات المعتمدة إلى التطبيق في تحديثه التالي: على بطاقة الموقع وعلى الخريطة. ويمكن أن يتحول موقع جديد إلى مدخل كامل بقصة ورسم.']],
 steps:[['المصادر','أوراق · أخبار · ملفات','الأبحاث تصل من أماكن كثيرة','المجلات العلمية والمواقع الإخبارية والتقارير الميدانية والكتالوج الأصلي كلها تصف هذه المواقع. ويمكن للباحثين أيضًا إرسال قصصهم بالبريد من رف القصص.','<b>مثال على مصدر:</b> Archeowieści، 2 ديسمبر 2024: الفريق الكويتي البولندي يكتشف تمثالًا وفخارًا محليًا وأدلة بيئية.'],
 ['فحص دوري','أوراق جديدة · أخبار','بحث عن كل جديد','يجري البحث دوريًا عن أعمال جديدة حول هذه المواقع. ويُتجاوز ما هو في القائمة أو معتمد أو مرفوض، فلا يُقترح الاكتشاف نفسه مرتين.','<b>عمليات بحث مثل:</b> «تنقيبات بحرة 1»، «معبد فيلكا»، «البراكين الطينية في الكويت»، «محجر الأحمدي تكوين الدمام».'],
 ['القراءة والاستخراج','الموقع · التاريخ · الإحداثيات','يُفتح كل مصدر ويُقرأ','تُؤخذ الحقائق فقط من صفحات فُتحت فعلًا: الموقع والتواريخ والفريق والرابط، والإحداثيات حين يذكرها المصدر. ثم يُربط الاكتشاف بموقع على الخريطة، أو يُعلَّم كموقع جديد.','<b>المستخرج:</b> الموقع ← بحرة 1 · النشر ← ديسمبر 2024 · الاكتشاف ← رأس طيني على طراز العبيد · الفريق ← البعثة الكويتية البولندية.'],
 ['الكتابة بلغتين','ملخص · عنوان · مصدر','ملخص قصير بالعربية والإنجليزية','يُكتب ملخص بسيط من جملتين أو ثلاث وعنوان باللغتين، باستخدام «الخليج العربي»، مع الاحتفاظ برابط المصدر ليتحقق منه أي أحد.','<b>Title:</b> A unique clay head and the Gulf’s oldest pottery workshop at Bahra 1<br><b>العنوان:</b> رأس طيني فريد وأقدم ورشة فخار في الخليج في بحرة 1'],
 ['مراجعة المؤلف','موافقة · رفض','لا شيء يُنشر دون المؤلف','تُقرأ كل مسودة مع مصدرها ويوافق عليها المؤلف أو يرفضها قبل أن تصل إلى أي أحد.','<b>التحقق:</b> يُفتح المصدر، ويُطابق الموقع، وتتفق التواريخ ← موافقة.'],
 ['مباشرة في التطبيق','تحديث · بطاقة · خريطة','تظهر الاكتشافات المعتمدة في التحديث التالي','تظهر الاكتشافات المعتمدة كـ«بحث جديد» على بطاقة الموقع مع رابط المصدر الأصلي. ويظهر الموقع الجديد ذو الإحداثيات نجمةً ذهبية على الخريطة.','<b>يظهر في:</b> بطاقة بحرة 1 ← بحث جديد ← رابط المصدر الأصلي.'],
 ['يصبح قصة','عنوان · قصة · رسم','الموقع الجديد قد يصبح مدخلًا كاملًا','يمكن أن يتحول الموقع الجديد إلى مدخل كامل: سجل للباحثين، وعنوان وقصة للمستكشف باللغتين، ورسم، وأيقونة، وشريط على الخط الزمني. هكذا أُضيف محجر الأحمدي.','<b>مثال:</b> محجر الأحمدي ← «نافذة على الزمن السحيق» · تكوين الدمام الإيوسيني · قبل 48–34 مليون سنة.']]}};
if(STANDALONE){['en','ar'].forEach(k=>Object.assign(HW[k],HW2[k]))}
let instEv=null;
const isStandalone=()=>{try{return matchMedia('(display-mode: standalone)').matches||navigator.standalone===true}catch(e){return false}};
const isIOS=/iPad|iPhone|iPod/.test(navigator.userAgent)||(navigator.platform=='MacIntel'&&navigator.maxTouchPoints>1);
function instUI(){const b=$('#inst');if(!b)return;b.textContent=INS[lang].btn;b.hidden=!STANDALONE||isStandalone()||!(instEv||isIOS)}
addEventListener('beforeinstallprompt',e=>{e.preventDefault();instEv=e;instUI()});
addEventListener('appinstalled',()=>{instEv=null;instUI()});
function openSheet(html){const s=$('#sheet');s.innerHTML=`<div class="soon-in"><button class="x" data-sheetx="1" aria-label="${E(L().close)}">×</button>${html}</div>`;s.hidden=false;const b=s.querySelector('.back');b&&b.focus()}
function closeSheet(){const s=$('#sheet');if(s&&!s.hidden){s.hidden=true;s.innerHTML=''}}
function openInstall(){const t=INS[lang];openSheet(`<h2>${E(t.t)}</h2><p>${E(t.p)}</p><ol>${t.ios.map(x=>`<li>${x}</li>`).join('')}</ol><p class="note">${E(t.iosNote)}</p><button class="back" data-sheetx="1">${E(t.ok)}</button>`)}
function openAbout(){const t=INS[lang];openSheet(`<div class="lgbig">${document.querySelector('.lg[data-lg="kw"] .v-on').outerHTML}</div><h2>${E(t.aT)}</h2><p>${E(t.aP1)}</p><p>${E(t.aP2)}</p><p>${E(t.aP3)}</p><div class="lnks">${STANDALONE?`<a href="privacy.html" target="_blank" rel="noopener">${E(t.privacy)}</a>`:''}<a href="https://smbehbehani-max.github.io/Layers2/" target="_blank" rel="noopener">${E(t.site)}</a></div><p class="note">${E(t.made)} · ${E(t.version)} ${APP_VERSION}</p><button class="back" data-sheetx="1">${E(t.ok)}</button>`)}
$('#inst').onclick=async()=>{if(instEv){try{instEv.prompt();await instEv.userChoice}catch(e){}instEv=null;instUI()}else openInstall()};
$('#sheet').addEventListener('click',e=>{if(e.target.id=='sheet'||e.target.closest('[data-sheetx]'))closeSheet()});
addEventListener('keydown',e=>{if(e.key=='Escape')closeSheet()});
function updToast(){if(document.querySelector('.updt'))return;const t=INS[lang],n=document.createElement('div');n.className='toast updt';n.innerHTML=`<span>${E(t.upd)}</span><button type="button">${E(t.reload)}</button>`;n.querySelector('button').onclick=()=>location.reload();document.body.appendChild(n)}
function route(){let hsh='';try{hsh=decodeURIComponent(location.hash.slice(1))}catch(e){hsh=location.hash.slice(1)}if(!hsh)return;let m;
 const toE=()=>{if(mode!='e'){mode='e';store.set('mode','e')}if(!welcomed){welcomed=true;store.set('welcomed',true)}chrome()};
 if((m=/^p=(.+)$/.exec(hsh))){const s=D.sites.find(x=>x.id==m[1]);if(s){if(!welcomed){welcomed=true;store.set('welcomed',true);chrome()}if(!on.has(s.c)){on.add(s.c);chrome()}if(view!='map')switchView('map');show(s.id)}}
 else if(hsh=='stories'){toE();openShelf()}
 else if((m=/^story=(.+)$/.exec(hsh))){toE();if(STORIES.find(s=>s.id==m[1]))openStory(m[1])}
 else if(hsh=='live'){if(!live.on)startLive()}
 else if(hsh=='timeline'){switchView('tl')}}
addEventListener('hashchange',route);
"""
rep("const HWKW=\"__HWKW__\";const KW_=HWKW;", "const HWKW=\"__HWKW__\";const KW_=HWKW;" + INS)
rep("chrome();fit();setVB();\n</script>", "chrome();fit();setVB();route();\n</script>")

open('/tmp/w/tpl3.html', 'w', encoding='utf-8').write(h)
print('ok', len(src), '->', len(h))
