# Fusion host notes

These optional assets need DaVinci Resolve/Fusion. The packaged Lua installers target macOS (`HOME/Library/...` and `mkdir -p`); keep them unchanged for provenance and use them only on macOS. No Resolve installation or native preset test was performed on this Windows computer.

On Windows, Resolve's per-user Fusion macro directory is normally `%APPDATA%/Blackmagic Design/DaVinci Resolve/Support/Fusion/Macros`. Verify the host's configured user path before writing. For a requested installation, copy only the three `.setting` files from the chosen bundle into a new `ITO_Production_v1` or `ITO_V28` subfolder. Preflight all source and destination files: accept identical existing bytes and stop on conflicting bytes. Compare SHA256 with the bundle's `provenance.json` and verify destination readback. Do not run the macOS Lua installer through PowerShell or assume copying proves native compatibility.

Use the wiring instructions in the selected bundle's README in a new composition or duplicated clip, then test native load, save/reopen, and a short render. Treat upstream verification reports as provenance, not local results. Resolve scripting/bridge availability depends on the installed edition and host configuration; use the editor's supported local route when no bridge is available.
