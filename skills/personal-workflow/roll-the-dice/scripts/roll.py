"""Choose uniformly from a fixed list and report the actual draw."""

import argparse
import json
import secrets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("options", nargs="+", help="Two or more distinct option labels")
    options = parser.parse_args().options
    if len(options) < 2:
        parser.error("Supply at least two options.")
    if any(not option.strip() for option in options):
        parser.error("Option labels must not be blank.")
    if len({option.strip() for option in options}) != len(options):
        parser.error("Use distinct labels so each option receives equal probability.")
    index = secrets.randbelow(len(options))
    print(json.dumps({"options": options, "draw": index + 1, "selected": options[index]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
