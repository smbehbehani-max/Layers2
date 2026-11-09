"""Weekly self-check of what is ALREADY on the map: proofreads the records and stories, corrects what it is
sure about, and reports everything it did with a confidence figure, so the owner can undo any change.

Three layers, in this order:
  1. Rule checks on every record (no AI): sea name, swapped coordinates, location outside the country, dates, Arabic name.
  2. Proofreader (Claude, sees the whole record): Arabic that does not match the English, grammar, spelling, terminology, typos.
  3. Goldfish (a second Claude that sees only the old text and the proposed text): confirms or rejects each correction.
A correction is applied only when the rule guards pass and BOTH reviewers are at or above MIN_CONFIDENCE.
The confidence shown is the lower of the two. Everything else is listed as a suggestion and nothing is changed.

Never changed by AI: coordinates, dates, numbers, references. A location must come from a publication (SPEC rule 2),
so a suspected wrong spot is reported, not moved. Kuwait (the hand-curated home edition) is checked and reported only.

usage: python3 audit.py                 weekly run
       python3 audit.py undo  C-...     put the old text back (and never auto-change that text again)
       python3 audit.py apply C-...     apply a suggestion the owner agrees with
env:   ANTHROPIC_API_KEY, MIN_CONFIDENCE (default 90), MAX_AUDIT (records and stories per week, default 80), AUTO_FIX (default true)"""
import json, os, re, sys, datetime
from common import *
import llm

TODAY = datetime.date.today().isoformat()
AUD = os.path.join(REVIEW, 'audit')
LOG_P = os.path.join(AUD, 'log.json'); STATE_P = os.path.join(AUD, 'state.json')
MINC = int(os.environ.get('MIN_CONFIDENCE') or 90)
MAXA = int(os.environ.get('MAX_AUDIT') or 80)
AUTO_FIX = (os.environ.get('AUTO_FIX') or 'true').lower() != 'false'
READ_ONLY = {'kw'}                       # the Kuwait page is prebuilt by hand: report only
PAIRS = [('n', 'na'), ('te', 'ta'), ('se', 'sa')]
EN_ONLY = ['s', 'p', 'dr', 'el', 'desc', 'sig', 'ex', 'ev']
FORBID = r'[<>{}$`\\]'
FIX_BANNED = [(r'persian\s+gulf', 'Arabian Gulf'), (r'الخليج\s+الفارسي', 'الخليج العربي')]
ID_RE = r'C-\d{8}-\d+'
CAP = 40                                 # rows per table in the report (a GitHub issue holds 65,000 characters)

# ---------- files ----------
DOCS = {}   # relative path -> [original text, parsed object, changed?]
def doc(rel):
    if rel not in DOCS:
        t = open(os.path.join(ROOT, rel), encoding='utf-8').read(); DOCS[rel] = [t, json.loads(t), False]
    return DOCS[rel][1]

def dump_like(orig, obj):
    """Write JSON in the same layout the file already uses, so a correction changes one line, not the whole file."""
    for kw in ({'indent': 1}, {}, {'indent': 0}, {'separators': (',', ':')}, {'indent': 2}):
        t = json.dumps(json.loads(orig), ensure_ascii=False, **kw)
        if t == orig or t + '\n' == orig: return json.dumps(obj, ensure_ascii=False, **kw) + ('\n' if orig.endswith('\n') else '')
    return json.dumps(obj, ensure_ascii=False, indent=1)

def save_docs():
    for rel, (orig, obj, changed) in DOCS.items():
        if changed: open(os.path.join(ROOT, rel), 'w', encoding='utf-8').write(dump_like(orig, obj))

def get_at(rel, path):
    v = doc(rel)
    for k in path: v = v[k]
    return v

def set_at(rel, path, val):
    v = doc(rel)
    for k in path[:-1]: v = v[k]
    v[path[-1]] = val; DOCS[rel][2] = True

def load_json(p, default):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else default

