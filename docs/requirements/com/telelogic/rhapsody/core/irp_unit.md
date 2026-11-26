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
(`filename`, `get_unit_path`, `set_unit_path`, `current_directory`,
`cm_header`, `get_last_modified_time`), CM/configuration state
(`get_cm_state`, `get_add_to_model_mode`, `include_in_next_load`,
`is_stub`, `is_read_only`/`set_read_only`,
`is_reference_unit`, `is_separate_save_unit`/`set_separate_save_unit`), language
(`get_language`, `set_language`) and collections (`get_nested_save_units`,
`get_nested_save_units_count`, `structure_diagrams`). `set_read_only` shall translate
Python booleans to the COM-style integers 1/0. `AddToModelMode` is an `IntEnum` mirroring
`IRPApplication.AddToModel_Mode` so raw COM integers compare directly.

Every COM call shall target exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`, with no runtime name probing or Java-name fallback:
method-shaped members (`getAddToModelMode`, `getCMState`, `getLanguage`,
`getLastModifiedTime`, `getNestedSaveUnits`, `getNestedSaveUnitsCount`, `isReadOnly`,
`isReferenceUnit`, `isSeparateSaveUnit`, `load`, `save`, `setLanguage`, `setReadOnly`,
`setSeparateSaveUnit`, `setUnitPath`, `unload`, ...) are invoked via `call_com`, and
property-shaped members (`CMHeader`, `currentDirectory`, `filename`, `includeInNextLoad`,
`isStub`, `structureDiagrams`) are exposed as Python `@property` accessors (with a
setter for the writable members) read/written via `get_com_property`/`set_com_property`.
The two collection getters wrap the result in `IRPCollection`. `get_unit_path` is a
documented-unavailable `NotImplementedError` stub: the catalog exposes only `setUnitPath`,
and a live probe on 2026-11-25 against a fresh hidden-UI Rhapsody instance found no
`getUnitPath`-like COM member on a real package (`dir()` listed only `setUnitPath` among
path/unit members), so the wrapper raises before COM dispatch rather than probing. The module uses
`from __future__ import annotations` with unquoted type references; names used only in
`cast()` are imported locally inside the method to avoid circular imports.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py:IRPUnit
(class renamed from `RPUnit`; §2 canonical package move completed. `models/core.py` imports
the class locally inside `get_save_unit()` before `cast()`, so no import cycle is created;
quoted type annotations are unnecessary because `core.py` uses
`from __future__ import annotations`)

## SWR_CORE_00012: IRPUnit path/getter live evidence

**ID:** SWR_CORE_00012
**Title:** getUnitPath absence confirmed live; collection getters have populated fixtures
**Status:** Implemented
**Priority:** Low
**Description:**
A live probe on 2026-11-25 against a fresh hidden-UI Rhapsody instance listed the
COM path/unit members on a real package: `getFullPathName`, `getFullPathNameIn`,
`getNestedSaveUnits`, `getNestedSaveUnitsCount`, `getSaveUnit`, `isReferenceUnit`,
`isSeparateSaveUnit`, `setSeparateSaveUnit` and `setUnitPath`. No `getUnitPath`-like
getter exists, confirming the `documented_unavailable` decision behind the
`NotImplementedError` stub.

Populated getter fixtures were proven live too: `add_new_aggr("StructureDiagram", name)`
on a class makes the diagram appear in `structure_diagrams`, and a nested package with
`set_separate_save_unit(1)` plus `save()` appears in `get_nested_save_units()`. The
integration tests assert those identities rather than empty-state/count-only results.
**Implementation:** tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py
**Last Changed:** 2026-11-25
