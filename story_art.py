# Storybook illustrations: 480x270, watercolour look via shared filters (#wc wobble, #blot wash, #paper grain)
INK = '#5b4330'
SKIN, HAIR, JACKET, SHIRT, PANTS, SHOE = '#e2b48c', '#cfcac2', '#c39a5b', '#8fb3d1', '#a88b62', '#5b3a24'

DEFS = '''
<filter id="wc" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="blot" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="5" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G"/><feGaussianBlur stdDeviation="1.4"/></filter>
<filter id="paper" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="8"/><feColorMatrix values="0 0 0 0 0.36 0 0 0 0 0.27 0 0 0 0 0.18 0 0 0 0.9 0"/></filter>
<linearGradient id="gSun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f5d86"/><stop offset=".45" stop-color="#d98a4e"/><stop offset=".8" stop-color="#f6c77c"/><stop offset="1" stop-color="#fbe4b0"/></linearGradient>
<linearGradient id="gDay" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc9e3"/><stop offset="1" stop-color="#e9f1ee"/></linearGradient>
<linearGradient id="gSand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e7c487"/><stop offset="1" stop-color="#c9955a"/></linearGradient>
<linearGradient id="gSalt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3eee4"/><stop offset="1" stop-color="#e3d8c4"/></linearGradient>
<radialGradient id="gGlow"><stop offset="0" stop-color="#fff2c4" stop-opacity=".95"/><stop offset="1" stop-color="#fff2c4" stop-opacity="0"/></radialGradient>
<linearGradient id="gWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f0dcb8"/><stop offset="1" stop-color="#e0c094"/></linearGradient>
'''

def paper():
    return '<rect width="480" height="270" filter="url(#paper)" opacity=".16"/>'

