#!/usr/bin/env python3
"""Check that every internal href/src/srcset in published .html files resolves to a file.
Run from anywhere: python3 _tools/check_links.py   (exit 1 on any broken link)"""
import os, re, sys
from urllib.parse import urlparse, unquote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = 0; n = 0
def resolve(page, url):
    u = urlparse(url)
    if u.scheme or url.startswith(("mailto:", "tel:", "#", "//")): return None
    p = unquote(u.path)
    if not p: return None
    full = os.path.join(ROOT, p.lstrip("/")) if p.startswith("/") else os.path.join(os.path.dirname(page), p)
    full = os.path.normpath(full)
    if os.path.isdir(full): full = os.path.join(full, "index.html")
    elif not os.path.exists(full) and os.path.exists(full + ".html"): full += ".html"  # GitHub Pages extensionless
    return full, u.fragment
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if not d.startswith((".", "_"))]
    for f in fn:
        if not f.endswith(".html"): continue
        page = os.path.join(dp, f); s = open(page, encoding="utf-8").read()
        urls = re.findall(r'(?:href|src)="([^"]+)"', s)
        for ss in re.findall(r'srcset="([^"]+)"', s): urls += [x.strip().split(" ")[0] for x in ss.split(",")]
        for url in urls:
            r = resolve(page, url)
            if not r: continue
            n += 1; full, frag = r
            ok = os.path.exists(full)
            if ok and frag and full.endswith(".html"):
                ok = re.search(r'id="%s"' % re.escape(frag), open(full, encoding="utf-8").read()) is not None
            if not ok:
                bad += 1; print("BROKEN", os.path.relpath(page, ROOT), "->", url)
print(f"checked {n} internal links, {bad} broken"); sys.exit(1 if bad else 0)
