import sys
sys.path.insert(0, '/tmp/w')
from story_art import S, INK, cone, cracks, clouds, shadow, paper, SKIN  # noqa

# ---------- generic watercolour figure ----------
def fig(x, y, s=1, pose='stand', flip=False, top='#c9a46a', robe=True, pants='#a88b62', skin=SKIN, head='hair',
        hair='#3b2a1e', headc='#f4efe6', back=False, step=0, hold=''):
    fx = -s if flip else s
    g = f'<g transform="translate({x} {y}) scale({fx} {s})" filter="url(#wc)">'
    if robe:
        body = S(f'M-14 -88 Q0 -95 14 -88 L{19+step} -4 L{-19-step} -4Z', top) + S('M-15 -4 h11 v4 h-12z M4 -4 h11 v4 h-12z', '#6b4a30', 1.1)
    else:
        body = (S(f'M-10 -50 L{-12-step} -3 L{-4-step} -3 L-1 -46Z', pants) + S(f'M1 -46 L{4+step} -3 L{12+step} -3 L10 -50Z', pants) +
                S(f'M{-14-step} -4 h12 v4 h-14z', '#5b3a24', 1.1) + S(f'M{2+step} -4 h12 v4 h-12z', '#5b3a24', 1.1) +
                S('M-15 -88 Q0 -95 15 -88 L16 -46 L-16 -46Z', top))
    hd = S('M-10 -101 a10 10 0 1 0 20 0 a10 10 0 1 0 -20 0', hair if back else skin, 1.3)
    if head == 'hair' and not back:
        hd += S('M-10.5 -102 Q-11 -115 0 -115 Q11 -115 10.5 -102 Q7 -109 0 -108 Q-7 -109 -10.5 -102Z', hair, 1.1)
    elif head == 'scarf':
        hd = S('M-13 -96 Q-14 -117 0 -117 Q14 -117 13 -96 L15 -84 L-15 -84Z', headc, 1.3) + ('' if back else S('M-8 -100 a8 9 0 1 0 16 0 a8 9 0 1 0 -16 0', skin, 1.2))
    elif head == 'ghutra':
        hd = S('M-14 -84 Q-15 -116 0 -117 Q15 -116 14 -84Z', headc, 1.3) + ('' if back else S('M-8 -100 a8 9 0 1 0 16 0 a8 9 0 1 0 -16 0', skin, 1.2)) + S('M-11 -110 Q0 -115 11 -110', 'none', 2.6)
    elif head == 'cap':
        hd += S('M-11 -103 Q-11 -114 0 -114 Q11 -114 11 -103Z', headc, 1.2) + S('M8 -105 h10 v3 h-10z', headc, 1.1)
    if not back and head in ('hair', 'cap'):
        hd += f'<g fill="none" stroke="{INK}" stroke-width="1.1"><circle cx="-3.5" cy="-101" r="1"/><circle cx="3.5" cy="-101" r="1"/><path d="M-2.5 -96 q2.5 1.8 5 0"/></g>'
    elif not back:
        hd += f'<g fill="none" stroke="{INK}" stroke-width="1.1"><circle cx="-3" cy="-100" r=".9"/><circle cx="3" cy="-100" r=".9"/><path d="M-2.2 -95.5 q2.2 1.6 4.4 0"/></g>'
    def arm(d, h):
        return S(d, top) + S(f'M{h[0]-3} {h[1]} a3 3 0 1 0 6 0 a3 3 0 1 0 -6 0', skin, 1.1)
    arms = {
        'stand': arm('M-14 -86 L-19 -54 L-13 -53 L-10 -80Z', (-16, -52)) + arm('M14 -86 L19 -54 L13 -53 L10 -80Z', (16, -52)),
        'reach': arm('M-14 -86 L-19 -54 L-13 -53 L-10 -80Z', (-16, -52)) + arm('M14 -86 L42 -70 L40 -64 L12 -76Z', (44, -67)),
        'up': arm('M-14 -86 L-22 -118 L-16 -120 L-9 -88Z', (-19, -121)) + arm('M14 -86 L22 -118 L16 -120 L9 -88Z', (19, -121)),
        'pull': arm('M-14 -86 L-6 -116 L0 -114 L-8 -84Z', (-3, -118)) + arm('M14 -86 L4 -110 L10 -112 L18 -84Z', (7, -114)),
        'hold': arm('M-14 -86 L-6 -62 L6 -64 L6 -70 L-4 -68 L-9 -82Z', (7, -67)) + arm('M14 -86 L12 -62 L4 -64 L6 -70 L9 -82Z', (3, -66)),
        'point': arm('M-14 -86 L-19 -54 L-13 -53 L-10 -80Z', (-16, -52)) + arm('M14 -86 L40 -104 L44 -98 L13 -77Z', (45, -103)),
    }
    out = body + hd + arms.get(pose, arms['stand']) + hold
    return g + out + '</g>'

