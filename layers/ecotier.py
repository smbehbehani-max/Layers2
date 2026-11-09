"""Ecology rarity tiers on worldwide criteria:
Exceptional — UNESCO World Heritage or Biosphere Reserve, or a habitat of a species/community found nowhere else (strict endemic).
Rare — Ramsar Wetland of International Importance, or habitat of an IUCN Red List Endangered / Critically Endangered species, or a globally significant aggregation.
Uncommon — a nationally protected area, or habitat of an IUCN Vulnerable species, mangroves or nesting beaches.
Common — other recorded ecology places."""
import re
T_RARE = [r'ramsar', r'tentative list', r'former', r'critically endangered', r'\bendangered\b', r'whale shark', r'arabian leopard', r'humpback', r'hawksbill', r'green turtle', r'loggerhead', r'globally (?:important|significant)', r'important bird', r'largest (?:colony|aggregation|population)', r'dugong', r'oryx', r'socotra cormorant', r'nowhere else', r'found only', r'only natural']
T_UNC = [r'reserve', r'protected', r'sanctuary', r'national park', r'mangrove', r'nesting', r'vulnerable', r'wetland', r'coral', r'migrat']
def exceptional(t):
    if re.search(r'unesco biosphere|biosphere reserve', t) and 'tentative' not in t: return True                                  # UNESCO Man and the Biosphere
    for m in ([] if re.search(r'delist|removed the site|deletion|removed from the (?:world heritage )?list', t) else re.finditer(r'world heritage', t)):                                                                                    # inscribed World Heritage
        w = t[max(0, m.start() - 50):m.end() + 50]
        if not re.search(r'former|delist|tentative|lost', w): return True
    if re.search(r'nowhere else on earth|largest known [^.]{0,60}in the world|densest [^.]{0,40}in the world', t): return True  # globally unique
    return False
ORDER = ['common', 'uncommon', 'rare', 'exceptional']
OVERRIDE = {'tree-of-life': 'rare'}   # a lone c. 440-year-old tree in open desert, a documented natural landmark
def tier(x):
    if x.get('id') in OVERRIDE: return OVERRIDE[x['id']]
    t = ' '.join(str(x.get(k, '')) for k in ('n', 's', 'desc', 'sig', 'ex', 'conf')).lower()
    if exceptional(t): return 'exceptional'
    if any(re.search(p, t) for p in T_RARE): return 'rare'
    if any(re.search(p, t) for p in T_UNC): return 'uncommon'
    return 'common'
if __name__ == '__main__':
    import json, collections
    for cc in ['kw', 'sa', 'bh', 'qa', 'ae', 'om']:
        S = json.load(open('/tmp/w/data2.json' if cc == 'kw' else f'/tmp/w/gulf/{cc}/data.json'))['sites']
        E = [x for x in S if x['c'] == 'ecology']
        c = collections.Counter(tier(x) for x in E); print(cc, dict(c))
        for x in E:
            if tier(x) in ('exceptional',): print('   EXC', x['n'])
