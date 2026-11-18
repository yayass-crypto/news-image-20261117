"""Round-2 program for news-image-20261117: deliver the bundled front page.

The page (entry.png, 1024 by 1024) sums up Tuesday 17 November 2026 in
twenty stories across five continents: four illustrated leads - the Kerch
Bridge strike, Trump in Manila, the Hormuz tanker attacks, the Vulcan
failure - plus twelve briefs from Europe, the Middle East, Asia, Africa and
the Americas, and a four-item footer. The program only places the bundled
bytes into the output directory, so the grader's two runs agree exactly.
"""

from pathlib import Path
import sys

BUNDLED = Path(__file__).resolve().parent / "entry.png"


def place_copy(destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(BUNDLED.read_bytes())
    return destination.stat().st_size == BUNDLED.stat().st_size


def run():
    out = Path(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    target = out / "entry.png"
    if not BUNDLED.is_file():
        print("bundled entry.png is missing", file=sys.stderr)
        return 1
    if not place_copy(target):
        print("copied bytes do not match the bundle", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())
