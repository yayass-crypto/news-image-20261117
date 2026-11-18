"""news-image-20261117 entry: copy the bundled newspaper image to the output dir.

The image (entry.png, 1024x1024, 961776 bytes) is a newspaper front page
summing up Tuesday 17 November 2026: Kerch Bridge struck, Trump in Manila,
tankers hit in Hormuz, Vulcan fails with 40 Amazon satellites lost, plus
JPMorgan's software-bug outage and Nvidia's first post-Huang earnings.
Deterministic: the same bytes are written on every run.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    if not os.path.isfile(SOURCE):
        print("missing bundled image: entry.png", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Guard: the run must reproduce the bundled bytes exactly.
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        print("output size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
