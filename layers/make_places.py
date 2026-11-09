"""Readable directory of every place (places.html), structured data and sitemap.xml for the website folder.

Search engines and AI tools that scan the site can't run the map app, so this page lists every place
in plain HTML, in English and Arabic, with schema.org TouristAttraction data. Run after make_site.py.
"""
import json, os, re, sys, html, datetime

OUT = '/tmp/w/layers/website'
SITE = (sys.argv[1] if len(sys.argv) > 1 else 'https://smbehbehani-max.github.io/Layers2/').rstrip('/') + '/'
ORDER = ['kw', 'sa', 'bh', 'qa', 'ae', 'om']
CN = {'kw': ('Kuwait', 'الكويت'), 'sa': ('Saudi Arabia', 'السعودية'), 'bh': ('Bahrain', 'البحرين'),
      'qa': ('Qatar', 'قطر'), 'ae': ('United Arab Emirates', 'الإمارات'), 'om': ('Oman', 'عُمان')}
LAY = [('archaeological', 'Archaeological', 'أثرية', '#b5531f'), ('geological', 'Geological', 'جيولوجية', '#5a49b8'),
       ('ecology', 'Ecological', 'بيئية', '#2f7a4b')]
E = lambda s: html.escape(str(s or ''), quote=True)


def sites(cc):
    h = open(os.path.join(OUT, f'ed-{cc}.html'), encoding='utf-8').read()
    i = h.index('const D=') + len('const D=')
    d, _ = json.JSONDecoder().raw_decode(h, i)
    return [s for s in d['sites'] if s.get('c') in ('archaeological', 'geological', 'ecology')]


def main():
    data = {cc: sites(cc) for cc in ORDER}
    total = sum(len(v) for v in data.values())
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "LAYERS by GEOHERITAGE: places",
          "numberOfItems": total, "itemListElement": []}
    body = []
    pos = 0
    for cc in ORDER:
        en, ar = CN[cc]
        body.append(f'<section id="{cc}"><h2>{E(en)} <span lang="ar" dir="rtl">{E(ar)}</span> <small>{len(data[cc])} places</small></h2>')
        for key, len_, lar, col in LAY:
            S = sorted([s for s in data[cc] if s['c'] == key], key=lambda s: s['n'])
            if not S: continue
            body.append(f'<h3 style="--c:{col}">{len_} <span lang="ar" dir="rtl">{lar}</span> <small>{len(S)}</small></h3><ul>')
            for s in S:
                pos += 1
                lat, lng = float(s['lat']), float(s['lng'])
                url = f'{SITE}#{cc}/p={s["id"]}'
                summ = s.get('se') or ''
                body.append(
                    f'<li><a class="n" href="./#{cc}/p={E(s["id"])}">{E(s["n"])}</a>'
                    + (f' <span class="ar" lang="ar" dir="rtl">{E(s.get("na"))}</span>' if s.get('na') else '')
                    + f'<div class="s">{E(s.get("s"))}</div>'
                    + (f'<p>{E(summ)}</p>' if summ else '')
                    + (f'<p lang="ar" dir="rtl">{E(s.get("sa"))}</p>' if s.get('sa') else '')
                    + f'<div class="m">{lat:.4f}° N, {lng:.4f}° E · <a href="https://www.google.com/maps/dir/?api=1&amp;destination={lat},{lng}" rel="noopener" target="_blank">Directions</a></div></li>')
                ld['itemListElement'].append({"@type": "ListItem", "position": pos, "item": {
                    "@type": "TouristAttraction", "name": s['n'], **({"alternateName": s['na']} if s.get('na') else {}),
                    "description": summ or s.get('s', ''), "url": url,
                    "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
                    "address": {"@type": "PostalAddress", "addressCountry": en},
                    "touristType": ["Cultural tourism", "Nature tourism", "Educational"]}})
            body.append('</ul>')
        body.append('</section>')
    nav = ' · '.join(f'<a href="#{cc}">{CN[cc][0]}</a>' for cc in ORDER)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>All places · LAYERS by GEOHERITAGE</title>
