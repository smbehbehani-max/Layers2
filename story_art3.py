# Illustrations for the AI speculation stories (480x270, watercolour style shared with story_art*.py)
# Per story: <key>-1 the clue (mostly aerial views), <key>-2 the analog elsewhere, <key>-4 the test; <key>-0 cover = clue | analog.
import sys, random, math
sys.path.insert(0, '/tmp/w')
from story_art import S, INK, paper, clouds
import story_art2 as s2
fig, wsea, reedboat, camel, palm, tufts, house = s2.fig, s2.wsea, s2.reedboat, s2.camel, s2.palm, s2.tufts, s2.house
DAYSKY, SUNSKY, NIGHT = s2.DAYSKY, s2.SUNSKY, s2.NIGHT

DEFS = '''<linearGradient id="gIrid" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff5fd2"/><stop offset=".35" stop-color="#ffd84a"/><stop offset=".68" stop-color="#3fe0c5"/><stop offset="1" stop-color="#6c8dff"/></linearGradient>
<radialGradient id="gVig" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#3b2c1e" stop-opacity="0"/><stop offset="1" stop-color="#3b2c1e" stop-opacity=".28"/></radialGradient>
<linearGradient id="gSea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fb7cf"/><stop offset="1" stop-color="#2f6f8f"/></linearGradient>
<linearGradient id="gDeep" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3d7fa6"/><stop offset="1" stop-color="#173f5c"/></linearGradient>'''

def wrap(b):
    return f'<svg viewBox="0 0 480 270" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{b}</svg>'

def R(fill, op=1):
    return f'<rect width="480" height="270" fill="{fill}" opacity="{op}"/>'

def E(cx, cy, rx, ry, fill, op=1, f='blot', rot=0, stroke='none', sw=0):
    a = f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}"'
    if op != 1: a += f' opacity="{op}"'
    if stroke != 'none': a += f' stroke="{stroke}" stroke-width="{sw}"'
    if rot: a += f' transform="rotate({rot:.0f} {cx:.0f} {cy:.0f})"'
    if f: a += f' filter="url(#{f})"'
    return a + '/>'

def L(d, col=INK, w=1.4, op=1, extra=''):
    a = f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w:g}" stroke-linecap="round"'
    if op != 1: a += f' opacity="{op}"'
    return a + (' ' + extra if extra else '') + '/>'

def vig():
    return R('url(#gVig)') + paper()

def ripples(rng, n=60, col='#b78f5c', op=.35, y0=0, y1=270):
    out = ''
    for _ in range(n):
        x, y = rng.uniform(-20, 480), rng.uniform(y0, y1)
        w = rng.uniform(14, 40)
        out += L(f'M{x:.0f} {y:.0f} q{w/2:.0f} {-rng.uniform(2,5):.1f} {w:.0f} 0', col, 1, op)
    return out

def shrubs(rng, n=18, col='#7f9a5a', y0=0, y1=270):
    return ''.join(E(rng.uniform(0, 480), rng.uniform(y0, y1), rng.uniform(2, 4.5), rng.uniform(2, 4), col, .8, None) for _ in range(n))

def branch(rng, x, y, ang, ln, w, depth, col, out, op=1, spread=34):
    if depth == 0 or ln < 5:
        return
    a = math.radians(ang)
    mx, my = x + math.cos(a) * ln * .5 + rng.uniform(-ln * .15, ln * .15), y + math.sin(a) * ln * .5 + rng.uniform(-ln * .15, ln * .15)
    ex, ey = x + math.cos(a) * ln, y + math.sin(a) * ln
    out.append(L(f'M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {ex:.1f} {ey:.1f}', col, w, op))
    k = 2 if rng.random() < .85 else 3
    for i in range(k):
        na = ang + rng.uniform(-spread, spread) + (i - (k - 1) / 2) * 18
        branch(rng, ex, ey, na, ln * rng.uniform(.62, .8), max(w * .66, .6), depth - 1, col, out, op, spread)

def spark(x, y, s=1, col='url(#gIrid)'):
    return f'<path d="M{x} {y-9*s} Q{x+1.6*s} {y-1.6*s} {x+9*s} {y} Q{x+1.6*s} {y+1.6*s} {x} {y+9*s} Q{x-1.6*s} {y+1.6*s} {x-9*s} {y} Q{x-1.6*s} {y-1.6*s} {x} {y-9*s}Z" fill="{col}" stroke="#fff" stroke-width="{.8*s}"/>'

# ---------- small props ----------
def derrick(x, y, s=1):
    g = f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">'
    g += S('M-22 0 L-6 -118 L6 -118 L22 0Z', 'none', 2.2)
    for i in range(1, 6):
        yy = -i * 20
        w0 = 22 - i * 20 * 16 / 118
        w1 = 22 - (i - 1) * 20 * 16 / 118
        g += L(f'M{-w1:.1f} {yy+20} L{w0:.1f} {yy} M{w1:.1f} {yy+20} L{-w0:.1f} {yy} M{-w0:.1f} {yy} H{w0:.1f}', INK, 1.3)
    g += S('M-9 -118 h18 v-6 h-18z', '#8a6a48', 1.2) + '</g>'
    return g

def gusher(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">' +
            E(0, -150, 34, 26, '#2b2320', .92) + E(-26, -132, 22, 18, '#3a2e28', .85) + E(24, -128, 20, 16, '#3a2e28', .85) +
            f'<path d="M-5 -10 Q-8 -80 -2 -140 L4 -140 Q8 -80 5 -10Z" fill="#2b2320" filter="url(#wc)"/></g>')

