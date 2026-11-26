## SWR_ELEM_00053: IRPComment Wrapper

**ID:** SWR_ELEM_00053
**Title:** IRPComment is an inheritance-only wrapper registered for the Comment meta class
**Status:** Implemented
**Priority:** Low
**Description:**
The `IRPComment` JavaDoc interface represents a free-text comment element. It
declares no owned members; all behavior is inherited from `IRPModelElement`.
The Python `IRPComment` shall extend `IRPModelElement`, register itself for meta
class `"Comment"`, and add no duplicate COM bindings.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_comment.py`; the class
was split out of the shared `irp_misc.py` module in its own sync run. With this
split the empty `irp_misc.py` shim and its mirrored unit test were removed.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper, asserting the wrapper shape and
registration. The mirrored integration test creates a real comment through the
documented generic aggregation factory and asserts it wraps as `IRPComment`;
the owning package is deleted during cleanup. Since the interface owns no
members, this is a registration/navigation check rather than owned-behavior
coverage. Live assertions are CI-only on Windows and are unverified in offline
runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_comment.py:IRPComment
**Last Changed:** 2026-11-27
