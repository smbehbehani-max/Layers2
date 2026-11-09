"""Check every draft in review/inbox before a human looks at it. Writes review/inbox/CHECKS.md; exit code 1 if any record has an error.
usage: python3 check.py"""
import json, os, re, sys
from common import *
MINC = int(os.environ.get('MIN_CONFIDENCE') or 90)

def check_record(cc, r, sites, seen):
    E, W = [], []
    miss = [k for k in REQ if r.get(k) in (None, '') and k not in ('conf', 'el')]
    if miss: E.append('missing fields: ' + ', '.join(miss))
    if r.get('c') not in ('archaeological', 'geological', 'ecology'): E.append('layer must be archaeological, geological or ecology')
    if r.get('era') not in ('D', 'P', 'H', 'N'): E.append('era must be D, P, H or N')
    if r.get('ic') not in ICONS: W.append(f"icon '{r.get('ic')}' unknown, will be replaced")
    rid = r.get('id', '')
    if not rid.startswith(cc + '-'): E.append(f'id must start with {cc}-')
    if rid in seen: E.append('id already exists')
    try:
        la, lo = float(r['lat']), float(r['lng'])
        b = BB[cc]
        if not (b[0] <= la <= b[1] and b[2] <= lo <= b[3]): E.append(f'location {la}, {lo} is outside {NAMES[cc]}')
        near = sorted((round(km(la, lo, float(s['lat']), float(s['lng'])), 2), s['id']) for s in sites if km(la, lo, float(s['lat']), float(s['lng'])) < 1.0)
        if near: W.append('within 1 km of ' + ', '.join(f'{i} ({d} km)' for d, i in near) + ': same place?')
        q = r.get('coordinate_quote') or ''
        if not q: E.append('no coordinate_quote: the location must be quoted from the source')
        else:
            nums = numbers_in(q)
            if not (any(abs(n - la) < 0.02 for n in nums) and any(abs(n - lo) < 0.02 for n in nums)):
                E.append(f'lat/lng do not match the quoted coordinates "{q}"')
    except (KeyError, ValueError, TypeError):
        E.append('lat/lng are not numbers')
    refs = r.get('refs') or []
    if not refs: E.append('no references')
    elif not any(re.search(r'10\.\d{4,9}/|https?://', json.dumps(x)) for x in refs): E.append('no reference has a DOI or URL')
    gf = r.get('goldfish')
    if not gf: W.append('no independent (goldfish) review')
    elif gf.get('verdict') != 'pass': E.append('independent reviewer found problems: ' + '; '.join(gf.get('problems', [])[:5]))
    elif int(gf.get('confidence') or 0) < MINC: W.append(f"independent reviewer is only {int(gf.get('confidence') or 0)}% sure (needs {MINC}% to publish without you)")
    blob = json.dumps(r, ensure_ascii=False).lower()
    for pat in BANNED:
        if re.search(pat, blob): E.append('uses a banned name (the sea is the Arabian Gulf / الخليج العربي)')
    for k in ('na', 'ta', 'sa'):
        if re.search(r'[<>{}$`\\]', str(r.get(k, ''))): E.append(f'forbidden character in {k}')
    if not re.search(r'[؀-ۿ]', str(r.get('na', ''))): E.append('Arabic name (na) is not Arabic')
    return E, W

def main():
    out = ['# Automatic checks', '', 'Errors must be fixed (or the record removed) before approving. Warnings need a human look.', '']
    bad = 0; n = 0; warn = 0
    seen = {s['id'] for cc in ['kw'] + CCS for s in load(cc)['sites']}
    for f in inbox_files('records'):
        cc = os.path.basename(f)[8:10]
        if cc not in CCS: continue
        sites = load(cc)['sites']
        recs = json.load(open(f, encoding='utf-8'))
        out.append(f'## {os.path.relpath(f, REVIEW)}  ({NAMES[cc]}, {len(recs)} records)'); out.append('')
        for r in recs:
            n += 1
            E, W = check_record(cc, r, sites, seen); seen.add(r.get('id'))
            mark = '❌' if E else ('⚠️' if W else '✅')
            bad += bool(E); warn += bool(W)
            out.append(f"- {mark} **{r.get('n', '?')}** `{r.get('id', '?')}` · {r.get('c', '?')} · {r.get('lat')}, {r.get('lng')} · confidence {int((r.get('goldfish') or {}).get('confidence') or 0)}%")
            for e in E: out.append(f'  - error: {e}')
            for w in W: out.append(f'  - warning: {w}')
        out.append('')
    for f in inbox_files('hypotheses'):
        hs = json.load(open(f, encoding='utf-8'))
        out.append(f'## {os.path.relpath(f, REVIEW)}  ({len(hs)} AI hypothesis drafts)'); out.append('')
        out.append('Drafts only. They are never added to the app automatically: approved ones are written into stories.py by hand or with Claude.'); out.append('')
        for h in hs:
            ok = all(h.get(k) for k in ('title', 'prediction', 'test', 'falsify', 'rivals', 'links'))
            out.append(f"- {'✅' if ok else '❌'} **{h.get('title', '?')}** · links: {', '.join(h.get('links', []))}")
            bad += not ok
        out.append('')
    out.insert(3, f'**{n} records checked, {bad} with errors.**\n')
    p = os.path.join(REVIEW, 'inbox', 'CHECKS.md'); open(p, 'w', encoding='utf-8').write('\n'.join(out))
    json.dump({'records': n, 'errors': bad, 'warnings': warn}, open(os.path.join(REVIEW, 'inbox', 'checks.json'), 'w'))
    print('\n'.join(out))
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
