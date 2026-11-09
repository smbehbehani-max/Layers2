"""Self-test for audit.py. No network and no API key: the two AI reviewers are replaced by scripted answers.
usage: python3 test_audit.py   (works on a temporary copy of the data; exits 1 on any failure)"""
import json, os, shutil, sys, tempfile
SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TMP = tempfile.mkdtemp(prefix='layers-audit-test-')
for d in ('gulf', 'autopilot'): shutil.copytree(os.path.join(SRC, d), os.path.join(TMP, d), ignore=shutil.ignore_patterns('site', 'app.html', '__pycache__', 'review'))
shutil.copy(os.path.join(SRC, 'data2.json'), TMP)
os.environ.update(LAYERS_ROOT=TMP, MIN_CONFIDENCE='90', MAX_AUDIT='100000', AUTO_FIX='true'); os.environ.pop('GITHUB_OUTPUT', None)
sys.path.insert(0, os.path.join(TMP, 'autopilot', 'tools'))
import audit, llm

BH = os.path.join(TMP, 'gulf', 'bh', 'data.json'); KW = os.path.join(TMP, 'data2.json')
read = lambda p: json.load(open(p, encoding='utf-8'))
def edit(p, fn):
    t = open(p, encoding='utf-8').read(); d = json.loads(t); fn(d); open(p, 'w', encoding='utf-8').write(audit.dump_like(t, d))

# --- plant errors the rule checks must find ---
orig = read(BH)['sites']
def plant(d):
    s = d['sites']
    s[0]['lat'], s[0]['lng'] = s[0]['lng'], s[0]['lat']                 # swapped coordinates
    s[1]['t0'], s[1]['t1'] = s[1]['t1'], s[1]['t0']                     # dates in the wrong order
    s[2]['desc'] = s[2]['desc'] + ' It faces the Persian Gulf.'           # banned sea name
    s[3]['lat'] = 51.5                                                    # far outside, cannot be fixed by a rule
edit(BH, plant)
before = open(BH, encoding='utf-8').read()

# --- scripted reviewers ---
GOOD = orig[4]['sa'] + ' (محسّن)'
def fake(system, user, max_tokens=0):
    data = json.loads(user)
    if 'independent second editor' in system:
        return {'reviews': [{'i': x['i'], 'verdict': 'reject' if 'REJECTME' in x['proposed'] else 'apply', 'confidence': 96, 'problem': ''} for x in data]}
    fixes, flags = [], []
    for rec in data:
        for it in rec['items']:
            if rec['key'] == f"bh:site:{orig[4]['id']}" and it['ctx'] == 'sa': fixes.append({'i': it['i'], 'side': 'ar', 'new': GOOD, 'kind': 'translation', 'why': 'test good fix', 'confidence': 94})
            if rec['key'] == f"bh:site:{orig[5]['id']}" and it['ctx'] == 'sa': fixes.append({'i': it['i'], 'side': 'ar', 'new': it['ar'] + ' 1999', 'kind': 'translation', 'why': 'adds a number', 'confidence': 99})
            if rec['key'] == f"bh:site:{orig[6]['id']}" and it['ctx'] == 'sa': fixes.append({'i': it['i'], 'side': 'ar', 'new': it['ar'] + ' REJECTME', 'kind': 'grammar', 'why': 'goldfish rejects', 'confidence': 99})
            if rec['key'] == f"bh:site:{orig[7]['id']}" and it['ctx'] == 'sa': fixes.append({'i': it['i'], 'side': 'ar', 'new': it['ar'] + ' أيضاً', 'kind': 'grammar', 'why': 'low confidence', 'confidence': 70})
            if rec['key'] == f"bh:site:{orig[8]['id']}" and it['ctx'] == 'desc': fixes.append({'i': it['i'], 'side': 'en', 'new': it['en'] if it['en'].endswith(' Checked.') else it['en'] + ' Checked.', 'kind': 'typo', 'why': 'english', 'confidence': 95})
            if rec['key'].startswith('kw:site:') and it['ctx'] == 'na' and not flags: fixes.append({'i': it['i'], 'side': 'ar', 'new': it['ar'] + ' الكويت', 'kind': 'translation', 'why': 'kuwait', 'confidence': 99})
        if rec['key'] == f"bh:site:{orig[9]['id']}": flags.append({'key': rec['key'], 'kind': 'location', 'note': 'This looks 40 km off.', 'confidence': 80})
    return {'fixes': fixes, 'flags': flags}
