import math, sys
FLAGS={
 'kw':{'name':'Kuwait','ar':'الكويت','svg':lambda r:f'<rect x="-{r}" y="-{r}" width="{2*r}" height="{2*r*2/3}" fill="#007a3d"/><rect x="-{r}" y="{-r+2*r/3}" width="{2*r}" height="{2*r/3}" fill="#fff"/><rect x="-{r}" y="{-r+4*r/3}" width="{2*r}" height="{2*r/3}" fill="#ce1126"/><path d="M-{r} -{r} L{-r+r*0.62} {-r+2*r/3} L{-r+r*0.62} {-r+4*r/3} L-{r} {r}Z" fill="#000"/>'},
 'ae':{'name':'UAE','ar':'الإمارات','svg':lambda r:f'<rect x="-{r}" y="-{r}" width="{2*r}" height="{2*r}" fill="#fff"/><rect x="-{r}" y="-{r}" width="{2*r}" height="{2*r/3}" fill="#00732f"/><rect x="-{r}" y="{r/3}" width="{2*r}" height="{2*r/3}" fill="#000"/><rect x="-{r}" y="-{r}" width="{r*0.62}" height="{2*r}" fill="#ff0000"/>'},
 'bh':{'name':'Bahrain','ar':'البحرين','svg':lambda r:'<rect x="-%s" y="-%s" width="%s" height="%s" fill="#ce1126"/>'%(r,r,2*r,2*r)+'<path d="M-%s -%s H%s '%(r,r,-r*0.45)+' '.join(f'L{-r*0.05:.1f} {-r+2*r*(i+.5)/5:.1f} L{-r*0.45:.1f} {-r+2*r*(i+1)/5:.1f}' for i in range(5))+f' H-{r}Z" fill="#fff"/>'},
 'qa':{'name':'Qatar','ar':'قطر','svg':lambda r:'<rect x="-%s" y="-%s" width="%s" height="%s" fill="#8a1538"/>'%(r,r,2*r,2*r)+'<path d="M-%s -%s H%s '%(r,r,-r*0.35)+' '.join(f'L{r*0.0:.1f} {-r+2*r*(i+.5)/9:.1f} L{-r*0.35:.1f} {-r+2*r*(i+1)/9:.1f}' for i in range(9))+f' H-{r}Z" fill="#fff"/>'},
}

FLAGS['sa']={'name':'Saudi Arabia','ar':'السعودية','svg':lambda r:(f'<rect x="-{r}" y="-{r}" width="{2*r}" height="{2*r}" fill="#006c35"/>'
  f'<text x="0" y="{-r*0.03:.1f}" text-anchor="middle" font-family="Amiri,\'Noto Naskh Arabic\',\'DejaVu Sans\',serif" font-weight="700" font-size="{r*0.22:.1f}" textLength="{r*1.6:.1f}" lengthAdjust="spacingAndGlyphs" fill="#fff" direction="rtl">لا إله إلا الله محمد رسول الله</text>'
  # sabre: tip toward the hoist (left), hilt toward the fly (right)
  f'<path d="M{-r*0.66:.1f} {r*0.3:.1f} Q{-r*0.45:.1f} {r*0.335:.1f} {r*0.4:.1f} {r*0.31:.1f} L{r*0.4:.1f} {r*0.37:.1f} Q{-r*0.4:.1f} {r*0.39:.1f} {-r*0.66:.1f} {r*0.3:.1f}Z" fill="#fff"/>'
  f'<rect x="{r*0.4:.1f}" y="{r*0.22:.1f}" width="{r*0.05:.1f}" height="{r*0.24:.1f}" rx="{r*0.02:.1f}" fill="#fff"/>'
  f'<path d="M{r*0.45:.1f} {r*0.31:.1f} L{r*0.6:.1f} {r*0.3:.1f} Q{r*0.66:.1f} {r*0.29:.1f} {r*0.67:.1f} {r*0.24:.1f} L{r*0.7:.1f} {r*0.25:.1f} Q{r*0.69:.1f} {r*0.36:.1f} {r*0.6:.1f} {r*0.37:.1f} L{r*0.45:.1f} {r*0.37:.1f}Z" fill="#fff"/>')}
