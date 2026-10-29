"""Exercise extraction, tracking, fitting, and protection of prior outputs.

Run with the skill's Python environment: python scripts/test_pipeline.py
Requires FFmpeg and requirements.txt. All artifacts stay in a verified temp dir.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import cv2
import numpy as np

scripts = Path(__file__).resolve().parent


def run(*args, success=True):
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf8")
    assert (result.returncode == 0) == success, result.stderr
    return result


with tempfile.TemporaryDirectory(prefix="ui-animation-check-") as directory:
    root = Path(directory).resolve()
    assert root.parent == Path(tempfile.gettempdir()).resolve()
    frames = root / "fixture"
    frames.mkdir()
    for i in range(31):
        image = np.zeros((120, 240, 3), dtype=np.uint8)
        if i:
            x = 10 + (i - 1) * 3
            image[40:60, x:x + 20] = 255
        assert cv2.imwrite(str(frames / f"frame_{i + 1:04d}.png"), image)
    video = root / "fixture.mkv"
    run("ffmpeg", "-v", "error", "-n", "-framerate", "30", "-start_number", "1",
        "-i", str(frames / "frame_%04d.png"), "-c:v", "ffv1", str(video))
    out = root / "extracted"
    extract = [sys.executable, str(scripts / "extract_frames.py"), str(video), str(out)]
    run(*extract, "--fps", "30", "--cols", "8")
    assert len(list(out.glob("frame_*.png"))) == 31
    assert cv2.imread(str(out / "contact_sheet.png")) is not None
    run(sys.executable, str(scripts / "track_motion.py"), str(out))
    metrics = json.loads((out / "metrics.json").read_text())
    tracked = [row for row in metrics["timeline"] if row.get("present") is not False]
    assert len(tracked) == 30
    assert tracked[0]["x"] == 10 and tracked[-1]["x"] == 97
    fit = json.loads(run(sys.executable, str(scripts / "fit_curves.py"),
                         str(out / "metrics.json"), "--fps", "30", "--property", "translate").stdout)
    assert fit["duration_ms"] == 967
    assert fit["properties"]["translate"]["bezier"]["error"] < 0.02
    before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()}
    run(*extract, success=False)
    after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()}
    assert after == before
    run(*extract[:-1], str(root / "invalid"), "--cols", "0", success=False)
    assert not (root / "invalid").exists()
    # The context manager removes only this resolved temporary directory.
    assert root.parent == Path(tempfile.gettempdir()).resolve()

print("PASS: 31 frames, 30 tracked positions, low-error linear fit, prior files preserved")
