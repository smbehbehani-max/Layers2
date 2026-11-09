import re, json
def story_index(order):
    out = {}
    for cc in order:
        h = open(f'/tmp/w/layers/site/{cc}.html', encoding='utf-8').read()
        i = h.find('const STORIES='); j = h.find('\n', i)
        seg = h[i:h.find('const AISTORIES', i) if h.find('const AISTORIES', i) > 0 else i + 400000]
        L = []
        for m in re.finditer(r"\{id:'([^']+)',kind:'(?:true|imag)'.*?title:P\('((?:[^'\\]|\\.)*)','((?:[^'\\]|\\.)*)'\)", seg, re.S):
            L.append({'id': m.group(1), 'en': m.group(2).replace("\\'", "'"), 'ar': m.group(3).replace("\\'", "'")})
        for m in re.finditer(r'\{"id":"([^"]+)","kind":"(?:true|imag)".*?"title":\{"en":"((?:[^"\\]|\\.)*)","ar":"((?:[^"\\]|\\.)*)"\}', seg, re.S):
            L.append({'id': m.group(1), 'en': json.loads('"' + m.group(2) + '"'), 'ar': json.loads('"' + m.group(3) + '"')})
        seen = set(); out[cc] = [x for x in L if not (x['id'] in seen or seen.add(x['id']))]
    return out
if __name__ == '__main__':
    S = story_index(['kw', 'sa', 'bh', 'qa', 'ae', 'om'])
    for k, v in S.items(): print(k, len(v), [x['id'] + ':' + x['en'][:30] for x in v[:3]])
