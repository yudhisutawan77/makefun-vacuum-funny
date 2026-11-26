"""Robot vacuum excuse entry for make.fun.

Writes one funny excuse line to /output/entry.txt (or the path the
grader hands us through ENTRY_OUT / MAKEFUN_OUTPUT_DIR).
Stdlib only.
"""

import os
import sys

# The entry: one line, a robot vacuum owning up to a missed spot.
# Vacuum world (dust bunny, couch), first-person machine voice,
# a real joke rather than a cute observation.
ENTRY = (
    "I missed that spot because the dust bunny under the couch "
    "pays rent, and evicting it is above my pay grade."
)


def resolve_output_path():
    """Pick where entry.txt goes.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    (directory) -> /output/entry.txt -> ./entry.txt (last resort).
    """
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        parent = os.path.dirname(entry_out) or "."
        if os.path.isdir(parent):
            return entry_out
        return entry_out

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if out_dir:
        return os.path.join(out_dir, "entry.txt")

    if os.path.isdir("/output"):
        return "/output/entry.txt"

    return os.path.join(os.getcwd(), "entry.txt")


def main():
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the gate counts characters, so the file
    # holds exactly the entry line, nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
