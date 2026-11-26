# Sync todo: `containment` — `Group-containment-1.md`

Category: legacy module subpackage `containment` · 10 classes · group 1 of 2 for this category.

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

- [ ] irp_component_api_report (IRPComponent · RPComponent · elements/containment/model_component.py · 17 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: core structural element (118 src / 29 test, 43 owned methods). Extends the synced `IRPUnit`, so this is a leaf-style migration with no base-class dependency.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_component.md`
  - [ ] Step 7 — §7 RST update: `irp_component.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate
- [ ] irp_collaboration_api_report (IRPCollaboration · RPCollaboration · elements/containment/model_collaboration.py · 1 legacy site)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: common containment wrapper (77 src / 11 test, 39 owned methods). Extends the synced `IRPUnit`; low legacy-site count but high structural use closes the group.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_collaboration.md`
  - [ ] Step 7 — §7 RST update: `irp_collaboration.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate
- [ ] irp_configuration_api_report (IRPConfiguration · RPConfiguration · rhapsody_cli/models/elements/containment/model_configuration.py · 23 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 73 src / 16 test refs, 46 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_configuration.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_configuration.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_node_api_report (IRPNode · RPNode · rhapsody_cli/models/elements/containment/model_node.py · 2 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 30 src / 13 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_node.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_node.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_component_instance_api_report (IRPComponentInstance · RPComponentInstance · rhapsody_cli/models/elements/containment/model_component_instance.py · 0 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 21 src / 11 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_component_instance.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_component_instance.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_profile_api_report (IRPProfile · RPProfile · rhapsody_cli/models/elements/containment/model_profile.py · 0 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 12 src / 8 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_profile.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_profile.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_module_api_report (IRPModule · RPModule · rhapsody_cli/models/elements/containment/model_module.py · 0 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 8 src / 8 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_module.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_module.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_package_remediation - IRPPackage
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: 8 arity mismatches; 8 disallowed integration exception assertions; 30 property-shape conversions; add_association is a COM-only extension (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [x] Section 3 the 100 Java API members are reconciled: 94 matched and six documented-unavailable; no actionable rows, signature mismatches, or property-shape mismatches remain. Inherited `add_association` is supplied by `IRPModelElement`.
  - [x] Section 4 TDD red/green verified: the inheritance assertion failed with the child override, then passed after removing it; the documented remote-mode string test failed against the old `int` conversion, then passed after correcting the wrapper to `str`. Focused unit file 174 passed with 100% statement/branch coverage (261 statements; 0 branch points); full unit suite 2201 passed.
  - [ ] Section 5 package integration file: 98 passed; all 30/30 getter properties have populated identity/value assertions. `add_link` and `add_link_between_sysml_ports` have real live tests. A local `get_remote_requirements_populate_mode` probe after setting `"None"` returned `""`; a Design Manager server is required for a valid value. Full integration suite: 491 passed, 0 failed (baseline 481 passed, 6 failed).
  - [x] Section 6 `docs/requirements/com/telelogic/rhapsody/core/irp_package.md` updated to record inherited `add_association` ownership, generic-factory getter fixtures, and populated `links` integration coverage.
  - [x] Section 7 `docs/api/com/telelogic/rhapsody/core/irp_package.rst` has valid directives for the 69 owned methods and 30 properties; the inherited `add_association` directive was removed. `verify_sync.py` passes and `sphinx-build -b dummy docs docs/_build/irppackage` succeeds with no IRPPackage page autodoc failures (52 repository-wide warnings remain).
  - [ ] Section 8 `validate_interface.py` reports no actionable deviations; regular, strict-getter, strict-inherited, and RST checks pass; rhapsody-sync self-tests 90 passed, ruff/Black/mypy and LSP diagnostics are clean. Keep open: the P0 Design Manager getter precondition remains; do not archive until it has valid live evidence. The full integration suite passes 491 tests.
- [ ] irp_project_remediation - IRPProject
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open. Duplicate row for IRPProject also in Group-containment-2.md.
  - Baseline: 21 arity mismatches; 24 disallowed integration exception assertions; 9 read-only and 1 writable property-shape conversions; 7 COM-only extensions (D2 default: retain and document).
  - [ ] Section 1 member checklist and getter matrix published.
  - [x] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 all 21 signatures, 9 read properties plus the writable property, and 7 extension dispositions reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_project.py at 100% statements/branches.
  - [ ] Section 5 project getters establish live project state and assert returned identity/value; all 24 exception sites resolved or blocked.
  - [ ] Section 6 irp_project.md checked/updated.
  - [ ] Section 7 irp_project.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [x] irp_package_api_report (IRPPackage · IRPPackage · models/elements/containment/model_package.py · 36 sites)
  - Main status (2026-11-26): verify_sync passes; all steps archived.
  - Note: 4 method-shaped (`getNamespace`, `getRemoteRequirementsPopulateMode`, `setRemoteRequirementsPopulateMode`, `getAllNestedElements`); `getRootInstanceSpecifications`/`rootInstanceSpecifications` absent from every catalog: blocker unless Windows typelib regen resolves it.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPPackage --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPPackage:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
