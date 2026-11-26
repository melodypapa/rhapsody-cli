"""Integration tests for IRPContextSpecification with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_context_specification import IRPContextSpecification
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPContextSpecificationIntegration:
    """Integration tests for IRPContextSpecification with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _context_specification(pkg: IRPPackage) -> tuple[IRPPackage, IRPContextSpecification]:
        element = pkg.add_new_aggr("ContextSpecification", f"ContextSpec_{uuid.uuid4().hex[:8]}")
        context = IRPContextSpecification(element._com)
        assert isinstance(context, IRPContextSpecification)
        return pkg, context

    @staticmethod
    def _string_collection(rhapsody_app: RhapsodyApplication, values: tuple[str, ...]) -> IRPCollection:
        collection = rhapsody_app.create_new_collection()
        collection.set_size(len(values))
        for index, value in enumerate(values, start=1):
            collection.set_string(index, value)
        return collection

    def test_multiplicities(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("MultiplicitiesPkg"))
        try:
            _, context = self._context_specification(pkg)
            values = ("1", "2")
            context.multiplicities = self._string_collection(rhapsody_app, values)
            assert list(context.multiplicities) == list(values)
        finally:
            pkg.delete_from_project()

    def test_value(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("ValuePkg"))
        try:
            _, context = self._context_specification(pkg)
            values = ("pkg", "cls")
            context.value = self._string_collection(rhapsody_app, values)
            assert list(context.value) == list(values)
        finally:
            pkg.delete_from_project()
