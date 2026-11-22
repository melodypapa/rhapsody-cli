## SWR_CORE_00011: IRPApplication Wrapper

**ID:** SWR_CORE_00011
**Title:** IRPApplication wraps IRPApplication, the Rhapsody application entry point
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPApplication` JavaDoc interface represents the Rhapsody application. The
Python `RhapsodyApplication` shall expose connection lifecycle (`connect`,
`disconnect`, `quit`), project access (`get_projects`, `open_project`,
`create_new_project`, `active_project`), UI control
(`get_is_hidden_ui`, `set_hidden_ui`, `bring_window_to_top`) and application
information (`get_version`, `get_build_no`, `get_omroot`).
This is the application layer, not a model-element wrapper, so §2's canonical
package move is N/A: the wrapper stays at `src/rhapsody_cli/application.py` and
calls `com_utils.*` directly.
Every catalog-backed COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: `projects`, `isHiddenUI`, `BuildNo` and
`OMROOT` are **properties** read/written via `get_com_property`/`set_com_property`,
and `setHiddenUI` is a method called via `call_com`.
`connect` and `disconnect` are python-only facade helpers with no static COM
member; they have live callers throughout the codebase, so their removal is a
blocker recorded rather than performed. `close_all_projects` and
`get_rhapsody_dir` were python-only conveniences that could never succeed at
runtime (their COM members do not exist and the live integration tests pinned
`AttributeError`); they were removed in the 2026-11-22 review fix — the
integration teardown closes each project through the exposed `IRPProject.close()`
member instead.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication
**Last Changed:** 2026-11-22
