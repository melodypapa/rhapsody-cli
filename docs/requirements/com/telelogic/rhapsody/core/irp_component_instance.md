## SWR_ELEM_00053: IRPComponentInstance Wrapper

**ID:** SWR_ELEM_00053
**Title:** IRPComponentInstance exposes component type and owning node through pywin32 properties
**Status:** Implemented
**Priority:** Low
**Description:**
The `IRPComponentInstance` JavaDoc interface represents a component instance
extending `IRPInstance`. The Python wrapper shall expose the component type and
the node containing the instance.

Pywin32 exposes `getComponentType` / `setComponentType` as a read/write
`componentType` property and `getNode` as a read-only `node` property; the
wrapper surfaces both as `@property` members. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.

Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
path create real nodes and component instances, assert populated getter values
by identity, and delete the owning package during cleanup. Live assertions are
CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component_instance.py:IRPComponentInstance
**Last Changed:** 2026-11-27
