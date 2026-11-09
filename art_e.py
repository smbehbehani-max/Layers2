from art_lib import *
A = {}

A['jahra-freshwater-lens'] = SKY + sun(64, 40) + \
    layers(116, [(24, 'd'), (80, 'w')]) + surface(116) + \
    '<path class="w2" d="M40 140 Q200 130 360 140 Q300 176 200 180 Q100 176 40 140Z"/>' + \
    '<path class="rd" d="M240 116 V80 h8 v-6 h8 v6 h16 v-6 h8 v6 h8 v36z"/><path class="dk" d="M262 116 v-14 a6 6 0 0 1 12 0 v14z"/>' + \
    palm(120, 116, 0.9) + palm(150, 118, 0.7) + \
    '<path class="l" d="M200 116 V156" stroke-dasharray="3 3"/><path class="l" d="M190 116 V96 H210 V116" stroke-width="2.6"/>' + \
    drops([(120, 150), (160, 158), (280, 152), (330, 146)], 'wh')

def plant_band(x0, x1, y, cls, step=14, h=10):
    return ''.join(f'<path class="{cls}" d="M{x} {y} q-4 -{h} 0 -{h+4} q4 {4} 0 {h+4}z"/>' for x in range(x0, x1, step))
A['jahra-halophytes'] = SKY + sun(330, 40) + sea(150).replace('width="400"', 'width="60"').replace('H400', 'H60') + \
    '<path class="wh" d="M56 150 L130 146 V222 H50Z"/><path class="d" d="M130 146 L402 140 V222 H130Z"/>' + \
    plant_band(140, 200, 160, 'pu', 18, 6) + plant_band(146, 206, 190, 'pu', 18, 6) + \
    plant_band(210, 290, 160, 'rd', 14, 10) + plant_band(214, 290, 192, 'rd', 14, 10) + \
    ''.join(tuft(x, y, 0.7) for x, y in [(310, 166), (340, 172), (370, 164), (320, 198), (356, 204), (390, 196)]) + \
    '<path class="wh" d="M80 176 l3 -6 l3 6 l-3 6z M100 196 l3 -6 l3 6 l-3 6z"/>'

def warbler(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="l" d="M-30 6 L30 -4" stroke-width="2"/>'
            '<ellipse class="d2" cx="0" cy="-6" rx="12" ry="7"/><circle class="d2" cx="10" cy="-14" r="6"/>'
            '<path class="su" d="M15 -15 l8 1 l-8 3z"/><circle class="k n" cx="12" cy="-15" r="1.2"/><path class="d2" d="M-11 -6 l-12 4 l2 -6z"/></g>')
A['basra-reed-warbler'] = SKY + sun(64, 40) + ground(190, 'w2', 0) + \
    reeds(40, 200, 6, 120) + reeds(280, 204, 7, 110) + reeds(150, 206, 4, 70) + \
    warbler(200, 100, 1.4) + \
    '<path class="l" d="M232 74 v-16 l10 -4 v16 M232 74 a3 3 0 1 1 -1 -1 M242 70 a3 3 0 1 1 -1 -1" stroke-width="1.8"/>' + \
    '<path class="wd" d="M110 170 q20 16 40 0 q-4 -10 -20 -10 q-16 0 -20 10z"/><ellipse class="wh" cx="124" cy="166" rx="5" ry="4"/><ellipse class="s" cx="136" cy="166" rx="5" ry="4"/>'

A['jahra-mudflat-nursery'] = SKY + sun(330, 36) + \
    '<path class="m" d="M-2 110 Q200 100 402 110 V222 H-2Z"/>' + \
    '<path class="w2" d="M-2 170 Q100 150 200 176 T402 170 V190 Q300 196 200 196 T-2 190Z"/>' + \
    fish(120, 180, 0.6, 'wh') + fish(160, 184, 0.5, 'su', True) + fish(260, 186, 0.55, 'wh') + \
    crab(80, 140, 1) + crab(320, 150, 0.8) + snail(200, 136, 0.9) + \
    '<path class="rd" d="M260 130 q4 -8 8 0 q4 -8 8 0" fill="none"/><path class="l" d="M260 130 q4 -8 8 0 q4 -8 8 0" stroke-width="3"/>' + \
    bird_stand(360, 110, 1, 'wh', 'su', 20)

