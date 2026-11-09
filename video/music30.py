"""Original soundtrack for the GeoHeritage ad: 96 BPM, D minor (Dorian colour), 60 s.
Bars are 2.5 s and line up with the cuts: hooks 0/2.5/5, reveal 7.5, app 12.5, end card 52.5, final chord 57.5.
Everything is synthesised here (no samples)."""
import json, sys
import numpy as np
from scipy.signal import lfilter, butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 30.0
N = int(SR * DUR)
BEAT = 0.625
BAR = 2.5
rng = np.random.default_rng(7)
clicks = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else []

L = np.zeros(N); R = np.zeros(N)          # dry bus
RL = np.zeros(N); RR = np.zeros(N)        # reverb send

def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def put(sig, t, gain=1.0, pan=0.0, send=0.0):
    i = int(t * SR)
    if i >= N: return
    s = sig[: N - i] * gain
    gl, gr = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    L[i:i + len(s)] += s * gl; R[i:i + len(s)] += s * gr
    if send:
        RL[i:i + len(s)] += s * gl * send; RR[i:i + len(s)] += s * gr * send
def lp(x, fc, order=2):
    return sosfilt(butter(order, fc / (SR / 2), 'low', output='sos'), x)
def hp(x, fc, order=2):
    return sosfilt(butter(order, fc / (SR / 2), 'high', output='sos'), x)
def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo / (SR / 2), hi / (SR / 2)], 'band', output='sos'), x)
def env(n, a, d, sustain=0.0, r=None):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4))
    e *= np.where(t < a, 1, sustain + (1 - sustain) * np.exp(-(t - a) / max(d, 1e-4)))
    if r: e *= np.clip((n / SR - t) / r, 0, 1)
    return e

# ---------------- harmony ----------------
CH = {  # pad voicing, bass root, arpeggio notes
    'Dm': ([50, 57, 62, 65, 64], 38, [62, 65, 69, 76]),
    'Bb': ([46, 53, 58, 62, 69], 34, [58, 62, 65, 69]),
    'Gm': ([43, 50, 55, 58, 62], 31, [62, 67, 70, 74]),
    'A':  ([45, 52, 57, 61, 64], 33, [61, 64, 69, 73]),
    'F':  ([41, 53, 60, 65, 69], 41, [60, 65, 69, 72]),
    'C':  ([48, 55, 60, 64, 67], 36, [60, 64, 67, 72]),
    'D':  ([50, 57, 62, 66, 69], 38, [62, 66, 69, 74]),
}
# (start time, length, chord)
prog = [(0, 2.5, 'Dm'), (2.5, 1.25, 'Gm'), (3.75, 1.25, 'A'), (5.0, 2.5, 'F'), (7.5, 2.5, 'C')]
loop = ['Dm', 'Bb', 'F', 'C']
for b in range(5):
    prog.append((10.0 + 2.5 * b, 2.5, loop[b % 4]))
prog += [(22.5, 2.5, 'Bb'), (25.0, 2.5, 'C'), (27.5, 2.5, 'D')]

def saw(f, n, det=0.0):
    t = np.arange(n) / SR
    ph = (f * (1 + det) * t + rng.random()) % 1.0
    return 2 * ph - 1

# ---------------- pad ----------------
for (t0, ln, c) in prog:
    notes = CH[c][0]
    hold = ln + 0.9 if t0 < 27 else DUR - t0
    n = int(hold * SR)
    sig = np.zeros(n)
    for m in notes:
        f = mtof(m)
        for det in (-0.004, 0.0, 0.0045):
            sig += saw(f, n, det)
    cut = 900 if t0 < 5.0 else (1500 if t0 < 22.5 else 1300)
    sig = lp(sig, cut, 2) / (len(notes) * 3)
    e = env(n, 0.5 if t0 > 0 else 1.2, 9.0, 1.0, r=0.85 if t0 < 27 else 2.4)
    g = 0.62 if t0 < 5.0 else (0.34 if t0 < 22.5 else 0.40)
    if t0 >= 27.5: g = 0.5
    put(sig * e, t0, g, 0.0, 0.55)

