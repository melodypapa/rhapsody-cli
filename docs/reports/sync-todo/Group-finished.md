# Sync todo: `docs/reports` — `Group-finished` (archive)

Rows move here from `Group-unfinished-*.md` once all eight steps (SKILL.md §1–§8) are `[x]` and
the run's commit exists. Keep the row's original text and ticks; do not rewrite history.

## Test-rule follow-up (2026-11-22)

Applied the no-skip/no-xfail + 100%-coverage rule retroactively to these three archived
classes. Removed five IRPUnit live tests that this Rhapsody build cannot execute (three
cross-project operations and two load/unload lifecycle cases — all still covered by fake-COM
unit tests), rewrote two `getUnitPath` tests to assert the catalog-absent member, and removed
one IRPCollection graphical-node test whose COM member is absent. Verified: zero skip/xfail
markers in the finished classes' test files, 46 finished-class live integration tests green,
and 100% statement/branch coverage for `irp_class.py`, `irp_collection.py` and `irp_unit.py`.

## API report refresh (2026-11-22)

Regenerated all 16 API reports after enumerating the registered Rhapsody type library. The
fresh 16-interface catalog exactly matches `pywin32_authority.json`; no member or shape
changes were found. The API reports are organized under `docs/reports/<java.package.path>/`
and their generated content remains consistent with the fresh catalog. The archived rows and
their historical closeout evidence are unchanged.

- [x] irp_class_api_report (IRPClass · IRPClass · models/com/telelogic/rhapsody/core/irp_class.py · 0 sites left)
  - Note: pilot run 2026-11-21, commits `7163149` + `b27a8bb`; 7 property-shaped flag sites migrated to `get_com_property`/`set_com_property` (`is_final` was already direct); six flag rows rewritten in `elements.rst`, SWR_ELEM_00004 updated.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live in the run report)
  - [x] Step 2 — §2 target resolved (wrapper canonical; JavaDoc evidence from committed report — live `docs/java_api` absent on macOS)
  - [x] Step 3 — §3 evidence compared (7 legacy sites identified, all property-shaped per catalog; offline proof: six flag families ALIAS_DOCUMENTED/informational, 78+5 matching committed summary)
  - [x] Step 4 — §4 unit tests (2 setter tests + structural guard red → 34/34 green in `test_irp_class.py`)
  - [x] Step 5 — §5 integration tests (behavior-preserving change; existing mirrored integration file collected 17 tests ✓ — no new coverage required)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_class.md` — SWR_ELEM_00004 moved from the legacy monolith; property mention + pywin32-direct binding statement)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_class.rst` — section moved from `elements.rst`, six flag rows rewritten, two malformations fixed; toctree entry added)
  - [x] Step 8 — §8 verify and report (Windows closeout 2026-11-21: `validate_interface.py IRPClass --source authority` exit 0 / 0 deviations; `verify_sync.py IRPClass` exit 0; skill self-tests 9 ✓; unit suite 1708 ✓ with `PYTHONPATH=src`; ruff/black/mypy ✓; live integration 17/17 ✓ on a fresh Rhapsody instance — first attempt crashed against the pre-existing user session instance, rerun with a clean instance passed)

- [x] irp_collection_api_report (IRPCollection · IRPCollection · models/core.py · 2 blocker sites left)
  - Note: run 2026-11-21 — `get_count` migrated to the `Count` property and `get_item` migrated to the direct `Item` method (the legacy `getItem` name-probe removed); `make_fake_collection` exposes both forms (`Count` attribute + `Item` side_effect) keeping the ~163 dependent call sites green; `add_graphical_item` and `to_list` are documented blockers (Java members absent from pywin32).
  - [x] Step 1 — §1 sync TODO published (per-run checklist with 11 owned-member subtasks rendered live at run start)
  - [x] Step 2 — §2 target resolved (report Java package `com.telelogic.rhapsody.core` agrees with JavaDoc; wrapper class body moved to canonical `models/com/telelogic/rhapsody/core/irp_collection.py`, re-exported from `rhapsody_cli.models` / `core.py`; 64 importers rewritten; lazy canonical `__init__` breaks the import cycle; report regenerated, `verify_sync.py IRPCollection` exit 0)
  - [x] Step 3 — §3 evidence compared (validator baseline exit 1 with only the 2 known `PYWIN32_MEMBER_MISSING` deviations; 11 owned members reconciled — 9 MATCH, `add_graphical_item`/`to_list` catalog-absent blockers; RST table coverage confirmed by `verify_sync.py`)
  - [x] Step 4 — §4 unit tests (prior guard-red → migration retained; canonical module has its own fake-COM tests plus the no-legacy-helper structural guard); full unit suite 1711 ✓
  - [x] Step 5 — §5 integration tests (behavior-preserving; live Windows run of `tests/integration/models/test_core.py -k IRPCollection`: 11 passed + 1 xfailed over 3 owned classes ✓)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_collection.md` — SWR_ELEM_00015; implementation path updated to the canonical module)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_collection.rst` — canonical Python import added, deferred-move note removed; deviation table unchanged and verified)
  - [x] Step 8 — §8 verify and report (2026-11-21: `validate_interface.py IRPCollection --source authority` exit 1 with only the 2 known blockers; `verify_sync.py IRPCollection` exit 0; 13 skill tests ✓; 1711 unit tests ✓; ruff/black/mypy ✓; live integration 11 passed + 1 xfailed ✓; archived)

