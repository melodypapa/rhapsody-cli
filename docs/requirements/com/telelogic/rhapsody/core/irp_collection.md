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
`add_graphical_item` (Java `addGraphicalItem`) is bound to the pywin32-exposed
`addGraphicalElementItem` alias (one COM-object argument, recorded in `documented_aliases`).
A live probe on 2026-11-25 with a real `IRPGraphElement` from an object-model diagram
confirmed the call succeeds and increments `count`; a non-graph model element faults with
COM `Type mismatch`. `set_string`'s `value` is annotated `object` to match the catalog's
VT_BYREF|VT_BSTR parameter. Negative indices are rejected locally by `__getitem__`
(unit-tested); the integration suite asserts real collection outcomes. `to_list` remains a
documented-unavailable `NotImplementedError` stub (no pywin32 member).
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py:IRPCollection
(canonical package)
**Last Changed:** 2026-11-25

## SWR_ELEM_00036: IRPCollection graphical-item COM alias live evidence

**ID:** SWR_ELEM_00036
**Title:** addGraphicalItem is exposed live as addGraphicalElementItem and works
**Status:** Closed — migrated
**Priority:** Low
**Description:**
JavaDoc declares `IRPCollection.addGraphicalItem(IRPGraphElement)`; the pywin32 catalog
exposes `addGraphicalElementItem` (one COM-object argument) instead. The earlier decision
kept a `NotImplementedError` stub because that catalog member's arity was unverified. On
2026-11-25 a fresh hidden-UI Rhapsody instance was used to probe it directly:

| Call | Result |
| --- | --- |
| `addGraphicalElementItem(real_graph_com)` where the argument came from an object-model diagram text box | success, collection `count` 0 -> 1 |
| the same call with a class or project COM object | `com_error(-2147352571, 'Type mismatch.', ...)` |

`add_graphical_item` is now bound to `addGraphicalElementItem`; the Java/COM name pair is
recorded in `documented_aliases`, and `scripts/validate_model_api.py` canonicalizes the
pair so the generated report shows MATCH instead of stacked `JAVA_DOC_MISSING` /
`JAVA_ONLY_MEMBER` findings. The integration fixture obtains the real graph element via
`IRPDiagram.add_text_box`, whose binding was corrected from the Java-style `addTextBox`
to the pywin32-exposed `AddTextBox`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py:IRPCollection.add_graphical_item
**Last Changed:** 2026-11-27
