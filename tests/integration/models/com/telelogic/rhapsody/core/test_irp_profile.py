"""Integration tests for IRPProfile with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_profile import IRPProfile
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPProfileIntegration:
    """Integration tests for IRPProfile with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_profile_wraps_registered_class(self, test_project: IRPProject) -> None:
        created = test_project.add_profile(self._unique("Profile"))
        assert isinstance(created, IRPProfile)
        created.delete_from_project()