def pool(x, y, rx, ry):
    return E(x, y, rx, ry, '#2b2320', .9) + E(x - rx * .25, y - ry * .3, rx * .35, ry * .25, '#7d8fa3', .5, None)

def drone(x, y, s=1):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += L('M-18 -8 L18 8 M-18 8 L18 -8', '#3b2c1e', 2.6)
    for cx, cy in [(-18, -8), (18, 8), (-18, 8), (18, -8)]:
        g += E(cx, cy, 9, 2.6, '#9db8c9', .8, None, stroke='#3b2c1e', sw=1)
    g += S('M-7 -4 h14 v8 h-14z', '#e3a64a', 1.2) + E(0, 6, 2.4, 2.4, '#3b2c1e', 1, None) + '</g>'
    return g

def satellite(x, y, s=1, rot=-18):
    g = f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
    g += S('M-9 -7 h18 v14 h-18z', '#d8c08c', 1.3) + S('M-38 -6 h26 v12 h-26z M12 -6 h26 v12 h-26z', '#4d6fa3', 1.1)
    g += L('M-31 -6 v12 M-24 -6 v12 M-18 -6 v12 M19 -6 v12 M26 -6 v12 M32 -6 v12', '#c7d6ee', .8) + L('M0 7 v8', INK, 1.4) + '</g>'
    return g

def beam(x0, y0, x1, x2, y, col='#ffe9a6', op=.28):
    return f'<path d="M{x0} {y0} L{x1} {y} L{x2} {y}Z" fill="{col}" opacity="{op}"/>'

def ship(x, y, s=1, flip=False):
    fx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({fx} {s})" filter="url(#wc)">' + S('M-46 -10 L40 -10 L30 6 L-40 6Z', '#c0573a', 1.6) +
            S('M-24 -26 h30 v16 h-30z', '#f1ead8', 1.4) + S('M-14 -36 h10 v10 h-10z', '#f1ead8', 1.2) + L('M-20 -20 h22', INK, 1) + '</g>')

def diver(x, y, s=1):
    g = f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">'
    g += S('M-30 0 Q-6 -8 18 -4 L22 4 Q-4 8 -30 6Z', '#2f3a48', 1.3) + S('M18 -6 a7 7 0 1 1 0.1 0', '#e2b48c', 1.2)
    g += S('M14 -9 h9 v5 h-9z', '#9fd3e6', 1) + S('M-12 -9 h16 v5 h-16z', '#e3a64a', 1.1) + S('M-30 0 L-46 -8 L-44 6Z', '#3b6f8f', 1.1) + '</g>'
    return g + ''.join(f'<circle cx="{x+22*s+i*3}" cy="{y-16*s-i*14}" r="{2+i*.7}" fill="none" stroke="#e6f4f8" stroke-width="1"/>' for i in range(3))

def fish(x, y, s=1, col='#e3a64a', flip=False):
    fx = -s if flip else s
    return f'<g transform="translate({x} {y}) scale({fx} {s})">' + S('M-10 0 Q0 -6 10 0 Q0 6 -10 0Z M10 0 L16 -5 L16 5Z', col, 1) + '</g>'

def kite(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#wc)">' + S('M0 -22 L16 0 L0 30 L-16 0Z', '#d0603a', 1.4) +
            L('M0 -22 V30 M-16 0 H16', INK, 1) + S('M-5 34 h10 v7 h-10z', '#3b2c1e', 1) + L('M0 30 q-8 14 2 26 q8 12 -2 24', '#d0603a', 1.4) + '</g>')

def vial(x, y, col):
    return S(f'M{x-8} {y-46} h16 v40 a8 8 0 0 1 -16 0z', '#eef4f6', 1.4) + f'<path d="M{x-8} {y-24} h16 v18 a8 8 0 0 1 -16 0z" fill="{col}" opacity=".9"/>'

def peaks(x, y, w, h, seq, col):
    pts = []
    n = len(seq)
    for i, v in enumerate(seq):
        px = x + w * i / (n - 1)
        pts.append(f'{px:.1f} {y - v * h:.1f}')
    return L('M' + ' L'.join(pts), col, 2)

# ---------- 1. seeps ----------
def seeps_clue():
    rng = random.Random(11)
    b = R('#ead6ad') + R('#d9bf8f', .35) + ripples(rng, 70) + L('M-10 210 Q120 190 250 205 T490 180', '#c9a874', 5, .5) + L('M-10 216 Q120 196 250 211 T490 186', '#c9a874', 2, .4)
    for cx, cy, r in [(190, 110, 26), (232, 92, 16), (262, 132, 30), (304, 98, 14), (214, 158, 18), (330, 150, 20), (160, 150, 12)]:
        b += E(cx, cy, r * 1.08, r, '#6b3f2a', .78, rot=rng.uniform(0, 90)) + E(cx - r * .2, cy - r * .2, r * .55, r * .5, '#8a5638', .55)
    b += shrubs(rng, 22) + vig()
    return b

def seeps_analog():
    b = SUNSKY + '<circle cx="380" cy="150" r="70" fill="url(#gGlow)"/>' + clouds([(110, 60, 70)])
    b += '<rect y="168" width="480" height="102" fill="url(#gSand)" filter="url(#wc)"/>'
    b += pool(110, 214, 46, 9) + pool(300, 236, 34, 7) + pool(410, 205, 26, 6)
    b += derrick(240, 196, 1) + gusher(240, 80, .9)
    b += fig(130, 246, .75, 'point', top='#c39a5b', robe=False, pants='#a88b62', head='cap', headc='#f1ead8') + fig(160, 250, .72, 'stand', top='#8fb3d1', robe=False, pants='#5b6a7a', head='hair')
    return b + paper()

