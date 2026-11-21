---
name: rhapsody-sync
description: "Sync Rhapsody Python wrappers against JavaDoc. Use for IRP* method parity, pywin32/COM mismatches, Java-derived Python package paths, or RST deviation docs—even when the user says 'bring IRPClass up to date' rather than 'sync'. Do not use for read-only API questions, CLI usage, user-guide edits, or unrelated code. Handle one interface per run and create a class-specific TODO list."
license: MIT
author: rhapsody-cli maintainers
repository: https://github.com/melodypapa/rhapsody-cli
version: 0.1.0
product-version: 0.1.0
spec-version: 1.0.0
keywords: [rhapsody, javadoc, com, api-sync, python]
agents: [pi]
---

# Rhapsody API sync

Sync one requested Java API interface with its Python wrapper in this project. The input is the JavaDoc interface name (such as `IRPClass`), not a hard-coded Python class. The Python class keeps the same name as the Java interface, so treat `IRPClass` as the example pattern, never as the default target.

## 1. Create the sync TODO list

Before any analysis or edit, publish the TODO list: use an available task-list tool, otherwise show the Markdown checklist in the response. Keep the shared steps concise, then add a subtask for every target-owned JavaDoc member so no method is silently skipped:

```markdown
## Sync TODO — IRPClass (`com.telelogic.rhapsody.core`)
- [ ] §2 Resolve JavaDoc package, class description, and member inventory; move wrapper + tests to the canonical package.
- [ ] §3 Compare every owned member across JavaDoc, COM exposure, and Python implementation.
- [ ] §4 Write/upgrade the fake-COM unit tests first (red), then migrate the binding call sites (green).
- [ ] §5 Add/update integration tests in the mirrored test package.
- [ ] §6 Update the class requirement document (per-class, package path).
- [ ] §7 Update the class RST page (per-class, package path) and list each verified deviation.
- [ ] §8 Run validation (unit suite, gate, validate_interface, verify_sync); summarize unresolved items.
- [ ] Render this checklist as the final sync report.
- [ ] Member: addExample() — [ ] JavaDoc [ ] COM [ ] wrapper [ ] disposition
```

This checklist is the run's live report. Tick a checkbox in the same response where its evidence lands — a command result, a test count, a documented disposition — and never batch-tick at the end. A box ends the run either ticked or open with the blocker and reason stated next to it. Only mark a task done after checking its evidence. Keep inherited-member notes separate from owned-member tasks.

## 2. Resolve the target and move to the canonical package

If the interface name is missing or ambiguous, ask for it before editing. Find its JavaDoc in `docs/java_api/`, read the declared package, then resolve the matching wrapper, base class, tests, and current exports. Do not infer the Java package or wrapper mapping from the existing Python folder alone.

The canonical Python package mirrors every Java package segment beneath `rhapsody_cli.models`, and the Python class name matches the Java interface name. For example:

- Java: `com.telelogic.rhapsody.core.IRPClass`
- Python import: `from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass`
- Directory: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py`

Move the wrapper only if it is not already in the canonical package. Add package `__init__.py` exports, preserve registration/import side effects, and update every internal reference to the canonical import. Keep the existing module naming convention where practical. Do not leave a compatibility shim at the old path for the migrated interface. Migrate only the requested interface; avoid unrelated package moves and refactors. If moving it safely requires broad changes or would break public imports, stop and ask before expanding scope.

Both unit and integration tests move with it, mirroring the canonical package segment by segment. Use snake_case for the test module name derived from the Java interface (`IRPClass` → `test_irp_class.py`), and add `__init__.py` at every mirrored directory level. For example:

- Unit test: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_class.py`
- Integration test: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py`

Do not leave the class's tests under an old domain folder such as `tests/unit/models/elements/classifiers/`.

## 3. Compare evidence efficiently, without skipping coverage

Run the skill-local wrapper once for a baseline and use its report as the member-by-member index:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
```

The helper locates the project root and delegates to the canonical `scripts/validate_model_api.py`; it does not duplicate that logic. A nonzero exit of `1` means actionable deviations were found, not that validation crashed. A nonzero exit of `2` is a setup failure: missing JavaDoc, or offline validation without COM evidence. On Windows with Rhapsody available, use `--source typelib` to inspect the registered binding. Without Rhapsody, the COM evidence is the committed report pair `docs/reports/<INTERFACE>_api_report.md` plus `docs/reports/pywin32_authority.json`, and the helper exits with a blocker when that evidence is missing. If the committed report exists but the catalog lacks the interface, rebuild the catalog from the committed reports with `python scripts/pywin32_authority.py --source reports` (on Windows you may instead regenerate from the live binding with `--source typelib`) and commit the refreshed JSON. If the committed report does not exist, exit the sync: with neither Rhapsody nor a committed report there is no COM evidence to compare against — record the missing report as the blocker on the corresponding TODO and stop; do not edit wrapper code, tests, or docs on unverifiable evidence. The current repository validator is hard-coded to Java package `com.telelogic.rhapsody.core`; if the selected JavaDoc declares another package, the helper stops rather than generating a misleading report.

Use these sources for different questions:

| Source | Trust it for | Do not infer |
| --- | --- | --- |
| JavaDoc HTML | Declared package, Java API, signatures, descriptions | That COM exposes a callable member |
| pywin32 catalog/type library | COM member presence and method/property shape | The complete Java contract or wrapper behavior |
| Python wrapper | Actual facade, COM calls, conversions, and return wrapping | That an absent wrapper is intentionally unsupported |

Reconcile every member declared by the target interface against the validator inventory. To save time, inspect implementation bodies and secondary references deeply for deviations, missing coverage, unsupported members, and code you will change; do not reread unrelated wrappers or inherited implementations. Check JavaDoc descriptions for the class and each method being added or changed. If evidence conflicts, record the sources and ask rather than guessing.

