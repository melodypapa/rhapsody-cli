## SWR_ELEM_00049: IRPComponent Wrapper

**ID:** SWR_ELEM_00049
**Title:** IRPComponent exposes component configuration, files, scope, and build settings through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPComponent` JavaDoc interface represents a component extending
`IRPUnit`. The Python `IRPComponent` shall expose the component's build
settings, configurations, files, nested components, scope elements and
diagrams through bindings that exactly match the pywin32 catalog.

Twelve JavaDoc accessor pairs are exposed by pywin32 as COM properties and are
surfaced as `@property` members (with setters where JavaDoc defines a setter);
all other supported members use `call_com` with the exact camelCase catalog
member. `get_path`, `set_path` and `update_contained_diagrams_on_server` are
JavaDoc-declared but absent from the catalog, so they are documented
pre-dispatch `NotImplementedError` stubs with entries in the stub evidence
ledger. The module uses `from __future__ import annotations` with unquoted type
references and local imports for names used only in `cast()`.

Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper (42 tests; 110 statements, 0 branches).
Integration tests in the mirrored path create real components, configurations,
files, nested components and scope elements and assert populated getter values
by identity/value, deleting the owning package during cleanup. `panel_diagrams`
and `variation_points` have no documented API that attaches a child, so their
empty states are recorded as P0 blockers. Live assertions are CI-only on
Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py:IRPComponent
**Last Changed:** 2026-11-27
