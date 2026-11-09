"""Hero scene: strata building from the bottom — 4 geological, 2 archaeological, 1 ecological surface with life rising."""
import math, random, json

COL = ['#efd09e', '#d98c5f', '#e2a36b', '#b4521c', '#8a3b1e', '#2c6e72', '#5b2a17']  # top -> bottom: the logo's own band colours
INK = '#3a1d10'; CREAM = '#fff4e0'

def wave(W, y, A, lam, ph, step):
    return [(x, y + A * math.sin(2 * math.pi * x / lam + ph) + A * .12 * math.sin(2 * math.pi * x / (lam * .43) + ph * 1.7)) for x in range(-20, int(W) + 21, step)]

def yat(line, x):
    for (x1, y1), (x2, y2) in zip(line, line[1:]):
        if x1 <= x <= x2: return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return line[-1][1]

def scene(W, H, mob=False):
    ys = H * .30          # surface line
    th = [.115, .115, .115, .16, .16, .16, .17]  # band thickness fractions (top->bottom)
    tot = sum(th); bh = [(H - ys) * t / tot for t in th]
    # long, deep, phase-shifted waves like the logo's bands (each band swells and pinches)
    A = (H - ys) / 7 * .42; lam = W * (1.05 if not mob else 1.25); step = 10 if not mob else 6
    lines = []; y = ys
    for i in range(8):
        lines.append(wave(W, y, A * (.8 if i == 0 else 1), lam, .9 + i * .95, step))
        if i < 7: y += bh[i]
    out = []
    # bands (bottom first so animation order matches; draw order top-down so upper bands sit above)
    bands = []
    for i in range(7):
        top = lines[i]; bot = lines[i + 1] if i < 6 else [(x, H + 40) for x, _ in lines[i + 1]]
        d = 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in top) + 'L' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in reversed(bot)) + 'Z'
        bands.append(d)
    rng = random.Random(7)
    def mid(i, x):  # vertical centre of band i at x
        return (yat(lines[i], x) + (yat(lines[i + 1], x) if i < 6 else H)) / 2
    feats = {i: [] for i in range(7)}
    s = min(bh[3], W * .06) * (1.4 if not mob else 1.1)  # feature scale
    _bw = W * (.028 if not mob else .05); _fs = max(13, _bw * .5) if not mob else 9.5
    LZ = W * .012 + _bw * 1.35 + _fs * .6 * len('Archaeological') + _fs * 1.2 + s * .45   # keep icons clear of the layer labels
    xs = lambda fr: [W * f for f in fr if W * f >= LZ]
    # --- geological (bands 3..6) ---
    # 6 bottom: ammonites + crystals
    for x in xs([.12, .5, .86] if not mob else [.2, .72]):
        y = mid(6, x); r = s * .32
        pts = [(x + math.cos(t) * r * t / 12.6, y + math.sin(t) * r * t / 12.6) for t in [k * .25 for k in range(1, 51)]]
        sp = f'M{x:.1f} {y:.1f}' + ''.join(f'L{px:.1f} {py:.1f}' for px, py in pts)
        ribs = ''.join(f'<path d="M{x + math.cos(t)*r*.45:.1f} {y + math.sin(t)*r*.45:.1f}L{x + math.cos(t)*r:.1f} {y + math.sin(t)*r:.1f}" stroke="{CREAM}" stroke-width="1" opacity=".7"/>' for t in [k * .52 for k in range(12)])
        feats[6].append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#8c6a50" stroke="{CREAM}" stroke-width="1.8"/>{ribs}<path d="{sp}" fill="none" stroke="{CREAM}" stroke-width="1.8" stroke-linecap="round"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r*.12:.1f}" fill="{CREAM}"/>')
    for x in xs([.32, .7] if not mob else [.46]):
        y = mid(6, x) + s * .05; c = ''
        for j, (dx, hh) in enumerate([(-.18, .5), (0, .7), (.17, .45)]):
            cx = x + dx * s; top = y + s*(.25-hh-.12)
            c += (f'<path d="M{cx - s*.08:.1f} {y + s*.25:.1f}L{cx - s*.08:.1f} {y + s*(.25-hh):.1f}L{cx:.1f} {top:.1f}L{cx + s*.08:.1f} {y + s*(.25-hh):.1f}L{cx + s*.08:.1f} {y + s*.25:.1f}Z" fill="#b79ad6" stroke="{CREAM}" stroke-width="1.3" stroke-linejoin="round"/>'
                  f'<path d="M{cx:.1f} {top:.1f}L{cx:.1f} {y + s*.25:.1f}" stroke="#8a6bb5" stroke-width="1"/><path d="M{cx - s*.06:.1f} {y + s*(.25-hh*.9):.1f}L{cx - s*.02:.1f} {top + s*.05:.1f}" stroke="#f1e6ff" stroke-width="1.4" stroke-linecap="round"/>')
        feats[6].append(c)
    # 5 teal: oil drops + laminations
    for x in xs([.24, .63, .93] if not mob else [.3, .82]):
        y = mid(5, x); r = s * .16
        feats[5].append(f'<path d="M{x:.1f} {y - r*1.9:.1f}C{x + r*.2:.1f} {y - r:.1f} {x + r:.1f} {y - r*.4:.1f} {x + r:.1f} {y + r*.2:.1f}A{r:.1f} {r:.1f} 0 0 1 {x - r:.1f} {y + r*.2:.1f}C{x - r:.1f} {y - r*.4:.1f} {x - r*.2:.1f} {y - r:.1f} {x:.1f} {y - r*1.9:.1f}Z" fill="#1a2a2b" stroke="{CREAM}" stroke-width="1.4"/><ellipse cx="{x - r*.4:.1f}" cy="{y - r*.1:.1f}" rx="{r*.18:.1f}" ry="{r*.3:.1f}" fill="#fff" opacity=".55"/>')
    lam5 = ''.join(f'<path d="M{x0:.1f} {mid(5, x0) + s*.32:.1f}h{W*.12:.1f}" stroke="{CREAM}" stroke-opacity=".35" stroke-width="1.5" stroke-dasharray="10 8"/>' for x0 in xs([.05, .38, .74]))
    feats[5].append(lam5)
    # 4: bivalve shells
    for x in xs([.18, .45, .78] if not mob else [.16, .6]):
        y = mid(4, x) + s * .08; r = s * .26
        rays = ''.join(f'<path d="M{x:.1f} {y + r*.25:.1f}Q{x + math.cos(a)*r*.5:.1f} {y - math.sin(a)*r*.3:.1f} {x + math.cos(a)*r*.97:.1f} {y - math.sin(a)*r*.82:.1f}" fill="none" stroke="{CREAM}" stroke-width="1.1" opacity=".85"/>' for a in [math.pi*k/9 for k in range(1, 9)])
        feats[4].append(f'<path d="M{x - r:.1f} {y:.1f}A{r:.1f} {r*.85:.1f} 0 0 1 {x + r:.1f} {y:.1f}L{x:.1f} {y + r*.25:.1f}Z" fill="#e2b48c" stroke="{CREAM}" stroke-width="1.5" stroke-linejoin="round"/>{rays}<path d="M{x - r*.5:.1f} {y + r*.05:.1f}Q{x:.1f} {y + r*.35:.1f} {x + r*.5:.1f} {y + r*.05:.1f}" fill="none" stroke="{CREAM}" stroke-width="1"/>')
    # 3: pebbles + fossil fish
    for k in range(14 if not mob else 7):
        x = rng.uniform(.03, .97) * W; y = mid(3, x) + rng.uniform(-.25, .25) * bh[3]
        feats[3].append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{s*rng.uniform(.05,.1):.1f}" ry="{s*.05:.1f}" fill="#efc7a0" opacity=".8"/>')
    for x in xs([.6] if not mob else [.78]):
        y = mid(3, x); r = s * .35
        bones = ''.join(f'<path d="M{x - r*.55 + i*r*.17:.1f} {y - r*.22:.1f}V{y + r*.22:.1f}" stroke="{CREAM}" stroke-width="1" opacity=".8"/>' for i in range(6))
        feats[3].append(f'<path d="M{x - r:.1f} {y:.1f}Q{x:.1f} {y - r*.55:.1f} {x + r*.6:.1f} {y:.1f}Q{x:.1f} {y + r*.55:.1f} {x - r:.1f} {y:.1f}Z" fill="#c99a70" fill-opacity=".35" stroke="{CREAM}" stroke-width="1.6" stroke-linejoin="round"/><path d="M{x + r*.6:.1f} {y:.1f}L{x + r:.1f} {y - r*.35:.1f}L{x + r:.1f} {y + r*.35:.1f}Z" fill="#c99a70" fill-opacity=".35" stroke="{CREAM}" stroke-width="1.4"/><path d="M{x - r*.6:.1f} {y:.1f}H{x + r*.5:.1f}" stroke="{CREAM}" stroke-width="1.3"/>{bones}<circle cx="{x - r*.72:.1f}" cy="{y - r*.08:.1f}" r="{r*.07:.1f}" fill="{CREAM}"/><path d="M{x - r*.3:.1f} {y - r*.3:.1f}Q{x - r*.1:.1f} {y - r*.6:.1f} {x + r*.1:.1f} {y - r*.3:.1f}" fill="none" stroke="{CREAM}" stroke-width="1.2"/>')
    # fault across geological bands
    fx = W * (.42 if not mob else .5)
    fault = f'<path d="M{fx:.1f} {yat(lines[3], fx):.1f}L{fx + s*.6:.1f} {H:.1f}" stroke="{INK}" stroke-width="2.4" stroke-dasharray="7 5" opacity=".55"/>'
    # --- archaeological (bands 1,2) ---
    for x in xs([.16, .55, .9] if not mob else [.22, .74]):
        y = mid(2, x); r = s * .2
        feats[2].append(f'<path d="M{x - r*.4:.1f} {y - r*1.35:.1f}H{x + r*.4:.1f}L{x + r*.28:.1f} {y - r*.95:.1f}Q{x + r*1.1:.1f} {y - r*.4:.1f} {x + r*.7:.1f} {y + r*.6:.1f}L{x:.1f} {y + r*1.5:.1f}L{x - r*.7:.1f} {y + r*.6:.1f}Q{x - r*1.1:.1f} {y - r*.4:.1f} {x - r*.28:.1f} {y - r*.95:.1f}Z" fill="#c2622a" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/><path d="M{x - r*.28:.1f} {y - r*.9:.1f}Q{x - r*.95:.1f} {y - r*.9:.1f} {x - r*.85:.1f} {y - r*.2:.1f}M{x + r*.28:.1f} {y - r*.9:.1f}Q{x + r*.95:.1f} {y - r*.9:.1f} {x + r*.85:.1f} {y - r*.2:.1f}" fill="none" stroke="{INK}" stroke-width="1.5"/><path d="M{x - r*.75:.1f} {y - r*.2:.1f}Q{x:.1f} {y - r*.05:.1f} {x + r*.75:.1f} {y - r*.2:.1f}M{x - r*.6:.1f} {y + r*.2:.1f}Q{x:.1f} {y + r*.35:.1f} {x + r*.6:.1f} {y + r*.2:.1f}" fill="none" stroke="#f3d9ae" stroke-width="1.2"/>')
    for x in xs([.36, .76] if not mob else [.48]):
        y = mid(2, x); r = s * .13
        coin = lambda cx, cy, rr: f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rr:.1f}" fill="#d9ab3c" stroke="{INK}" stroke-width="1.4"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rr*.68:.1f}" fill="none" stroke="{INK}" stroke-width=".9" opacity=".7"/><path d="M{cx - rr*.3:.1f} {cy + rr*.25:.1f}L{cx:.1f} {cy - rr*.3:.1f}L{cx + rr*.3:.1f} {cy + rr*.25:.1f}" fill="none" stroke="{INK}" stroke-width="1"/>'
        feats[2].append(coin(x, y, r) + coin(x + r*2.3, y + r*.45, r*.82))
    for x in xs([.27, .68] if not mob else [.36, .86]):
        y = mid(1, x) + bh[1] * .1; w = s * .26; c = ''
        for row in range(2):
            for col in range(3 - row):
                bx = x - w * 1.5 + col * w + row * w * .5; by = y - row * w * .55
                c += f'<rect x="{bx:.1f}" y="{by - w*.5:.1f}" width="{w*.96:.1f}" height="{w*.52:.1f}" rx="{w*.05:.1f}" fill="#f0d3a3" stroke="{INK}" stroke-width="1.3"/><path d="M{bx + w*.08:.1f} {by - w*.1:.1f}H{bx + w*.6:.1f}" stroke="#d9b985" stroke-width="1.2"/>'
        feats[1].append(c)
    for x in xs([.08, .47, .93] if not mob else [.1, .62]):
        y = mid(1, x); r = s * .12
        feats[1].append(f'<path d="M{x - r:.1f} {y:.1f}L{x:.1f} {y - r*.9:.1f}L{x + r*1.3:.1f} {y - r*.15:.1f}L{x + r*.3:.1f} {y + r*.7:.1f}Z" fill="#8f5a3a" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/><path d="M{x - r*.4:.1f} {y - r*.2:.1f}L{x + r*.5:.1f} {y - r*.1:.1f}M{x - r*.1:.1f} {y - r*.55:.1f}L{x + r*.2:.1f} {y + r*.3:.1f}" stroke="#f3d9ae" stroke-width=".9" opacity=".8"/>')
    # --- ecological surface: roots + life ---
    for x in xs([.1, .3, .52, .72, .9] if not mob else [.14, .5, .86]):
        y = yat(lines[0], x)
        feats[0].append(f'<path d="M{x:.1f} {y + 2:.1f}q-{s*.1:.1f} {s*.25:.1f} -{s*.25:.1f} {s*.35:.1f}M{x:.1f} {y + 2:.1f}q{s*.08:.1f} {s*.3:.1f} {s*.22:.1f} {s*.42:.1f}" fill="none" stroke="#4d6b38" stroke-width="1.6" opacity=".7"/>')
    life = []
    def grow(svg, x, y, d):
        life.append(f'<g class="gr" style="transform-origin:{x:.1f}px {y:.1f}px;animation-delay:{d:.2f}s"><g class="sw" style="transform-origin:{x:.1f}px {y:.1f}px;animation-delay:{-d*1.3:.2f}s">{svg}</g></g>')
    pal = [.12, .83] if not mob else [.9]   # phone: the left palm is gone; the camel starts its walk from that spot
    for k, fr in enumerate(pal):
        x = W * fr; y = yat(lines[0], x); hgt = s * (1.5 if not mob else 1.35)
        fr_ = ''.join(f'<path d="M{x:.1f} {y - hgt:.1f}q{dx*s*.45:.1f} {-s*.2:.1f} {dx*s*.9:.1f} {s*.25:.1f}" fill="none" stroke="#2c7a4c" stroke-width="{s*.12:.1f}" stroke-linecap="round"/>' for dx in (-1, 1, -.7, .7))
        grow(f'<path d="M{x:.1f} {y:.1f}Q{x + s*.1:.1f} {y - hgt*.5:.1f} {x:.1f} {y - hgt:.1f}" fill="none" stroke="#7a5233" stroke-width="{s*.09:.1f}" stroke-linecap="round"/>{fr_}', x, y, 2.5 + k * .25)
    for k, fr in enumerate([.22, .38, .6, .7, .95] if not mob else [.3, .62, .76]):
        x = W * fr; y = yat(lines[0], x); hgt = s * (.55 + (k % 3) * .15)
        blades = ''.join(f'<path d="M{x:.1f} {y:.1f}Q{x + dx*s*.08:.1f} {y - hgt*.6:.1f} {x + dx*s*.18:.1f} {y - hgt:.1f}" fill="none" stroke="#3f8a4f" stroke-width="{s*.05:.1f}" stroke-linecap="round"/>' for dx in (-1.2, -.4, .4, 1.2))
        flw = f'<circle cx="{x + s*.18:.1f}" cy="{y - hgt:.1f}" r="{s*.07:.1f}" fill="#f6c24a"/>' if k % 2 == 0 else f'<circle cx="{x - s*.18:.1f}" cy="{y - hgt:.1f}" r="{s*.065:.1f}" fill="#d9643a"/>'
        grow(blades + flw, x, y, 2.75 + k * .18)
    for k, fr in enumerate([.46] if not mob else [.42]):  # mangrove
        x = W * fr; y = yat(lines[0], x); hgt = s * 1.0
        roots = ''.join(f'<path d="M{x:.1f} {y - hgt*.35:.1f}Q{x + dx*s*.2:.1f} {y - hgt*.2:.1f} {x + dx*s*.3:.1f} {y:.1f}" fill="none" stroke="#6b4a2e" stroke-width="{s*.04:.1f}"/>' for dx in (-1, -.4, .4, 1))
        grow(f'{roots}<path d="M{x:.1f} {y - hgt*.35:.1f}V{y - hgt*.75:.1f}" stroke="#6b4a2e" stroke-width="{s*.06:.1f}"/><ellipse cx="{x:.1f}" cy="{y - hgt*.9:.1f}" rx="{s*.42:.1f}" ry="{s*.24:.1f}" fill="#4f8f5a"/>', x, y, 3.0)
    birds = ''
    for k in range(0):  # birds removed: they flew behind the title and buttons
        bx = W * (.3 + k * .12); by = ys * (.25 + k * .12); r = s * .14
        birds += f'<g class="bird" style="animation-delay:{3.4 + k*.6:.2f}s"><path d="M{bx - r:.1f} {by:.1f}q{r*.5:.1f} {-r*.6:.1f} {r:.1f} 0q{r*.5:.1f} {-r*.6:.1f} {r:.1f} 0" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/></g>'
    # discipline scale bar at the left (like a geological time scale)
    bw = W * (.028 if not mob else .05); bx0 = W * .012
    segs = [('leco', 'Ecological', '#2c7a4c', yat(lines[0], bx0 + bw), yat(lines[1], bx0 + bw)),
            ('larch', 'Archaeological', '#b4521c', yat(lines[1], bx0 + bw), yat(lines[3], bx0 + bw)),
            ('lgeo', 'Geological', '#5847b0', yat(lines[3], bx0 + bw), H)]
    fsz = bw * (.55 if not mob else .48) if not mob else 9.5
    if not mob: fsz = max(13, bw * .5)
    labs = f'<g class="scale"><rect x="{bx0:.1f}" y="{segs[0][3]:.1f}" width="{bw:.1f}" height="{H - segs[0][3]:.1f}" rx="{bw*.25:.1f}" fill="#fffaf0" opacity=".92"/>'
    for key, en, col, y1, y2 in segs:
        ym = (y1 + y2) / 2; pad = bw * .18; tw = fsz * .6 * len(en) + fsz * 1.2
        labs += (f'<rect x="{bx0 + pad:.1f}" y="{y1 + pad:.1f}" width="{bw - 2*pad:.1f}" height="{y2 - y1 - 2*pad:.1f}" rx="{bw*.18:.1f}" fill="{col}"/>'
                 f'<path d="M{bx0 + bw:.1f} {ym:.1f}h{bw*.35:.1f}" stroke="{col}" stroke-width="2"/>'
                 f'<rect x="{bx0 + bw*1.35:.1f}" y="{ym - fsz*.8:.1f}" width="{tw:.1f}" height="{fsz*1.6:.1f}" rx="{fsz*.8:.1f}" fill="#fffaf0" opacity=".92"/>'
                 f'<text data-i="{key}" x="{bx0 + bw*1.35 + tw/2:.1f}" y="{ym + fsz*.36:.1f}" text-anchor="middle" font-size="{fsz:.1f}" fill="{col}" font-family="Instrument Sans,system-ui,sans-serif" font-weight="700" letter-spacing="{fsz*.04:.1f}">{en}</text>')
    labs += '</g>'
    # the camel walks slowly along the surface line itself (feet follow the ground)
    LP = json.load(open('/tmp/w/layers/logo_parts.json'))
    cs = (bh[0] * (1.0 if not mob else .95)) / (340 * .86)
    x0 = W * .1 if mob else lines[0][0][0]   # phone: start where the left palm used to stand
    walk = [(x0, yat(lines[0], x0))] + [(x, y) for x, y in lines[0] if x > x0]
    surf = 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in walk)
    dur = (90 if not mob else 55) * (lines[0][-1][0] - x0) / (lines[0][-1][0] - lines[0][0][0])   # same walking speed as before
    camel = (f'<g class="walk"><g><g transform="scale({cs:.4f})">{LP["camel"]}</g>'
             f'<animateMotion dur="{dur:.1f}s" begin="{4.5 if mob else 0}s" repeatCount="indefinite" path="{surf}"/></g></g>')   # 4.5s = when the camel fades in
    # assemble: bottom band rises first
    g = ''
    order = list(range(6, -1, -1))
    delay = {i: .15 + n * .28 for n, i in enumerate(order)}
    for i in range(7):
        g += f'<g class="band" style="animation-delay:{delay[i]:.2f}s"><path d="{bands[i]}" fill="{COL[i]}"/><g class="ft" style="animation-delay:{delay[i] + .55:.2f}s">{"".join(feats[i])}</g></g>'
    g = f'<g class="bands">{g}</g>' + labs + f'<g class="ft" style="animation-delay:1.4s">{fault}</g>' + ''.join(life) + birds + camel
    return f'<svg class="scene {"sm" if mob else "lg"}" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMax slice" aria-hidden="true">{g}</svg>'

if __name__ == '__main__':
    open('/tmp/w/layers/scene_test.html', 'w').write('<body style="margin:0;background:#fbeedb">' + scene(1600, 560) + '<br>' + scene(420, 400, True) + '</body>')
