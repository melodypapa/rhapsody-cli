## SWR_ELEM_00015: IRPCollection Wrapper

**ID:** SWR_ELEM_00015
**Title:** IRPCollection wraps IRPCollection, the generic element collection
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPCollection` interface is Rhapsody's generic element collection. The Python
`IRPCollection` shall expose 1-based indexed access (`count`, `get_item`, iteration, and
`__getitem__`) and the mutators (`add_item`, `set_size`, `remove`, `set_string`,
`set_integer`, `set_model_element`, `empty`). Every COM call shall target exactly one
pywin32-exposed member from `docs/reports/pywin32_authority.json` with no runtime name
probing: `Count` is a property read via `get_com_property`, `Item` is a method invoked via
`call_com` (the legacy `getItem` name-probe in `get_item` was removed), and the mutators are
invoked as methods via `call_com`. Elements returned by `get_item` are wrapped through
`AbstractRPModelElement._wrap_if_element`.
`add_graphical_item` (Java `addGraphicalItem`) is a documented-unavailable
`NotImplementedError` stub (the catalog exposes `addGraphicalElementItem`, whose arity is
unverified — do not migrate blind); `to_list` is a Python-side helper with no COM member.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py:IRPCollection
(canonical package)
**Last Changed:** 2026-11-24
