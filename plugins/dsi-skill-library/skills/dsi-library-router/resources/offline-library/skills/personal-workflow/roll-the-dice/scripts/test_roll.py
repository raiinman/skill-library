"""Small regression check for the draw report and invalid candidate lists."""

import json
from pathlib import Path
import subprocess
import sys


script = Path(__file__).with_name("roll.py")


def run(*options):
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(script), "--", *options],
        capture_output=True, text=True, encoding="utf-8", timeout=5,
    )


options = ["Keep the existing layout", "Try the café layout", "Use the compact layout"]
result = run(*options)
assert result.returncode == 0, result.stderr
draw = json.loads(result.stdout)
assert draw["options"] == options
assert 1 <= draw["draw"] <= len(options)
assert draw["selected"] == options[draw["draw"] - 1]

for invalid in ([], ["Only one"], ["A", "A"], ["A", " A "], ["A", "  "]):
    result = run(*invalid)
    assert result.returncode != 0 and not result.stdout, invalid

print("Draw reporting and invalid-option checks passed.")