def sit(x, y, s=1, **k):
    top = k.pop('top', '#c9a46a')
    up = fig(x, y + 30 * s, s, k.pop('pose', 'hold'), top=top, **k)
    up = up.replace('L19 -4 L-19 -4Z', 'L16 -58 L-16 -58Z').replace(S('M-15 -4 h11 v4 h-12z M4 -4 h11 v4 h-12z', '#6b4a30', 1.1), '')
    lap = f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M-26 0 Q-24 -30 0 -32 Q24 -30 26 0Z', top) + '</g>'
    return up + lap

def fire(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="0" cy="2" rx="40" ry="10" fill="#f6b04a" opacity=".35" filter="url(#blot)"/>'
            + S('M-14 2 l28 -6 M-14 -4 l28 6', 'none', 3) +
            '<path d="M0 -2 q-12 -14 -2 -30 q2 10 8 6 q8 12 -6 24z" fill="#e2602e" filter="url(#wc)"/><path d="M0 -3 q-6 -8 0 -16 q6 8 0 16z" fill="#f6c24a"/></g>')

def stars(pts):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff8dc"/>' for x, y, r in pts)

def wsea(y, col='#5f94b4'):
    return (f'<rect y="{y}" width="480" height="{270-y}" fill="{col}" filter="url(#wc)"/>' +
            ''.join(f'<path d="M{x} {yy} q8 -4 16 0 q8 4 16 0" fill="none" stroke="#e9f4f6" stroke-width="1.4" opacity=".7"/>' for x, yy in [(40, y+20), (200, y+30), (330, y+16), (120, y+50), (380, y+60)]))

def reedboat(x, y, s=1, masts=2, sails=True):
    out = (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' +
           S('M-60 -6 C-40 22 40 22 60 -6 C48 14 20 22 0 22 C-20 22 -48 14 -60 -6Z', '#c9a15f') +
           f'<path d="M-40 6 l-3 9 M-20 12 l-1 9 M0 13 v9 M20 12 l1 9 M40 6 l3 9" stroke="{INK}" stroke-width="1.2"/>')
    if masts:
        out += S('M-12 12 V-70', 'none', 2.6) + (S('M12 12 V-60', 'none', 2.6) if masts > 1 else '')
        if sails:
            out += S('M-10 -66 L22 -24 L-10 -18Z', '#f7f0dd', 1.4) + (S('M14 -56 L40 -22 L14 -18Z', '#f7f0dd', 1.4) if masts > 1 else '')
    return out + '</g>'

def camel(x, y, s=1, col='#c79a5e', flip=False):
    fx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({fx} {s})" filter="url(#wc)">' +
            S('M-16 0 v-22 M-8 0 v-22 M10 0 v-22 M17 0 v-22', 'none', 3.4) +
            S('M-24 -20 q-2 -14 8 -18 q5 -13 13 -3 q8 -13 15 0 q8 3 8 21z', col) +
            S('M16 -26 q10 -8 10 -22 q5 -5 12 -2 l2 5 l-7 2 q0 12 -10 19z', col) + '<circle cx="34" cy="-48" r="1.3" fill="#3b2c1e"/></g>')

def oryx(x, y, s=1, flip=False):
    fx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({fx} {s})" filter="url(#wc)">' +
            S('M-18 0 v-20 M-8 0 v-19 M10 0 v-19 M20 0 v-20', 'none', 3) +
            S('M-28 -22 q0 -12 26 -12 q26 0 28 12 q-2 8 -26 8 q-26 0 -28 -8z', '#f2ede2') +
            S('M22 -28 q10 -10 18 -6 q4 6 -2 12 q-8 4 -16 2z', '#f2ede2') + S('M34 -32 q6 2 6 8 q-4 2 -8 -2z', '#4a3a2c', 1) +
            S('M32 -34 L16 -64 M36 -34 L26 -64', 'none', 2.2) + S('M-20 -14 q14 -4 40 -2', 'none', 1) +
            S('M-28 -18 q-8 6 -4 14', 'none', 1.4) + '</g>')

