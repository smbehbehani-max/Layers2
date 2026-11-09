"""Package the GitHub repository (source at the root, plus .github/workflows) as layers-github-repo.zip."""
import os, re, zipfile
exec(open('/tmp/w/layers/make_zip.py').read().split('n = 0')[0].replace("OUT = '/tmp/layers-source.zip'", "OUT = '/tmp/layers-github-repo.zip'"))
n = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for d, ds, fs in os.walk(ROOT):
        rel = os.path.relpath(d, ROOT); rel = '' if rel == '.' else rel + '/'
        ds[:] = [x for x in ds if not SKIP_DIRS.match(rel + x + '/') or (rel + x).startswith('video')]
        for f in fs:
            p = rel + f
            if SKIP_DIRS.match(p) or SKIP_FILES.search(p) or ROOT_MEDIA.match(p) or p.startswith('autopilot/github/'): continue
            if p.startswith('video/') and not p.endswith('.py'): continue
            z.write(os.path.join(d, f), p); n += 1
    for f in os.listdir('/tmp/w/autopilot/github/workflows'):
        z.write('/tmp/w/autopilot/github/workflows/' + f, '.github/workflows/' + f)
    z.write('/tmp/w/autopilot/github/gitignore', '.gitignore')
    z.write('/tmp/w/autopilot/SETUP.md', 'README.md')
    W = '/tmp/w/layers/website'
    for d, ds, fs in os.walk(W):
        for f in fs:
            full = os.path.join(d, f); z.write(full, 'docs/' + os.path.relpath(full, W))
print(n, 'files', os.path.getsize(OUT) // 1_000_000, 'MB')