For each target-owned JavaDoc member, track: Java name/signature and description; inherited vs owned; COM method/property/alias/unavailable status; Python method and actual COM call; result type/wrapping; and a disposition. Use concise dispositions such as matched, inherited, intentional facade helper, binding mismatch, JavaDoc-only, COM-only, missing wrapper, intentionally unsupported, or unresolved.

Never add a direct COM call for a member absent from the binding. Keep exact camelCase COM identifiers and snake_case Python names. Follow `AGENTS.md` for `call_com`, property helpers, argument unwrapping, result wrapping, collection handling, annotations, and exception handling. In particular, do not add `Any` or `from __future__ import annotations`.

Bindings are pywin32-authoritative: every wrapper member depends on exactly one pywin32-exposed COM member, with no runtime name probing or Java-name fallback. Method-shaped members are called with `call_com(lambda: self._com.Name(...))`; property-shaped members are read/written with `get_com_property` / `set_com_property` (name confirmed against `docs/reports/pywin32_authority.json`). Legacy dual-binding call sites (`_get_method_or_property` / `_set_method_or_property`) are migrated as part of the sync — see section 4.

## 4. Write the unit tests first (TDD)

Follow TDD: write or update a focused fake-COM unit test before changing behavior or import wiring. Unit tests must not use real COM. For each wrapper method added or changed, use JavaDoc for its description, arguments, and return contract while retaining project-specific usage notes and known runtime limitations.

**Migrate legacy binding call sites for this class.** For every `_get_method_or_property` / `_set_method_or_property` call in the class's **own** methods: look up the pywin32 member for that operation in `docs/reports/pywin32_authority.json`, then rewrite the site to a direct call — method-shaped → `call_com(lambda: self._com.Name(...))`, property-shaped → `get_com_property` / `set_com_property` — and update the class's unit tests to configure and assert on that single member (fakes use the `properties=` channel of `make_fake_element` for property-shaped members). Inherited members keep base-class behavior until the base class's own sync run. If a call site's member is absent from the catalog for this interface, record it as a blocker and leave the site unchanged — do not migrate on unverifiable evidence.

Run the full unit suite after the change and fix any failure before continuing; never advance to the next step with a failing unit test (verification rules in section 8).

## 5. Update the integration tests

Add or update integration coverage only for supported behavior owned by this wrapper; inherited methods may set up fixtures but are not child assertions. Respect the integration-test ownership rules in `AGENTS.md`, including child overrides with different return contracts. Integration tests live in the mirrored test path from section 2 — do not leave them under an old domain folder.

## 6. Update the class requirement document

Create or update the class's own requirement file at
`docs/requirements/<java.package.path>/<snake_case>.md` — the same package path as the
wrapper (for example `docs/requirements/com/telelogic/rhapsody/core/irp_class.md` for
`IRPClass`). Use the JavaDoc class description for the summary, but retain project-specific
requirements and implementation facts that JavaDoc cannot express. Keep the existing SWR
entry format (`ID`, `Title`, `Status`, `Priority`, `Description`, `Implementation`,
`Last Changed`); the `ID` stays stable when the entry moves. When migrating a class out of
the legacy monolith `docs/requirements/swr_elem_requirements.md`, move its entry into the
per-class file — do not duplicate it; leave unrelated and not-yet-migrated entries in the
monolith until their own sync run moves them.

## 7. Update the class RST document

Create or update the class's API page at `docs/api/<java.package.path>/<snake_case>.rst` —
for example `docs/api/com/telelogic/rhapsody/core/irp_class.rst` for `IRPClass`. Start the
page with the verifier-recognized anchor `.. _rhapsody-java-interface-<INTERFACE>:` and
include the Java interface, Java package, JavaDoc-derived description, Python wrapper, and
canonical import path. Promote the class heading to the page title.

List each verified deviation between JavaDoc, COM/pywin32, and Python implementation in a
valid reStructuredText `list-table` with headers `JavaDoc member/signature`,
`COM/pywin32 exposure`, `Python implementation`, and `Deviation and treatment`. Include
method-vs-property shape and evidence-backed resolution; if there are no deviations, say so
explicitly. The verifier checks that the page contains every member reported by the API
validator. Keep the page reachable by listing it in `docs/api/elements.rst`'s toctree under
the Java package heading (one entry per synced class). When migrating a class out of the
legacy `elements.rst` sections, move its section — do not duplicate it; leave unrelated and
not-yet-migrated classes unchanged. Keep RST navigation valid.

## 8. Verify and report

After edits, run final validation and artifact checks:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>
python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q
```

`verify_sync.py` checks Java-package-derived wrapper placement, the class requirement entry, and the RST anchor/table coverage against the generated report. An exit code of `1` lists incomplete or mismatched artifacts. Also run import/registration checks, relevant lint/type checks, and RST/Sphinx validation when available.

Verification rules:

- **Unit tests must pass all the time.** Run the full unit suite after every change and fix any failure before continuing; never finish a sync with a failing unit test.
- **On Windows, integration tests must pass.** If the current environment is Windows, run the migrated class's focused integration test with live Rhapsody and require a green result. Collection-only is not a live test. If Rhapsody is not available on Windows, report the blocker and leave the corresponding TODO open rather than claiming success.
- On non-Windows environments, integration tests may be collection-only; state that explicitly in the report.

Leave TODO items open when blocked, with the reason.

Finish by rendering the TODO checklist as the sync report: every shared step ticked with its key evidence (command result, test counts, files changed) or left open with the blocker and reason next to it, and every member line showing its final disposition. Lead the report with the Java interface/package, the old and canonical Python paths, and the files changed, followed by the completed checklist. Sync one interface per run; complete and review it before starting another.
