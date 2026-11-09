"""Layers front page v3: LAYERS by GEOHERITAGE. Pre-rendered English text (works without scripts), Arabic toggle, editions in-page."""
import json, re, os, base64, sys, runpy
sys.path.insert(0, '/tmp/w/layers'); sys.path.insert(0, '/tmp/w')
import hub as H
SITE = '/tmp/w/layers/site'; OUT = '/tmp/w/layers/one'
BASE = 'https://smbehbehani-max.github.io/Layers2/docs/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
os.makedirs(OUT, exist_ok=True)
from onefile2 import patch_edition

ART = runpy.run_path('/tmp/w/art.py')['ART']
_w = lambda body: f'<svg viewBox="0 0 400 220" aria-hidden="true">{body}</svg>'
for m in ('art_a', 'art_g', 'art_e'):
    for k, v in runpy.run_path(f'/tmp/w/{m}.py')['A'].items(): ART[k] = _w(v)
KV = open('/tmp/w/layers/kvars.css').read(); ARTCSS = open('/tmp/w/layers/artcss.css').read()

def texts(total):
    EN = {
     'wm': 'LAYERS', 'by': 'by GEOHERITAGE', 'lang': 'عربي', 'n1': 'Explore', 'n2': 'What is Layers', 'n3': 'Destinations',
     'h1': 'Discover the Gulf <em>Beyond the Ordinary.</em>',
     'hl': 'Explore destinations through geological, archaeological and ecological layers, with AI revealing the connections and stories behind each place.',
     'c1': 'Explore the Gulf', 'c2': 'What is LAYERS?', 'c3': 'Choose a country', 'cap': 'Tap a country to open it',
     's1n': str(total), 's1': 'places', 's2n': '6', 's2': 'Gulf countries', 's3n': '3', 's3': 'layers', 's4n': '2', 's4': 'languages',
     'k2': 'What is LAYERS', 't2': 'One Landscape. Multiple Stories.',
     'l2': 'Every place in the Gulf can be read through three layers of knowledge. They are not three subjects — they are three dimensions of the same landscape, and the logo shows them: a Gulf country seen as its layers, from top to bottom.',
     'st1': 'Ecological', 'st1d': 'The living surface: habitats, wetlands, reefs, species',
     'st2': 'Archaeological', 'st2d': 'The human layer: settlements, tombs, inscriptions, ports',
     'st3': 'Geological', 'st3d': 'The Earth beneath: rock, fossils, landforms, deep time',
     'g1': 'Geological', 'g1d': 'Formations, fossils, craters, lava fields, dunes and springs — the deep-time stage on which everything else happened.',
     'g2': 'Archaeological', 'g2d': 'Settlements, tombs, inscriptions, ports and forts — from the first herders to the pearling towns and the first oil wells.',
     'g3': 'Ecological', 'g3d': 'Reserves, wetlands, reefs, mangroves and the species that depend on them — the living layer, and the one most at risk.',
     'ai': 'Artificial Intelligence', 'aid': 'Connecting knowledge, interpreting relationships and revealing stories.',
     'ai1': 'Connects the layers', 'ai1d': 'Why a town rose where water left the rock; why the birds still come to the same shore.',
     'ai2': 'Interprets relationships', 'ai2d': 'Reads geology, archaeology and ecology together, not as separate summaries.',
     'ai3': 'Simplifies research', 'ai3d': 'Turns published papers into stories a traveller would tell — with the sources kept in place.',
     'ai4': 'Proposes hypotheses', 'ai4d': 'Explores connections not yet documented, always labelled as untested ideas with their reasoning.',
     'tag': 'A new way to experience the Gulf.',
     'k3': 'Explore the Gulf', 't3': 'Six countries, one landscape', 'l3': 'Choose a country to open its layers: map, timeline, explorer routes, live directions, in Arabic and English, offline too.',
     'places': 'places', 'arch': 'archaeology', 'geo': 'geology', 'eco': 'ecology', 'lg1': 'Archaeological', 'lg2': 'Geological', 'lg3': 'Ecology',
     'wl1': 'Arabian Gulf', 'wl2': 'Red Sea', 'wl3': 'Arabian Sea',
     'k4': 'Destinations', 't4': 'Places you did not know you could visit', 'l4': f'A few of the {total} places across the six countries. Tap one to open it on its map.',
     'pa': 'Archaeology', 'pg': 'Geology', 'pe': 'Ecology', 'ps': 'AI hypothesis',
     'k5': 'GEOHERITAGE', 't5': 'The website behind LAYERS',
     'l5': 'GEO is geological — the Earth itself — and geographical: the places on its surface where archaeology and ecology show themselves. HERITAGE is what makes those places matter: scientific, natural, historical and cultural. LAYERS is how you explore it.',
     'f1': 'Every place carries its sources. Facts come from published research, heritage bodies and official reports; illustrated stories and AI hypotheses are marked as such.',
     'priv': 'Privacy', 'made': 'Made in Kuwait', 'loading': 'Opening…',
    }
    AR = {
     'wm': 'طبقات', 'by': 'من جيوهيريتيج', 'lang': 'English', 'n1': 'استكشف', 'n2': 'ما هو «طبقات»', 'n3': 'الوجهات',
     'h1': 'اكتشف الخليج <em>بما يتجاوز المألوف.</em>',
     'hl': 'استكشف الوجهات عبر طبقاتها الجيولوجية والأثرية والبيئية، مع ذكاء اصطناعي يكشف الروابط والقصص خلف كل مكان.',
     'c1': 'استكشف الخليج', 'c2': 'ما هو «طبقات»؟', 'c3': 'اختر دولة', 'cap': 'اضغط على دولة لفتحها',
     's1n': str(total), 's1': 'موقعًا', 's2n': '6', 's2': 'دول خليجية', 's3n': '3', 's3': 'طبقات', 's4n': '2', 's4': 'لغتان',
     'k2': 'ما هو «طبقات»', 't2': 'أرض واحدة. قصص متعددة.',
     'l2': 'كل مكان في الخليج يمكن قراءته عبر ثلاث طبقات من المعرفة. ليست ثلاثة مواضيع، بل ثلاثة أبعاد للأرض نفسها، وهذا ما يظهره الشعار: دولة خليجية تُرى بطبقاتها من الأعلى إلى الأسفل.',
     'st1': 'البيئة', 'st1d': 'السطح الحي: موائل وأراضٍ رطبة وشعاب وأنواع',
     'st2': 'الآثار', 'st2d': 'الطبقة البشرية: مستوطنات ومقابر ونقوش وموانئ',
     'st3': 'الجيولوجيا', 'st3d': 'الأرض في الأسفل: صخر وأحافير وتضاريس وزمن سحيق',
     'g1': 'جيولوجيا', 'g1d': 'تكوينات وأحافير وفوهات وحرّات وكثبان وعيون — مسرح الزمن السحيق الذي جرى عليه كل شيء آخر.',
     'g2': 'آثار', 'g2d': 'مستوطنات ومقابر ونقوش وموانئ وقلاع — من أوائل الرعاة إلى مدن اللؤلؤ وأولى آبار النفط.',
     'g3': 'بيئة', 'g3d': 'محميات وأراضٍ رطبة وشعاب وقرم والأنواع التي تعتمد عليها — الطبقة الحيّة، وهي الأكثر عرضة للخطر.',
     'ai': 'الذكاء الاصطناعي', 'aid': 'يربط المعرفة، ويفسّر العلاقات، ويكشف القصص.',
     'ai1': 'يربط الطبقات', 'ai1d': 'لماذا قامت بلدة حيث خرج الماء من الصخر؛ ولماذا ما زالت الطيور تأتي إلى الشاطئ نفسه.',
     'ai2': 'يفسّر العلاقات', 'ai2d': 'يقرأ الجيولوجيا والآثار والبيئة معًا، لا كملخصات منفصلة.',
     'ai3': 'يبسّط البحث العلمي', 'ai3d': 'يحوّل الأوراق المنشورة إلى قصص يرويها المسافر — مع إبقاء المصادر في مكانها.',
     'ai4': 'يقترح فرضيات', 'ai4d': 'يستكشف روابط لم تُوثَّق بعد، مُعلَّمة دائمًا كأفكار غير مختبَرة مع منطقها.',
     'tag': 'طريقة جديدة لتجربة الخليج.',
     'k3': 'استكشف الخليج', 't3': 'ست دول وأرض واحدة', 'l3': 'اختر دولة لفتح طبقاتها: خريطة وخط زمني ومسارات استكشاف وإرشادات حيّة، بالعربية والإنجليزية، ودون إنترنت أيضًا.',
     'places': 'موقعًا', 'arch': 'آثار', 'geo': 'جيولوجيا', 'eco': 'بيئة', 'lg1': 'آثار', 'lg2': 'جيولوجيا', 'lg3': 'بيئة',
     'wl1': 'الخليج العربي', 'wl2': 'البحر الأحمر', 'wl3': 'بحر العرب',
     'k4': 'الوجهات', 't4': 'أماكن لم تكن تعرف أنك تستطيع زيارتها', 'l4': f'بعض من {total} موقعًا في الدول الست. اضغط على أحدها لفتحه على خريطته.',
     'pa': 'آثار', 'pg': 'جيولوجيا', 'pe': 'بيئة', 'ps': 'فرضية ذكية',
     'k5': 'جيوهيريتيج', 't5': 'الموقع الذي يقف خلف «طبقات»',
     'l5': '«جيو» هي الجيولوجيا — الأرض نفسها — والجغرافيا: الأماكن على سطحها حيث تظهر الآثار والبيئة. و«التراث» هو ما يجعل تلك الأماكن مهمة: علميًا وطبيعيًا وتاريخيًا وثقافيًا. و«طبقات» هو طريقك لاستكشافه.',
     'f1': 'كل موقع يحمل مصادره. الحقائق مأخوذة من أبحاث منشورة وهيئات التراث والتقارير الرسمية؛ والقصص المصوّرة والفرضيات الذكية مميّزة بوضوح.',
     'priv': 'الخصوصية', 'made': 'صُنع في الكويت', 'loading': 'جارٍ الفتح…',
    }
    for cc in ORDER:
        c = H.C[cc]; EN['c.' + cc] = c['en']; AR['c.' + cc] = c['ar']; EN['ct.' + cc] = c['ten']; AR['ct.' + cc] = c['tar']
    return EN, AR

