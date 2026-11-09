"""Composable storybook scenes (480x270) in the Layers watercolour style. Used for the five Gulf editions.
scene(spec) where spec = {bg, ground, horizon, el:[{t,x,y,s,flip}], people:[{t,x,y,s,pose,flip,back,hat}], fx:[...]}"""
import runpy, math, random
SA = runpy.run_path('/tmp/w/story_art.py')
INK = SA['INK']; S = SA['S']; prof = SA['prof']; shadow = SA['shadow']; clouds = SA['clouds']; cracks = SA['cracks']; paper = SA['paper']; headgear = SA['headgear']; jar = SA['jar']
DEFS = SA['DEFS'] + '''
<linearGradient id="gNight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#13213a"/><stop offset="1" stop-color="#3f4e6e"/></linearGradient>
<linearGradient id="gSea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fa9b4"/><stop offset="1" stop-color="#2c6e72"/></linearGradient>
<linearGradient id="gLagoon" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fd9d6"/><stop offset="1" stop-color="#4aa3a8"/></linearGradient>
<linearGradient id="gRock" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9a27a"/><stop offset="1" stop-color="#8f6a4a"/></linearGradient>
<linearGradient id="gLava" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a3f3c"/><stop offset="1" stop-color="#2b2422"/></linearGradient>
<linearGradient id="gGreen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fbf6b"/><stop offset="1" stop-color="#6d9a4c"/></linearGradient>
<linearGradient id="gCave" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b2c24"/><stop offset="1" stop-color="#1c1411"/></linearGradient>
<linearGradient id="gDusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b5b95"/><stop offset=".6" stop-color="#e08a6a"/><stop offset="1" stop-color="#f6c77c"/></linearGradient>
<radialGradient id="gMoon"><stop offset="0" stop-color="#fff7d6"/><stop offset="1" stop-color="#fff7d6" stop-opacity="0"/></radialGradient>
'''
SKY = {'day': 'url(#gDay)', 'sunset': 'url(#gSun)', 'night': 'url(#gNight)', 'dusk': 'url(#gDusk)', 'wall': 'url(#gWall)', 'cave': 'url(#gCave)'}
GROUND = {'sand': 'url(#gSand)', 'salt': 'url(#gSalt)', 'sea': 'url(#gSea)', 'lagoon': 'url(#gLagoon)', 'rock': 'url(#gRock)', 'lava': 'url(#gLava)', 'green': 'url(#gGreen)', 'floor': '#9a7350', 'cave': '#2a1e18', 'none': ''}

def rr(seed): return random.Random(seed)

# ---------- motifs: each returns SVG drawn around (x, y) = base point, scale s ----------
def m_palm(x, y, s=1, **k):
    fr = ''.join(f'<path d="M{x} {y-60*s} q{dx*18*s} {-10*s} {dx*34*s} {8*s}" fill="none" stroke="#4f8f5a" stroke-width="{5*s}" stroke-linecap="round"/>' for dx in (-1, 1, -.6, .6, -.25, .25))
    return f'<g filter="url(#wc)">' + S(f'M{x-3*s} {y} Q{x+4*s} {y-30*s} {x} {y-60*s}', 'none', 4*s) + fr + f'<circle cx="{x}" cy="{y-60*s}" r="{3*s}" fill="#b87a2e"/></g>'
def m_mangrove(x, y, s=1, **k):
    roots = ''.join(f'<path d="M{x} {y-22*s} Q{x+dx*8*s} {y-12*s} {x+dx*14*s} {y}" fill="none" stroke="#6b4a2e" stroke-width="{2.2*s}"/>' for dx in (-1.2, -.5, .5, 1.2))
    return f'<g filter="url(#wc)">{roots}' + S(f'M{x-2*s} {y-22*s} v-{16*s} h{4*s} v{16*s}z', '#6b4a2e', 1) + S(f'M{x-24*s} {y-40*s} a{24*s} {14*s} 0 1 0 {48*s} 0 a{24*s} {14*s} 0 1 0 -{48*s} 0z', '#4f8f5a', 1.4) + '</g>'
def m_grass(x, y, s=1, **k):
    return ''.join(f'<path d="M{x} {y}q{dx*4*s} {-10*s} {dx*9*s} {-20*s}" fill="none" stroke="#3f8a4f" stroke-width="{1.6*s}" stroke-linecap="round"/>' for dx in (-1.2, -.4, .4, 1.2))
