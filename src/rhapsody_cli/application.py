"""RhapsodyApplication: the entry point for connecting to IBM Rhapsody.

The connection lifecycle (attach/launch/connect/disconnect) lives here; every
COM member of the ``IRPApplication`` interface lives on the canonical wrapper
:class:`rhapsody_cli.models.com.telelogic.rhapsody.core.IRPApplication`, which
this facade subclasses.
"""

from typing import Any

try:
    import win32com.client as win32_client
except ImportError:  # pragma: no cover - pywin32 is Windows-only
    # pywin32 is only installed on Windows (see pyproject.toml). Importing
    # this module must still succeed on other platforms (e.g. Sphinx
    # autodoc running on Read the Docs' Linux build image); the COM calls
    # themselves will simply fail at runtime with a clear error instead.
    win32_client = None

from rhapsody_cli import com_utils
from rhapsody_cli.exceptions import RhapsodyConnectionError, RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication

_PROG_ID = "Rhapsody2.Application.1"


class RhapsodyApplication(IRPApplication):
    """Connects to the Rhapsody application and exposes its COM surface.

    Subclasses the canonical :class:`IRPApplication` wrapper: all COM members
    (``get_version``, ``open_project``, ``get_projects``, ...) are inherited
    from it; this facade adds only the connection lifecycle
    (:meth:`connect`, :meth:`disconnect`) that selects attach-vs-launch
    behaviour — pure Python orchestration with no COM member of its own.
    """

    def __init__(self, com_obj: Any) -> None:
        """Initialize with a COM object representing IRPApplication.

        Args:
            com_obj: The COM object returned by GetActiveObject or Dispatch.
        """
        super().__init__(com_obj)

    @classmethod
    def _attach(cls) -> "RhapsodyApplication":
        """Attach to an already-running Rhapsody instance (internal helper).

        Returns:
            A RhapsodyApplication wrapping the active COM object.

        Raises:
            RhapsodyConnectionError: If pywin32 is unavailable or no running
                Rhapsody instance can be found.
        """
        if win32_client is None:
            raise RhapsodyConnectionError("pywin32 is not available; Rhapsody automation requires Windows.")
        try:
            com_obj = com_utils.call_com(lambda: win32_client.GetActiveObject(_PROG_ID))
        except RhapsodyRuntimeException as exc:
            raise RhapsodyConnectionError(f"No running Rhapsody instance found: {exc}") from exc
        return cls(com_obj)

    @classmethod
    def _launch(cls) -> "RhapsodyApplication":
        """Launch a new Rhapsody instance (internal helper).

        Returns:
            A RhapsodyApplication wrapping the newly launched COM object.

        Raises:
            RhapsodyConnectionError: If pywin32 is unavailable or launching
                Rhapsody fails.
        """
        if win32_client is None:
            raise RhapsodyConnectionError("pywin32 is not available; Rhapsody automation requires Windows.")
        try:
            com_obj = com_utils.call_com(lambda: win32_client.Dispatch(_PROG_ID))
        except RhapsodyRuntimeException as exc:
            raise RhapsodyConnectionError(f"Failed to launch Rhapsody: {exc}") from exc
        return cls(com_obj)

    @classmethod
    def connect(cls, attach_only: bool = False, show_gui: bool = True) -> "RhapsodyApplication":
        """Connect to Rhapsody, trying attach first with fallback to launch.

        Args:
            attach_only: If True, only try to attach to a running instance.
                Raises RhapsodyConnectionError if no instance is running.
            show_gui: When a new instance is launched, controls whether its
                GUI window is visible. Ignored when attaching to a running
                instance.

        Returns:
            A RhapsodyApplication wrapping the connected COM object.
        """
        try:
            return cls._attach()
        except RhapsodyConnectionError:
            if attach_only:
                raise
        app = cls._launch()
        if show_gui:
            app.set_hidden_ui(False)
        return app

    def disconnect(self) -> None:
        """Disconnect from Rhapsody. Calls quit() and provides a cleanup hook."""
        self.quit()
