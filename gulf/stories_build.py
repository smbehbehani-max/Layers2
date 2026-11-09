"""Turn /tmp/w/gulf/<cc>/stories.json (STORIES + SPEC with kit art specs) into template pieces, and give every record a card picture."""
import json, runpy, sys, os
sys.path.insert(0, '/tmp/w')
K = runpy.run_path('/tmp/w/story_kit.py')
scene, DEFS, BUBBLE = K['scene'], K['DEFS'], K['BUBBLE_CLIP']
P = lambda en, ar: {'en': en, 'ar': ar}

# card picture by map icon (fallback by category)
CARD = {
 'shell': dict(bg='day', ground='sea', horizon=130, el=[{'t': 'coral', 'x': 150, 'y': 250, 's': 1.2}, {'t': 'fish', 'x': 300, 'y': 190}, {'t': 'fish', 'x': 360, 'y': 230, 'flip': True}]),
 'boat': dict(bg='sunset', ground='sea', horizon=140, back=[{'t': 'dhow', 'x': 240, 'y': 150, 's': 1.2}]),
 'mound': dict(bg='dusk', ground='sand', horizon=150, el=[{'t': 'tomb', 'x': 140, 'y': 220}, {'t': 'tomb', 'x': 240, 'y': 240, 's': 1.2}, {'t': 'tomb', 'x': 360, 'y': 226, 's': .9}]),
 'platform': dict(bg='day', ground='sand', horizon=150, el=[{'t': 'wall', 'x': 180, 'y': 240, 's': 1.2}, {'t': 'wall', 'x': 330, 'y': 250, 's': .9}]),
 'well': dict(bg='day', ground='sand', horizon=150, el=[{'t': 'well', 'x': 160, 'y': 250, 's': 1.1}, {'t': 'palm', 'x': 330, 'y': 230, 's': 1.1}]),
 'jar': dict(bg='wall', ground='floor', horizon=190, el=[{'t': 'jar', 'x': 180, 'y': 236, 's': 1.4}, {'t': 'jar', 'x': 250, 'y': 236, 's': 1.1}, {'t': 'coins', 'x': 320, 'y': 236, 's': 1.3}]),
 'caravan': dict(bg='sunset', ground='sand', horizon=150, el=[{'t': 'camel', 'x': 150, 'y': 240}, {'t': 'camel', 'x': 260, 'y': 246, 's': .9}, {'t': 'tent', 'x': 400, 'y': 240, 's': .8}]),
 'island': dict(bg='day', ground='sea', horizon=140, el=[{'t': 'dune', 'x': 240, 'y': 180, 's': .9}, {'t': 'palm', 'x': 240, 'y': 150, 's': .8}, {'t': 'dhow', 'x': 400, 'y': 200, 's': .7}]),
 'sword': dict(bg='dusk', ground='sand', horizon=150, el=[{'t': 'fort', 'x': 240, 'y': 230, 's': 1.1}]),
 'flame': dict(bg='night', ground='lava', horizon=150, el=[{'t': 'volcano', 'x': 300, 'y': 200, 's': 1.1}]),
 'wall': dict(bg='day', ground='sand', horizon=150, el=[{'t': 'fort', 'x': 180, 'y': 230}, {'t': 'wall', 'x': 360, 'y': 250, 's': .9}]),
 'cliff': dict(bg='day', ground='sand', horizon=160, el=[{'t': 'cliff', 'x': 240, 'y': 200, 's': 1.1}]),
 'mudvolc': dict(bg='day', ground='rock', horizon=150, el=[{'t': 'crater', 'x': 240, 'y': 210, 's': 1.3}]),
 'quake': dict(bg='dusk', ground='rock', horizon=150, el=[{'t': 'crater', 'x': 240, 'y': 210, 's': 1.2}, {'t': 'fossil', 'x': 80, 'y': 240}]),
 'fault': dict(bg='day', ground='rock', horizon=150, el=[{'t': 'cliff', 'x': 160, 'y': 210, 's': .8}, {'t': 'cliff', 'x': 360, 'y': 240, 's': .8}]),
 'steam': dict(bg='day', ground='rock', horizon=150, el=[{'t': 'spring', 'x': 240, 'y': 230, 's': 1.4}]),
 'sinkhole': dict(bg='day', ground='rock', horizon=150, el=[{'t': 'lavatube', 'x': 240, 'y': 250, 's': 1.1}]),
 'wood': dict(bg='day', ground='green', horizon=150, el=[{'t': 'palm', 'x': 120, 'y': 230}, {'t': 'palm', 'x': 330, 'y': 240, 's': 1.2}, {'t': 'bird', 'x': 400, 'y': 60}]),
 'fossil': dict(bg='day', ground='rock', horizon=160, el=[{'t': 'fossil', 'x': 180, 'y': 230, 's': 1.4}, {'t': 'footprints', 'x': 260, 'y': 246}]),
 'dune': dict(bg='sunset', ground='sand', horizon=150, el=[{'t': 'dune', 'x': 180, 'y': 230, 's': 1.1}, {'t': 'dune', 'x': 380, 'y': 250, 's': .8}]),
 'salt': dict(bg='day', ground='salt', horizon=150, el=[{'t': 'bird', 'x': 300, 'y': 70}]),
 'wave': dict(bg='day', ground='lagoon', horizon=140, el=[{'t': 'coral', 'x': 200, 'y': 250}, {'t': 'turtle', 'x': 320, 'y': 220, 's': 1.2}]),
 'river': dict(bg='day', ground='green', horizon=150, el=[{'t': 'spring', 'x': 240, 'y': 240, 's': 1.6}, {'t': 'palm', 'x': 100, 'y': 230}]),
 'delta': dict(bg='day', ground='lagoon', horizon=140, el=[{'t': 'mangrove', 'x': 140, 'y': 240}, {'t': 'flamingo', 'x': 300, 'y': 250}]),
 'bird': dict(bg='day', ground='lagoon', horizon=140, el=[{'t': 'flamingo', 'x': 200, 'y': 250}, {'t': 'flamingo', 'x': 260, 'y': 256, 'flip': True}, {'t': 'bird', 'x': 380, 'y': 60}]),
 'crab': dict(bg='day', ground='salt', horizon=150, el=[{'t': 'mangrove', 'x': 240, 'y': 240, 's': 1.2}, {'t': 'bird', 'x': 120, 'y': 70}]),
 'mangrove': dict(bg='day', ground='lagoon', horizon=140, el=[{'t': 'mangrove', 'x': 120, 'y': 240}, {'t': 'mangrove', 'x': 240, 'y': 250, 's': 1.2}, {'t': 'mangrove', 'x': 370, 'y': 244}]),
 'oil': dict(bg='sunset', ground='sand', horizon=150, el=[{'t': 'oilwell', 'x': 240, 'y': 250, 's': 1.1}]),
 'gazelle': dict(bg='day', ground='sand', horizon=150, el=[{'t': 'oryx', 'x': 200, 'y': 250, 's': 1.1}, {'t': 'gazelle', 'x': 340, 'y': 254, 's': .9, 'flip': True}]),
 'plant': dict(bg='day', ground='green', horizon=150, el=[{'t': 'grass', 'x': 150, 'y': 240, 's': 1.6}, {'t': 'grass', 'x': 300, 'y': 250, 's': 1.4}]),
 'dolphin': dict(bg='day', ground='sea', horizon=130, el=[{'t': 'whale', 'x': 240, 'y': 220, 's': 1.2}]),
 'map': dict(bg='wall', ground='floor', horizon=190, el=[{'t': 'map', 'x': 240, 'y': 230, 's': 1.3}]),
 'trench': dict(bg='day', ground='sand', horizon=150, el=[{'t': 'wall', 'x': 240, 'y': 240}], people=[{'t': 'adult', 'x': 120, 'y': 262, 'pose': 'kneel'}]),
 'eye': dict(bg='day', ground='rock', horizon=150, el=[{'t': 'rockart', 'x': 240, 'y': 230, 's': 1.2}]),
}
CAT = {'archaeological': 'platform', 'geological': 'cliff', 'ecology': 'plant'}

