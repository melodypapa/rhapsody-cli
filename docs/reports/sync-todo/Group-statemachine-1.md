# Sync todo: `statemachine` — `Group-statemachine-1.md`

Category: legacy module subpackage `statemachine` · 2 classes · group 1 of 1 for this category.

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

- [ ] irp_state_api_report (IRPState · RPState · elements/statemachine/model_statemachine.py · 28 legacy sites)
  - Note: highest-use unsynced wrapper (234 src / 99 test references, 48 owned methods). Depends on `RPStateVertex` (stays in the legacy module); inherited members wait for a future base row. Sync after the catalog/report prerequisite above.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate the committed report + catalog entry; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior in the mirrored test path; Windows = live run
  - [ ] Step 6 — §6 SWR update: per-class requirement document `docs/requirements/com/telelogic/rhapsody/core/irp_state.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_state.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit and integration suites (new no-regression rule) + ruff/black/mypy; render the sync-report checklist
- [ ] irp_state_vertex_api_report (IRPStateVertex · RPStateVertex · rhapsody_cli/models/elements/statemachine/model_statemachine.py · 3 legacy sites)
  - Note: usage 29 src / 18 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_state_vertex.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_state_vertex.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy
