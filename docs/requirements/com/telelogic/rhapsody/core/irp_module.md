## SWR_ELEM_00041: IRPModule Wrapper

**ID:** SWR_ELEM_00041
**Title:** IRPModule wraps a module element that extends IRPInstance
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPModule` interface extends `IRPInstance` and declares no members of its own. The Python wrapper shall extend `IRPInstance` and register for the meta class `"Module"`, so that a module returned by `IRPPackage.add_module` is wrapped as `IRPModule`. All members are inherited from `IRPInstance`, `IRPRelation`, `IRPUnit`, and `IRPModelElement` and are owned by those wrappers.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_module.py:IRPModule` (canonical package; registration retained; no own members).
**Last Changed:** 2026-11-26
