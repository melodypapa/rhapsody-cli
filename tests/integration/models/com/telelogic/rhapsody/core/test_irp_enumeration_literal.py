"""Integration tests for IRPEnumerationLiteral with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_enumeration_literal import IRPEnumerationLiteral
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType


@pytest.mark.integration
class TestIRPEnumerationLiteralIntegration:
    """Integration tests for IRPEnumerationLiteral with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _literal(pkg: IRPPackage) -> tuple[IRPPackage, IRPEnumerationLiteral]:
        type_element = IRPType(pkg.add_type(f"Enum_{uuid.uuid4().hex[:8]}")._com)
        type_element.kind = "Enumeration"
        literal = type_element.add_enumeration_literal(f"Literal_{uuid.uuid4().hex[:8]}")
        assert isinstance(literal, IRPEnumerationLiteral)
        return pkg, literal

    def test_value(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("LiteralPkg"))
        try:
            _, literal = self._literal(pkg)
            literal.value = "42"
            assert literal.value == "42"
        finally:
            pkg.delete_from_project()
