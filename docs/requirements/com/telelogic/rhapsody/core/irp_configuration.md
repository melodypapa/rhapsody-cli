## SWR_ELEM_00051: IRPConfiguration Wrapper

**ID:** SWR_ELEM_00051
**Title:** IRPConfiguration exposes configuration build settings through the pywin32 catalog
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPConfiguration` JavaDoc interface represents a component configuration.
The Python `IRPConfiguration` shall extend `IRPUnit` and expose build settings,
instrumentation scope, initial instances and related state through bindings
that exactly match the pywin32 catalog.

Sixteen JavaDoc accessor pairs are exposed by pywin32 as COM properties and are
surfaced as `@property` members (with setters where JavaDoc defines a setter);
remaining supported members use `call_com` with the catalog's exact camelCase
member. `get_path` and `set_path` are JavaDoc-declared but absent from the
catalog, so they are documented pre-dispatch `NotImplementedError` stubs with
entries in the stub evidence ledger. The module uses
`from __future__ import annotations` with unquoted type references.

Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper (48 tests; 129 statements, 0 branches).
Integration tests in the mirrored path create real configurations and assert
documented empty/default values; populated fixtures for the read-only properties
are P0 blockers in `docs/reports/sync-todo/index.md`. Live assertions are
CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py:IRPConfiguration
**Last Changed:** 2026-11-27
