## SWR_CORE_00002: IRPPackage Wrapper

**ID:** SWR_CORE_00002
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
