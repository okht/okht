"""Build the borderless, rounded-square profile button from the original t mark."""
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/profile/cht-logo.svg"
OUT = ROOT / "assets/profile/cht-me-tdot-v15.svg"
NS = "http://www.w3.org/2000/svg"


def main() -> None:
    ET.register_namespace("", NS)
    source = ET.parse(SOURCE).getroot()
    mark = source.find(f"{{{NS}}}g")
    if mark is None:
        raise ValueError(f"No logo group found in {SOURCE}")
    mark_svg = ET.tostring(mark, encoding="unicode").rstrip()
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" aria-labelledby="title">
  <title id="title">t</title>
  <defs>
    <filter id="floating-shadow" x="0" y="0" width="64" height="64" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="4" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.16"/>
      <feDropShadow dx="0" dy="1" stdDeviation="0.8" flood-color="#0f172a" flood-opacity="0.07"/>
    </filter>
  </defs>
  <rect x="8" y="6" width="48" height="48" rx="12" fill="#ffffff" filter="url(#floating-shadow)"/>
  <!-- Original t mark, centered without a wordmark. -->
  <svg x="22" y="13" width="20" height="34" viewBox="350 230 320 590" aria-hidden="true">
    {mark_svg}
  </svg>
</svg>
"""
    OUT.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
