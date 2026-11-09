from art_lib import *
A = {}

def cone(x, y, w, h, cls='m'):
    return f'<path class="{cls}" d="M{x-w} {y} L{x-w*0.18} {y-h} h{w*0.36} L{x+w} {y}Z"/><ellipse class="m2" cx="{x}" cy="{y-h}" rx="{w*0.2}" ry="{h*0.08+1.5}"/>'
def fold(y, amp=10, cls='l'):
    return f'<path class="{cls}" d="M0 {y} q25 -{amp} 50 0 t50 0 t50 0 t50 0 t50 0 t50 0 t50 0 t50 0"/>'

A['mud-volcano-z2'] = SKY + sun(330, 40) + \
    layers(118, [(30, 'd2'), (24, 'cl'), (48, 'm')]) + surface(118) + \
    '<path class="w2" d="M30 118 q30 -6 60 0z M250 118 q40 -7 80 0z"/>' + cone(160, 118, 30, 22) + cone(220, 118, 20, 14) + cone(300, 118, 14, 10) + \
    '<g class="bub"><circle class="m n rise" cx="160" cy="92" r="4"/><circle class="m n rise d1s" cx="220" cy="100" r="3"/></g>' + \
    '<g fill="none">' + fold(160, 10).replace('class="l"', 'class="l t"') + fold(176, 14).replace('class="l"', 'class="l t"') + '</g>' + \
    '<path class="l" d="M196 220 L204 190 L192 170 L200 150" stroke-dasharray="5 4"/>' + ripples([(40, 130), (300, 130)])

A['mud-volcano-z3'] = SKY + sun(64, 40) + \
    layers(130, [(90, 'd2')]) + surface(130) + \
    '<path class="m" d="M90 130 Q120 92 200 90 Q280 92 310 130Z"/><path class="m2" d="M140 104 Q200 94 260 104 Q240 120 200 120 Q160 120 140 104Z"/>' + \
    '<path class="l t" d="M20 150 l20 10 l-6 18 l22 6 M56 184 l20 -10 l16 14 M300 150 l26 8 l-4 18 l20 8 M342 184 l24 -8 M326 158 l20 -12"/>' + \
    '<path class="m n" d="M0 200 q50 -24 100 0 t100 0 t100 0 t100 0 V220 H0Z" opacity=".7"/>' + person(352, 130, 0.5)

A['khor-subiyah'] = SKY + \
    '<path class="d" d="M-2 0 V220 H120 Q150 120 130 0Z" transform="translate(0 0)"/>' + \
    '<path class="d" d="M402 0 V220 H300 Q260 120 290 0Z"/>' + \
    '<rect class="w n" x="120" y="0" width="180" height="220"/>' + \
    '<path class="d" d="M-2 0 V220 H120 Q150 120 130 0Z"/><path class="d" d="M402 0 V220 H300 Q260 120 290 0Z"/>' + \
    '<path class="l" d="M160 0 Q200 60 170 120 Q150 180 180 220" stroke-dasharray="7 6" opacity=".5"/>' + \
    arrow_up(210, 120, 40, 'wh', 180) + arrow_up(240, 80, 40, 'wh', 0) + \
    fish(170, 170, 0.9, 'su') + fish(250, 150, 0.7, 'wh', True) + \
    '<path class="r" d="M196 196 q10 -12 20 -4 q-6 6 -2 10 q-10 2 -18 -6z"/>' + \
    mangrove(110, 150, 0.9) + mangrove(126, 196, 0.8) + mangrove(296, 120, 0.85) + mangrove(310, 180, 0.8)