def m_tomb(x, y, s=1, **k):  # Hafit/beehive tomb
    return f'<g filter="url(#wc)">' + S(f'M{x-30*s} {y} Q{x-30*s} {y-52*s} {x} {y-56*s} Q{x+30*s} {y-52*s} {x+30*s} {y}Z', '#d8bb8e', 1.6) + ''.join(f'<path d="M{x-28*s+i*0} {y-10*s-i*11*s} q{30*s} {-6*s} {56*s} 0" fill="none" stroke="{INK}" stroke-width="1" opacity=".5"/>' for i in range(4)) + S(f'M{x-6*s} {y} v-{16*s} h{12*s} v{16*s}z', '#4a3a2c', 1.1) + '</g>'
def m_fort(x, y, s=1, **k):
    bat = ''.join(f'<rect x="{x-44*s+i*14*s}" y="{y-66*s}" width="{8*s}" height="{8*s}" fill="#d9b985" stroke="{INK}" stroke-width="1"/>' for i in range(7))
    return f'<g filter="url(#wc)">' + S(f'M{x-44*s} {y} v-{58*s} h{88*s} v{58*s}z', '#e0c094', 1.6) + S(f'M{x-56*s} {y} v-{74*s} q{12*s} -{6*s} {24*s} 0 v{74*s}z', '#d9b985', 1.5) + S(f'M{x+32*s} {y} v-{74*s} q{12*s} -{6*s} {24*s} 0 v{74*s}z', '#d9b985', 1.5) + bat + S(f'M{x-8*s} {y} v-{22*s} a{8*s} {8*s} 0 0 1 {16*s} 0 v{22*s}z', '#4a3a2c', 1.1) + '</g>'
def m_tower(x, y, s=1, **k):  # Nabataean/rock-cut facade
    return f'<g filter="url(#wc)">' + S(f'M{x-40*s} {y} v-{80*s} l{10*s} -{10*s} h{60*s} l{10*s} {10*s} v{80*s}z', '#d9a46a', 1.6) + S(f'M{x-30*s} {y-70*s} h{60*s} M{x-30*s} {y-60*s} h{60*s}', 'none', 1.2) + ''.join(S(f'M{x-32*s+i*16*s} {y-80*s} l{8*s} -{8*s} l{8*s} {8*s}z', '#c48d55', 1) for i in range(4)) + S(f'M{x-10*s} {y} v-{36*s} h{20*s} v{36*s}z', '#3a2a20', 1.1) + '</g>'
def m_wall(x, y, s=1, **k):  # ruined mud-brick wall
    out = ''
    for row in range(3):
        for col in range(5 - row):
            bx = x - 40*s + col*16*s + row*8*s; by = y - row*10*s
            out += f'<rect x="{bx}" y="{by-10*s}" width="{15*s}" height="{9*s}" fill="#f3d9ae" stroke="{INK}" stroke-width="1.1"/>'
    return f'<g filter="url(#wc)">{out}</g>'
def m_jar(x, y, s=1, **k): return f'<g filter="url(#wc)">{jar(x, y, 28*s)}</g>'
def m_coins(x, y, s=1, **k):
    return ''.join(f'<circle cx="{x+dx*s}" cy="{y+dy*s}" r="{6*s}" fill="#d8b24a" stroke="{INK}" stroke-width="1.1"/>' for dx, dy in ((0, 0), (10, 3), (5, -6)))
def m_stone(x, y, s=1, **k):  # inscribed standing stone
    lines = ''.join(f'<path d="M{x-12*s} {y-50*s+i*8*s} h{24*s}" stroke="{INK}" stroke-width="1" opacity=".55"/>' for i in range(5))
    return f'<g filter="url(#wc)">' + S(f'M{x-18*s} {y} v-{56*s} q{18*s} -{10*s} {36*s} 0 v{56*s}z', '#b9a089', 1.5) + lines + '</g>'
