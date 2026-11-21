# Sync todo: `docs/reports` — `Group-unfinished-1` (IRPClass → IRPUseCase)

Baseline: 16 committed reports · 16 rows · ~249 legacy sites (2026-11-21 survey; queue order =
core.py base classes first, then leaves)
(Resume = the first row still `[ ]`; a row archives to [Group-finished.md](Group-finished.md)
only when all 8 steps are `[x]` and its commit exists)
Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target ·
③ §3 compare evidence · ④ §4 unit tests (TDD) · ⑤ §5 integration tests ·
⑥ §6 SWR update · ⑦ §7 RST update · ⑧ §8 verify and report
Per-row binding rules: one pywin32-exposed COM member per call —
`call_com(lambda: self._com.Name(...))` for method-shaped members,
`get_com_property`/`set_com_property` for property-shaped members, names confirmed in
`docs/reports/pywin32_authority.json`; catalog-absent sites are blockers, never blind
migrations; inherited members wait for their base class's own row.

- [ ] irp_class_api_report (IRPClass · IRPClass · models/com/telelogic/rhapsody/core/irp_class.py · 0 sites left)
  - Note: pilot run 2026-11-21, commits `7163149` + `b27a8bb`; 7 property-shaped flag sites migrated to `get_com_property`/`set_com_property` (`is_final` was already direct); six flag rows rewritten in `elements.rst`, SWR_ELEM_00004 updated.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live in the run report)
  - [x] Step 2 — §2 target resolved (wrapper canonical; JavaDoc evidence from committed report — live `docs/java_api` absent on macOS)
  - [x] Step 3 — §3 evidence compared (7 legacy sites identified, all property-shaped per catalog; offline proof: six flag families ALIAS_DOCUMENTED/informational, 78+5 matching committed summary)
  - [x] Step 4 — §4 unit tests (2 setter tests + structural guard red → 34/34 green in `test_irp_class.py`)
  - [x] Step 5 — §5 integration tests (behavior-preserving change; existing mirrored integration file collected 17 tests ✓ — no new coverage required)
  - [x] Step 6 — §6 SWR update (`docs/requirements/swr_elem_requirements.md` SWR_ELEM_00004: property mention + pywin32-direct binding statement)
  - [x] Step 7 — §7 RST update (`docs/api/elements.rst`: six flag rows rewritten, two pre-existing malformations fixed)
  - [ ] Step 8 — §8 verify and report (unit suite 1699 ✓, ruff/black/mypy ✓, skill tests 9 ✓; OPEN blocker: Windows closeout — `validate_interface.py IRPClass --source authority` + `verify_sync.py IRPClass` + live integration, then archive)