A['coastal-sabkha'] = SKY + sun(200, 40, 26) + \
    '<path class="l t" d="M120 90 q-6 -8 0 -16 q6 -8 0 -16 M200 96 q-6 -8 0 -16 q6 -8 0 -16 M280 90 q-6 -8 0 -16 q6 -8 0 -16"/>' + \
    '<rect class="w n" x="0" y="120" width="70" height="100"/>' + \
    '<path class="wh" d="M60 122 L402 116 V222 H50Z"/>' + \
    '<path class="l t" d="M90 140 l40 6 l30 -10 l40 8 l40 -6 l40 8 l40 -4 l30 6 M110 170 l40 -6 l40 10 l40 -8 l40 6 l40 -8 l40 6 M100 200 l50 6 l40 -8 l50 6 l40 -6 l50 8"/>' + \
    ''.join(f'<path class="wh" d="M{x} {y} l7 -4 l7 4 l-7 4z M{x} {y} v8 l7 4 v-8 M{x+14} {y} v8 l-7 4"/>' for x, y in [(160, 180), (250, 150), (330, 186)]) + \
    '<path class="w2" d="M60 130 q20 4 40 0 q-10 8 -40 8z"/>'

A['kuwait-geopark'] = SKY + sun(340, 36, 18) + \
    '<path class="r" d="M-2 120 L60 70 L140 66 L170 120Z"/><path class="l t" d="M20 100 h120 M40 86 h100"/>' + \
    ground(120, 'd', 6) + cone(220, 120, 30, 24) + mound(300, 124, 22) + flower(360, 160, 'pu') + flower(372, 166, 'su') + \
    '<path class="l" d="M110 200 V140" stroke-width="3"/><path class="wh" d="M110 144 h40 l8 7 l-8 7 h-40z"/><path class="wh" d="M110 162 h-38 l-8 7 l8 7 h38z"/>' + \
    person(160, 196, 0.8) + person(184, 200, 0.6, 'rd')

A['wadi-al-batin'] = SKY + sun(64, 40) + cloud(320, 30, 0.8, True) + \
    '<path class="d" d="M-2 100 H402 V222 H-2Z"/>' + \
    '<path class="d2" d="M-2 222 L150 100 L230 100 L402 200 V222Z"/>' + \
    '<path class="w2" d="M110 222 L180 104 L200 104 L250 222Z" opacity=".55"/>' + \
    '<path class="l" d="M110 222 L180 104 M250 222 L200 104" stroke-dasharray="6 5"/>' + \
    '<path class="l" d="M-2 222 L150 100 M230 100 L402 200"/>' + pebbles([(150, 190), (190, 170), (210, 196), (170, 150), (196, 130)])

A['bahrah-hydrothermal'] = SKY + \
    layers(110, [(30, 'd'), (30, 'd2'), (30, 'r'), (20, 'r2')]) + surface(110) + \
    '<rect class="rd n" x="0" y="206" width="400" height="14" opacity=".8"/>' + \
    '<path class="l" d="M140 220 L160 110 M260 220 L240 110" stroke-width="3"/>' + \
    arrow_up(150, 200, 36, 'rd', 10) + arrow_up(250, 200, 36, 'rd', -10) + arrow_up(156, 160, 30, 'rd', 10) + arrow_up(244, 160, 30, 'rd', -10) + \
    '<g class="smoke"><path class="l t rise" d="M160 104 q-6 -8 0 -16 q6 -8 0 -16"/><path class="l t rise d1s" d="M240 104 q-6 -8 0 -16 q6 -8 0 -16"/></g>' + \
    '<g transform="translate(330 70)"><rect class="wh" x="-6" y="-34" width="12" height="40" rx="6"/><circle class="rd" cx="0" cy="12" r="9"/><rect class="rd n" x="-2.5" y="-14" width="5" height="22"/></g>'

def rose(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">' +
            ''.join(f'<ellipse class="d2" cx="0" cy="-12" rx="7" ry="16" transform="rotate({a})"/>' for a in (-60, -30, 0, 30, 60)) +
            '<ellipse class="d" cx="0" cy="-6" rx="9" ry="6"/></g>')
A['gypcrete-formations'] = SKY + sun(330, 40) + ground(120, 'd2', 4) + \
    '<path class="cl" d="M-2 120 Q200 116 402 120 V134 Q200 130 -2 134Z"/><path class="l t" d="M40 120 v14 M110 120 v14 M190 118 v14 M260 120 v14 M340 120 v14"/>' + \
    rose(140, 200, 1.6) + rose(230, 196, 1.2) + rose(300, 206, 0.9)

