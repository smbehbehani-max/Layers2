"""Add approved drafts to the app data. Runs only after a human merged the review pull request.
Every record must pass check.py again; failing records are left in the inbox and reported. Approved files move to review/done/."""
import json, os, shutil, sys, datetime
from common import *
from check import check_record

def main():
    added = 0; kept = []
    seen = {s['id'] for cc in ['kw'] + CCS for s in load(cc)['sites']}
    for f in inbox_files('records'):
        cc = os.path.basename(f)[8:10]
        if cc not in CCS: continue
        P = data_path(cc); D = load(cc); recs = json.load(open(f, encoding='utf-8')); left = []
        for r in recs:
            E, _ = check_record(cc, r, D['sites'], seen)
            if E: left.append(r); print('NOT ADDED', r.get('id'), E); continue
            if r['ic'] not in ICONS: r['ic'] = {'archaeological': 'wall', 'geological': 'cliff', 'ecology': 'plant'}[r['c']]
            r['t0'], r['t1'] = sorted((float(r['t0']), float(r['t1'])), reverse=True)
            r['added'] = datetime.date.today().isoformat(); r['review'] = os.path.relpath(f, REVIEW)
            D['sites'].append(r); seen.add(r['id']); added += 1
        shutil.copy(P, P + '.bak-autopilot')
        json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        dest = f.replace(os.sep + 'inbox' + os.sep, os.sep + 'done' + os.sep); os.makedirs(os.path.dirname(dest), exist_ok=True)
        if left:
            json.dump(left, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); kept.append(f)
            json.dump([r for r in recs if r not in left], open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        else:
            shutil.move(f, dest)
    for f in inbox_files('hypotheses') + [x for x in __import__('glob').glob(os.path.join(REVIEW, 'inbox', '*', '*.md'))]:
        dest = f.replace(os.sep + 'inbox' + os.sep, os.sep + 'done' + os.sep); os.makedirs(os.path.dirname(dest), exist_ok=True); shutil.move(f, dest)
    print('added', added, 'records;', len(kept), 'files still have records to fix')
    open(os.path.join(REVIEW, 'last_apply.txt'), 'w').write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()} added {added}\n')

if __name__ == '__main__':
    main()