def build(mode='pc', fname='index.html'):
    data = {cc: dict(zip(['n', 'k'], H.counts(cc))) for cc in ORDER}
    IDX = {}; S = {}
    for cc in ORDER:
        for s in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']: IDX[s['id']] = cc; S[(cc, s['id'])] = s
    total = sum(data[cc]['n'] for cc in ORDER)
    EN, AR = texts(total)
    for cc in ORDER:
        d = data[cc]; k = d['k']
        EN['cs.' + cc] = f"{d['n']} places · {k['archaeological']} archaeology · {k['geological']} geology · {k['ecology']} ecology"
        AR['cs.' + cc] = f"{d['n']} موقعًا · {k['archaeological']} آثار · {k['geological']} جيولوجيا · {k['ecology']} بيئة"
    SHOW = [('sa', 'hegra'), ('kw', 'mud-volcano-z3'), ('om', 'bimmah-sinkhole'), ('ae', 'mleisa-elephant-trackway'), ('bh', 'al-sayah-island'), ('qa', 'ruwayda'), ('sa', 'umm-jirsan'), ('om', 'arabian-sea-humpback'), ('kw', 'spec-polychrome-escarpment'), ('ae', 'al-sinniyah-island'), ('bh', 'tree-of-life'), ('qa', 'dahl-al-misfir')]
    CV = {'archaeological': ('arch', 'pa'), 'geological': ('geo', 'pg'), 'ecology': ('eco', 'pe'), 'speculative': ('spec', 'ps')}
    show = ''
    for i, (cc, sid) in enumerate(SHOW):
        s = S[(cc, sid)]; cv, pk = CV[s['c']]
        EN[f'sh{i}h'] = s['te']; AR[f'sh{i}h'] = s['ta']; EN[f'sh{i}n'] = s['n']; AR[f'sh{i}n'] = s['na']
        show += f'<a class="sh" href="#{cc}/p={sid}" style="--c:var(--{cv})"><span class="pill" data-i="{pk}">{EN[pk]}</span><span class="cc" data-i="c.{cc}">{EN["c."+cc]}</span><h4 data-i="sh{i}h">{s["te"]}</h4><p data-i="sh{i}n">{s["n"]}</p></a>'
    M = H.M; W, Hh = M['w'], M['h']; VY0 = -70; VH = Hh + 70
    shapes = ''.join(f'<path class="cs" data-cc="{cc}" d="{M["paths"][cc]}"/>' for cc in ORDER)
    badges = ''; leaders = ''; cards = ''
    for cc in ORDER:
        c = H.C[cc]; x, y = H.P(*c['pt']); bx, by = H.P(*c['bd'])
        if (bx, by) != (x, y): leaders += f'<line class="ld" x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/><circle class="ldp" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
        badges += f'<a class="bd" href="#{cc}" data-cc="{cc}" style="left:{bx/W*100:.2f}%;top:{(by-VY0)/VH*100:.2f}%"><span class="bdl">{H.flag_logo(cc, "bd"+cc)}</span><span class="bdn" data-i="c.{cc}">{c["en"]}</span><span class="bdc">{data[cc]["n"]}</span></a>'
        cards += f'<a class="card" href="#{cc}" data-cc="{cc}"><span class="cl">{H.flag_logo(cc, "cd"+cc)}</span><span class="ct"><b data-i="ct.{cc}">{c["ten"]}</b><small data-i="cs.{cc}">{EN["cs."+cc]}</small></span><span class="go" aria-hidden="true">›</span></a>'
    wl = ''.join(f'<text class="wl" data-i="wl{i+1}" x="{H.P(*g)[0]:.0f}" y="{H.P(*g)[1]:.0f}">{EN["wl"+str(i+1)]}</text>' for i, g in enumerate([(50.9, 28.9), (36.8, 21.0), (56.8, 16.9)]))
    b64 = lambda f: base64.b64encode(open(f'{SITE}/{f}', 'rb').read()).decode()
    man = {'name': 'Layers · طبقات', 'short_name': 'Layers', 'start_url': BASE, 'scope': BASE, 'display': 'standalone', 'background_color': '#f7f8f5', 'theme_color': '#f7f8f5',
           'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'}]}
    manifest = 'data:application/manifest+json;base64,' + base64.b64encode(json.dumps(man, ensure_ascii=False).encode()).decode()
    html = open('/tmp/w/layers/hub3_tpl.html', encoding='utf-8').read()
    # [[key]] -> span with EN text; [[=key]] -> plain EN text; [[!key]] -> innerHTML allowed (h1)
    def sub(m):
        f, k = m.group(1), m.group(2)
        if f == '=': return EN[k]
        return f'<span data-i="{k}"{" data-html=1" if f=="!" else ""}>{EN[k]}</span>'
    html = re.sub(r'\[\[([=!]?)([a-zA-Z0-9_.]+)\]\]', sub, html)
    big_logo = H.plain_logo('big')
    rep = {'__SHAPES__': shapes, '__LEADERS__': leaders, '__BADGES__': badges, '__CARDS__': cards, '__WL__': wl, '__W__': f'{W:.0f}', '__H__': f'{VH:.0f}', '__VY0__': f'{VY0:.0f}', '__SHOW__': show,
           '__LOGO__': H.plain_logo('hub'), '__BIGLOGO__': big_logo, '__IDX__': json.dumps(IDX), '__TEXTS__': json.dumps({'en': EN, 'ar': AR}, ensure_ascii=False), '__BASE__': BASE, '__TOTAL__': str(total), '__MANIFEST__': manifest,
           '__KV__': KV, '__ARTCSS__': ARTCSS, '__ART_G__': ART['jal-az-zor'], '__ART_A__': ART['failaka-island'], '__ART_E__': ART['khor-sabiyah-marsh'], '__MODE__': mode,
           '__CN__': json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in H.C.items()}, ensure_ascii=False)}
    for k, v in rep.items(): html = html.replace(k, v)
    leftover = re.findall(r'__[A-Z_]+__', html); assert not leftover, leftover
    payload = ''.join(f'<script type="text/plain" id="ed-{cc}">{patch_edition(cc)}</script>\n' for cc in ORDER)
    html = html.replace('<!--PAYLOAD-->', payload)
    open(f'{OUT}/{fname}', 'w', encoding='utf-8').write(html)
    return total, os.path.getsize(f'{OUT}/{fname}')

if __name__ == '__main__':
    print(build('pc', 'index.html')); print(build('mob', 'mobile.html'))