def deino(x, y, s=1, col='#9c8a78', ghost=False):
    st = ' opacity=".45" stroke-dasharray="4 3"' if ghost else ''
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)"{st}>' +
            S('M-30 0 v-28 M-14 0 v-28 M14 0 v-28 M28 0 v-28', 'none', 8) +
            S('M-42 -22 q0 -38 42 -40 q40 0 46 32 q2 10 -6 12 h-76 q-6 0 -6 -4z', col) +
            S('M38 -44 q22 -6 24 16 q2 22 -6 36 l-6 -2 q4 -18 -2 -30z', col) +
            S('M44 -18 q4 16 -6 26 l-2 -4 q6 -8 2 -18z', '#f4efe2', 1.2) + S('M30 -52 q-12 4 -10 22 q8 -2 14 -10z', '#b5a493') +
            '<circle cx="46" cy="-40" r="2" fill="#3b2c1e"/></g>')

def palm(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M0 0 q-4 -40 6 -70', 'none', 5) +
            S('M6 -70 q-26 -10 -40 6 q20 -4 40 -6z M6 -70 q22 -16 42 -4 q-20 0 -42 4z M6 -70 q-10 -22 6 -32 q-2 16 -6 32z M6 -70 q18 -2 26 14 q-12 -6 -26 -14z', '#6f9a52', 1.3) + '</g>')

def owlfig(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M-14 0 q-4 -30 14 -34 q18 4 14 34z', '#c49464') +
            S('M-11 -30 l2 -10 l5 7 M11 -30 l-2 -10 l-5 7', '#c49464', 1.3) +
            S('M-11 -22 a5 5 0 1 0 10 0 a5 5 0 1 0 -10 0 M1 -22 a5 5 0 1 0 10 0 a5 5 0 1 0 -10 0', '#f4e6c8', 1.2) +
            '<circle cx="-6" cy="-22" r="2" fill="#3b2c1e"/><circle cx="6" cy="-22" r="2" fill="#3b2c1e"/>' + S('M-2 -16 l2 4 l2 -4z', '#d98a3a', 1) +
            f'<path d="M-7 -8 q7 4 14 0 M-6 -3 q6 3 12 0" stroke="{INK}" stroke-width="1" fill="none"/></g>')

def house(x, y, w=80, h=46):
    return (S(f'M{x} {y} v-{h} h{w} v{h}z', '#d8b98a') + S(f'M{x-4} {y-h} h{w+8} v-7 h-{w+8}z', '#c9a46a', 1.3) +
            f'<path d="M{x} {y-h*0.5} h{w} M{x+w*0.3} {y-h} v{h*0.5} M{x+w*0.7} {y-h*0.5} v{h*0.5}" stroke="{INK}" stroke-width=".9" opacity=".55"/>' +
            S(f'M{x+w*0.42} {y} v-20 a7 7 0 0 1 14 0 v20z', '#5b3a24', 1.2))

def tufts(pts, col='#7aa05a'):
    return ''.join(S(f'M{x} {y} q-5 -14 -9 -17 q6 3 9 11 q0 -12 4 -19 q2 10 0 19 q4 -9 9 -13 q-2 8 -4 19z', col, 1.1) for x, y in pts)

def sheep(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M-10 0 v-8 M8 0 v-8', 'none', 2.4) +
            S('M-16 -10 q-2 -12 10 -12 q4 -6 12 -2 q10 0 10 10 q0 6 -8 6 h-18 q-6 0 -6 -2z', '#f1ece2') + S('M14 -14 q8 -2 10 4 q-2 5 -8 4z', '#5b4a3a', 1.1) + '</g>')

def tooth(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M-16 0 q-2 -14 6 -20 q10 -4 20 0 q8 6 6 20 q-4 -6 -8 0 q-4 -6 -8 0 q-4 -6 -8 0 q-4 -6 -8 0z', '#efe4c8', 1.4) +
            f'<path d="M-8 -12 q8 -4 16 0" stroke="{INK}" stroke-width="1" fill="none"/></g>')

