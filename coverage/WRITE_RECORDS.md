# How to write app-ready records for LAYERS

Research each assigned place from authoritative sources (web search + fetch), then write it directly in the app's record format. See three real examples in `/tmp/w/coverage/example_records.json` and copy their style and length exactly.

Fields (all required unless noted):
- `id`: lowercase-hyphen slug, unique, prefixed with the country code (e.g. `om-wadi-bani-awf`).
- `n` English name; `na` Arabic name (established Arabic name if one exists, else a careful transliteration; say in `conf` if you made it).
- `c`: `archaeological` | `geological` | `ecology`.
- `ic` icon, one of: shell, boat, mound, platform, well, jar, caravan, island, sword, flame, wall, cliff, mudvolc, quake, fault, steam, sinkhole, wood, fossil, dune, salt, wave, river, delta, bird, crab, mangrove, oil, gazelle, plant, dolphin, map, trench, eye.
- `era`: `D` deep time (geology) | `P` prehistory | `H` history | `N` nature today (ecology).
- `s`: one-line subtitle (what it is · why notable).
- `lat`, `lng`: decimal degrees from a published/official source. Never estimate; if no source coordinate exists, do not write the record — report it as skipped.
- `p` period label; `dr` date/designation line as published; `el` one key measurable fact.
- `t0`, `t1`: start and end in years before present (present ≈ 2000 for history: 3rd century BC ≈ 2250; ecology designated 2010 → t0 = 16, t1 = 0; geology in years, e.g. 66 Ma = 66000000). If the source gives no date, use a broad estimate and say so in `conf`.
- `te`, `ta`: Explorer title EN/AR (short, vivid, for families).
- `se`, `sa`: Explorer one-sentence summary EN/AR.
- `desc`: 3–5 factual Researcher sentences in English, every number from the source.
- `sig`: one sentence on significance. `ex`: short source label (e.g. "Ramsar RIS 2013"). `disc`: 2–3 short key facts.
- `refs`: list of full citations with DOI or URL. Real and checkable only.
- `conf`: notes on estimates, coordinate precision, translations ('' if none).
- `region`: first-level region name. `must_have`: the Part A number (e.g. "OM-A7") or null.

Rules: never invent anything; the sea is the Arabian Gulf (الخليج العربي); countries are the Arab Gulf countries (دول الخليج العربي); politically neutral; Arabic follows `/tmp/w/arfix/STYLE.md` (natural MSA, no straight quotes in Arabic, glossary terms). Before writing, check `/tmp/w/coverage/existing_<cc>.json` so you do not duplicate a place already on the map (same name or within ~2 km for the same thing).

Output: a JSON list written with `ensure_ascii=False` to the path given in your task. Then reply briefly: how many written, which items skipped and why, and anything uncertain.

## Part B tasks (regional quotas)
For Part B the task file `/tmp/w/coverage/partB_<cc>.json` gives `quota` = {region: {layer: count}} and a `focus` list of themes. Find the most significant, well-documented places that fill each quota (priority: published coordinates > scientific significance > visitor access). Set `must_have` = null and `region` = that region. Never pad with weak sites; if a quota cannot be met honestly, say so. Choose places that are clearly distinct from everything in `existing_<cc>.json` (check names and distance).

## Coordinate rescue tasks
For the rescue lists (`rescue_<cc>.json`), these official places were skipped only because no paper or authority page printed a coordinate. You may now use a public gazetteer coordinate — Wikipedia/Wikidata, GeoNames, OpenStreetMap/Nominatim, Mapcarta, or a point on an official map — **only when it clearly refers to the named place** (or, for a large reserve, to a named landmark/village that an official source places inside it). Put the source and precision in `conf` (e.g. "Coordinates from Wikidata Q123, ≈1 km"; "point at Rawdat X inside the reserve, ≈10 km"). Still never estimate or average a coordinate yourself, and skip anything you cannot pin this way.
