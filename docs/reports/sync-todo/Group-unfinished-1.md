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

- [ ] irp_model_element_api_report (IRPModelElement · models/core.py · 1 blocker site left)
  - Note: re-run completed 2026-11-21 under the updated skill (shape-follows-COM, future annotations, own-members report + Correct Items, Java-package declaration). Class renamed `RPModelElement` → `IRPModelElement`; python-only `get_oslc_links` removed (stale premise — `getOSLCLinks` is exposed by pywin32); `core.py` converted to `from __future__ import annotations` with unquoted type references and local runtime imports for `cast()` (25 casts + 84 annotations); `wrap()` reads the `metaClass` property; RPCollection migrated; IRPUnit's 21 sites remain for its own row.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live)
  - [ ] Step 2 — §2 target resolved; report Java-package declaration verified (`com.telelogic.rhapsody.core`, agrees with JavaDoc); §2 canonical move still pending — the old cycle blocker is lifted by the revised standing decision (local import before `cast()` + `from __future__ import annotations`, proven by the IRPUnit move), so the move no longer needs a separate refactor
  - [x] Step 3 — §3 evidence compared offline (committed own-members report + catalog: 1 actionable blocker `get_rmm_url` left unchanged, 96 correct items, 5 backlog rows; python-only `get_oslc_links` removed per §4 — report row disappears at closeout regeneration)
  - [x] Step 4 — §4 unit tests (structural guard green; future-annotations guard green: no quoted casts/annotations, `from __future__ import annotations` present; full unit suite 1711 green)
  - [x] Step 5 — §5 integration tests (mirror unit/integration files verified exercising `IRPModelElement` via `test_core.py`; behavior-preserving; Windows live run tracked in Step 8)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_model_element.md` — binding rules, `get_rmm_url` blocker, deferred-move note, future-annotations fact)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_model_element.rst` — 6 deviation rows + 96 Correct-Items rows, coverage complete; get_oslc_links row removed per §7; toctree wired)
  - [ ] Step 8 — §8 verify and report (unit suite 1711 ✓, ruff/black/mypy ✓, skill tests 15 ✓, mirror test files ✓; OPEN blocker: Windows closeout — regenerate the report (resolves the stale `RPModelElement` target line and the removed `get_oslc_links` row), then `validate_interface.py` + `verify_sync.py` + live integration; the pending canonical move keeps verify_sync's wrapper-placement check red until this row performs its §2 move; the rule no longer requires waiting for a dedicated core.py refactor)

- [ ] irp_unit_api_report (IRPUnit · canonical `models/com/telelogic/rhapsody/core/irp_unit.py`) — 8/8, awaiting commit to archive
  - Note: unit-family members — catalog kinds: methods `getAddToModelMode`/`getCMState`/`getLanguage`/`getLastModifiedTime`/`getNestedSaveUnits`/`getNestedSaveUnitsCount`/`isReadOnly`/`isReferenceUnit`/`isSeparateSaveUnit`/`setReadOnly`/`setSeparateSaveUnit`/`setUnitPath`; properties `CMHeader`/`currentDirectory`/`filename`/`includeInNextLoad`/`isStub`/`structureDiagrams`; landing this row resolves IRPModelElement's cross-catalog blockers.
  - [x] Step 1 — §1 sync TODO published: 7 shared step tasks + 29-member inventory (all owned; inherited `IRPModelElement` members kept separate)
  - [x] Step 2 — §2 target resolved and canonical move completed: report Java package `com.telelogic.rhapsody.core` agrees with `IRPUnit.html`; `RPUnit` → `IRPUnit` renamed, then wrapper + `AddToModelMode` moved to `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py`; mirrored tests at `tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_irp_unit.py`; canonical `__init__.py` lazy exports; all internal imports updated; `core.py:get_save_unit()` imports locally before `cast()` (no cycle; quoted types unnecessary under `from __future__ import annotations`); no compatibility shim. Doubled-prefix artifacts from the bulk rename were fixed repo-wide.
  - [x] Step 3 — §3 evidence compared offline (regenerated report: 0 deviations, 29 owned members; 21 legacy dual-binding sites mapped one-to-one to pywin32 members; catalog-absent `getUnitPath` left unchanged as expected informational difference; no python-only members)
  - [x] Step 4 — §4 unit tests (TDD): 10 tests red → green; structural guard (21 offenders → 0) + future-annotations guard added; full unit suite 1714 green; canonical `irp_unit.py` coverage 100% (68/68 statements, 40/40 branches)
  - [x] Step 5 — §5 integration tests: mirrored canonical path, 22 tests collected; Windows live run 15 passed / 3 skipped (pre-existing `second_test_project` TODO fixture) / 4 xfailed (pre-existing getUnitPath COM gaps), no failures
  - [x] Step 6 — §6 SWR update: `docs/requirements/com/telelogic/rhapsody/core/irp_unit.md` (SWR_CORE_00002 moved out of `swr_core_requirements.md`, no duplicate; canonical implementation path)
  - [x] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_unit.rst` (anchor + 7-row deviation list-table covering getUnitPath/setUnitPath and method-vs-property shapes; canonical import; toctree wired in `docs/api/elements.rst`)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` ✓ (0 deviations), `verify_sync.py` ✓ (artifacts verified), skill self-tests 15 ✓, full unit suite 1714 ✓, ruff/black/mypy ✓, Windows live integration ✓

- [ ] irp_classifier_api_report (IRPClassifier · RPClassifier · models/elements/classifiers/model_classifier.py · 20 sites)
  - Note: 3 method-shaped (`getAttributesIncludingBases`, `getInterfaceItemsIncludingBases`, `getRelationsIncludingBases`), rest property-shaped.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPClassifier --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPClassifier:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_operation_api_report (IRPOperation · RPOperation · models/elements/classifiers/model_operation.py · 25 sites)
  - Note: 3 method-shaped (`setReturnTypeDeclaration`, `getReturnTypeDeclaration`, `getImplementationSignature`); `isAbstract`/`isStatic`/`isVirtual` are IRPOperation **properties** (arg2 wins — unlike IRPClass's method-exposed `getIsFinal`); `operation_action.py` facade stays untouched.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPOperation --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPOperation:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_attribute_api_report (IRPAttribute · RPAttribute · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPArgument in the same module; `multiplicity`/`declaration`/`defaultValue` properties per catalog.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAttribute --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAttribute:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_port_api_report (IRPPort · RPPort · models/elements/relations/model_port.py · 10 sites)
  - Note: `getContract`/`setContract` ↔ `contract` — absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPort --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPort:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_package_api_report (IRPPackage · RPPackage · models/elements/containment/model_package.py · 36 sites)
  - Note: 4 method-shaped (`getNamespace`, `getRemoteRequirementsPopulateMode`, `setRemoteRequirementsPopulateMode`, `getAllNestedElements`); `getRootInstanceSpecifications`/`rootInstanceSpecifications` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPackage --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPackage:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_project_api_report (IRPProject · RPProject · models/elements/containment/model_project.py · 24 sites)
  - Note: 12 method-shaped (`setWaitDialogWatchdogValue`, `isActivelyManaged`, `getRoundtripShadowModel`, ...); `setGlobalConfiguration`/`setUseUniqueStereotypeAndRefCache` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPProject --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPProject:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_type_api_report (IRPType · RPType · models/elements/common/model_other_model.py · 9 sites)
  - Note: RPClassifierRole (1) and RPSysMLPort (3) sites in the same module are uncovered — out of this row's scope.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPType --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPType:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_argument_api_report (IRPArgument · RPArgument · models/elements/variables/model_variables.py · within shared 14)
  - Note: shares the 14 covered sites with IRPAttribute in the same module.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPArgument --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPArgument:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_application_api_report (IRPApplication · RhapsodyApplication · application.py · 3 sites)
  - Note: `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`tests/unit/test_application.py`), then migrate the 3 sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_association_class_api_report (IRPAssociationClass · RPAssociationClass · models/elements/classifiers/model_association_class.py · 3 sites)
  - Note: integration-test ownership rules apply — assert only `get_end1`/`get_end2`/`get_is_class`/`set_is_class`.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAssociationClass --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior only (own-method assertions; mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAssociationClass:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_interface_item_api_report (IRPInterfaceItem · RPInterfaceItem · models/elements/classifiers/model_interface_item.py · 4 sites)
  - Note: 2 method-shaped (`getSignatureNoArgNames`, `getSignatureNoArgTypes`).
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPInterfaceItem --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPInterfaceItem:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

- [ ] irp_usecase_api_report (IRPUseCase · RPUseCase · models/elements/classifiers/model_usecase.py · 4 sites)
  - Note: RPExtensionPoint lives in the same module with 0 legacy sites.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPUseCase --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [ ] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPUseCase:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