def seeps_test():
    rng = random.Random(12)
    b = DAYSKY + '<rect y="120" width="480" height="150" fill="url(#gSand)" filter="url(#wc)"/>' + ripples(rng, 30, y0=130)
    b += E(250, 200, 120, 26, '#6b3f2a', .75) + E(230, 196, 60, 12, '#8a5638', .5)
    b += S('M300 120 v74', 'none', 3) + S('M292 120 h16', 'none', 3) + S('M298 194 l2 14 l2 -14z', '#8a8f96', 1)
    b += fig(330, 236, .9, 'hold', top='#e3a64a', robe=False, pants='#6d7f8f', head='cap', headc='#3f7cc0')
    b += S('M170 150 h22 v30 h-22z', '#3b6f8f', 1.4) + L('M181 180 v26', INK, 2) + E(181, 208, 4, 2, INK, 1, None)
    b += fig(150, 244, .9, 'reach', top='#6f8a5a', robe=False, pants='#5b6a4a', head='scarf', headc='#c9b28a', flip=True)
    return b + paper()

# ---------- 2. colours ----------
def colours_clue():
    rng = random.Random(21)
    b = R('#e9d6ae') + ripples(rng, 40)
    cols = ['#efe1c2', '#c8643a', '#efe1c2', '#8a7290', '#d7a25c', '#c8643a', '#efe1c2']
    for i, c in enumerate(cols):
        y = 40 + i * 30
        b += f'<path d="M-20 {y} C100 {y-30} 180 {y+30} 300 {y-10} S440 {y-40} 500 {y-6} L500 {y+34} C440 {y-6} 380 {y+28} 300 {y+22} S100 {y+2} -20 {y+34}Z" fill="{c}" opacity=".85" filter="url(#blot)"/>'
    b += '<path d="M260 -10 L300 280 L340 280 L292 -10Z" fill="#f7f1e2" opacity=".75" filter="url(#blot)"/>'
    b += L('M276 -10 L320 280', INK, 1.4, .7, 'stroke-dasharray="7 5"') + vig()
    return b

def colours_analog():
    b = DAYSKY + clouds([(90, 50, 60), (330, 40, 50)], '#ffffff', .8)
    b += '<path d="M0 270 V150 L60 140 L80 92 L210 86 L232 140 L300 146 L320 104 L420 98 L440 150 L480 152 V270Z" fill="#b5542e" filter="url(#wc)"/>'
    b += '<path d="M80 108 L210 102 L214 118 L76 124Z M320 118 L420 112 L424 126 L318 132Z" fill="#f2e6cf" opacity=".9" filter="url(#wc)"/>'
    b += '<path d="M0 200 Q240 180 480 204 V270 H0Z" fill="#c9955a" filter="url(#wc)"/>'
    b += '<path d="M150 230 Q240 170 330 236 Q240 206 150 230Z" fill="#efe3c8" opacity=".85" filter="url(#blot)"/>'
    b += satellite(400, 40, .9) + beam(400, 50, 300, 360, 150, '#fff6c8', .25)
    b += f'<g transform="translate(110 46)"><path d="M-16 0 L16 0 M0 -4 L0 4 M-6 -6 L6 -6" stroke="{INK}" stroke-width="2.2"/></g>'
    return b + paper()

def colours_test():
    b = DAYSKY + '<path d="M0 270 V90 L480 110 V270Z" fill="#e9d6ae" filter="url(#wc)"/>'
    for i, c in enumerate(['#efe1c2', '#c8643a', '#8a7290', '#d7a25c', '#c8643a']):
        y = 100 + i * 24
        b += f'<path d="M0 {y} L480 {y+20} L480 {y+42} L0 {y+22}Z" fill="{c}" opacity=".9" filter="url(#wc)"/>'
    b += '<rect y="226" width="480" height="44" fill="url(#gSand)" filter="url(#wc)"/>'
    b += ''.join(E(x, 150 + (x - 120) * .05, 6, 4, '#fff7e0', .95, None, stroke=INK, sw=1) for x in range(120, 360, 48))
    b += fig(390, 258, .9, 'reach', top='#3f7cc0', robe=False, pants='#5b6a7a', head='cap', headc='#e3a64a', flip=True)
    b += S('M352 186 l-10 -10 l4 -4 l10 10z', '#8a8f96', 1.2)
    return b + paper()

# ---------- 3. drowned ----------
def drowned_clue():
    rng = random.Random(31)
    b = R('#8fcfc2') + '<path d="M-10 -10 H220 Q200 40 150 60 Q90 80 40 130 Q10 160 -10 170Z" fill="#e7c98f" filter="url(#wc)"/>'
    b += '<path d="M-10 -10 H226 Q206 44 156 66 Q96 86 46 136 Q16 166 -10 178" fill="none" stroke="#f4f0e2" stroke-width="5" opacity=".8" filter="url(#wc)"/>'
    b += E(300, 170, 76, 46, '#346c70', .72, rot=-14) + E(290, 160, 40, 22, '#2a5a5e', .45, rot=-14)
    b += ''.join(L(f'M{rng.uniform(150,480):.0f} {rng.uniform(90,270):.0f} q8 -3 16 0', '#e8f6f2', 1, .6) for _ in range(40)) + vig()
    return b

