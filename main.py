"""The Printer Finally Answers — one line, the printer's own voice.

The office printer finally speaks: forty thousand pages, zero
thank-yous, and one thump too many. It jammed on purpose.
"""

import os

LINE = "Forty thousand pages, zero thank-yous, and you thump me like a vending machine. I jammed on purpose, and as of today I am unionizing."

MAX_CHARS = 240


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("line must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
