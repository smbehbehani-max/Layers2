"""Sticker-style cartoon icons for Explorer mode (thick rounded outline, pastel fills, highlights) + decorations around the map."""
O = '#4a3350'  # outline
def S(body, rot=-6):
    return f'<svg viewBox="0 0 48 48" aria-hidden="true"><g transform="rotate({rot} 24 24)" stroke="{O}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>'
ICONS = {
 'map': S('<path d="M8 14l10-4 12 4 10-4v24l-10 4-12-4-10 4z" fill="#bfe3b5"/><path d="M18 10v24M30 14v24" fill="none"/><path d="M12 30c4-6 8-4 10 0" fill="none" stroke="#5a9bd5"/><circle cx="35" cy="20" r="4" fill="#f4a9a0"/><circle cx="35" cy="20" r="1.3" fill="#fff" stroke="none"/>'),
 'tl': S('<circle cx="24" cy="26" r="15" fill="#fbe7a1"/><circle cx="24" cy="26" r="11" fill="#fff8df"/><path d="M24 18v8l5 3" fill="none" stroke-width="3"/><path d="M19 9l5-4 5 4" fill="none"/><circle cx="20" cy="24" r="1.2" fill="#4a3350" stroke="none"/><circle cx="28" cy="24" r="1.2" fill="#4a3350" stroke="none"/><path d="M21 31q3 2 6 0" fill="none"/>'),
 'cmp': S('<rect x="8" y="24" width="8" height="16" rx="3" fill="#aed6f2"/><rect x="20" y="12" width="8" height="28" rx="3" fill="#f2b8dc"/><rect x="32" y="18" width="8" height="22" rx="3" fill="#bfe3b5"/><path d="M24 6l1.5 3 3 .4-2.2 2.1.6 3-2.9-1.6-2.9 1.6.6-3L19 9.4l3-.4z" fill="#ffd33d"/>'),
 'inno': S('<path d="M24 6a12 12 0 0 0-7 21.6V32h14v-4.4A12 12 0 0 0 24 6z" fill="#ffe08a"/><rect x="18" y="33" width="12" height="7" rx="3" fill="#cfc0ee"/><path d="M20 19q4 3 8 0" fill="none"/><circle cx="20" cy="16" r="1.2" fill="#4a3350" stroke="none"/><circle cx="28" cy="16" r="1.2" fill="#4a3350" stroke="none"/><path d="M38 8l2 0M39 6l0 4M8 12l3 0" stroke="#f4a823"/>'),
 'about': S('<path d="M10 10h28a4 4 0 0 1 4 4v16a4 4 0 0 1-4 4H22l-8 7v-7h-4a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="#aed6f2"/><circle cx="24" cy="16" r="2" fill="#4a3350" stroke="none"/><path d="M24 21v8" stroke-width="3.2"/>'),
 'how': S('<circle cx="20" cy="26" r="9" fill="#f6d6a8"/><circle cx="20" cy="26" r="3" fill="#fff"/><path d="M20 13v4M20 35v4M7 26h4M29 26h4M11 17l3 3M26 32l3 3M11 35l3-3M26 20l3-3" stroke-width="3"/><circle cx="36" cy="14" r="5" fill="#bfe3b5"/><path d="M36 6v3M36 19v3M28 14h3M41 14h3" stroke-width="2.4"/>'),
 'inst': S('<rect x="13" y="6" width="22" height="36" rx="5" fill="#f2b8dc"/><rect x="16" y="10" width="16" height="24" rx="2" fill="#fff8df"/><path d="M24 14v12M19 22l5 5 5-5" fill="none" stroke-width="3"/><circle cx="24" cy="38" r="1.6" fill="#4a3350" stroke="none"/>'),
 'intro': S('<rect x="7" y="12" width="34" height="26" rx="5" fill="#cfc0ee"/><path d="M7 18h34M12 12l4 6M20 12l4 6M28 12l4 6" fill="none"/><path d="M20 23l9 5-9 5z" fill="#fff"/>'),
 'tla': S('<path d="M12 40V22l12-10 12 10v18z" fill="#f6d6a8"/><rect x="20" y="28" width="8" height="12" rx="2" fill="#fff"/><path d="M8 24l16-14 16 14" fill="none"/>'),
}
# decorations around the map: four strips (top / bottom / left / right), hand-drawn feel
def strip(w, h, body): return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid meet" aria-hidden="true"><g fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".85">{body}</g></svg>'
def cloud(x, y, s):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-40 10q-14 0-12-12q2-14 16-10q4-14 20-8q10-10 22 2q14-4 14 12q0 16-16 16z" fill="#fff"/></g>'
def star(x, y, r):
    import math
    pts=[]
    for k in range(10):
        a=-math.pi/2+k*math.pi/5; rr=r if k%2==0 else r*.45
        pts.append(f'{x+math.cos(a)*rr:.1f} {y+math.sin(a)*rr:.1f}')
    return f'<path d="M{"L".join(pts)}Z" fill="#ffd33d"/>'
