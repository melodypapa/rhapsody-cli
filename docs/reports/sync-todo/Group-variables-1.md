# Sync todo: `variables` — `Group-variables-1.md`

Category: legacy module subpackage `variables` · 8 classes · group 1 of 1 for this category.

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

- [ ] irp_tag_api_report (IRPTag · RPTag · rhapsody_cli/models/elements/variables/model_variables.py · 8 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 37 src / 29 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_tag.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_tag.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_variable_api_report (IRPVariable · RPVariable · rhapsody_cli/models/elements/variables/model_variables.py · 8 legacy sites)
  - Main status (2026-11-26): not synced: no committed API report on main; verify_sync fails.
  - Note: usage 30 src / 20 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_variable.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_variable.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_argument_remediation - IRPArgument
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and populated getter fixture matrix row published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 Java getter/setter and COM property type/shapes reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
  - [ ] Section 5 create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
  - [ ] Section 6 irp_argument.md checked/updated.
  - [ ] Section 7 irp_argument.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_attribute_remediation - IRPAttribute
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and six populated getter fixture matrix rows published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 six property names/types and JavaDoc-valid values reconciled.
  - [ ] Section 4 fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
  - [ ] Section 5 create a real attribute attached to a class, set a documented value, and assert each getter returns it.
  - [ ] Section 6 irp_attribute.md checked/updated.
  - [ ] Section 7 irp_attribute.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_argument_remediation - IRPArgument
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and populated getter fixture matrix row published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 Java getter/setter and COM property type/shapes reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
  - [ ] Section 5 create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
  - [ ] Section 6 irp_argument.md checked/updated.
  - [ ] Section 7 irp_argument.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_attribute_remediation - IRPAttribute
  - Main status (2026-11-26): verify_sync passes; 7/8 steps still open.
  - Baseline: 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
  - [ ] Section 1 member checklist and six populated getter fixture matrix rows published.
  - [x] Section 2 canonical wrapper, tests, and exports verified. Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Section 3 six property names/types and JavaDoc-valid values reconciled.
  - [ ] Section 4 fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
  - [ ] Section 5 create a real attribute attached to a class, set a documented value, and assert each getter returns it.
  - [ ] Section 6 irp_attribute.md checked/updated.
  - [ ] Section 7 irp_attribute.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [x] irp_attribute_api_report (IRPAttribute · IRPAttribute · models/elements/variables/model_variables.py · within shared 14)
  - Main status (2026-11-26): verify_sync passes; all steps archived.
  - Note: shares the 14 covered sites with IRPArgument in the same module; `multiplicity`/`declaration`/`defaultValue` properties per catalog.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPAttribute --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAttribute:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
- [x] irp_argument_api_report (IRPArgument · IRPArgument · models/elements/variables/model_variables.py · within shared 14)
  - Main status (2026-11-26): verify_sync passes; all steps archived.
  - Note: shares the 14 covered sites with IRPAttribute in the same module.
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPArgument --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPArgument:` + deviation list-table)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist
