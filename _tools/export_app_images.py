#!/usr/bin/env python3
"""Export web-sized app icon + screen crops for velkmoor.com.

Usage:
  python3 _tools/export_app_images.py <slug> <icon_1024.png> <lang>:<name>:<store_screenshot.png> [...]

Writes into assets/img/<slug>/:
  icon-512.png/.webp, icon-180.png (touch), icon-128.webp
  <name>-<lang>.webp/.jpg  — the phone screen cropped out of a 1320x2868
  App Store screenshot (caption removed), 720px wide.
Never deletes anything; overwrites only its own outputs.
"""
import sys, os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# phone screen inside our 1320x2868 store screenshots (same generator for all apps)
CROP = (136, 724, 1184, 2868)

def main():
    slug, icon, *shots = sys.argv[1:]
    out = os.path.join(ROOT, "assets", "img", slug)
    os.makedirs(out, exist_ok=True)
    im = Image.open(icon).convert("RGB")
    for s in (512, 180, 128):
        r = im.resize((s, s), Image.LANCZOS)
        if s == 512:
            r.save(os.path.join(out, "icon-512.png"), optimize=True)
            r.save(os.path.join(out, "icon-512.webp"), quality=88)
        elif s == 180:
            r.save(os.path.join(out, "icon-180.png"), optimize=True)
        else:
            r.save(os.path.join(out, "icon-128.webp"), quality=88)
            r.save(os.path.join(out, "icon-128.png"), optimize=True)
    for spec in shots:
        lang, name, path = spec.split(":", 2)
        s = Image.open(path).convert("RGB")
        if s.size != (1320, 2868):
            raise SystemExit(f"unexpected size {s.size} for {path}")
        c = s.crop(CROP)
        w = 720
        c = c.resize((w, round(c.height * w / c.width)), Image.LANCZOS)
        base = os.path.join(out, f"{name}-{lang}")
        c.save(base + ".webp", quality=82, method=6)
        c.save(base + ".jpg", quality=82, optimize=True, progressive=True)
        print(base, c.size)

if __name__ == "__main__":
    main()
