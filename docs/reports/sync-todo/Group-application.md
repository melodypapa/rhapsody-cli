# Sync todo — `application`

**1 classes** · ✅ 1 archived · ⬜ 0 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

## Step legend

| Step | Meaning |
| --- | --- |
| ① §1 | publish the per-run checklist with a subtask per target-owned JavaDoc member |
| ② §2 | resolve the wrapper, inheritance, exports, and tests; move to the canonical package |
| ③ §3 | reconcile every owned member against JavaDoc, pywin32, and the Python wrapper |
| ④ §4 | failing fake-COM unit tests first, then migrate the legacy sites |
| ⑤ §5 | integration coverage on the mirrored path; live run on Windows |
| ⑥ §6 | update the per-class requirement document |
| ⑦ §7 | update the per-class RST page and its toctree entry |
| ⑧ §8 | run the validator, `verify_sync.py`, skill tests, both suites, and the quality gate |

`[x] §2` on every row records the 2026-11-24 bulk package move; other steps show their evidence inline when it differs from the legend.

## At a glance

| # | Class | Interface | Legacy source | Sites | Owned | Steps | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `irp_application_api_report` | IRPApplication | `application.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_application_api_report</code> · IRPApplication · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
- [x] ① §1
- [x] ② §2 — locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
- [x] ③ §3 — baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
- [x] ⑧ §8 — 0/0/0 deviations; 13 COM-property members exposed as `@property` with `documented_aliases`; `validate_interface.py IRPApplication --source authority` exits 0, `verify_sync.py IRPApplication` exits 0; focused unit file 197 passed, coverage 424 statements/358 branches, 100.00%; full unit suite 2168 passed; skill harness 49 passed; focused live integration 69 passed / 0 failed, full live integration 444 passed / 0 failed on a fresh hidden-UI instance; ruff/black/mypy ✓; integration layer has no coverage gate per §4)

</details>