A['sabkha-seismites'] = SKY + zig(30, 50) + zig(330, 50) + \
    layers(96, [(30, 'd'), (26, 'cl'), (34, 'm'), (34, 'd2')]) + surface(96) + \
    '<path class="cl" d="M40 150 q10 -24 20 0 q10 -30 20 0 q10 -20 20 0z M220 150 q10 -26 20 0 q10 -18 20 0z"/>' + \
    ''.join(f'<ellipse class="m" cx="{x}" cy="182" rx="22" ry="11"/>' for x in (130, 190, 300, 360)) + \
    '<path class="l t" d="M0 200 q40 -14 80 0 t80 0 t80 0 t80 0 t80 0"/>'

A['holocene-sea-level'] = SKY + sun(340, 36, 18) + \
    '<path class="d2" d="M-2 76 L120 76 L160 102 L240 102 L280 130 L402 130 V222 H-2Z"/>' + \
    '<path class="l" d="M0 76 H400 M0 102 H400 M0 130 H400" stroke-dasharray="5 6" opacity=".8"/>' + sea(160) + ripples([(260, 180), (340, 196)]) + \
    '<path class="l" d="M-2 160 H402"/>' + hut(60, 76, 0.6) + mound(200, 102, 16) + \
    '<path class="r2" d="M300 130 l-20 0 q0 -6 10 -8 q10 2 10 8z"/>' + arrow_up(380, 154, 22, 'wh', 180) + arrow_up(380, 92, 22, 'wh', 0)

A['jahra-escarpment-interface'] = SKY + sun(340, 40) + \
    '<path class="r" d="M-2 60 L120 50 L170 130 L-2 140Z"/><path class="l t" d="M10 80 h120 M10 104 h140"/>' + \
    '<path class="d" d="M-2 140 L170 130 L402 140 V222 H-2Z"/>' + \
    '<path class="d2" d="M150 132 Q260 150 330 222 L90 222 Q120 160 150 132Z"/>' + \
    pebbles([(160, 150), (180, 170), (140, 176), (200, 196), (120, 200), (240, 206), (170, 210), (220, 180)]) + \
    '<path class="l" d="M60 50 q30 30 90 80" stroke-dasharray="5 4"/>' + arrow_up(60, 120, 36, 'wh')

A['dextral-slip-fault'] = '<rect class="d n" width="400" height="220"/>' + \
    '<path class="d2" d="M-2 -2 H220 L180 222 H-2Z"/>' + \
    '<path class="l" d="M220 -2 L180 222" stroke-width="3.2"/>' + \
    '<path class="w2" d="M-2 60 Q100 70 200 68 L200 78 Q100 82 -2 72Z"/><path class="w2" d="M196 128 Q300 128 402 136 V146 Q300 140 194 140Z"/>' + \
    '<path class="l" d="M200 68 V78 M196 128 V140" stroke-dasharray="3 3"/>' + \
    arrow_up(110, 170, 50, 'wh', 0) + arrow_up(300, 40, 50, 'wh', 180) + \
    '<path class="l t" d="M200 78 L196 128" stroke-dasharray="3 3"/>'

A['had-safah-sinkholes'] = SKY + sun(64, 40) + \
    layers(110, [(36, 'd'), (74, 'cl')]) + surface(110) + \
    '<path class="dk" d="M150 110 Q200 100 250 110 L236 146 Q200 152 164 146Z"/>' + \
    '<path class="m2" d="M120 160 Q200 140 280 160 Q300 190 200 196 Q100 190 120 160Z"/>' + \
    '<path class="l t" d="M150 110 l-20 -6 M250 110 l24 -6 M164 146 l-14 10 M236 146 l16 10"/>' + \
    '<path class="su" d="M310 110 l14 -28 l14 28z"/><path class="dk" d="M322 92 h4 v8 h-4z M322 102 h4 v3 h-4z"/>'

