# Sync todo: `classifiers` — `Group-classifiers-1.md`

Category: legacy module subpackage `classifiers` · 10 classes · group 1 of 2 for this category.

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

- [ ] irp_statechart_api_report (IRPStatechart · RPStatechart · elements/classifiers/model_statechart.py · 10 legacy sites)
  - Note: behavioural container (97 src / 14 test, 31 owned methods). Already extends the synced `IRPClass`; a direct leaf migration once its report exists.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_statechart.md`
  - [ ] Step 7 — §7 RST update: `irp_statechart.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate
- [ ] irp_stereotype_api_report (IRPStereotype · RPStereotype · rhapsody_cli/models/elements/classifiers/model_stereotype.py · 3 legacy sites)
  - Note: usage 30 src / 15 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_stereotype.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_stereotype.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_actor_api_report (IRPActor · RPActor · rhapsody_cli/models/elements/classifiers/model_actor.py · 2 legacy sites)
  - Note: usage 31 src / 11 test refs, 4 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_actor.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_actor.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_exception_api_report (IRPException · RPException · rhapsody_cli/models/elements/classifiers/model_exception.py · 0 legacy sites)
  - Note: usage 5 src / 4 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_exception.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_exception.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_extension_point_api_report (IRPExtensionPoint · RPExtensionPoint · rhapsody_cli/models/elements/classifiers/model_usecase.py · 0 legacy sites)
  - Note: usage 6 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_extension_point.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_extension_point.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_classifier_remediation - IRPClassifier
  - Baseline: 17 property-shape conversions; add_port maps to COM addNewAggr absent from JavaDoc (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 all 17 property members and add_port disposition reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_classifier.py at 100% statements/branches.
  - [ ] Section 5 each collection getter creates its target attribute/operation/port/diagram/relationship and asserts membership/identity.
  - [ ] Section 6 irp_classifier.md checked/updated.
  - [ ] Section 7 irp_classifier.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_association_class_remediation - IRPAssociationClass
  - Baseline: end1, end2, and is_class are property-shaped; integration test asserts AttributeError on a regular association; test docstring contains stale xfail text.
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 establish whether a real AssociationClass can be created through documented live APIs.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_association_class.py at 100% statements/branches.
  - [ ] Section 5 assert both ends and class flag on a real AssociationClass, or leave a user-approved blocker open; remove stale xfail claim.
  - [ ] Section 6 irp_association_class.md checked/updated.
  - [ ] Section 7 irp_association_class.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_operation_remediation - IRPOperation
  - Baseline: 15 property-shaped members; integration test asserts AttributeError for get_flowchart.
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 all 15 properties and the get_flowchart/catalog disposition reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_operation.py at 100% statements/branches.
  - [ ] Section 5 create a real operation/flowchart fixture and assert live outcome, or document the verified unavailable-member stub.
  - [ ] Section 6 irp_operation.md checked/updated.
  - [ ] Section 7 irp_operation.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_class_remediation - IRPClass
  - Baseline: property shape already conforms; 2 integration tests assert RhapsodyRuntimeException.
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 resolve both failing members against JavaDoc and pywin32 signatures.
  - [ ] Section 4 full unit suite green; irp_class.py at 100% statements/branches.
  - [ ] Section 5 assert positive live outcomes for both members with authentic setup, or leave verified blockers open.
  - [ ] Section 6 irp_class.md checked/updated.
  - [ ] Section 7 irp_class.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_use_case_remediation - IRPUseCase
  - Baseline: 4 property-shape conversions; 3 integration tests assert TypeError; two JavaDoc-only methods already have unavailable stubs.
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 reconcile find_extension_point and both other failing signatures against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_use_case.py at 100% statements/branches.
  - [ ] Section 5 create entry/extension points and assert getter identity/content; replace all three exception assertions.
  - [ ] Section 6 irp_use_case.md checked/updated.
  - [ ] Section 7 irp_use_case.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
