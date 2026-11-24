## SWR_ELEM_00001: IRPProject Wrapper

**ID:** SWR_ELEM_00001
**Title:** IRPProject wraps IRPProject, the top-level project container
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPProject` JavaDoc interface represents the top-level Rhapsody project. The
Python `IRPProject` shall extend `IRPPackage` and expose Java-mirrored creation and
lookup methods (`add_class`, `add_actor`, `add_node`, `find_node`, `delete_node`),
gateway/report operations (`gateway_export_to_xml`, `gateway_export_to_xml2`,
`generate_report`), configuration (`set_global_configuration`,
`use_unique_stereotype_and_ref_cache`, `active_configuration`,
`default_directory_scheme`, `set_active_component`/`set_active_configuration`,
`get_notify_plugin_on_elements_changed`/`set_notify_plugin_on_elements_changed`,
`set_wait_dialog_watchdog_value`), CDM/diagram helpers (`get_new_collaboration`,
`get_code_generated_files`, `get_active_custom_views_on_browser`,
`get_active_custom_views_on_diagram`, `get_remote_resource_packages`,
`get_roundtrip_shadow_model`, `is_actively_managed`,
`check_events_base_ids_solve_collisions`, `get_new_progress_bar`,
`enable_rhapsody_model_manager`, `migrate_design_manager_links`).
The wrapper registers itself for meta class `"Project"`.
Catalog-backed members call exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: property-shaped members use
`get_com_property`/`set_com_property` and method-shaped members use `call_com`.
`active_component`, `active_configuration`, `all_stereotypes`,
`cg_simplified_model_package`, `components`, `default_directory_scheme`, `nodes`,
`packages`, `profiles`, and `use_unique_stereotype_and_ref_cache` are exposed as
Python `@property` accessors. `active_component`/`active_configuration` keep
method-shaped `set_active_component`/`set_active_configuration` setters because
pywin32 exposes those as methods. `set_global_configuration` is a catalog blocker
whose legacy dual-binding site is left unchanged. Several members (`add_actor`,
`add_class`, `add_node`, `delete_node`, `find_node`, `nodes`, `packages`) are COM
extensions absent from the JavaDoc and are documented as such. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.
Every wrapper signature matches the pywin32 parameter list (arity and types) for
the 21 members that previously took fewer arguments: `find_element_by_file_name`
(`theFolderName`, `theFileName`), `locate_in_ide` (`config`, `filename`,
`lineNumber`), `gateway_export_to_xml` (`filename`, `params`),
`gateway_export_to_xml2` (`filename`, `params`, `proj`), `generate_report`
(`modelscope`, `templatename`, `docType`, `filename`, `showDocument`,
`silentMode`), `add_custom_view_on_diagram`/`remove_custom_view_on_diagram`
(`diagram`, `customView`), `apply_browser_custom_views_on_diagrams` (`newVal`),
`get_active_custom_views_on_diagram` (`diagram`), `close_csv_file`/
`reload_csv_file` (`fullCSVFileName`), `apply_roundtrip_diff_merge`
(`magicNumber`, `shadowModel`, `filesToUpdate`), `find_elements_with_oslc_link`
(`type`, `purl`), `get_roundtrip_shadow_model` (`magicNumber`),
`import_package_from_rose` (`projectName`, `packageName`, `logFileName`),
`import_project_from_rose` (`projectName`, `logFileName`),
`add_spell_checker_result` (`value`), `clean_unresolved_elements`
(`rootElement`), `get_new_progress_bar` (`amount`, `name`),
`get_requirements_by_id` (`requirementID`, `returnFirstFoundOnly`) and
`save_as_prev_version` (`filename`, `prevVersion`).
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
(class renamed from `RPProject`; §2 canonical package move completed; 22 legacy
call sites migrated; 2 catalog-absent sites left unchanged)
**Last Changed:** 2026-11-25
