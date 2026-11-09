import json,re
d=json.load(open('data.json'));kw=open('kw_rings.json').read()
js=json.dumps(d,ensure_ascii=False).replace('<','\\u003c')
h=open('tpl.html').read().replace('__DATA__',js).replace('__KW__',kw)
open('/mnt/user-data/outputs/kuwait-geoheritage-explorer.html','w').write(h)
open('chk.js','w').write(re.search(r'<script>(.*)</script>',h,re.S).group(1))
print(len(h))
