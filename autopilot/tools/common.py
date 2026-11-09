"""Shared paths and helpers for the LAYERS autopilot. LAYERS_ROOT is the build folder (the source zip's w/ folder)."""
import os, json, math, re, glob
ROOT = os.environ.get('LAYERS_ROOT', '/tmp/w')
AUTO = os.path.join(ROOT, 'autopilot')
REVIEW = os.path.join(AUTO, 'review')
CCS = ['sa', 'om', 'ae', 'qa', 'bh']            # Kuwait (kw) is the prebuilt home edition: new Kuwait finds go to the report as leads
NAMES = {'kw': 'Kuwait', 'sa': 'Saudi Arabia', 'om': 'Oman', 'ae': 'United Arab Emirates', 'qa': 'Qatar', 'bh': 'Bahrain'}
BB = {'sa': (16, 32.5, 34, 56), 'om': (16.5, 26.6, 51.9, 60), 'ae': (22.5, 26.3, 51.4, 56.5), 'qa': (24.4, 26.3, 50.6, 51.8), 'bh': (25.5, 27.0, 50.3, 51.0), 'kw': (28.5, 30.2, 46.5, 48.6)}
ICONS = set('shell boat mound platform well jar caravan island sword flame wall cliff mudvolc quake fault steam sinkhole wood fossil dune salt wave river delta bird crab mangrove oil gazelle plant dolphin map trench eye'.split())
REQ = 'id n na c ic era s lat lng p dr el t0 t1 te ta se sa desc sig ex disc refs conf'.split()
BANNED = [r'persian\s+gulf', r'الخليج\s+الفارسي']

def data_path(cc):
    return os.path.join(ROOT, 'data2.json') if cc == 'kw' else os.path.join(ROOT, 'gulf', cc, 'data.json')

def load(cc):
    return json.load(open(data_path(cc), encoding='utf-8'))

def km(a, b, c, d):
    return 2 * 6371 * math.asin(math.sqrt(math.sin(math.radians(c - a) / 2) ** 2 + math.cos(math.radians(a)) * math.cos(math.radians(c)) * math.sin(math.radians(d - b) / 2) ** 2))

def known_dois():
    """Every DOI already cited anywhere in the app, lower-case."""
    out = set()
    for cc in ['kw'] + CCS:
        for s in load(cc)['sites']:
            for r in s.get('refs', []):
                t = r if isinstance(r, str) else json.dumps(r)
                out.update(m.lower().rstrip('.,);') for m in re.findall(r'10\.\d{4,9}/[^\s"\'<>]+', t))
    return out

def numbers_in(text):
    """Decimal degrees found in a coordinate quote, including DMS like 28°40′46.5″."""
    vals = []
    for m in re.finditer(r'(\d{1,3})\s*[°º]\s*(\d{1,2})?\s*[′\'’]?\s*(\d{1,2}(?:\.\d+)?)?\s*[″"”]?', text):
        d, mi, se = m.group(1), m.group(2), m.group(3)
        vals.append(int(d) + (int(mi) / 60 if mi else 0) + (float(se) / 3600 if se else 0))
    vals += [float(x) for x in re.findall(r'(?<![\d.])(\d{1,3}\.\d+)(?![\d.])', text)]
    return vals

def inbox_files(kind='records'):
    return sorted(glob.glob(os.path.join(REVIEW, 'inbox', '*', f'{kind}_*.json')))