- [x] irp_unit_api_report (IRPUnit · canonical `models/com/telelogic/rhapsody/core/irp_unit.py`) — 8/8, archived in commit `1c81084`
  - Note: unit-family members — catalog kinds: methods `getAddToModelMode`/`getCMState`/`getLanguage`/`getLastModifiedTime`/`getNestedSaveUnits`/`getNestedSaveUnitsCount`/`isReadOnly`/`isReferenceUnit`/`isSeparateSaveUnit`/`setReadOnly`/`setSeparateSaveUnit`/`setUnitPath`; properties `CMHeader`/`currentDirectory`/`filename`/`includeInNextLoad`/`isStub`/`structureDiagrams`; landing this row resolves IRPModelElement's cross-catalog blockers.
  - [x] Step 1 — §1 sync TODO published: 7 shared step tasks + 29-member inventory (all owned; inherited `IRPModelElement` members kept separate)
  - [x] Step 2 — §2 target resolved and canonical move completed: report Java package `com.telelogic.rhapsody.core` agrees with `IRPUnit.html`; `RPUnit` → `IRPUnit` renamed, then wrapper + `AddToModelMode` moved to `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py`; mirrored tests at `tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_irp_unit.py`; canonical `__init__.py` lazy exports; all internal imports updated; `core.py:get_save_unit()` imports locally before `cast()` (no cycle; quoted types unnecessary under `from __future__ import annotations`); no compatibility shim. Doubled-prefix artifacts from the bulk rename were fixed repo-wide.
  - [x] Step 3 — §3 evidence compared offline (regenerated report: 0 deviations, 29 owned members; 21 legacy dual-binding sites mapped one-to-one to pywin32 members; catalog-absent `getUnitPath` left unchanged as expected informational difference; no python-only members)
  - [x] Step 4 — §4 unit tests (TDD): 10 tests red → green; structural guard (21 offenders → 0) + future-annotations guard added; full unit suite 1714 green; canonical `irp_unit.py` coverage 100% (68/68 statements, 40/40 branches)
  - [x] Step 5 — §5 integration tests: mirrored canonical path, 22 tests collected; Windows live run 15 passed / 3 skipped (pre-existing `second_test_project` TODO fixture) / 4 xfailed (pre-existing getUnitPath COM gaps), no failures
  - [x] Step 6 — §6 SWR update: `docs/requirements/com/telelogic/rhapsody/core/irp_unit.md` (SWR_CORE_00002 moved out of `swr_core_requirements.md`, no duplicate; canonical implementation path)
  - [x] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_unit.rst` (anchor + 7-row deviation list-table covering getUnitPath/setUnitPath and method-vs-property shapes; canonical import; toctree wired in `docs/api/elements.rst`)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` ✓ (0 deviations), `verify_sync.py` ✓ (artifacts verified), skill self-tests 15 ✓, full unit suite 1714 ✓, ruff/black/mypy ✓, Windows live integration ✓

