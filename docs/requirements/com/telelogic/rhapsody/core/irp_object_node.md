## SWR_ELEM_00045: IRPObjectNode Wrapper

**ID:** SWR_ELEM_00045
**Title:** IRPObjectNode exposes In State states and represented type through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPObjectNode` JavaDoc interface represents Object Node elements in
activity diagrams. The Python `IRPObjectNode` shall extend `IRPState`, register
itself for meta class `"ObjectNode"`, and expose the node's "In State" states
and represented class/type.

Pywin32 exposes `inState`, `inStateList`, and `represents` as properties; they
are read with `get_com_property` and the two writable ones also use
`set_com_property`. `add_in_state` and `remove_in_state` are method-shaped and
call their exact camelCase COM members through `call_com`. The deprecated
JavaDoc `getInState` / `setInState` pair maps to the `inState` property, with
the JavaDoc warning preserved in the docstrings. The module uses
`from __future__ import annotations` with unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_object_node.py`; the
class was split out of the shared `irp_activity.py` module in its own sync run.
With this split the empty `irp_activity.py` shim and its mirrored unit test
were removed. Unit tests in the mirrored unit path use only fake COM objects
and give 100% statement/branch coverage of the wrapper. Integration tests in
the mirrored path create real activity nodes; `add_in_state` and
`remove_in_state` bind the object node to a represented class and use a state
from that class's statechart. They assert membership changes and delete the
owning package during cleanup. The focused Windows live run passes all four
integration tests; offline runs provide collection only.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_object_node.py:IRPObjectNode
**Last Changed:** 2026-03-19
