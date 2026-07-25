# Two-Level CLI Command Structure with Session Management

**Status:** Approved
**Date:** 2026-07-25
**Author:** Design via brainstorming skill

## Overview

This design adds a two-level command structure to `rhapsody-cli`:
- **Single-level commands**: `connect`, `disconnect`, `status`, `version`
- **Two-level commands**: Existing commands (`project`, `package`, `class`, `attribute`, `operation`, `port`)

Single-level commands manage session state. Two-level commands require a valid session before execution.

## Goals

1. Provide explicit connection lifecycle management via `connect`/`disconnect`
2. Support session timeout with configurable duration
3. Maintain backward compatibility with existing two-level commands
4. Optimize integration tests with session-level connection lifecycle

## Non-Goals

1. Interactive mode (REPL-like) - not in this iteration
2. Multiple concurrent sessions - single session per user
3. Remote Rhapsody instances - only local instances supported

## Command Structure

### Single-Level Commands

```
rhapsody-cli connect [--timeout MINUTES] [--attach-only] [--no-gui]
rhapsody-cli disconnect
rhapsody-cli status
rhapsody-cli version
```

**`connect`:**
- Connect to Rhapsody (attach to existing or launch new instance)
- `--timeout MINUTES`: Override session timeout (default: 5 minutes)
- `--attach-only`: Only attach to existing instance, fail if none running
- `--no-gui`: If launching new instance, keep GUI hidden

**`disconnect`:**
- Disconnect from Rhapsody
- If instance was launched, quit Rhapsody
- If instance was attached, just clear session (don't close user's Rhapsody)

**`status`:**
- Show connection status, instance type, connected time, remaining time
- Show Rhapsody version if connected

**`version`:**
- Show CLI version
- Show Rhapsody version if connected

### Two-Level Commands

Existing commands unchanged:

```
rhapsody-cli project <subcommand> [options]
rhapsody-cli package <subcommand> [options]
rhapsody-cli class <subcommand> [options]
rhapsody-cli attribute <subcommand> [options]
rhapsody-cli operation <subcommand> [options]
rhapsody-cli port <subcommand> [options]
```

**Requirement:** Must have valid session (connected, not timed out) before execution.

## Session Management

### Session File

Location: `~/.rhapsody-cli/session.json`

```json
{
  "connected": true,
  "instance_type": "attached",
  "connected_at": "2026-07-25T10:30:00Z",
  "last_activity": "2026-07-25T10:35:00Z",
  "timeout_minutes": 5
}
```

Fields:
- `connected`: `true` if session is active
- `instance_type`: `"attached"` (existing instance) or `"launched"` (new instance)
- `connected_at`: ISO 8601 timestamp when connection was established
- `last_activity`: ISO 8601 timestamp of last command execution
- `timeout_minutes`: Session timeout duration

### SessionManager Class

Module: `src/rhapsody_cli/session.py`

**Session type:** `TypedDict` with fields matching session file schema (connected, instance_type, connected_at, last_activity, timeout_minutes).

Methods:
- `load() -> Optional[Session]` - Load session from file, return None if not exists
- `save(session: Session) -> None` - Save session to file
- `clear() -> None` - Clear session file
- `is_valid(session: Session) -> bool` - Check if session is valid (connected + not timed out)
- `update_activity(session: Session) -> None` - Update last_activity timestamp

### Timeout Configuration

Priority (highest to lowest):
1. CLI flag: `--timeout MINUTES`
2. Config file: `~/.rhapsody-cli/config.json` → `{"timeout_minutes": 10}`
3. Environment variable: `RHAPSODY_CLI_TIMEOUT=10`
4. Default: 5 minutes

Timeout behavior:
- `timeout = 0`: No timeout (session never expires)
- `timeout < 0`: Invalid, use default (5 minutes)
- Timeout is captured at connect time, stored in session file

### Lazy Timeout Check

- On each command execution, `SessionManager.is_valid()` checks `last_activity`
- If `now - last_activity > timeout_minutes`, session is invalid
- Invalid session → raise `CliExecutionError("Session timed out. Please connect again.")`
- No background thread needed