A['petrified-wood-field'] = SKY + sun(340, 40) + \
    '<g opacity=".55">' + tree(110, 110, 1.1).replace('class="g"', 'class="l"').replace('class="wd"', 'class="l"') + '</g>' + \
    '<path class="w2" d="M-2 120 Q200 100 402 118 V128 Q200 112 -2 132Z" opacity=".5"/>' + ground(130, 'd', 6) + \
    '<path class="r2" d="M90 176 L280 158 q14 10 0 22 L90 196z"/><ellipse class="r" cx="90" cy="186" rx="10" ry="10"/>' + \
    '<circle class="l t" cx="90" cy="186" r="6"/><circle class="l t" cx="90" cy="186" r="2.5"/>' + \
    ''.join(f'<circle class="dk" cx="{x}" cy="{y}" r="2"/>' for x, y in [(150, 178), (180, 174), (210, 176), (240, 170)]) + \
    magnifier(330, 170, 26, '<circle class="l t" r="16"/><circle class="l t" r="10"/><circle class="l t" r="4"/>')

A['sand-injectite-biotope'] = SKY + sun(330, 40) + \
    layers(118, [(102, 'm')]) + surface(118) + \
    '<path class="d" d="M100 220 L108 160 L96 140 L112 118 h14 L120 140 L132 166 L124 220Z"/><path class="d" d="M250 220 L256 170 L272 146 L266 118 h12 L288 150 L270 176 L274 220Z"/>' + \
    '<path class="d" d="M120 166 L170 150 L172 156 L130 172Z"/>' + \
    '<ellipse class="su" cx="40" cy="116" rx="12" ry="4"/><ellipse class="g" cx="70" cy="116" rx="10" ry="3.5"/><ellipse class="rd" cx="340" cy="116" rx="12" ry="4"/>' + \
    lizard(200, 116, 0.8) + '<circle class="dk" cx="330" cy="112" r="4"/><path class="l t" d="M326 112 l-4 3 M334 112 l4 3"/>'

A['positive-flower-structure'] = SKY + \
    layers(80, [(30, 'd'), (30, 'r'), (30, 'd2'), (50, 'r2')]) + \
    '<path class="d" d="M-2 80 Q200 30 402 80 V110 Q200 70 -2 110Z"/>' + \
    '<path class="l" d="M200 220 V160 M200 160 Q170 120 120 80 M200 160 Q230 120 280 80 M200 170 Q180 130 160 70 M200 170 Q220 130 240 70" stroke-width="2.6"/>' + \
    arrow_up(30, 160, 40, 'wh', 90) + arrow_up(370, 160, 40, 'wh', -90) + \
    '<path class="pu" d="M200 40 q-8 -12 0 -20 q8 8 0 20z M200 40 q-14 -2 -16 -12 q12 0 16 12z M200 40 q14 -2 16 -12 q-12 0 -16 12z"/>'

A['karst-sinkhole-zone'] = '<rect class="d n" width="400" height="220"/>' + \
    ''.join(f'<ellipse class="d2" cx="{x}" cy="{y}" rx="{r}" ry="{r*0.85}"/><ellipse class="m2" cx="{x}" cy="{y+1}" rx="{r*0.45}" ry="{r*0.38}"/>' for x, y, r in [(60, 70, 18), (130, 150, 24), (210, 80, 14), (290, 170, 20), (330, 70, 16), (60, 190, 12)]) + \
    '<ellipse class="g" cx="210" cy="160" rx="14" ry="12"/><ellipse class="g" cx="250" cy="120" rx="8" ry="7"/>' + \
    satellite(320, 30) + '<path class="l t" d="M320 38 L210 150 M320 38 L250 112" stroke-dasharray="4 5" opacity=".7"/>'

