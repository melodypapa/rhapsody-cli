## SWR_ELEM_00040: IRPDependency Wrapper

**ID:** SWR_ELEM_00040
**Title:** IRPDependency wraps a dependency relationship between model elements
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPDependency` interface represents a dependency relationship and extends `IRPModelElement`. The Python wrapper shall register for the meta class `"Dependency"` and expose `dependent` and `depends_on` as read/write Python properties backed by the typelib properties `dependent` and `dependsOn`. `set_owner_without_changing_dependent` shall bind exactly one pywin32 method. `is_need_to_migrate` and `set_link_type` are JavaDoc-only and raise `NotImplementedError` before any COM dispatch, because neither member is present in the registered IRPDependency typelib.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_dependency.py:IRPDependency` (canonical package; registration retained; legacy `_get_method_or_property` helpers removed; exchange exporter and importer use the properties).
**Last Changed:** 2026-11-26