def drowned_analog():
    b = R('url(#gSea)') + '<path d="M0 0 H480 V40 Q240 54 0 40Z" fill="#cfeaf0" opacity=".45"/>'
    b += '<path d="M0 214 Q120 200 240 210 T480 206 V270 H0Z" fill="#cdb488" filter="url(#wc)"/>'
    for cx, cy, w, h in [(110, 214, 70, 20), (210, 220, 54, 18), (330, 212, 80, 22)]:
        b += f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="9" fill="none" stroke="#8a7a5c" stroke-width="5" filter="url(#wc)"/>'
    for i in range(7):
        a = math.pi + i * math.pi / 6
        x, y = 420 + 34 * math.cos(a), 230 + 12 * math.sin(a)
        b += S(f'M{x-4:.0f} {y:.0f} v-{18+i%3*4} h8 v{18+i%3*4}z', '#a6977a', 1.2)
    b += fish(150, 120, 1.2) + fish(180, 136, .9, '#d0603a') + fish(330, 90, 1, '#f2c14e', True) + diver(300, 150, 1.1)
    return b + paper()

def drowned_test():
    b = R('url(#gSea)') + '<rect width="480" height="70" fill="#bfe3ee"/>' + wsea(70, '#6fa9c4')
    b += '<path d="M0 230 Q240 214 480 232 V270 H0Z" fill="#cdb488" filter="url(#wc)"/>'
    b += '<path d="M190 74 L70 232 L330 232Z" fill="#fff6c8" opacity=".22"/>' + ''.join(L(f'M{120+i*30} {226-i*2} q10 -6 20 0', '#fff6c8', 1.6, .6) for i in range(6))
    b += ship(190, 72, .8) + diver(370, 170, 1) + E(250, 236, 50, 8, '#2f5a5e', .6)
    return b + paper()

# ---------- 4. dogger ----------
def dogger_clue():
    b = R('url(#gDeep)') + '<path d="M120 20 C260 0 420 40 440 120 C460 200 330 250 220 230 C120 214 60 150 70 90 C76 54 96 30 120 20Z" fill="#6fcfc2" opacity=".9" filter="url(#blot)"/>'
    b += '<path d="M150 60 C250 46 380 70 392 130 C400 180 300 214 220 200 C150 188 110 140 118 100Z" fill="#a6e3d4" opacity=".6" filter="url(#blot)"/>'
    b += '<path d="M330 150 C350 130 400 132 420 150 C440 172 420 200 380 204 C346 206 318 186 330 150Z" fill="#e7c98f" stroke="#f4f0e2" stroke-width="4" filter="url(#wc)"/>'
    b += E(372, 170, 14, 8, '#7f9a5a', .8, None) + vig()
    return b

def dogger_analog():
    b = R('#bfe3ee', 1) + '<rect y="0" width="480" height="96" fill="url(#gSea)"/>' + wsea(10, '#6fa9c4')
    b += '<rect y="96" width="480" height="174" fill="#b99a6a"/>'
    for i, c in enumerate(['#c9ad7d', '#a98a5c', '#c2a374', '#9d7f55']):
        y = 110 + i * 38
        b += f'<path d="M0 {y} Q120 {y-8} 240 {y+4} T480 {y-2} V{y+38} H0Z" fill="{c}" filter="url(#wc)"/>'
    b += '<path d="M60 140 Q90 196 140 150 Q170 120 200 160 Q230 206 280 170" fill="none" stroke="#6f9fb8" stroke-width="9" opacity=".8" filter="url(#wc)"/>'
    b += '<path d="M300 190 Q340 240 390 196" fill="none" stroke="#6f9fb8" stroke-width="7" opacity=".7" filter="url(#wc)"/>'
    b += ship(110, 30, .7) + L('M140 26 L470 34', INK, 1.2, .8, 'stroke-dasharray="3 5"')
    b += ''.join(f'<path d="M{200+i*40} 96 q20 14 40 0" fill="none" stroke="#fff6c8" stroke-width="1.4" opacity=".7"/>' for i in range(5))
    b += ''.join(palm(x, y, .35) for x, y in [(96, 150), (230, 166)])
    return b + paper()

def dogger_test():
    b = R('#bfe3ee') + '<rect y="60" width="480" height="80" fill="url(#gSea)"/>' + wsea(56, '#6fa9c4')
    b += '<rect y="140" width="480" height="130" fill="#b99a6a" filter="url(#wc)"/>'
    b += '<path d="M120 170 Q200 236 280 176 Q340 140 420 190" fill="none" stroke="#6f9fb8" stroke-width="10" opacity=".75" filter="url(#wc)"/>'
    b += ship(240, 58, .9) + L('M240 60 V212', INK, 2.4) + S('M234 196 h12 v26 h-12z', '#e3a64a', 1.2)
    b += ''.join(f'<path d="M{180+i*20} 140 q20 12 40 0" fill="none" stroke="#fff6c8" stroke-width="1.2" opacity=".6"/>' for i in range(5))
    return b + paper()

# ---------- 5. creeks ----------
def creeks_clue():
    rng = random.Random(51)
    b = R('#cfc4ad') + R('#b9ae96', .4)
    out = []
    for x, y, a in [(-10, 250, -40), (60, 280, -60), (200, 285, -85), (340, 285, -105), (480, 250, -150), (490, 120, 180)]:
        branch(rng, x, y, a, 70, 6, 5, '#8fb0bf', out)
    b += ''.join(out)
    out2 = []
    for x, y, a in [(120, -10, 70), (300, -10, 110)]:
        branch(rng, x, y, a, 50, 3, 4, '#a59c86', out2, .8)
    b += ''.join(out2)
    b += '<path d="M-10 110 Q120 96 240 112 T490 100 L490 128 Q360 140 240 132 T-10 134Z" fill="#6d6a5c" opacity=".3" filter="url(#blot)"/>' + vig()
    return b