A['wadi-batin-fault'] = SKY + sun(330, 40) + \
    layers(110, [(110, 'd2')]) + '<path class="d" d="M-2 110 L130 110 L150 130 L250 130 L270 110 L402 110 V222 H-2Z"/>' + \
    '<path class="d2" d="M150 130 L250 130 L240 222 L160 222Z" opacity=".0"/>' + \
    '<path class="l" d="M200 130 L200 220" stroke-width="3" stroke-dasharray="1 0"/><path class="l t" d="M200 150 l-8 10 l8 10 l-8 10 l8 10 l-8 10"/>' + \
    '<rect class="su" x="60" y="80" width="280" height="14" rx="2" transform="rotate(-2 200 87)"/>' + \
    ''.join(f'<path class="l t" d="M{x} 81 v6"/>' for x in range(72, 340, 16)).replace('<path', '<path transform="rotate(-2 200 87)"')

A['dibdibba-alluvial-fan'] = SKY + \
    '<path class="r" d="M-2 110 L30 60 L60 90 L90 50 L130 110Z"/><path class="r2" d="M60 110 L90 50 L130 110Z"/>' + \
    ground(110, 'd', 0) + \
    '<path class="d2" d="M110 112 Q260 100 402 160 V222 H130 Q100 160 110 112Z"/>' + \
    '<path class="w2" d="M110 112 q60 10 120 40 l-4 6 q-60 -30 -118 -40z" opacity=".7"/>' + \
    pebbles([(170, 140), (200, 160), (240, 180), (280, 200), (320, 190), (360, 200), (220, 206), (180, 196), (260, 156), (300, 170), (150, 180), (330, 210)])

A['subbiya-sandstone-pipes'] = SKY + sun(64, 40) + ground(160, 'd', 4) + \
    ''.join(f'<path class="d2" d="M{x-w} 160 L{x-w+3} {160-h} Q{x} {160-h-8} {x+w-3} {160-h} L{x+w} 160Z"/><path class="l t" d="M{x-w+4} {160-h*0.6} h{2*w-8} M{x-w+3} {160-h*0.3} h{2*w-6}"/>' for x, w, h in [(130, 16, 80), (180, 12, 60), (230, 18, 96), (280, 10, 50)]) + \
    person(330, 160, 0.7) + arrow_up(80, 200, 36, 'wh')

def deino(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M-30 0 v-26 M-14 0 v-26 M14 0 v-26 M28 0 v-26" stroke-width="7"/>'
            '<path class="r2" d="M-40 -20 q0 -36 40 -38 q38 0 44 30 q2 10 -6 12 h-72q-6 0 -6 -4z"/>'
            '<path class="r2" d="M38 -40 q20 -6 22 14 q2 20 -6 34 l-6 -2 q4 -16 -2 -28z"/>'
            '<path class="wh" d="M44 -16 q4 16 -6 24 l-2 -4 q6 -8 2 -18z"/><circle class="k n" cx="44" cy="-38" r="2"/>'
            '<path class="r" d="M30 -50 q-12 4 -10 22 q8 -2 14 -10z"/></g>')
A['huwaimiliyah-fossils'] = SKY + sun(330, 36) + \
    '<path class="g" d="M-2 120 Q200 100 402 120 V222 H-2Z"/>' + \
    '<path class="w2" d="M-2 190 Q120 170 240 196 T402 190 V206 Q300 210 240 208 T-2 206Z"/>' + \
    tree(70, 128, 1) + tree(340, 124, 0.8) + deino(200, 176, 1.1) + birds([(120, 50), (140, 40)])

A['anthropic-slope-markers'] = SKY + sun(330, 40) + \
    '<path class="d2" d="M-2 80 Q200 90 402 170 V222 H-2Z"/>' + \
    '<path class="dk" d="M60 100 l30 10 l-10 14 l40 12 l-12 16 l40 10" stroke-width="0"/><path class="l" d="M60 100 l30 10 l-10 14 l40 12 l-12 16 l40 10" stroke-width="6"/>' + \
    '<path class="l t" d="M200 130 q30 30 40 80 M240 140 q30 30 30 70" stroke-dasharray="2 4"/>' + \
    '<path class="w2" d="M250 150 q10 20 6 60 l-6 0 q2 -40 -6 -58z"/>' + \
    '<path class="r2" d="M-2 190 L402 160 L402 168 L-2 198Z"/><path class="l t" d="M100 186 v-8 M200 178 v-8 M300 170 v-8"/>'

