"""Paper-cut children's painting for Explorer mode: soft vertical rainbow stripes, paper dots, a paper plane, a sun with cut rays, paper clouds along the bottom."""
import math, random, urllib.parse
STRIPES = ['#f6d6a8', '#bde6b5', '#aed6f2', '#cfc0ee', '#f2b8dc', '#f3aca6', '#f6d6a8', '#bde6b5', '#aed6f2', '#cfc0ee', '#f2b8dc', '#f3aca6']
def shade(hexc, k=.9):
    r, g, b = int(hexc[1:3], 16), int(hexc[3:5], 16), int(hexc[5:7], 16)
    return '#%02x%02x%02x' % (int(r * k), int(g * k), int(b * k))
def sun(x, y, r, n=18):
    pts = []
    for k in range(2 * n):
        a = k * math.pi / n; rr = r * 1.45 if k % 2 == 0 else r * 1.12
        pts.append(f'{x + math.cos(a)*rr:.1f} {y + math.sin(a)*rr:.1f}')
    return (f'<path d="M{"L".join(pts)}Z" fill="#f3cf86"/><path d="M{"L".join(pts)}Z" fill="#000" opacity=".06" transform="translate(3 5)"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f6d898"/><circle cx="{x}" cy="{y}" r="{r*.8:.0f}" fill="#f9e3ad"/>')
def cloud(x, y, s, col='#fff', op=1):
    return (f'<g transform="translate({x} {y}) scale({s})" opacity="{op}"><ellipse cx="0" cy="24" rx="150" ry="36" fill="#000" opacity=".07"/>'
            f'<ellipse cx="0" cy="0" rx="150" ry="52" fill="{col}"/><circle cx="-80" cy="-24" r="48" fill="{col}"/><circle cx="-10" cy="-48" r="64" fill="{col}"/><circle cx="70" cy="-28" r="52" fill="{col}"/><circle cx="125" cy="4" r="36" fill="{col}"/></g>')
def plane(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate(-12)"><path d="M0 0L120 -30L40 20Z" fill="#f4f6fa"/><path d="M40 20L120 -30L58 4Z" fill="#d9e0ea"/><path d="M0 0L58 4L40 20Z" fill="#eaeef4"/>'
            f'<path d="M0 0L120 -30L40 20Z" fill="#000" opacity=".06" transform="translate(4 7)"/></g>')
def paint(W, H, n, seed, dots, clouds, plane_s, sun_r):
    rng = random.Random(seed); sw = W / n; g = ''
    for i in range(n):
        c = STRIPES[i % len(STRIPES)]; x = i * sw
        g += f'<rect x="{x:.1f}" y="0" width="{sw+1:.1f}" height="{H}" fill="{c}"/><rect x="{x:.1f}" y="0" width="{sw*.08:.1f}" height="{H}" fill="{shade(c,.93)}"/>'
    for _ in range(dots):
        x, y, r = rng.uniform(0, W), rng.uniform(0, H * .72), rng.uniform(W * .004, W * .014)
        g += f'<circle cx="{x+r*.3:.1f}" cy="{y+r*.5:.1f}" r="{r:.1f}" fill="#000" opacity=".07"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#f6f7fb"/>'
    if sun_r: g += sun(W * .83, H * .2, sun_r)
    if plane_s: g += plane(W * .07, H * .3, plane_s)
    for (fx, fy, s, col) in clouds: g += cloud(W * fx, H * fy, s, col)
    return g
def star(x, y, r, col='#fff', op=.95):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5; rr = r if k % 2 == 0 else r * .5
        pts.append(f'{x + math.cos(a)*rr:.1f} {y + math.sin(a)*rr:.1f}')
    return f'<path d="M{"L".join(pts)}Z" fill="{col}" opacity="{op}"/>'
def wave(W, y, A, lam, ph, step=30):
    return [(x, y + A * math.sin(2 * math.pi * x / lam + ph)) for x in range(-30, W + 61, step)]
def rainbow_arc(x, y, r, w):
    cols = ['#f6a9a0', '#f8c98f', '#f8e59a', '#bfe3b0', '#aed6f2', '#cfc0ee']
    g = ''
    for i, c in enumerate(cols):
        rr = r - i * w
        g += f'<path d="M{x-rr:.0f} {y}A{rr:.0f} {rr:.0f} 0 0 1 {x+rr:.0f} {y}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    return g
