# Sync todo — `support` (group 3 of 3)

**7 classes** · ✅ 0 archived · ⬜ 7 open

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
| 1 | `irpascii_file_api_report` | IRPASCIIFile | `rhapsody_cli/models/support/model_files.py` | 0 | 3 | 1/8 (②) | ⬜ open |
| 2 | `irp_code_generator_api_report` | IRPCodeGenerator | `rhapsody_cli/models/support/model_codegen.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 3 | `irpax_view_ctrl_api_report` | IRPAXViewCtrl | `rhapsody_cli/models/support/model_ide.py` | 0 | 2 | 1/8 (②) | ⬜ open |
| 4 | `irp_round_trip_api_report` | IRPRoundTrip | `rhapsody_cli/models/support/model_codegen.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 5 | `irp_external_code_generator_invoker_api_report` | IRPExternalCodeGeneratorInvoker | `rhapsody_cli/models/support/model_codegen.py` | 0 | 1 | 1/8 (②) | ⬜ open |
| 6 | `irp_java_plugins_api_report` | IRPJavaPlugins | `rhapsody_cli/models/support/model_ide.py` | 0 | 0 | 1/8 (②) | ⬜ open |
| 7 | `irp_integrator_api_report` | IRPIntegrator | `rhapsody_cli/models/support/model_codegen.py` | 0 | 0 | 1/8 (②) | ⬜ open |

## Row details

<details>
<summary><code>irpascii_file_api_report</code> · IRPASCIIFile · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 7 src / 5 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `irpascii_file.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_code_generator_api_report</code> · IRPCodeGenerator · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 6 src / 4 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irpax_view_ctrl_api_report</code> · IRPAXViewCtrl · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 6 src / 4 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7 — `irpax_view_ctrl.rst` (anchor + deviation list-table) and toctree entry
- [ ] ⑧ §8

</details>

<details>
<summary><code>irp_round_trip_api_report</code> · IRPRoundTrip · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 5 src / 3 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_external_code_generator_invoker_api_report</code> · IRPExternalCodeGeneratorInvoker · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 5 src / 3 test refs, 1 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_java_plugins_api_report</code> · IRPJavaPlugins · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
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
<summary><code>irp_integrator_api_report</code> · IRPIntegrator · 1/8 steps · ⬜ open</summary>

- **Status (2026-11-26):** not synced: no committed API report on main; verify_sync fails.
- **Note:** usage 4 src / 0 test refs, 0 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
- [ ] ① §1
- [x] ② §2
- [ ] ③ §3
- [ ] ④ §4
- [ ] ⑤ §5
- [ ] ⑥ §6
- [ ] ⑦ §7
- [ ] ⑧ §8

</details>
