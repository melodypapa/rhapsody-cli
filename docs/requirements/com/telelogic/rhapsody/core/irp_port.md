## SWR_CORE_00009: IRPPort Wrapper

**ID:** SWR_CORE_00009
**Title:** IRPPort wraps IRPPort, a port on a classifier
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPPort` JavaDoc interface represents a port on a classifier. The Python
`IRPPort` shall extend `RPInstance` and expose Java-mirrored members for behavioral
and reversed state (`get_is_behavioral`/`set_is_behavioral`,
`get_is_reversed`/`set_is_reversed`), the port contract
(`get_port_contract`/`set_port_contract`), and provided/required interfaces
(`get_provided_interfaces`/`add_provided_interface`/`remove_provided_interface`,
`get_required_interfaces`/`add_required_interface`/`remove_required_interface`).
The deprecated `get_contract`/`set_contract` aliases are retained for compatibility.
The wrapper registers itself for meta class `"Port"`.
Every catalog-backed COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: `isBehavioral`, `isReversed`, `portContract`,
`providedInterfaces`, and `requiredInterfaces` are properties read/written with
`get_com_property`/`set_com_property`. `get_contract`/`set_contract` are blockers:
`getContract`/`setContract`/`contract` are absent from every pywin32 catalog, so
their legacy dual-binding sites are left unchanged pending Windows typelib evidence.
The module uses `from __future__ import annotations` with unquoted type references.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py:IRPPort
(class renamed from `RPPort`; §2 canonical package move completed; 8 legacy call
sites migrated; 2 catalog-absent sites left unchanged)
**Last Changed:** 2026-11-22