# ---------------- plucked arpeggio (Karplus-Strong) ----------------
def pluck(f, dur=1.6, bright=0.5, decay=0.996):
    n = int(dur * SR); P = max(2, int(round(SR / f - 0.5)))
    x = np.zeros(n); burst = rng.uniform(-1, 1, P)
    burst = lfilter([1 - bright], [1, -bright], burst)  # soften the attack
    x[:P] = burst
    a = np.zeros(P + 2); a[0] = 1; a[P] = -0.5 * decay; a[P + 1] = -0.5 * decay
    y = lfilter([1], a, x)
    y = lp(y, 5200, 2)
    return y * env(n, 0.002, dur * 0.45, 0.0, r=0.08)

PAT = [0, 2, 1, 3, 2, 1, 3, 2]
for (t0, ln, c) in prog:
    arp = CH[c][2]
    steps = int(round(ln / (BEAT / 2)))
    for k in range(steps):
        t = t0 + k * BEAT / 2
        if t >= 29.0: break
        intro = t < 5.0
        if intro and k % 2: continue          # quarter notes during the hooks
        m = arp[PAT[k % 8]] + (12 if (t >= 10.0 and t < 22.5 and k % 8 == 7) else 0)
        vel = 0.9 if k % 4 == 0 else 0.62
        if intro: vel *= 1.05
        if 22.5 <= t < 27.5: vel *= 0.8 * (1 - (t - 22.5) / 6)
        if t >= 27.5: continue
        put(pluck(mtof(m), 1.4 if not intro else 2.2, 0.42), t, 0.23 * vel, 0.35 if k % 2 else -0.3, 0.45)
# final chord: rolled plucks
for i, m in enumerate([50, 57, 62, 66, 69, 74]):
    put(pluck(mtof(m), 3.0, 0.35, 0.998), 27.5 + i * 0.045, 0.22, -0.4 + i * 0.16, 0.6)

# ---------------- bass ----------------
def bass(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    s = np.tanh(1.6 * s) / 1.2
    return s * env(n, 0.006, dur * 0.6, 0.0, r=0.06)
for (t0, ln, c) in prog:
    if t0 < 5.0: continue
    f = mtof(CH[c][1])
    if t0 < 10.0:             # reveal: long notes
        put(bass(f, 2.4), t0, 0.32, 0, 0.05); continue
    if t0 >= 27.5:
        put(bass(f, 2.5), t0, 0.34, 0, 0.05); continue
    for bt, d in ((0, 0.9), (1.5, 0.5), (2.5, 0.8), (3.5, 0.3)):
        if bt * BEAT >= ln: continue
        put(bass(f, d), t0 + bt * BEAT, 0.3 if bt == 0 else 0.22, 0, 0.04)

# ---------------- drums: maqsum on frame drum + shaker ----------------
def doum():
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 52 + 70 * np.exp(-t / 0.045)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)
    s += 0.25 * lp(rng.uniform(-1, 1, n), 900) * np.exp(-t / 0.02)
    return s
def tak():
    n = int(0.16 * SR); t = np.arange(n) / SR
    s = bp(rng.uniform(-1, 1, n), 1800, 6000) * np.exp(-t / 0.035)
    s += 0.5 * np.sin(2 * np.pi * 720 * t) * np.exp(-t / 0.025)
    return s
def shaker():
    n = int(0.09 * SR); t = np.arange(n) / SR
    return hp(rng.uniform(-1, 1, n), 6500) * env(n, 0.012, 0.03)
D, Tk, Sh = doum(), tak(), shaker()
MAQ = {0: 'D', 1: 'T', 3: 'T', 4: 'D', 6: 'T'}
for b in range(5 + 2):
    t0 = 10.0 + 2.5 * b
    light = b >= 5                       # first two bars of the end card: doum only
    for k in range(8):
        t = t0 + k * BEAT / 2
        h = MAQ.get(k)
        if h == 'D': put(D, t, 0.62 if k == 0 else 0.5, 0, 0.12)
        elif h == 'T' and not light: put(Tk, t, 0.2, 0.25, 0.15)
        elif not light and k in (2, 7) and b % 2: put(Tk, t, 0.07, -0.25, 0.1)   # ghost notes
    if not light:
        for k in range(16):
            put(Sh, t0 + k * BEAT / 4, 0.05 if k % 2 else 0.028, -0.5 if k % 4 < 2 else 0.5, 0.05)
# soft heartbeat doums under the reveal
for t in (5.0, 6.25, 7.5, 8.75):
    put(D, t, 0.4, 0, 0.2)