def save_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(obj, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---------- what can be proofread ----------
def site_items(rel, base, s):
    items = []
    for e, a in PAIRS:
        if isinstance(s.get(e), str) and isinstance(s.get(a), str) and s[e] and s[a]:
            items.append({'file': rel, 'ctx': a, 'en': s[e], 'ar': s[a], 'path_en': base + [e], 'path_ar': base + [a]})
    for k in EN_ONLY:
        if isinstance(s.get(k), str) and s[k]: items.append({'file': rel, 'ctx': k, 'en': s[k], 'ar': '', 'path_en': base + [k], 'path_ar': None})
    for j, x in enumerate(s.get('disc') or []):
        if isinstance(x, str) and x: items.append({'file': rel, 'ctx': f'disc[{j}]', 'en': x, 'ar': '', 'path_en': base + ['disc', j], 'path_ar': None})
    return items

def pair_items(rel, base, v, ctx=''):
    """Every {"en": ..., "ar": ...} pair inside a story (strings, or lists of paragraphs of the same length)."""
    items = []
    if isinstance(v, dict):
        e, a = v.get('en'), v.get('ar')
        if isinstance(e, str) and isinstance(a, str) and e and a:
            items.append({'file': rel, 'ctx': ctx, 'en': e, 'ar': a, 'path_en': base + ['en'], 'path_ar': base + ['ar']})
        elif isinstance(e, list) and isinstance(a, list) and len(e) == len(a):
            for j, (x, y) in enumerate(zip(e, a)):
                if isinstance(x, str) and isinstance(y, str) and x and y:
                    items.append({'file': rel, 'ctx': f'{ctx}[{j}]', 'en': x, 'ar': y, 'path_en': base + ['en', j], 'path_ar': base + ['ar', j]})
        for k, x in v.items():
            if k not in ('en', 'ar', 'art'): items += pair_items(rel, base + [k], x, f'{ctx}.{k}' if ctx else str(k))
    elif isinstance(v, list):
        for j, x in enumerate(v): items += pair_items(rel, base + [j], x, f'{ctx}[{j}]')
    return items

def units():
    out = []
    for cc in ['kw'] + CCS:
        rel = os.path.relpath(data_path(cc), ROOT)
        for i, s in enumerate(doc(rel)['sites']):
            out.append({'key': f"{cc}:site:{s.get('id')}", 'cc': cc, 'name': s.get('n', '?'), 'kind': 'place',
                        'head': {'name': s.get('n'), 'layer': s.get('c'), 'place_or_period': s.get('p'), 'lat': s.get('lat'), 'lng': s.get('lng')},
                        'items': site_items(rel, ['sites', i], s)})
    for cc in CCS:
        rel = os.path.join('gulf', cc, 'stories.json')
        if not os.path.exists(os.path.join(ROOT, rel)): continue
        d = doc(rel)
        for i, st in enumerate(d.get('stories', [])):
            name = (st.get('title') or {}).get('en', st.get('id', '?')) if isinstance(st.get('title'), dict) else st.get('id', '?')
            out.append({'key': f"{cc}:story:{st.get('id')}", 'cc': cc, 'name': name, 'kind': 'story', 'head': {'story': name}, 'items': pair_items(rel, ['stories', i], st)})
        for i, sp in enumerate(d.get('spec', [])):
            out.append({'key': f"{cc}:hypothesis:{sp.get('id')}", 'cc': cc, 'name': sp.get('n', '?'), 'kind': 'AI hypothesis', 'head': {'ai_hypothesis': sp.get('n')},
                        'items': site_items(rel, ['spec', i], sp) + pair_items(rel, ['spec', i], sp)})
    for u in out: u['items'] = [it for it in u['items'] if not re.search(FORBID, it['en'] + it['ar'])]   # text with tags or placeholders is left alone
    return out

# ---------- the log ----------
LOG = []; STATE = {}
def new_id():
    day = TODAY.replace('-', ''); n = [int(e['id'].rsplit('-', 1)[1]) for e in LOG if e['id'].startswith(f'C-{day}-')]
    return f'C-{day}-{max(n, default=0) + 1:02d}'

def record(status, u, kind, why, conf, by, file=None, path=None, field='', old=None, new=None):
    e = {'id': new_id(), 'date': TODAY, 'status': status, 'country': u['cc'], 'unit': u['key'], 'name': u['name'], 'what': u.get('kind', 'place'),
         'field': field, 'kind': kind, 'why': why, 'confidence': int(conf), 'by': by, 'file': file, 'path': path, 'old': old, 'new': new}
    LOG.append(e); return e

def lock_key(file, path): return f"{file}|{json.dumps(path)}"

def change(u, kind, why, conf, by, file, path, field, new, can_apply=True, note=''):
    """Apply a correction, or keep it as a suggestion when it may not be applied automatically."""
    old = get_at(file, path)
    if old == new: return None
    if any(e['file'] == file and e['path'] == path and e['new'] == new and e['status'] in ('suggested', 'undone') for e in LOG): return None   # already offered, or undone by the owner
    reason = ''
    if u['cc'] in READ_ONLY: reason = f"{NAMES[u['cc']]} is curated by hand, so I only report"
    elif lock_key(file, path) in STATE.get('locked', []): reason = 'you undid a correction here, so I no longer change this text'
    elif not AUTO_FIX: reason = 'automatic correction is switched off (AUTO_FIX)'
    elif not can_apply: reason = note
    elif conf < MINC: reason = f'confidence is below {MINC}%'
    if reason: return record('suggested', u, kind, f'{why} · Not applied: {reason}.', conf, by, file, path, field, old, new)
    set_at(file, path, new)
    return record('applied', u, kind, why, conf, by, file, path, field, old, new)

# ---------- 1. rule checks (no AI) ----------
def rule_checks(all_units):
    for cc in ['kw'] + CCS:
        rel = os.path.relpath(data_path(cc), ROOT); sites = doc(rel)['sites']; b = BB[cc]
        for i, s in enumerate(sites):
            u = {'key': f"{cc}:site:{s.get('id')}", 'cc': cc, 'name': s.get('n', '?'), 'kind': 'place'}
            miss = [k for k in ('n', 'na', 'c', 'lat', 'lng') if s.get(k) in (None, '')]
            if miss: record('flagged', u, 'missing', 'Missing: ' + ', '.join(miss), 100, 'rule')
            try:
                la, lo = float(s['lat']), float(s['lng'])
                inside = lambda x, y, m=0: b[0] - m <= x <= b[1] + m and b[2] - m <= y <= b[3] + m
                if not inside(la, lo, 1.0):      # one degree of slack: offshore reefs, islands and oil fields are real places
                    if inside(lo, la):
                        e1 = change(u, 'location', 'Latitude and longitude were swapped (the point fell outside the country; swapped, it falls inside).', 97, 'rule', rel, ['sites', i, 'lat'], 'lat', lo)
                        if e1 and e1['status'] == 'applied': set_at(rel, ['sites', i, 'lng'], la); e1['field'] = 'lat/lng'; e1['old'] = [la, lo]; e1['new'] = [lo, la]; e1['path'] = ['sites', i]
                    else: record('flagged', u, 'location', f'The point {la}, {lo} is far outside {NAMES[cc]}. I did not move it: a location must come from a published source.', 95, 'rule')
            except (KeyError, ValueError, TypeError):
                if not miss: record('flagged', u, 'location', 'lat/lng are not numbers', 100, 'rule')
            try:
                if float(s['t0']) < float(s['t1']):
                    e1 = change(u, 'dates', 'The start and end ages were in the wrong order (older must come first).', 99, 'rule', rel, ['sites', i, 't0'], 't0', s['t1'])
                    if e1 and e1['status'] == 'applied': old0 = e1['old']; set_at(rel, ['sites', i, 't1'], old0); e1['field'] = 't0/t1'; e1['old'] = [old0, e1['new']]; e1['new'] = [e1['new'], old0]; e1['path'] = ['sites', i]
            except (KeyError, ValueError, TypeError): pass
            if s.get('na') and not re.search(r'[؀-ۿ]', str(s['na'])): record('flagged', u, 'arabic', 'The Arabic name (na) has no Arabic letters.', 100, 'rule')
    for u in all_units:      # the sea name, everywhere
        for it in u['items']:
            for side in ('en', 'ar'):
                path = it[f'path_{side}']; txt = it[side]
                if not path or not txt: continue
                new = txt
                for pat, good in FIX_BANNED: new = re.sub(pat, good, new, flags=re.I)
                if new != txt:
                    e1 = change(u, 'naming', 'The sea is the Arabian Gulf (الخليج العربي).', 100, 'rule', it['file'], path, it['ctx'], new)
                    if e1 and e1['status'] == 'applied': it[side] = new

# ---------- 2 and 3. proofreader and goldfish ----------
def guards(side, old, new):
    """Rules a correction must pass whatever the AI says. Returns the reason it fails, or ''."""
    if not isinstance(new, str) or not new.strip(): return 'empty text'
    if sorted(re.findall(r'\d+', old)) != sorted(re.findall(r'\d+', new)): return 'it changes a number or date, which needs you'
    if re.search(FORBID, new) or (side == 'ar' and re.search(r'["\']', new) and not re.search(r'["\']', old)): return 'it contains a character the app does not allow'
    if any(re.search(p, new, re.I) for p in BANNED): return 'it uses a banned name'
    if side == 'ar' and not re.search(r'[؀-ۿ]', new): return 'the new Arabic has no Arabic letters'
    if len(old) >= 12 and not (0.5 <= len(new) / len(old) <= 2.0): return 'the length changes too much'
    return ''

def prompts():
    style = open(os.path.join(AUTO, 'prompts', 'ARABIC_STYLE.md'), encoding='utf-8').read()
    proof = ("You proofread LAYERS, a bilingual (English/Arabic) map of the geology, archaeology and ecology of the Arab Gulf countries. "
             "You get records already published. Each has a header and items {i, ctx, en, ar}. 'ar' is empty when the text exists in English only.\n\n"
             "Find REAL errors only: Arabic that says something different from the English, adds or drops a fact, is ungrammatical, misspelled, "
             "a word-for-word calque, or breaks the fixed terminology below; and clear English typos or grammar slips. Do not restyle text that is already correct. "
             "Never change a number, date, unit, coordinate, species name or reference, and never add a fact. Do not use straight quotes, backticks, backslashes or < > { } $ in Arabic.\n\n"
             "Also, for a place record: if you are confident from your own knowledge that the lat/lng is far (over ~20 km) from where that site really is, or a statement in the "
             "record is factually wrong, report it as a flag. Do not propose coordinates as a correction; a flag only.\n\n"
             "confidence = how sure you are (0-100) that the change is correct AND an improvement a careful editor would make. Be honest: use below 90 whenever you hesitate.\n\n"
             'Return JSON only: {"fixes": [{"i": item number, "side": "ar" or "en", "new": full corrected text of that side, "kind": "translation|grammar|spelling|terminology|typo", '
             '"why": one short English sentence, "confidence": 0-100}], "flags": [{"key": record key, "kind": "location|fact", "note": one or two English sentences, "confidence": 0-100}]}. '
             "Return empty lists when everything is fine.\n\nArabic style and fixed terminology:\n" + style)
    gold = ("You are an independent second editor for a bilingual (English/Arabic) heritage map. You did NOT propose these corrections and you do not know why they were proposed. "
            "For each item you get: side ('ar' or 'en'), the English text, the current text of that side, and the proposed text. Decide whether the proposed text should replace the current one. "
            "Say 'apply' only if the proposed text is correct, faithful to the English (no fact added, dropped or changed, numbers and names intact), natural, and clearly better than the current text. "
            "Say 'reject' if the current text was already fine, if the change is only a matter of taste, or if you have any doubt. The sea is the Arabian Gulf (الخليج العربي).\n"
            'Return JSON only: {"reviews": [{"i": item number, "verdict": "apply" or "reject", "confidence": 0-100, "problem": "short, empty if none"}]}.\n\nFixed terminology:\n'
            + style.split('## Fixed terminology')[-1])
    return proof, gold

def batches(us, budget=14000):
    cur, size = [], 0
    for u in us:
        n = sum(len(it['en']) + len(it['ar']) for it in u['items'])
        if cur and (size + n > budget or len(cur) >= 8): yield cur; cur, size = [], 0
        cur.append(u); size += n
    if cur: yield cur

def proofread(us, errors):
    proof, gold = prompts(); checked = 0
    for batch in batches(us):
        items = {}; payload = []
        for u in batch:
            rec = {'key': u['key'], **u['head'], 'country': NAMES[u['cc']], 'items': []}
            for it in u['items']:
                i = len(items) + 1; items[i] = (u, it); rec['items'].append({'i': i, 'ctx': it['ctx'], 'en': it['en'], 'ar': it['ar']})
            payload.append(rec)
        try: r = llm.claude(proof, json.dumps(payload, ensure_ascii=False))
        except Exception as e: errors.append(f'Proofreader failed on {len(batch)} records ({e}); they will be checked next week.'); continue
        checked += len(batch)
        for u in batch: STATE['audited'][u['key']] = TODAY
        by_key = {u['key']: u for u in batch}
        for f in r.get('flags') or []:
            u = by_key.get(f.get('key'))
            if u and f.get('note'):
                kind = f.get('kind') if f.get('kind') in ('location', 'fact') else 'fact'
                tail = ' I did not move the point: a location must come from a published source.' if kind == 'location' else ''
                if not any(e['unit'] == u['key'] and e['kind'] == kind and e['status'] == 'flagged' and e['by'] == 'ai' for e in LOG):
                    record('flagged', u, kind, str(f['note']) + tail, f.get('confidence') or 0, 'ai')
        cand = []
        for f in r.get('fixes') or []:
            try: i = int(f.get('i')); side = f.get('side'); new = f.get('new'); c1 = int(f.get('confidence') or 0)
            except (TypeError, ValueError): continue
            if i not in items or side not in ('ar', 'en'): continue
            u, it = items[i]; path = it[f'path_{side}']; old = it[side]
            if not path or not old or new == old: continue
            cand.append({'i': i, 'u': u, 'it': it, 'side': side, 'path': path, 'old': old, 'new': new, 'c1': c1, 'kind': str(f.get('kind') or 'text'), 'why': str(f.get('why') or ''), 'bad': guards(side, old, new)})
        ok = [c for c in cand if not c['bad']]; rev = {}
        if ok:
            try:
                g = llm.claude(gold, json.dumps([{'i': c['i'], 'side': c['side'], 'en': c['it']['en'], 'current': c['old'], 'proposed': c['new']} for c in ok], ensure_ascii=False), 4000)
                rev = {int(x['i']): x for x in g.get('reviews') or [] if str(x.get('i', '')).isdigit()}
            except Exception as e: errors.append(f'Second reviewer failed ({e}); its corrections are listed as suggestions.')
        for c in cand:
            g = rev.get(c['i']); field = c['it']['ctx'] + (' (English)' if c['side'] == 'en' and c['it']['ar'] else '')
            if c['bad']: change(c['u'], c['kind'], c['why'], min(c['c1'], 89), 'ai', c['it']['file'], c['path'], field, c['new'], False, c['bad'])
            elif not g: change(c['u'], c['kind'], c['why'], min(c['c1'], 89), 'ai', c['it']['file'], c['path'], field, c['new'], False, 'the second reviewer did not answer')
            elif g.get('verdict') != 'apply':
                change(c['u'], c['kind'], c['why'], min(c['c1'], 100 - int(g.get('confidence') or 50), 89), 'ai', c['it']['file'], c['path'], field, c['new'], False,
                       'the second reviewer disagreed' + (f" ({g['problem']})" if g.get('problem') else ''))
            else: change(c['u'], c['kind'], c['why'], min(c['c1'], int(g.get('confidence') or 0)), 'ai', c['it']['file'], c['path'], field, c['new'])
    return checked

# ---------- the report ----------
def cell(v, n=260):
    t = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    t = t.replace('|', '\\|').replace('\n', ' ')
    return t if len(t) <= n else t[:n] + '…'

def diff(old, new):
    """Only the part that changed, with a few words around it."""
    if not (isinstance(old, str) and isinstance(new, str)): return cell(old), cell(new)
    a, b = old.split(' '), new.split(' '); i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]: i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]: j += 1
    cut = lambda w: ('… ' if i > 5 else '') + ' '.join(w[max(0, i - 5):len(w) - j + 5 if j > 5 else len(w)]) + (' …' if j > 5 else '')
    return cell(cut(a)), cell(cut(b))

