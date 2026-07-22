"""Replace SleepClaw title wordmark with GT Eesti Display Bold (roman).
Subtitle (Coming soon...) keeps original Georgia paths; only its X is shifted.
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
    r"C:\Users\ROG\Desktop\GitHub\okht-profile\assets\sleepclaw\sleepclaw-coming-soon-v12.svg"
)

TITLE = "SleepClaw"
# Match original visual cap height (Segoe Bold scale × unit ratio)
SCALE = 0.06975760 * (1458.0 / 715.0)
# Slightly farther from owl than v11, and a bit higher overall
TITLE_BASELINE_Y = 148.0  # was 158
TITLE_LEFT_X = 250.0  # was 235 (v11) / 285 (v8)
SUBTITLE_LEFT_X = 257.0  # was 242 (v11) / 292 (v8)
SUBTITLE_BASELINE_Y = 218.0  # was 228


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
    print(f"{TITLE!r} width_px={width_px:.1f} scale={SCALE:.6f}")
    print(f"title x={TITLE_LEFT_X} subtitle x={SUBTITLE_LEFT_X}")

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

    # Shift subtitle x/y (keep paths/scale)
    out2, n = re.subn(
        r'(class="sc-wordmark sc-wordmark-subtitle"[^>]*transform="translate\()'
        r'[\d.]+ [\d.]+'
        r'(\) scale\()',
        rf"\g<1>{SUBTITLE_LEFT_X:.0f} {SUBTITLE_BASELINE_Y:.0f}\2",
        out,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"subtitle shift failed n={n}")
    out = out2

    OUT.write_text(out, encoding="utf-8")
    print("wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
