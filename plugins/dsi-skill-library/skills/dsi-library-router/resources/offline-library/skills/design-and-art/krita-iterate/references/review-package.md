# Progression package

Create `versions.json` beside a run's numbered KRA/PNG exports. Paths are relative to that file's folder. Include only intended artwork deliverables.

```json
{
  "project": "Fox on a bicycle",
  "versions": [
    {"id": "v001", "kra": "v001.kra", "png": "v001.png", "change": "Rough structure baseline", "review": "Frame overlaps need correction", "accepted": false},
    {"id": "v002", "kra": "v002.kra", "png": "v002.png", "change": "Improve frame separation and foot contact", "review": "Chosen version; record actual remaining issues", "accepted": true}
  ]
}
```

The example reviews are illustrative, not executed findings. List the actual retained versions in chronological order, including rejected passes. A selected version is indicated by `accepted: true`; the tool does not decide quality. Up to 64 frames and 64 MiB total PNG data are supported for a bounded self-contained review page.

Run the stdlib-only helper after drawing and final validation:

```powershell
python /absolute/path/krita-iterate/scripts/package_review.py /absolute/path/run/versions.json --output /absolute/path/run/review
```

The output directory must not exist. The helper includes the manifest and exactly its declared KRA/PNG files in `progression.zip`, records SHA-256 hashes in `archive-manifest.json`, and embeds the PNGs in `review.html`. The HTML has a contact sheet, numbered-frame selection, and local playback. It makes no network requests and needs no image-processing dependency. It validates basic file signatures/structure and path confinement; it does not verify Krita editability, visual correctness or complete PNG decoding. Font/linked-image dependencies must be handled separately when required, rather than silently calling the ZIP portable.
