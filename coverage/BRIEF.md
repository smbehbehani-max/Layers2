# Must-have list brief — LAYERS by GEOHERITAGE

LAYERS is a bilingual map app of the geology, archaeology and ecology of the six Arab Gulf countries. The owner wants each country's count to be defensible: "all officially listed sites plus X more". Your job is to compile, for ONE country, the complete **must-have list** of officially designated sites, from authoritative sources, and mark which ones the app already has.

## What counts as must-have (all four groups)
1. **UNESCO World Heritage sites** — every inscribed property; list each separate component (e.g. each oasis/site of a serial property) as its own row when the property has named components with their own location.
2. **UNESCO Tentative List** entries — every current entry; again one row per named component when components are given with locations.
3. **Protected areas** — every officially designated national park, nature reserve, royal reserve, marine protected area, plus Ramsar sites and UNESCO Biosphere Reserves. Use the national authority (e.g. Saudi National Center for Wildlife, Oman Environment Authority, UAE federal/emirate environment agencies, Qatar Ministry of Environment and Climate Change, Bahrain Supreme Council for Environment, Kuwait Environment Public Authority), Ramsar's site list, UNESCO MAB, and Protected Planet (WDPA) as sources.
4. **Recognised geosites** — UNESCO Global Geoparks and aspiring geoparks, IUGS geological heritage sites / Geoheritage Stones, and geosites published by national geological surveys or official geopark/geotourism programmes.

## Rules
- Use web search and fetch official pages. **Never invent** a site, a designation, a year or a coordinate. If you cannot find coordinates in a source, put `lat`/`lng` = null (do not estimate). If a designation is uncertain, leave it out or mark `"confidence": "low"` with the reason.
- Political neutrality. The sea is the "Arabian Gulf".
- Check the date: it is November 2026; include inscriptions and Tentative List additions up to now if your sources show them.
- For each row decide whether the app already has it: compare with `/tmp/w/coverage/existing_<cc>.json` (fields id, n = English name, na = Arabic name, c = layer, lat, lng). Match by name (allow spelling variants) or by location within a few km for the same thing. If matched, put the app `id` in `in_app`; otherwise `in_app` = null.

## Output
Write `/tmp/w/coverage/musthave_<cc>.json` — a JSON list (UTF-8, `ensure_ascii=False`) of objects:
```
{"name": "...", "name_ar": "... or null", "group": "WHS | Tentative | Protected area | Ramsar | Biosphere | Geopark | Geosite",
 "layer": "archaeological | geological | ecology", "region": "first-level region / governorate / emirate / municipality",
 "designation": "e.g. UNESCO World Heritage 2008 (component of ...)", "lat": number|null, "lng": number|null,
 "coord_source": "where the coordinate came from or null", "source_url": "official URL", "in_app": "app id or null", "confidence": "high|medium|low", "note": "optional"}
```
One site can belong to several groups (e.g. a reserve that is also a Ramsar site): give one row with the strongest group and mention the others in `designation`.

Then reply with: total rows per group, how many are already in the app, how many are missing, and anything you were unsure about. Keep the reply short.
