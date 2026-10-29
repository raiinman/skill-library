---
name: the-forge
description: Use The Forge framework for custom-engine rendering, platform bring-up,
  shader/resource loading and native graphics sample integration. Use when extending
  a native engine rather than adding a turnkey game engine.
license: Apache-2.0
---

# The Forge

Read [the source map](references/source-map.md) for pinned official docs and archived inputs. Before using API/build syntax, use Context7 for this exact library where available; otherwise use its official version-matched docs and headers. Honor the project's existing engine and dependency choices. Gather compatibility details from the project first, and request only genuinely missing blocking information.

Treat The Forge as cross-platform programming/rendering infrastructure. Confirm that a custom engine or native renderer integration is intended; it is not a drop-in Godot/Unity/Unreal gameplay plug-in. Record the exact revision, host compiler, graphics API, platform SDKs and existing build system.

Start with the matching upstream sample and its actual build instructions. Inspect pre-build scripts before running them: they can fetch separate assets and tools, and this skill installation has not downloaded those payloads. Confirm platform prerequisites and legal access. Public desktop/mobile code does not grant access to proprietary console SDKs or the separately licensed console platform components.

Bring up one supported sample, then integrate the minimum renderer, application/window/input lifecycle and resource-loader pieces required by the host. Preserve API-specific synchronization, frame resources, descriptor lifetimes, shaders and asset paths. Use the framework's current FSL/shader generation flow for the selected version instead of mixing older tutorial interfaces with current headers.

Validate startup/shutdown, resize/minimize, device/resource failures, asset loading and a simple rendered scene on each requested API/platform. Enable applicable validation/debug tooling and report shader/runtime errors. Add animation or advanced rendering systems only when required, keeping their formats and ownership boundaries explicit.

Deliver the scoped integration or authored asset with reproducible dependency/conversion settings and the checks actually performed. Installation of this skill supplies guidance and source snapshots, not compiled SDKs, an engine plug-in, a live MCP service or evidence of game integration. Install/build a project dependency when the user's concrete integration task needs it. Preserve unrelated project files and existing assets; keep outputs and migrations recoverable.