ART = {}
SUNSKY = '<rect width="480" height="270" fill="url(#gSun)"/>'
DAYSKY = '<rect width="480" height="270" fill="url(#gDay)"/>'
NIGHT = '<rect width="480" height="270" fill="#26324a"/>' + '<rect width="480" height="270" fill="url(#gSun)" opacity=".18"/>'

# ===== A. The First Sail (H3) =====
ART['a0'] = (SUNSKY + '<circle cx="380" cy="150" r="80" fill="url(#gGlow)"/>' + clouds([(110, 60, 70), (300, 40, 60)]) + wsea(150) +
    reedboat(230, 170, 1.15) + fig(214, 176, .42, 'up', top='#d9c49a', head='hair') + fig(246, 178, .5, 'stand', top='#b98d5c', head='hair') +
    S('M90 80 q5 -5 10 0 q5 -5 10 0 M120 96 q4 -4 8 0 q4 -4 8 0', 'none', 1.4) + paper())
ART['a1'] = (DAYSKY + wsea(160) + '<rect y="150" width="480" height="120" fill="url(#gSand)" filter="url(#wc)" clip-path="url(#shoreA)"/>' +
    '<clipPath id="shoreA"><path d="M0 150 H300 Q260 200 180 270 H0Z"/></clipPath>' +
    S('M30 196 l90 -4 l2 8 l-90 4z M36 206 l90 -4 l2 8 l-90 4z M28 186 l84 -4 l2 7 l-84 4z', '#d9c07a', 1.2) +
    reedboat(330, 186, .9, masts=0) + fire(150, 230, .9) + S('M134 216 q16 -12 32 0 q-2 14 -16 14 q-14 0 -16 -14z', '#3b2c1e') +
    fig(80, 250, .9, 'reach', top='#b98d5c') + fig(206, 252, .62, 'hold', top='#d9c49a', head='hair') + paper())
ART['a2'] = (DAYSKY + clouds([(380, 40, 60)], '#ffffff', .8) + wsea(140) +
    reedboat(240, 196, 1.3) + fig(210, 200, .62, 'pull', top='#b98d5c') + fig(282, 204, .45, 'up', top='#d9c49a') +
    S('M222 128 L188 76', 'none', 1.4) + paper())
ART['a3'] = (NIGHT + stars([(40, 30, 1.6), (90, 60, 1.2), (160, 24, 1.4), (300, 40, 1.8), (420, 26, 1.2), (380, 80, 1.4), (240, 70, 1)]) +
    '<rect y="190" width="480" height="80" fill="#8a6a4a" filter="url(#wc)"/>' + fire(130, 222, 1.1) +
    sit(210, 226, .9, top='#d9c49a', pose='hold') +
    '<circle cx="340" cy="150" r="64" fill="#c08a52" stroke="#5b4330" stroke-width="2" filter="url(#wc)"/>' +
    f'<g fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"><path d="M302 160 q40 24 80 0"/><path d="M328 166 V112 M354 166 V120"/><path d="M330 116 l22 32 h-22 M356 124 l18 28 h-18"/></g>' +
    '<circle cx="340" cy="150" r="54" fill="none" stroke="#7a5532" stroke-width="1.2" stroke-dasharray="2 4"/>' + paper())

# ===== B. The Owl of Bahra (Bahra 1) =====
ART['b0'] = (SUNSKY + '<circle cx="120" cy="150" r="80" fill="url(#gGlow)"/>' + '<rect y="150" width="480" height="120" fill="url(#gSand)" filter="url(#wc)"/>' +
    '<g filter="url(#wc)">' + house(40, 160, 90, 40) + house(150, 158, 70, 34) + '</g>' +
    '<g filter="url(#wc)">' + S('M270 250 q50 -16 110 0 v14 h-110z', '#a9805a') + '</g>' + owlfig(325, 246, 2.6) + paper())
ART['b1'] = (DAYSKY + '<rect y="120" width="480" height="150" fill="#e2c391" filter="url(#wc)"/>' +
    '<g filter="url(#wc)">' + house(10, 140, 120, 60) + house(360, 140, 110, 56) + '</g>' +
    sit(190, 240, 1, top='#b98d5c') + sit(290, 244, .8, top='#d9c49a') +
    ''.join(S(f'M{x} {y} c-7 -1 -8 -9 0 -10 c6 -1 8 5 3 7', '#fbf3e3', 1.1) for x, y in [(230, 250), (244, 254), (236, 262), (252, 262), (220, 262)]) +
    '<path d="M330 236 q20 14 40 0" fill="none" stroke="#5b4330" stroke-width="1"/>' +
    ''.join(f'<circle cx="{332+i*5}" cy="{238+abs(4-i)*-1.2+5}" r="2.2" fill="{c}"/>' for i, c in enumerate(['#d0603a', '#f2b84b', '#3f7cc0', '#fbf3e3', '#d0603a', '#f2b84b', '#3f7cc0', '#fbf3e3'])) + paper())