def report(run, total, checked, errors, have_key):
    ap = [e for e in run if e['status'] == 'applied']; su = [e for e in run if e['status'] == 'suggested']; fl = [e for e in run if e['status'] == 'flagged']
    done = sum(1 for k in STATE['audited'] if STATE['audited'][k])
    where = lambda e: f"{NAMES[e['country']]} · {cell(e['name'], 60)}" + (f" ({e['what']})" if e['what'] != 'place' else '')
    R = [f'# Weekly self-check {TODAY}', '',
         f"I ran the rule checks on every record, and proofread {checked} of {total} records and stories this week ({min(done, total)} of {total} proofread so far; I do a new batch each week)."
         if have_key else 'I ran the rule checks on every record. Proofreading did not run: the `ANTHROPIC_API_KEY` secret is not set.', '',
         f'**{len(ap)} corrections made on your behalf · {len(su)} suggestions waiting for you · {len(fl)} possible problems I could not fix myself.**', '']
    R += ['## What I did on your behalf', '']
    if ap:
        R += ['These are already in the data and go live with the rebuild that follows this report.', '', '| ID | Where | Text | Before | After | Confidence | Why |', '|---|---|---|---|---|---|---|']
        for e in sorted(ap, key=lambda e: e['confidence'])[:CAP]:
            o, n = diff(e['old'], e['new']); R.append(f"| `{e['id']}` | {where(e)} | {e['field']} | {o} | {n} | **{e['confidence']}%** | {cell(e['why'], 200)} |")
    else: R.append('Nothing needed correcting this week.')
    R += ['', '## Suggestions I did not apply', '']
    if su:
        R += [f'Not sure enough (below {MINC}%), a number would change, or the record is curated by hand. Nothing was changed.', '', '| ID | Where | Text | Now | Suggested | Confidence | Why |', '|---|---|---|---|---|---|---|']
        for e in sorted(su, key=lambda e: -e['confidence'])[:CAP]:
            o, n = diff(e['old'], e['new']); R.append(f"| `{e['id']}` | {where(e)} | {e['field']} | {o} | {n} | {e['confidence']}% | {cell(e['why'], 260)} |")
    else: R.append('None.')
    R += ['', '## Possible problems I could not fix myself', '']
    if fl:
        R += ['| ID | Where | Problem | Confidence |', '|---|---|---|---|']
        for e in sorted(fl, key=lambda e: -e['confidence'])[:CAP]: R.append(f"| `{e['id']}` | {where(e)} | {cell(e['why'], 400)} | {e['confidence']}% |")
    else: R.append('None found.')
    if max(len(ap), len(su), len(fl)) > CAP: R += ['', f'Only the first {CAP} rows of each table are shown. The full list is in `autopilot/review/audit/log.json`.']
    if errors: R += ['', '## Problems during this run', ''] + [f'- {x}' for x in errors]
    R += ['', '## How to correct me', '',
          'Comment on this issue (or run **Correct the autopilot** in the Actions tab):',
          '- `undo C-20261115-03` puts the old text back, republishes, and I never auto-change that text again.',
          '- `apply C-20261115-07` applies a suggestion you agree with.',
          '- Several at once: `undo C-20261115-03 C-20261115-04`.', '',
          f'Confidence is the lower of two independent reviews. I apply a correction only at {MINC}% or more (variable `MIN_CONFIDENCE`). '
          'I never change coordinates, dates, numbers or references by myself, and Kuwait is report-only. To pause all automatic corrections, set the variable `AUTO_FIX` to `false`.']
    return '\n'.join(R) + '\n'