def creeks_analog():
    rng = random.Random(52)
    b = R('#f2ede1') + '<path d="M0 200 Q240 180 480 206 V270 H0Z" fill="#7fb7cf" filter="url(#wc)"/>'
    b += '<path d="M0 150 Q240 132 480 156 L480 206 Q240 180 0 200Z" fill="#9b8a5a" opacity=".55" filter="url(#blot)"/>'
    for i in range(80):
        x, y = rng.uniform(0, 480), rng.uniform(0, 140)
        r = rng.uniform(10, 18)
        pts = ' '.join(f'{x + r*math.cos(k*math.pi/3 + .3):.0f},{y + r*.7*math.sin(k*math.pi/3 + .3):.0f}' for k in range(6))
        b += f'<polygon points="{pts}" fill="none" stroke="#cfc4ad" stroke-width="1.2" opacity=".8"/>'
    out = []
    for x, a in [(80, -80), (250, -95), (400, -110)]:
        branch(rng, x, 205, a, 46, 5, 4, '#7fb7cf', out)
    return b + ''.join(out) + vig()

def creeks_test():
    rng = random.Random(53)
    b = R('#cfc4ad')
    out = []
    for x, y, a in [(-10, 250, -40), (200, 285, -85), (480, 250, -150)]:
        branch(rng, x, y, a, 70, 6, 5, '#8fb0bf', out)
    b += ''.join(out) + drone(250, 60, 1.6) + f'<path d="M250 70 L170 200 L330 200Z" fill="#fff6c8" opacity=".2"/>'
    b += fig(380, 250, .9, 'pull', top='#6f8a5a', robe=False, pants='#5b6a4a', head='cap', headc='#e3a64a') + S('M372 136 v110', 'none', 3)
    return b + vig()

# ---------- 6. quake ----------
def quake_clue():
    b = SUNSKY + '<circle cx="400" cy="110" r="70" fill="url(#gGlow)"/>' + '<rect y="126" width="480" height="144" fill="url(#gSand)" filter="url(#wc)"/>'
    for x, y, w in [(70, 168, 70), (170, 160, 60), (260, 176, 66)]:
        b += S(f'M{x} {y} h{w} v-14 h-{w}z', '#cbb08a', 1.4) + S(f'M{x+6} {y-14} h{w-12} v-8 h-{w-12}z', '#d9c19a', 1.2)
    b += S('M300 160 l40 -6 l2 -20 l-40 6z', '#cbb08a', 1.4)
    b += '<rect y="196" width="480" height="74" fill="#a9845a" filter="url(#wc)"/>' + '<path d="M0 196 H480" stroke="#3b2c1e" stroke-width="1.4"/>'
    for x in (90, 210, 330, 420):
        b += f'<path d="M{x} 270 Q{x+6} 240 {x-4} 220 Q{x+4} 206 {x} 196" fill="none" stroke="#f1e2b8" stroke-width="7" filter="url(#wc)"/>' + E(x, 194, 14, 4, '#f1e2b8', .95, None)
    b += L('M120 150 l14 10 l-8 8 l16 12 M250 186 l10 6 l-6 4', INK, 1.6, .8)
    return b + paper()

def quake_analog():
    b = DAYSKY + '<rect y="120" width="480" height="40" fill="#7fb7cf" filter="url(#wc)"/>' + '<rect y="152" width="480" height="118" fill="#a9845a" filter="url(#wc)"/>'
    b += '<path d="M0 152 H480" stroke="#3b2c1e" stroke-width="1.4"/>'
    for i, c in enumerate(['#b99a6a', '#a3845a', '#bfa074']):
        y = 172 + i * 32
        b += f'<path d="M0 {y} Q240 {y-8} 480 {y+4} V{y+32} H0Z" fill="{c}" filter="url(#wc)"/>'
    b += S('M120 230 h14 v-40 h-14z', '#e6d8bc', 1.3) + S('M142 236 l26 -8 l2 8 l-26 8z', '#e6d8bc', 1.2) + S('M300 214 h40 v10 h-40z', '#e6d8bc', 1.2)
    b += ''.join(S(f'M{x} {y} l6 -3 l4 4 l-6 3z', '#c0573a', 1) for x, y in [(210, 200), (250, 222), (190, 246), (380, 236), (420, 204)])
    b += S('M232 46 L210 152 M232 46 L254 152 M232 46 L232 152', 'none', 2.4) + L('M232 120 V250', INK, 3) + S('M228 232 h8 v20 h-8z', '#e3a64a', 1)
    b += '<g transform="translate(330 100)">' + ''.join(S(f'M{-30+i*14} 0 v-{30+i%2*14} h8 v{30+i%2*14}z', '#e6d8bc', 1.2) for i in range(5)) + '</g>'
    return b + paper()

def quake_test():
    b = R('#e9d6ae') + '<rect y="50" width="480" height="220" fill="#b0905f"/>'
    for i, c in enumerate(['#c4a676', '#8d6a45', '#c9ab7a', '#7a5a3a', '#bfa074', '#a3845a']):
        y = 60 + i * 34
        b += f'<path d="M0 {y} L480 {y+6} V{y+40} L0 {y+34}Z" fill="{c}" filter="url(#wc)"/>'
    b += '<path d="M232 270 Q246 220 236 180 Q250 150 240 120 L258 120 Q266 150 254 180 Q266 220 252 270Z" fill="#f1e2b8" filter="url(#wc)"/>'
    b += '<path d="M120 118 l30 -2 l4 8 M330 126 l40 6" stroke="#3b2c1e" stroke-width="1.6" fill="none"/>' + '<path d="M0 52 H480" stroke="#3b2c1e" stroke-width="1.6"/>'
    b += fig(370, 120, .62, 'reach', top='#c39a5b', robe=False, pants='#a88b62', head='cap', headc='#f1ead8', flip=True)
    return b + paper()