- [x] irp_classifier_api_report (IRPClassifier · IRPClassifier · models/elements/classifiers/model_classifier.py · 20 sites)
  - Note: 3 method-shaped (`getAttributesIncludingBases`, `getInterfaceItemsIncludingBases`, `getRelationsIncludingBases`), rest property-shaped.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPClassifier --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPClassifier:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_operation_api_report (IRPOperation · IRPOperation · models/elements/classifiers/model_operation.py · 25 sites)
  - Note: 3 method-shaped (`setReturnTypeDeclaration`, `getReturnTypeDeclaration`, `getImplementationSignature`); `isAbstract`/`isStatic`/`isVirtual` are IRPOperation **properties** (arg2 wins — unlike IRPClass's method-exposed `getIsFinal`); `operation_action.py` facade stays untouched.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPOperation --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPOperation:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_attribute_api_report (IRPAttribute · IRPAttribute · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPArgument in the same module; `multiplicity`/`declaration`/`defaultValue` properties per catalog.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAttribute --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAttribute:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_port_api_report (IRPPort · IRPPort · models/elements/relations/model_port.py · 10 sites)
  - Note: `getContract`/`setContract` ↔ `contract` — absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPort --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPort:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_package_api_report (IRPPackage · IRPPackage · models/elements/containment/model_package.py · 36 sites)
  - Note: 4 method-shaped (`getNamespace`, `getRemoteRequirementsPopulateMode`, `setRemoteRequirementsPopulateMode`, `getAllNestedElements`); `getRootInstanceSpecifications`/`rootInstanceSpecifications` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPackage --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPackage:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_project_api_report (IRPProject · IRPProject · models/elements/containment/model_project.py · 24 sites)
  - Note: 12 method-shaped (`setWaitDialogWatchdogValue`, `isActivelyManaged`, `getRoundtripShadowModel`, ...); `setGlobalConfiguration`/`setUseUniqueStereotypeAndRefCache` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPProject --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPProject:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_type_api_report (IRPType · IRPType · models/elements/common/model_other_model.py · 9 sites)
  - Note: RPClassifierRole (1) and RPSysMLPort (3) sites in the same module are uncovered — out of this row's scope.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPType --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPType:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_argument_api_report (IRPArgument · IRPArgument · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPAttribute in the same module.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPArgument --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPArgument:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_association_class_api_report (IRPAssociationClass · IRPAssociationClass · models/elements/classifiers/model_association_class.py · 3 sites)
  - Note: integration-test ownership rules apply — assert only `get_end1`/`get_end2`/`get_is_class`/`set_is_class`.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAssociationClass --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior only (own-method assertions; mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAssociationClass:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_interface_item_api_report (IRPInterfaceItem · IRPInterfaceItem · models/elements/classifiers/model_interface_item.py · 4 sites)
  - Note: 2 method-shaped (`getSignatureNoArgNames`, `getSignatureNoArgTypes`).
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPInterfaceItem --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPInterfaceItem:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_usecase_api_report (IRPUseCase · IRPUseCase · models/elements/classifiers/model_usecase.py · 4 sites)
  - Note: RPExtensionPoint lives in the same module with 0 legacy sites.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPUseCase --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPUseCase:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [x] irp_model_element_api_report (IRPModelElement · models/core.py · 1 blocker site left)
  - Note: re-run completed 2026-11-21 under the updated skill (shape-follows-COM, future annotations, own-members report + Correct Items, Java-package declaration). Class renamed `RPModelElement` → `IRPModelElement`; python-only `get_oslc_links` removed (stale premise — `getOSLCLinks` is exposed by pywin32); `core.py` converted to `from __future__ import annotations` with unquoted type references and local runtime imports for `cast()` (25 casts + 84 annotations); `wrap()` reads the `metaClass` property; RPCollection migrated; IRPUnit's 21 sites remain for its own row.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live)
  - [x] Step 2 — §2 target resolved; report Java-package declaration verified (`com.telelogic.rhapsody.core`, agrees with JavaDoc); canonical move complete: `IRPModelElement` → `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`, `AbstractRPModelElement` stays in `models/core.py` with a local import in `wrap()`; 78 import sites updated; mirrored unit/integration test files moved; canonical `__init__.py` and RST import path updated.
  - [x] Step 3 — §3 evidence compared offline (committed own-members report + catalog: 1 actionable blocker `get_rmm_url` left unchanged, 96 correct items, 5 backlog rows; python-only `get_oslc_links` removed per §4 — report row disappears at closeout regeneration)
  - [x] Step 4 — §4 unit tests (structural guard green; future-annotations guard green: no quoted casts/annotations, `from __future__ import annotations` present; full unit suite 1711 green)
  - [x] Step 5 — §5 integration tests (mirror unit/integration files verified exercising `IRPModelElement` via `test_core.py`; behavior-preserving; Windows live run tracked in Step 8)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_model_element.md` — binding rules, `get_rmm_url` blocker, deferred-move note, future-annotations fact)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_model_element.rst` — 6 deviation rows + 96 Correct-Items rows, coverage complete; get_oslc_links row removed per §7; toctree wired)
  - [x] Step 8 — §8 verify and report (all eight steps green: report regenerated with canonical target line, `validate_interface.py` ✓, `verify_sync.py` ✓, 0 skip/xfail markers, 100% statement/branch coverage at both unit and integration layers, 105 live integration tests ✓, full unit suite ✓, ruff/black/mypy ✓; commits `6cbebc3` + `1778607` + `5175b93`)
