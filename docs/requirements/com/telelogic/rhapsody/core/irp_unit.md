## SWR_CORE_00002: IRPUnit Save and File Operations

**ID:** SWR_CORE_00002
**Title:** IRPUnit wraps IRPUnit for elements that can be saved as separate files
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPUnit` JavaDoc interface represents model elements that can be saved as separate
files. The Python `IRPUnit` shall extend `IRPModelElement` and expose the Java-mirrored
members declared by `com.telelogic.rhapsody.core.IRPUnit`: cross-project operations
(`copy_to_another_project`, `move_to_another_project_leave_a_reference`,
`reference_to_another_project`), lifecycle (`load`, `save`, `unload`), file/path state
(`get_filename`/`set_filename`, `get_unit_path`, `set_unit_path`, `get_current_directory`,
`get_cm_header`/`set_cm_header`, `get_last_modified_time`), CM/configuration state
(`get_cm_state`, `get_add_to_model_mode`, `get_include_in_next_load`/
`set_include_in_next_load`, `get_is_stub`, `is_read_only`/`set_read_only`,
`is_reference_unit`, `is_separate_save_unit`/`set_separate_save_unit`), language
(`get_language`, `set_language`) and collections (`get_nested_save_units`,
`get_nested_save_units_count`, `get_structure_diagrams`). `set_read_only` shall translate
Python booleans to the COM-style integers 1/0. `AddToModelMode` is an `IntEnum` mirroring
`IRPApplication.AddToModel_Mode` so raw COM integers compare directly.

Every COM call shall target exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`, with no runtime name probing or Java-name fallback:
method-shaped members (`getAddToModelMode`, `getCMState`, `getLanguage`,
`getLastModifiedTime`, `getNestedSaveUnits`, `getNestedSaveUnitsCount`, `isReadOnly`,
`isReferenceUnit`, `isSeparateSaveUnit`, `load`, `save`, `setLanguage`, `setReadOnly`,
`setSeparateSaveUnit`, `setUnitPath`, `unload`, ...) are invoked via `call_com`, and
property-shaped members (`CMHeader`, `currentDirectory`, `filename`, `includeInNextLoad`,
`isStub`, `structureDiagrams`) are read/written via `get_com_property`/`set_com_property`.
The two collection getters wrap the result in `IRPCollection`. `get_unit_path` is a
documented-unavailable `NotImplementedError` stub: the catalog exposes only `setUnitPath`
(the getter `getUnitPath` is an `ACCESSOR_ALIAS_MISMATCH` row in the API report), so the
wrapper raises instead of probing pending Windows typelib evidence. The module uses
`from __future__ import annotations` with unquoted type references; names used only in
`cast()` are imported locally inside the method to avoid circular imports.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py:IRPUnit
(class renamed from `RPUnit`; §2 canonical package move completed. `models/core.py` imports
the class locally inside `get_save_unit()` before `cast()`, so no import cycle is created;
quoted type annotations are unnecessary because `core.py` uses
`from __future__ import annotations`)
**Last Changed:** 2026-11-21