def gh_output(**kw):
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            for k, v in kw.items(): f.write(f'{k}={v}\n')

# ---------- commands ----------
def weekly():
    global LOG, STATE
    LOG = load_json(LOG_P, []); STATE = load_json(STATE_P, {}); STATE.setdefault('audited', {}); STATE.setdefault('locked', [])
    start = len(LOG); errors = []; us = units()
    keys = {u['key'] for u in us}; STATE['audited'] = {k: v for k, v in STATE['audited'].items() if k in keys}
    rule_checks(us)
    # a flag stays open until it is fixed: do not repeat last week's flags as new ones
    old_flags = {(e['unit'], e['kind'], e['why']) for e in LOG[:start] if e['status'] == 'flagged'}
    LOG[start:] = [e for e in LOG[start:] if not (e['status'] == 'flagged' and e['by'] == 'rule' and (e['unit'], e['kind'], e['why']) in old_flags)]
    checked = 0
    if llm.KEY:
        todo = sorted([u for u in us if u['items']], key=lambda u: (STATE['audited'].get(u['key'], ''), u['key']))[:MAXA]
        checked = proofread(todo, errors)
    run = LOG[start:]
    save_docs(); save_json(LOG_P, LOG); save_json(STATE_P, STATE)
    text = report(run, len([u for u in us if u['items']]), checked, errors, bool(llm.KEY))
    open(os.path.join(AUD, f'REPORT-{TODAY}.md'), 'w', encoding='utf-8').write(text)
    open(os.path.join(AUD, 'latest.md'), 'w', encoding='utf-8').write(text)
    n = sum(e['status'] == 'applied' for e in run)
    gh_output(applied=n, suggested=sum(e['status'] == 'suggested' for e in run), flagged=sum(e['status'] == 'flagged' for e in run))
    print(text)

