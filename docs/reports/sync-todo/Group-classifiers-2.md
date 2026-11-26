# Sync todo: `classifiers` — `Group-classifiers-2.md`

Category: legacy module subpackage `classifiers` · 6 classes · group 2 of 2 for this category.

Rows were regrouped from the former numbered batch files by legacy module subpackage (the domain folder in each row's path); classes without a legacy path were mapped from their legacy class names.

Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target · ③ §3 compare
evidence · ④ §4 unit tests (TDD) · ⑤ §5 integration tests · ⑥ §6 SWR update · ⑦ §7 RST update ·
⑧ §8 verify and report. Per-row binding rules: one pywin32-exposed COM member per call —
`call_com(lambda: self._com.Name(...))` for method-shaped members,
`get_com_property` / `set_com_property` for property-shaped members; catalog-absent sites are
blockers, never blind migrations.

Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` with mirrored
`tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_<snake>.py`.

## Rows

- [x] irp_interface_item_remediation - IRPInterfaceItem
  - Main status (2026-11-26): verify_sync passes; all steps archived.
  - Baseline: JavaDoc and report declare `com.telelogic.rhapsody.core`; seven owned members, zero validator deviations. Existing canonical wrapper/tests/exports verified.
  - [x] Section 1: member checklist published; both getter matrix rows include fixture, relationship, identity/value assertion, test, and package cleanup.
  - [x] Section 2: canonical wrapper, mirrored tests, imports/exports, and registration verified; report package agrees with JavaDoc.
  - [x] Section 3: all seven owned members reconciled and matched. Live COM showed `addArgumentBeforePosition` expects zero-based position although JavaDoc specifies 1-based; wrapper converts `pos - 1`. Report regenerated; no actionable deviations.
  - [x] Section 4: unit test first failed on the position conversion, then passed after the minimal wrapper fix. Focused unit coverage: 100% statements and branches (25 statements, 10 branches); full unit suite: 2,172 passed.
  - [x] Section 5: four live integration tests pass, including populated `arguments` identity, exact operation/signature values, insertion order, and positive/negative signature matching. Fixtures delete their test packages; no exception assertions, skips, or xfails. Full integration suite: 449 passed.
  - [x] Section 6: `docs/requirements/com/telelogic/rhapsody/core/irp_interface_item.md` updated with JavaDoc class description and verified COM position conversion.
  - [x] Section 7: `docs/api/com/telelogic/rhapsody/core/irp_interface_item.rst` corrected to JavaDoc description and complete canonical identity; all seven public members documented; page already present in `docs/api/elements.rst` toctree.
  - [x] Section 8: report regenerated; `validate_interface.py`, `verify_sync.py`, and `--strict-getters` pass; sync self-tests 83 passed; `ruff`, `black`, and `mypy` clean; baseline → final counts: unit 2,171 → 2,172 passed, integration 449 → 449 passed. Integration exception-catch list: none. Commit is recorded by the commit that archives this row.
  - Members: `addArgument(String)` matched; `addArgumentBeforePosition(String, int)` matched with documented 1-based → COM 0-based conversion; `getArguments()` → `arguments` matched/property; `getSignature()` → `signature` matched/property; `getSignatureNoArgNames()` matched; `getSignatureNoArgTypes()` matched; `matchOnSignature(IRPInterfaceItem)` matched.
- [x] irp_classifier_api_report (IRPClassifier · IRPClassifier · models/elements/classifiers/model_classifier.py · 20 sites)
  - Main status (2026-11-26): verify_sync passes; all steps archived. Duplicate row for IRPClassifier also in Group-classifiers-1.md.
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
  - Main status (2026-11-26): verify_sync passes; all steps archived. Duplicate row for IRPOperation also in Group-classifiers-1.md.
  - Note: 3 method-shaped (`setReturnTypeDeclaration`, `getReturnTypeDeclaration`, `getImplementationSignature`); `isAbstract`/`isStatic`/`isVirtual` are IRPOperation **properties** (arg2 wins — unlike IRPClass's method-exposed `getIsFinal`); `operation_action.py` facade stays untouched.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPOperation --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPOperation:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_association_class_api_report (IRPAssociationClass · IRPAssociationClass · models/elements/classifiers/model_association_class.py · 3 sites)
  - Main status (2026-11-26): verify_sync passes; all steps archived. Duplicate row for IRPAssociationClass also in Group-classifiers-1.md.
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
  - Main status (2026-11-26): verify_sync passes; all steps archived.
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
  - Main status (2026-11-26): verify_sync passes; all steps archived. Duplicate row for IRPUseCase also in Group-classifiers-1.md.
  - Note: RPExtensionPoint lives in the same module with 0 legacy sites.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPUseCase --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPUseCase:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