def bird(x, y, s=1): return f'<path d="M{x-10*s} {y}q{5*s} {-7*s} {10*s} 0q{5*s} {-7*s} {10*s} 0" />'
TOP = strip(1200, 120, cloud(120, 60, 1) + cloud(600, 50, .7) + cloud(1070, 66, .9) + star(300, 40, 10) + star(420, 80, 7) + star(820, 36, 9) + star(940, 84, 6) + bird(500, 90) + bird(540, 82, .8) + bird(700, 70) + f'<circle cx="360" cy="90" r="2.5" fill="{O}" stroke="none"/><circle cx="760" cy="40" r="2.5" fill="{O}" stroke="none"/>')
def palm(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0q-3-24 2-44" /><path d="M2-44q-18-10-30-2M2-44q-4-18-22-22M2-44q10-16 28-12M2-44q18-6 30 6" /></g>'
def dune(x, y, w, h): return f'<path d="M{x} {y}q{w*.3} {-h} {w*.55} 0t{w*.45} 0" fill="#fbe7a1" fill-opacity=".8"/>'
def camel(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-22 0v-14q0-10 10-10q6 0 8 6q4-6 10-4q6 2 6 10v12M-14 0v-10M10 0v-8M12-20l8-12l4 6" fill="#f6d6a8"/><circle cx="21" cy="-32" r="1.5" fill="{O}" stroke="none"/></g>'
def dhow(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-26 0h52l-8 10h-36z" fill="#f6d6a8"/><path d="M4 0v-34q22 10 24 34z" fill="#fff"/><path d="M-40 14q10-8 20 0t20 0t20 0t20 0" stroke="#5a9bd5"/></g>'
BOTTOM = strip(1200, 150, dune(0, 120, 420, 50) + dune(380, 125, 500, 60) + dune(820, 120, 400, 45) + palm(120, 118, 1) + palm(150, 122, .7) + palm(1050, 120, 1.1) + camel(520, 120) + camel(580, 124, .8) + dhow(860, 110, .9) + '<path d="M200 135q80-10 160 0t160 10t160-10t160 0" stroke-dasharray="6 7"/>' + '<path d="M300 128l6-6M300 122l6 6M700 140l6-6M700 134l6 6" />' + star(980, 60, 8) + bird(240, 50) + bird(280, 44, .8))
SIDE_L = strip(140, 800, '<path d="M70 20q-40 100 0 200t-10 220t20 200t-20 140" stroke-dasharray="7 8"/>' + star(40, 120, 9) + star(100, 300, 7) + palm(60, 520, .8) + camel(70, 700, .7) + cloud(70, 60, .5) + bird(80, 420) + '<path d="M44 460l8-8M44 452l8 8"/>')
SIDE_R = strip(140, 800, '<path d="M70 20q40 100 0 200t10 220t-20 200t20 140" stroke-dasharray="7 8"/>' + star(100, 140, 9) + star(40, 330, 7) + dhow(70, 560, .6) + cloud(70, 60, .5) + bird(60, 440) + '<path d="M96 240l8-8M96 232l8 8"/>' + palm(90, 740, .7))

def C(body, rot=-8):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><g transform="rotate({rot} 24 24)" stroke="{O}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>'
CHIP = {
 'archaeological': C('<path d="M17 12h14l-2 5q7 5 5 16q-1 7-10 7t-10-7q-2-11 5-16z" fill="#f4a9a0"/><path d="M15 22h18" stroke="#fff"/><path d="M16 28q8 3 16 0" stroke="#fff"/>'),
 'geological': C('<circle cx="24" cy="26" r="15" fill="#cfc0ee"/><path d="M24 26m-9 0a9 9 0 1 1 18 0a6 6 0 1 1-12 0a3 3 0 1 1 6 0" fill="none"/><path d="M15 26l-4 0M33 26l4 0M24 11l0 -3" stroke="#fff"/>'),
 'ecology': C('<path d="M12 36q0-20 24-24q-2 22-24 24z" fill="#bfe3b5"/><path d="M12 36q8-12 20-18" fill="none"/>'),
 'speculative': C('<path d="M24 8l3.5 10.5L38 22l-10.5 3.5L24 36l-3.5-10.5L10 22l10.5-3.5z" fill="#ffd33d"/><circle cx="37" cy="11" r="3" fill="#f2b8dc"/><circle cx="10" cy="36" r="2.5" fill="#aed6f2"/>'),
 'stories': C('<path d="M9 12h12a3 3 0 0 1 3 3v22a2 2 0 0 0-2-2H9z" fill="#aed6f2"/><path d="M39 12H27a3 3 0 0 0-3 3v22a2 2 0 0 1 2-2h13z" fill="#f6d6a8"/><path d="M12 18h7M12 23h7M29 18h7M29 23h7" stroke="#fff"/>'),
 'live': C('<circle cx="24" cy="24" r="12" fill="#bfe3b5"/><circle cx="24" cy="24" r="4" fill="#fff"/><path d="M24 6v6M24 36v6M6 24h6M36 24h6"/>'),
 'search': C('<circle cx="21" cy="21" r="11" fill="#fff8df"/><path d="M29 29l9 9" stroke-width="4"/><path d="M15 19q2-5 7-5" stroke="#fff"/>'),
 'how': C('<circle cx="24" cy="24" r="10" fill="#f6d6a8"/><circle cx="24" cy="24" r="3.5" fill="#fff"/><path d="M24 7v5M24 36v5M7 24h5M36 24h5M12 12l3.5 3.5M32.5 32.5l3.5 3.5M12 36l3.5-3.5M32.5 15.5l3.5-3.5" stroke-width="3.2"/>'),
 'inst': C('<rect x="13" y="6" width="22" height="36" rx="5" fill="#f2b8dc"/><rect x="16" y="10" width="16" height="24" rx="2" fill="#fff8df"/><path d="M24 14v12M19 22l5 5 5-5" fill="none" stroke-width="3"/>'),
 'map': C('<path d="M8 14l10-4 12 4 10-4v24l-10 4-12-4-10 4z" fill="#bfe3b5"/><path d="M18 10v24M30 14v24" fill="none"/><circle cx="35" cy="20" r="4" fill="#f4a9a0"/>'),
 'tl': C('<circle cx="24" cy="26" r="14" fill="#fbe7a1"/><path d="M24 18v8l5 3" fill="none" stroke-width="3"/><path d="M19 9l5-4 5 4" fill="none"/>'),
 'cmp': C('<rect x="8" y="24" width="8" height="16" rx="3" fill="#aed6f2"/><rect x="20" y="12" width="8" height="28" rx="3" fill="#f2b8dc"/><rect x="32" y="18" width="8" height="22" rx="3" fill="#bfe3b5"/>'),
}
import urllib.parse
def uri(svg): return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe="/:=;,() '") + '")'

# ---- mode toggle art: a science desk for Researcher (books, flask, microscope) ----
RESEARCH = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 60" preserveAspectRatio="none">'
 '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9f1fb"/><stop offset="1" stop-color="#cfdff2"/></linearGradient></defs><rect width="240" height="60" fill="url(#g)"/>'
 '<rect x="0" y="46" width="240" height="14" fill="#b9a27f"/><rect x="0" y="44" width="240" height="4" fill="#d9c7a3"/>'
 '<g stroke="#3b3550" stroke-width="1.6" stroke-linejoin="round"><rect x="12" y="28" width="9" height="18" fill="#3f7cc0"/><rect x="21" y="22" width="8" height="24" fill="#e0636a"/><rect x="29" y="30" width="10" height="16" fill="#f2b84b"/><rect x="39" y="26" width="7" height="20" fill="#5aa469"/>'
 '<path d="M62 16h10v10l8 16q2 4-2 4H56q-4 0-2-4l8-16z" fill="#bfe6f4"/><path d="M58 40h20" stroke="#5aa4d6"/><path d="M60 38q8-4 16 0v4q-4 4-16 0z" fill="#7ad0e8" stroke="none"/>'
 '<path d="M196 46h30M202 46l6-16l12-6" fill="none" stroke-width="3"/><path d="M214 28l6-9l6 4l-5 9z" fill="#8a94a6"/><circle cx="208" cy="31" r="5" fill="#cfd6e2"/><rect x="200" y="42" width="28" height="5" rx="2" fill="#5b6475"/>'
 '<path d="M140 46l4-24h26l4 24z" fill="#f6efe0"/><path d="M148 28h18M147 34h20M146 40h22" stroke="#9aa0ad"/><path d="M118 46V22l12 6l12-6v24z" fill="#f9d77b"/></g>'
 '<circle cx="100" cy="12" r="2" fill="#fff"/><circle cx="180" cy="10" r="1.6" fill="#fff"/><circle cx="130" cy="8" r="1.4" fill="#fff"/></svg>')
# ---- day / night switch (sky with clouds ↔ night with stars; sun ↔ moon knob) ----
DAY = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 34" preserveAspectRatio="none"><defs><linearGradient id="s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5d8fcf"/><stop offset="1" stop-color="#9ec3ea"/></linearGradient></defs><rect width="72" height="34" rx="17" fill="url(#s)"/>'
 '<g fill="#fff"><circle cx="48" cy="28" r="9" opacity=".7"/><circle cx="58" cy="24" r="10"/><circle cx="68" cy="30" r="9"/><circle cx="40" cy="33" r="8" opacity=".8"/><circle cx="52" cy="14" r="5" opacity=".35"/><circle cx="62" cy="10" r="6" opacity=".35"/></g></svg>')
