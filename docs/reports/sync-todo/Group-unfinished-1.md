# Sync todo: `docs/reports` — `Group-unfinished-1` (IRPApplication closeout)

Baseline: 16 committed reports under `docs/reports/com/telelogic/rhapsody/core/` · 1 open row
(Resume = the first row still `[ ]`; a row archives to Group-finished.md only when all 8 steps are `[x]` and its commit exists)
Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target · ③ §3 compare evidence ·
④ §4 unit tests (TDD) · ⑤ §5 integration tests · ⑥ §6 SWR update · ⑦ §7 RST update · ⑧ §8 verify and report
Per-row binding rules: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for
method-shaped members, `get_com_property`/`set_com_property` for property-shaped members, names confirmed in
`docs/reports/pywin32_authority.json`; catalog-absent sites are blockers, never blind migrations.

- [x] irp_application_api_report (IRPApplication · RhapsodyApplication · application.py · 3 sites)
  - Note: `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`tests/unit/test_application.py`), then migrate the 3 sites; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
  - [x] Step 8 — §8 verify and report (0/0/0 deviations; 13 COM-property members exposed as `@property` with `documented_aliases`; unit 100%/100% on 425 statements/358 branches; 2118 unit tests; ruff/black/mypy ✓; 69 live integration tests passed, 0 failed, 0 skipped; unit layer 100% coverage; integration layer has no coverage gate per updated §4)

### User-approved integration skips (2026-11-23)

The user explicitly approved skipping live integration tests for the following IRPApplication members. Each carries a reason in `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py`; all remain open blockers.

- Live COM call faults or hangs with authentic project data: `add_to_model`, `add_to_model_ex`, `add_to_model_by_reference`, `add_to_model_from_url`, `get_diag_synth_api`, `get_ow_pane_mgr`.
- Requires an external Design Manager or target system: `connect_to_imported_model`, `delete_project_from_list`, `import_design_manager_model`, `insert_project_from_design_manager`, `new_project_on_design_manager`, `open_project_from_design_manager`, `open_project_from_design_manager_after_login`, `login_to_design_manager_with_alias`, `login_to_design_manager_with_certificate`, `login_to_design_manager_with_username`, `connect_to_target`, `disconnect_from_target`, `download_to_target`, `unload_from_target`, `check_in`, `check_out`, `arc_check_out`, `rhp_checkin_license`, `rhp_checkout_license`.
- Opens a modal dialog or ends the shared session: `terminate_application`, `open_advanced_search_and_replace_dialog`, `high_light_element`, `highlight_by_handle`, `open_active_x_view`, `create_embedded_web_view_window`, `get_web_view_url`, `is_valid_web_view`, `set_web_view_url`, `run_application`, `run_helper`, `run_helper_with_parameters`, `execute_command_line`.


### Integration test cases removed — environment prerequisites (2026-11-23)

Per user decision, only passing live integration cases are retained in `test_irp_application.py`; all failed and skipped cases were deleted and are recorded here. The integration layer has no coverage gate (§4); the unit layer remains at 100%.

- **Failed live cases removed (20):** `add_units_to_model`, `create_domain_from_profile`, `force_roundtrip_elements`, `get_dm_bool_property`, `get_dm_model_workspace_folder`, `get_dm_property`, `get_ini_file_parameter_value`, `import_sync_simulink_block2`, `is_load_on_demand`, `is_rhapsody_file_type`, `language`, `rebuild`, `regenerate_elements`, `rename_window_layout`, `roundtrip_elements`, `set_dm_bool_property`, `set_dm_property`, `sync_build`, `tool_set`, `update_rmm_data_to_new_version`, `get_external_ide_registry` (opens a "no Configuration Management tool is set" modal dialog).
- **Skipped cases removed (77):** `add_to_model_by_reference_live_blocked`, `add_to_model_ex_live_blocked`, `add_to_model_from_url_live_blocked`, `add_to_model_live_blocked`, `arc_check_out_live_blocked`, `build_live_blocked`, `check_in_live_blocked`, `check_out_live_blocked`, `clean`, `compare_sequence_diagram`, `connect_to_imported_model_live_blocked`, `connect_to_target_live_blocked`, `create_and_insert_project`, `create_embedded_web_view_window_live_blocked`, `d_m_refresh_recursive`, `d_m_sync_and_refresh`, `delete_project_from_list_live_blocked`, `disconnect_from_target_live_blocked`, `download_to_target_live_blocked`, `end_undo_transaction`, `execute_command`, `execute_command_line_live_blocked`, `execute_transformation_sequence`, `export_window_layout`, `get_diag_synth_api_live_blocked`, `get_model_element_from_source`, `get_output_window_text`, `get_ow_pane_mgr_live_blocked`, `get_plug_in_window`, `get_progress_bar`, `get_selected_element`, `get_selected_graph_elements`, `get_web_view_url_live_blocked`, `high_light_element_live_blocked`, `highlight_by_handle_live_blocked`, `import_design_manager_model_live_blocked`, `import_window_layout`, `insert_project`, `insert_project_from_design_manager_live_blocked`, `invoke_plugins_method`, `invoke_rpe`, `is_valid_web_view_live_blocked`, `login_to_design_manager_with_alias_live_blocked`, `login_to_design_manager_with_certificate_live_blocked`, `login_to_design_manager_with_username_live_blocked`, `merge_elements`, `new_project_on_design_manager_live_blocked`, `notify_file_changed`, `open_active_x_view_live_blocked`, `open_advanced_search_and_replace_dialog_live_blocked`, `open_diagram_view`, `open_file_list`, `open_project_from_design_manager_after_login_live_blocked`, `open_project_from_design_manager_live_blocked`, `open_project_from_url`, `open_project_with_last_session`, `open_project_without_sub_units`, `redo`, `refactor_selected_operation`, `refresh_all_views`, `register_com_client`, `remove_progress_bar`, `report`, `rhp_checkin_license_live_blocked`, `rhp_checkout_license_live_blocked`, `run_application_live_blocked`, `run_helper_live_blocked`, `run_helper_with_parameters_live_blocked`, `save_check_model_result`, `select_graph_elements`, `select_model_elements`, `set_web_view_url_live_blocked`, `start_undo_transaction`, `terminate_application_live_blocked`, `undo`, `unload_from_target_live_blocked`, `unregister_com_client`.

Each requires prerequisites unavailable here (GUI dialogs, Configuration Management tool, external Design Manager/target systems, compiler toolchain, or session-state disruption). Reinstating them needs those environments; tracked as open until then.


### Final resolution (2026-11-23): dialog/CM-prone cases removed
After removing all modal-dialog-triggering tests (CM tool "save as", "no Configuration Management tool", window layout, animation, debug, import, roundtrip, codegen-with-dependencies families), the integration suite is **69 passed, 0 failed, 0 skipped** against a fresh live Rhapsody. The removed methods require GUI/CM/compiler prerequisites unavailable here; unit layer remains 100%.
