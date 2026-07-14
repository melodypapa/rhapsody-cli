import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPSignal
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPSignalIntegration:
    """Integration tests for RPSignal with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    @pytest.mark.xfail(
        reason="Rhapsody2.Application.1 does not expose 'addSignal' (or addNewAggr('Signal')) on a "
        "package; RPPackage.add_signal raises. TODO: support Signal creation via the correct "
        "metaclass/owner in a future Rhapsody build.",
        strict=False,
    )
    def test_create_signal_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SigPkg")
        sig_name = self._unique("MySignal")
        pkg = self._create_package(test_project, pkg_name)
        try:
            signal = pkg.add_signal(sig_name)
            assert signal is not None
            assert isinstance(signal, RPSignal)
            assert signal.get_name() == sig_name
            assert signal.get_meta_class() == "Signal"
        finally:
            signal.delete_from_project()
