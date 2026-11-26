## SWR_ELEM_00047: IRPContextSpecification Wrapper

**ID:** SWR_ELEM_00047
**Title:** IRPContextSpecification exposes path and multiplicity collections through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPContextSpecification` JavaDoc interface represents the exact context
of an object in a hierarchy: a collection of strings giving the full path to
the element and a collection of indices disambiguating multiplicities. The
Python `IRPContextSpecification` shall extend `IRPValueSpecification`, register
itself for meta class `"ContextSpecification"`, and expose both collections.

Pywin32 exposes the JavaDoc `getMultiplicities` / `setMultiplicities` and
`getValue` / `setValue` pairs as two read/write properties, so the wrapper
reads them with `get_com_property` and writes them with `set_com_property`.
The module uses `from __future__ import annotations` with unquoted type
references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_context_specification.py`;
the class was split out of the shared `irp_actions.py` module in its own sync
run. Unit tests in the mirrored unit path use only fake COM objects and give
100% statement/branch coverage of the wrapper. Integration tests in the
mirrored integration path create a real context specification, write string
collections through the documented application collection API, and assert the
getter values; the owning package is deleted during cleanup. Live assertions
are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_context_specification.py:IRPContextSpecification
**Last Changed:** 2026-11-26
