s=open('hub3.py').read()
a=s.index('def texts(total):'); b=s.index('def build(')
s=s[:a]+open('/tmp/w/layers/texts4.py').read()+'\n\n'+s[b:]
s=s.replace("hub3_tpl.html","hub4_tpl.html")
s=s.replace("    big_logo = H.plain_logo('big')","""    big_logo = H.plain_logo('big')
    LP = json.load(open('/tmp/w/layers/logo_parts.json'))
    pills = ''.join(f'<a class="pill" href="#{cc}" data-cc="{cc}"><span class="l">{H.flag_logo(cc, "pl"+cc)}</span><span data-i="c.{cc}">{EN["c."+cc]}</span></a>' for cc in ORDER)""")
s=s.replace("'__MODE__': mode,","'__MODE__': mode, '__PILLS__': pills, '__BANDS__': ''.join(LP['bands']), '__CAMEL__': LP['camel'],")
s=s.replace("    for cc in ORDER:\n        d = data[cc]; k = d['k']","    for cc in []:\n        d = data[cc]; k = d['k']")
s=s.replace("        EN[f'sh{i}h'] = s['te']","        continue\n        EN[f'sh{i}h'] = s['te']")
s=s.replace('<span class="bdn" data-i="c.{cc}">{c["en"]}</span>','<span class="bdn" data-i="c.{cc}">{EN["c."+cc]}</span>')
i=s.index("        cards += f'"); j=s.index('\n',i)
s=s[:i]+"        pass"+s[j:]
open('hub4.py','w').write(s)
