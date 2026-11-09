# Layers — research brief for adding places to a country edition

You are adding new places to a bilingual (English/Arabic) map app of **geology, archaeology and ecology**. The user is from Kuwait, a beginner, and wants the "same research logic" as before: **every fact comes from a web page you actually opened in this session** (WebSearch to find, WebFetch to read). No facts from memory. Each record carries references to the pages/papers you used. Use "Arabian Gulf" (الخليج العربي), never "Persian Gulf". Keep everything politically neutral: no borders, no disputes, no political labels.

## Output
Write a Python file at the path you are given, in exactly this style (one `add(...)` per place), and run it at the end with `python3 -I <path>` — it must print the number of sites and write the JSON next to it:

```python
import json, sys
S = []
def add(**k): S.append(k)

add(id='bahla-fort', n='Bahla Fort', na='قلعة بهلاء', c='archaeological', s='Mud-brick fortress of the Banu Nabhan · World Heritage', lat=22.9642, lng=57.3011,
    p='Islamic (Nabhani to Ya’ariba)', dr='12th – 18th century AD', el='Oasis wall about 13 km', ic='wall', era='H', t0=900, t1=250,
    te='A castle made of earth', ta='قلعة من تراب', se='A mud-brick fortress and a 13 km wall around an oasis famous for its potters', sa='قلعة من الطوب الطيني وسور بطول 13 كم حول واحة اشتهرت بخزّافيها',
    desc="3–5 sentences of facts from the pages you opened: what it is, numbers (size, dates, counts), who studied it, status (World Heritage year, protected since).",
    sig="One sentence: why it matters.",
    ex='Who excavated / surveys / manages it',
    disc=['Short discovery or key fact 1', 'Short key fact 2'],
    refs=['Author (year). Title. Journal/Publisher.', 'Organisation. Page title (year).'])

json.dump({'sites': S}, open(sys.argv[0].replace('.py', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(S), 'sites')
```

## Field rules
- `id`: kebab-case, unique, must not collide with the existing ids listed in your task.
- `n` English name; `na` Arabic name (correct, natural Arabic — e.g. محمية, قلعة, وادي, جبل).
- `c`: exactly one of `archaeological`, `geological`, `ecology`.
- `s`: one-line English subtitle (what · status).
- `lat`, `lng`: decimal degrees, inside the country bbox given in your task. Take them from a page if it gives them; otherwise use the best approximate location of the named place and keep to 2 decimals.
- `p`: period/formation; `dr`: date range in words; `el`: one striking measured element.
- `ic`: one icon key from: shell boat mound platform well jar caravan island sword flame wall cliff mudvolc quake fault steam sinkhole wood fossil dune salt wave river delta bird crab mangrove oil gazelle plant dolphin map trench eye
- `era`: `D` = deep time (geology, before humans), `P` = prehistory (Stone Age to Bronze/Iron Age), `H` = history (classical to 20th century), `N` = now (living ecology, modern).
- `t0`, `t1`: start and end in **years before present** (integers; 0 = today; e.g. 1256 AD → about 770; 5000 BC → 7025; 50 million years → 50000000). t0 ≥ t1.
- `te` / `ta`: short explorer title EN/AR (an evocative 3–7 word title, like a chapter name). `se` / `sa`: one-sentence explorer summary EN/AR.
- `desc`: 3–5 sentences, English, facts only from opened pages, with numbers. `sig`: one sentence. `ex`: teams/institutions. `disc`: 2 short strings. `refs`: 2–3 citations (papers, UNESCO pages, official bodies, major newspapers). Wikipedia is acceptable as "Wikipedia contributors (2026). Title, citing …" when it cites a source.
- Arabic must be real, fluent Arabic (not transliteration), matching the English meaning.

## Research logic
1. For each candidate place, WebSearch, then WebFetch one or two of the result URLs (en.wikipedia.org links that appear in search results usually work; direct Wikipedia URLs not from a search result are often refused — then use another source such as whc.unesco.org, protectedplanet.net, saudipedia.com, official heritage bodies, museums, newspapers like The National, Gulf News, Arab News, Oman Observer, Gulf Times).
2. Record only what the page said. If a fact is not on a page, leave it out. If coordinates are not on a page, approximate and keep 2 decimals.
3. Prefer a balanced mix across the three categories, and spread places across the country, including lesser-known but well-documented ones: specific archaeological sites and excavations, geological formations/outcrops/caves/craters/fossil beds/springs/wadis/dunes/sabkhas/oil discovery wells, and protected areas/wetlands/islands/reefs/mangroves/species hotspots.
4. Do not duplicate places already in the edition (ids given in the task); you may add a *different* site in the same area.
5. Work steadily: about 2–3 tool calls per place. Aim for the number of places asked in your task. Quality over count: a place with thin sources is better dropped.

When finished, reply with: the file path, the count, and a one-line note on any place you were unsure about.
