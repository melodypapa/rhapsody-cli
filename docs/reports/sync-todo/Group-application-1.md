# Sync todo: `application` — `Group-application-1.md`

Category: legacy module subpackage `application` · 1 classes · group 1 of 1 for this category.

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

- [x] irp_application_api_report (IRPApplication · RhapsodyApplication · application.py · 3 sites)
  - Note: `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`tests/unit/test_application.py`), then migrate the 3 sites; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
  - [x] Step 8 — §8 verify and report (re-verified 2026-11-25: 0/0/0 deviations; 13 COM-property members exposed as `@property` with `documented_aliases`; `validate_interface.py IRPApplication --source authority` exits 0, `verify_sync.py IRPApplication` exits 0; focused unit file 197 passed, coverage 424 statements/358 branches, 100.00%; full unit suite 2168 passed; skill harness 49 passed; focused live integration 69 passed / 0 failed, full live integration 444 passed / 0 failed on a fresh hidden-UI instance; ruff/black/mypy ✓; integration layer has no coverage gate per §4)
