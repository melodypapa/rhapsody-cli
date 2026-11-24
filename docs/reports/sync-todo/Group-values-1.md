# Sync todo: `values` — `Group-values-1.md`

Category: legacy module subpackage `values` · 5 classes · group 1 of 1 for this category.

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

- [ ] irp_literal_specification_api_report (IRPLiteralSpecification · RPLiteralSpecification · rhapsody_cli/models/elements/values/model_values.py · 2 legacy sites)
  - Note: usage 17 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_literal_specification.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_literal_specification.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_instance_specification_api_report (IRPInstanceSpecification · RPInstanceSpecification · rhapsody_cli/models/elements/values/model_values.py · 0 legacy sites)
  - Note: usage 13 src / 10 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_instance_specification.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_instance_specification.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_instance_slot_api_report (IRPInstanceSlot · RPInstanceSlot · rhapsody_cli/models/elements/values/model_values.py · 0 legacy sites)
  - Note: usage 14 src / 9 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_instance_slot.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_instance_slot.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_instance_value_api_report (IRPInstanceValue · RPInstanceValue · rhapsody_cli/models/elements/values/model_values.py · 0 legacy sites)
  - Note: usage 17 src / 5 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_instance_value.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_instance_value.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
- [ ] irp_value_specification_api_report (IRPValueSpecification · RPValueSpecification · rhapsody_cli/models/elements/values/model_values.py · 0 legacy sites)
  - Note: usage 12 src / 4 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/` Bulk package move 2026-11-24: wrapper + mirrored tests moved to `models/com/telelogic/rhapsody/core/`, `RP*` renamed to `IRP*`, all imports rewritten, no compatibility shim; unit suite 2157 passed, ruff/black clean.
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_value_specification.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_value_specification.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
