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
`set_use_unique_stereotype_and_ref_cache`, `get_active_configuration`,
`get_default_directory_scheme`/`set_default_directory_scheme`,
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
`set_global_configuration` and `set_use_unique_stereotype_and_ref_cache` are
catalog blockers whose legacy dual-binding sites are left unchanged. Several
members (`add_actor`, `add_class`, `add_node`, `delete_node`, `find_node`,
`get_nodes`, `get_packages`) are COM extensions absent from the JavaDoc and are
documented as such. The module uses `from __future__ import annotations` with
unquoted type references and local imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
(class renamed from `RPProject`; §2 canonical package move completed; 22 legacy
call sites migrated; 2 catalog-absent sites left unchanged)
**Last Changed:** 2026-11-22