def build(cc, data):
    d = f'/tmp/w/gulf/{cc}'
    out = {'stories': '[]', 'ai': [], 'art': {}, 'defs': DEFS + BUBBLE, 'card': {}}
    art = out['art']
    # card art for every record
    for s in data['sites']:
        sp = CARD.get(s.get('ic'), CARD[CAT.get(s['c'], 'platform')])
        out['card'][s['id']] = scene(sp)
    p = f'{d}/stories.json'
    if not os.path.exists(p): return out
    J = json.load(open(p, encoding='utf-8'))
    stories = []
    for st in J['stories']:
        pages = []
        for i, pg in enumerate(st['pages']):
            key = f"{st['id']}-{i}"; art[key] = scene(pg['art'])
            q = {k: v for k, v in pg.items() if k != 'art'}; q['art'] = key
            pages.append(q)
        s2 = {k: v for k, v in st.items() if k != 'pages'}; s2['pages'] = pages; s2['cover'] = f"{st['id']}-0"
        stories.append(s2)
    out['stories'] = json.dumps(stories, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    byid = {s['id']: s for s in data['sites']}
    for sp in J['spec']:
        sid = sp['id']; key = sp['key']
        rec = dict(id=sid, n=sp['n'], c='speculative', s=sp['s'], lat=sp['lat'], lng=sp['lng'], p=sp['p'], dr=sp['dr'], el='', desc=sp['desc'], sig=sp['sig'], ex='',
                   conf='Untested AI speculation (connection between published records)', ev=sp['ev'], an=sp['an'], val=sp['val'], disc=sp['dlist'], refs=sp['refs'], ic='spark', era='?',
                   te=sp['te'], ta=sp['ta'], se=sp['se'], sa=sp['sa'], na=sp['na'], t0=sp['ages'][0], t1=sp['ages'][1])
        for l in sp['lk']: assert l[0] in byid, (cc, sid, l[0])
        rec['spec'] = dict(bas=sp['bas'], key=key, sty='ai-' + key, spot=sp['spot'], lk=sp['lk'], pred=sp['pred'], test=sp['test'], wrong=sp['wrong'])
        data['sites'].append(rec); byid[sid] = rec
        for k, v in sp['art'].items(): art[f'x-{key}-{k[1:]}'] = scene(v)
        st = sp['story']
        out['ai'].append(dict(id='ai-' + key, kind='ai', disc=sp['disc'], cover=f'x-{key}-0', color='#7b3fb8', sites=[sid], mapSite=sid,
            title=st['title'], tag=st['tag'], refs=[{'label': r, 'url': ''} for r in st['refs']],
            pages=[{'art': f'x-{key}-0', 'cover': 1},
                   {'art': f'x-{key}-1', 'h': P('The clue', 'الدليل'), 'p': st['p1']},
                   {'art': f'x-{key}-2', 'h': st['h2'], 'p': st['p2']},
                   {'cmap': sid, 'h': P('Connecting the dots', 'صِل النقاط'), 'p': st['p3']},
                   {'art': f'x-{key}-4', 'h': P('The prediction', 'التوقّع'), 'pred': sid}]))
    return out
