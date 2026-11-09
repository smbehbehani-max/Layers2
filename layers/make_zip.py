"""Package the build sources into layers-source.zip (paths start with w/). Keeps everything the build reads, skips media and caches."""
import os, re, zipfile, sys
ROOT = '/tmp/w'; OUT = '/tmp/layers-source.zip'
SKIP_DIRS = re.compile(r'^(video/(?!.*\.py$)|kit/raw/|kit/screenshots/|review/|promo/|shots/|.*/shots/|.*__pycache__/|layers/one/|layers/website/|pwa/)')
SKIP_FILES = re.compile(r'(\.log|\.mp4|\.webm|\.wav|\.zip)$|\.bak|before|_v1\.|(^|/)t\d+\.py$|^(prev|out3)')
ROOT_MEDIA = re.compile(r'^[^/]+\.(png|jpg)$|^layers/[^/]+\.(png|jpg)$|^gulf/[^/]+/[^/]+\.png$')
n = 0
with zipfile.ZipFile(OUT + '.tmp', 'w', zipfile.ZIP_DEFLATED) as z:
    for d, ds, fs in os.walk(ROOT):
        rel = os.path.relpath(d, ROOT); rel = '' if rel == '.' else rel + '/'
        ds[:] = [x for x in ds if not SKIP_DIRS.match(rel + x + '/') or (rel + x).startswith('video')]
        for f in fs:
            p = rel + f
            if SKIP_DIRS.match(p) or SKIP_FILES.search(p) or ROOT_MEDIA.match(p): continue
            if p.startswith('video/') and not p.endswith('.py'): continue
            z.write(os.path.join(d, f), 'w/' + p); n += 1
    z.write('/tmp/w/SOURCE.md', 'SOURCE.md')
os.replace(OUT + '.tmp', OUT)
print(n, 'files', os.path.getsize(OUT) // 1_000_000, 'MB')
