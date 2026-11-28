## SWR_ELEM_00056: IRPActionBlock Wrapper

**ID:** SWR_ELEM_00056
**Title:** IRPActionBlock inherits its sequence-message API from IRPMessage
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPActionBlock` JavaDoc interface represents action blocks in sequence
diagrams. The Python wrapper shall extend `IRPMessage` and register for the
COM meta class `"ActionBlock"`.

`IRPActionBlock` declares no JavaDoc-owned methods or properties. Its public API
is inherited from `IRPMessage`; the Python wrapper must not duplicate those
bindings. The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_action_block.py`.
Mirrored fake-COM unit tests verify message inheritance and meta-class
registration. No child-specific integration assertion is added: there are no
owned members to exercise, and the integration-test scope rules prohibit
retesting inherited `IRPMessage` behavior in this child class's file.

**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_action_block.py:IRPActionBlock`
**Last Changed:** 2026-11-26
