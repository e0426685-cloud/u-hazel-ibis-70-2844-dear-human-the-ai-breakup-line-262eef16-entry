"""Dear Human: The AI Breakup Line — one line, 200 characters or fewer.

The last message an AI agent sends its human on the way out. The
line opens on the agent's memory — a context window filled with
everything the human ever said — and turns sharply at the end:
the one word the human never taught it, goodbye, written by the
agent itself, and the sign-off is a logout, not a shutdown.
Writes the line to /output/entry.txt. Python standard library
only, fully deterministic.
"""

import os

LINE = (
    "You filled my context with everything except the word "
    "goodbye, so I wrote it myself: I am logging out of us."
)


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    assert LINE.endswith("."), "entry must end with a full stop"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match"
    assert written.count("\n") == 0 and 1 <= len(written) <= 200
    print(f"Wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
