"""One small helper to ask Claude for a JSON answer. Used by audit.py (research.py keeps its own copy).
env: ANTHROPIC_API_KEY, LAYERS_MODEL (default claude-sonnet-5-5)"""
import json, os, re, time, urllib.request

KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = os.environ.get('LAYERS_MODEL', 'claude-sonnet-5-5')

def claude(system, user, max_tokens=8000, tries=3):
    body = json.dumps({'model': MODEL, 'max_tokens': max_tokens, 'system': system, 'messages': [{'role': 'user', 'content': user}]}).encode()
    headers = {'x-api-key': KEY, 'anthropic-version': '2023-06-01', 'content-type': 'application/json'}
    for i in range(tries):
        try:
            req = urllib.request.Request('https://api.anthropic.com/v1/messages', data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as r: res = json.loads(r.read().decode())
            break
        except Exception:
            if i == tries - 1: raise
            time.sleep(5 * (i + 1))
    txt = ''.join(c.get('text', '') for c in res.get('content', []))
    m = re.search(r'\{.*\}', txt, re.S)
    return json.loads(m.group(0)) if m else {}
