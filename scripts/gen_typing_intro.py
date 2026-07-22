"""Generate typing-intro SVG from GT Eesti font glyphs."""
from __future__ import annotations

from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_PATH = Path(
    r"C:\Users\ROG\Desktop\GitHub\cht-me\public\fonts\GT-Eesti-Display-Regular-Italic-Trial.woff2"
)
OUT_PATH = Path(
    r"C:\Users\ROG\Desktop\GitHub\okht-profile\assets\profile\typing-intro-gt-eesti-regular-italic-v3.svg"
)

LINES = [
    "Build from real problems.",
    # Extra spaces between words so Agent / Code / Data read more separated
    "Agent   Code   Data",
    "Make ideas tangible, testable, and reusable.",
]

WIDTH_CANVAS = 820
HEIGHT = 44
TARGET_EM_PX = 28.0


def main() -> None:
    font = TTFont(str(FONT_PATH))
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    units_per_em = font["head"].unitsPerEm
    hmtx = font["hmtx"].metrics
    scale = TARGET_EM_PX / units_per_em
    baseline = HEIGHT * 0.68

    def text_to_paths(text: str) -> tuple[list[str], float]:
        paths: list[str] = []
        pen_x = 0.0
        for ch in text:
            gname = cmap.get(ord(ch))
            if gname is None:
                print(f"MISSING glyph {ch!r} U+{ord(ch):04X}")
                pen_x += units_per_em * 0.3
                continue
            aw, _lsb = hmtx[gname]
            sp = SVGPathPen(glyph_set)
            tp = TransformPen(sp, Transform(1, 0, 0, 1, pen_x, 0))
            glyph_set[gname].draw(tp)
            d = sp.getCommands()
            if d:
                paths.append(d)
            pen_x += aw
        return paths, pen_x

    line_data: list[tuple[str, list[str], float, float]] = []
    for text in LINES:
        paths, total_w = text_to_paths(text)
        width_px = total_w * scale
        print(f"{text!r} width_px={width_px:.1f} paths={len(paths)}")
        line_data.append((text, paths, total_w, width_px))

    xs = [(WIDTH_CANVAS - w) / 2 for *_rest, w in line_data]

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH_CANVAS}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH_CANVAS} {HEIGHT}" role="img" aria-labelledby="title">\n'
    )
    title = " ".join(LINES)
    parts.append(f'  <title id="title">{title}</title>\n')
    parts.append(
        "  <desc>GT Eesti Display Regular Italic typing intro.</desc>\n"
    )
    parts.append("  <defs>\n    <style>\n")
    parts.append(
        """    svg { color: #000000; }
    @media (prefers-color-scheme: dark) {
      svg { color: #EDEDED; }
    }
    .clip-rect {
      animation-duration: 9s;
      animation-timing-function: steps(24, end);
      animation-iteration-count: infinite;
    }
    .clip-rect-0 { animation-name: type0; }
    .clip-rect-1 { animation-name: type1; }
    .clip-rect-2 { animation-name: type2; }
    .line-wrap {
      opacity: 0;
      animation-duration: 9s;
      animation-timing-function: linear;
      animation-iteration-count: infinite;
    }
    .line-wrap-0 { animation-name: show0; }
    .line-wrap-1 { animation-name: show1; }
    .line-wrap-2 { animation-name: show2; }
    @keyframes show0 {
      0%, 32.5%, 100% { opacity: 0; }
      1%, 30% { opacity: 1; }
    }
    @keyframes show1 {
      0%, 33%, 65.5%, 100% { opacity: 0; }
      34%, 63% { opacity: 1; }
    }
    @keyframes show2 {
      0%, 66%, 98.5%, 100% { opacity: 0; }
      67%, 96% { opacity: 1; }
    }
"""
    )

    for i, (_text, _paths, _total_w, width_px) in enumerate(line_data):
        w = round(width_px, 1)
        if i == 0:
            parts.append(
                f"""    @keyframes type0 {{
      0% {{ width: 0; }}
      15% {{ width: {w}px; }}
      30% {{ width: {w}px; }}
      32.5%, 100% {{ width: 0; }}
    }}
"""
            )
        elif i == 1:
            parts.append(
                f"""    @keyframes type1 {{
      0%, 33% {{ width: 0; }}
      48% {{ width: {w}px; }}
      63% {{ width: {w}px; }}
      65.5%, 100% {{ width: 0; }}
    }}
"""
            )
        else:
            parts.append(
                f"""    @keyframes type2 {{
      0%, 66% {{ width: 0; }}
      81% {{ width: {w}px; }}
      96% {{ width: {w}px; }}
      98.5%, 100% {{ width: 0; }}
    }}
"""
            )

    parts.append("    </style>\n")
    for i, (_text, _paths, _total_w, width_px) in enumerate(line_data):
        x = xs[i]
        parts.append(
            f"""    <clipPath id="clip{i}">
      <rect class="clip-rect clip-rect-{i}" x="{x:.2f}" y="0" width="0" height="{HEIGHT}" />
    </clipPath>
"""
        )
    parts.append("  </defs>\n")

    for i, (_text, paths, _total_w, _width_px) in enumerate(line_data):
        x = xs[i]
        parts.append(
            f'  <g class="line-wrap line-wrap-{i}" clip-path="url(#clip{i})">\n'
        )
        parts.append(
            f'    <g fill="currentColor" transform="translate({x:.2f} {baseline:.2f}) '
            f'scale({scale:.6f} {-scale:.6f})">\n'
        )
        for d in paths:
            parts.append(f'      <path d="{d}" />\n')
        parts.append("    </g>\n  </g>\n")

    parts.append("</svg>\n")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("".join(parts), encoding="utf-8")
    print("wrote", OUT_PATH, "bytes", OUT_PATH.stat().st_size)


if __name__ == "__main__":
    main()
