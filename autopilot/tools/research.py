"""Weekly research run. Finds new papers (OpenAlex, free and open), asks Claude to draft records ONLY where the
abstract itself gives coordinates, drafts a few AI hypotheses from places on the map, and checks a sample of
references. Everything lands in review/inbox/<date>/ for a human to approve. Nothing is published from here.

env: ANTHROPIC_API_KEY (required for drafting), LAYERS_MODEL (default claude-sonnet-5-5),
     MAX_PAPERS (default 20), MAX_HYP (default 3), CONTACT (optional e-mail for OpenAlex's polite pool)"""
import json, os, re, sys, time, datetime, urllib.request, urllib.parse, random
from common import *

TODAY = datetime.date.today().isoformat()
OUT = os.path.join(REVIEW, 'inbox', TODAY); os.makedirs(OUT, exist_ok=True)
STATE_P = os.path.join(REVIEW, 'state.json')
STATE = json.load(open(STATE_P)) if os.path.exists(STATE_P) else {'last_run': '2025-06-01', 'seen_works': [], 'pairs_done': []}
MODEL = os.environ.get('LAYERS_MODEL', 'claude-sonnet-5-5')
KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MAXP = int(os.environ.get('MAX_PAPERS', '20')); MAXH = int(os.environ.get('MAX_HYP', '3'))
UA = 'LAYERS-geoheritage-research/1.0' + (f" (mailto:{os.environ['CONTACT']})" if os.environ.get('CONTACT') else '')
REPORT = [f'# Research run {TODAY}', '']
TOPICS = {'archaeological': 'archaeology OR archaeological OR excavation OR Neolithic OR Palaeolithic OR "Bronze Age"',
          'geological': 'geology OR geological OR outcrop OR formation OR fossil OR ophiolite OR "salt dome"',
          'ecology': 'ecology OR biodiversity OR mangrove OR "protected area" OR reef OR wildlife'}

