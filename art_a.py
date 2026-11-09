from art_lib import *
A = {}

def platform(x, y, rot, L=46):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><path class="r2" d="M-{L} 0 Q0 -16 {L} 0 Q0 16 -{L} 0Z"/>'
            f'<path class="l t" d="M-{L*0.6} 0 H{L*0.6}"/>' +
            ''.join(f'<circle class="r" cx="{dx}" cy="{dy}" r="3"/>' for dx, dy in [(-L*0.5, -3), (-L*0.2, -6), (L*0.15, -6), (L*0.45, -3), (-L*0.35, 5), (0, 6), (L*0.3, 5)]) + '</g>')
A['stone-platforms'] = SKY + sun(330, 70, 24) + sea(96) + ripples([(40, 108), (250, 112), (350, 104)]) + \
    '<path class="d" d="M-2 120 Q200 104 402 118 V222 H-2Z"/>' + \
    platform(90, 186, -18) + platform(200, 176, 0) + platform(312, 186, 18) + \
    '<g opacity=".7"><path class="l" d="M240 60 q40 16 80 0" stroke-dasharray="4 4"/><path class="l" d="M280 64 V36 M282 38 l14 20 h-14" stroke-dasharray="4 4"/></g>' + birds([(120, 50), (140, 40)])

A['shell-midden-smq24'] = SKY + sun(60, 40) + sea(150) + \
    '<path class="d" d="M120 222 L120 150 Q240 70 360 150 L360 222Z"/>' + \
    '<defs><clipPath id="mid"><path d="M120 222 L120 150 Q240 70 360 150 L360 222Z"/></clipPath></defs><g clip-path="url(#mid)">' + \
    layers(110, [(24, 'd2'), (22, 'cl'), (24, 'd2'), (22, 'cl'), (40, 'd2')], 100, 280) + \
    ''.join(shell(x, y, 0.75) for x, y in [(190, 126), (240, 120), (290, 128), (210, 150), (260, 156), (320, 150), (170, 172), (230, 178), (300, 176), (200, 200), (270, 204), (330, 198)]) + '</g>' + \
    '<path class="l" d="M120 150 Q240 70 360 150"/>' + person(250, 98, 0.7) + shell(272, 66, 0.8) + \
    '<path class="l t" d="M262 78 q6 -8 10 -12" stroke-dasharray="3 3"/>'

A['coastal-wells'] = SKY + sun(330, 40) + \
    '<rect class="w n" x="0" y="150" width="90" height="70"/><path class="l t" d="M0 150 H90"/>' + \
    '<path class="d" d="M60 150 Q80 140 120 138 L402 132 V222 H60Z"/>' + \
    '<rect class="w2 n" x="62" y="182" width="340" height="16" opacity=".75"/><path class="l t" d="M62 182 H402 M62 198 H402" opacity=".6"/>' + \
    arrow_up(40, 178, 30, 'wh', -90) + '<path class="l" d="M90 150 Q110 160 104 222" stroke-dasharray="5 4"/>' + \
    '<rect class="r" x="196" y="128" width="44" height="18" rx="4"/><ellipse class="dk" cx="218" cy="128" rx="18" ry="5"/>' + \
    '<path class="l" d="M218 128 V184" stroke-dasharray="3 3"/><path class="l" d="M200 128 V98 H236 V128" stroke-width="3"/><path class="l t" d="M218 98 V114"/><rect class="wd" x="212" y="114" width="12" height="10"/>' + \
    '<rect class="r2" x="262" y="140" width="40" height="10"/>' + camel(318, 152, 0.9) + \
    ''.join(f'<ellipse class="d2 n" cx="{x}" cy="{y}" rx="3" ry="2"/>' for x, y in [(340, 166), (352, 172), (366, 166), (378, 172)])