# ---------------- effects ----------------
def whoosh(d=0.5, lo=500, hi=4000):
    n = int(d * SR); t = np.arange(n) / SR
    s = rng.uniform(-1, 1, n); k = t / d
    out = np.zeros(n); segs = 12
    for i in range(segs):   # sweep a band upwards in short chunks
        a, b2 = int(i * n / segs), int((i + 1) * n / segs)
        c = lo * (hi / lo) ** (i / segs)
        out[a:b2] = bp(s, c * 0.7, min(c * 1.4, SR / 2 - 100))[a:b2]
    return out * np.sin(np.pi * k) ** 2
for t in (2.42,):
    put(whoosh(0.32, 900, 7000), t - 0.12, 0.16, 0, 0.3)
put(whoosh(0.55, 400, 5000), 9.7, 0.14, 0, 0.3)
for t in (12.5, 16.25, 20.0):
    put(whoosh(0.3, 900, 6500), t - 0.16, 0.09, 0, 0.3)
# riser into the reveal
n = int(1.7 * SR); tt = np.arange(n) / SR
rs = np.zeros(n); src = rng.uniform(-1, 1, n)
for i in range(20):
    a, b2 = int(i * n / 20), int((i + 1) * n / 20); c = 300 * (12 ** (i / 20))
    rs[a:b2] = bp(src, c * .7, c * 1.5)[a:b2]
put(rs * (tt / 1.7) ** 2.2, 3.3, 0.32, 0, 0.4)
# impact at 7.5
n = int(2.2 * SR); tt = np.arange(n) / SR
boom = np.sin(2 * np.pi * np.cumsum(40 + 60 * np.exp(-tt / 0.06)) / SR) * np.exp(-tt / 0.7)
boom += 0.4 * lp(rng.uniform(-1, 1, n), 2500) * np.exp(-tt / 0.12)
put(boom, 5.0, 0.42, 0, 0.5)
# UI clicks
n = int(0.03 * SR); tt = np.arange(n) / SR
clk = (0.6 * np.sin(2 * np.pi * 2900 * tt) + 0.4 * hp(rng.uniform(-1, 1, n), 3000)) * np.exp(-tt / 0.006)
for t in clicks:
    put(clk, t, 0.16, 0.1, 0.05)
# chime when the end card arrives
def bell(f, d=2.6):
    n = int(d * SR); t = np.arange(n) / SR
    mod = 1.9 * np.exp(-t / 0.5) * np.sin(2 * np.pi * f * 3.5 * t)
    return np.sin(2 * np.pi * f * t + mod) * np.exp(-t / 0.9)
for i, m in enumerate([74, 78, 81]):
    put(bell(mtof(m)), 22.5 + i * 0.12, 0.12, -0.3 + 0.3 * i, 0.6)
put(bell(mtof(86), 3.0), 27.5, 0.09, 0.2, 0.7)

# ---------------- reverb (Freeverb-style) ----------------
def reverb(x, scale=1.0):
    combs = [1557, 1617, 1491, 1422, 1277, 1356, 1188, 1116]
    y = np.zeros_like(x)
    for d in combs:
        d = int(d * SR / 44100 * scale); g = 0.83
        a = np.zeros(d + 1); a[0] = 1; a[d] = -g
        b = np.zeros(d + 1); b[d] = 1
        y += lfilter(b, a, x)
    y = lp(y, 5000, 1) / len(combs)
    for d in (556, 441, 341, 225):
        d = int(d * SR / 44100); g = 0.5
        a = np.zeros(d + 1); a[0] = 1; a[d] = -g
        b = np.zeros(d + 1); b[0] = -g; b[d] = 1
        y = lfilter(b, a, y)
    return y
wl, wr = reverb(RL, 1.0), reverb(RR, 1.023)
mixL, mixR = L + 0.9 * wl, R + 0.9 * wr

# ---------------- master ----------------
mix = np.stack([mixL, mixR], 1)
mix = hp(mix.T, 30, 2).T
t = np.arange(N) / SR
fade = np.clip(t / 0.25, 0, 1) * np.clip((DUR - t) / 1.6, 0, 1)
mix *= fade[:, None]
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(1.35 * mix) / np.tanh(1.35)       # gentle glue
peak = 10 ** (-1.0 / 20)
mix = mix / np.max(np.abs(mix)) * peak
rms = np.sqrt(np.mean(mix ** 2)); print('rms dBFS', 20 * np.log10(rms))
wavfile.write('/tmp/w/video/music30.wav', SR, (mix * 32767).astype(np.int16))
print('wrote music.wav', mix.shape)
