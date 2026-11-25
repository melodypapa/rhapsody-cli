# Integration Test Failure Remediation Design

**Date:** 2026-11-25
**Status:** Proposed — pending user review

## Goal

Diagnose and remediate the failing live integration tests as a coherent suite, grouping work by shared root cause rather than fixing tests in isolation. Keep existing passing integration coverage intact and avoid making a broken COM call appear green through broad skips, xfails, or expected-exception assertions.

## Current evidence and baseline

The earlier integration run reported **40 failed, 432 passed**, but it was run before local `main` was synchronized with GitHub. Those counts and its per-interface findings are historical only. After sync to `a3ede5a`, a fresh hidden-UI run was interrupted at approximately 76% by the **ReporterPLUS Wizard: Select Task** dialog. Pytest was terminated and the Rhapsody process launched by that run was closed. Therefore, the current branch has **no complete integration baseline yet**.

Pre-sync checks surfaced potential shared causes—COM authority/runtime disagreement, a model wrapper retaining a generic COM interface, binding argument mismatches, and invalid test preconditions. They must be rechecked against the synchronized code and installed generated binding before any are treated as current defects.

## Proposed workflow

1. **Establish current evidence.** On a freshly launched Rhapsody instance, collect the current integration results and tracebacks. If a modal operation blocks the run, identify the exact test and dialog, stop only the test-launched process, and record the interruption rather than reporting a partial run as a baseline.
2. **Cluster failures by root cause.** Group failures by evidence, including:
   - COM member availability or method/property-shape disagreement between the committed authority and installed generated binding;
   - parameter count/type or incorrect COM interface-pointer forwarding;
   - missing model state, invalid object ownership/type, or non-authentic placeholder data;
   - test-order/shared-session state and GUI/external-tool preconditions.
3. **Validate each cluster against sources.** Use JavaDoc for the model contract, the current pywin32 generated interface for actual COM availability and shape, and wrapper/test source for the data flow. Treat catalog/runtime disagreement as unresolved until reconciled; do not guess or add runtime fallback probing.
4. **Implement shared fixes with TDD.** Add or update focused fake-COM unit tests first for wrapper changes. Update integration fixtures/tests to create real supported objects and relationships, assert populated-state results, restore application/project state, and clean up created elements. Keep each integration assertion within the owning wrapper's contract.
5. **Handle modal/external operations safely.** Replace invalid placeholder arguments with authentic inputs where available. Do not start a report/code-generation/Gateway operation without its documented fixture and preconditions. Do not rerun an operation that blocks the automation server until the cause and safe test path are known. Any truly unavailable live capability remains an explicit blocker unless the user approves a specific skip.
6. **Verify by cluster, then suite.** Run affected unit tests, affected integration tests, the full unit suite, and finally the full integration suite against a fresh Rhapsody process. Compare against the current complete baseline and report exact pass/fail/blocked counts.

## Test and repository constraints

- Preserve all tests that pass in the current baseline; do not delete or weaken them to obtain a green run.
- No broad `pytest.skip`, `xfail`, or assertions that ordinary COM calls raise. The documented `NotImplementedError` contract is the only normal exception assertion for a JavaDoc member confirmed absent from pywin32.
- Use hidden UI only for non-visual cases; it does not guarantee that COM operations are non-modal.
- Follow `AGENTS.md` ownership, project-switch save, authentic-data, getter-population, and cleanup rules.
- Keep the user's existing uncommitted `docs/reports/com/telelogic/rhapsody/core/IRPModelElement_api_report.md` edit untouched and out of this work.
- Work on `feature/integration-test-fixes`; do not commit directly to `main`.

## Acceptance criteria

- A complete current-commit integration baseline is recorded before behavior changes, or any environment blocker preventing one is explicitly documented.
- Every changed COM call is supported by current pywin32 evidence and uses its exact exposed member, shape, and signature.
- All previously passing integration tests remain passing; all fixable baseline failures pass with meaningful live assertions.
- The full unit suite passes, and the final full integration result is recorded. Any remaining failure is a specific evidence-backed blocker, not silently skipped.

## Out of scope

Unrelated wrapper parity work, broad integration-suite redesign, and changes to the user's existing API report edit. Changes to a specific wrapper/report are limited to what the confirmed integration root causes require.