A['iris-playa-meadow'] = '<rect class="s n" width="400" height="220"/>' + cloud(80, 30, 0.9, True) + sun(340, 40) + \
    layers(140, [(80, 'd2')]) + surface(140) + \
    '<ellipse class="d" cx="220" cy="142" rx="160" ry="10"/>' + \
    ''.join(flower(x, 142, 'pu', 22 + (x % 3) * 4) for x in range(110, 340, 24)) + \
    ''.join(f'<ellipse class="wd" cx="{x}" cy="176" rx="6" ry="8"/><path class="l t" d="M{x} 168 V146 M{x-4} 184 l-4 8 M{x+4} 184 l4 8"/>' for x in (134, 206, 278))

A['sabriya-oil-ecology'] = SKY + sun(64, 40) + ground(150, 'd', 0) + \
    '<ellipse class="l" cx="200" cy="176" rx="160" ry="34" stroke-dasharray="5 5" opacity=".6"/><ellipse class="l" cx="200" cy="170" rx="100" ry="22" stroke-dasharray="5 5" opacity=".6"/>' + \
    pumpjack(200, 160, 1) + tuft(300, 190, 1.2) + tuft(100, 196, 1.1) + \
    ''.join(f'<circle class="pu n" cx="{x}" cy="{y}" r="2.4"/>' for x, y in [(300, 206), (302, 196), (100, 210), (98, 200)]) + \
    arrow_up(318, 208, 26, 'wh') + arrow_up(80, 214, 26, 'wh')

A['bahra-ecology'] = SKY + sun(330, 40) + ground(130, 'd', 0) + \
    '<ellipse class="g" cx="180" cy="176" rx="130" ry="34" opacity=".35"/>' + \
    '<path class="r" d="M110 190 h140 v-34 h-140z" fill-opacity="0"/><path class="l" d="M110 190 h140 v-34 h-140z M160 156 v34 M210 156 v34" stroke-width="5"/>' + \
    ''.join(tuft(x, y, 0.8) for x, y in [(70, 176), (96, 200), (280, 172), (300, 196), (140, 210), (230, 212), (190, 150), (60, 150)]) + \
    magnifier(340, 160, 26, ''.join(f'<circle class="g" cx="{x}" cy="{y}" r="3"/>' for x, y in [(-8, -6), (6, -8), (8, 6), (-4, 8)]))

A['um-al-aish-ecology'] = SKY + \
    ''.join(f'<path class="l t" d="M{x} {y} q3.5 -4 7 0 q3.5 -4 7 0"/>' for x, y in [(200, 30), (186, 40), (214, 40), (172, 50), (228, 50)]) + \
    ground(120, 'd', 0) + '<ellipse class="w2" cx="140" cy="170" rx="100" ry="24"/><ellipse class="w2" cx="320" cy="186" rx="60" ry="14"/>' + \
    reeds(40, 170, 4, 40) + reeds(230, 176, 4, 34) + snail(130, 196, 0.8) + \
    '<g transform="translate(180 120)"><path class="l" d="M-20 0 H20" stroke-width="3"/><ellipse class="w" cx="-8" cy="-6" rx="10" ry="4"/><ellipse class="w" cx="8" cy="-6" rx="10" ry="4"/><ellipse class="w" cx="-8" cy="6" rx="8" ry="3"/><ellipse class="w" cx="8" cy="6" rx="8" ry="3"/><circle class="dk" cx="22" cy="0" r="3"/></g>'

A['burgan-oil-ecology'] = '<rect class="dk n" x="0" y="0" width="200" height="220" opacity=".55"/><rect class="s n" x="200" y="0" width="200" height="220"/>' + \
    '<path class="d2" d="M-2 150 H200 V222 H-2Z"/><path class="d" d="M200 150 H402 V222 H200Z"/>' + \
    ''.join(f'<path class="rd" d="M{x} 150 q-12 -20 0 -40 q4 10 8 4 q6 18 -8 36z"/><path class="su n" d="M{x+2} 148 q-6 -10 0 -20 q6 10 0 20z"/><path class="dk" d="M{x-6} 150 h14 v6 h-14z"/>' for x in (60, 130)) + \
    '<path class="dk n" d="M40 110 q20 -40 60 -30 q30 -30 60 0 q30 0 30 30z" opacity=".8"/>' + \
    sun(340, 40) + tuft(250, 180, 1) + tuft(310, 190, 1.1) + tuft(370, 176, 0.9) + \
    ''.join(f'<circle class="g" cx="{x}" cy="{y}" r="3"/>' for x, y in [(230, 206), (280, 210), (340, 206)]) + split()

