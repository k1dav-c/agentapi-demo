"""Turns titles into URL slugs."""

import argparse
import re
import sys
import unicodedata


def slugify(title: str, max_length: int | None = None) -> str:
    """Returns title as a lowercase slug of ASCII letters, digits and dashes.

    With max_length, the slug is cut to at most that many characters, at a dash
    where possible so that no word is cut in half.
    """
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    if max_length is None or len(text) <= max_length:
        return text
    cut = text[:max_length]
    if text[max_length] != "-" and "-" in cut:
        cut = cut[: cut.rindex("-")]
    return cut.rstrip("-")


def non_negative_int(value: str) -> int:
    n = int(value)
    if n < 0:
        raise argparse.ArgumentTypeError(f"must not be negative: {value}")
    return n


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="slug.py", description=__doc__)
    parser.add_argument("title")
    parser.add_argument(
        "--max-length",
        type=non_negative_int,
        metavar="N",
        help="cut the slug to at most N characters, at a dash where possible",
    )
    args = parser.parse_args(argv)
    print(slugify(args.title, args.max_length))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
