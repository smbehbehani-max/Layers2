# LAYERS by GEOHERITAGE — website

This folder is the whole website. There is no server program and no database, so it runs on any free static host. You don't need to build or install anything to publish it.

## What is in the folder

| File | What it does |
|---|---|
| `index.html` | The app for computers. Phones that open it are sent to `mobile.html` automatically. |
| `mobile.html` | The app for phones. Large screens with a mouse are sent back to `index.html`. |
| `ed-kw.html` … `ed-om.html` | The six country editions. Each loads only when someone opens that country, so the first page opens in under a second. |
| `places.html` | A plain directory of every place in English and Arabic, with coordinates and directions. Search engines and AI tools read this page, because they can't use the map. |
| `sitemap.xml` | Tells search engines which pages to index. |
| `kw.html` `sa.html` `bh.html` `qa.html` `ae.html` `om.html` | Short share pages, one per country, each with its own preview image. They open the app on that country. |
| `og-*.png` | Preview images shown when a link is shared on WhatsApp, X and similar apps. |
| `manifest.webmanifest`, `sw.js`, `icon-*.png`, `apple-touch-icon.png` | Let people add the app to their home screen. After the first visit it also works offline. |
| `privacy.html` | Privacy policy. The app collects nothing. |
| `404.html`, `robots.txt`, `.nojekyll` | Small files for hosting. Keep them. |

## Requirements

- **A static web host with HTTPS.** GitHub Pages, Netlify and Cloudflare Pages are all free. HTTPS is needed for the offline mode, for "Track live" (GPS) and for sharing.
- **Internet access for visitors** on their first visit. The fonts (Newsreader, Instrument Sans, Amiri, IBM Plex Sans Arabic) come from Google Fonts. If the fonts can't load, the app still works with system fonts.
- **Optional: your own domain** (for example `layers.example.com`). All three hosts support one.

The maps, data, stories and drawings are all inside these HTML files, so nothing else needs to be uploaded. The first page is about 2 MB, or about 0.9 MB after compression, which every host above applies automatically. That opens in under a second on 4G.

## Option A — GitHub Pages

You already have `smbehbehani-max.github.io/Layers/`.

1. Open your **Layers** repository on github.com.
2. Click **Add file → Upload files**.
3. Drag in **every file from this folder**. `.nojekyll` is a hidden file, so on a Mac press `Cmd + Shift + .` in Finder to see it. Replace the old files when GitHub asks.
4. Click **Commit changes**.
5. Go to **Settings → Pages**. Check that **Source** is "Deploy from a branch", the branch is `main` and the folder is `/ (root)`. Tick **Enforce HTTPS**.
6. Wait about one minute, then open `https://smbehbehani-max.github.io/Layers/`.

GitHub's web upload accepts files up to 25 MB, so every file in this folder is fine.

## Option B — Netlify (drag and drop)

1. Sign in at app.netlify.com.
2. Go to **Sites → Add new site → Deploy manually**.
3. Drag this whole folder onto the page.
4. You get an address like `something.netlify.app`. Rename it under **Site configuration → Change site name**.

To update the site later, open **Deploys** and drag in the new folder.

## Your own domain

- **GitHub Pages:** go to Settings → Pages → Custom domain. Then add the DNS records GitHub shows you at your domain registrar.
- **Netlify:** go to Domain management → Add a domain.

Share links work on any address: the app builds them from the address it is running on.

If you move to your own domain, also rebuild the website folder with your address so the sitemap and preview links point to it: `python3 make_site.py https://your-domain.com/`.

After the site is live, submit `sitemap.xml` in Google Search Console (search.google.com/search-console) so Google indexes the places.

## Updating the site

When you get a new version, replace `index.html` and `mobile.html` (and any other changed files) and upload again.

Visitors get the new version on their next visit. The offline copy refreshes itself whenever they are online.

## Testing on your own computer

Opening `index.html` by double-clicking works, but offline mode and the phone/computer switch only work over http. To test properly:

1. Open a terminal in this folder.
2. Run `python3 -m http.server 8000`.
3. Visit `http://localhost:8000`.

To force one version, add `?desktop=1` (stay on the computer version) or `?mobile=1` (stay on the phone version) to the end of the address.

## Source code

`layers-source.zip` holds the scripts and data that produce these two pages. You only need it to change content. See `SOURCE.md` inside it.
