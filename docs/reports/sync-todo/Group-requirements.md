# Sync todo — `requirements`

**2 classes** · ✅ 1 archived · ⬜ 1 open

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
| 1 | `irp_annotation_api_report` | IRPAnnotation | `rhapsody_cli/models/elements/requirements/model_requirements.py` | 8 | 10 | 1/8 (②) | ⬜ open |
| 2 | `irp_requirement_api_report` | IRPRequirement | `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirement.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_annotation_api_report</code> · IRPAnnotation · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 20 src / 15 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_requirement_api_report</code> · IRPRequirement · 8/8 steps · ✅ archived</summary>

- **Status (2026-03-19):** `IRPRequirement` sync is archived; validator reports 0 actionable deviations and strict getter verification passes. No live blocker remains for this class.
- **Note:** the JavaDoc getter/setter pair maps to the pywin32 read/write `requirementID` property and one Python `requirement_id` property. `IRPRequirement.__init__` casts generic factory dispatches to the exact interface; the sibling `IRPAnnotation` remains in its own open sync row.
- [x] ① §1 — documented both JavaDoc accessors and the single pywin32 property mapping.
- [x] ② §2 — canonical `irp_requirement.py` and mirrored per-class tests; package exports and registration updated.
- [x] ③ §3 — validator reports 0 actionable deviations after aligning the property shape and exact interface cast.
- [x] ④ §4 — TDD red/green; unit module has 7 tests and 100% statement/branch coverage; full unit suite 2322 passed.
- [x] ⑤ §5 — focused live requirement-ID round-trip passes (1 passed) with a real package-created requirement.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_requirement.md` holds SWR_ELEM_00010.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_requirement.rst` is linked from `docs/api/elements.rst`.
- [x] ⑧ §8 — `verify_sync.py IRPRequirement --strict-getters`, skill harness (90 passed), full unit suite (2322 passed), focused integration (1 passed), Ruff, Black, and mypy pass. Sphinx is unavailable in this environment (`No module named sphinx`).

</details>
