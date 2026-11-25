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
method-shaped and use `call_com`. `get_root_instance_specifications` is a blocker
because `getRootInstanceSpecifications` is absent from the catalog and its legacy
dual-binding site is left unchanged pending Windows typelib evidence. Several
JavaDoc names differ from the Python surface (`add_statechart_diagram`,
`get_nested_packages`, `recalculate_events_base_id`, `get_saved_in_separate_directory`
and its setter); these are documented aliases, not code changes. The module uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py:IRPPackage
(class renamed from `RPPackage`; §2 canonical package move completed; 35 legacy
dual-binding sites migrated; 1 catalog-absent site left unchanged)
**Last Changed:** 2026-11-22

## SWR_ELEM_00034: IRPPackage link mutators live-fixture blocker

**ID:** SWR_ELEM_00034
**Title:** add_link and link getters have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`addLink` between real objects or SysML ports fails with `E_FAIL` in this
Rhapsody build, which also blocks the `get_links` populated-getter fixture. This
matches the previously recorded `add_link_to_element` `E_FAIL` blocker. The
integration tests were removed per SKILL §5; the bindings keep full fake-COM
unit coverage. Live verification needs a build that accepts link creation,
after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py:IRPPackage
**Last Changed:** 2026-11-25
