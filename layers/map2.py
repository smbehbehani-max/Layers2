"""Basemap for the Layers hub: Natural Earth 10m, GCC + neighbouring land, equirectangular (cos 23°)."""
import json, math
G = json.load(open('/tmp/nev/geojson/ne_10m_admin_0_countries.geojson'))
LNG0, LNG1, LAT0, LAT1 = 25.0, 73.0, 2.0, 44.0
K = math.cos(math.radians(23)); S = 1000 / ((LNG1 - LNG0) * K)
W = 1000; H = round((LAT1 - LAT0) * S)
GCC = {'KWT': 'kw', 'SAU': 'sa', 'BHR': 'bh', 'QAT': 'qa', 'ARE': 'ae', 'OMN': 'om'}
# small islands not drawn (kept out of the map to stay neutral)
SKIP = [(55.03, 25.87), (55.30, 26.26), (55.15, 26.24)]
def P(lng, lat): return ((lng - LNG0) * K * S, (LAT1 - lat) * S)
def dp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    im, dm = 0, -1
    for i in range(1, len(pts) - 1):
        x, y = pts[i]; d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / L
        if d > dm: im, dm = i, d
    if dm > eps: return dp(pts[:im + 1], eps)[:-1] + dp(pts[im:], eps)
    return [pts[0], pts[-1]]
def ring_path(ring, eps):
    pts = [P(x, y) for x, y in ring]
    m = len(pts) // 2
    s = dp(pts[:m + 1], eps)[:-1] + dp(pts[m:], eps)
    if len(s) < 4: return ''
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in s) + 'Z'
def build():
    gcc = {}; other = []
    for f in G['features']:
        a3 = f['properties'].get('ADM0_A3')
        g = f['geometry']; polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        xs = [c[0] for p in polys for c in p[0]]; ys = [c[1] for p in polys for c in p[0]]
        if max(xs) < LNG0 - 2 or min(xs) > LNG1 + 2 or max(ys) < LAT0 - 2 or min(ys) > LAT1 + 2: continue
        d = ''
        for p in polys:
            r = p[0]; cx = sum(c[0] for c in r) / len(r); cy = sum(c[1] for c in r) / len(r)
            if a3 == 'IRN' and any(abs(cx - sx) < .12 and abs(cy - sy) < .12 for sx, sy in SKIP): continue
            d += ring_path(r, 0.35 if a3 not in GCC else (0.12 if a3 in ('KWT', 'BHR', 'QAT') else 0.3))
        if not d: continue
        if a3 in GCC: gcc[GCC[a3]] = d
        else: other.append(d)
    return dict(W=W, H=H, gcc=gcc, other=[''.join(other)])   # neighbours as one borderless land mass
if __name__ == '__main__':
    m = build(); json.dump(m, open('/tmp/w/layers/map2.json', 'w')); print(W, H, list(m['gcc']), len(m['other']))