def S(d, fill, sw=1.6, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'

def cone(x, y, s=1, wet=False):
    out = (S(f'M{x-15*s} {y} Q{x-7*s} {y-5*s} {x-4.5*s} {y-17*s} L{x+4.5*s} {y-17*s} Q{x+7*s} {y-5*s} {x+15*s} {y}Z', '#c08a52', 1.3) +
           f'<path d="M{x-2*s} {y-16*s} Q{x-4*s} {y-6*s} {x-11*s} {y-1*s}" fill="none" stroke="#e4b47a" stroke-width="{1.6*s}" opacity=".8"/>' +
           f'<ellipse cx="{x}" cy="{y-17*s}" rx="{4.5*s}" ry="{1.6*s}" fill="#5e3f26" stroke="{INK}" stroke-width="1"/>')
    if wet:
        out += f'<ellipse cx="{x+6*s}" cy="{y+1*s}" rx="{12*s}" ry="{2.6*s}" fill="#8fb3c4" opacity=".55"/>'
    return out

def cracks(y0, color=INK, op=.35):
    d = (f'M0 {y0+30} L60 {y0+24} L110 {y0+40} L170 {y0+28} L240 {y0+46} L300 {y0+30} L370 {y0+44} L480 {y0+32} '
         f'M30 {y0+90} L90 {y0+70} L150 {y0+96} L220 {y0+78} L290 {y0+104} L360 {y0+80} L440 {y0+100} '
         f'M110 {y0+40} L90 {y0+70} M240 {y0+46} L220 {y0+78} M370 {y0+44} L360 {y0+80} M150 {y0+96} L140 {y0+130} M290 {y0+104} L300 {y0+130}')
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.1" opacity="{op}"/>'

def head(back=False):
    if back:
        return (S('M-10 -101 a10 10 0 1 0 20 0 a10 10 0 1 0 -20 0', HAIR, 1.4))
    return (S('M-10 -101 a10 10 0 1 0 20 0 a10 10 0 1 0 -20 0', SKIN, 1.4) +
            S('M-10.5 -102 Q-11 -115 0 -115 Q11 -115 10.5 -102 Q8 -109 2 -108 Q-4 -111 -10.5 -102Z', HAIR, 1.2) +
            f'<g fill="none" stroke="{INK}" stroke-width="1.1"><circle cx="-4" cy="-101" r="2.8"/><circle cx="4.2" cy="-101" r="2.8"/><path d="M-1.2 -101 h2.6"/><path d="M-2.5 -95 q2.5 1.8 5 0"/></g>')

def torso(back=False):
    return (S('M-15 -88 Q0 -95 15 -88 L17 -48 L-17 -48Z', JACKET) +
            ('' if back else S('M-5 -90 L0 -70 L5 -90Z', SHIRT, 1.1)) +
            f'<path d="M0 -70 V-50" stroke="{INK}" stroke-width="1" opacity=".6"/>')

def legs_stand(step=0):
    return (S(f'M-10 -50 L{-12-step} -3 L{-4-step} -3 L-1 -46Z', PANTS) + S(f'M1 -46 L{4+step} -3 L{12+step} -3 L10 -50Z', PANTS) +
            S(f'M{-14-step} -4 h12 v4 h-14z', SHOE, 1.2) + S(f'M{2+step} -4 h12 v4 h-12z', SHOE, 1.2))

def arm(d, hand):
    hx, hy = hand
    return S(d, JACKET) + S(f'M{hx-3} {hy} a3 3 0 1 0 6 0 a3 3 0 1 0 -6 0', SKIN, 1.1)

def prof(x, y, s=1, pose='stand', flip=False, back=False, step=0):
    fx = -s if flip else s
    g = f'<g transform="translate({x} {y}) scale({fx} {s})" filter="url(#wc)">'
    if pose == 'kneel':
        legs = (S('M-8 -36 L22 -28 L22 -19 L-8 -25Z', PANTS) + S('M15 -26 L23 -26 L23 -3 L14 -3Z', PANTS) + S('M12 -4 h14 v4 h-14z', SHOE, 1.2) +
                S('M-10 -34 L2 -5 L-6 -2 L-17 -28Z', PANTS) + S('M-3 -8 L-32 -5 L-32 1 L-3 1Z', PANTS) + S('M-40 -5 h9 v6 h-9z', SHOE, 1.2))
        up = (f'<g transform="translate(-2 34) rotate(12)">' + torso() + head() +
              arm('M-15 -86 L-22 -56 L-16 -54 L-10 -82Z', (-19, -53)) + arm('M14 -86 L34 -54 L28 -50 L9 -80Z', (32, -49)) + '</g>')
        return g + legs + up + '</g>'
    out = legs_stand(step) + torso(back) + head(back)
    if pose == 'stand':
        out += arm('M-15 -86 L-20 -54 L-14 -53 L-11 -80Z', (-17, -52)) + arm('M15 -86 L20 -54 L14 -53 L11 -80Z', (17, -52))
    elif pose == 'think':
        out += arm('M-15 -86 L-16 -60 L10 -64 L10 -70 L-10 -68 L-10 -82Z', (11, -67)) + arm('M15 -86 L20 -66 L6 -92 L1 -90 L13 -70 L11 -82Z', (3, -92))
    elif pose == 'point':
        out += arm('M-15 -86 L-20 -54 L-14 -53 L-11 -80Z', (-17, -52)) + arm('M15 -86 L46 -82 L46 -75 L14 -77Z', (49, -78))
    elif pose == 'lecture':
        out += arm('M-15 -86 L-20 -60 L-6 -58 L-6 -64 L-12 -66 L-11 -80Z', (-5, -61)) + arm('M15 -86 L40 -98 L43 -92 L14 -77Z', (44, -97))
    elif pose == 'cheer':
        out += (arm('M-14 -86 L-25 -118 L-18 -121 L-9 -88Z', (-22, -122)) + arm('M14 -86 L25 -118 L18 -121 L9 -88Z', (22, -122)) +
                S('M17 -140 h10 v15 h-10z', '#e9d9b0', 1.2) + '<rect x="17" y="-133" width="10" height="8" fill="#c9955a" opacity=".85"/>')
    return g + out + '</g>'

def shadow(x, y, w=26, dx=0):
    return f'<ellipse cx="{x+dx}" cy="{y}" rx="{w}" ry="{w*0.18}" fill="#7a5532" opacity=".28"/>'

def clouds(pts, col='#f3c79a', op=.7):
    return ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx*0.28}" fill="{col}" opacity="{op}" filter="url(#blot)"/>' for x, y, rx in pts)

ART = {}

# Cover — sunset walk among cones
ART['cover'] = ('<rect width="480" height="270" fill="url(#gSun)"/>' +
    '<circle cx="240" cy="150" r="90" fill="url(#gGlow)"/>' +
    clouds([(90, 70, 70), (380, 60, 80), (300, 110, 60), (130, 120, 50)]) +
    '<rect y="148" width="480" height="122" fill="url(#gSand)" filter="url(#wc)"/>' + cracks(150) +
    ''.join(cone(x, y, s) for x, y, s in [(120, 172, .5), (180, 168, .45), (300, 170, .5), (360, 174, .55), (70, 190, .8), (420, 192, .8), (150, 214, 1.1), (330, 218, 1.2), (60, 250, 1.6), (420, 256, 1.7)]) +
    cone(190, 246, 1.5, True) +
    shadow(240, 236, 30, 6) + prof(240, 236, .95, 'stand', step=3) + paper())

# Chapter 1 — kneeling at the cones
ART['c1'] = ('<rect width="480" height="270" fill="url(#gDay)"/>' + clouds([(380, 30, 60), (120, 24, 50)], '#ffffff', .8) +
    '<rect y="52" width="480" height="218" fill="url(#gSand)" filter="url(#wc)"/>' + cracks(60) + cracks(140) +
    ''.join(cone(x, y, s) for x, y, s in [(300, 150, .8), (340, 160, .9), (380, 150, .8), (420, 168, 1), (450, 150, .7), (280, 190, 1.2), (330, 200, 1.3), (390, 196, 1.2), (440, 210, 1.3), (300, 240, 1.6), (370, 250, 1.7), (450, 252, 1.6), (250, 220, 1.2)]) +
    shadow(180, 248, 46, 8) + prof(180, 248, 1.25, 'kneel') +
    '<g filter="url(#wc)">' + S('M70 252 L102 244 L104 262 L72 268Z', '#f4ecd8', 1.3) + S('M104 244 L136 250 L134 268 L104 262Z', '#f4ecd8', 1.3) +
    f'<path d="M78 252 l18 -4 M78 257 l18 -4 M110 250 l18 4 M110 255 l18 4" stroke="{INK}" stroke-width=".9" opacity=".6"/>' + '</g>' + paper())

# Chapter 2 — imagining the cones alive
def puff(x, y, s=1):
    return f'<g class="rise" opacity=".85"><ellipse cx="{x}" cy="{y}" rx="{7*s}" ry="{5*s}" fill="#b9b3ab" filter="url(#blot)"/><ellipse cx="{x+3*s}" cy="{y-9*s}" rx="{6*s}" ry="{4.5*s}" fill="#cbc6be" filter="url(#blot)"/></g>'
ART['c2'] = ('<rect width="480" height="270" fill="url(#gDay)"/>' +
    '<rect y="150" width="480" height="120" fill="url(#gSalt)" filter="url(#wc)"/>' +
    f'<path d="M0 180 L80 172 L150 188 L240 176 L330 190 L480 178 M40 230 L120 212 L200 236 L290 216 L380 238 L480 222 M80 172 L120 212 M240 176 L200 236 M330 190 L380 238" fill="none" stroke="#b9a98d" stroke-width="1.4"/>' +
    '<g filter="url(#wc)">' + S('M170 30 Q170 6 230 8 Q280 -2 330 10 Q400 6 410 40 Q440 70 410 100 Q400 132 330 128 Q280 140 230 130 Q170 136 160 104 Q130 70 170 30Z', '#fbf6ec', 1.8) + '</g>' +
    '<clipPath id="bub2"><path d="M178 36 Q180 16 230 18 Q280 8 330 20 Q392 16 400 44 Q426 70 400 96 Q392 122 330 118 Q280 130 230 120 Q182 126 172 100 Q146 70 178 36Z"/></clipPath>' +
    '<g clip-path="url(#bub2)"><rect x="140" y="0" width="300" height="140" fill="#cfe4ec"/><rect x="140" y="80" width="300" height="60" fill="#ece3d2"/>' +
    cone(220, 100, 1.4) + cone(290, 96, 1.1) + cone(350, 104, 1.5) + cone(260, 116, 1.2, True) +
    puff(220, 70, 1) + puff(290, 72, .8) + puff(350, 70, 1.1) +
    '<g fill="#7a5532"><circle class="rise" cx="256" cy="92" r="2.4"/><circle class="rise d1s" cx="264" cy="88" r="1.8"/><circle class="rise d2s" cx="252" cy="86" r="1.6"/></g></g>' +
    '<g filter="url(#wc)" fill="#fbf6ec" stroke="' + INK + '" stroke-width="1.4"><circle cx="150" cy="150" r="9"/><circle cx="132" cy="170" r="6"/><circle cx="120" cy="186" r="4"/></g>' +
    shadow(96, 262, 34, 6) + prof(96, 262, 1.35, 'think') + paper())

# Chapter 3 — the lab and the isotope chart
def jar(x, y, h=26, col='#c9955a'):
    return (S(f'M{x-8} {y} v-{h} h16 v{h}z', '#efe6d2', 1.2) + f'<rect x="{x-7}" y="{y-h*0.55}" width="14" height="{h*0.55}" fill="{col}" opacity=".8"/>' + S(f'M{x-9} {y-h} h18 v-4 h-18z', '#8a6a4a', 1.1))
ART['c3'] = ('<rect width="480" height="270" fill="url(#gWall)"/>' +
    '<g filter="url(#wc)">' + S('M10 80 H150', 'none', 3) + S('M10 140 H150', 'none', 3) +
    jar(30, 80) + jar(56, 80, 22, '#8a6a4a') + jar(82, 80, 28, '#d9b07a') + jar(110, 80, 24) + jar(134, 80, 20, '#a07850') +
    jar(34, 140, 24, '#b9884e') + jar(62, 140, 28) + jar(92, 140, 22, '#8a6a4a') + jar(122, 140, 26, '#d9b07a') +
    S('M0 200 H480 V270 H0Z', '#9a7350') + S('M0 200 H480', 'none', 2) +
    S('M150 196 L160 100 H330 L340 196Z', '#3d3a36', 2) + S('M168 108 H322 V188 H168Z', '#fbf8f0', 1.2) + S('M236 196 h18 l6 8 h-30z', '#3d3a36', 1.4) +
    f'<path d="M182 176 H310 M182 176 V118" stroke="{INK}" stroke-width="1.2" fill="none"/>' + '</g>' +
    ''.join(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="2.3" fill="{c}"/>' for cx, cy, c in [(286, 128, '#3f7cc0'), (262, 148, '#2f9a8a'), (212, 164, '#d0603a')] for dx, dy in [(0, 0), (6, 3), (-5, 4), (3, -5), (-6, -3), (8, -2), (2, 7)]) +
    '<path d="M214 158 l1.8 3.8 4.2 .5 -3.1 2.9 .8 4.2 -3.7 -2 -3.7 2 .8 -4.2 -3.1 -2.9 4.2 -.5z" fill="#f2b84b" stroke="#5b4330" stroke-width=".9"/>' +
    '<g filter="url(#wc)">' + S('M380 40 l30 50 h-60z', '#d6a64a', 1.4) + S('M380 40 l-10 -40 h4 l8 36z', '#5b4330', 1) + '</g><ellipse cx="380" cy="96" rx="40" ry="10" fill="#fff2c4" opacity=".5"/>' +
    prof(410, 268, 1.45, 'point', flip=True) + paper())

# Chapter 4 — cut-away: quake pushes ancient water up
ART['c4'] = ('<rect width="480" height="270" fill="#f0e2c6"/>' +
    '<rect width="480" height="80" fill="url(#gSun)"/>' +
    '<g filter="url(#wc)">' + S('M0 80 H480 V112 H0Z', '#e7c487') + S('M0 112 Q60 104 120 116 Q180 128 240 112 Q300 98 360 114 Q420 126 480 110 V146 H0Z', '#c99a64') +
    S('M0 146 Q40 132 80 148 Q120 162 160 144 Q200 128 240 150 Q280 166 320 146 Q360 130 400 150 Q440 164 480 146 V182 H0Z', '#d8b98c') +
    S('M0 182 H480 V270 H0Z', '#a98466') +
    S('M120 270 Q140 222 220 220 Q320 216 360 270Z', '#5f94b4') + '</g>' +
    '<ellipse cx="240" cy="246" rx="110" ry="22" fill="#9fd0e6" opacity=".45" filter="url(#blot)"/>' +
    f'<path d="M210 222 L218 190 L204 160 L214 130 L206 100 M290 222 L282 186 L296 150 L286 118 L292 98" fill="none" stroke="{INK}" stroke-width="2.4" stroke-dasharray="1 0"/>' +
    ''.join(f'<path class="rise{d}" d="M{x} {y} v-14 h-5 l8 -10 l8 10 h-5 v14z" fill="#5f94b4" stroke="{INK}" stroke-width="1"/>' for x, y, d in [(204, 206, ''), (204, 160, ' d1s'), (284, 200, ' d2s'), (284, 150, '')]) +
    cone(206, 98, 1.3) + cone(292, 98, 1.2) + cone(380, 96, .9) + cone(120, 96, .8) +
    f'<path class="shake" d="M20 210 l8 -10 l8 16 l8 -16 l8 10 M420 210 l8 -10 l8 16 l8 -16 l8 10" fill="none" stroke="#c0392b" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>' +
    prof(60, 98, .55, 'cheer') + paper())

# Chapter 5 — the lecture
def headgear(x, y, kind):
    if kind == 'gh':
        return (S(f'M{x-15} {y+14} Q{x-14} {y-16} {x} {y-17} Q{x+14} {y-16} {x+15} {y+14}Z', '#f7f4ee', 1.3) + S(f'M{x-11} {y-9} Q{x} {y-14} {x+11} {y-9}', 'none', 2.4))
    if kind == 'sh':
        return (S(f'M{x-15} {y+14} Q{x-14} {y-16} {x} {y-17} Q{x+14} {y-16} {x+15} {y+14}Z', '#cf5b4b', 1.3) +
                f'<path d="M{x-10} {y-8} l20 14 M{x+10} {y-8} l-20 14 M{x-12} {y} l24 0" stroke="#f7e9e4" stroke-width="1.2" opacity=".8"/>' + S(f'M{x-11} {y-9} Q{x} {y-14} {x+11} {y-9}', 'none', 2.4))
    if kind == 'hj':
        return S(f'M{x-14} {y+16} Q{x-15} {y-15} {x} {y-16} Q{x+15} {y-15} {x+14} {y+16}Z', '#8a6f9e', 1.3)
    return S(f'M{x-11} {y-2} Q{x-12} {y-14} {x} {y-14} Q{x+12} {y-14} {x+11} {y-2} Q{x+6} {y-8} {x} {y-8} Q{x-6} {y-8} {x-11} {y-2}Z', '#4a3a2c', 1.2)
ART['c5'] = ('<rect width="480" height="270" fill="url(#gWall)"/>' +
    '<g filter="url(#wc)">' + S('M80 20 H330 V150 H80Z', '#5b4330', 2) + S('M88 28 H322 V142 H88Z', '#f2d9a8', 1.2) + '</g>' +
    '<clipPath id="scr5"><rect x="88" y="28" width="234" height="114"/></clipPath><g clip-path="url(#scr5)"><rect x="88" y="28" width="234" height="50" fill="#f7d8a0"/>' +
    ''.join(cone(x, y, s) for x, y, s in [(120, 98, 1.2), (170, 104, 1.5), (230, 100, 1.3), (290, 106, 1.6), (150, 130, 2), (250, 134, 2.1)]) + '</g>' +
    prof(392, 214, 1.15, 'lecture', flip=True) +
    '<g filter="url(#wc)">' + S('M350 170 h72 l-6 60 h-60z', '#8a6040', 1.6) + S('M346 164 h80 v8 h-80z', '#9d7150', 1.4) + S('M372 164 l-8 -18', 'none', 2) + '</g>' +
    S('M0 222 H480 V270 H0Z', '#8a6a4a', 0) +
    ''.join((S(f'M{x-20} 270 Q{x-20} 240 {x} 238 Q{x+20} 240 {x+20} 270Z', c, 1.3) + S(f'M{x-10} {y} a10 10 0 1 0 20 0 a10 10 0 1 0 -20 0', SKIN, 1.2) + headgear(x, y, k))
            if False else '' for x, y, k, c in []) + ''.join((S(f'M{x-20} 270 Q{x-20} 240 {x} 238 Q{x+20} 240 {x+20} 270Z', c, 1.3) + (headgear(x, y, k) + S(f'M{x-8} {y+1} a8 9 0 1 0 16 0 a8 9 0 1 0 -16 0', SKIN, 1.2) if k != 'hr' else S(f'M{x-10} {y} a10 10 0 1 0 20 0 a10 10 0 1 0 -20 0', SKIN, 1.2) + headgear(x, y, k)))
            for x, y, k, c in [(30, 232, 'gh', '#f2efe8'), (82, 236, 'hr', '#6d7f8f'), (134, 230, 'sh', '#f2efe8'), (186, 236, 'hj', '#4f4a6a'), (238, 232, 'gh', '#f2efe8'), (290, 236, 'hr', '#7a5a46'), (342, 232, 'sh', '#f2efe8'), (450, 234, 'gh', '#f2efe8')]) + paper())

# The end — walking away into the sunset
ART['end'] = ('<rect width="480" height="270" fill="url(#gSun)"/>' + '<circle cx="300" cy="150" r="100" fill="url(#gGlow)"/>' +
    clouds([(80, 60, 80), (380, 70, 70), (240, 40, 60)]) +
    '<rect y="150" width="480" height="120" fill="url(#gSand)" filter="url(#wc)"/>' + cracks(152) +
    '<path d="M150 236 L60 268 L90 270 L170 238Z" fill="#7a5532" opacity=".25"/>' +
    ''.join(cone(x, y, s) for x, y, s in [(260, 172, .6), (330, 176, .7), (390, 170, .5), (40, 254, 2.2), (440, 258, 2.4), (300, 214, 1.3)]) +
    prof(160, 238, .95, 'stand', back=True, step=2) + paper())

def wrap(body):
    return f'<svg viewBox="0 0 480 270" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{body}</svg>'
ART = {k: wrap(v) for k, v in ART.items()}