A['umm-gudair-ecology'] = '<rect class="s2 n" width="400" height="220"/>' + \
    ground(110, 'd', 0) + \
    '<path class="d2" d="M-2 170 L402 130 V140 L-2 182Z"/><path class="r2" d="M-2 176 L402 136" stroke-width="5" fill="none"/>' + \
    ''.join(tuft(x, 168 - x * 0.1, 0.7) for x in range(20, 400, 40)) + \
    fox(170, 190, 1.1) + hedgehog(300, 170, 1) + \
    '<path class="l" d="M350 110 V70" stroke-width="3"/><path class="rd" d="M350 70 q-8 -12 0 -24 q8 12 0 24z"/><path class="su n" d="M350 68 q-4 -6 0 -12 q4 6 0 12z"/>'

A['um-al-rros-ecology'] = SKY + sun(330, 40) + ground(130, 'd', 0) + \
    '<path class="d2" d="M60 170 Q140 120 220 170Z"/><path class="dk" d="M110 170 q30 -16 60 0z"/>' + \
    lizard(140, 140, 1.2, 'wd') + \
    '<path class="l t" d="M240 200 h140 M240 210 h140 M250 196 v18 M270 196 v18 M290 196 v18 M310 196 v18 M330 196 v18 M350 196 v18 M370 196 v18" opacity=".6"/>' + \
    '<ellipse class="m2 n" cx="300" cy="166" rx="40" ry="8" opacity=".4"/>'

def flamingo(x, y, s=1):
    return bird_stand(x, y, s, 'rd', 'dk', 26)
A['khor-sabiyah-marsh'] = SKY + sun(64, 40) + birds([(260, 40), (280, 30), (300, 44)]) + \
    '<rect class="w2 n" x="0" y="130" width="400" height="30"/>' + '<path class="m" d="M-2 160 H402 V222 H-2Z"/>' + \
    ''.join(tuft(x, 164, 0.7) for x in range(10, 400, 36)) + \
    flamingo(150, 158, 0.9) + flamingo(200, 160, 1) + flamingo(250, 156, 0.85) + \
    ''.join(f'<circle class="dk n" cx="{x}" cy="{y}" r="2.5"/>' for x, y in [(60, 190), (120, 204), (200, 196), (280, 206), (340, 192)]) + arrow_up(372, 180, 24, 'wh', 180)

A['mubarak-reserve'] = SKY + sun(330, 36) + sea(90) + \
    '<g class="bob">' + dolphin(170, 92, 1.3) + '</g>' + \
    '<path class="wh n" d="M120 96 q10 -6 20 0 M200 96 q10 -6 20 0" />' + ripples([(110, 100), (230, 100), (60, 130), (300, 140)]) + \
    '<path class="m" d="M-2 190 Q200 176 402 190 V222 H-2Z"/>' + \
    ''.join(f'<path class="cl" d="M{x} 192 q-10 -6 -6 -14 q10 -2 14 8 q0 6 -8 6z"/>' for x in range(30, 400, 34)) + \
    fish(260, 170, 0.6, 'su') + fish(300, 160, 0.5, 'wh', True)

A['arfaj-steppe-habitat'] = SKY + sun(64, 40) + layers(140, [(80, 'd2')]) + surface(140) + \
    '<path class="g" d="M120 140 q-10 -30 20 -40 q10 -24 40 -18 q30 -8 40 16 q30 6 20 42z"/>' + \
    ''.join(f'<circle class="su" cx="{x}" cy="{y}" r="4"/>' for x, y in [(150, 104), (180, 92), (210, 98), (232, 116), (138, 124), (196, 118)]) + \
    '<path class="l" d="M180 140 q-20 30 -60 50 M180 140 q-6 40 -20 70 M180 140 q10 36 30 64 M180 140 q30 24 70 40" stroke-width="2.4"/>' + \
    '<path class="l t" d="M120 190 q-20 6 -30 20 M160 210 q-10 4 -14 10 M250 180 q20 4 30 16"/>' + lizard(310, 140, 0.9, 'wd') + \
    '<g transform="translate(90 110)"><ellipse class="su" cx="0" cy="0" rx="6" ry="4"/><path class="l t" d="M-3 -3 q-6 -6 -10 -2 M3 -3 q6 -6 10 -2"/></g>'

A['bubiyan-mangrove-plot'] = SKY + sun(330, 36) + \
    '<path class="l t" d="M200 40 l-10 10 M200 40 l10 10" opacity=".0"/>' + \
    '<rect class="w n" x="0" y="140" width="400" height="80"/><path class="l t" d="M0 140 H400"/>' + \
    ''.join(mangrove(x, 150, 0.9 - (i % 2) * 0.15) for i, x in enumerate(range(40, 400, 60))) + \
    ''.join(f'<path class="l t" d="M{x} 150 v-8"/>' for x in range(30, 400, 12)) + \
    fish(120, 190, 0.6, 'su') + fish(260, 196, 0.55, 'wh', True) + \
    cloud(176, 42, 0.7) + arrow_up(162, 96, 30, 'wh', 180)

