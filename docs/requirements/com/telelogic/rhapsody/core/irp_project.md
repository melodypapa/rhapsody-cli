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
Python `@property` accessors. The unique-stereotype cache property is write-only:
JavaDoc declares only its setter and the registered pywin32 interface exposes only
`prop_map_put`, so integration exercises the setter rather than calling a nonexistent getter.
`active_component`/`active_configuration` keep
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
**Last Changed:** 2026-11-26

## SWR_ELEM_00022: IRPProject lifecycle methods live-fixture blocker

**ID:** SWR_ELEM_00022
**Title:** close, become_active_project and remove have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`IRPProject.close()` raises a modal "Projects can only be removed from project
lists" dialog on the session-shared project, `become_active_project()` would
switch the active project out from under the shared fixture, and `remove()`
deletes the session-shared project. Their former integration tests asserted a
mocked `call_com` binding shape, which proves only the call shape and not the
live behaviour (SKILL §5). Those tests were removed; the bindings keep full
fake-COM unit coverage. Live verification needs an isolated project per case and
a session that tolerates project switching, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00024: IRPProject generate_report live-fixture blocker

**ID:** SWR_ELEM_00024
**Title:** generate_report has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`IRPProject.generate_report()` requires a ReporterPLUS `.tpl` template file. No
`.tpl` template ships with the installed Rhapsody build (verified across the
installation, user profile, ProgramData and this workspace), and passing any
other file makes Rhapsody raise a modal "Error Opening the Template" dialog that
blocks COM automation. The former integration test passed a Python source file
as the template, which produced that modal and blocked the live suite. Per SKILL
§5 the test was removed rather than kept as a fake or exception assertion; the
binding keeps full fake-COM unit coverage. Live verification needs a valid
ReporterPLUS template, after which the row can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject.generate_report
**Last Changed:** 2026-11-25

## SWR_ELEM_00028: IRPProject creation and collection live-fixture blocker

**ID:** SWR_ELEM_00028
**Title:** add_class/add_actor/add_node and related getters have no live proof
**Status:** Blocked
**Priority:** Low
**Description:**
`addClass(name)`, `addActor(name)` and `addNode(name)` are catalog-backed methods
with the documented single string argument, but this Rhapsody build rejects them
with HRESULT `0x80040006`. The `nodes` and `all_stereotypes` getter cases are
blocked at their `add_node`/`add_stereotype` setup step for the same reason.
Their integration tests were removed per SKILL §5; the bindings keep full
fake-COM unit coverage. Live verification needs a build that permits these
project-level creations, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00029: IRPProject active component/configuration live-fixture blocker

**ID:** SWR_ELEM_00029
**Title:** active component and configuration access have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`activeConfiguration`, `activeComponent`, `setActiveConfiguration` and
`setActiveComponent` are catalog-backed, but this Rhapsody build rejects both
the getter and the setter with HRESULT `0x80040005`/`0x80040006` regardless of
whether the setter receives the documented name string or the COM object. The
integration tests were removed; the bindings keep full fake-COM unit coverage.
Live verification needs a build that permits switching active configuration,
after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00030: IRPProject gateway and explicit-object live-fixture blocker

**ID:** SWR_ELEM_00030
**Title:** gateway exports and setObjectExplicit/Implicit have no live proof
**Status:** Blocked
**Priority:** Low
**Description:**
`GatewayExportToXML`/`GatewayExportToXML2` are documented as internal-use-only
and fail with `E_FAIL` even with a real output path. `setObjectExplicit` and
`setObjectImplicit` reject a real model element with `E_FAIL`/typemismatch.
Their integration tests were removed per SKILL §5; the bindings keep full
fake-COM unit coverage. Live verification needs the gateway feature and the
correct instance fixture, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00031: IRPProject UseUniqueStereotypeAndRefCache catalog mismatch

**ID:** SWR_ELEM_00031
**Title:** UseUniqueStereotypeAndRefCache has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
The pywin32 catalog and generated `IRPProject` class list
`UseUniqueStereotypeAndRefCache`, but the live Rhapsody instance omits it from
`_prop_map_get_`, so any access raises `AttributeError`. This is a catalog /
runtime type-library mismatch, not a wrapper binding defect. The integration
test was removed per SKILL §5; the binding keeps full fake-COM unit coverage.
Live verification needs an authority catalog regenerated from this build's type
library, after which the row can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject.use_unique_stereotype_and_ref_cache
**Last Changed:** 2026-11-25