## Architecture

### Current Architecture

```
AbstractAction
  └── RhapsodyContextAction (connects lazily via _connect_app())
        └── ProjectOpenAction, PackageCreateAction, etc.
```

### New Architecture

```
AbstractAction
  └── RhapsodyContextAction (modified)
        └── SessionAwareAction (new) - checks session before execution
              └── All element actions (Project, Package, Class, etc.)
```

### SessionAwareAction Class

Location: `src/rhapsody_cli/actions/abstract_action.py`

Behavior:
```python
def execute(self, args: argparse.Namespace) -> None:
    session_manager = SessionManager()
    session = session_manager.load()
    if not session or not session_manager.is_valid(session):
        raise CliExecutionError("Not connected. Run 'rhapsody-cli connect' first.")
    session_manager.update_activity(session)
    super().execute(args)
```

All existing actions change parent class from `RhapsodyContextAction` to `SessionAwareAction`.

### CLI Dispatch

Location: `src/rhapsody_cli/cli/cli.py`

Changes:
1. Add single-level command dispatch before two-level command dispatch
2. Single-level commands: `connect`, `disconnect`, `status`, `version`
3. Two-level commands: existing command groups

```python
def main() -> None:
    # ... existing code ...

    # Single-level commands
    if command_name == "connect":
        cmd = ConnectCommand(command_args)
    elif command_name == "disconnect":
        cmd = DisconnectCommand(command_args)
    elif command_name == "status":
        cmd = StatusCommand(command_args)
    elif command_name == "version":
        cmd = VersionCommand(command_args)
    # Two-level commands (existing)
    elif command_name == "project":
        cmd = ProjectCommand(command_args)
    # ... rest of existing commands ...
```

## Error Handling

### Session File Errors

| Scenario | Behavior |
|----------|----------|
| Session file malformed (invalid JSON) | Log warning, treat as no session, require `connect` |
| Session directory doesn't exist | Create on first `connect` |
| Session file doesn't exist | Treat as no session |

### Connection Errors

| Scenario | Behavior |
|----------|----------|
| Not connected | Error: "Not connected. Run 'rhapsody-cli connect' first." |
| Session timed out | Error: "Session timed out after X minutes. Please connect again." |
| Rhapsody not running | Error: "Rhapsody is not running. Please start Rhapsody and connect again." |
| Already connected | Info: "Already connected to Rhapsody (instance type: attached/launched)" |

### Disconnect Errors

| Scenario | Behavior |
|----------|----------|
| Not connected | Info: "Not connected" |
| Rhapsody busy | Log warning, clear session, user can manually close |

### Timeout Edge Cases

| Scenario | Behavior |
|----------|----------|
| Timeout = 0 | No timeout (session never expires) |
| Timeout < 0 | Invalid, use default (5 minutes) |
| Timeout config change | Doesn't affect existing session (use value at connect time) |

## File Structure

### New Files

```
src/rhapsody_cli/
├── session.py                          # SessionManager class
└── actions/
    └── session_action.py               # ConnectAction, DisconnectAction, StatusAction, VersionAction

tests/unit/
├── test_session.py                     # SessionManager tests
└── actions/
    └── test_session_action.py          # Session action tests
```

### Modified Files

```
src/rhapsody_cli/
├── actions/
│   ├── abstract_action.py              # Add SessionAwareAction class
│   ├── project_action.py               # Change parent to SessionAwareAction
│   ├── package_action.py               # Change parent to SessionAwareAction
│   ├── class_action.py                 # Change parent to SessionAwareAction
│   ├── attribute_action.py             # Change parent to SessionAwareAction
│   ├── operation_action.py             # Change parent to SessionAwareAction
│   └── port_action.py                  # Change parent to SessionAwareAction
└── cli/
    └── cli.py                          # Add single-level command dispatch
```

### User Files (Created at Runtime)

```
~/.rhapsody-cli/
├── session.json                        # Session state
└── config.json                         # Optional config file
```

