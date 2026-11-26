# Sync todo: `relations` — `Group-relations-1.md`

Category: legacy module subpackage `relations` · 8 classes · group 1 of 1 for this category.

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

- [ ] irp_instance_api_report (IRPInstance · `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py` · Java package `com.telelogic.rhapsody.core`)
  - Main status (2026-11-26): verify_sync passes; validator 0 actionable (2 documented-unavailable stubs); Step 5 and Step 8 open (see below).
  - Note: the wrapper moved to the canonical package. The typelib catalog is merged for IRPInstance; `instantiated_by` is now a property (get/set) backed by `instantiatedBy`; `get_all_nested_elements` and `update_contained_diagrams_on_server` are documented-unavailable stubs.
  - [x] Step 1 — §1 sync TODO: 13-member JavaDoc inventory published in the wrapper checklist and the report.
  - [x] Step 2 — §2 resolve target: canonical wrapper and mirrored unit test confirmed; report Java package line present; no compatibility shim.
  - [x] Step 3 — §3 compare evidence: typelib catalog merged for IRPInstance only; validator 0 actionable; 12 Python members vs 13 Java members (2 stubs documented unavailable).
  - [x] Step 4 — §4 unit tests (TDD): 4 new tests failed first (red), then passed; `test_irp_instance.py` 16 passed, `irp_instance.py` 35 statements / 18 branches, 100.00%; full unit suite 2201 passed; ruff/black/mypy clean.
  - [ ] Step 5 — §5 integration tests: `test_irp_instance.py` has 2 live stub tests (`pytest.raises(NotImplementedError)`), both passing. Open blocker: no documented creation path for an `IRPInstance` is exposed by the registered typelib. `IRPPackage.addInstanceSpecification` is JavaDoc-only (pywin32 stub raises NotImplementedError), no catalog member adds an instance, and `add_new_aggr("Instance", …)` is not a valid creation route. The test project contains no instances, so the populated checks for `instantiated_by`, `get_attribute_value`/`set_attribute_value`, links, initializer arguments, and `add_relation_to_the_whole` cannot be built authentically. A second blocker is a design choice: objects returned to the wrapper expose the generic `IRPModelElement` interface, and `win32com.client.CastTo(obj, "IRPInstance")` reaches the instance members (probe-verified). Checked `docs/java_api/rational_rhapsody_api_getting_started.pdf`: its only object-creation sample is `IRPConfiguration.addInitialInstance(class)`. Probe-verified live: the call succeeds, but `initialInstances` returns the class itself (metaClass `Class`), not an IRPInstance, so this route does not create an IRPInstance either.
  - [x] Step 6 — §6 SWR update: `docs/requirements/com/telelogic/rhapsody/core/irp_instance.md` holds SWR_ELEM_00009 (moved from the legacy monolith, which no longer contains it).
  - [x] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_instance.rst` documents all 12 public members; toctree entry added in `docs/api/elements.rst`.
  - [ ] Step 8 — §8 validation: `validate_interface.py`, `verify_sync.py`, skill harness (85 passed), unit suite (2201 passed), ruff/black/mypy and Sphinx (exit 0) pass. Open: `verify_sync.py --strict-getters` fails on `instantiated_by` (MISSING populated test) until Step 5 is resolved; full Windows integration run not repeated.
- [ ] irp_relation_api_report (IRPRelation · RPRelation · elements/relations/model_relation.py · 27 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: foundational relation type (108 src / 47 test, 31 owned methods). Do this before IRPInstance; 27 legacy sites make it the highest cleanup value in this group.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_relation.md`
  - [ ] Step 7 — §7 RST update: `irp_relation.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate
- [ ] irp_dependency_api_report (IRPDependency · RPDependency · rhapsody_cli/models/elements/relations/model_dependency.py · 2 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 33 src / 13 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_dependency.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_dependency.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_generalization_api_report (IRPGeneralization · RPGeneralization · rhapsody_cli/models/elements/relations/model_generalization.py · 5 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 24 src / 8 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_generalization.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_generalization.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_association_role_api_report (IRPAssociationRole · RPAssociationRole · rhapsody_cli/models/elements/relations/model_association_role.py · 3 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 16 src / 8 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_association_role.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_association_role.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_hyper_link_api_report (IRPHyperLink · RPHyperLink · rhapsody_cli/models/elements/relations/model_hyperlink.py · 2 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 13 src / 8 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_hyper_link.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_hyper_link.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_port_remediation - IRPPort
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: 5 property-shape conversions; the headless full-integration baseline has 2 port-test failures requiring evidence-based triage.
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 all 5 property members and the two live failures reconciled against JavaDoc/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_port.py at 100% statements/branches.
  - [ ] Section 5 create real provided/required interfaces and assert returned membership/value; resolve the two baseline failures.
  - [ ] Section 6 irp_port.md checked/updated.
  - [ ] Section 7 irp_port.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [x] irp_port_api_report (IRPPort · IRPPort · models/elements/relations/model_port.py · 10 sites)
  - Main status (2026-11-26): verify_sync passes; all steps archived.
  - Note: `getContract`/`setContract` ↔ `contract` — absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPort --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPort:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
