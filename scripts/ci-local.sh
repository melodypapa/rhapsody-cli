#!/usr/bin/env bash
# Local equivalent of the CI gate (.github/workflows/python-package.yml).
#
# CI runs ruff, black --check, pytest tests/unit on every job, plus the
# full-tree `mypy src/ tests/` on Python 3.8/3.9 only. A modern local venv
# (3.10+) cannot run that mypy step: mypy type-checks the installed pytest
# package's own source under the 3.9 target and crashes on its pattern-
# matching syntax. This script provisions a real Python 3.9 environment
# (via uv) so the gate runs exactly as CI does — catching full-tree type
# errors BEFORE the push instead of after.
#
# Usage:
#   scripts/ci-local.sh              # run the whole gate
#   scripts/ci-local.sh --setup-only # only provision/check the environment
set -euo pipefail

PYTHON_TARGET="3.9"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv-ci"
PY="$VENV/bin/python"

log() { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }
fail() { printf '\033[1;31mFAILED: %s\033[0m\n' "$*" >&2; exit 1; }

cd "$ROOT"

# ---------------------------------------------------------------- environment
log "Checking environment (Python $PYTHON_TARGET via uv)"
if ! command -v uv >/dev/null 2>&1; then
  fail "uv is required (brew install uv)"
fi

if [ ! -x "$PY" ]; then
  log "Provisioning $VENV"
  uv venv --python "$PYTHON_TARGET" "$VENV"
  uv pip install --python "$PY" -e ".[dev,cli]"
fi

# macOS development stand-in for pywintypes (Windows CI gets the real
# pywin32 module; the unit fakes import only pywintypes.com_error).
if ! "$PY" -c "import pywintypes" >/dev/null 2>&1; then
  log "Installing venv-local pywintypes macOS stub"
  cat > "$VENV/lib/python$PYTHON_TARGET/site-packages/pywintypes.py" <<'STUB'
"""Minimal macOS development stand-in for ``pywintypes`` (venv-local, not committed).

The real ``pywintypes`` ships with pywin32, which installs on Windows only
(see pyproject.toml). Unit tests that run on macOS (``tests/unit/models/fakes.py``)
import only ``pywintypes.com_error``; CI on windows-latest gets the real module.
"""


class com_error(Exception):  # noqa: N818 - mirrors the real pywintypes name
    """Matches pywintypes.com_error's positional signature used by the test fakes."""

    def __init__(self, scode, message=None, excepinfo=None, argerror=None, hresult_error_info=None):
        super().__init__(message if message is not None else f"COM error 0x{scode & 0xFFFFFFFF:08X}")
        self.scode = scode
        self.message = message
        self.excepinfo = excepinfo
        self.argerror = argerror
        self.hresult_error_info = hresult_error_info
STUB
fi

if [ "${1:-}" = "--setup-only" ]; then
  log "Environment ready: $PY"
  "$PY" --version
  exit 0
fi

# ---------------------------------------------------------------- CI gate
log "Lint with ruff (CI: every job)"
"$VENV/bin/ruff" check src/ tests/ || fail "ruff"

log "Format check with black (CI: every job)"
"$VENV/bin/black" --check src/ tests/ || fail "black"

log "Type check with mypy, full tree (CI: 3.8/3.9 jobs only)"
"$VENV/bin/mypy" src/ tests/ || fail "mypy"

log "Unit tests (CI: every job)"
"$PY" -m pytest tests/unit -q || fail "pytest tests/unit"

log "Integration collection (AGENTS offline-verification contract)"
"$PY" -m pytest tests/integration --collect-only -q || fail "integration collect-only"

log "ALL CHECKS PASSED — safe to commit/push"