## Testing

### Unit Tests

**SessionManager tests** (`tests/unit/test_session.py`):
- `test_load_no_session` - returns None when file doesn't exist
- `test_load_valid_session` - loads valid session
- `test_load_corrupted_session` - handles malformed JSON
- `test_save_session` - saves session to file
- `test_clear_session` - clears session file
- `test_is_valid_connected` - returns True for connected, not timed out
- `test_is_valid_timed_out` - returns False for timed out session
- `test_is_valid_disconnected` - returns False for disconnected session
- `test_update_activity` - updates last_activity timestamp

**Session action tests** (`tests/unit/actions/test_session_action.py`):
- `test_connect_new_session` - creates new session
- `test_connect_already_connected` - informs user already connected
- `test_connect_attach_only` - attaches to existing instance
- `test_connect_launch_new` - launches new instance
- `test_disconnect_launched_instance` - quits Rhapsody if launched
- `test_disconnect_attached_instance` - clears session only if attached
- `test_disconnect_not_connected` - informs user not connected
- `test_status_connected` - shows connection info
- `test_status_not_connected` - shows not connected
- `test_version` - shows CLI version

### Test Migration

**Challenge:** Existing tests don't set up session state.

**Solution:** Auto-use fixture in `tests/conftest.py`:

```python
@pytest.fixture(autouse=True)
def mock_session(tmp_path, monkeypatch):
    """Auto-use fixture: provide valid session for all tests."""
    session_file = tmp_path / ".rhapsody-cli" / "session.json"
    session_file.parent.mkdir(parents=True, exist_ok=True)
    session_file.write_text(json.dumps({
        "connected": True,
        "instance_type": "attached",
        "connected_at": "2026-07-25T10:00:00Z",
        "last_activity": "2026-07-25T10:30:00Z",
        "timeout_minutes": 5
    }))
    monkeypatch.setattr(SessionManager, "SESSION_DIR", tmp_path / ".rhapsody-cli")
```

**Benefits:**
- Minimal changes to existing tests (auto-use fixture)
- Tests session check logic
- No test-specific code paths in production code

### Integration Tests

**Optimized flow:** Connect once, run many operations, disconnect at end.

```python
# tests/integration/conftest.py
@pytest.fixture(scope="session")
def rhapsody_session():
    """Connect once for entire test session, disconnect at end."""
    session_manager = SessionManager()
    app = RhapsodyApplication.connect()
    session_manager.save(Session(
        connected=True,
        instance_type="launched",
        connected_at=datetime.now().isoformat(),
        last_activity=datetime.now().isoformat(),
        timeout_minutes=30
    ))
    yield app
    session_manager.clear()
    app.quit()
```

**Benefits:**
- Performance: Connect once, run many operations
- Realistic: Mimics real user workflow
- Tests session persistence across commands

## Implementation Notes

### Dependencies

No new dependencies required. Uses existing:
- `RhapsodyApplication.connect()` / `quit()`
- `argparse` for CLI parsing
- `json` for session file I/O

### Breaking Changes

**Behavior change:** Existing commands now require `connect` before execution.

**Migration guide for users:**
```bash
# Before (old behavior)
rhapsody-cli project open MyProject.rpy  # Works without connect

# After (new behavior)
rhapsody-cli connect                      # Required first
rhapsody-cli project open MyProject.rpy  # Then run commands
rhapsody-cli disconnect                  # Optional cleanup
```

### Future Enhancements

1. **Interactive mode:** Add REPL-like session with persistent connection
2. **Multiple sessions:** Support connecting to multiple Rhapsody instances
3. **Remote connections:** Support connecting to Rhapsody on remote machines
4. **Session sharing:** Share session between multiple CLI instances

## References

- [AGENTS.md](../../AGENTS.md) - Project conventions
- [application.py](../../src/rhapsody_cli/application.py) - RhapsodyApplication class
- [abstract_action.py](../../src/rhapsody_cli/actions/abstract_action.py) - Current action architecture