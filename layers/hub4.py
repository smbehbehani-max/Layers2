"""Layers front page v3: LAYERS by GEOHERITAGE. Pre-rendered English text (works without scripts), Arabic toggle, editions in-page."""
import json, re, os, base64, sys, runpy
sys.path.insert(0, '/tmp/w/layers'); sys.path.insert(0, '/tmp/w')
import hub as H
SITE = '/tmp/w/layers/site'; OUT = '/tmp/w/layers/one'
BASE = 'https://smbehbehani-max.github.io/Layers/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
os.makedirs(OUT, exist_ok=True)
from onefile2 import patch_edition

ART = runpy.run_path('/tmp/w/art.py')['ART']
_w = lambda body: f'<svg viewBox="0 0 400 220" aria-hidden="true">{body}</svg>'
for m in ('art_a', 'art_g', 'art_e'):
    for k, v in runpy.run_path(f'/tmp/w/{m}.py')['A'].items(): ART[k] = _w(v)
KV = open('/tmp/w/layers/kvars.css').read(); ARTCSS = open('/tmp/w/layers/artcss.css').read()

def texts(total):
    EN = {'lang': 'عربي', 'by': 'by GEOHERITAGE', 'tag1': 'Discover the Gulf Beyond the Ordinary.', 'c1': 'Explore the Gulf',
     'k2': 'What is LAYERS', 't2': 'One Landscape. Multiple Stories.', 'st1': 'Ecological', 'st2': 'Archaeological', 'st3': 'Geological',
     'g1': 'Geological', 'g2': 'Archaeological', 'g3': 'Ecological',
     'k3': 'Powered by', 'ai': 'Artificial Intelligence', 'aid': 'Connecting knowledge, interpreting relationships and revealing stories.',
     'tag2': 'A new way to experience the Gulf.', 'k4': 'Six countries', 't4': 'Explore the Gulf',
     'wl1': 'Arabian Gulf', 'wl2': 'Red Sea', 'wl3': 'Arabian Sea',
     'f1': 'GEO — geological and geographical. HERITAGE — what makes a place matter. LAYERS — how you explore it.',
     'priv': 'Privacy', 'made': 'Made in Kuwait', 'loading': 'Opening…'}
    AR = {'lang': 'English', 'by': 'من جيوهيريتيج', 'tag1': 'اكتشف الخليج بما يتجاوز المألوف.', 'c1': 'استكشف الخليج',
     'k2': 'ما هو «طبقات»', 't2': 'أرض واحدة. قصص متعددة.', 'st1': 'البيئة', 'st2': 'الآثار', 'st3': 'الجيولوجيا',
     'g1': 'جيولوجيا', 'g2': 'آثار', 'g3': 'بيئة',
     'k3': 'بقوة', 'ai': 'الذكاء الاصطناعي', 'aid': 'يربط المعرفة، ويفسّر العلاقات، ويكشف القصص.',
     'tag2': 'طريقة جديدة لتجربة الخليج.', 'k4': 'ست دول', 't4': 'استكشف الخليج',
     'wl1': 'الخليج العربي', 'wl2': 'البحر الأحمر', 'wl3': 'بحر العرب',
     'f1': 'جيو — الجيولوجيا والجغرافيا. التراث — ما يجعل المكان مهمًا. طبقات — طريقك لاستكشافه.',
     'priv': 'الخصوصية', 'made': 'صُنع في الكويت', 'loading': 'جارٍ الفتح…'}
    for cc in ORDER:
        c = H.C[cc]; EN['c.' + cc] = c['en'].replace('the UAE', 'UAE'); AR['c.' + cc] = c['ar']
    return EN, AR