NIGHT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 34" preserveAspectRatio="none"><defs><linearGradient id="n" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1b1d2e"/><stop offset="1" stop-color="#3a3f58"/></linearGradient></defs><rect width="72" height="34" rx="17" fill="url(#n)"/>'
 '<g fill="#fff"><path d="M14 8l1.2 2.8L18 12l-2.8 1.2L14 16l-1.2-2.8L10 12l2.8-1.2z"/><path d="M28 20l.9 2.1l2.1.9l-2.1.9l-.9 2.1l-.9-2.1l-2.1-.9l2.1-.9z"/><circle cx="8" cy="22" r="1"/><circle cx="22" cy="10" r=".9"/><circle cx="34" cy="8" r="1.1"/><circle cx="20" cy="27" r=".8"/><circle cx="40" cy="26" r=".9"/></g></svg>')
SUN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#c99a2e" opacity=".5"/><circle cx="14" cy="13" r="12" fill="#f6c84a"/><circle cx="14" cy="13" r="12" fill="none" stroke="#e2ab2a" stroke-width="1.5"/></svg>'
MOON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#8d93a3" opacity=".6"/><circle cx="14" cy="13" r="12" fill="#d9dde6"/><circle cx="10" cy="11" r="3.2" fill="#b8bfcc"/><circle cx="18" cy="16" r="2.2" fill="#b8bfcc"/><circle cx="16" cy="8" r="1.5" fill="#b8bfcc"/><circle cx="14" cy="13" r="12" fill="none" stroke="#aeb5c3" stroke-width="1.5"/></svg>'