- [ ] irp_model_element_api_report (IRPModelElement · RPModelElement · models/core.py · ~86 sites)
  - Note: core.py holds 92 sites total incl. RPCollection + 2 forwarders — split at run start; 22 unit-family member names (`CMHeader`, `filename`, `isReadOnly`, ...) resolvable only via other interfaces' catalogs — resolve against IRPUnit's catalog entry or record blocker; `wrap()` (`getMetaClass`/`metaClass`) migrates here.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: JavaDoc package, wrapper/inheritance/exports/tests located; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` (mirrored test paths, `__init__.py` per level, no shim)
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPModelElement --source authority`; reconcile every owned member across JavaDoc/COM/Python; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`make_fake_element` method kwargs / `properties=` channel), then migrate every legacy helper site in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior in the mirrored test path (`tests/integration/models/com/telelogic/rhapsody/core/`); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md` (JavaDoc-derived description, deviations, implementation facts)
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPModelElement:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_collection_api_report (IRPCollection · RPCollection · models/core.py · ~2 sites)
  - Note: `get_count` (`getCount`/`Count` — catalog says `Count` property); mutators (`addItem`, `setSize`, `remove`, ...) already direct `call_com`; `make_fake_collection` stubs `getCount`/`getItem` — 163 test call sites depend on that shape.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPCollection --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPCollection:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_unit_api_report (IRPUnit · RPUnit · models/core.py · within core.py's 92)
  - Note: unit-family members — catalog kinds: methods `getAddToModelMode`/`getCMState`/`getLanguage`/`getLastModifiedTime`/`getNestedSaveUnits`/`getNestedSaveUnitsCount`/`isReadOnly`/`isReferenceUnit`/`isSeparateSaveUnit`/`setReadOnly`/`setSeparateSaveUnit`/`setUnitPath`; properties `CMHeader`/`currentDirectory`/`filename`/`includeInNextLoad`/`isStub`/`structureDiagrams`; landing this row resolves IRPModelElement's cross-catalog blockers.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPUnit --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPUnit:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_classifier_api_report (IRPClassifier · RPClassifier · models/elements/classifiers/model_classifier.py · 20 sites)
  - Note: 3 method-shaped (`getAttributesIncludingBases`, `getInterfaceItemsIncludingBases`, `getRelationsIncludingBases`), rest property-shaped.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPClassifier --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPClassifier:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_operation_api_report (IRPOperation · RPOperation · models/elements/classifiers/model_operation.py · 25 sites)
  - Note: 3 method-shaped (`setReturnTypeDeclaration`, `getReturnTypeDeclaration`, `getImplementationSignature`); `isAbstract`/`isStatic`/`isVirtual` are IRPOperation **properties** (arg2 wins — unlike IRPClass's method-exposed `getIsFinal`); `operation_action.py` facade stays untouched.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPOperation --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPOperation:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_attribute_api_report (IRPAttribute · RPAttribute · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPArgument in the same module; `multiplicity`/`declaration`/`defaultValue` properties per catalog.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAttribute --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPAttribute:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_port_api_report (IRPPort · RPPort · models/elements/relations/model_port.py · 10 sites)
  - Note: `getContract`/`setContract` ↔ `contract` — absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPort --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPPort:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_package_api_report (IRPPackage · RPPackage · models/elements/containment/model_package.py · 36 sites)
  - Note: 4 method-shaped (`getNamespace`, `getRemoteRequirementsPopulateMode`, `setRemoteRequirementsPopulateMode`, `getAllNestedElements`); `getRootInstanceSpecifications`/`rootInstanceSpecifications` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPackage --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPPackage:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_project_api_report (IRPProject · RPProject · models/elements/containment/model_project.py · 24 sites)
  - Note: 12 method-shaped (`setWaitDialogWatchdogValue`, `isActivelyManaged`, `getRoundtripShadowModel`, ...); `setGlobalConfiguration`/`setUseUniqueStereotypeAndRefCache` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPProject --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPProject:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_type_api_report (IRPType · RPType · models/elements/common/model_other_model.py · 9 sites)
  - Note: RPClassifierRole (1) and RPSysMLPort (3) sites in the same module are uncovered — out of this row's scope.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPType --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPType:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_argument_api_report (IRPArgument · RPArgument · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPAttribute in the same module.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPArgument --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPArgument:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_application_api_report (IRPApplication · RhapsodyApplication · application.py · 3 sites)
  - Note: `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`tests/unit/test_application.py`), then migrate the 3 sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_association_class_api_report (IRPAssociationClass · RPAssociationClass · models/elements/classifiers/model_association_class.py · 3 sites)
  - Note: integration-test ownership rules apply — assert only `get_end1`/`get_end2`/`get_is_class`/`set_is_class`.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAssociationClass --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior only (own-method assertions; mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPAssociationClass:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_interface_item_api_report (IRPInterfaceItem · RPInterfaceItem · models/elements/classifiers/model_interface_item.py · 4 sites)
  - Note: 2 method-shaped (`getSignatureNoArgNames`, `getSignatureNoArgTypes`).
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPInterfaceItem --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPInterfaceItem:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_usecase_api_report (IRPUseCase · RPUseCase · models/elements/classifiers/model_usecase.py · 4 sites)
  - Note: RPExtensionPoint lives in the same module with 0 legacy sites.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPUseCase --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: requirement entry in `docs/requirements/swr_elem_requirements.md`
  - [ ] Step 7 — §7 RST update: package-organized entry in `docs/api/elements.rst` (anchor `.. _rhapsody-java-interface-IRPUseCase:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