ART['b2'] = (NIGHT + stars([(60, 30, 1.4), (200, 20, 1.2), (330, 40, 1.6), (430, 70, 1.2), (130, 70, 1)]) +
    '<rect y="180" width="480" height="90" fill="#7a5a3e" filter="url(#wc)"/>' +
    ''.join('<g filter="url(#wc)">' + S(f'M{x-34} 196 a34 30 0 0 1 68 0z', '#a96c43') + S(f'M{x-12} 196 a12 12 0 0 1 24 0z', '#3b2418', 1.2) + '</g>' +
            f'<ellipse cx="{x}" cy="190" rx="30" ry="14" fill="#f6b04a" opacity=".45" filter="url(#blot)"/><path d="M{x} 194 q-6 -8 0 -14 q6 6 0 14z" fill="#f6c24a"/>' for x in (80, 190, 400)) +
    sit(300, 236, 1, top='#d9c49a') + owlfig(330, 222, .9) + paper())
ART['b3'] = (DAYSKY + '<rect y="140" width="480" height="130" fill="url(#gSand)" filter="url(#wc)"/>' +
    '<g filter="url(#wc)">' + house(330, 160, 130, 54) + '</g>' +
    fig(70, 240, .9, 'stand', top='#8a6f9e', head='ghutra', headc='#efe6d6', step=3) + camel(130, 236, .9, flip=True) +
    S('M110 196 h22 v14 h-22z M136 194 h18 v16 h-18z', '#b08a5a', 1.2) +
    fig(250, 246, .7, 'reach', top='#d9c49a') + owlfig(282, 214, .5) +
    fig(318, 250, .95, 'stand', top='#7a5a8a', head='scarf', headc='#d9cbb5', flip=True) + paper())

# ===== C. When Elephants Walked Here (Huwaimiliyah) =====
ART['c0'] = (DAYSKY + '<rect y="150" width="480" height="120" fill="#8db465" filter="url(#wc)"/>' +
    '<path d="M0 230 Q120 210 240 236 T480 228 V246 Q360 252 240 250 T0 248Z" fill="#7fb6c9" filter="url(#wc)"/>' +
    ''.join('<g filter="url(#wc)">' + S(f'M{x} {y} v-30', 'none', 4) + S(f'M{x-26} {y-30} q-4 -16 14 -20 q6 -14 22 -8 q18 -2 18 16 q8 8 -2 14 q-26 6 -52 -2z', '#6f9a52') + '</g>' for x, y in [(70, 160), (420, 156)]) +
    deino(240, 214, 1.15) + deino(360, 196, .6) + paper())
ART['c1'] = (DAYSKY + '<rect y="120" width="480" height="150" fill="url(#gSand)" filter="url(#wc)"/>' + cracks(130, op=.25) +
    tooth(250, 232, 1.4) + fig(200, 250, .85, 'reach', top='#e3a64a', robe=False, pants='#6d7f8f', head='cap', headc='#3f7cc0', hair='#3b2a1e') +
    fig(320, 250, 1.05, 'point', top='#8fa3b8', robe=False, pants='#a88b62', flip=True) +
    '<g filter="url(#wc)">' + S('M236 252 l-6 -12 l6 -2 l6 12z', '#c9a15f', 1) + '</g>' + paper())
ART['c2'] = ('<rect width="480" height="270" fill="#bfe0d6"/>' + '<rect y="140" width="480" height="130" fill="#8db465" filter="url(#wc)"/>' +
    '<path d="M0 200 Q120 180 240 206 T480 198 V230 Q360 236 240 234 T0 232Z" fill="#7fb6c9" filter="url(#wc)"/>' +
    deino(180, 214, 1.1) + deino(340, 210, .9) +
    ''.join('<g filter="url(#wc)">' + S(f'M{x} {y} v-34', 'none', 4) + S(f'M{x-28} {y-34} q-4 -16 14 -20 q6 -14 22 -8 q18 -2 18 16 q8 8 -2 14 q-26 6 -52 -2z', '#6f9a52') + '</g>' for x, y in [(40, 150), (450, 146), (260, 140)]) +
    '<g opacity=".5">' + fig(60, 262, .7, 'stand', top='#e3a64a', robe=False, pants='#6d7f8f', head='cap', headc='#3f7cc0') + '</g>' +
    S('M300 60 q5 -5 10 0 q5 -5 10 0 M330 74 q4 -4 8 0 q4 -4 8 0', 'none', 1.3) + paper())