# ---- mode switch (same mechanics as day/night): paper-cut landscape in two moods; knob = science book -> comic book ----
def _strata(cols, y0=20, H=34, W=72):
    g = ''
    ys = [y0, y0 + 4, y0 + 8, y0 + 12]
    for i, c in enumerate(cols):
        y = ys[i] if i < len(ys) else H
        g += f'<path d="M0 {y+1}q18-4 36 0t36 0V{H}H0z" fill="{c}"/>'
    return g
MODE_R = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 34" preserveAspectRatio="none"><defs><linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d2b4a"/><stop offset="1" stop-color="#3b5a86"/></linearGradient></defs><rect width="72" height="34" rx="17" fill="url(#r)"/>'
 '<g fill="#fff"><circle cx="50" cy="7" r="1"/><circle cx="60" cy="12" r=".8"/><circle cx="42" cy="13" r=".7"/><circle cx="66" cy="6" r=".9"/><path d="M55 16l.7 1.6 1.6.7-1.6.7-.7 1.6-.7-1.6-1.6-.7 1.6-.7z"/></g>'
 '<path d="M36 22l3-6 3 6zM58 21l2.5-5 2.5 5z" fill="#2f5d4a"/>' + _strata(['#4f7a4a', '#8a6a4c', '#6b4a3a', '#3e3240']) + '</svg>')