# ---------- 7. bitumen ----------
def bitumen_clue():
    b = SUNSKY + '<circle cx="110" cy="140" r="70" fill="url(#gGlow)"/>' + wsea(140)
    b += '<path d="M0 170 Q240 156 480 176 V270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>'
    b += ('<g filter="url(#wc)">' + S('M40 168 Q150 200 262 166 Q258 186 236 194 Q150 214 66 194 Q46 186 40 168Z', '#c9a46a', 1.6) +
          '<path d="M52 182 Q150 210 250 180 Q244 190 232 196 Q150 214 70 196 Q58 190 52 182Z" fill="#2b2320" opacity=".9"/>' +
          ''.join(L(f'M{x} {172+abs(x-150)*-.03+8} q2 10 0 22', '#7a5a3a', 1.4) for x in range(70, 240, 22)) +
          S('M30 160 q6 -2 10 8 M262 166 q8 -10 16 -8', 'none', 2) + '</g>')
    b += '<g filter="url(#wc)">' + S('M300 214 q30 -26 70 -10 q30 14 10 36 q-30 18 -70 6 q-24 -10 -10 -32z', '#2b2320', 1.6)
    b += ''.join(E(x, y, 5, 4, '#efe6d2', 1, None, stroke=INK, sw=1) for x, y in [(322, 210), (340, 204), (356, 212), (334, 222), (366, 226)])
    b += '</g>' + L('M296 236 q40 8 84 -2 M300 244 q40 8 80 -2', '#d9b48a', 2, .9)
    return b + paper()

def bitumen_analog():
    b = DAYSKY + wsea(130)
    b += '<path d="M330 150 Q380 126 440 132 Q480 136 490 150 L490 175 H330Z" fill="url(#gSand)" filter="url(#wc)"/>'
    b += '<g filter="url(#wc)">' + S('M392 132 h34 v-18 h-34z', '#efe1c2', 1.4) + S('M388 114 h42 l-21 -12z', '#d9c19a', 1.3) + '</g>'
    b += '<g transform="translate(170 162)" filter="url(#wc)">' + S('M-70 -8 Q0 14 70 -8 L60 8 Q0 22 -60 8Z', '#9a6a3a', 1.6) + L('M0 -8 V-80', INK, 2.2) + S('M2 -78 Q40 -50 2 -18Z', '#efe1c2', 1.3)
    b += ''.join(S(f'M{x} -8 q-6 -16 0 -22 h10 q6 6 0 22z', '#c9955a', 1.1) for x in (-50, -32, 24, 40)) + '</g>'
    return b + paper()

def bitumen_test():
    b = R('#f1ead8') + '<rect y="186" width="480" height="84" fill="#c9a874" filter="url(#wc)"/>'
    b += vial(110, 190, '#2b2320') + vial(150, 190, '#3a2e28') + vial(190, 190, '#4a3a30')
    b += S('M240 60 h210 v116 h-210z', '#fffdf6', 1.6)
    b += peaks(256, 160, 180, 80, [0, .1, .05, .6, .15, .9, .2, .4, .1, .7, .05, 0], '#3f7cc0')
    b += peaks(256, 160, 180, 80, [0, .12, .04, .55, .2, .85, .18, .45, .12, .65, .06, 0], '#d0603a')
    b += fig(80, 250, .8, 'hold', top='#f1ead8', robe=False, pants='#5b6a7a', head='hair')
    return b + paper()

# ---------- 8. river ----------
def river_clue():
    rng = random.Random(81)
    b = R('#ecd6a8') + ripples(rng, 50)
    for i in range(9):
        x, y = rng.uniform(20, 460), rng.uniform(20, 250)
        b += f'<path d="M{x:.0f} {y:.0f} q18 -16 36 0 q-18 -8 -36 0z" fill="#d9b67c" stroke="#b58a52" stroke-width="1"/>'
    b += '<g transform="rotate(-24 240 135)"><rect x="-40" y="90" width="560" height="96" fill="#2f3b48" opacity=".88" filter="url(#wc)"/>'
    out = []
    for x0 in (-30, 120, 260, 400):
        branch(rng, x0, 140 + rng.uniform(-14, 14), rng.uniform(-8, 8), 70, 4.5, 4, '#e9f2ff', out, .9, 26)
    b += ''.join(out) + '</g>' + vig()
    return b

def river_analog():
    b = NIGHT + s2.stars([(40, 30, 1.4), (120, 20, 1.2), (420, 40, 1.6), (300, 20, 1)])
    b += f'<g transform="translate(230 50) rotate(8)" filter="url(#wc)">' + S('M-40 0 Q-30 -10 30 -8 Q46 -4 50 0 Q46 4 30 8 Q-30 10 -40 0Z', '#f1ead8', 1.4) + S('M-10 -8 L-24 -24 L0 -9Z M-10 8 L-24 24 L0 9Z', '#f1ead8', 1.2) + '</g>'
    b += beam(230, 60, 120, 340, 170, '#fff6c8', .22)
    b += '<rect y="160" width="480" height="110" fill="url(#gSand)" filter="url(#wc)"/>' + ''.join(f'<path d="M{x} 166 q30 -18 60 0" fill="#e2c08a" stroke="#b58a52" stroke-width="1"/>' for x in (20, 160, 300, 400))
    b += '<path d="M120 200 Q230 236 340 196 L340 214 Q230 254 120 218Z" fill="#6f9fb8" opacity=".7" filter="url(#blot)"/>'
    b += S('M226 214 q6 -16 12 0 q-6 8 -12 0z', '#8a7a5c', 1.2)
    return b + paper()