def _om(r):
    hx=-r+r*0.62
    s=(f'<rect x="-{r}" y="-{r}" width="{2*r}" height="{2*r}" fill="#db161b"/><rect x="{hx:.1f}" y="-{r}" width="{2*r}" height="{2*r/3:.1f}" fill="#fff"/>'
       f'<rect x="{hx:.1f}" y="{r/3:.1f}" width="{2*r}" height="{2*r/3:.1f}" fill="#008000"/>')
    cx,cy,k=-r*0.66,-r*0.5,r*0.2   # simplified national emblem: crossed swords and khanjar
    s+=(f'<g fill="none" stroke="#fff" stroke-width="{k*0.16:.1f}" stroke-linecap="round"><path d="M{cx-k:.1f} {cy-k:.1f} L{cx+k:.1f} {cy+k:.1f} M{cx+k:.1f} {cy-k:.1f} L{cx-k:.1f} {cy+k:.1f}"/>'
        f'<path d="M{cx:.1f} {cy-k*1.05:.1f} L{cx:.1f} {cy+k*0.3:.1f} Q{cx:.1f} {cy+k*0.95:.1f} {cx+k*0.55:.1f} {cy+k*0.85:.1f}"/></g>'
        f'<rect x="{cx-k*0.45:.1f}" y="{cy-k*0.12:.1f}" width="{k*0.9:.1f}" height="{k*0.22:.1f}" fill="#fff"/>')
    return s
FLAGS['om']={'name':'Oman','ar':'عُمان','svg':_om}
def camel():
    body=("M-160 -190 C-168 -222 -146 -250 -116 -262 C-86 -310 -44 -338 2 -338 C46 -338 70 -306 90 -276 "
          "C100 -262 112 -264 120 -280 C130 -318 146 -352 172 -366 C190 -376 210 -374 226 -366 "
          "C238 -360 250 -352 262 -350 C276 -348 280 -334 270 -328 C258 -321 242 -324 230 -322 "
          "C214 -318 204 -300 198 -280 C188 -244 178 -214 160 -196 C146 -182 128 -174 108 -170 "
          "C60 -160 -40 -158 -100 -162 C-130 -164 -150 -170 -160 -190Z")
    def leg(x,w,kx,ky,fx,top=-185):
        return (f'M{x-w/2} {top} L{x+w/2} {top} C{x+w/2-2} {top+30} {kx+9} {ky-22} {kx+8} {ky} '
                f'L{fx+5} -10 C{fx+7} -4 {fx+12} -1 {fx+12} 0 L{fx-11} 0 C{fx-10} -2 {fx-6} -5 {fx-5} -10 '
                f'L{kx-8} {ky} C{kx-9} {ky-22} {x-w/2-4} {top+32} {x-w/2} {top}Z')
    legs=[leg(-110,52,-128,-92,-142,-180),leg(-72,46,-60,-95,-46,-175),leg(104,40,112,-98,128,-174),leg(138,34,150,-96,170,-188)]
    s=f'<path d="{body}"/>'+''.join(f'<path d="{d}"/>' for d in legs)
    s+='<path d="M-158 -214 C-180 -200 -186 -170 -178 -140" fill="none" stroke-width="10" stroke-linecap="round"/>'
    # saddle blanket: an explorer's camel, striped like the strata
    s+=('<g stroke="none"><path d="M-62 -318 C-30 -334 30 -334 62 -316 L70 -232 C30 -220 -30 -220 -74 -236Z" fill="#b4521c"/>'
        '<path d="M-72 -252 C-30 -238 30 -238 70 -250 L70 -236 C30 -224 -30 -224 -74 -238Z" fill="#f3d9ae"/>'
        '<path d="M-70 -270 C-30 -256 30 -256 68 -268 L69 -258 C30 -246 -30 -246 -71 -260Z" fill="#2c6e72"/>'
        '<circle cx="0" cy="-342" r="11" fill="#c99a2e"/></g>')
    return s