A['torpedo-jar-scatters'] = SKY + sun(64, 42) + sea(120) + ripples([(200, 134), (300, 140)]) + \
    '<g class="bob"><path class="wd" d="M250 118 q40 14 80 0 l-8 10 h-64z"/><path class="l" d="M290 118 V70" stroke-width="2.6"/><rect class="cl" x="268" y="74" width="44" height="34" rx="2"/></g>' + \
    '<path class="d" d="M-2 156 Q200 140 402 154 V222 H-2Z"/>' + \
    '<g transform="translate(110 186) rotate(-14)"><path class="r" d="M-34 0 q0 -11 22 -12 h26 q16 0 22 12 q-6 12 -22 12 h-26 q-22 -1 -22 -12z"/><path class="r" d="M34 0 l10 -3 v6z"/><path class="l t" d="M-14 -12 v24 M10 -12 v24"/></g>' + \
    '<path class="r" d="M220 196 l18 -14 l24 2 l-6 14z"/><path class="r" d="M282 200 q6 -12 20 -12 l10 6 l-14 10z"/><path class="r" d="M330 182 l14 -6 l8 8 l-12 6z"/>' + \
    '<path class="l t" d="M232 186 l20 2 M290 194 l12 2"/>'

A['kadhima'] = SKY + sun(340, 40) + sea(150) + \
    '<path class="d" d="M-2 128 Q160 118 300 150 L-2 160Z"/><path class="d" d="M-2 158 L300 150 Q340 160 402 180 V222 H-2Z"/>' + \
    palm(40, 132, 1) + palm(70, 134, 0.8) + \
    '<path class="w2" d="M100 142 q20 6 30 14 q-6 4 -16 0 q-6 -6 -14 -14z"/>' + drops([(108, 130), (118, 124)]) + \
    '<rect class="r" x="150" y="176" width="44" height="10" rx="3"/><rect class="r" x="204" y="178" width="40" height="10" rx="3"/>' + \
    camel(170, 176, 0.85) + camel(250, 182, 0.85) + camel(320, 190, 0.85) + \
    '<path class="l t" d="M186 150 l18 4 M276 160 l20 6" opacity=".5"/>'

A['akkaz-island'] = '<rect class="s n" width="400" height="220"/>' + sun(100, 36, 16) + \
    '<rect class="w n" x="0" y="110" width="400" height="110"/><path class="l t" d="M0 110 H400"/>' + \
    '<ellipse class="d" cx="100" cy="150" rx="62" ry="20"/>' + \
    '<path class="r" d="M92 146 q-6 -10 0 -20 h16 q6 10 0 20z"/><path class="l t" d="M94 132 h12"/>' + ripples([(20, 180), (150, 190), (40, 128)]) + \
    '<path class="d" d="M240 150 Q300 128 360 150 L402 160 V222 H230 L250 170Z"/><path class="d" d="M402 120 V160 L360 150Z"/>' + \
    '<rect class="cl" x="300" y="112" width="22" height="34"/><rect class="cl" x="326" y="100" width="26" height="46"/><rect class="cl" x="356" y="118" width="20" height="28"/>' + \
    '<path class="l t" d="M306 120 h10 M306 130 h10 M332 110 h14 M332 122 h14 M332 134 h14 M360 126 h12"/>' + \
    split() + '<path class="wh" d="M186 110 l14 -10 l14 10 l-7 0 v8 h-14 v-8z" transform="rotate(90 200 110)"/>'

A['umm-an-namil'] = SKY + sun(60, 40) + sea(120) + ripples([(30, 140), (330, 150), (80, 196)]) + \
    '<path class="d" d="M140 156 q-30 -18 0 -30 q30 -6 50 4 q60 4 90 10 q20 8 0 14 q-40 6 -90 6 q-30 6 -50 -4z"/>' + \
    '<path class="r" d="M170 140 q-5 -9 0 -16 h12 q5 7 0 16z"/><circle class="su" cx="220" cy="140" r="7"/><circle class="l t" cx="220" cy="140" r="4"/>' + \
    '<g class="bob"><path class="wd" d="M300 176 q24 10 48 0 l-6 9 h-36z"/><path class="l" d="M322 176 V140" stroke-width="2.4"/><path class="wh" d="M324 142 L344 172 H324Z"/></g>' + \
    '<path class="l t" d="M304 182 q-14 12 -20 24" stroke-dasharray="3 3"/><path class="l" d="M278 204 v10 M272 212 q6 6 12 0 M274 206 h8" stroke-width="2"/>'