ART['c3'] = (SUNSKY + '<circle cx="240" cy="150" r="80" fill="url(#gGlow)"/>' + clouds([(110, 60, 70), (360, 50, 70)]) +
    deino(250, 120, .9, '#f3c79a', ghost=True) +
    '<rect y="160" width="480" height="110" fill="url(#gSand)" filter="url(#wc)"/>' +
    fig(240, 250, 1, 'up', top='#e3a64a', robe=False, pants='#6d7f8f', head='cap', headc='#3f7cc0', hold='') + tooth(259, 132, .55).replace('translate(259 132)', 'translate(259 132)') + paper())

# ===== D. The Caravan of Kadhima =====
ART['d0'] = (SUNSKY + '<circle cx="380" cy="150" r="90" fill="url(#gGlow)"/>' + clouds([(120, 60, 70)]) +
    '<path d="M0 170 Q120 140 240 166 T480 158 V270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>' + wsea(214, '#5f94b4').replace('<rect y="214"', '<rect y="214" opacity=".0"') +
    ''.join(camel(x, y, s) for x, y, s in [(110, 190, .8), (190, 184, .85), (270, 180, .9)]) +
    fig(330, 184, .62, 'stand', top='#efe6d6', head='ghutra', headc='#f7f4ee', step=3) + paper())
ART['d1'] = ('<rect width="480" height="270" fill="#f3d8a2"/>' + '<circle cx="390" cy="50" r="30" fill="#fff2c4"/>' +
    '<path d="M0 150 Q120 120 240 146 T480 140 V270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>' +
    S('M60 110 q10 -6 20 0 t20 0 M300 100 q10 -6 20 0 t20 0', 'none', 1.2) +
    fig(180, 236, 1, 'reach', top='#efe6d6', head='ghutra', headc='#f7f4ee', step=4) + camel(270, 234, 1.2) + paper())
ART['d2'] = (DAYSKY + wsea(150) + '<path d="M0 150 L300 150 Q340 190 300 270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>' +
    palm(60, 176, 1) + palm(110, 170, .8) + palm(250, 168, .7) +
    '<path d="M150 196 q30 -10 60 0 q-6 10 -30 10 q-24 0 -30 -10z" fill="#7fb6c9" filter="url(#wc)"/>' +
    '<g filter="url(#wc)">' + S('M120 236 h70 v12 h-70z M200 240 h60 v12 h-60z', '#a98466') + '</g>' +
    camel(150, 238, .9) + camel(230, 244, .85, flip=True) + fig(300, 246, .8, 'stand', top='#efe6d6', head='ghutra', headc='#f7f4ee', flip=True) + paper())
ART['d3'] = (NIGHT + stars([(40, 30, 1.6), (80, 50, 1.2), (120, 22, 1.4), (170, 60, 1), (220, 30, 1.8), (260, 50, 1.2), (320, 24, 1.4), (360, 60, 1.6), (420, 36, 1.2), (450, 70, 1)]) +
    '<path d="M220 30 L260 50 L320 24" fill="none" stroke="#fff8dc" stroke-width=".8" opacity=".6"/>' +
    '<rect y="190" width="480" height="80" fill="#8a6a4a" filter="url(#wc)"/>' + fire(240, 226, 1) +
    sit(160, 232, 1, top='#efe6d6', pose='point', head='ghutra', headc='#f7f4ee') + sit(320, 236, .8, top='#d9c49a', head='ghutra', headc='#f7f4ee') +
    ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#7fb6c9" stroke="{INK}" stroke-width="1"/>' for x, y in [(330, 262), (360, 258), (390, 256), (420, 252), (450, 250)]) +
    f'<path d="M330 262 Q390 250 450 250" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>' + paper())

