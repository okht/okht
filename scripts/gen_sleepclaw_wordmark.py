"""Replace SleepClaw title wordmark with GT Eesti Display Bold (roman).
Subtitle (Coming soon...) is left unchanged.
Size/position matched to sleepclaw-coming-soon-v8 title transform.
"""
from __future__ import annotations

import re
from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_PATH = Path(
    r"C:\Users\ROG\Desktop\GitHub\cht-me\public\fonts\GT-Eesti\GT-Eesti-Display-Bold-Trial.woff2"
)
SRC = Path(
    r"C:\Users\ROG\Desktop\GitHub\okht-profile\assets\sleepclaw\sleepclaw-coming-soon-v8.svg"
)
OUT = Path(
    r"C:\Users\ROG\Desktop\GitHub\okht-profile\assets\sleepclaw\sleepclaw-coming-soon-v10.svg"
)

TITLE = "SleepClaw"
# Original v8 title: translate(285 158) scale(0.06975760 -0.06975760)
SCALE = 0.06975760
TITLE_BASELINE_Y = 158.0
TITLE_LEFT_X = 285.0


def text_to_paths(font: TTFont, text: str) -> tuple[list[str], float]:
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"].metrics
    paths: list[str] = []
    pen_x = 0.0
    for ch in text:
        gname = cmap.get(ord(ch))
        if gname is None:
            print(f"MISSING {ch!r}")
            pen_x += font["head"].unitsPerEm * 0.3
            continue
        aw, _ = hmtx[gname]
        sp = SVGPathPen(glyph_set)
        tp = TransformPen(sp, Transform(1, 0, 0, 1, pen_x, 0))
        glyph_set[gname].draw(tp)
        d = sp.getCommands()
        if d:
            paths.append(d)
        pen_x += aw
    return paths, pen_x


def main() -> None:
    font = TTFont(str(FONT_PATH))
    print("font:", font["name"].getDebugName(4))
    paths, total_w = text_to_paths(font, TITLE)
    width_px = total_w * SCALE
    print(f"{TITLE!r} width_units={total_w:.1f} width_px={width_px:.1f} paths={len(paths)}")
    print(f"transform=translate({TITLE_LEFT_X} {TITLE_BASELINE_Y}) scale({SCALE} -{SCALE})")

    lines = [
        f'  <g class="sc-wordmark sc-wordmark-title" fill="#17171A" aria-hidden="true" '
        f'transform="translate({TITLE_LEFT_X:.2f} {TITLE_BASELINE_Y:.2f}) '
        f'scale({SCALE:.8f} {-SCALE:.8f})" '
        f'data-source-style="gt-eesti-display:font-weight:Bold;font-style:normal">'
    ]
    for d in paths:
        lines.append(f'    <path d="{d}" />')
    lines.append("  </g>")
    new_title = "\n".join(lines) + "\n"

    src = SRC.read_text(encoding="utf-8")
    pattern = re.compile(
        r'  <g class="sc-wordmark sc-wordmark-title"[^>]*>.*?</g>\n',
        re.S,
    )
    if not pattern.search(src):
        raise SystemExit("title wordmark group not found")
    out = pattern.sub(new_title, src, count=1)
    OUT.write_text(out, encoding="utf-8")
    print("wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
