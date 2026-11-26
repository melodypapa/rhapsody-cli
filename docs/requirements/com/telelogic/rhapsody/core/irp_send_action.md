## SWR_ELEM_00043: IRPSendAction Wrapper

**ID:** SWR_ELEM_00043
**Title:** IRPSendAction exposes event, target, invoked operation, and argument values through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPSendAction` JavaDoc interface represents Send Action elements in an
activity or statechart. The Python `IRPSendAction` shall extend `IRPAction`,
register itself for meta class `"SendAction"`, and expose the event it sends,
its target, the invoked interface item, and its argument values.

Pywin32 exposes the JavaDoc accessors as four COM properties (`argVals`,
`event`, `invokedOperation`, `target`), so the Python surface uses
``@property`` accessors; `event`, `invokedOperation`, and `target` also have
setters using `set_com_property`. `add_argument_value` is method-shaped and
calls `addArgumentValue` through `call_com`. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_send_action.py`; the
class was split out of the shared `irp_actions.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create a real state's send action and assert populated getter
values by identity/membership, deleting the owning package during cleanup.
Live assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_send_action.py:IRPSendAction
**Last Changed:** 2026-11-26