# ===== F. Return of the Oryx (Sabah Al-Ahmad) =====
ART['f0'] = ('<rect width="480" height="270" fill="url(#gSun)" opacity=".75"/><rect width="480" height="270" fill="url(#gDay)" opacity=".35"/>' + '<circle cx="90" cy="150" r="70" fill="url(#gGlow)"/>' +
    '<path d="M0 160 Q140 140 280 158 T480 150 V270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>' +
    tufts([(40, 200), (90, 230), (160, 210), (320, 220), (400, 200), (440, 240), (230, 250), (360, 256)]) +
    oryx(200, 220, 1.3) + oryx(320, 200, .9, flip=True) + oryx(400, 230, 1) + paper())
ART['f1'] = ('<rect width="480" height="270" fill="#eadcc0"/>' + clouds([(240, 60, 160)], '#d8c3a0', .6) +
    '<rect y="140" width="480" height="130" fill="#d9b98a" filter="url(#wc)"/>' +
    S('M0 230 Q120 200 240 216 T480 196 M0 246 Q120 214 240 230 T480 210', 'none', 1.6) +
    sheep(110, 200, 1) + sheep(160, 206, .9) + sheep(330, 190, .8) + sheep(380, 196, .9) + paper())
ART['f2'] = (DAYSKY + '<rect y="140" width="480" height="130" fill="url(#gSand)" filter="url(#wc)"/>' +
    S('M0 196 H480', 'none', 1.4) + ''.join(S(f'M{x} 200 V170', 'none', 2.4) for x in range(20, 480, 60)) + S('M0 178 H480 M0 188 H480', 'none', .9) +
    tufts([(60, 240), (110, 252), (300, 236), (350, 250), (420, 238)]) +
    fig(220, 252, 1, 'reach', top='#6f8a5a', robe=False, pants='#5b6a4a', head='scarf', headc='#c9b28a') +
    '<g filter="url(#wc)">' + S('M262 252 q-2 -16 6 -22 q4 8 0 22z', '#7aa05a', 1.1) + '</g>' + paper())
ART['f3'] = (DAYSKY + '<rect y="150" width="480" height="120" fill="url(#gSand)" filter="url(#wc)"/>' + tufts([(40, 220), (420, 230), (300, 250), (120, 256)]) +
    '<g filter="url(#wc)">' + S('M60 236 v-46 h60 v46z', '#b08a5a') + S('M120 190 l30 -14 v46 l-30 14z', '#9a7650') + '</g>' +
    oryx(230, 230, 1.1) + oryx(320, 214, .9) +
    fig(420, 250, 1, 'hold', top='#6f8a5a', robe=False, pants='#5b6a4a', head='scarf', headc='#c9b28a', flip=True) +
    '<g filter="url(#wc)">' + S('M402 182 h14 v8 h-14z M418 182 h14 v8 h-14z', '#3b2c1e', 1) + '</g>' + paper())

def wrap(body):
    return f'<svg viewBox="0 0 480 270" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{body}</svg>'
ART = {k: wrap(v) for k, v in ART.items()}

# Duane story extra page: the GeoPark
ART['g6'] = wrap(DAYSKY + '<rect y="130" width="480" height="140" fill="url(#gSalt)" filter="url(#wc)"/>' +
    ''.join(cone(x, y, s) for x, y, s in [(250, 170, .8), (300, 176, 1), (360, 170, .8), (410, 186, 1.1), (280, 214, 1.4), (380, 230, 1.6), (460, 214, 1.2)]) +
    S('M0 196 H200', 'none', 1.2) + ''.join(S(f'M{x} 200 V176', 'none', 2.2) for x in range(10, 200, 40)) + S('M0 182 H200 M0 190 H200', 'none', .8) +
    '<g filter="url(#wc)">' + S('M120 250 V160', 'none', 4) + S('M70 120 h100 v44 h-100z', '#6f8a5a', 1.8) +
    f'<path d="M84 136 h72 M84 148 h50" stroke="#f4efe2" stroke-width="3" stroke-linecap="round"/>' + S('M90 128 l8 -6 l8 6', 'none', 1.6) + '</g>' +
    fig(186, 252, .85, 'point', top='#3f7cc0', robe=False, pants='#5b6a7a') + fig(214, 254, .6, 'up', top='#e3a64a', robe=False, pants='#6d7f8f', head='cap', headc='#d0603a') +
    fig(160, 252, .85, 'stand', top='#8a6f9e', head='scarf', headc='#d9cbb5') + paper())