def sky(W=1200, H=1000, seed=3):
    """Paper-cut sky: teal gradient, sparse stars, paper clouds hanging in the corners, soft wavy rainbow ground at the bottom with clouds over it."""
    rng = random.Random(seed)
    g = (f'<defs><linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9e2ea"/><stop offset=".6" stop-color="#d8eff3"/><stop offset="1" stop-color="#eef7f8"/></linearGradient></defs>'
         f'<rect width="{W}" height="{H}" fill="url(#s)"/>')
    for _ in range(70):
        x, y = rng.uniform(0, W), rng.uniform(0, H * .72); r = rng.uniform(3, 9)
        g += star(x, y, r, '#fff', .9) if rng.random() < .45 else f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r*.4:.1f}" fill="#fff" opacity=".85"/>'
    # soft wavy rainbow ground
    y = H * .74; lines = []
    PAST = ['#f7b7c7', '#fbd1b3', '#fbe9a6', '#c9ecb6', '#b4dcf6', '#d8c7f3', '#f7b7c7']
    for i in range(8): lines.append(wave(W, y, 22, W * .95, .6 + i * .7)); y += H * .3 / 7
    for i in range(7):
        bot = lines[i + 1] if i < 6 else [(x, H + 60) for x, _ in lines[i + 1]]
        d = 'M' + 'L'.join(f'{x:.0f} {yy:.0f}' for x, yy in lines[i]) + 'L' + 'L'.join(f'{x:.0f} {yy:.0f}' for x, yy in reversed(bot)) + 'Z'
        g += f'<path d="{d}" fill="{PAST[i]}"/>'
    for _ in range(50):
        x, yy = rng.uniform(0, W), rng.uniform(H * .74, H); g += star(x, yy, rng.uniform(4, 9)) if rng.random() < .6 else f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="{rng.uniform(2,4):.1f}" fill="#fff" opacity=".9"/>'
    # clouds: hanging in the top corners, resting on the ground at the bottom
    g += cloud(W * .06, H * .05, 1.0, '#f4f7fb') + cloud(W * .95, H * .04, 1.15, '#f4f7fb') + cloud(W * .5, H * .035, .55, '#eef3f9', .9)
    g += cloud(W * .1, H * .98, 1.2, '#ffffff') + cloud(W * .42, H * 1.02, 1.3, '#ffffff') + cloud(W * .74, H * .99, 1.1, '#ffffff') + cloud(W * 1.0, H * 1.03, 1.2, '#ffffff')
    g += cloud(W * .27, H * .94, .7, '#dfeaf5') + cloud(W * .6, H * .95, .8, '#dfeaf5') + cloud(W * .9, H * .93, .7, '#dfeaf5')
    # a small hanging rainbow with a star, top right
    g += f'<line x1="{W*.93:.0f}" y1="{H*.07:.0f}" x2="{W*.93:.0f}" y2="{H*.17:.0f}" stroke="#fff" stroke-width="2" opacity=".8"/>' + rainbow_arc(W * .93, H * .2, 46, 7) + star(W * .87, H * .19, 14, '#fbd34d', 1)
    g += sun(W * .83, H * .2, 0) if False else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">{g}</svg>'
def button(W=240, H=60, seed=5):
    cl = [(.5, .95, .22, '#c6dcef'), (.15, 1.05, .16, '#eef2f8'), (.85, 1.02, .18, '#eef2f8')]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="none">{paint(W, H, 8, seed, 9, cl, .22, 0)}</svg>'
def uri(svg): return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe="/:=;,() '") + '")'
if __name__ == '__main__':
    open('/tmp/w/layers/kid_test.html', 'w').write(f'<body style="margin:0"><div style="width:1200px;height:700px">{sky()}</div><div style="width:240px;height:60px;margin:10px;border-radius:999px;background:{uri(button())} center/100% 100%"></div><div style="width:120px;height:36px;margin:10px;border-radius:999px;background:{uri(button())} center/100% 100%"></div></body>')
