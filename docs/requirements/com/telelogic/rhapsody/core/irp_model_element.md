## SWR_ELEM_00014: IRPModelElement Wrapper

**ID:** SWR_ELEM_00014
**Title:** IRPModelElement wraps IRPModelElement, the base interface of all model elements
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPModelElement` interface is the base interface of all Rhapsody model elements. The
Python `IRPModelElement` shall extend `ComHelper` and expose the inherited Java-mirrored
members following the pywin32 shape: COM-property members (`name`, `meta_class`, `guid`,
`description`, `description_html`, `display_name`, `binary_id`, `owner`, `project`,
`main_diagram`, `of_template`, `ti`, `stereotype`, `stereotypes`, `all_tags`, `local_tags`,
`references`, `constraints`, `is_external`, ...) are exposed as Python properties with
`@<name>.setter` only where pywin32 exposes the writable property; method-shaped members
(`getDecorationStyle`, `getFullPathName`, `isATemplate`, `isModified`, `setPropertyValue`,
...) are invoked via `call_com`. `get_error_message` passes the pywin32-required MIDL output
buffer (`_midl__irp_model_element0002_: str`). `add_link_to_element` accepts `None` for the
two port arguments when the link represents an association (per JavaDoc). The deprecated
single-stereotype access is exposed as the read/write `stereotype` property. Every COM call
targets exactly one pywin32-exposed member from `docs/reports/pywin32_authority.json` with no
runtime name probing. `AbstractRPModelElement.wrap()` resolves the wrapper class from the
`meta_class` property. `get_rmm_url` is a documented blocker: the `getRmmUrl`/`rmmUrl` members
are absent from the committed pywin32 catalog (see `documented_unavailable` for
IRPModelElement), so it raises `NotImplementedError` before any COM dispatch. By the user's
explicit decision on 2026-11-24, `constraints_by_him` and `hyper_links` also raise
`NotImplementedError` before COM dispatch, despite their pywin32 properties being present:
`constraints_by_him` is documented as internal-only, and the live hyperlink setup attempts
could not produce retrievable data. These are intentional runtime deviations recorded in the
finished-class remediation ledger. The module uses
`from __future__ import annotations` with unquoted type references; names used only in
`cast()` are imported locally inside the method to avoid circular imports.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py
**Last Changed:** 2026-11-24
