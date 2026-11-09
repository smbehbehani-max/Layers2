# LAYERS by GEOHERITAGE: source code

These are the scripts, templates and data that produce the website's `index.html` and `mobile.html`. You only need them to change content (places, stories, translations). Publishing the finished site needs only the `website` folder.

## Requirements

- **Python 3.10 or newer.** The build uses only Python's standard library.
- **Node.js 18 or newer with Playwright and Chromium.** These are needed only for the test and screenshot scripts and for `mkpwa2.py` (it renders icons and preview images in a headless browser). Install them with `npm i playwright && npx playwright install chromium`.
- **Linux or macOS.**
- **Location:** the scripts use absolute paths that start with `/tmp/w/`. Unzip so that this folder becomes `/tmp/w`, or search and replace `/tmp/w/` in the `.py` files with your own path.

## Folder map

| Folder | What it holds |
|---|---|
| `gulf/<cc>/` | One folder per country edition: `sa` Saudi Arabia, `om` Oman, `ae` UAE, `qa` Qatar, `bh` Bahrain. Each has:<br>• `data.json` (the places)<br>• `stories.py` (scientific stories and AI hypotheses)<br>• `config.json`<br>• `_tpl.html` (the edition page) |
| `gulf/edition.py`, `gulf/mkpwa2.py` | Build one country edition. |
| `pwa2/` | The Kuwait edition, already built. The hub patches it in place. |
| `layers/` | The hub, that is, the front page and the six-country app:<br>• `hub5.py` (main build)<br>• `hub5_tpl.html` (page template)<br>• `scene.py` (intro scene)<br>• `map2.py` (Gulf map)<br>• `unify.py` (shared look across editions)<br>• `make_site.py` (website folder) |
| `arfix/ar_map.json` | Arabic corrections, applied on every build (current Arabic mapped to improved Arabic). |
| `coverage/` | Must-have lists and the ingestion tool for new places:<br>• `ingest.py`<br>• `WRITE_RECORDS.md`, the record format and rules |
| `story_kit.py`, `kit/`, `logo/`, `ages.py`, `art*.py` | Drawing kit, logos and geological-age tables used by the builds. |

## Build everything

```
cd /tmp/w/gulf
for cc in sa om ae qa bh; do python3 edition.py $cc; python3 mkpwa2.py $cc; done
cd /tmp/w/layers
python3 unify.py
python3 hub5.py          # writes layers/one/index.html and layers/one/mobile.html
python3 make_site.py     # writes layers/website/ (upload this folder)
```

## Add new places

1. Write the new records as JSON. `coverage/WRITE_RECORDS.md` gives the fields and the rules: real sources only, and coordinates must come from a published source.
2. Check them: `python3 /tmp/w/coverage/ingest.py <cc> new.json`.
3. Add them: `python3 /tmp/w/coverage/ingest.py <cc> new.json --apply`. This backs up `data.json` first.
4. Rebuild as described above.

## Notes

- The Gulf is always written as "Arabian Gulf" (الخليج العربي).
- Each place's sources are stored in its `refs` field.
- Every story and hypothesis written by AI is labelled as such in the app.
