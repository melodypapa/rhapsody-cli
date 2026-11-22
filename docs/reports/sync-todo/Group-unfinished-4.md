# Sync todo: `docs/reports` — `Group-unfinished-4` (IRPVariable → IRPEventReception)

Baseline: 2026-11-22 inventory of unsynced wrapper classes. 10 open rows · ordered by
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

- [ ] irp_variable_api_report (IRPVariable · RPVariable · rhapsody_cli/models/elements/variables/model_variables.py · 8 legacy sites)
  - Note: usage 30 src / 20 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_variable.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_variable.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_matrix_view_api_report (IRPMatrixView · RPMatrixView · rhapsody_cli/models/elements/graphics/model_graphics.py · 7 legacy sites)
  - Note: usage 31 src / 8 test refs, 19 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_matrix_view.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_matrix_view.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_classifier_role_api_report (IRPClassifierRole · RPClassifierRole · rhapsody_cli/models/elements/common/model_other_model.py · 1 legacy sites)
  - Note: usage 34 src / 13 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_classifier_role.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_classifier_role.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_table_view_api_report (IRPTableView · RPTableView · rhapsody_cli/models/elements/graphics/model_graphics.py · 7 legacy sites)
  - Note: usage 29 src / 9 test refs, 17 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_table_view.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_table_view.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

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

- [ ] irp_dependency_api_report (IRPDependency · RPDependency · rhapsody_cli/models/elements/relations/model_dependency.py · 2 legacy sites)
  - Note: usage 33 src / 13 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_dependency.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_dependency.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_stereotype_api_report (IRPStereotype · RPStereotype · rhapsody_cli/models/elements/classifiers/model_stereotype.py · 3 legacy sites)
  - Note: usage 30 src / 15 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_stereotype.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_stereotype.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_connector_api_report (IRPConnector · RPConnector · rhapsody_cli/models/elements/graphics/model_graphics.py · 1 legacy sites)
  - Note: usage 29 src / 13 test refs, 16 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_connector.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_connector.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_node_api_report (IRPNode · RPNode · rhapsody_cli/models/elements/containment/model_node.py · 2 legacy sites)
  - Note: usage 30 src / 13 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_node.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_node.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_event_reception_api_report (IRPEventReception · RPEventReception · rhapsody_cli/models/elements/interactions/model_interactions.py · 2 legacy sites)
  - Note: usage 32 src / 12 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_event_reception.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_event_reception.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