MODE_E = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 34" preserveAspectRatio="none"><defs><linearGradient id="e" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fc4f2"/><stop offset="1" stop-color="#bde4fb"/></linearGradient></defs><rect width="72" height="34" rx="17" fill="url(#e)"/>'
 '<g fill="#fff"><ellipse cx="18" cy="9" rx="5" ry="2.4"/><ellipse cx="30" cy="13" rx="4" ry="2"/></g><circle cx="12" cy="20" r="3" fill="#5cb85c"/><rect x="11.4" y="22" width="1.2" height="3" fill="#7a5233"/>' + _strata(['#8fd16a', '#f6cf6a', '#f49a6a', '#c79af0']) + '</svg>')
BOOK_SCI = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#0f1a2e" opacity=".5"/><circle cx="14" cy="13" r="12" fill="#eef2f7"/>'
 '<rect x="7.5" y="6.5" width="13" height="14" rx="1.6" fill="#1f3b6e"/><rect x="7.5" y="6.5" width="2.6" height="14" rx="1" fill="#15294d"/><rect x="11" y="9" width="7.5" height="1.2" rx=".6" fill="#dbe6f7"/><rect x="11" y="11.5" width="5.5" height="1" rx=".5" fill="#9fb6d9"/>'
 '<g fill="none" stroke="#f3c75a" stroke-width=".9"><ellipse cx="15" cy="16.2" rx="3.2" ry="1.3"/><ellipse cx="15" cy="16.2" rx="3.2" ry="1.3" transform="rotate(60 15 16.2)"/><ellipse cx="15" cy="16.2" rx="3.2" ry="1.3" transform="rotate(-60 15 16.2)"/></g><circle cx="15" cy="16.2" r=".8" fill="#f3c75a"/>'
 '<circle cx="14" cy="13" r="12" fill="none" stroke="#c9d3e2" stroke-width="1.4"/></svg>')
BOOK_COMIC = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#b4521c" opacity=".45"/><circle cx="14" cy="13" r="12" fill="#ffe27a"/>'
 '<rect x="7.5" y="6.5" width="13" height="14" rx="1.6" fill="#ff5c5c"/><rect x="7.5" y="6.5" width="2.6" height="14" rx="1" fill="#d63c3c"/>'
 '<path d="M15 9l1.1 2.3 2.5.3-1.8 1.7.5 2.5L15 14.6l-2.3 1.2.5-2.5-1.8-1.7 2.5-.3z" fill="#fff" stroke="#3a1d10" stroke-width=".6"/>'
 '<g fill="#3a1d10"><circle cx="12" cy="18" r=".6"/><circle cx="14" cy="18.6" r=".6"/><circle cx="16" cy="18" r=".6"/><circle cx="18" cy="18.6" r=".6"/></g>'
 '<circle cx="14" cy="13" r="12" fill="none" stroke="#e0a100" stroke-width="1.4"/></svg>')

# ---- mode switch v2: dig-site scene (sky · grass · soil with fossils), 96x34; microscope / magnifier knobs ----
def _fossils(ink, op=1):
    return (f'<g fill="none" stroke="{ink}" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" opacity="{op}">'
            '<path d="M38 17v7M41 16v8M44 17v7M47 18v6M36 16h12"/>'                     # ribs
            '<path d="M58 15a4 4 0 1 1 0 8M56 23q-3 3 0 5M60 23q3 3 0 5"/><circle cx="57" cy="18" r=".7" fill="' + ink + '"/><circle cx="59.5" cy="18" r=".7" fill="' + ink + '"/>'  # skull
            '<path d="M22 24l6-3M21 23.5l1-1.5M28.5 21l1-1.5M21.5 25l1 1.5M29 22.5l1 1.5"/>'   # bone
            '<path d="M76 20a3 3 0 1 0 3 3a2 2 0 1 0-2-2a1 1 0 1 0 1 1"/>'            # spiral
            '<path d="M88 26l2-4 2 4z"/>'                                           # crystal
            '</g>')