A['bubiyan-island'] = '<rect class="s2 n" width="400" height="220"/>' + \
    '<path class="d2" d="M-2 0 H402 V60 Q300 70 200 64 Q100 70 -2 60Z"/>' + \
    '<path class="w2" d="M60 0 Q90 30 150 46 Q180 56 196 70 L208 70 Q190 50 160 38 Q110 22 86 0Z"/>' + \
    '<path class="w2" d="M340 0 Q310 30 250 46 Q220 56 206 70 L196 70 Q214 50 244 38 Q290 22 316 0Z"/>' + \
    '<rect class="w n" x="0" y="96" width="400" height="124"/><path class="l t" d="M0 96 H400"/>' + \
    '<path class="d" d="M120 100 Q200 76 300 104 Q340 140 300 176 Q220 196 150 176 Q100 140 120 100Z"/>' + \
    '<path class="l t" d="M200 96 q-10 20 -30 30 q-20 10 -24 30 M200 96 q10 24 30 34 q16 8 22 26 M200 120 q4 20 -6 40"/>' + \
    ''.join(f'<circle class="m n" cx="{x}" cy="{y}" r="2.2"/>' for x, y in [(110, 26), (140, 40), (170, 54), (290, 26), (262, 40), (232, 54), (200, 76), (204, 86)]) + \
    birds([(320, 140), (338, 130)])

A['kazma-shoreline'] = SKY + sun(340, 40) + \
    '<rect class="w2 n" x="0" y="96" width="400" height="34" opacity=".6"/><path class="l" d="M0 130 Q200 120 400 130" stroke-dasharray="6 5"/>' + \
    '<path class="d" d="M-2 130 Q200 120 402 130 V222 H-2Z"/>' + sea(180) + ripples([(60, 196), (250, 200)]) + \
    '<path class="l" d="M-2 180 H402"/>' + arrow_up(380, 176, 40, 'wh', 0) + \
    person(150, 160, 0.9) + \
    '<g transform="translate(176 146)"><path class="wd" d="M-12 0 h24 l-4 16 h-16z"/><path class="dk" d="M-11 4 h22 l-3 12 h-16z" opacity=".85"/><path class="l t" d="M-8 0 l2 16 M0 0 v16 M8 0 l-2 16 M-12 8 h24"/></g>' + \
    '<path class="l" d="M158 138 l12 6" stroke-width="2.4"/>'

A['smq-49-tomb'] = '<rect class="s2 n" width="400" height="220"/>' + sun(330, 60, 22) + \
    '<path class="d" d="M-2 120 H402 V222 H-2Z"/><path class="l" d="M0 120 H400"/>' + \
    '<path class="r" d="M90 120 a110 70 0 0 1 220 0Z"/>' + \
    '<path class="d2" d="M110 222 V160 H290 V222Z"/><path class="l" d="M110 160 H290 M200 160 V222 M150 160 V222 M250 160 V222"/>' + \
    '<path class="dk" d="M90 120 h220 v40 h-220z" opacity="0"/>' + \
    '<g transform="translate(225 200) scale(.8)" opacity=".85"><path class="wh" d="M-20 -14 q0 -10 14 -10 h18 q4 -10 12 -8 l4 6 q-4 4 -8 4 q0 6 -4 8 v20 h-4 v-14 h-18 v14 h-4 v-14 q-10 0 -10 -6z"/></g>' + \
    '<path class="r2" d="M168 206 q-5 -10 0 -18 h12 q5 8 0 18z"/><circle class="su" cx="275" cy="196" r="5"/>' + \
    '<ellipse class="r2" cx="200" cy="120" rx="130" ry="10" opacity=".0"/>'

