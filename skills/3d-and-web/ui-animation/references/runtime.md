# Local measurement runtime

The three helpers run under Python and FFmpeg on Windows. Resolve `scripts/` paths relative to this installed skill directory, not the project being edited. Run extraction into a new or empty directory each time so frames cannot mix across recordings. Probe the source frame rate and pass it explicitly to extraction and fitting.

On this computer the isolated Python 3.11 environment is:

`C:/Users/mikea/.codex/tools/skill-library-ui-animation/Scripts/python.exe`

It contains the pinned OpenCV, NumPy, and SciPy versions in `requirements.txt`. FFmpeg/ffprobe are already on PATH. Use quoted absolute paths in PowerShell:

```powershell
& 'C:/Users/mikea/.codex/tools/skill-library-ui-animation/Scripts/python.exe' 'C:/Users/mikea/.codex/skills/ui-animation/scripts/test_pipeline.py'
```

On another computer, create an isolated Python 3.11 environment and install this package's requirements. No cloud account, API token, or paid service is required. CSS/Motion/framework libraries belong in the target project only when needed by the requested implementation.

The Codex adaptation replaces FFmpeg's optional glob-pattern input with a numbered PNG sequence, validates positive extraction settings, and refuses populated output directories. The original changed helper is preserved as `upstream-extract_frames.py.txt`. `test_pipeline.py` verifies a synthetic recording through extraction, a contact sheet, known-position tracking, curve fitting, and non-overwrite behavior.

Tracking assumes a static background and detects changes from the first frame. Opacity, blur, and radius measurements are proxies; review the measurement guide before interpreting them. A successful fixture is not proof of accuracy on arbitrary footage or dropped-frame recordings.
