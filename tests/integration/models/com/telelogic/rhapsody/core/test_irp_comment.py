"""Integration tests for IRPComment with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_comment import IRPComment
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPCommentIntegration:
    """Integration tests for IRPComment with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_comment_wraps_registered_class(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CommentPkg"))
        try:
            element = pkg.add_new_aggr("Comment", self._unique("Comment"))
            comment = IRPComment(element._com)
            assert isinstance(comment, IRPComment)
            assert comment._com is not None
        finally:
            pkg.delete_from_project()