A['um-al-rimam-yardangs'] = SKY + \
    ''.join(f'<path class="l" d="M{x} {y} q30 -6 60 0 q20 4 40 0"/>' for x, y in [(10, 50), (40, 76), (0, 100)]) + \
    ground(150, 'd', 0) + \
    ''.join(f'<path class="r" d="M{x} {y} Q{x+10} {y-h} {x+w*0.4} {y-h} Q{x+w} {y-h*0.6} {x+w} {y}Z"/><path class="l t" d="M{x+8} {y-h*0.4} Q{x+w*0.5} {y-h*0.7} {x+w-10} {y-h*0.3}"/>' for x, y, w, h in [(60, 156, 110, 40), (190, 162, 140, 54), (300, 150, 90, 28)])

A['sabbiya-varnish-ridge'] = SKY + sun(64, 40) + ground(160, 'd', 4) + \
    '<path class="r" d="M40 160 L110 90 L220 80 L300 160Z"/><path class="dk" d="M90 110 L110 90 L220 80 L248 108 Q170 100 90 110Z"/>' + \
    '<path class="wh" d="M150 90 l3 -6 l3 6 l-3 6z M200 88 l2 -5 l2 5 l-2 5z"/>' + \
    magnifier(330, 110, 30, ''.join(f'<circle class="pu" cx="{x}" cy="{y}" r="3"/>' for x, y in [(-10, -6), (6, -10), (10, 6), (-6, 10), (0, 0)]))

A['volcanic-flood-erratics'] = SKY + \
    '<path class="r2" d="M-2 110 L30 70 L60 96 L100 60 L140 110Z"/>' + ground(110, 'd', 0) + \
    '<path class="w2" d="M100 112 Q200 104 300 130 Q260 120 200 122 Q150 120 100 112Z" opacity=".7"/>' + arrow_up(240, 120, 50, 'wh', 100) + \
    ''.join(f'<path class="dk" d="M{x-r} {y} q0 -{r*1.2} {r} -{r*1.2} q{r} 0 {r} {r*1.2}z"/>' for x, y, r in [(250, 180, 16), (300, 196, 12), (200, 200, 10), (340, 176, 9)]) + \
    '<path class="l t" d="M244 172 l6 -6 M296 190 l5 -5"/>'

A['bubiyan-coastal-sabkha'] = '<rect class="w n" width="400" height="220"/>' + \
    '<path class="wh" d="M60 60 Q200 20 340 60 Q380 120 330 180 Q200 210 70 180 Q20 120 60 60Z"/>' + \
    '<path class="l t" d="M100 90 l30 10 l30 -6 l30 8 l30 -4 l40 6 M90 130 l40 -6 l40 8 l40 -6 l40 6 l30 -4 M110 164 l40 4 l40 -6 l40 6 l40 -4"/>' + \
    '<path class="w2" d="M200 30 q-10 30 -40 46 M200 30 q14 30 40 44" opacity=".8"/>' + ripples([(20, 40), (350, 200), (30, 200)])

A['jal-al-liyah-dunes'] = SKY + sun(330, 40) + ground(160, 'd', 0) + \
    ''.join(f'<path class="l" d="M{x} {y} q30 -6 60 0 q20 4 40 0"/>' for x, y in [(10, 60), (30, 86)]) + \
    '<path class="l" d="M60 160 Q110 110 160 160 Q130 150 110 160" stroke-dasharray="5 4" opacity=".6"/>' + \
    '<path class="d2" d="M170 160 Q230 96 300 160 Q260 140 240 160Z"/><path class="d2" d="M280 170 Q320 130 360 170 Q340 160 320 170Z"/>' + \
    arrow_up(130, 190, 40, 'wh', 90)

