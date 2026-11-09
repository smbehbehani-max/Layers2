# Layers — brief for writing illustrated stories + AI connections for one country edition

You are writing the Explorer-mode content for a bilingual (EN/AR) heritage map app. Kuwait already has this; your country must get the same treatment, in the same voice. Everything factual must come from the country's existing records in `data.json` (already researched, with references) — you do not need the web, and you must not invent facts, dates, numbers, named living people or quotes. Use "Arabian Gulf" (الخليج العربي), never "Persian Gulf". Stay politically neutral (no borders, disputes, politics).

## Output
Write a Python file at the path given in your task that defines two lists, `STORIES` and `SPEC`, and ends with:
```python
import json, sys
json.dump({'stories': STORIES, 'spec': SPEC}, open(sys.argv[0].replace('.py', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(STORIES), 'stories', len(SPEC), 'spec')
```
Run it with `python3 -I <path>` and fix any error.

`P = lambda en, ar: {'en': en, 'ar': ar}` for bilingual fields.

## 1. STORIES — 6 illustrated stories
Mix: 2–3 `kind:'true'` (retelling documented research or history, no invented dialogue; a `paper` reference from the record's refs) and 3–4 `kind:'imag'` (an imagined child/family/traveller in the real place and period — this is where dialogue and names like Nura, Salem, Maryam belong). Cover geology, archaeology and ecology at least once each. Each story must be about places that exist in `data.json` (`sites` ids).

```python
dict(id='pearl-town', kind='imag', disc='archaeological', color='#3f7cc0', sites=['al-sinniyah-island'], mapSite='al-sinniyah-island',
 title=P('The Diver’s Weight','ثقل الغواص'), tag=P('A boy, a pearl and a town on an island','فتى ولؤلؤة وبلدة على جزيرة'),
 # optional for kind 'true':  credit=P('Based on the research of …','مستندة إلى أبحاث …'), paper={'label':'Author (year). Title. Journal.','url':'https://…'},
 pages=[
  {'cover':1, 'art': ART_SPEC},
  {'art': ART_SPEC, 'h':P('Reeds and Tar','القصب والقار'), 'p':P(['para 1','para 2'],['فقرة 1','فقرة 2'])},
  {'art': ART_SPEC, 'h':P(...), 'p':P([...],[...]), 'q':P('“a short quote”','«اقتباس قصير»'), 'p2':P('one line after the quote','سطر بعد الاقتباس')},   # q/p2 optional
  ... 4–6 inner pages ...
  {'art': ART_SPEC, 'h':P('The End','النهاية'), 'p':P(['one closing thought'],['خاتمة'])}])
```
- `disc`: one of 'geological','archaeological','ecology' (or a list of two).
- `color`: a hex that suits the story (geology purples/browns, archaeology oranges/blues, ecology greens/teals).
- Pages: 2 short paragraphs each (40–70 words EN per paragraph), vivid, concrete, for a curious 10-year-old and their parent; Arabic must be fluent, natural Arabic of the same meaning (not a word-for-word translation).
- Facts come from `desc`/`sig`/`disc` of the records. Keep numbers exact.

## 2. ART_SPEC — pictures composed from the kit (480×270 watercolour)
Each page's `art` is a dict the kit renders. Vocabulary:
```python
{'bg':'day'|'sunset'|'dusk'|'night'|'wall'(indoor)|'cave', 'ground':'sand'|'salt'|'sea'|'lagoon'|'rock'|'lava'|'green'|'floor'(indoor)|'cave'|'none', 'horizon': 120–200 (y of ground line),
 'sun': [x, y, scale],                      # optional
 'back':  [ {motif}, ... ],                  # drawn before the ground (distant: dhow on horizon, dune, volcano)
 'el':    [ {motif}, ... ],                  # drawn on the ground
 'people':[ {'t':'child'|'adult'|'scientist'|'elder', 'x':..,'y':..,'s':1,'pose':'stand'|'point'|'think'|'kneel'|'lecture'|'cheer','flip':bool,'back':bool,'hat':'gh'(ghutra)|'sh'(shemagh)|'hj'(hijab)|None,'step':0..3} ],
 'front': [ {motif}, ... ],                  # drawn last (foreground)
 'bubble': {another spec}                    # optional thought-bubble scene (top-right) — use for "imagining the past"
}
motif = {'t': NAME, 'x': 0–480, 'y': base line 0–270, 's': scale, 'flip': bool}
NAMES: palm mangrove grass tomb fort tower(rock-cut facade) wall(ruined bricks) jar coins stone(inscribed) well dhow oryx gazelle whale turtle bird flamingo falcon coral fish crater volcano lavatube dune cliff(strata) fossil footprints spring oilwell tent camel oasis house(coral-stone tower house) lab map satellite moon sun rockart
```
People's `y` is their feet (240–266 for foreground). Keep 1–4 motifs per scene; compose like a picture book: a cover with the key place, then scenes that follow the text. For indoor pages use bg 'wall' + ground 'floor' + 'lab' or 'map'.

## 3. SPEC — 3 AI connections (hypotheses), each with its own story
These are *untested ideas* linking records on the map (e.g. a spring and a settlement; a lava field and a cave shelter; a reef and a pearling town; a fault and a hot spring). They must be labelled as hypotheses and be falsifiable. Follow this structure exactly (copy of a Kuwait example is at /tmp/w/layers/spec_example.json — read it first):

```python
dict(id='spec-<slug>', new=True, bas='link', sh='link', key='<short-key>', disc=['geological','archaeological'],
 lat=.., lng=.. (between the linked sites), ages=(t0, t1) years before present,
 n='Title of the connection', na='عنوان الرابط', te='Explorer title?', ta='عنوان استكشافي؟', s='Cross-category hypothesis', p='period', dr='date window',
 desc='3–4 sentences: the two or three records, what they share, the idea.', sig='Why it would matter if true.',
 ev='Evidence actually in the records: dates, distances, materials (name the records).', an='Analogy: a documented case elsewhere in the world where this kind of link is proven (name it, with a reference).',
 val='How to test it in the field or lab.', dlist=['Rival explanation 1: …','Rival explanation 2: …'],
 refs=['references copied from the linked records, plus the analogy reference'],
 se='One-sentence explorer summary ending with “Nobody has tested this yet.”', sa='ملخص بجملة واحدة ينتهي بـ «لم يختبر أحد ذلك بعد».',
 spot=P('Born from … on this map. (how the idea arose: a coincidence of dates/places)','…'),
 lk=[['site-id','one-line why this record matters','سطر بالعربية'], ... 2–4 records],
 pred=P('What we would find if the idea is right.','…'), test=P('The test.','…'), wrong=P('What result would kill the idea.','…'),
 story=dict(title=P(..), tag=P(..), p1=P([2 paras],[2 paras]), h2=P('Seen before: <analogy place>','…'), p2=P([2 paras],[..]), p3=P([1–2 paras: connecting the dots],[..]), refs=['ref label 1','ref label 2']),
 art={'x0': ART_SPEC (cover), 'x1': ART_SPEC (the clue), 'x2': ART_SPEC (the analogy), 'x4': ART_SPEC (the prediction)})
```
Analogy references must be real, well-known published cases (give author, year, title, journal); if unsure of a reference, choose a different, well-known analogy you are sure about.

## Style
Warm, clear, wonder-driven. Short sentences. No hype words. Arabic: فصحى مبسطة, with correct hamza/ta marbuta; dialogue in «». Avoid religious or political content. Do not use real living people as characters in 'imag' stories.