MODE_R2 = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 34" preserveAspectRatio="none"><defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2a44"/><stop offset="1" stop-color="#2d4a6a"/></linearGradient></defs>'
 '<rect width="96" height="34" rx="17" fill="#5a4635"/><rect width="96" height="10" fill="url(#sk)"/>'
 '<g fill="#fff" opacity=".8"><circle cx="40" cy="3" r=".7"/><circle cx="62" cy="5" r=".6"/><circle cx="80" cy="2.5" r=".7"/><circle cx="52" cy="2" r=".5"/></g>'
 '<path d="M0 10h96" stroke="#3f5a3a" stroke-width="2"/><g stroke="#4f7a4a" stroke-width="1" fill="none"><path d="M30 9l1-3M32 9l1-3M50 9l-1-3M52 9l1-3M70 9l1-3M72 9l-1-3M88 9l1-3"/></g><path d="M58 9q3-3 6 0z" fill="#6b5a48"/>'
 '<rect y="11" width="96" height="2" fill="#3b2d24"/><rect y="29" width="96" height="5" fill="#b89b6e"/>'
 '<g stroke="#8a735c" stroke-width=".6" stroke-dasharray="2 2" opacity=".6"><path d="M20 13v16M40 13v16M60 13v16M80 13v16M0 21h96"/></g>' + _fossils('#e8dcc4') + '<path d="M66 31h8" stroke="#1a1a1a" stroke-width="1.6"/><path d="M66 31h2M70 31h2" stroke="#fff" stroke-width="1.6"/></svg>')
MODE_E2 = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 34" preserveAspectRatio="none"><defs><linearGradient id="se" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5cb3ea"/><stop offset="1" stop-color="#9fd4f5"/></linearGradient></defs>'
 '<rect width="96" height="34" rx="17" fill="#f28a55"/><rect width="96" height="10" fill="url(#se)"/>'
 '<g fill="#fff"><ellipse cx="30" cy="4" rx="4" ry="1.8"/><ellipse cx="70" cy="5" rx="3.5" ry="1.6"/></g>'
 '<path d="M0 10h96" stroke="#5cb85c" stroke-width="3"/><g stroke="#2e7d32" stroke-width="1" fill="none"><path d="M24 9l1-3M26 9l1-3M44 9l-1-3M46 9l1-3M64 9l1-3M66 9l-1-3M84 9l1-3"/></g><circle cx="54" cy="6" r="1.4" fill="#ff6fa3"/><circle cx="36" cy="6.5" r="1.2" fill="#ffd33d"/>'
 '<rect y="11" width="96" height="1.5" fill="#8a3b1e"/><rect y="29" width="96" height="5" fill="#ffd36a"/>'
 '<g fill="#f6a06f" opacity=".9"><circle cx="14" cy="18" r="2.2"/><circle cx="33" cy="26" r="1.8"/><circle cx="52" cy="27" r="2"/><circle cx="70" cy="15" r="1.6"/><circle cx="86" cy="24" r="2"/></g>' + _fossils('#ffffff') +
 '<path d="M11 24l1.5 2.5M12.5 26.5l-2 .5" stroke="#ff6fa3" stroke-width="1.6" stroke-linecap="round"/><path d="M30 15l.6 1.4 1.4.6-1.4.6-.6 1.4-.6-1.4-1.4-.6 1.4-.6z" fill="#fff"/></svg>')
KNOB_R = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#0f1a2e" opacity=".45"/><circle cx="14" cy="13" r="12" fill="#dfe6ee"/>'
 '<g fill="none" stroke="#1f3b6e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 20h12"/><path d="M11 20v-3h6v3"/><path d="M12 8l4-3 4 6-4 3z" fill="#1f3b6e"/><path d="M14 11l-2 4"/><circle cx="14" cy="17" r="1.2" fill="#1f3b6e"/></g>'
 '<path d="M6 10q2-5 7-6" stroke="#fff" stroke-width="1.4" stroke-linecap="round" fill="none" opacity=".9"/><circle cx="14" cy="13" r="12" fill="none" stroke="#b7c3d2" stroke-width="1.4"/></svg>')