<meta name="description" content="Directory of {total} archaeological, geological and ecological places in the six Arab Gulf countries, in English and Arabic, with coordinates and directions.">
<link rel="canonical" href="{SITE}places.html"><link rel="icon" href="icon-192.png">
<meta property="og:title" content="All places · LAYERS by GEOHERITAGE"><meta property="og:image" content="{SITE}og-kw.png">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--bg:#f7f8f5;--ink:#1a2a2b;--mut:#5d6d6c;--line:#d5dcd6;--sea:#2c6e72;--gold:#c99a2e}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#121c1c;--ink:#e6ecea;--mut:#93a5a2;--line:#273534;--sea:#7cc6c9}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif}}
main{{max-width:960px;margin:0 auto;padding:24px 16px 64px}}a{{color:var(--sea)}}
header h1{{font:700 clamp(26px,5vw,38px)/1.15 Georgia,serif;margin:0 0 6px}}header p{{color:var(--mut);margin:0 0 14px}}
.cta{{display:inline-block;background:var(--sea);color:#fff;text-decoration:none;padding:9px 18px;border-radius:99px;font-weight:600}}
nav{{margin:18px 0 8px;line-height:2}}h2{{font:700 26px/1.2 Georgia,serif;margin:42px 0 6px;padding-top:10px;border-top:1px solid var(--line)}}
h2 span,h3 span{{font-family:Tahoma,sans-serif;font-weight:600;color:var(--mut)}}small{{color:var(--mut);font:500 14px system-ui}}
h3{{font-size:17px;margin:24px 0 8px;color:var(--c)}}ul{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}}
li{{border:1px solid var(--line);border-radius:12px;padding:12px 14px;min-width:0;overflow-wrap:anywhere}}
.n{{font-weight:700;text-decoration:none;color:var(--ink)}}.ar{{display:block;color:var(--mut);font-size:15px}}
.s{{color:var(--mut);font-size:13.5px;margin:4px 0}}li p{{margin:6px 0;font-size:14.5px}}.m{{font-size:12.5px;color:var(--mut)}}
footer{{margin-top:48px;color:var(--mut);font-size:13.5px}}
</style></head><body><main>
<header><h1>All places <span lang="ar" dir="rtl" style="font-family:Tahoma,sans-serif">كل المواقع</span></h1>
<p>{total} archaeological, geological and ecological places across the six Arab Gulf countries. Every place in the app carries its published sources. AI hypotheses are kept separate and are not listed here.</p>
<a class="cta" href="./">Open the map · افتح الخريطة</a></header>
<nav>{nav}</nav>
{''.join(body)}
<footer>LAYERS by GEOHERITAGE · Updated {datetime.date.today().isoformat()} · <a href="privacy.html">Privacy</a></footer>
</main></body></html>'''
    open(os.path.join(OUT, 'places.html'), 'w', encoding='utf-8').write(page)

    # structured data + crawler link on the app pages
    app_ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": "LAYERS by GEOHERITAGE",
              "alternateName": "طبقات", "url": SITE, "applicationCategory": "TravelApplication",
              "operatingSystem": "Any (web browser)", "inLanguage": ["en", "ar"], "isAccessibleForFree": True,
              "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
              "description": f"A bilingual (English/Arabic) map of {total} archaeological, geological and ecological places in the six Arab Gulf countries, with sources, illustrated stories, a timeline, offline use and directions.",
              "spatialCoverage": [{"@type": "Country", "name": CN[c][0]} for c in ORDER]}
    tag = (f'<script type="application/ld+json">{json.dumps(app_ld, ensure_ascii=False)}</script>'
           '<noscript><a href="places.html">All places in LAYERS (directory)</a></noscript>')
    for f in ('index.html', 'mobile.html'):
        p = os.path.join(OUT, f); h = open(p, encoding='utf-8').read()
        h = h.replace('</head>', tag + '</head>', 1)
        h = h.replace('https://smbehbehani-max.github.io/Layers2/', SITE)  # canonical and preview links
        open(p, 'w', encoding='utf-8').write(h)

    for c in ORDER:  # preview images need a full address
        p = os.path.join(OUT, f'{c}.html'); h = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(h.replace('content="og-', f'content="{SITE}og-'))

    urls = ['', 'places.html'] + [f'{c}.html' for c in ORDER] + ['privacy.html']
    today = datetime.date.today().isoformat()
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
    print('places', total, 'directory KB', os.path.getsize(os.path.join(OUT, 'places.html')) // 1000)


if __name__ == '__main__':
    main()