def build(mode='pc', fname='index.html'):
    data = {cc: dict(zip(['n', 'k'], H.counts(cc))) for cc in ORDER}
    IDX = {}; S = {}
    for cc in ORDER:
        for s in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']: IDX[s['id']] = cc; S[(cc, s['id'])] = s
    total = sum(data[cc]['n'] for cc in ORDER)
    EN, AR = texts(total)
    for cc in []:
        d = data[cc]; k = d['k']
        EN['cs.' + cc] = f"{d['n']} places · {k['archaeological']} archaeology · {k['geological']} geology · {k['ecology']} ecology"
        AR['cs.' + cc] = f"{d['n']} موقعًا · {k['archaeological']} آثار · {k['geological']} جيولوجيا · {k['ecology']} بيئة"
    SHOW = [('sa', 'hegra'), ('kw', 'mud-volcano-z3'), ('om', 'bimmah-sinkhole'), ('ae', 'mleisa-elephant-trackway'), ('bh', 'al-sayah-island'), ('qa', 'ruwayda'), ('sa', 'umm-jirsan'), ('om', 'arabian-sea-humpback'), ('kw', 'spec-polychrome-escarpment'), ('ae', 'al-sinniyah-island'), ('bh', 'tree-of-life'), ('qa', 'dahl-al-misfir')]
    CV = {'archaeological': ('arch', 'pa'), 'geological': ('geo', 'pg'), 'ecology': ('eco', 'pe'), 'speculative': ('spec', 'ps')}
    show = ''
    for i, (cc, sid) in enumerate(SHOW):
        s = S[(cc, sid)]; cv, pk = CV[s['c']]
        continue
        EN[f'sh{i}h'] = s['te']; AR[f'sh{i}h'] = s['ta']; EN[f'sh{i}n'] = s['n']; AR[f'sh{i}n'] = s['na']
        show += f'<a class="sh" href="#{cc}/p={sid}" style="--c:var(--{cv})"><span class="pill" data-i="{pk}">{EN[pk]}</span><span class="cc" data-i="c.{cc}">{EN["c."+cc]}</span><h4 data-i="sh{i}h">{s["te"]}</h4><p data-i="sh{i}n">{s["n"]}</p></a>'
    M = H.M; W, Hh = M['w'], M['h']; VY0 = -70; VH = Hh + 70
    shapes = ''.join(f'<path class="cs" data-cc="{cc}" d="{M["paths"][cc]}"/>' for cc in ORDER)
    badges = ''; leaders = ''; cards = ''
    for cc in ORDER:
        c = H.C[cc]; x, y = H.P(*c['pt']); bx, by = H.P(*c['bd'])
        if (bx, by) != (x, y): leaders += f'<line class="ld" x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/><circle class="ldp" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
        badges += f'<a class="bd" href="#{cc}" data-cc="{cc}" style="left:{bx/W*100:.2f}%;top:{(by-VY0)/VH*100:.2f}%"><span class="bdl">{H.flag_logo(cc, "bd"+cc)}</span><span class="bdn" data-i="c.{cc}">{EN["c."+cc]}</span><span class="bdc">{data[cc]["n"]}</span></a>'
        pass
    wl = ''.join(f'<text class="wl" data-i="wl{i+1}" x="{H.P(*g)[0]:.0f}" y="{H.P(*g)[1]:.0f}">{EN["wl"+str(i+1)]}</text>' for i, g in enumerate([(50.9, 28.9), (36.8, 21.0), (56.8, 16.9)]))
    b64 = lambda f: base64.b64encode(open(f'{SITE}/{f}', 'rb').read()).decode()
    man = {'name': 'Layers · طبقات', 'short_name': 'Layers', 'start_url': BASE, 'scope': BASE, 'display': 'standalone', 'background_color': '#f7f8f5', 'theme_color': '#f7f8f5',
           'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'}]}
    manifest = 'data:application/manifest+json;base64,' + base64.b64encode(json.dumps(man, ensure_ascii=False).encode()).decode()
    html = open('/tmp/w/layers/hub4_tpl.html', encoding='utf-8').read()
    # [[key]] -> span with EN text; [[=key]] -> plain EN text; [[!key]] -> innerHTML allowed (h1)
    def sub(m):
        f, k = m.group(1), m.group(2)
        if f == '=': return EN[k]
        return f'<span data-i="{k}"{" data-html=1" if f=="!" else ""}>{EN[k]}</span>'
    html = re.sub(r'\[\[([=!]?)([a-zA-Z0-9_.]+)\]\]', sub, html)
    big_logo = H.plain_logo('big')
    LP = json.load(open('/tmp/w/layers/logo_parts.json'))
    pills = ''.join(f'<a class="pill" href="#{cc}" data-cc="{cc}"><span class="l">{H.flag_logo(cc, "pl"+cc)}</span><span data-i="c.{cc}">{EN["c."+cc]}</span></a>' for cc in ORDER)
    rep = {'__SHAPES__': shapes, '__LEADERS__': leaders, '__BADGES__': badges, '__CARDS__': cards, '__WL__': wl, '__W__': f'{W:.0f}', '__H__': f'{VH:.0f}', '__VY0__': f'{VY0:.0f}', '__SHOW__': show,
           '__LOGO__': H.plain_logo('hub'), '__BIGLOGO__': big_logo, '__IDX__': json.dumps(IDX), '__TEXTS__': json.dumps({'en': EN, 'ar': AR}, ensure_ascii=False), '__BASE__': BASE, '__TOTAL__': str(total), '__MANIFEST__': manifest,
           '__KV__': KV, '__ARTCSS__': ARTCSS, '__ART_G__': ART['jal-az-zor'], '__ART_A__': ART['failaka-island'], '__ART_E__': ART['khor-sabiyah-marsh'], '__MODE__': mode, '__PILLS__': pills, '__BANDS__': ''.join(LP['bands']), '__CAMEL__': LP['camel'],
           '__CN__': json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in H.C.items()}, ensure_ascii=False)}
    for k, v in rep.items(): html = html.replace(k, v)
    leftover = re.findall(r'__[A-Z_]+__', html); assert not leftover, leftover
    payload = ''.join(f'<script type="text/plain" id="ed-{cc}">{patch_edition(cc)}</script>\n' for cc in ORDER)
    html = html.replace('<!--PAYLOAD-->', payload)
    open(f'{OUT}/{fname}', 'w', encoding='utf-8').write(html)
    return total, os.path.getsize(f'{OUT}/{fname}')

if __name__ == '__main__':
    print(build('pc', 'index.html')); print(build('mob', 'mobile.html'))