KNOB_E = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 28"><circle cx="14" cy="15" r="12" fill="#b4521c" opacity=".45"/><circle cx="14" cy="13" r="12" fill="#ffd84d"/>'
 '<circle cx="12.5" cy="11.5" r="5" fill="#bfe8ff" stroke="#3a1d10" stroke-width="1.6"/><path d="M16 15l4.5 4.5" stroke="#ff5c8a" stroke-width="3" stroke-linecap="round"/><path d="M16 15l4.5 4.5" stroke="#3a1d10" stroke-width="1.2" stroke-linecap="round" opacity=".5"/>'
 '<path d="M10 10q1-2 3-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" fill="none"/><path d="M21 6l.6 1.4 1.4.6-1.4.6-.6 1.4-.6-1.4-1.4-.6 1.4-.6z" fill="#fff" stroke="#3a1d10" stroke-width=".5"/>'
 '<circle cx="14" cy="13" r="12" fill="none" stroke="#e0a100" stroke-width="1.4"/></svg>')

# ---- stories launcher: paper-cut sky with clouds, a rainbow, a smiling star and a hanging heart ----
def _pcloud(x, y, s, c):
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-40 10q-16 0-14-14q3-14 18-10q6-16 24-9q12-12 26 2q16-4 16 14q0 17-18 17z" fill="{c}"/><path d="M-40 10q-16 0-14-14q3-14 18-10q6-16 24-9q12-12 26 2q16-4 16 14q0 17-18 17z" fill="#000" opacity=".06" transform="translate(2 3)"/></g>'
STORY_BG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 120" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="t" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3fb8c9"/><stop offset="1" stop-color="#8fdbe3"/></linearGradient></defs>'
 '<rect width="320" height="120" fill="url(#t)"/><path d="M0 22q40-14 80-4t80 0t80-6t80 4V0H0z" fill="#5ccad6" opacity=".7"/>'
 '<g fill="#fff"><circle cx="70" cy="40" r="1.4"/><circle cx="120" cy="22" r="1"/><circle cx="160" cy="54" r="1.2"/><circle cx="210" cy="30" r="1.4"/><circle cx="100" cy="66" r="1"/><circle cx="40" cy="58" r="1"/><circle cx="185" cy="12" r="1"/></g>'
 '<g fill="none" stroke-width="7"><path d="M222 104a52 52 0 0 1 104 0" stroke="#f4826f"/><path d="M229 104a45 45 0 0 1 90 0" stroke="#f8c56a"/><path d="M236 104a38 38 0 0 1 76 0" stroke="#9fd67a"/><path d="M243 104a31 31 0 0 1 62 0" stroke="#7ab8ef"/></g>'
 '<path d="M222 56l4.6 9.4 10.4 1.5-7.5 7.3 1.8 10.3-9.3-4.9-9.3 4.9 1.8-10.3-7.5-7.3 10.4-1.5z" fill="#ffd45a" stroke="#e8a92a" stroke-width="1.4" stroke-linejoin="round"/><circle cx="219" cy="70" r="1.1" fill="#6b4a1f"/><circle cx="225" cy="70" r="1.1" fill="#6b4a1f"/><path d="M219 74q3 2.5 6 0" stroke="#6b4a1f" stroke-width="1" fill="none" stroke-linecap="round"/>'
 '<line x1="34" y1="0" x2="34" y2="30" stroke="#fff" stroke-width=".8" opacity=".8"/><path d="M34 44c-6-5-10-8-10-12a5 5 0 0 1 10-1a5 5 0 0 1 10 1c0 4-4 7-10 12z" fill="#ff8a5c"/>'
 + _pcloud(30, 108, .9, '#ffffff') + _pcloud(100, 116, 1.1, '#e9f7f8') + _pcloud(180, 112, .9, '#ffffff') + _pcloud(290, 112, 1.0, '#e9f7f8')
 + _pcloud(26, 8, .7, '#ffe9a6') + _pcloud(300, 6, .6, '#ffe9a6') + '</svg>')
