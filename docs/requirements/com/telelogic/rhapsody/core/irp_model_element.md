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
`meta_class` property. `create_oslc_link`/`delete_oslc_link` dispatch to the pywin32
`createOSLCLink`/`deleteOSLCLink` methods. `get_rmm_url` is a documented blocker: the `getRmmUrl`/`rmmUrl` members
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
**Last Changed:** 2026-11-25

## SWR_ELEM_00023: IRPModelElement GUI-dialog methods live-fixture blocker

**ID:** SWR_ELEM_00023
**Title:** high_light_element and open_features_dialog have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`IRPModelElement.high_light_element()` opens a modal GUI window and
`open_features_dialog()` opens a modal "Features" window, both of which block
COM automation for the rest of the session. Their former integration tests
asserted a mocked `call_com` binding shape, which proves only the call shape and
not the live behaviour (SKILL §5). Those tests were removed; the bindings keep
full fake-COM unit coverage. Live verification needs a session that can drive or
dismiss those dialogs, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py:IRPModelElement
**Last Changed:** 2026-11-25

## SWR_ELEM_00033: IRPModelElement OSLC link roundtrip live-fixture blocker

**ID:** SWR_ELEM_00033
**Title:** OSLC link create/delete has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`createOSLCLink`/`deleteOSLCLink` dispatch to pywin32-exposed members, but a
round trip against a real element fails with `E_FAIL` in this Rhapsody build.
The integration test was removed per SKILL §5; the bindings keep full fake-COM
unit coverage. Live verification needs an OSLC-enabled server configuration,
after which the row can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py:IRPModelElement
**Last Changed:** 2026-11-25
