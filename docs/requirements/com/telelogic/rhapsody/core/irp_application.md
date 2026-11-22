## SWR_CORE_00011: IRPApplication Wrapper

**ID:** SWR_CORE_00011
**Title:** IRPApplication wraps IRPApplication, the Rhapsody application entry point
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPApplication` JavaDoc interface represents the Rhapsody application. The
Python `RhapsodyApplication` shall expose connection lifecycle (`connect`,
`disconnect`, `quit`), project access (`get_projects`, `open_project`,
`create_new_project`, `active_project`, `close_all_projects`), UI control
(`get_is_hidden_ui`, `set_hidden_ui`, `bring_window_to_top`) and application
information (`get_version`, `get_build_no`, `get_omroot`, `get_rhapsody_dir`).
This is the application layer, not a model-element wrapper, so §2's canonical
package move is N/A: the wrapper stays at `src/rhapsody_cli/application.py` and
calls `com_utils.*` directly.
The three migrated sites use exactly one pywin32 member each from
`docs/reports/pywin32_authority.json`: `projects` and `isHiddenUI` are
**properties** read via `get_com_property`, and `setHiddenUI` is a method called
via `call_com`. `getBuildNo`/`BuildNo` and `getOMROOT`/`OMROOT` are documented
binding differences left unchanged. `connect`, `disconnect`, `close_all_projects`
and `get_rhapsody_dir` are python-only facade helpers with no static COM member;
they have live callers throughout the codebase, so their removal is a blocker
recorded rather than performed.
**Last Changed:** 2026-11-22
