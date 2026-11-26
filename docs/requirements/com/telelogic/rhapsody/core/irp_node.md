## SWR_ELEM_00052: IRPNode Wrapper

**ID:** SWR_ELEM_00052
**Title:** IRPNode exposes CPU type and component instances through pywin32 properties
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPNode` JavaDoc interface represents a node extending `IRPUnit`. The
Python `IRPNode` shall expose the node's CPU type and component instances.

Pywin32 exposes `getCPUtype` / `setCPUtype` as a read/write `CPUtype` property
and `getComponentInstances` as a read-only `componentInstances` property; the
wrapper surfaces both as `@property` members. Component-instance creation,
deletion and lookup remain method-shaped `call_com` bindings. The module uses
`from __future__ import annotations` with unquoted type references.

Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
path create real nodes and component instances through `IRPPackage.add_node`
and `IRPNode.add_component_instance`, assert populated getter values, and
delete the owning package during cleanup. Live assertions are CI-only on
Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_node.py:IRPNode
**Last Changed:** 2026-11-27
