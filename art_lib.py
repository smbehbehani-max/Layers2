import sys
sys.path.insert(0, '/tmp/w')
from art import SKY, sun, person, birds, shell, mound, tuft  # noqa

def sea(y, cls='w'):
    return f'<rect class="{cls} n" x="0" y="{y}" width="400" height="{220-y}"/><path class="l t" d="M0 {y} H400"/>'
def ground(y, cls='d', curve=10):
    return f'<path class="{cls}" d="M-2 {y} Q200 {y-curve} 402 {y} V222 H-2Z"/>'
def ripples(pts):
    return ''.join(f'<path class="l t" d="M{x} {y} q8 -4 16 0"/>' for x, y in pts)
def palm(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M0 0 q-2 -26 4 -40" stroke-width="3"/>'
            '<path class="g" d="M4 -40 q-16 -6 -24 4 q12 -2 24 -4z M4 -40 q14 -10 26 -2 q-12 0 -26 2z M4 -40 q-6 -14 4 -20 q-2 10 -4 20z M4 -40 q10 -2 16 8 q-8 -4 -16 -8z"/></g>')
def reeds(x, y, n=5, h=30):
    out = ''
    for i in range(n):
        xx = x + i * 7; hh = h - (i % 3) * 6
        out += f'<path class="l t" d="M{xx} {y} q2 -{hh/2} -1 -{hh}"/><ellipse class="wd" cx="{xx-1}" cy="{y-hh-3}" rx="2.2" ry="5"/>'
    return out
def fish(x, y, s=1, cls='su', flip=False):
    f = -1 if flip else 1
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})"><path class="{cls}" d="M-12 0 Q-2 -9 10 0 Q-2 9 -12 0Z"/>'
            f'<path class="{cls}" d="M-11 0 l-8 -6 v12z"/><circle class="k n" cx="5" cy="-1" r="1.4"/></g>')
def crab(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse class="rd" cx="0" cy="0" rx="10" ry="6.5"/>'
            '<path class="l t" d="M-8 2 l-6 5 M-9 -1 l-7 1 M8 2 l6 5 M9 -1 l7 1"/>'
            '<path class="rd" d="M-7 -5 l-5 -7 l-3 4z M7 -5 l5 -7 l3 4z"/>'
            '<circle class="wh" cx="-3" cy="-6" r="2"/><circle class="wh" cx="3" cy="-6" r="2"/></g>')
def snail(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="sk" d="M-12 0 h22 q4 0 4 -4 l-2 -2 v4 h-24z"/>'
            '<circle class="wd" cx="0" cy="-7" r="7"/><path class="l t" d="M0 -7 m-3 0 a3 3 0 1 1 3 3"/></g>')
def bird_stand(x, y, s=1, cls='wh', beak='su', legs=14):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M-2 0 v-{legs} M3 0 v-{legs}" stroke-width="1.8"/>'
            f'<ellipse class="{cls}" cx="0" cy="-{legs+7}" rx="11" ry="7"/><path class="l" d="M8 -{legs+10} q4 -10 2 -16" stroke-width="3"/>'
            f'<circle class="{cls}" cx="10" cy="-{legs+27}" r="4.5"/><path class="{beak}" d="M14 -{legs+28} l9 3 l-9 1z"/></g>')
def flower(x, y, cls='pu', h=18):
    return (f'<path class="l t" d="M{x} {y} v-{h}"/><path class="g" d="M{x} {y-6} q-7 -2 -8 -8 q6 0 8 8z"/>'
            f'<path class="{cls}" d="M{x} {y-h} q-6 -8 0 -12 q6 4 0 12z M{x} {y-h} q-9 -2 -9 -8 q7 0 9 8z M{x} {y-h} q9 -2 9 -8 q-7 0 -9 8z"/>')
def pumpjack(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect class="dk" x="-30" y="-4" width="60" height="6"/>'
            '<path class="l" d="M-14 -4 L0 -40 L14 -4" stroke-width="3"/><path class="rd" d="M-34 -46 L30 -36 L32 -42 L-32 -52z"/>'
            '<path class="rd" d="M28 -46 q14 2 12 14 l-8 -2 q0 -6 -6 -6z"/><path class="l" d="M38 -32 V-4" stroke-width="1.6"/>'
            '<circle class="su" cx="0" cy="-42" r="3.5"/><rect class="r2" x="-38" y="-24" width="14" height="20"/></g>')
def camel(x, y, s=1, cls='wd'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M-14 0 v-18 M-6 0 v-18 M10 0 v-18 M16 0 v-18" stroke-width="3"/>'
            f'<path class="{cls}" d="M-20 -16 q0 -12 8 -14 q4 -10 10 -2 q6 -10 12 0 q6 2 6 14z"/>'
            f'<path class="{cls}" d="M14 -22 q8 -6 8 -18 q4 -4 10 -2 l2 4 l-6 2 q0 10 -8 16z"/><circle class="k n" cx="28" cy="-41" r="1.2"/></g>')
def fox(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M-10 0 v-10 M-4 0 v-10 M8 0 v-10 M13 0 v-10" stroke-width="2.4"/>'
            '<ellipse class="su" cx="2" cy="-14" rx="16" ry="7"/><path class="su" d="M-14 -14 q-16 2 -20 12 q12 -2 20 -8z"/>'
            '<path class="su" d="M16 -18 l12 2 l-8 6z M16 -18 l2 -10 l5 8z M22 -16 l4 -9 l3 9z"/><circle class="k n" cx="22" cy="-15" r="1.2"/></g>')
