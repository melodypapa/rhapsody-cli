# Sync todo — `variables` (group 1 of 1)

**8 classes** · ✅ 2 archived · ⬜ 6 open

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
| 1 | `irp_tag_api_report` | IRPTag | `rhapsody_cli/models/elements/variables/model_variables.py` | 8 | 8 | 1/8 (②) | ⬜ open |
| 2 | `irp_variable_api_report` | IRPVariable | `rhapsody_cli/models/elements/variables/model_variables.py` | 8 | 10 | 1/8 (②) | ⬜ open |
| 3 | `irp_argument_remediation` | IRPArgument | — | — | — | 1/8 (②) | ⬜ open |
| 4 | `irp_attribute_remediation` | IRPAttribute | — | — | — | 1/8 (②) | ⬜ open |
| 5 | `irp_argument_remediation` | IRPArgument | — | — | — | 1/8 (②) | ⬜ open |
| 6 | `irp_attribute_remediation` | IRPAttribute | — | — | — | 1/8 (②) | ⬜ open |
| 7 | `irp_attribute_api_report` | IRPAttribute | `models/elements/variables/model_variables.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 8 | `irp_argument_api_report` | IRPArgument | `models/elements/variables/model_variables.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_tag_api_report</code> · IRPTag · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 37 src / 29 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_variable_api_report</code> · IRPVariable · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 30 src / 20 test refs, 10 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_argument_remediation</code> · IRPArgument · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
- [ ] ① §1 — member checklist and populated getter fixture matrix row published.
- [x] ② §2
- [ ] ③ §3 — Java getter/setter and COM property type/shapes reconciled.
- [ ] ④ §4 — fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
- [ ] ⑤ §5 — create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
- [ ] ⑥ §6 — irp_argument.md checked/updated.
- [ ] ⑦ §7 — irp_argument.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_attribute_remediation</code> · IRPAttribute · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
- [ ] ① §1 — member checklist and six populated getter fixture matrix rows published.
- [x] ② §2
- [ ] ③ §3 — six property names/types and JavaDoc-valid values reconciled.
- [ ] ④ §4 — fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
- [ ] ⑤ §5 — create a real attribute attached to a class, set a documented value, and assert each getter returns it.
- [ ] ⑥ §6 — irp_attribute.md checked/updated.
- [ ] ⑦ §7 — irp_attribute.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_argument_remediation</code> · IRPArgument · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** argumentDirection is a COM property but is exposed by Java-style get_argument_direction()/set_argument_direction() methods; verify_sync.py otherwise passes.
- [ ] ① §1 — member checklist and populated getter fixture matrix row published.
- [x] ② §2
- [ ] ③ §3 — Java getter/setter and COM property type/shapes reconciled.
- [ ] ④ §4 — fake-COM tests first; full unit suite green; irp_argument.py at 100% statements/branches.
- [ ] ⑤ §5 — create a real operation argument, set a JavaDoc-valid direction, and assert the live property value.
- [ ] ⑥ §6 — irp_argument.md checked/updated.
- [ ] ⑦ §7 — irp_argument.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_attribute_remediation</code> · IRPAttribute · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** verify_sync passes; 7/8 steps still open.
- **Baseline:** 6 COM properties are exposed through Java-style getter/setter methods; verify_sync.py otherwise passes.
- [ ] ① §1 — member checklist and six populated getter fixture matrix rows published.
- [x] ② §2
- [ ] ③ §3 — six property names/types and JavaDoc-valid values reconciled.
- [ ] ④ §4 — fake-COM property read/write tests first using properties=; full unit suite green; irp_attribute.py at 100% statements/branches.
- [ ] ⑤ §5 — create a real attribute attached to a class, set a documented value, and assert each getter returns it.
- [ ] ⑥ §6 — irp_attribute.md checked/updated.
- [ ] ⑦ §7 — irp_attribute.rst checked/updated for every public member.
- [ ] ⑧ §8 — generated report, verify_sync, gates, live counts, and blockers recorded.

</details>

<details>
<summary><code>irp_attribute_api_report</code> · IRPAttribute · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** shares the 14 covered sites with IRPArgument in the same module; `multiplicity`/`declaration`/`defaultValue` properties per catalog.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPAttribute --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAttribute:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>

<details>
<summary><code>irp_argument_api_report</code> · IRPArgument · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** shares the 14 covered sites with IRPAttribute in the same module.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPArgument --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPArgument:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>