llm.KEY = 'test'; llm.claude = fake

def run(fn, *a):
    audit.DOCS.clear(); fn(*a)
    return json.load(open(audit.LOG_P, encoding='utf-8'))
ok = True
def check(name, cond):
    global ok; ok = ok and bool(cond); print(('PASS ' if cond else 'FAIL ') + name)

kw_before = open(KW, encoding='utf-8').read()
log = run(audit.weekly)
S = read(BH)['sites']; by = lambda why: [e for e in log if why in e['why']]
check('swapped coordinates are swapped back', (S[0]['lat'], S[0]['lng']) == (orig[0]['lat'], orig[0]['lng']) and by('swapped')[0]['confidence'] == 97)
check('dates are put in order', (S[1]['t0'], S[1]['t1']) == (orig[1]['t0'], orig[1]['t1']))
check('sea name is corrected', 'Arabian Gulf' in S[2]['desc'] and 'Persian' not in S[2]['desc'])
check('a far-away point is flagged, not moved', S[3]['lat'] == 51.5 and by('far outside')[0]['status'] == 'flagged')
check('a confident correction is applied; confidence is the lower of the two', S[4]['sa'] == GOOD and by('test good fix')[0]['status'] == 'applied' and by('test good fix')[0]['confidence'] == 94)
check('a correction that changes a number is only suggested', S[5]['sa'] == orig[5]['sa'] and by('adds a number')[0]['status'] == 'suggested')
check('a correction the goldfish rejects is only suggested', S[6]['sa'] == orig[6]['sa'] and by('goldfish rejects')[0]['status'] == 'suggested')
check('a low-confidence correction is only suggested', S[7]['sa'] == orig[7]['sa'] and by('low confidence')[0]['status'] == 'suggested' and by('low confidence')[0]['confidence'] == 70)
check('an English typo fix is applied', S[8]['desc'].endswith(' Checked.') and by('english')[0]['status'] == 'applied')
check('Kuwait is never changed', open(KW, encoding='utf-8').read() == kw_before and by('kuwait')[0]['status'] == 'suggested')
check('an AI location doubt is a flag', by('40 km off')[0]['status'] == 'flagged' and S[9]['lat'] == orig[9]['lat'])
after = open(BH, encoding='utf-8').read()
check('only the corrected lines changed in the file', sum(a != b for a, b in zip(before.split('\n'), after.split('\n'))) <= 8 and len(before.split('\n')) == len(after.split('\n')))
rep = open(os.path.join(audit.AUD, 'latest.md'), encoding='utf-8').read()
check('the report lists the corrections with confidence', '**94%**' in rep and 'What I did on your behalf' in rep and 'How to correct me' in rep)

good = by('test good fix')[0]['id']; low = by('low confidence')[0]['id']
log = run(audit.command, 'undo', f'Undo {good.lower()} please')
check('undo puts the old text back', read(BH)['sites'][4]['sa'] == orig[4]['sa'] and [e for e in log if e['id'] == good][0]['status'] == 'undone')
log = run(audit.command, 'apply', low)
check('apply applies a suggestion', read(BH)['sites'][7]['sa'].endswith('أيضاً'))
n = len(log); log = run(audit.weekly)
check('an undone correction is never made again', read(BH)['sites'][4]['sa'] == orig[4]['sa'])
check('a second run repeats nothing', not [e for e in log[n:] if e['status'] in ('applied', 'flagged')])
log = run(audit.command, 'undo', 'C-19990101-01 nonsense; rm -rf /')
check('an unknown ID changes nothing', 'no correction with this ID' in open(os.path.join(audit.AUD, 'command_result.md'), encoding='utf-8').read())
shutil.rmtree(TMP, ignore_errors=True)
print('ALL PASSED' if ok else 'FAILED'); sys.exit(0 if ok else 1)
