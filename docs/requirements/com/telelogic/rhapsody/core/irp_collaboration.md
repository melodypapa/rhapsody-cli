## SWR_ELEM_00050: IRPCollaboration Wrapper

**ID:** SWR_ELEM_00050
**Title:** IRPCollaboration exposes collaboration state through pywin32 properties and methods
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPCollaboration` JavaDoc interface represents a collaboration in a
Rhapsody model. The Python `IRPCollaboration` shall extend `IRPUnit` and expose
the collaboration's activation condition/mode, associations, classifier,
execution occurrences, interaction occurrences/operators, message points,
messages and mode through the pywin32 catalog.

Ten JavaDoc getter-only members are exposed by pywin32 as read-only COM
properties and are surfaced as `@property` members; all other supported
members remain method-shaped `call_com` bindings. The module uses
`from __future__ import annotations` with unquoted type references.

Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper (43 tests; 104 statements, 6 branches).
Integration tests in the mirrored path create real collaborations and messages;
only `messages` could be populated through a documented API, so the other nine
read-only getters have documented empty/default-state tests and P0 blockers in
`docs/reports/sync-todo/index.md`. Live assertions are CI-only on Windows and
are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py:IRPCollaboration
**Last Changed:** 2026-11-27