A2 = {}
A2['spec-polychrome-escarpment'] = SKY + sun(52, 40, 18) + \
    '<defs><clipPath id="pc"><path d="M0 220 L0 186 L70 186 L100 78 Q130 58 180 56 L400 46 V220Z"/></clipPath></defs><g clip-path="url(#pc)">' + \
    layers(40, [(20, 'rd'), (16, 'su'), (18, 'pu'), (16, 'rd'), (14, 'wh'), (20, 'su'), (18, 'pu'), (64, 'rd')]) + '</g>' + \
    '<path class="l" d="M0 186 L70 186 L100 78 Q130 58 180 56 L400 46"/>' + sea(186) + \
    magnifier(300, 120, 30, '<rect class="rd n" x="-30" y="-30" width="60" height="20"/><rect class="pu n" x="-30" y="-10" width="60" height="20"/><rect class="su n" x="-30" y="10" width="60" height="20"/>') + qmark(300, 116, 0.7).replace('class="wh"', 'class="wh"')

A2['spec-submerged-kathma'] = SKY + sun(330, 36) + sea(80) + \
    '<g class="bob"><path class="wd" d="M80 80 q30 10 60 0 l-8 10 h-44z"/><path class="l" d="M110 80 V50" stroke-width="2.4"/><path class="wh" d="M112 52 L130 76 H112Z"/></g>' + \
    '<path class="m" d="M-2 190 Q200 176 402 190 V222 H-2Z"/>' + \
    '<ellipse class="dk" cx="250" cy="186" rx="60" ry="14" stroke-dasharray="6 4"/>' + qmark(250, 150, 0.8) + \
    '<g transform="translate(160 140) rotate(20)"><ellipse class="dk" cx="0" cy="0" rx="18" ry="7"/><circle class="sk" cx="20" cy="-2" r="6"/><rect class="w2" x="18" y="-6" width="8" height="5" rx="2"/><path class="l" d="M-18 0 l-12 -6 M-18 2 l-12 6" stroke-width="3"/></g>' + \
    '<g class="bub"><circle class="wh n rise" cx="184" cy="128" r="3"/><circle class="wh n rise d1s" cx="188" cy="120" r="2.4"/></g>'

A2['spec-failaka-platform'] = SKY + sun(64, 40) + sea(70) + \
    '<path class="d" d="M260 70 Q300 50 360 70Z"/>' + \
    '<path class="d2" d="M-2 160 L80 140 H300 L402 160 V222 H-2Z"/><path class="l" d="M80 140 H300" stroke-width="2.6"/>' + \
    '<g opacity=".6">' + person(150, 140, 0.8).replace('class="cl"', 'class="l"').replace('class="sk"', 'class="l"') + person(180, 140, 0.65).replace('class="cl"', 'class="l"').replace('class="sk"', 'class="l"') + '</g>' + \
    '<path class="l" d="M60 70 V140" stroke-dasharray="5 4"/>' + arrow_up(40, 136, 40, 'wh') + fish(240, 110, 0.7, 'su') + fish(320, 120, 0.6, 'wh', True)

A2['spec-bubiyan-paleotidal'] = '<rect class="w n" width="400" height="220"/>' + \
    '<path class="wh" d="M60 40 Q200 10 340 40 Q380 110 330 180 Q200 210 70 180 Q20 110 60 40Z"/>' + \
    '<g fill="none"><path class="l" stroke="var(--k-sea)" d="M60 100 q40 0 60 -20 q20 -20 40 -10 M120 80 q10 30 40 40 M160 70 q20 0 30 -20" stroke-width="3"/>' + \
    '<path class="l" d="M340 120 q-40 0 -60 20 q-20 20 -50 14 M280 140 q-6 24 -30 34 M230 154 q-10 -20 -40 -20" stroke-width="3"/>' + \
    '<path class="l" d="M100 160 q40 -10 70 0 q30 10 60 -4 M170 160 q0 -20 20 -30" stroke-dasharray="5 4"/></g>' + \
    satellite(340, 22) + magnifier(110, 150, 0)
A2['spec-bubiyan-paleotidal'] = A2['spec-bubiyan-paleotidal'].replace(magnifier(110, 150, 0), '')
A.update(A2)