def hedgehog(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="wd" d="M-14 0 q2 -16 14 -16 q12 0 14 10 l6 4 q-2 2 -6 2z"/>'
            '<path class="l t" d="M-10 -6 l-4 -6 M-4 -10 l-2 -7 M2 -12 l1 -7 M8 -10 l3 -6"/><circle class="k n" cx="14" cy="-4" r="1.2"/></g>')
def lizard(x, y, s=1, cls='g'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="{cls}" d="M-26 0 q14 -4 20 -4 q6 -4 18 -3 q8 0 10 3 q-2 3 -10 3 q-12 1 -18 -1 q-8 2 -20 2z"/>'
            '<path class="l t" d="M-4 -3 l-4 -6 M2 -3 l2 -6 M-4 0 l-4 5 M4 0 l3 5"/><circle class="k n" cx="18" cy="-3" r="1"/></g>')
def dolphin(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="r" d="M-30 6 C-18 -18 18 -22 30 -6 l8 -2 l-6 6 q-10 -6 -22 -2 q-10 4 -16 12 l-6 6 v-8z"/>'
            '<path class="r" d="M-2 -14 l-6 -12 l12 9z"/><circle class="k n" cx="20" cy="-8" r="1.5"/><path class="wh n" d="M-14 2 q14 -10 32 -8 q-14 4 -32 8z" opacity=".6"/></g>')
def mangrove(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M0 -10 V-32" stroke-width="3"/>'
            '<path class="l" d="M0 -14 q-8 4 -12 14 M0 -14 q8 4 12 14 M0 -12 q-2 6 -4 12" stroke-width="2"/>'
            '<path class="g" d="M-18 -32 q0 -18 18 -18 q18 0 18 18 q-8 4 -18 2 q-10 2 -18 -2z"/></g>')
def tree(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="wd" d="M-3 0 v-26 h6 v26z"/>'
            '<path class="g" d="M-26 -30 q-4 -14 12 -18 q4 -14 18 -10 q16 -4 18 12 q10 6 2 16 q-20 6 -50 0z"/></g>')
def hut(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect class="cl" x="-18" y="-24" width="36" height="24"/>'
            '<path class="wd" d="M-23 -22 L0 -40 L23 -22Z"/><rect class="dk" x="-5" y="-14" width="10" height="14"/></g>')
def arrow_up(x, y, h=34, cls='wh', rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><path class="{cls}" d="M-6 0 v-{h-14} h-7 l13 -14 l13 14 h-7 v{h-14}z"/></g>')
def magnifier(x, y, r=34, inner=''):
    return (f'<g transform="translate({x} {y})"><circle class="s" r="{r}" opacity=".55"/>{inner}'
            f'<circle class="l" r="{r}" stroke-width="6"/><circle class="l t" r="{r}"/><path class="l" d="M{r*0.72} {r*0.72} L{r*1.3} {r*1.3}" stroke-width="10"/></g>')
def qmark(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="wh" d="M-14 -4 q0 -14 14 -14 q14 0 14 12 q0 9 -12 13 v6 h-6 v-10 q11 -3 11 -9 q0 -5 -7 -5 q-7 0 -7 7z"/>'
            '<circle class="wh" cx="-1" cy="22" r="3.6"/></g>')
def satellite(x, y):
    return (f'<g transform="translate({x} {y})"><rect class="wh" x="-10" y="-8" width="20" height="16" rx="3"/>'
            '<rect class="w" x="-40" y="-6" width="26" height="12"/><rect class="w" x="14" y="-6" width="26" height="12"/>'
            '<path class="l t" d="M-27 -6 v12 M27 -6 v12 M-14 0 h4 M10 0 h4"/></g>')
def cloud(x, y, s=1, rain=False):
    r = ''.join(f'<path class="l t" d="M{x+dx} {y+14*s} l-3 8"/>' for dx in (-14, -4, 6, 16)) if rain else ''
    return (f'<path class="wh" d="M{x-26*s} {y+10*s} q-8 -14 8 -16 q4 -14 20 -10 q12 -10 22 4 q14 0 10 16 z"/>' + r)
def layers(y0, bands, x0=0, w=400):
    out, y = '', y0
    for h, cls in bands:
        out += f'<rect class="{cls} n" x="{x0}" y="{y}" width="{w}" height="{h}"/>'
        y += h
    ys, y = [], y0
    for h, _ in bands[:-1]:
        y += h; ys.append(y)
    out += '<path class="l t" opacity=".55" d="' + ' '.join(f'M{x0} {yy} H{x0+w}' for yy in ys) + '"/>'
    return out
def surface(y):
    return f'<path class="l" d="M0 {y} H400"/>'
def drops(pts, cls='w2'):
    return ''.join(f'<path class="{cls}" d="M{x} {y} q-4 6 0 8 q4 -2 0 -8z"/>' for x, y in pts)
def pebbles(pts):
    cl = ['r', 'd2', 'r2', 'wh', 'pu', 'su']
    return ''.join(f'<ellipse class="{cl[i % 6]}" cx="{x}" cy="{y}" rx="{4+i%3}" ry="{3+i%2}"/>' for i, (x, y) in enumerate(pts))
def zig(x, y, w=26):
    return f'<path class="l t shake" d="M{x} {y} l{w/5} -7 l{w/5} 12 l{w/5} -12 l{w/5} 12 l{w/5} -7"/>'
def split():
    return '<path class="l" d="M200 0 V220" stroke-dasharray="6 5" stroke-width="2.4"/>'
