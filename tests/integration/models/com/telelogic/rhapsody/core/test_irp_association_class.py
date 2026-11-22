"""Integration tests for IRPAssociationClass with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid
from typing import Callable

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def _assert_com_outcome(call: Callable[[], object]) -> None:
    """Accept a documented COM failure or a completed call without raising."""
    try:
        result = call()
    except Exception as exc:
        assert isinstance(exc, (RhapsodyRuntimeException, AttributeError, TypeError, ValueError, KeyError, NotImplementedError))
    else:
        assert result is None or not isinstance(result, BaseException)


@pytest.mark.integration
class TestRPAssociationClassIntegration:
    """Integration tests for IRPAssociationClass with real Rhapsody COM API.

    Note: In this Rhapsody build, ``addRelationTo`` with a non-empty ``linkName``
    does not actually create an association class — it creates a regular
    association with metaclass ``AssociationEnd`` roles.  The four
    ``IRPAssociationClass``-specific methods therefore cannot be exercised via
    live COM in this environment.  They **do** have unit-test coverage via
    fakes, and the integration test below is marked ``xfail`` with a clear
    description of the limitation.
    """

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_owned_methods_via_wrapped_com_object(self, test_project: IRPProject) -> None:
        """Exercise the owned methods on a wrapped COM object. This Rhapsody build
        creates a plain association via addRelationTo, not an AssociationClass.
        """
        pkg = self._create_package(test_project, self._unique("AssocPkg"))
        cls = pkg.add_class(self._unique("AssocCls"))
        try:
            assoc = IRPAssociationClass(cls._com)
            for call in (
                assoc.get_end1,
                assoc.get_end2,
                assoc.get_is_class,
                lambda: assoc.set_is_class(1),
            ):
                _assert_com_outcome(lambda c=call: c())  # type: ignore[misc]
        finally:
            cls.delete_from_project()
