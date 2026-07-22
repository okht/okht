"""Build cht.me pill button: cht-logo mark + GT Eesti Display Regular Italic wordmark."""
from __future__ import annotations

from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_PATH = Path(
    r"C:\Users\ROG\Desktop\GitHub\cht-me\public\fonts\GT-Eesti\GT-Eesti-Display-Regular-Italic-Trial.woff2"
)
OUT = Path(
    r"C:\Users\ROG\Desktop\GitHub\okht-profile\assets\profile\cht-me-tdot-v13.svg"
)

WORD = "cht.me"
# Fit next to 13×21 logo inside 136×52 pill
SCALE = 0.026
BASELINE_Y = 34.905
TEXT_X = 40.0
BUTTON_W = 136
BUTTON_H = 52


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
            pen_x += font["head"].unitsPerEm * 0.25
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
    paths, total_w = text_to_paths(font, WORD)
    print(f"{WORD!r} width_px={total_w * SCALE:.1f}")

    logo = """  <!-- cht-logo.svg mark -->
  <svg x="17" y="15.5" width="13" height="21" viewBox="350 230 320 590" aria-hidden="true">
    <g fill="#000000">
      <path d="M601.257 727.417C594.199 727.417 587.892 731.829 585.473 738.46L569.38 782.566C565.381 793.527 573.497 805.128 585.165 805.128H627.104C634.162 805.128 640.469 800.716 642.888 794.085L658.981 749.979C662.98 739.018 654.864 727.417 643.196 727.417H601.257Z" transform="translate(-15 0)"/>
      <g transform="matrix(1 0 -0.167078 1 85.544 0)">
        <path d="M532.778 237H488.79Q478.79 237 476.872 246.814L390.259 690.172C388.506 701.568 386.765 712.963 386.765 723.457C386.765 776.938 421.827 805 476.222 805H497.975Q505.975 805 507.479 797.142L515.879 753.254Q517.383 745.395 509.383 745.395H493.753C465.605 745.395 452.543 732.247 452.543 710.297C452.543 703.247 453.42 697.173 455.136 689.284L540.876 246.81Q542.778 237 532.778 237Z"/>
      </g>
      <path d="M383.436 388.906C376.377 388.906 370.071 393.318 367.652 399.949L351.559 444.055C347.56 455.016 355.676 466.617 367.343 466.617H563.87C570.929 466.617 577.235 462.205 579.654 455.573L595.747 411.468C599.746 400.506 591.631 388.906 579.963 388.906H383.436Z" transform="translate(14.075 0)"/>
    </g>
  </svg>
"""

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{BUTTON_W}" height="{BUTTON_H}" '
        f'viewBox="0 0 {BUTTON_W} {BUTTON_H}" role="img" aria-labelledby="title">\n',
        '  <title id="title">cht.me</title>\n',
        f'  <rect x="1" y="1" width="{BUTTON_W - 2}" height="{BUTTON_H - 2}" rx="25" '
        f'fill="#ffffff" stroke="#000000" stroke-width="2"/>\n',
        logo,
        f'  <g fill="#000000" transform="translate({TEXT_X:.2f} {BASELINE_Y:.3f}) '
        f'scale({SCALE:.6f} {-SCALE:.6f})" '
        f'data-source-style="gt-eesti-display:font-style:Italic">\n',
    ]
    for d in paths:
        parts.append(f'    <path d="{d}" />\n')
    parts.append("  </g>\n</svg>\n")

    OUT.write_text("".join(parts), encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
