## SWR_ELEM_00002: IRPPackage Wrapper

**ID:** SWR_ELEM_00002
**Title:** IRPPackage wraps IRPPackage, a container for classes, actors, and other elements
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPPackage` JavaDoc interface represents a package containing model elements.
The Python `IRPPackage` shall extend `IRPUnit` and expose Java-mirrored creation
methods (`add_class`, `add_nested_package`, `add_actor`, `add_use_case`,
`add_global_function`, and the diagram `add_*` methods), finders (`find_class`,
`find_actor`, `find_use_case`, etc.), and collection getters for nested classifiers,
diagrams, nodes, modules, types, global functions/objects/variables, events, flows,
and links. The wrapper registers itself for meta class `"Package"`.
Every catalog-backed COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: most getters are pywin32 **properties** and
are read with `get_com_property`; `getRemoteRequirementsPopulateMode`,
`setRemoteRequirementsPopulateMode`, `getAllNestedElements`, and `getNamespace` are
method-shaped and use `call_com`. The remote-requirements mode getter is a
P0 live blocker: JavaDoc permits `"All"`, `"Linked"`, or `"None"`, but a local
probe after setting `"None"` returned an empty string because no Design Manager
server is configured. `get_root_instance_specifications` raises `NotImplementedError` before COM
dispatch because `getRootInstanceSpecifications` is absent from the catalog and
is listed in `documented_unavailable`. Live getter tests use the JavaDoc-backed
`IRPModelElement.add_new_aggr` factory to create package-owned components,
instance specifications, source artifacts, and user-defined stereotypes.
Package link retrieval is positively tested by creating class instances through
`addGlobalObject`, wrapping them as `IRPInstance`, and calling `IRPPackage.add_link`
with a real association relation; the SysML-port link variant is also live-tested
with `SysMLPort` children created on the classes. Several
JavaDoc names differ from the Python surface (`add_statechart_diagram`,
`get_nested_packages`, `recalculate_events_base_id`, `get_saved_in_separate_directory`
and its setter); these are documented aliases, not code changes. The
`IRPPackage` inherits `IRPModelElement.add_association` directly. Its
JavaDoc contract supports package and class containers and returns an
`IRPAssociationClass`; the child wrapper adds no duplicate COM binding or
return-type override. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py:IRPPackage
(class renamed from `RPPackage`; §2 canonical package move completed; owned
bindings use direct catalog members or documented pre-dispatch stubs)
**Last Changed:** 2026-11-26

## SWR_ELEM_00034: IRPPackage link creation and retrieval

**ID:** SWR_ELEM_00034
**Title:** Package links can be created through the documented add_link API and retrieved
**Status:** Implemented
**Priority:** Low
**Description:**
`IRPPackage.add_link` and the `links` getter have populated live integration proof.
`test_get_links_returns_link_created_with_add_link` creates two classes and their
instances through the documented package APIs, creates an association relation,
wraps the real COM instances as `IRPInstance`, calls `add_link`, and asserts the
returned link is present in `package.links`; cleanup deletes the test package.
`test_add_link_between_sysml_ports_returns_link_in_package` also verifies the
SysML-port variant with real objects and ports created through the documented
`addNewAggr` factory. The generic `addNewAggr("Link", name)` path still faults
on packages, but is unnecessary for these supported package link APIs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py:IRPPackage
**Last Changed:** 2026-11-26
