## SWR_ELEM_00019: IRPPort Wrapper

**ID:** SWR_ELEM_00019
**Title:** IRPPort wraps IRPPort, a port on a classifier
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPPort` JavaDoc interface represents a port on a classifier. The Python
`IRPPort` shall extend `IRPInstance` and expose Java-mirrored members for behavioral
and reversed state (`is_behavioral`, `is_reversed`), the port contract
(`port_contract`), and provided/required interfaces
(`provided_interfaces`/`add_provided_interface`/`remove_provided_interface`,
`required_interfaces`/`add_required_interface`/`remove_required_interface`).
The deprecated `get_contract`/`set_contract` aliases are retained for compatibility.
The wrapper registers itself for meta class `"Port"`.
Every catalog-backed COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: `isBehavioral`, `isReversed`, `portContract`,
`providedInterfaces`, and `requiredInterfaces` are properties exposed as Python
`@property` accessors (with setters for the writable members) read/written with
`get_com_property`/`set_com_property`. `get_contract`/`set_contract` are deprecated
aliases of the same underlying data: their legacy probe sites (getContract/contract were
absent from every pywin32 catalog) were migrated in the 2026-11-22 review fix to read/write
the exposed `portContract` property directly.
The module uses `from __future__ import annotations` with unquoted type references.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py:IRPPort
(class renamed from `RPPort`; §2 canonical package move completed; 8 legacy call
sites migrated; 2 catalog-absent sites left unchanged). Incoming generic dispatches
are now cast by `IRPInstance.__init__` to the exact `IRPPort` interface; this resolves
the live `isBehavioral` and `providedInterfaces` dispatch failures.
**Last Changed:** 2026-03-19

## SWR_ELEM_00027: IRPPort interface mutators live-fixture blocker

**ID:** SWR_ELEM_00027
**Title:** provided/required interface mutators have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`addProvidedInterface`, `removeProvidedInterface`, `addRequiredInterface` and
`removeRequiredInterface` are exposed by pywin32 but this Rhapsody build rejects
every write with `E_FAIL`, for Class and Interface arguments alike. The generic
dispatch issue is resolved by the class-local cast in `IRPInstance.__init__`; the
port property tests now pass live. The collection getters still expose only empty
collections because the mutators cannot populate them. The central P0 row and
issue #202 retain this live deviation; a build that accepts the mutators is needed
to verify populated membership and close the remaining rows.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py:IRPPort
**Last Changed:** 2026-03-19