def strata():
    bands=[('#f3d9ae',0),('#e2a36b',1),('#b4521c',2),('#f6e7cc',3),('#8a3b1e',4),('#2c6e72',5),('#d98c5f',6),('#5b2a17',7)]
    out='';W=1024
    for c,i in bands:
        y0=560+i*58; a=26+i*3; ph=i*0.7
        pts=[(x, y0 - 80*(x/W) + a*math.sin(x/W*2*math.pi*1.1+ph)) for x in range(-20,W+41,32)]
        d='M'+' L'.join(f'{x:.0f} {y:.1f}' for x,y in pts)+f' L{W+40} 1100 L-20 1100Z'
        out+=f'<path d="{d}" fill="{c}"/>'
    return out
def icon(flag='kw',badge=True,px='',big=False):
    F=FLAGS[flag]
    r=118; bx,by=1024-150,150
    if big: r=215; bx,by=1024-250,250
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbeedb"/><stop offset=".55" stop-color="#f3d2a8"/><stop offset="1" stop-color="#e7b07c"/></linearGradient>
<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe8b0"/><stop offset=".6" stop-color="#f7c86e" stop-opacity=".9"/><stop offset="1" stop-color="#f7c86e" stop-opacity="0"/></radialGradient>
<clipPath id="sq"><rect width="1024" height="1024" rx="228"/></clipPath><clipPath id="fc"><circle r="{r}"/></clipPath>
<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="9" flood-color="#5b2a17" flood-opacity=".35"/></filter></defs>
<g clip-path="url(#sq)"><rect width="1024" height="1024" fill="url(#sky)"/><circle cx="{250 if big else 330}" cy="{330 if big else 300}" r="200" fill="url(#sun)"/>
{strata()}
<g transform="{'translate(300 556) scale(.66)' if big else 'translate(395 544) scale(.86)'}" fill="#3a1d10" stroke="#3a1d10">{camel()}</g></g>
{f'<g transform="translate({bx} {by})" filter="url(#sh)"><circle r="{r+14}" fill="#fff"/><g clip-path="url(#fc)">{F["svg"](r)}</g><circle r="{r}" fill="none" stroke="rgba(0,0,0,.12)" stroke-width="3"/></g>' if badge else ''}
</svg>'''
def gulf_icon():
    order=['kw','sa','bh','qa','ae','om'];r=60;gap=(1024-2*120)/5
    flags=''.join(f'<g transform="translate({120+i*gap:.0f} 175)" filter="url(#sh)"><circle r="{r+11}" fill="#fff"/><g clip-path="url(#fc)">{FLAGS[f]["svg"](r)}</g><circle r="{r}" fill="none" stroke="rgba(0,0,0,.12)" stroke-width="2"/></g>' for i,f in enumerate(order))
    s=icon('kw',False)
    s=s.replace('<clipPath id="fc"><circle r="118"/></clipPath>',f'<clipPath id="fc"><circle r="{r}"/></clipPath>')
    s=s.replace('translate(395 544) scale(.86)','translate(430 556) scale(.78)').replace('<circle cx="330" cy="300"','<circle cx="300" cy="380"')
    return s.replace('</svg>',flags+'</svg>')
def inline(flag,big):
    s=icon(flag,True,big=big);pf=f'lg{flag}{"b" if big else "n"}'
    for i in ['sky','sun','sq','fc','sh']:
        s=s.replace(f'id="{i}"',f'id="{pf}-{i}"').replace(f'url(#{i})',f'url(#{pf}-{i})')
    return s.replace('xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"','viewBox="0 0 1024 1024" aria-hidden="true"')
if __name__=='__main__':
    for f in FLAGS: open(f'icon-{f}.svg','w').write(icon(f))
    open('icon-plain.svg','w').write(icon('kw',False))
    open('icon-gulf.svg','w').write(gulf_icon())
    import json; json.dump({f:inline(f,False).replace('<svg ','<svg class="v-on" ',1)+inline(f,True).replace('<svg ','<svg class="v-sm" ',1) for f in ['kw','sa','bh','qa','ae','om']},open('/tmp/w/logos_inline.json','w'),ensure_ascii=False)
