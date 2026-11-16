"""Turns titles into URL slugs."""

import re
import sys
import unicodedata


def slugify(title: str) -> str:
    """Returns title as a lowercase slug of ASCII letters, digits and dashes."""
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-")
    return text.lower()


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: slug.py TITLE", file=sys.stderr)
        return 2
    print(slugify(argv[0]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