def m_well(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-18*s} {y} v-{16*s} a{18*s} {7*s} 0 0 1 {36*s} 0 v{16*s} a{18*s} {7*s} 0 0 1 -{36*s} 0z', '#c9b08a', 1.4) + S(f'M{x-14*s} {y-16*s} v-{30*s} M{x+14*s} {y-16*s} v-{30*s} M{x-18*s} {y-46*s} h{36*s}', 'none', 2.2) + S(f'M{x} {y-46*s} v{14*s}', 'none', 1.2) + S(f'M{x-5*s} {y-32*s} h{10*s} v{8*s} h-{10*s}z', '#8a6a4a', 1) + '</g>'
def m_dhow(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-34*s} {y-8*s} Q{x} {y+6*s} {x+40*s} {y-10*s} L{x+30*s} {y+2*s} L{x-28*s} {y+2*s}Z', '#8a5a34', 1.4) + S(f'M{x} {y-8*s} v-{46*s}', 'none', 2) + S(f'M{x+2*s} {y-52*s} L{x+36*s} {y-10*s} L{x+2*s} {y-12*s}Z', '#f4ecd8', 1.3) + '</g>'
def m_oryx(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    body = S(f'M{x-22*s} {y-30*s} q{22*s} -{10*s} {44*s} 0 l{2*s} {30*s} h-{6*s} l-{4*s} -{20*s} h-{28*s} l-{4*s} {20*s} h-{6*s}z', '#f1e8d6', 1.3)
    head = S(f'M{x+20*f*s} {y-34*s} l{10*f*s} -{8*s} l{6*f*s} {10*s} l-{10*f*s} {6*s}z', '#f1e8d6', 1.2) + f'<path d="M{x+28*f*s} {y-40*s} l{8*f*s} -{26*s} M{x+32*f*s} {y-40*s} l{10*f*s} -{26*s}" stroke="{INK}" stroke-width="1.6" fill="none"/>' + f'<path d="M{x+22*f*s} {y-30*s} l{12*f*s} {4*s}" stroke="#5a4634" stroke-width="{3*s}"/>'
    return f'<g filter="url(#wc)">{body}{head}</g>'
def m_gazelle(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return f'<g filter="url(#wc)">' + S(f'M{x-16*s} {y-24*s} q{16*s} -{8*s} {32*s} 0 l{2*s} {24*s} h-{4*s} l-{3*s} -{16*s} h-{22*s} l-{3*s} {16*s} h-{4*s}z', '#d8b98c', 1.2) + S(f'M{x+14*f*s} {y-28*s} l{8*f*s} -{10*s} l{5*f*s} {8*s} l-{7*f*s} {4*s}z', '#d8b98c', 1.1) + f'<path d="M{x+20*f*s} {y-36*s} q{2*f*s} -{10*s} -{3*f*s} -{14*s} M{x+24*f*s} {y-36*s} q{2*f*s} -{10*s} -{2*f*s} -{14*s}" stroke="{INK}" stroke-width="1.3" fill="none"/></g>'
def m_whale(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return f'<g filter="url(#wc)">' + S(f'M{x-60*f*s} {y} q{30*f*s} -{34*s} {80*f*s} -{24*s} q{30*f*s} {4*s} {40*f*s} {24*s} q-{40*f*s} {10*s} -{80*f*s} {6*s} q-{30*f*s} -{2*s} -{40*f*s} -{6*s}z', '#4a6a7a', 1.4) + S(f'M{x-56*f*s} {y-4*s} l-{18*f*s} -{16*s} l{4*f*s} {18*s} l-{4*f*s} {16*s}z', '#4a6a7a', 1.2) + f'<circle cx="{x+36*f*s}" cy="{y-14*s}" r="{2*s}" fill="{INK}"/>' + f'<path d="M{x+6*f*s} {y-18*s} q{10*f*s} {6*s} {24*f*s} {4*s}" fill="none" stroke="#dfe7ea" stroke-width="{1.6*s}" opacity=".7"/></g>'
def m_turtle(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return f'<g filter="url(#wc)">' + S(f'M{x-18*s} {y} a{18*s} {12*s} 0 1 1 {36*s} 0z', '#5f8a5a', 1.3) + ''.join(f'<path d="M{x-10*s+i*7*s} {y-11*s} v{10*s}" stroke="{INK}" stroke-width="1" opacity=".5"/>' for i in range(4)) + S(f'M{x+18*f*s} {y-4*s} l{10*f*s} -{3*s} l{2*f*s} {6*s} l-{10*f*s} {2*s}z', '#7aa06c', 1.1) + S(f'M{x-14*s} {y} l-{8*s} {6*s} l{10*s} 0z M{x+12*s} {y} l{8*s} {6*s} l-{10*s} 0z', '#7aa06c', 1.1) + '</g>'
def m_bird(x, y, s=1, **k):
    return f'<path d="M{x-10*s} {y} q{5*s} -{7*s} {10*s} 0 q{5*s} -{7*s} {10*s} 0" fill="none" stroke="{INK}" stroke-width="{1.5*s}" stroke-linecap="round"/>'
def m_flamingo(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return f'<g filter="url(#wc)">' + S(f'M{x-14*s} {y-30*s} a{14*s} {9*s} 0 1 1 {28*s} 0z', '#e8a0a0', 1.2) + f'<path d="M{x+10*f*s} {y-34*s} q{6*f*s} -{20*s} -{4*f*s} -{30*s} q-{6*f*s} -{2*s} -{2*f*s} -{8*s}" fill="none" stroke="#e8a0a0" stroke-width="{3*s}"/><path d="M{x-4*s} {y-30*s} v{30*s} M{x+4*s} {y-30*s} v{30*s}" stroke="{INK}" stroke-width="1.2"/><path d="M{x+2*f*s} {y-72*s} l{6*f*s} {2*s}" stroke="{INK}" stroke-width="2.2"/></g>'
def m_falcon(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x} {y} l-{40*s} -{18*s} q{20*s} -{4*s} {36*s} {6*s} q{16*s} -{10*s} {36*s} -{6*s}z', '#7a5a3a', 1.2) + f'<circle cx="{x}" cy="{y-2*s}" r="{3*s}" fill="{INK}"/></g>'
def m_coral(x, y, s=1, **k):
    br = ''.join(f'<path d="M{x} {y} q{dx*6*s} -{14*s} {dx*10*s} -{26*s} M{x+dx*10*s} {y-26*s} l{dx*5*s} -{6*s} M{x+dx*10*s} {y-26*s} l-{dx*2*s} -{8*s}" fill="none" stroke="{c}" stroke-width="{3*s}" stroke-linecap="round"/>' for dx, c in ((-1, '#e07a6a'), (0, '#f0a060'), (1, '#d86a8a')))
    return f'<g filter="url(#wc)">{br}' + S(f'M{x-14*s} {y+2*s} a{14*s} {8*s} 0 1 1 {28*s} 0z', '#c2a07a', 1) + '</g>'
def m_fish(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return S(f'M{x-10*f*s} {y} q{10*f*s} -{8*s} {20*f*s} 0 q-{10*f*s} {8*s} -{20*f*s} 0z M{x-10*f*s} {y} l-{7*f*s} -{5*s} v{10*s}z', '#f0b060', 1.1)
def m_crater(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-90*s} {y} l{30*s} -{30*s} h{120*s} l{30*s} {30*s}z', '#b08860', 1.5) + S(f'M{x-60*s} {y-30*s} h{120*s} q-{20*s} {22*s} -{60*s} {24*s} q-{40*s} -{2*s} -{60*s} -{24*s}z', '#6b4a3a', 1.2) + f'<ellipse cx="{x}" cy="{y-10*s}" rx="{36*s}" ry="{8*s}" fill="#f3eee4" opacity=".9"/></g>'
def m_volcano(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-80*s} {y} l{60*s} -{70*s} h{40*s} l{60*s} {70*s}z', '#3b302c', 1.5) + f'<path d="M{x-20*s} {y-70*s} h{40*s} l-{8*s} {30*s} l-{12*s} -{10*s} l-{12*s} {10*s}z" fill="#d9643a" opacity=".85"/>' + ''.join(f'<ellipse cx="{x+dx*s}" cy="{y-90*s+dy*s}" rx="{14*s}" ry="{8*s}" fill="#b9b3ab" opacity=".8" filter="url(#blot)"/>' for dx, dy in ((0, 0), (12, -12), (-6, -22))) + '</g>'
def m_lavatube(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-70*s} {y} q{10*s} -{60*s} {70*s} -{64*s} q{60*s} {4*s} {70*s} {64*s}z', '#4a3f3c', 1.5) + S(f'M{x-38*s} {y} q{8*s} -{36*s} {38*s} -{38*s} q{30*s} {2*s} {38*s} {38*s}z', '#120c0a', 1.2) + '</g>'
def m_dune(x, y, s=1, **k):
    return f'<path d="M{x-120*s} {y} q{60*s} -{50*s} {120*s} -{44*s} q{60*s} {6*s} {120*s} {44*s}z" fill="#e2a36b" stroke="{INK}" stroke-width="1.2" filter="url(#wc)"/><path d="M{x-40*s} {y-30*s} q{40*s} -{12*s} {80*s} -{4*s}" fill="none" stroke="#c98650" stroke-width="{1.5*s}"/>'
def m_cliff(x, y, s=1, **k):
    bands = ''.join(f'<path d="M{x-100*s} {y-80*s+i*16*s} h{200*s}" stroke="{c}" stroke-width="{12*s}"/>' for i, c in enumerate(('#d9a066', '#b4521c', '#e8c08a', '#9b78bd', '#cf8e5c')))
    return f'<g filter="url(#wc)"><clipPath id="clf{int(x)}{int(y)}"><path d="M{x-100*s} {y} v-{70*s} q{40*s} -{18*s} {100*s} -{16*s} q{60*s} 2 {100*s} {16*s} v{70*s}z"/></clipPath><g clip-path="url(#clf{int(x)}{int(y)})"><rect x="{x-100*s}" y="{y-90*s}" width="{200*s}" height="{90*s}" fill="#d9a066"/>{bands}</g>' + S(f'M{x-100*s} {y} v-{70*s} q{40*s} -{18*s} {100*s} -{16*s} q{60*s} 2 {100*s} {16*s} v{70*s}', 'none', 1.6) + '</g>'
def m_fossil(x, y, s=1, **k):
    sp = f'M{x} {y}' + ''.join(f'L{x + math.cos(t)*14*s*t/12.6:.1f} {y + math.sin(t)*14*s*t/12.6:.1f}' for t in [k2*.35 for k2 in range(1, 37)])
    return f'<circle cx="{x}" cy="{y}" r="{15*s}" fill="#c9b08a" stroke="{INK}" stroke-width="1.3"/><path d="{sp}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
def m_footprints(x, y, s=1, **k):
    return ''.join(f'<ellipse cx="{x+i*26*s}" cy="{y+(i%2)*8*s}" rx="{9*s}" ry="{6*s}" fill="#b08860" stroke="{INK}" stroke-width="1" opacity=".8"/>' for i in range(5))
def m_spring(x, y, s=1, **k):
    return f'<g filter="url(#wc)"><ellipse cx="{x}" cy="{y}" rx="{40*s}" ry="{12*s}" fill="#7fc4d6" stroke="{INK}" stroke-width="1.2"/>' + ''.join(f'<g class="rise{d}"><circle cx="{x+dx*s}" cy="{y-4*s}" r="{3*s}" fill="#dff3f8"/></g>' for dx, d in ((-10, ''), (6, ' d1s'), (18, ' d2s'))) + '</g>'
def m_oilwell(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-18*s} {y} l{14*s} -{70*s} h{8*s} l{14*s} {70*s}z', '#5b4330', 1.3) + ''.join(f'<path d="M{x-14*s+i*2*s} {y-i*18*s} h{28*s-i*4*s}" stroke="{INK}" stroke-width="1"/>' for i in range(1, 4)) + S(f'M{x} {y-70*s} l-{6*s} -{14*s} h{12*s}z', '#1a2a2b', 1) + '</g>'
def m_tent(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-50*s} {y} l{30*s} -{34*s} h{40*s} l{30*s} {34*s}z', '#5a4634', 1.4) + S(f'M{x-20*s} {y-34*s} h{40*s} l-{10*s} {34*s} h-{20*s}z', '#3a2d24', 1) + '</g>'
def m_camel(x, y, s=1, flip=False, **k):
    f = -1 if flip else 1
    return f'<g filter="url(#wc)">' + S(f'M{x-24*s} {y-34*s} q{10*s} -{16*s} {24*s} -{12*s} q{14*s} -{4*s} {26*s} {12*s} l{2*s} {34*s} h-{6*s} l-{3*s} -{22*s} h-{30*s} l-{3*s} {22*s} h-{6*s}z', '#c48d55', 1.3) + S(f'M{x+22*f*s} {y-40*s} q{8*f*s} -{16*s} {6*f*s} -{30*s} l{8*f*s} 0 l{2*f*s} {6*s} l-{6*f*s} {4*s} q-{2*f*s} {12*s} -{6*f*s} {22*s}z', '#c48d55', 1.2) + '</g>'
def m_oasis(x, y, s=1, **k):
    return m_spring(x, y, s*1.4) + m_palm(x-40*s, y-6*s, s*.8) + m_palm(x+44*s, y-4*s, s*.9) + m_palm(x+10*s, y-14*s, s*.7)
def m_house(x, y, s=1, **k):  # coral-stone tower house with wooden screens
    win = ''
    for i in range(3):
        for r in range(2):
            wy = y - (64 - r*26)*s; wx = x - 20*s + i*22*s
            win += S(f'M{wx} {wy} h{14*s} v{18*s} h-{14*s}z', '#8a5a34', 1.1) + f'<path d="M{wx} {wy+6*s} h{14*s} M{wx} {wy+12*s} h{14*s}" stroke="#f3d9ae" stroke-width="1"/>'
    return f'<g filter="url(#wc)">' + S(f'M{x-30*s} {y} v-{76*s} h{60*s} v{76*s}z', '#efe2c6', 1.5) + win + '</g>'
def m_lab(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-60*s} {y} v-{10*s} h{120*s} v{10*s}z', '#8a6a4a', 1.3) + jar(x-40*s, y-10*s, 26*s) + jar(x-14*s, y-10*s, 20*s, '#8a6a4a') + S(f'M{x+10*s} {y-10*s} l{6*s} -{36*s} h{14*s} l{6*s} {36*s}z', '#dff3f8', 1.2) + S(f'M{x+40*s} {y-10*s} v-{30*s} h{18*s} v{30*s}z', '#3d3a36', 1.2) + '</g>'
def m_satellite(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-40*s} {y} h{28*s} v{14*s} h-{28*s}z M{x+12*s} {y} h{28*s} v{14*s} h-{28*s}z', '#4f7fb0', 1.2) + S(f'M{x-10*s} {y-4*s} h{20*s} v{22*s} h-{20*s}z', '#cfcac2', 1.3) + '</g>'
def m_map(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-50*s} {y} l{6*s} -{70*s} h{88*s} l{6*s} {70*s}z', '#f4ecd8', 1.3) + f'<path d="M{x-30*s} {y-50*s} q{30*s} -{10*s} {50*s} {10*s} q{10*s} {20*s} -{20*s} {26*s}" fill="none" stroke="#2c6e72" stroke-width="{1.6*s}"/><circle cx="{x+8*s}" cy="{y-30*s}" r="{4*s}" fill="#d9643a"/></g>'
def m_moon(x, y, s=1, **k): return f'<circle cx="{x}" cy="{y}" r="{60*s}" fill="url(#gMoon)"/><circle cx="{x}" cy="{y}" r="{16*s}" fill="#fff7d6"/>'
def m_sun(x, y, s=1, **k): return f'<circle cx="{x}" cy="{y}" r="{80*s}" fill="url(#gGlow)"/><circle cx="{x}" cy="{y}" r="{18*s}" fill="#f6c24a" stroke="{INK}" stroke-width="1"/>'
def m_stars(x, y, s=1, **k):
    r = rr(int(x + y))
    return ''.join(f'<circle cx="{r.uniform(0,480):.0f}" cy="{r.uniform(0,120):.0f}" r="{r.uniform(.8,1.8):.1f}" fill="#fff7d6" opacity=".9"/>' for _ in range(40))
def m_rockart(x, y, s=1, **k):
    return f'<g filter="url(#wc)">' + S(f'M{x-60*s} {y} v-{60*s} q{60*s} -{14*s} {120*s} 0 v{60*s}z', '#b08860', 1.5) + f'<g fill="none" stroke="#f3d9ae" stroke-width="{1.8*s}" stroke-linecap="round"><path d="M{x-40*s} {y-30*s} l{8*s} -{14*s} l{8*s} {14*s} M{x-32*s} {y-40*s} v{14*s}"/><path d="M{x-6*s} {y-24*s} h{24*s} l{6*s} -{10*s} M{x-2*s} {y-24*s} v{10*s} M{x+14*s} {y-24*s} v{10*s}"/><path d="M{x+34*s} {y-40*s} l{6*s} -{8*s} l{6*s} {8*s}"/></g></g>'
MOTIFS = {k[2:]: v for k, v in globals().items() if k.startswith('m_')}

def person(t='adult', x=240, y=240, s=1, pose='stand', flip=False, back=False, hat=None, step=0):
    sc = {'child': .7, 'adult': 1, 'scientist': 1, 'elder': .95}.get(t, 1) * s
    g = prof(x, y, sc, pose, flip, back, step)
    if hat and not back:
        g += f'<g transform="translate({x} {y}) scale({-sc if flip else sc} {sc})">' + headgear(0, -101, hat) + '</g>'
    return shadow(x, y, 26 * sc, 4) + g

def scene(spec):
    bg = spec.get('bg', 'day'); gnd = spec.get('ground', 'sand'); hz = spec.get('horizon', 150)
    out = f'<rect width="480" height="270" fill="{SKY.get(bg, SKY["day"])}"/>'
    if bg == 'night': out += m_stars(1, 1) + m_moon(400, 50, .7)
    if bg in ('sunset', 'dusk'): out += f'<circle cx="240" cy="{hz}" r="90" fill="url(#gGlow)"/>' + clouds([(90, 70, 70), (380, 60, 80)])
    if bg == 'day': out += clouds([(380, 30, 60), (120, 24, 50)], '#ffffff', .8)
    if spec.get('sun'): out += m_sun(*spec['sun'][:2], spec['sun'][2] if len(spec['sun']) > 2 else 1)
    for e in spec.get('back', []): out += MOTIFS[e['t']](e['x'], e['y'], e.get('s', 1), flip=e.get('flip', False))
    if gnd != 'none':
        out += f'<rect y="{hz}" width="480" height="{270-hz}" fill="{GROUND[gnd]}" filter="url(#wc)"/>'
        if gnd == 'salt': out += cracks(hz)
        if gnd in ('sea', 'lagoon'): out += ''.join(f'<path d="M{20+i*60} {hz+20+(i%3)*30} q10 -4 20 0" fill="none" stroke="#dff3f8" stroke-width="1.4" opacity=".7"/>' for i in range(8))
        if gnd == 'lava': out += ''.join(f'<path d="M{i*48} {hz+30+(i%2)*40} l16 10 l-10 14" fill="none" stroke="#1a1310" stroke-width="1.2" opacity=".6"/>' for i in range(10))
        if gnd == 'green': out += ''.join(m_grass(30 + i*52, hz + 30 + (i%3)*35, .7) for i in range(9))
    for e in spec.get('el', []): out += MOTIFS[e['t']](e['x'], e['y'], e.get('s', 1), flip=e.get('flip', False))
    for p in spec.get('people', []): out += person(p.get('t', 'adult'), p.get('x', 240), p.get('y', 240), p.get('s', 1), p.get('pose', 'stand'), p.get('flip', False), p.get('back', False), p.get('hat'), p.get('step', 0))
    for e in spec.get('front', []): out += MOTIFS[e['t']](e['x'], e['y'], e.get('s', 1), flip=e.get('flip', False))
    if spec.get('bubble'):  # thought bubble with a smaller scene inside (top-right)
        out += '<g filter="url(#wc)">' + S('M250 30 Q250 8 300 10 Q350 2 400 12 Q450 10 456 40 Q470 70 450 96 Q446 122 400 120 Q350 130 300 122 Q250 126 244 100 Q226 70 250 30Z', '#fbf6ec', 1.8) + '</g>'
        out += f'<circle cx="236" cy="140" r="8" fill="#fbf6ec" stroke="{INK}" stroke-width="1.3"/><circle cx="222" cy="156" r="5" fill="#fbf6ec" stroke="{INK}" stroke-width="1.2"/>'
        inner = spec['bubble']; out += f'<g clip-path="url(#bubK)" transform="translate(236 12) scale(.46)">' + scene({**inner, 'bubble': None}).split('>', 1)[1].rsplit('</svg>', 1)[0] + '</g>'
    return f'<svg viewBox="0 0 480 270" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{out}{paper()}</svg>'

BUBBLE_CLIP = '<clipPath id="bubK"><path d="M30 40 Q30 -8 140 -4 Q250 -22 360 0 Q470 -4 480 60 Q508 128 468 184 Q458 240 360 236 Q250 258 140 240 Q30 248 18 192 Q-20 128 30 40Z"/></clipPath>'
if __name__ == '__main__':
    demo = [
        dict(bg='sunset', ground='sand', horizon=150, el=[{'t': 'tower', 'x': 340, 'y': 190, 's': 1.1}, {'t': 'dune', 'x': 80, 'y': 200, 's': .7}], people=[{'t': 'child', 'x': 140, 'y': 250, 'pose': 'point', 'hat': 'sh'}, {'t': 'adult', 'x': 200, 'y': 256, 'pose': 'stand', 'hat': 'gh'}]),
        dict(bg='day', ground='sea', horizon=120, back=[{'t': 'dhow', 'x': 380, 'y': 130, 's': .8}], el=[{'t': 'coral', 'x': 120, 'y': 250, 's': 1.3}, {'t': 'fish', 'x': 200, 'y': 200}, {'t': 'turtle', 'x': 300, 'y': 220, 's': 1.4}, {'t': 'fish', 'x': 400, 'y': 240, 'flip': True}]),
        dict(bg='night', ground='lava', horizon=160, el=[{'t': 'volcano', 'x': 360, 'y': 180, 's': 1}, {'t': 'lavatube', 'x': 110, 'y': 250, 's': 1}], people=[{'t': 'scientist', 'x': 250, 'y': 258, 'pose': 'think'}]),
        dict(bg='day', ground='green', horizon=140, el=[{'t': 'mangrove', 'x': 90, 'y': 230, 's': 1.2}, {'t': 'flamingo', 'x': 220, 'y': 240}, {'t': 'flamingo', 'x': 260, 'y': 250, 'flip': True}, {'t': 'bird', 'x': 380, 'y': 60}, {'t': 'bird', 'x': 410, 'y': 48, 's': .8}, {'t': 'mangrove', 'x': 400, 'y': 250, 's': 1}]),
        dict(bg='day', ground='rock', horizon=150, el=[{'t': 'crater', 'x': 240, 'y': 200, 's': 1.3}], people=[{'t': 'adult', 'x': 60, 'y': 262, 'pose': 'point', 'hat': 'gh'}]),
        dict(bg='dusk', ground='sand', horizon=160, el=[{'t': 'tomb', 'x': 120, 'y': 220}, {'t': 'tomb', 'x': 200, 'y': 232, 's': .8}, {'t': 'oryx', 'x': 380, 'y': 240, 's': 1.1}, {'t': 'gazelle', 'x': 300, 'y': 250, 's': .8, 'flip': True}]),
        dict(bg='wall', ground='floor', horizon=200, el=[{'t': 'lab', 'x': 150, 'y': 200}, {'t': 'map', 'x': 380, 'y': 190}], people=[{'t': 'scientist', 'x': 290, 'y': 266, 'pose': 'lecture', 'flip': True}]),
        dict(bg='day', ground='sand', horizon=150, el=[{'t': 'oasis', 'x': 240, 'y': 240, 's': 1.1}, {'t': 'well', 'x': 60, 'y': 250}, {'t': 'camel', 'x': 420, 'y': 250, 's': .9, 'flip': True}]),
        dict(bg='day', ground='salt', horizon=140, el=[{'t': 'fort', 'x': 150, 'y': 200, 's': .9}, {'t': 'house', 'x': 380, 'y': 220, 's': .9}, {'t': 'jar', 'x': 260, 'y': 250}, {'t': 'coins', 'x': 300, 'y': 252}], people=[{'t': 'child', 'x': 220, 'y': 258, 'pose': 'kneel'}]),
        dict(bg='cave', ground='cave', horizon=170, el=[{'t': 'rockart', 'x': 160, 'y': 200, 's': 1.2}, {'t': 'fossil', 'x': 380, 'y': 230, 's': 1.2}, {'t': 'footprints', 'x': 280, 'y': 250, 's': .8}], people=[{'t': 'adult', 'x': 420, 'y': 266, 'pose': 'point', 'flip': True}]),
        dict(bg='day', ground='sand', horizon=150, el=[{'t': 'cliff', 'x': 300, 'y': 190, 's': 1}, {'t': 'oilwell', 'x': 80, 'y': 230}], people=[{'t': 'scientist', 'x': 170, 'y': 262, 'pose': 'kneel'}], bubble=dict(bg='sunset', ground='sea', horizon=140, el=[{'t': 'whale', 'x': 240, 'y': 200, 's': 1.4}])),
        dict(bg='day', ground='lagoon', horizon=130, el=[{'t': 'whale', 'x': 200, 'y': 220, 's': 1.3}, {'t': 'dhow', 'x': 400, 'y': 150, 's': .7}, {'t': 'bird', 'x': 100, 'y': 50}], people=[]),
    ]
    html = '<body style="margin:0;background:#eee;display:grid;grid-template-columns:repeat(3,480px);gap:8px"><svg width="0" height="0"><defs>' + DEFS + BUBBLE_CLIP + '</defs></svg>' + ''.join(f'<div class="art">{scene(d)}</div>' for d in demo) + '</body>'
    html = '<style>.art .rise{animation:none}</style>' + html
    open('/tmp/w/layers/kit_test.html', 'w').write(html)