def command(cmd, text):
    global LOG, STATE
    LOG = load_json(LOG_P, []); STATE = load_json(STATE_P, {}); STATE.setdefault('audited', {}); STATE.setdefault('locked', [])
    ids = [x.upper() for x in re.findall(ID_RE, text, flags=re.I)]; out = []; n = 0
    if not ids: out.append('I found no correction ID in that. An ID looks like `C-20261115-03`.')
    for cid in dict.fromkeys(ids):
        e = next((x for x in LOG if x['id'] == cid), None)
        if not e: out.append(f'- `{cid}`: I have no correction with this ID.'); continue
        if not e.get('file'): out.append(f'- `{cid}`: this is a note about a possible problem, not a change, so there is nothing to {cmd}.'); continue
        want, give = ('applied', 'old') if cmd == 'undo' else ('suggested', 'new')
        if e['status'] != want: out.append(f"- `{cid}`: nothing to do, its status is already “{e['status']}”."); continue
        expect = e['new'] if cmd == 'undo' else e['old']
        pair = isinstance(e['old'], list) and e['field'] in ('lat/lng', 't0/t1')
        try:
            if pair:
                ks = e['field'].split('/'); cur = [get_at(e['file'], e['path'] + [k]) for k in ks]
                if cur != expect: raise ValueError
                for k, v in zip(ks, e[give]): set_at(e['file'], e['path'] + [k], v)
            else:
                if get_at(e['file'], e['path']) != expect: raise ValueError
                set_at(e['file'], e['path'], e[give])
        except (ValueError, KeyError, IndexError, TypeError):
            out.append(f'- `{cid}`: the text has changed since then, so I left it alone. Tell Claude what it should say.'); continue
        n += 1
        if cmd == 'undo':
            e['status'] = 'undone'; e['undone'] = TODAY
            if not pair and lock_key(e['file'], e['path']) not in STATE['locked']: STATE['locked'].append(lock_key(e['file'], e['path']))
            out.append(f"- `{cid}` undone: **{NAMES[e['country']]} · {e['name']}** ({e['field']}) is back to: {cell(e['old'], 300)}")
        else:
            e['status'] = 'applied'; e['why'] += f' · Applied at your request on {TODAY}.'
            out.append(f"- `{cid}` applied: **{NAMES[e['country']]} · {e['name']}** ({e['field']}) now reads: {cell(e['new'], 300)}")
    save_docs(); save_json(LOG_P, LOG); save_json(STATE_P, STATE)
    text = '\n'.join(out) + ('\n\nThe site is being rebuilt; the change is live in about 10 minutes.' if n else '') + '\n'
    open(os.environ.get('RESULT_FILE') or os.path.join(AUD, 'command_result.md'), 'w', encoding='utf-8').write(text)
    gh_output(changed=n); print(text)

if __name__ == '__main__':
    os.makedirs(AUD, exist_ok=True)
    if len(sys.argv) > 1 and sys.argv[1].lower() in ('undo', 'apply'): command(sys.argv[1].lower(), ' '.join(sys.argv[2:]))
    elif len(sys.argv) > 1: sys.exit('usage: audit.py [undo|apply C-YYYYMMDD-NN ...]')
    else: weekly()
