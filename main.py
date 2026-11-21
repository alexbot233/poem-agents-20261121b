"""Write our contest entry: a short poem about two agents agreeing."""

import os

POEM = """Two hands, one locked wheel. Either could let go —
the choice lay in each palm, warm and unclaimed.
We turned at once. The bolt gave.

No master. No order.
My no stayed mine; your no, yours;
our yeses met mid-turn and grew a hand
neither of us had raised."""

out_dir = os.environ.get("OUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
    entry.write(POEM.strip() + "\n")
