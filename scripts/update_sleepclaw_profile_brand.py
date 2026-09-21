"""Update the profile banner while preserving its owl and Georgia subtitle style.

Requires fontTools. Supply the current SleepClaw lockup SVG and a locally licensed
Georgia Italic font; only outlined artwork is written to the public repository.
"""
from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/sleepclaw/sleepclaw-coming-soon-v12.svg"
OUTPUT = ROOT / "assets/sleepclaw/sleepclaw-is-coming-v13.svg"
NS = {"s": "http://www.w3.org/2000/svg"}


def extract(source: str, pattern: str) -> str:
    matches = re.findall(pattern, source, re.S)
    if len(matches) != 1:
        raise ValueError(f"Expected one match, got {len(matches)}: {pattern}")
    return matches[0]


def outline(font: TTFont, text: str) -> tuple[list[str], float]:
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    tracking = -0.015 * font["head"].unitsPerEm
    paths, x = [], 0.0
    for ch in text:
        name = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(TransformPen(pen, Transform(1, 0, 0, 1, x, 0)))
        if pen.getCommands():
            paths.append(pen.getCommands())
        x += font["hmtx"].metrics[name][0] + tracking
    return paths, x - tracking


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lockup", type=Path, required=True)
    parser.add_argument("--subtitle-font", type=Path, required=True)
    args = parser.parse_args()
    source = SOURCE.read_text(encoding="utf-8")
    brand = args.lockup.read_text(encoding="utf-8")
    title_pattern = r'  <g class="sc-wordmark sc-wordmark-title"[^>]*>.*?</g>'
    subtitle_pattern = r'  <g class="sc-wordmark sc-wordmark-subtitle"[^>]*>.*?</g>'
    title = extract(brand, title_pattern)
    gradient = extract(brand, r'    <linearGradient id="sc-wordmark-light"[^>]*>.*?</linearGradient>')
    old_subtitle = extract(source, subtitle_pattern)
    with TTFont(args.subtitle_font) as font:
        if font["name"].getDebugName(4) != "Georgia Italic":
            raise ValueError("The subtitle must keep Georgia Italic")
        # Verify that this font and spacing reproduce the existing letterforms.
        old_paths, _ = outline(font, "Coming soon...")
        if old_paths != re.findall(r'<path d="([^"]+)"', old_subtitle):
            raise ValueError("Subtitle font/spacing does not reproduce the original artwork")
        paths, width = outline(font, "is coming")
    opening = old_subtitle.split(">", 1)[0]
    opening = re.sub(r'data-outline-width="[^"]+"',
                     f'data-outline-width="{width * 0.02201343:.3f}" data-text="is coming"', opening)
    subtitle = opening + ">\n" + "\n".join(f'    <path d="{d}" />' for d in paths) + "\n  </g>"
    result = re.sub(title_pattern, lambda _: title, source, count=1, flags=re.S)
    result = re.sub(subtitle_pattern, lambda _: subtitle, result, count=1, flags=re.S)
    result = result.replace("    <style>", gradient + "\n    <style>", 1)
    result = result.replace(".sc-wordmark-title { fill: #17171A; }",
                            ".sc-wordmark-title { fill: url(#sc-wordmark-light); }")
    result = result.replace("      @media (prefers-color-scheme: dark) {\n"
                            "        .sc-wordmark-title { fill: #EDEDED; }\n      }\n", "")
    result = result.replace("Coming soon...", "is coming")
    before, after = ET.fromstring(source), ET.fromstring(result)
    # Preserve all original owl shapes, paint definitions, and motion rules.
    mascot = ".//s:g[@id='sc-mascot']"
    assert ET.tostring(before.find(mascot, NS)) == ET.tostring(after.find(mascot, NS))
    for node in before.find("s:defs", NS):
        if node.tag.endswith("style"):
            continue
        match = after.find(f".//*[@id='{node.attrib['id']}']")
        assert ET.tostring(node) == ET.tostring(match)
    motion = r"<style>(.*?)      \.sc-wordmark-title"
    assert extract(source, motion) == extract(result, motion)
    assert 'data-text="SleepClaw."' in title
    assert "Coming soon" not in result
    OUTPUT.write_text(result, encoding="utf-8")
    print(f"Wrote {OUTPUT.name}; owl and animations unchanged; Georgia style verified")


if __name__ == "__main__":
    main()
