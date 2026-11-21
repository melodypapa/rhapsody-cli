## SWR_ELEM_00014: IRPModelElement Wrapper

**ID:** SWR_ELEM_00014
**Title:** IRPModelElement wraps IRPModelElement, the base interface of all model elements
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPModelElement` interface is the base interface of all Rhapsody model elements. The
Python `IRPModelElement` shall extend `AbstractRPModelElement` and expose the inherited
Java-mirrored members (`get_name`, `get_guid`, `get_owner`, `get_description`, collections,
template members, ...). Every COM call shall target exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json` with no runtime name probing: method-shaped members
(`getDecorationStyle`, `getFullPathName`, `isATemplate`, `isModified`, `setDecorationStyle`,
...) are invoked via `call_com`, and property-shaped members (`name`, `GUID`, `metaClass`,
`description`, `BinaryID`, ...) are read/written via `get_com_property`/`set_com_property`.
`AbstractRPModelElement.wrap()` shall resolve the wrapper class from the `metaClass`
property. `get_rmm_url` is a documented blocker: the `getRmmUrl`/`rmmUrl` members are absent
from the committed pywin32 catalog (see `documented_unavailable` for IRPClass), so its legacy
dual-binding call site stays unchanged until Windows typelib evidence lands.
**Implementation:** src/rhapsody_cli/models/core.py:IRPModelElement (§2 canonical package move
deferred until the IRPCollection and IRPUnit rows leave `models/core.py` — see
`docs/reports/sync-todo`)
**Last Changed:** 2026-11-21
