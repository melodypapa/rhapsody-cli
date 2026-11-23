## SWR_CORE_00011: IRPApplication Wrapper

**ID:** SWR_CORE_00011
**Title:** IRPApplication wraps IRPApplication, the Rhapsody application entry point
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPApplication` JavaDoc interface represents the Rhapsody application. The
canonical Python wrapper `IRPApplication` (model layer, Java-derived package
path) exposes the COM-bound surface: project access (`get_projects`,
`open_project`, `create_new_project`, `active_project`), UI control
(`get_is_hidden_ui`, `set_hidden_ui`, `bring_window_to_top`), application
information (`get_version`, `get_build_no`, `get_omroot`), code generation
(`generate`, `generate_elements`, `generate_entire_project`, `regenerate`),
model import (`add_to_model`, `add_to_model_ex`), diagnostics
(`check_model`, `set_log`), collection creation (`create_new_collection`),
`quit`, and the support-manager accessors (`get_search_manager`,
`get_selection`, `get_code_gen_simplifiers_registry`, `get_diag_synth_api`,
`get_external_checker_registry`, `get_external_ide_registry`,
`get_external_roundtrip_invoker`, `get_ow_pane_mgr`).
The connection lifecycle is pure Python orchestration with no COM member of
its own and lives on the `RhapsodyApplication` facade
(`src/rhapsody_cli/application.py`), which **subclasses** `IRPApplication`:
`connect` (attach-first with launch fallback), `_attach`/`_launch`, and
`disconnect` (a cleanup hook delegating to the inherited `quit`). COM calls
inside `_attach`/`_launch` (`GetActiveObject`/`Dispatch` on the Rhapsody2
Prog ID) are connection plumbing, not interface members.
Every catalog-backed COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: `projects`, `isHiddenUI`, `BuildNo` and
`OMROOT` are **properties** read via `get_com_property`; every other member is
a **method** called via `call_com` (shape confirmed by the regenerated
`IRPApplication_api_report.md` MATCH rows).
The remaining ~140 Java members that pywin32 exposes but the wrapper
deliberately omits are recorded as
`documented_intentionally_unsupported` in `docs/reports/pywin32_authority.json`
and appear in the generated report's Wrapper Backlog as
`INTENTIONALLY_UNSUPPORTED_DOCUMENTED`.
`close_all_projects` and `get_rhapsody_dir` were python-only conveniences that
could never succeed at runtime (their COM members do not exist and the live
integration tests pinned `AttributeError`); they were removed in the
2026-11-22 review fix — the integration teardown closes each project through
the exposed `IRPProject.close()` member instead.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_application.py:IRPApplication; facade src/rhapsody_cli/application.py:RhapsodyApplication (subclass)
**Last Changed:** 2026-11-23
