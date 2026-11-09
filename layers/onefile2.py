"""Single-file Layers v2: light front page + six editions loaded in an in-page frame (no document.write)."""
import json, re, os, base64, sys
sys.path.insert(0, '/tmp/w/layers')
import hub as H
SITE = '/tmp/w/layers/site'
OUT = '/tmp/w/layers/one'
BASE = 'https://smbehbehani-max.github.io/Layers2/docs/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
os.makedirs(OUT, exist_ok=True)
VALID = "['kw','sa','bh','qa','ae','om']"

def patch_edition(cc):
    h = open(f'{SITE}/{cc}.html', encoding='utf-8').read()
    def rep(a, b, n=1):
        nonlocal h
        assert h.count(a) == n, (cc, a[:70], h.count(a))
        h = h.replace(a, b)
    # hash comes from the frame element (set by the hub), not from the frame's own URL
    rep("function route(){let hsh='';try{hsh=decodeURIComponent(location.hash.slice(1))}catch(e){hsh=location.hash.slice(1)}",
        "function LH(){try{return (frameElement&&frameElement.dataset.hash)||''}catch(e){return location.hash}}function route(){let hsh='';try{hsh=decodeURIComponent(LH().slice(1))}catch(e){hsh=LH().slice(1)}")
    rep("history.replaceState(null,'','#p='+encodeURIComponent(sel))", "parent.postMessage({layers:'hash',h:'#p='+encodeURIComponent(sel)},'*')")
    rep("try{if(location.hash.indexOf('#p=')==0)history.replaceState(null,'',location.pathname+location.search)}", "try{parent.postMessage({layers:'hash',h:''},'*')}")
    h2 = re.sub(r"SHARE_BASE=STANDALONE\?location\.href\.split\(/\[\?#\]/\)\[0\]:'[^']*'", "SHARE_BASE=(function(){try{return frameElement&&frameElement.dataset.base}catch(e){}return ''})()||'" + BASE + "'", h, count=1)
    assert h2 != h, (cc, 'SHARE_BASE'); h = h2
    rep("SHARE_BASE+'#p='", f"SHARE_BASE+'#{cc}/p='")
    rep("function goCountry(k){location.href=k+'.html'}", "function goCountry(k){parent.postMessage({layers:'open',cc:k},'*')}")
    rep("location.href='./'", "parent.postMessage({layers:'home'},'*')")
    h = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>\s*", "", h, count=1, flags=re.S)
    assert "serviceWorker' in navigator" not in h, cc
    # drop head links that make no sense inside a frame
    h = re.sub(r'<link rel="(manifest|apple-touch-icon|canonical)"[^>]*>', '', h)
    assert '<\\/script' not in h and '<!--' not in h
    return h.replace('</script', '<\\/script')

def build():
    data = {}
    for cc in ORDER: data[cc] = dict(zip(['n', 'k'], H.counts(cc)))
    IDX = {}; S = {}
    for cc in ORDER:
        for s in json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']: IDX[s['id']] = cc; S[(cc, s['id'])] = s
    total = sum(data[cc]['n'] for cc in ORDER)
    SHOW = [('sa', 'hegra'), ('kw', 'mud-volcano-z3'), ('om', 'bimmah-sinkhole'), ('ae', 'mleisa-elephant-trackway'), ('bh', 'al-sayah-island'), ('qa', 'ruwayda'), ('sa', 'umm-jirsan'), ('om', 'arabian-sea-humpback'), ('kw', 'spec-polychrome-escarpment'), ('ae', 'al-sinniyah-island'), ('bh', 'tree-of-life'), ('qa', 'dahl-al-misfir')]
    show = [dict(cc=cc, id=i, c=S[(cc, i)]['c'], te=S[(cc, i)]['te'], ta=S[(cc, i)]['ta'], n=S[(cc, i)]['n'], na=S[(cc, i)]['na']) for cc, i in SHOW]
    M = H.M; W, Hh = M['w'], M['h']; VY0 = -70; VH = Hh + 70
    shapes = ''.join(f'<path class="cs" data-cc="{cc}" d="{M["paths"][cc]}"/>' for cc in ORDER)
    badges = ''; leaders = ''; cards = ''
    for cc in ORDER:
        c = H.C[cc]; x, y = H.P(*c['pt']); bx, by = H.P(*c['bd'])
        if (bx, by) != (x, y): leaders += f'<line class="ld" x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/><circle class="ldp" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
        badges += f'<a class="bd" href="#{cc}" data-cc="{cc}" style="left:{bx/W*100:.2f}%;top:{(by-VY0)/VH*100:.2f}%"><span class="bdl">{H.flag_logo(cc, "bd"+cc)}</span><span class="bdn" data-n="{cc}"></span><span class="bdc">{data[cc]["n"]}</span></a>'
        cards += f'<a class="card" href="#{cc}" data-cc="{cc}"><span class="cl">{H.flag_logo(cc, "cd"+cc)}</span><span class="ct"><b data-t="{cc}"></b><small><span data-s="{cc}"></span></small></span><span class="go" aria-hidden="true">›</span></a>'
    wl = ''.join(f'<text class="wl" id="wl{i+1}" x="{H.P(*g)[0]:.0f}" y="{H.P(*g)[1]:.0f}">{t}</text>' for i, (g, t) in enumerate([((50.9, 28.9), 'Arabian Gulf'), ((36.8, 21.0), 'Red Sea'), ((56.8, 16.9), 'Arabian Sea')]))
    b64 = lambda f: base64.b64encode(open(f'{SITE}/{f}', 'rb').read()).decode()
    man = {'name': 'Layers · طبقات', 'short_name': 'Layers', 'start_url': BASE, 'scope': BASE, 'display': 'standalone', 'background_color': '#f7f8f5', 'theme_color': '#f7f8f5',
           'icons': [{'src': 'data:image/png;base64,' + b64('icon-192.png'), 'sizes': '192x192', 'type': 'image/png'}, {'src': 'data:image/png;base64,' + b64('icon-512.png'), 'sizes': '512x512', 'type': 'image/png'}]}
    manifest = 'data:application/manifest+json;base64,' + base64.b64encode(json.dumps(man, ensure_ascii=False).encode()).decode()
    html = open('/tmp/w/layers/hub_tpl.html', encoding='utf-8').read()
    for k, v in {'__SHAPES__': shapes, '__LEADERS__': leaders, '__BADGES__': badges, '__CARDS__': cards, '__WL__': wl, '__W__': f'{W:.0f}', '__H__': f'{VH:.0f}', '__VY0__': f'{VY0:.0f}',
                 '__LOGO__': H.plain_logo('hub'), '__DATA__': json.dumps({cc: dict(n=data[cc]['n'], **data[cc]['k']) for cc in ORDER}), '__IDX__': json.dumps(IDX), '__SHOW__': json.dumps(show, ensure_ascii=False),
                 '__C__': json.dumps({k: {x: v[x] for x in ('en', 'ar', 'ten', 'tar')} for k, v in H.C.items()}, ensure_ascii=False), '__BASE__': BASE, '__TOTAL__': str(total), '__MANIFEST__': manifest}.items():
        html = html.replace(k, v)
    leftover = re.findall(r'__[A-Z]+__', html)
    assert not leftover, leftover
    payload = ''.join(f'<script type="text/plain" id="ed-{cc}">{patch_edition(cc)}</script>\n' for cc in ORDER)
    html = html.replace('<!--PAYLOAD-->', payload)
    open(f'{OUT}/index.html', 'w', encoding='utf-8').write(html)
    return total, os.path.getsize(f'{OUT}/index.html')

if __name__ == '__main__':
    print(build())
