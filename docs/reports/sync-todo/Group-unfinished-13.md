# Sync todo: `docs/reports` — `Group-unfinished-13` (IRPExtensionPoint → IRPIntegrator)

Baseline: 2026-11-22 inventory of unsynced wrapper classes. 3 open rows · ordered by
importance (usage in `src/` then `tests/`, legacy cleanup value and owned surface). All
higher-importance classes are already queued in Group-unfinished-1/2 or archived in
Group-finished.md.

(Resume = first row still `[ ]`; archive to [Group-finished.md](Group-finished.md) only when all
eight steps are `[x]` and its commit exists.)

## Prerequisites

None of these interfaces has a committed API report or a catalog entry yet. Regenerate both on
Windows with Rhapsody before Step 3 (see Group-unfinished-2.md). JavaDoc is available locally at
`docs/java_api/com/telelogic/rhapsody/core/<IFACE>.html`. Never migrate a catalog-absent member.

Steps = SKILL.md §1–§8; canonical package and mirrored test paths as in Group-unfinished-2.md.

Prerequisite for every row: regenerate API report + catalog entry before §3.

- [ ] irp_extension_point_api_report (IRPExtensionPoint · RPExtensionPoint · rhapsody_cli/models/elements/classifiers/model_usecase.py · 0 legacy sites)
  - Note: usage 6 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_extension_point.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_extension_point.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_java_plugins_api_report (IRPJavaPlugins · RPJavaPlugins · rhapsody_cli/models/support/model_ide.py · 0 legacy sites)
  - Note: usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_java_plugins.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_java_plugins.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_integrator_api_report (IRPIntegrator · RPIntegrator · rhapsody_cli/models/support/model_codegen.py · 0 legacy sites)
  - Note: usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_integrator.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_integrator.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