A['lower-fars-marine-bed'] = SKY + \
    '<rect class="w2 n" x="0" y="0" width="400" height="110" opacity=".55"/>' + fish(120, 60, 1, 'l') + fish(260, 40, 0.8, 'l', True) + \
    layers(110, [(34, 'd'), (40, 'cl'), (36, 'd2')]) + surface(110) + \
    '<g transform="translate(140 166)"><circle class="wh" r="14"/>' + ''.join(f'<path class="l t" d="M0 0 L{dx} {dy}"/>' for dx, dy in [(0, -12), (11, -4), (7, 10), (-7, 10), (-11, -4)]) + '</g>' + \
    shell(220, 164, 1.2) + shell(300, 170, 1) + '<path class="wh" d="M60 172 q10 -14 22 0 q-10 6 -22 0z"/>'

A['mud-volcano-outcrops'] = SKY + sun(330, 40) + \
    layers(120, [(30, 'd2'), (30, 'd'), (40, 'd2')]) + surface(120) + \
    '<path class="m" d="M170 220 Q180 170 186 120 L214 120 Q220 170 230 220Z"/>' + cone(200, 120, 30, 20) + \
    '<path class="l t" d="M150 150 q20 -8 30 -2 M220 150 q16 -6 30 2 M140 180 q30 -10 40 0 M220 180 q20 -8 40 2"/>' + \
    arrow_up(200, 210, 50, 'wh')

A['wadi-batin-playas'] = SKY + cloud(110, 34, 0.9, True) + \
    ground(120, 'd', 0) + '<ellipse class="w2" cx="220" cy="170" rx="120" ry="26"/>' + \
    flower(110, 170, 'pu') + flower(124, 176, 'su') + flower(320, 184, 'pu') + flower(340, 176, 'wh') + \
    tuft(80, 196, 0.9) + tuft(360, 204, 0.8) + \
    '<g transform="translate(250 154) scale(.7)"><ellipse class="r" cx="0" cy="0" rx="24" ry="11"/><path class="l" d="M-14 8 v20 M-6 10 v19 M8 10 v19 M16 8 v20" stroke-width="3"/><path class="r" d="M20 0 q12 4 14 16 l-6 2 q-4 -10 -12 -12z"/><path class="l" d="M22 -6 q-2 -12 4 -18 M26 -4 q4 -12 10 -14" stroke-width="2.2"/></g>'

# Al-Ahmadi quarry: stepped quarry walls in Dammam carbonates, karst holes, gas rising from the oil field below
A['ahmadi-quarry'] = SKY + sun(64, 36, 18) + \
    layers(92, [(30, 'd'), (26, 'cl'), (26, 'wh'), (46, 'r')]) + \
    '<path class="d2" d="M-2 92 H120 V118 H170 V144 H230 V170 H402 V222 H-2Z" opacity=".0"/>' + \
    '<path class="d" d="M120 92 V118 H170 V144 H230 V170 H402 V92Z"/>' + \
    '<path class="l" d="M-2 92 H120 V118 H170 V144 H230 V170 H402" stroke-width="2.6"/>' + \
    ''.join(f'<ellipse class="dk" cx="{x}" cy="{y}" rx="{r}" ry="{r*0.7}"/>' for x, y, r in [(30, 132, 7), (64, 140, 5), (96, 128, 6), (48, 156, 4), (150, 160, 6), (190, 158, 4), (110, 150, 3.5)]) + \
    '<path class="l t" d="M0 196 q40 -10 80 0 t80 0 t80 0" opacity=".6"/>' + \
    ''.join(f'<circle class="wh n rise{dd}" cx="{x}" cy="{y}" r="2.6"/>' for x, y, dd in [(40, 206, ''), (100, 204, ' d1s'), (160, 208, ' d2s'), (70, 212, ' d1s')]) + \
    '<g transform="translate(330 170)"><path class="l" d="M-12 0 L0 -44 L12 0 M-8 -14 H8 M-5 -28 H5" stroke-width="2.4"/><path class="rd" d="M-2 -48 h4 v6 h-4z"/></g>' + \
    person(278, 170, 0.75) + '<path class="l" d="M286 140 l14 -10 M296 128 h8" stroke-width="2.4"/>'