A['atraf-ancient-wells'] = SKY + sun(60, 40) + \
    layers(110, [(36, 'd'), (26, 'w2'), (16, 'm'), (32, 'd2')]) + surface(110) + \
    '<path class="dk" d="M196 110 h16 v52 h-16z"/><path class="l" d="M196 110 V162 M212 110 V162"/>' + \
    '<path class="l" d="M188 110 V78 H220 V110" stroke-width="3"/><path class="l t" d="M204 78 V150"/><rect class="wd" x="198" y="146" width="12" height="10"/>' + \
    person(250, 110, 0.85) + '<path class="l" d="M240 86 L220 80" stroke-width="2.2"/>' + \
    drops([(120, 152), (300, 154), (60, 150)], 'w')

A['ghanim-paleochannel'] = SKY + sun(340, 40) + \
    layers(118, [(102, 'd2')]) + surface(118) + \
    '<path class="w2" d="M-2 170 Q60 150 120 172 T240 170 T402 176 V196 Q340 190 240 192 T120 194 T-2 192Z"/>' + \
    hut(150, 118, 0.8) + hut(200, 118, 0.7) + hut(240, 118, 0.75) + \
    '<path class="l" d="M290 118 V178" stroke-dasharray="4 3"/><path class="l" d="M280 118 V96 H300 V118" stroke-width="2.6"/>' + \
    arrow_up(80, 168, 34, 'wh') + arrow_up(340, 172, 34, 'wh')

A['faydhat-nayif-smelter'] = SKY + \
    ground(150, 'd', 6) + \
    '<path class="r" d="M150 150 L160 70 h40 l10 80z"/><ellipse class="dk" cx="180" cy="70" rx="20" ry="5"/>' + \
    '<path class="dk" d="M168 150 v-22 a12 12 0 0 1 24 0 v22z"/><path class="rd n" d="M180 150 q-8 -12 0 -20 q8 8 0 20z"/><path class="su n" d="M180 150 q-4 -6 0 -10 q4 4 0 10z"/>' + \
    '<g class="smoke"><path class="l t rise" d="M176 62 q-6 -8 0 -16 q6 -8 0 -16"/><path class="l t rise d1s" d="M186 64 q-6 -8 0 -16 q6 -8 0 -16"/></g>' + \
    person(250, 168, 0.9) + '<path class="wd" d="M218 152 l18 -8 l4 8 l-18 6z"/>' + \
    ''.join(f'<ellipse class="dk" cx="{x}" cy="{y}" rx="{r}" ry="{r*0.7}"/>' for x, y, r in [(70, 176, 14), (92, 180, 10), (58, 186, 9), (80, 192, 12), (104, 192, 8)]) + \
    '<path class="l" d="M300 190 h80 v-24 h-80z M326 166 v24 M352 166 v24"/>' + \
    '<rect class="rd" x="200" y="176" width="26" height="6" rx="2"/>'

A['subbiya-desert-wall'] = SKY + sun(330, 40) + ground(110, 'd2', 0) + \
    '<path class="d" d="M-2 150 Q200 136 402 150 V222 H-2Z"/>' + \
    '<path class="r" d="M30 210 Q120 170 200 150 Q280 132 380 116 l2 6 Q282 140 202 158 Q124 178 38 216z"/>' + \
    ''.join(f'<circle class="r2" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(50, 204, 4), (90, 188, 3.6), (130, 174, 3.2), (170, 162, 3), (210, 152, 2.6), (250, 144, 2.4), (290, 136, 2.2), (330, 128, 2), (365, 121, 1.8)]) + \
    camel(236, 196, 0.75) + camel(280, 190, 0.7) + \
    '<g transform="translate(190 60)">' + cloud(0, 0, 1) + '</g>' + qmark(196, 56, 0.55).replace('class="wh"', 'class="dk"')