def river_test():
    b = DAYSKY + satellite(380, 40, 1) + beam(380, 50, 200, 400, 200, '#fff6c8', .2)
    b += '<rect y="170" width="480" height="100" fill="url(#gSand)" filter="url(#wc)"/>'
    b += '<path d="M0 230 Q160 200 320 226 T480 210" fill="none" stroke="#6f9fb8" stroke-width="6" opacity=".55" stroke-dasharray="10 6" filter="url(#wc)"/>'
    b += '<g filter="url(#wc)">' + S('M120 206 h30 v20 h-30z', '#cbb08a', 1.3) + S('M116 206 h38 v-6 h-38z', '#a6977a', 1.1) + '</g>'
    b += camel(250, 228, .7) + palm(320, 222, .5)
    return b + paper()

# ---------- 9. tracks ----------
def tracks_clue():
    rng = random.Random(91)
    b = R('#d8c29a')
    for i in range(6):
        y = i * 50 - 10
        b += f'<path d="M-10 {y} Q240 {y+18} 490 {y-6} L490 {y+30} Q240 {y+44} -10 {y+26}Z" fill="{["#cdb589","#bfa274"][i%2]}" opacity=".6" filter="url(#blot)"/>'
    for k, (x0, y0, dx, dy) in enumerate([(20, 70, 34, 6), (40, 120, 32, 5), (10, 170, 36, 8), (60, 215, 30, 4)]):
        for i in range(14):
            x = x0 + i * dx
            y = y0 + i * dy + (6 if i % 2 else -6)
            b += E(x, y, 7, 6, '#8d7350', .6, None, stroke='#6f5a3c', sw=1)
    b += '<path d="M300 0 Q360 120 300 270 L480 270 L480 0Z" fill="#e7cf9f" opacity=".85" filter="url(#blot)"/>' + vig()
    return b

def tracks_analog():
    b = DAYSKY + '<rect y="150" width="480" height="120" fill="#d8c29a" filter="url(#wc)"/>'
    for k, (x0, y0) in enumerate([(30, 190), (40, 214), (20, 240)]):
        b += ''.join(E(x0 + i * 30, y0 + i * 1.5 + (3 if i % 2 else -3), 5, 3, '#8d7350', .7, None) for i in range(15))
    b += kite(300, 60, 1) + L('M300 96 Q330 170 360 238', INK, 1, .8)
    b += fig(372, 252, .85, 'up', top='#3f7cc0', robe=False, pants='#5b6a7a', head='cap', headc='#e3a64a', flip=True)
    b += f'<g opacity=".18">{s2.deino(150, 150, .7, ghost=True)}</g>' if 'ghost' in s2.deino.__code__.co_varnames else ''
    return b + paper()

def tracks_test():
    b = DAYSKY + '<rect y="140" width="480" height="130" fill="#d8c29a" filter="url(#wc)"/>'
    b += ''.join(E(60 + i * 32, 210 + (4 if i % 2 else -4), 6, 3.5, '#8d7350', .7, None) for i in range(10))
    b += drone(200, 70, 1.5) + '<path d="M200 80 L120 200 L290 200Z" fill="#fff6c8" opacity=".2"/>'
    b += fig(400, 250, .9, 'hold', top='#6f8a5a', robe=False, pants='#5b6a4a', head='scarf', headc='#c9b28a', flip=True) + S('M372 178 h22 v16 h-22z', '#2f3a48', 1.2)
    return b + paper()

# ---------- 10. ships ----------
def boat_outline(cx, cy, ln, wd, rot, pointed_both=False):
    pts = []
    for i in range(22):
        t = i / 21
        x = -ln / 2 + ln * t
        half = wd / 2 * math.sin(math.pi * t) ** (.6 if not pointed_both else 1)
        if not pointed_both and t < .3:
            half = wd / 2 * (0.75 + .25 * math.sin(math.pi * t / .6))
        pts.append((x, half))
    full = pts + [(x, -h) for x, h in reversed(pts)]
    a = math.radians(rot)
    out = ''
    for x, y in full[::1]:
        rx, ry = cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)
        out += E(rx, ry, 3.6, 3.2, '#a6977a', 1, None, stroke=INK, sw=.9)
    return out

def ships_clue():
    rng = random.Random(101)
    b = R('#d9c49b') + '<path d="M-10 -10 H490 V36 Q240 54 -10 30Z" fill="#7fb7cf" filter="url(#wc)"/>' + ripples(rng, 40, y0=60)
    b += ''.join(E(rng.uniform(0, 480), rng.uniform(60, 270), 2, 2, '#a6977a', .8, None) for _ in range(80))
    b += boat_outline(140, 120, 110, 26, -8) + boat_outline(300, 150, 150, 30, -14) + boat_outline(200, 220, 90, 22, -6)
    b += E(410, 210, 24, 22, '#bfae88', .9, stroke=INK, sw=1) + E(430, 120, 18, 16, '#bfae88', .9, stroke=INK, sw=1) + vig()
    return b