def get(url, data=None, headers=None, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={'User-Agent': UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=90) as r: return json.loads(r.read().decode())
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(5 * (i + 1))

def claude(system, user, max_tokens=6000):
    body = json.dumps({'model': MODEL, 'max_tokens': max_tokens, 'system': system, 'messages': [{'role': 'user', 'content': user}]}).encode()
    r = get('https://api.anthropic.com/v1/messages', body, {'x-api-key': KEY, 'anthropic-version': '2023-06-01', 'content-type': 'application/json'})
    txt = ''.join(c.get('text', '') for c in r.get('content', []))
    m = re.search(r'\{.*\}', txt, re.S)
    return json.loads(m.group(0)) if m else {}

def abstract(w):
    inv = w.get('abstract_inverted_index') or {}
    pos = sorted((p, word) for word, ps in inv.items() for p in ps)
    return ' '.join(word for _, word in pos)

# ---------- 1. new papers ----------
def find_papers():
    dois = known_dois(); found = []
    for cc in ['kw'] + CCS:
        for layer, q in TOPICS.items():
            params = {'search': f'"{NAMES[cc]}" AND ({q})', 'filter': f"from_publication_date:{STATE['last_run']},has_abstract:true,type:article|review|book-chapter",
                      'per-page': '25', 'select': 'id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,open_access'}
            try: res = get('https://api.openalex.org/works?' + urllib.parse.urlencode(params)).get('results', [])
            except Exception as e: REPORT.append(f'- OpenAlex error for {cc}/{layer}: {e}'); continue
            for w in res:
                doi = (w.get('doi') or '').replace('https://doi.org/', '').lower()
                if w['id'] in STATE['seen_works'] or (doi and doi in dois): continue
                if any(x[2]['id'] == w['id'] for x in found): continue
                found.append((cc, layer, w))
            time.sleep(0.3)
    return found


# ---------- goldfish: an independent reviewer that never saw how the draft was written ----------
GOLDFISH = ("You are an independent fact checker for a scientific heritage map. You did NOT write this record and you know nothing else about it. "
            "You get ONLY the source paper's title and abstract and the draft record. Check every factual claim in the record against the paper text: "
            "the place name, the coordinates (the coordinate_quote must appear in the paper text and match lat/lng), dates, ages, numbers, the layer "
            "(archaeological/geological/ecology), and every sentence of desc, sig, se. Anything not stated in the paper is unsupported, even if it sounds right. "
            "Also flag: the sea named anything other than the Arabian Gulf; political or border claims; Arabic that changes the meaning of the English. "
            "Return JSON only: {\"verdict\": \"pass\" or \"fail\", \"confidence\": 0-100, \"problems\": [short strings]}. Pass only if there are no problems. "
            "confidence = how sure you are that every claim in the record is stated in the paper text; use below 90 whenever you hesitate.")
def goldfish(rec, title, ab):
    try:
        r = claude(GOLDFISH, f"Paper title: {title}\nPaper abstract:\n{ab}\n\nDraft record:\n{json.dumps({k: v for k, v in rec.items() if k != 'goldfish'}, ensure_ascii=False)}", 1500)
        return {'verdict': r.get('verdict', 'fail'), 'confidence': int(r.get('confidence') or 0), 'problems': r.get('problems', [])}
    except Exception as e:
        return {'verdict': 'fail', 'confidence': 0, 'problems': [f'review failed: {e}']}

def draft_records(papers):
    rules = open(os.path.join(AUTO, 'prompts', 'WRITE_RECORDS.md'), encoding='utf-8').read()
    style = open(os.path.join(AUTO, 'prompts', 'ARABIC_STYLE.md'), encoding='utf-8').read()
    ex = open(os.path.join(AUTO, 'prompts', 'example_records.json'), encoding='utf-8').read()
    system = (f"You draft place records for LAYERS, a bilingual map of the geology, archaeology and ecology of the Arab Gulf countries.\n{rules}\n\nArabic style:\n{style}\n\nExamples:\n{ex}\n\n"
              "HARD RULES: Use ONLY the paper text you are given. Write a record only if that text itself states the site's coordinates; copy them verbatim into "
              "'coordinate_quote' and convert to decimal lat/lng. Never estimate, average or look up a coordinate. If the paper is relevant but has no coordinates, return it as a lead. "
              "Never invent facts, dates, numbers or references; the reference is this paper. The sea is the Arabian Gulf (الخليج العربي). Stay politically neutral. "
              "Return JSON only: {\"records\": [...], \"leads\": [{\"name\": ..., \"why\": ...}], \"note\": \"one line\"}.")
    by_cc = {}; leads = []
    for cc, layer, w in papers[:MAXP]:
        STATE['seen_works'].append(w['id'])
        ab = abstract(w)
        doi = w.get('doi') or ''
        src = (w.get('primary_location') or {}).get('source') or {}
        cite = f"{', '.join(a['author']['display_name'] for a in w.get('authorships', [])[:4])}{' et al.' if len(w.get('authorships', [])) > 4 else ''} ({w.get('publication_year')}). {w.get('title')}. {src.get('display_name', '')}. {doi}"
        nearby = [f"{s['id']} | {s['n']} | {s['lat']},{s['lng']}" for s in load(cc)['sites']][:400]
        user = f"Country: {NAMES[cc]} (id prefix '{cc}-'). Layer hint: {layer}.\nReference to use: {cite}\n\nPaper title: {w.get('title')}\nAbstract:\n{ab}\n\nPlaces already on the map (do not duplicate):\n" + '\n'.join(nearby)
        try: r = claude(system, user)
        except Exception as e: REPORT.append(f'- Claude error on {doi or w["id"]}: {e}'); continue
        for rec in r.get('records', []):
            rec['refs'] = [cite];  # the paper is the only source a draft may cite
            rec.setdefault('source_paper', doi or w['id'])
            rec['goldfish'] = goldfish(rec, w.get('title'), ab)
            by_cc.setdefault(cc, []).append(rec)
        for l in r.get('leads', []): leads.append(f"- **{NAMES[cc]}** · {l.get('name')}: {l.get('why')} · [{w.get('title')}]({doi or w['id']})")
    for cc, recs in by_cc.items():
        if cc == 'kw':
            leads += [f"- **Kuwait** (home edition, added by hand) · {x.get('n')} · {x.get('lat')}, {x.get('lng')} · {x.get('source_paper')}" for x in recs]; continue
        json.dump(recs, open(os.path.join(OUT, f'records_{cc}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    REPORT.append(f"## New papers\n\n{len(papers)} new papers found; {min(len(papers), MAXP)} read; "
                  f"{sum(len(v) for k, v in by_cc.items() if k != 'kw')} draft records with published coordinates.\n")
    if leads: REPORT.append('## Leads (relevant, but no coordinates in the abstract: a human must find a published location)\n\n' + '\n'.join(leads) + '\n')

# ---------- 2. AI hypothesis drafts ----------
def linked_ids():
    ids = set()
    for cc in CCS:
        p = os.path.join(ROOT, 'gulf', cc, 'stories.json')
        if os.path.exists(p):
            for sp in json.load(open(p, encoding='utf-8')).get('spec', []): ids.update(json.dumps(sp).split('"'))
    return ids

def draft_hypotheses():
    used = linked_ids(); cands = []
    for cc in CCS:
        S = [s for s in load(cc)['sites'] if s.get('c') in ('archaeological', 'geological', 'ecology')]
        for i, a in enumerate(S):
            for b in S[i + 1:]:
                if a['c'] == b['c'] or a['id'] in used and b['id'] in used: continue
                d = km(float(a['lat']), float(a['lng']), float(b['lat']), float(b['lng']))
                if d > 25: continue
                key = f"{a['id']}|{b['id']}"
                if key in STATE['pairs_done']: continue
                cands.append((d, cc, a, b, key))
    random.seed(TODAY); cands.sort(key=lambda x: x[0]); pick = cands[:40]; random.shuffle(pick)
    system = ("You propose AI hypotheses for LAYERS: testable ideas that connect two published places from different layers (geology, archaeology, ecology). "
              "Use ONLY the two records given. A hypothesis is an idea to test, never a finding. If there is no scientifically sensible link, return {\"skip\": true}. "
              "Otherwise return JSON: {\"title\": EN, \"title_ar\": AR, \"idea\": 2-3 sentences, \"idea_ar\": AR, \"prediction\": ..., \"test\": ..., \"falsify\": what would prove it wrong, "
              "\"rivals\": [three rival explanations], \"links\": [id1, id2], \"why_these\": one line}. The sea is the Arabian Gulf (الخليج العربي). Stay neutral; no politics or borders.")
    out = []
    for d, cc, a, b, key in pick:
        if len(out) >= MAXH: break
        STATE['pairs_done'].append(key)
        strip = lambda s: {k: s.get(k) for k in ('id', 'n', 'c', 's', 'p', 'dr', 'desc', 'sig', 'refs', 'lat', 'lng')}
        try: h = claude(system, f"Country: {NAMES[cc]}. Distance {d:.1f} km.\nRecord A:\n{json.dumps(strip(a), ensure_ascii=False)}\nRecord B:\n{json.dumps(strip(b), ensure_ascii=False)}", 2500)
        except Exception as e: REPORT.append(f'- Claude error on hypothesis {key}: {e}'); continue
        if h.get('skip') or not h.get('title'): continue
        h['country'] = cc; h['links'] = [a['id'], b['id']]; out.append(h)
    if out: json.dump(out, open(os.path.join(OUT, f'hypotheses_{TODAY}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    REPORT.append(f'## AI hypothesis drafts\n\n{len(out)} drafts from {len(pick)} candidate pairs (two layers, under 25 km apart).\n')

# ---------- 3. reference health (self-correction leads) ----------
def check_refs(n=30):
    urls = []
    for cc in ['kw'] + CCS:
        for s in load(cc)['sites']:
            for r in s.get('refs', []):
                for u in re.findall(r'https?://[^\s"\'<>)\]]+', json.dumps(r, ensure_ascii=False)): urls.append((cc, s['id'], u.rstrip('.,;')))
    random.seed(TODAY + 'r'); random.shuffle(urls); bad = []
    for cc, sid, u in urls[:n]:
        try:
            req = urllib.request.Request(u, method='HEAD', headers={'User-Agent': UA})
            urllib.request.urlopen(req, timeout=20)
        except urllib.error.HTTPError as e:
            if e.code in (404, 410): bad.append(f'- {NAMES[cc]} · `{sid}` · {u} → {e.code}')
        except Exception: pass
    REPORT.append(f'## Reference links checked\n\n{n} random links checked; {len(bad)} broken (fix by hand or ask Claude to find the new address).\n' + '\n'.join(bad) + '\n')

PENDING = []
if __name__ == '__main__':
    if not KEY: print('ANTHROPIC_API_KEY is not set: only the reference check runs.')
    else:
        PENDING = find_papers(); draft_records(PENDING)
        draft_hypotheses()
    check_refs()
    STATE['last_run'] = STATE['last_run'] if KEY and len(PENDING) > MAXP else TODAY; STATE['seen_works'] = STATE['seen_works'][-5000:]; STATE['pairs_done'] = STATE['pairs_done'][-5000:]
    json.dump(STATE, open(STATE_P, 'w'), indent=0)
    open(os.path.join(OUT, 'REPORT.md'), 'w', encoding='utf-8').write('\n'.join(REPORT))
    print('\n'.join(REPORT))
