## SWR_ELEM_00001: IRPProject Wrapper

**ID:** SWR_ELEM_00001
**Title:** IRPProject wraps IRPProject, the top-level project container
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPProject` JavaDoc interface represents the top-level Rhapsody project.
The Python wrapper extends `IRPPackage` and registers for meta class `"Project"`.
Project-owned methods use the exact pywin32 member and signature; package methods
such as `add_actor`, `add_class`, `add_node`, `find_node`, `nodes`, and `packages`
are inherited from `IRPPackage`, not duplicated on the child wrapper. Project
`save()` directly overrides `IRPUnit.save(with_subs)` because pywin32 exposes the
project overload with zero arguments.

Property-shaped APIs use `get_com_property`/`set_com_property`; method-shaped
APIs use `call_com`. `active_component`, `active_configuration`,
`all_stereotypes`, `cg_simplified_model_package`, `components`,
`default_directory_scheme`, and `profiles` are project-owned properties. The
unique-stereotype cache is write-only: JavaDoc declares only its setter and the
registered interface exposes only `prop_map_put`. The `set_active_component`
and `set_active_configuration` methods take the catalog's string `name` argument
(the pywin32 overload), and `set_wait_dialog_watchdog_value` takes a string.

`move_to_design_manager` and `move_to_design_manager_after_login` retain direct
bindings because pywin32 exposes them, although JavaDoc deprecates them and notes
Design Manager support was removed in Rhapsody 8.4. `enable_rhapsody_model_manager`,
`migrate_design_manager_links`, `set_global_configuration`,
`is_resolve_on_demand`, and `set_resolve_on_demand` are JavaDoc-defined but absent
from pywin32; their documented `NotImplementedError` stubs raise before COM
dispatch and are recorded in the stub evidence ledger.

The module uses `from __future__ import annotations`, unquoted type references,
and local imports for names used only in `cast()`. Catalog-backed methods pass
the pywin32 arity and argument types, including the zero-argument project save
and string-valued active component/configuration and wait-dialog setters.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
(class renamed from `RPProject`; canonical package move completed; project-owned
bindings match the pywin32 catalog; six package API overrides removed in favor
of inherited `IRPPackage` implementations)
**Last Changed:** 2026-11-26

## SWR_ELEM_00022: IRPProject lifecycle methods live-fixture blocker

**ID:** SWR_ELEM_00022
**Title:** close, become_active_project and remove have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`IRPProject.close()` raises a modal "Projects can only be removed from project
lists" dialog on the session-shared project, `become_active_project()` would
switch the active project out from under the shared fixture, and `remove()`
deletes the session-shared project. Their former integration tests asserted a
mocked `call_com` binding shape, which proves only the call shape and not the
live behaviour (SKILL §5). Those tests were removed; the bindings keep full
fake-COM unit coverage. Live verification needs an isolated project per case and
a session that tolerates project switching, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00024: IRPProject generate_report live-fixture blocker

**ID:** SWR_ELEM_00024
**Title:** generate_report has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
`IRPProject.generate_report()` requires a ReporterPLUS `.tpl` template file. No
`.tpl` template ships with the installed Rhapsody build (verified across the
installation, user profile, ProgramData and this workspace), and passing any
other file makes Rhapsody raise a modal "Error Opening the Template" dialog that
blocks COM automation. The former integration test passed a Python source file
as the template, which produced that modal and blocked the live suite. Per SKILL
§5 the test was removed rather than kept as a fake or exception assertion; the
binding keeps full fake-COM unit coverage. Live verification needs a valid
ReporterPLUS template, after which the row can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject.generate_report
**Last Changed:** 2026-11-25

## SWR_ELEM_00028: Project-root class/actor/node creation live-fixture blocker

**ID:** SWR_ELEM_00028
**Title:** inherited package creation methods fault on the project root
**Status:** Blocked
**Priority:** Low
**Description:**
`add_actor`, `add_class`, `add_node`, `find_node`, `nodes`, and `packages` are
inherited from `IRPPackage`; `IRPProject` has no duplicate child overrides. The
Rhapsody build rejects `addClass(name)`, `addActor(name)`, and `addNode(name)` on
the project root with HRESULT `0x80040006`; a node created in a nested package is
not returned by the project-root `nodes` collection. Package-level collection
coverage is in `test_irp_package.py`; populated project-root coverage remains
blocked until a build/API fixture supports these relationships.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-26

## SWR_ELEM_00029: IRPProject active component/configuration live-fixture blocker

**ID:** SWR_ELEM_00029
**Title:** active component and configuration access have no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
The getters and setters are catalog-backed. The setters now use the pywin32
string signatures (`setActiveComponent(name)` and
`setActiveConfiguration(name)`), rather than JavaDoc's unexposed object
overloads. This Rhapsody build still faults on getter/setter calls with HRESULT
`0x80040005`/`0x80040006`, including valid names; no populated getter or safe
round-trip fixture is available. The bindings have fake-COM coverage and the
live blocker stays open until a build permits successful reads and switching.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-26

## SWR_ELEM_00030: IRPProject gateway and explicit-object live-fixture blocker

**ID:** SWR_ELEM_00030
**Title:** gateway exports and setObjectExplicit/Implicit have no live proof
**Status:** Blocked
**Priority:** Low
**Description:**
`GatewayExportToXML`/`GatewayExportToXML2` are documented as internal-use-only
and fail with `E_FAIL` even with a real output path. `setObjectExplicit` and
`setObjectImplicit` reject a real model element with `E_FAIL`/typemismatch.
Their integration tests were removed per SKILL §5; the bindings keep full
fake-COM unit coverage. Live verification needs the gateway feature and the
correct instance fixture, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-25

## SWR_ELEM_00031: Write-only UseUniqueStereotypeAndRefCache property

**ID:** SWR_ELEM_00031
**Title:** The cache setting follows the pywin32 write-only property contract
**Status:** Implemented
**Priority:** Low
**Description:**
JavaDoc declares only `setUseUniqueStereotypeAndRefCache(int)` and pywin32
exposes `UseUniqueStereotypeAndRefCache` through `prop_map_put`, not
`prop_map_get`. The Python property therefore has a setter and no getter. The
live setter is exercised by `test_use_unique_stereotype_and_ref_cache_setter_returns_none`
and restores the original value after the case; a nonexistent getter is not
part of the API.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject.use_unique_stereotype_and_ref_cache
**Last Changed:** 2026-11-26

## SWR_ELEM_00039: Simplified-model package getter has no populated fixture

**ID:** SWR_ELEM_00039
**Title:** cg_simplified_model_package has no documented way to establish a live value
**Status:** Blocked
**Priority:** Low
**Description:**
The live project returns `None` from `cg_simplified_model_package`; JavaDoc and
pywin32 expose no setter or factory that associates a simplified-model package
with the project. The integration case records only the observed empty state,
so the getter matrix remains WEAK until an authentic populated project fixture
is available.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject.cg_simplified_model_package
**Last Changed:** 2026-11-26

## SWR_ELEM_00040: Deprecated Design Manager project methods lack live fixture

**ID:** SWR_ELEM_00040
**Title:** move_to_design_manager bindings are exposed but cannot be verified live
**Status:** Blocked
**Priority:** Low
**Description:**
`move_to_design_manager` and `move_to_design_manager_after_login` forward to the
exact pywin32 methods and have fake-COM unit tests. JavaDoc marks both deprecated
because Design Manager support was removed in Rhapsody 8.4; no supported server
fixture is available for live execution. Keep the bindings and leave integration
verification open rather than asserting the expected COM failure.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:IRPProject
**Last Changed:** 2026-11-26
