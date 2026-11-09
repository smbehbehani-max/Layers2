SKY = '<rect class="s n" width="400" height="220"/>'
def sun(x, y, r=20):
    return f'<circle class="su" cx="{x}" cy="{y}" r="{r}"/>'
def person(x, y, s=1, cloth='cl'):
    # simple seated/standing figure, feet at (x,y)
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path class="{cloth}" d="M-13 0 Q-11 -30 0 -32 Q11 -30 13 0 Z"/>'
            f'<circle class="sk" cx="0" cy="-40" r="8.5"/>'
            f'<path class="l t" d="M-4 -41 h0.1 M4 -41 h0.1" stroke-width="2.6"/></g>')
def birds(pts):
    return ''.join(f'<path class="l t" d="M{x-7} {y} q3.5 -4 7 0 q3.5 -4 7 0"/>' for x, y in pts)
def shell(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="wh" d="M0 8 C-9 6 -10 -6 0 -8 C8 -9 10 0 4 3 C0 5 -3 1 0 -1"/></g>')

ART = {}

# 1 Bahra 1 — The Shell Workshop
ART['bahra-1'] = SKY + sun(345, 42) + birds([(250, 40), (275, 30)]) + '''
<path class="d n" d="M0 148 Q200 132 400 148 V220 H0Z"/>
<path class="l t" d="M0 148 Q200 132 400 148"/>
<rect class="d2" x="34" y="78" width="146" height="72" rx="3"/>
<path class="l t" d="M34 102 H180 M34 126 H180 M70 78 V102 M120 78 V102 M160 78 V102 M52 102 V126 M100 102 V126 M146 102 V126 M70 126 V150 M150 126 V150"/>
<rect class="cl" x="28" y="70" width="158" height="10" rx="3"/>
<path class="dk" d="M92 150 V116 a14 14 0 0 1 28 0 V150Z"/>
<path class="r" d="M246 150 a28 28 0 0 1 56 0Z"/>
<path class="dk" d="M262 150 a12 12 0 0 1 24 0Z"/>
<path class="rd n" d="M274 149 q-7 -9 0 -16 q7 7 0 16z"/>
<path class="r" d="M310 150 a19 19 0 0 1 38 0Z"/>
<path class="dk" d="M321 150 a8 8 0 0 1 16 0Z"/>
<g class="smoke"><path class="l t rise" d="M274 118 q-6 -8 0 -16 q6 -8 0 -16"/><path class="l t rise d2s" d="M329 128 q-5 -7 0 -14 q5 -7 0 -14"/></g>
''' + person(205, 178, 1) + '''
<path class="l" d="M196 158 L214 166"/>
''' + shell(218, 166, 0.9) + shell(232, 190, 0.8) + shell(250, 196, 0.7) + shell(240, 202, 0.75) + '''
<ellipse class="r" cx="150" cy="182" rx="17" ry="6"/>
<ellipse class="d2" cx="150" cy="166" rx="9" ry="12"/>
<path class="d2" d="M142 157 l2 -8 l4 6 M158 157 l-2 -8 l-4 6"/>
<circle class="wh" cx="146.5" cy="163" r="3.4"/><circle class="wh" cx="153.5" cy="163" r="3.4"/>
<circle class="k n" cx="146.5" cy="163" r="1.4"/><circle class="k n" cx="153.5" cy="163" r="1.4"/>
<path class="su" d="M148 168 l2 3 l2 -3z"/>
'''

# 2 H3 — Where Sailing Began
ART['h3-site'] = SKY + sun(62, 48, 22) + birds([(120, 40), (140, 52), (330, 36)]) + '''
<rect class="w n" x="0" y="140" width="400" height="80"/>
<path class="l t" d="M0 140 H400"/>
<path class="w2 n" d="M0 160 q12 -5 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 V168 H0Z" opacity=".7"/>
<path class="d" d="M0 138 Q70 120 140 150 Q80 158 0 166Z"/>
<path class="l t g2s" d="M18 140 v-22 M26 138 v-28 M34 138 v-20 M44 139 v-26 M54 141 v-18"/>
<g class="bob">
<path class="wd" d="M146 136 C172 168 288 168 314 136 C302 158 264 174 230 174 C196 174 158 158 146 136Z"/>
<path class="l t" d="M172 152 l-4 10 M196 160 l-2 11 M230 162 v12 M262 160 l2 11 M288 152 l4 10"/>
<path class="l" d="M205 162 V70 M255 162 V82" stroke-width="3"/>
<path class="wh" d="M208 74 L246 122 L208 130Z"/>
<path class="wh" d="M258 86 L292 126 L258 132Z"/>
<circle class="wh" cx="180" cy="163" r="2.2"/><circle class="wh" cx="186" cy="166" r="1.8"/><circle class="wh" cx="276" cy="165" r="2"/>
</g>
<circle class="r" cx="352" cy="184" r="27"/>
<circle class="l t" cx="352" cy="184" r="21" stroke-dasharray="2 3"/>
<path class="l" d="M334 188 q18 10 36 0 M345 191 V170 M359 191 V173 M346 172 l9 12 M360 175 l7 10" stroke-width="2"/>
'''

# 3 Subiyah tumuli — Hill of a Hundred Graves
def mound(x, y, r):
    return (f'<ellipse class="r2" cx="{x}" cy="{y}" rx="{r*1.35}" ry="{r*0.32}"/>'
            f'<path class="r" d="M{x-r} {y} a{r} {r*0.85} 0 0 1 {2*r} 0Z"/>'
            f'<path class="l t" d="M{x-r*0.55} {y-r*0.35} q{r*0.3} -4 {r*0.55} 0 M{x+r*0.1} {y-r*0.55} q{r*0.25} -3 {r*0.5} 0"/>')
ART['subiyah-tumuli'] = '<rect class="s2 n" width="400" height="220"/>' + sun(320, 108, 30) + '''
<path class="w2" d="M0 118 H400 V132 H0Z"/>
<path class="d2" d="M0 132 L400 124 V220 H0Z"/>
<path class="d" d="M0 166 L400 156 V220 H0Z"/>
''' + ''.join(mound(*m) for m in [(60, 138, 20), (128, 135, 16), (192, 133, 14), (250, 131, 11), (300, 129, 9), (350, 128, 7)]) \
    + ''.join(mound(*m) for m in [(96, 178, 30), (220, 172, 25), (334, 167, 19)]) + '''
<path class="l t" d="M20 206 q40 14 80 0"/>
<circle class="rd" cx="30" cy="209" r="4"/><circle class="su" cx="44" cy="213" r="4"/><circle class="w" cx="58" cy="214" r="4"/><circle class="rd" cx="72" cy="213" r="4"/><circle class="pu" cx="86" cy="209" r="4"/>
''' + birds([(150, 60), (170, 70)])

# 4 Failaka — Island of Four Thousand Years
ART['failaka-island'] = SKY + sun(58, 44, 20) + '''
<rect class="w n" x="0" y="128" width="400" height="92"/>
<path class="l t" d="M0 128 H400"/>
<path class="d" d="M60 166 Q110 112 200 116 Q300 110 352 166Z"/>
<rect class="wh" x="104" y="128" width="62" height="8" rx="1"/>
<path class="wh" d="M100 108 L135 92 L170 108Z"/>
<rect class="wh" x="104" y="108" width="62" height="5"/>
<path class="l" d="M112 113 V128 M124 113 V128 M136 113 V128 M148 113 V128 M160 113 V128" stroke-width="3"/>
<rect class="r" x="262" y="96" width="34" height="46"/>
<path class="r" d="M260 96 v-8 h7 v5 h6 v-5 h7 v5 h6 v-5 h7 v5 h5 v8z"/>
<path class="dk" d="M273 142 v-14 a6 6 0 0 1 12 0 v14z"/>
<path class="l" d="M212 140 q-2 -26 4 -40" stroke-width="3"/>
<path class="g" d="M216 100 q-16 -6 -24 4 q12 -2 24 -4z M216 100 q14 -10 26 -2 q-12 0 -26 2z M216 100 q-6 -14 4 -20 q-2 10 -4 20z"/>
<g class="bob"><path class="wd" d="M318 186 q22 10 46 0 l-6 8 h-34z"/><path class="l" d="M338 186 V150" stroke-width="2.5"/><path class="wh" d="M340 150 L362 182 H340Z"/></g>
<path class="l t" d="M30 178 q10 -4 20 0 M80 196 q10 -4 20 0 M240 200 q10 -4 20 0"/>
<circle class="r" cx="46" cy="196" r="20"/>
<circle class="l t" cx="46" cy="196" r="14"/>
<path class="l t" d="M38 200 l4 -10 l4 10 l4 -10 l4 10"/>
<circle class="k n" cx="46" cy="186" r="1.8"/>
'''

# 5 Kazima — The Battle of the Chains (the escarpment as a funnel)
ART['kazima-battle-site'] = SKY + sun(80, 40, 18) + '''
<path class="r" d="M0 118 L110 98 L230 76 L400 62 V112 Q300 116 220 132 Q120 146 0 150Z"/>
<path class="l t" d="M40 128 L150 108 M150 116 L280 94 M250 102 L380 82"/>
<path class="d" d="M0 150 Q120 146 220 132 Q300 116 400 112 V220 H0Z"/>
<path class="wh" d="M40 190 l14 -22 l14 22z"/><path class="wh" d="M70 196 l12 -19 l12 19z"/><path class="wh" d="M22 202 l11 -17 l11 17z"/>
<path class="l" d="M54 168 v-16 M82 177 v-14" stroke-width="2.4"/><path class="rd" d="M54 152 h12 l-4 4 l4 4 h-12z"/><path class="rd" d="M82 163 h11 l-4 4 l4 4 h-11z"/>
<path class="l" d="M318 168 v-24 M338 176 v-26 M358 168 v-22" stroke-width="2.4"/>
<path class="g" d="M318 144 h14 l-5 5 l5 5 h-14z"/><path class="g" d="M338 150 h14 l-5 5 l5 5 h-14z"/><path class="g" d="M358 146 h14 l-5 5 l5 5 h-14z"/>
<path class="l" d="M110 182 Q170 168 205 158 M300 176 Q250 166 215 158" stroke-dasharray="7 6" stroke-width="2.6"/>
<path class="k" d="M205 158 l-10 -1 l4 8z M215 158 l9 -2 l-3 8z"/>
<ellipse class="l" cx="160" cy="206" rx="11" ry="6" stroke-width="3"/><ellipse class="l" cx="178" cy="206" rx="11" ry="6" stroke-width="3"/><ellipse class="l" cx="196" cy="206" rx="11" ry="6" stroke-width="3"/>
''' + birds([(260, 40), (282, 30)])

# 6 Jal Az-Zor — The Great Cliff (striped layers, uplift)
ART['jal-az-zor'] = SKY + sun(52, 40, 18) + '''
<defs><clipPath id="jz"><path d="M0 220 L0 186 L70 186 L100 78 Q130 58 180 56 L400 46 V220Z"/></clipPath></defs>
<g clip-path="url(#jz)">
<rect class="r n" x="0" y="40" width="400" height="30"/>
<rect class="d n" x="0" y="70" width="400" height="18"/>
<rect class="pu n" x="0" y="88" width="400" height="16" opacity=".85"/>
<rect class="r2 n" x="0" y="104" width="400" height="22"/>
<rect class="d2 n" x="0" y="126" width="400" height="16"/>
<rect class="wh n" x="0" y="142" width="400" height="10"/>
<rect class="r n" x="0" y="152" width="400" height="34"/>
<path class="l t" d="M0 70 H400 M0 88 H400 M0 104 H400 M0 126 H400 M0 142 H400 M0 152 H400" opacity=".6"/>
</g>
<path class="l" d="M0 186 L70 186 L100 78 Q130 58 180 56 L400 46"/>
''' + shell(150, 96, 0.8) + shell(210, 100, 0.7) + shell(270, 94, 0.75) + '''
<rect class="w n" x="0" y="186" width="400" height="34"/>
<path class="l t" d="M0 186 H70 M20 200 q10 -4 20 0 M120 206 q10 -4 20 0 M300 202 q10 -4 20 0"/>
<path class="wh" d="M352 150 v-46 h-12 l20 -24 l20 24 h-12 v46z"/>
''' + person(250, 52, 0.55)

# 7 Mud volcanoes — Where the Earth Bubbles
ART['mud-volcano-z1'] = SKY + sun(340, 40, 18) + '''
<rect class="d2 n" x="0" y="120" width="400" height="100"/>
<rect class="d n" x="0" y="150" width="400" height="22"/>
<rect class="m2 n" x="0" y="190" width="400" height="30"/>
<path class="l t" d="M0 150 H400 M0 172 H400 M0 190 H400" opacity=".6"/>
<path class="l" d="M0 120 H400"/>
<path class="m" d="M80 120 L126 66 h22 L194 120Z"/>
<ellipse class="m2" cx="137" cy="66" rx="12" ry="4"/>
<path class="m2" d="M128 68 q-4 8 -10 14 q8 -2 12 -10z M146 68 q4 8 10 14 q-8 -2 -12 -10z"/>
<path class="m" d="M248 120 L276 92 h14 L318 120Z"/>
<ellipse class="m2" cx="283" cy="92" rx="8" ry="3"/>
<g class="bub"><circle class="m n rise" cx="137" cy="58" r="5"/><circle class="m n rise d1s" cx="131" cy="56" r="3.5"/><circle class="m n rise d2s" cx="143" cy="54" r="4"/><circle class="m n rise d1s" cx="283" cy="86" r="3"/></g>
<path class="l" d="M140 120 L148 142 L132 160 L146 180 L138 200" stroke-width="2.6" stroke-dasharray="1 0"/>
<ellipse class="m2" cx="150" cy="204" rx="56" ry="12"/>
<path class="wh" d="M90 182 v-18 h-6 l10 -12 l10 12 h-6 v18z" opacity=".9"/>
<path class="wh" d="M196 182 v-18 h-6 l10 -12 l10 12 h-6 v18z" opacity=".9"/>
<circle class="wh" cx="141" cy="170" r="2.4"/><circle class="wh" cx="139" cy="150" r="2"/><circle class="wh" cx="145" cy="132" r="1.8"/>
'''

# 8 Paleo-liquefaction — The Day the Ground Turned to Liquid
ART['paleo-liquefaction'] = SKY + '''
<path class="l t shake" d="M12 60 l8 -8 l6 10 l8 -10 l6 8 M352 50 l8 -8 l6 10 l8 -10 l6 8"/>
<rect class="d n" x="0" y="112" width="400" height="108"/>
<rect class="w2 n" x="0" y="158" width="400" height="44" opacity=".75"/>
<rect class="d2 n" x="0" y="202" width="400" height="18"/>
<path class="l t" d="M0 158 H400 M0 202 H400" opacity=".6"/>
<g fill="none"><circle class="wh n" cx="40" cy="176" r="2"/><circle class="wh n" cx="90" cy="186" r="2"/><circle class="wh n" cx="300" cy="172" r="2"/><circle class="wh n" cx="350" cy="190" r="2"/><circle class="wh n" cx="250" cy="192" r="2"/><circle class="wh n" cx="140" cy="170" r="2"/></g>
<path class="l" d="M0 112 H170 M230 112 H400"/>
<path class="d2" d="M186 202 L194 112 h12 L214 202Z"/>
<path class="l t" d="M196 190 v-10 M204 170 v-12 M198 146 v-10 M203 128 v-8"/>
<path class="d2" d="M170 112 Q200 92 230 112Z"/>
<g class="burst"><circle class="d2 rise" cx="200" cy="96" r="6"/><circle class="d2 rise d1s" cx="186" cy="90" r="4.5"/><circle class="d2 rise d2s" cx="214" cy="88" r="5"/><circle class="d2 rise d1s" cx="200" cy="80" r="3.5"/></g>
<g transform="rotate(-10 92 112)"><rect class="cl" x="70" y="80" width="44" height="32"/><path class="wd" d="M64 82 L92 60 L120 82Z"/><rect class="dk" x="86" y="94" width="12" height="18"/></g>
<g transform="rotate(12 312 112)"><rect class="cl" x="292" y="86" width="38" height="26"/><path class="wd" d="M286 88 L311 68 L336 88Z"/><rect class="dk" x="305" y="96" width="10" height="16"/></g>
<path class="l" d="M140 112 q4 -30 -6 -50" stroke-width="3"/>
<path class="g" d="M134 62 q-16 -4 -22 8 q12 -4 22 -8z M134 62 q12 -10 24 -2 q-12 -1 -24 2z"/>
'''

# 9 Sabah Al-Ahmad Reserve — The Desert Comes Back to Life
def tuft(x, y, s=1):
    return f'<path class="g" d="M{x} {y} q{-6*s} {-14*s} {-10*s} {-18*s} q{6*s} {4*s} {10*s} {12*s} q{0} {-12*s} {4*s} {-20*s} q{2*s} {10*s} {0} {20*s} q{4*s} {-10*s} {10*s} {-14*s} q{-2*s} {8*s} {-4*s} {20*s}z"/>'
ART['sabah-al-ahmad-reserve'] = SKY + sun(330, 44, 22) + '''
<path class="d2" d="M0 132 Q90 112 190 128 T400 122 V220 H0Z"/>
<path class="d" d="M0 160 Q120 146 240 160 T400 156 V220 H0Z"/>
<path class="l t" d="M8 150 V118 M48 146 V114 M88 144 V112 M8 124 H88 M8 136 H88"/>
''' + ''.join(tuft(x, y, s) for x, y, s in [(130, 170, 1), (170, 178, .8), (300, 176, 1.1), (360, 170, .9), (40, 190, 1), (250, 196, .9), (110, 204, .8), (340, 206, 1)]) + '''
<g transform="translate(210 150)">
<ellipse class="wh" cx="0" cy="0" rx="28" ry="13"/>
<path class="l" d="M-18 10 v20 M-8 12 v19 M10 12 v19 M20 10 v20" stroke-width="3"/>
<path class="wh" d="M22 -6 q10 -10 18 -6 q4 6 -2 12 q-8 4 -16 2z"/>
<path class="dk" d="M34 -10 q6 2 6 8 q-4 2 -8 -2z"/>
<path class="l" d="M32 -12 L18 -40 M36 -12 L26 -40" stroke-width="2.4"/>
<path class="l t" d="M-28 -2 q-8 6 -4 14"/>
</g>
<g transform="translate(96 168) scale(.7)">
<ellipse class="r" cx="0" cy="0" rx="24" ry="11"/>
<path class="l" d="M-14 8 v20 M-6 10 v19 M8 10 v19 M16 8 v20" stroke-width="3"/>
<path class="r" d="M18 -6 q10 -8 16 -4 q2 6 -4 10 q-6 2 -12 0z"/>
<path class="l" d="M28 -10 q-4 -14 2 -22 M32 -10 q2 -14 8 -20" stroke-width="2.4"/>
<path class="wh n" d="M-20 2 h36 v4 h-36z" opacity=".8"/>
</g>
''' + birds([(160, 50), (182, 40)])

# 10 Dark seepage mounds — The Dark Circles (satellite view)
ART['spec-seepage-mounds'] = '''
<rect class="d n" width="400" height="220"/>
<path class="l t" d="M0 60 Q100 40 200 70 T400 50 M0 150 Q120 130 240 160 T400 140" opacity=".45"/>
<g opacity=".9">
<ellipse class="m2" cx="70" cy="80" rx="16" ry="14"/><ellipse class="m2" cx="120" cy="140" rx="22" ry="19"/>
<ellipse class="m2" cx="185" cy="60" rx="12" ry="11"/><ellipse class="m2" cx="60" cy="176" rx="14" ry="13"/>
<ellipse class="m2" cx="160" cy="190" rx="10" ry="9"/><ellipse class="m2" cx="215" cy="125" rx="9" ry="8"/>
</g>
<g transform="translate(286 128)">
<circle class="s" cx="0" cy="0" r="50" opacity=".55"/>
<ellipse class="m2" cx="-6" cy="4" rx="30" ry="26" stroke-dasharray="5 4"/>
<path class="wh" d="M-14 -4 q0 -14 14 -14 q14 0 14 12 q0 9 -12 13 v6 h-6 v-10 q11 -3 11 -9 q0 -5 -7 -5 q-7 0 -7 7z"/>
<circle class="wh" cx="-1" cy="22" r="3.6"/>
<circle class="l" cx="0" cy="0" r="50" stroke-width="7"/>
<circle class="l t" cx="0" cy="0" r="50"/>
<path class="l" d="M36 36 L64 64" stroke-width="12"/>
</g>
<g transform="translate(70 26)">
<rect class="wh" x="-10" y="-8" width="20" height="16" rx="3"/>
<rect class="w" x="-40" y="-6" width="26" height="12"/><rect class="w" x="14" y="-6" width="26" height="12"/>
<path class="l t" d="M-27 -6 v12 M27 -6 v12 M-14 0 h4 M10 0 h4"/>
<path class="l t" d="M0 8 L-30 160 M0 8 L40 150" stroke-dasharray="4 5" opacity=".6"/>
</g>
'''

def wrap(body):
    return f'<svg viewBox="0 0 400 220" aria-hidden="true">{body}</svg>'
ART = {k: wrap(v) for k, v in ART.items()}
