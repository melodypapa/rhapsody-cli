## SWR_ELEM_00019: IRPPort Wrapper

**ID:** SWR_ELEM_00019
**Title:** IRPPort wraps IRPPort, a port on a classifier
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPPort` JavaDoc interface represents a port on a classifier. The Python
`IRPPort` shall extend `RPInstance` and expose Java-mirrored members for behavioral
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
sites migrated; 2 catalog-absent sites left unchanged)
**Last Changed:** 2026-11-24

## SWR_ELEM_00027: IRPPort interface mutators live-fixture blocker

**ID:** SWR_ELEM_00027
**Title:** provided/required interface mutators have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`addProvidedInterface`, `removeProvidedInterface`, `addRequiredInterface` and
`removeRequiredInterface` are exposed by pywin32 but this Rhapsody build rejects
every write with `E_FAIL`, for Class and Interface arguments alike. The former
integration test asserted those failures indirectly; per SKILL §5 the assertions
were removed and the rows recorded as blocked, while the collection getters keep
their live smoke assertions and the bindings keep full fake-COM unit coverage.
Live verification needs a build that accepts the mutators, after which the rows
can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py:IRPPort
**Last Changed:** 2026-11-25