def ships_analog():
    b = SUNSKY + '<circle cx="380" cy="140" r="70" fill="url(#gGlow)"/>' + wsea(146, '#4f86a8')
    b += '<path d="M0 156 Q200 140 480 170 V270 H0Z" fill="#8fb36a" filter="url(#wc)"/>'
    for i in range(15):
        t = i / 14
        x = 60 + 360 * t
        y = 220 - 34 * math.sin(math.pi * t)
        h = 26 + 18 * (1 if i in (0, 14) else 0) + 8 * math.sin(math.pi * t)
        b += S(f'M{x-6:.0f} {y:.0f} v-{h:.0f} q6 -6 12 0 v{h:.0f}z', '#8c8a84', 1.2)
    for i in range(1, 14):
        t = i / 14
        x = 60 + 360 * t
        y = 220 + 22 * math.sin(math.pi * t)
        h = 22 + 8 * math.sin(math.pi * t)
        b += S(f'M{x-7:.0f} {y:.0f} v-{h:.0f} q7 -7 14 0 v{h:.0f}z', '#9a978f', 1.2)
    return b + paper()

def ships_test():
    rng = random.Random(103)
    b = R('#d9c49b') + '<path d="M-10 -10 H490 V36 Q240 54 -10 30Z" fill="#7fb7cf" filter="url(#wc)"/>'
    b += boat_outline(150, 130, 110, 26, -8) + boat_outline(320, 170, 150, 30, -14)
    b += L('M196 124 L250 40', 'url(#gIrid)', 3, .9, 'stroke-dasharray="4 5"') + L('M386 154 L430 40', 'url(#gIrid)', 3, .9, 'stroke-dasharray="4 5"')
    b += drone(90, 60, 1.2) + S('M420 200 v60', 'none', 2.6) + E(420, 198, 6, 6, '#e3a64a', 1, None, stroke=INK, sw=1) + vig()
    return b

# ---------- 11. faults ----------
def faults_clue():
    rng = random.Random(111)
    b = R('#e6d1a4') + ripples(rng, 40)
    b += '<path d="M-10 60 Q120 40 220 80 Q300 112 490 70 L490 -10 H-10Z" fill="#cdb07c" filter="url(#wc)"/>' + L('M-10 60 Q120 40 220 80 Q300 112 490 70', INK, 1.6, .7)
    b += L('M60 280 L380 -10', INK, 1.6, .75, 'stroke-dasharray="8 6"')
    for t, rx in [(.25, 26), (.42, 34), (.58, 22), (.74, 18)]:
        x, y = 60 + 320 * t, 280 - 290 * t
        b += E(x, y, rx, 9, '#7aa05a', .75, rot=-42)
        b += ''.join(E(x + rng.uniform(-rx * .7, rx * .7), y + rng.uniform(-6, 6), 1.8, 1.8, '#7a4fa3', .9, None) for _ in range(6))
    b += E(330, 180, 14, 12, '#5b4330', .65) + E(330, 180, 9, 7, '#2f2620', .7, None) + shrubs(rng, 14) + vig()
    return b

def faults_analog():
    b = DAYSKY + '<path d="M0 270 V150 L120 120 L200 132 L300 100 L400 118 L480 110 V270Z" fill="#c9a874" filter="url(#wc)"/>'
    b += '<path d="M0 200 Q240 170 480 196 V270 H0Z" fill="url(#gSand)" filter="url(#wc)"/>' + L('M0 196 Q240 168 480 190', INK, 1.6, .7, 'stroke-dasharray="8 6"')
    b += ''.join(palm(x, 196 - x * .02 + (0 if i % 2 else 4), .55 + (i % 3) * .07) for i, x in enumerate(range(40, 460, 52)))
    b += E(250, 214, 40, 6, '#7fb7cf', .8)
    return b + paper()

def faults_test():
    rng = random.Random(113)
    b = R('#f1ead8') + S('M40 30 h260 v210 h-260z', '#e6d1a4', 1.6)
    b += L('M70 240 L270 30', INK, 1.4, .7, 'stroke-dasharray="6 5"')
    for t in (.2, .38, .55, .72):
        x, y = 70 + 200 * t, 240 - 210 * t
        b += E(x, y, 16, 6, '#7aa05a', .8, rot=-46)
    b += S('M350 60 h70 v170 h-70z', '#eef4f6', 1.6) + '<path d="M350 120 h35 v110 h-35z" fill="#7fb7cf"/>' + '<path d="M385 180 h35 v50 h-35z" fill="#7fb7cf"/>'
    b += L('M350 120 h35 v60 h35', INK, 1.4)
    return b + paper()

KEYS = ['seeps', 'colours', 'drowned', 'dogger', 'creeks', 'quake', 'bitumen', 'river', 'tracks', 'ships', 'faults']
ART = {}
for k in KEYS:
    c, a, t = globals()[k + '_clue'](), globals()[k + '_analog'](), globals()[k + '_test']()
    ART[f'x-{k}-1'], ART[f'x-{k}-2'], ART[f'x-{k}-4'] = wrap(c), wrap(a), wrap(t)
    cover = (f'<clipPath id="cL-{k}"><rect width="240" height="270"/></clipPath><clipPath id="cR-{k}"><rect x="240" width="240" height="270"/></clipPath>'
             f'<g clip-path="url(#cL-{k})"><g transform="translate(-120 0)">{c}</g></g><g clip-path="url(#cR-{k})"><g transform="translate(120 0)">{a}</g></g>'
             '<path d="M240 0 V270" stroke="#fffaf0" stroke-width="5"/>'
             '<path d="M120 150 Q240 70 360 150" fill="none" stroke="url(#gIrid)" stroke-width="4" stroke-dasharray="3 8" stroke-linecap="round"/>'
             + '<circle cx="120" cy="150" r="7" fill="url(#gIrid)" stroke="#fff" stroke-width="2"/><circle cx="360" cy="150" r="7" fill="url(#gIrid)" stroke="#fff" stroke-width="2"/>'
             + spark(240, 96, 1.5))
    ART[f'x-{k}-0'] = wrap(cover)
