---
name: uefn-toolbelt
description: Inspect and automate Unreal Editor for Fortnite through UEFN Toolbelt when its MCP server and editor listener are available. Use for UEFN actors, assets, devices, imports, level inspection, Toolbelt setup, and choosing existing editor tools; exclude ordinary Unreal Engine projects and unrelated game engines.
metadata:
  library_source:
    kind: installed-local-snapshot
    original_skill_sha256: 4bb802f0fbb642b50bcb1b585027784ff9f63bf282293ad36b0e2e629fff7436
---

# UEFN Toolbelt

## Execution contract

Input: the intended UEFN project/level and requested inspection or editor operation.
Output: inspected state or the requested scoped change, verified by editor readback.
Requires an actual UEFN Toolbelt MCP connection and a listener in the intended editor
session. The paths and historical test results below describe the source machine;
check them on this host before using them. If either connection is unavailable,
report setup guidance and leave editor execution unverified. Tool discovery alone
does not prove an editor action succeeded.

## Local installation

- Published repository: `C:/Users/mikea/Documents/MCP/UEFN-TOOLBELT`.
- Global Codex MCP server: `uefn-toolbelt`, running `mcp_server.py` through the repository's `.venv/Scripts/python.exe`.
- The adapter uses MCP Python SDK 1.x (`mcp<2`); SDK 2.x removes its FastMCP API. Keep dependency upgrades separate from ordinary installation.
- The global MCP Verse reference lives under the installation repository's `verse-book/docs/`. Each of the five configured projects also has a documentation-only `verse-book` Git clone for the dashboard. Refresh its status by revisiting Quick Actions.

Read the target project's AGENTS.md chain before editor or project work. For
changes to Toolbelt itself, read the installation repository's AGENTS.md and
WORKORDER.md, then the applicable child guides. Its repository development
gates do not grant permission to operate another project.

## Connect and choose tools

Use this server's `ping`, then `get_level_info` to confirm the intended editor
project/level. Use `list_toolbelt_tools` and `describe_toolbelt_tool` before
`run_toolbelt_tool`; discover supported names and parameter defaults rather
than guessing them or adding an overlapping tool.

Successful MCP startup/tool discovery does not mean the editor listener is
running. The user's five existing UEFN projects are configured for deferred
automatic startup through `C:/Users/mikea/Documents/MCP/uefn-toolbelt-startup`.
Read its `projects.json` for the authorized paths. Startup opens the Qt dashboard
after starting the listener, using private PySide6 libraries in `python-libs`.
Automatic dashboard opening was visually verified in FNSoT after a full restart.
If it is hidden, discover `launch_qt` and call it through `run_toolbelt_tool`
to reopen it; confirm the window appears, since the tool's success reply can
fall back to text mode when PySide6 is missing. Project hooks preserve existing startup code. Open the intended project normally
and confirm a live `ping`; automatic startup passed six offline tests and a live FNSoT check
(ping plus level readback, 97 actors); the other four projects are configured
but have not been opened for live testing.

If the handoff stays missing after loading, inspect `[CODEX TOOLBELT]` editor
logs and the startup configuration before asking the user to type commands.
Toolbelt Quirk #36 concerns Epic MCP's early initialization; a top-bar Toolbelt
menu also fails to render on UEFN 42.00. Opening the Qt dashboard starts its
listener, but that behavior alone does not provide a working menu launcher.

Manual recovery belongs inside UEFN: Window > Output Log, change Cmd to Python,
then run `import UEFN_Toolbelt as tb; tb.register(); tb.run("mcp_start")`. It cannot
run in Windows PowerShell. The user prefers automatic startup without typing
Python. Before Launch Session, Push Changes or publishing, stage project Python
files with the published `prepare_launch.bat` and restore afterward with
`restore_after_launch.bat`, supplying `-Project` and `-ProjectsRoot` explicitly
for these nonstandard paths (Quirk #42).

Install into a named, authorized project with the repository's `install.py`.
Keep the editor startup/manual acceptance steps explicit. The adapter loads the
rotating same-user credential internally; report connection status without
printing the handoff file or copying its token into configuration.

Toolbelt's bridge, Epic's official UEFN MCP, and Trashbyrd Power Tools are
separate surfaces. Use the supported surface for the operation and establish
its capabilities from current tool schemas. Toolbelt is not exposed through
Epic's official MCP server.

## Work and verify

- Inspect actual actors/assets and readable device values before changes; inaccessible settings remain unknown. Read `docs/UEFN_QUIRKS.md` for sandbox and Creative device limits.
- Use project mounts for assets and keyword arguments for Unreal structs. Read `docs/ui_style_guide.md` before Toolbelt window changes.
- Read the structured tool result and verify the intended state afterward. A transport timeout does not cancel the operation; inspect state before repeating a mutation.
- Preserve visual references and asset identity when building environments. Compile/cook results do not establish visual fidelity or gameplay correctness.
- Use Verse reference tools for syntax and verify current UEFN APIs with official documentation and the project compiler; reference examples may describe newer language features.
- Follow the project's deploy, restart, live-test, and publication rules. New Toolbelt modules and persistent Qt/Slate window changes require a full editor restart.


## Local window repair

The dashboard uses normal desktop stacking and restores hidden/minimized
windows through launch_qt. A local repair is installed in all five projects
and the installation repository; it is uncommitted and must be preserved
during updates. FNSoT passed live after a full restart: tool and dashboard windows each came
forward, hidden/minimized dashboard reopened, and saved level retained 98 actors.
Other four projects were not opened for live window verification.
