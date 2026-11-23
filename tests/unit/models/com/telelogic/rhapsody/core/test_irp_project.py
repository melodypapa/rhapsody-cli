"""Tests for rhapsody_cli.elements.project.IRPProject."""

from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_project_is_a_package() -> None:
    fake = make_fake_element("Project", properties={"name": "MyProject"})
    project = IRPProject(fake)

    assert isinstance(project, IRPPackage)
    assert project.get_name() == "MyProject"


def test_project_add_package_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    new_pkg = make_fake_element("Package", properties={"name": "NewPkg"})
    fake.addPackage.return_value = new_pkg
    project = IRPProject(fake)

    result = project.add_package("NewPkg")

    fake.addPackage.assert_called_once_with("NewPkg")
    assert result.get_name() == "NewPkg"


def test_project_close_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.close()

    fake.close.assert_called_once_with()


def test_project_become_active_project_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.become_active_project()

    fake.becomeActiveProject.assert_called_once_with()


def test_project_find_component_wraps_result() -> None:
    fake = make_fake_element("Project")
    found = make_fake_element("Component", properties={"name": "Comp1"})
    fake.findComponent.return_value = found
    project = IRPProject(fake)

    result = project.find_component("Comp1")

    fake.findComponent.assert_called_once_with("Comp1")
    assert result.get_name() == "Comp1"


def test_project_get_packages_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    fake.packages = make_fake_collection([make_fake_element("Package", properties={"name": "P1"})])
    project = IRPProject(fake)

    packages = project.get_packages()

    assert isinstance(packages, IRPCollection)
    assert len(packages) == 1
    assert packages[0].get_name() == "P1"


def test_project_is_registered_for_meta_class_project() -> None:

    fake = make_fake_element("Project", properties={"name": "MyProject"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPProject)


def test_project_add_class_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    cls = make_fake_element("Class", properties={"name": "Class1"})
    fake.addClass.return_value = cls
    project = IRPProject(fake)

    result = project.add_class("Class1")

    fake.addClass.assert_called_once_with("Class1")
    assert result.get_name() == "Class1"


def test_project_add_actor_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    actor = make_fake_element("Actor", properties={"name": "Actor1"})
    fake.addActor.return_value = actor
    project = IRPProject(fake)

    result = project.add_actor("Actor1")

    fake.addActor.assert_called_once_with("Actor1")
    assert result.get_name() == "Actor1"


def test_project_get_components_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    comp1 = make_fake_element("Component", properties={"name": "Comp1"})
    fake.getComponents.return_value = make_fake_collection([comp1])
    project = IRPProject(fake)

    result = project.get_components()

    assert isinstance(result, IRPCollection)


def test_project_find_element_by_guid_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    found = make_fake_element("Class", properties={"name": "MyClass"})
    fake.findElementByGUID.return_value = found
    project = IRPProject(fake)

    result = project.find_element_by_guid("12345")

    fake.findElementByGUID.assert_called_once_with("12345")
    assert result is not None and result.get_name() == "MyClass"


# --- New tests for IRPProject ---
def test_project_add_component_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    comp = make_fake_element("Component", properties={"name": "Comp1"})
    fake.addComponent.return_value = comp
    project = IRPProject(fake)

    result = project.add_component("Comp1")

    fake.addComponent.assert_called_once_with("Comp1")
    assert result.get_name() == "Comp1"


def test_project_delete_component_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    comp_fake = make_fake_element("Component", properties={"name": "ToDelete"})

    project.delete_component(IRPUnit(comp_fake))

    fake.deleteComponent.assert_called_once_with(comp_fake)


def test_project_add_node_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake.addNode.return_value = node
    project = IRPProject(fake)

    result = project.add_node("Node1")

    fake.addNode.assert_called_once_with("Node1")
    assert result.get_name() == "Node1"


def test_project_get_nodes_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake.getNodes.return_value = make_fake_collection([node])
    project = IRPProject(fake)

    result = project.get_nodes()

    assert isinstance(result, IRPCollection)


def test_project_find_node_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake.findNode.return_value = node
    project = IRPProject(fake)

    result = project.find_node("Node1")

    fake.findNode.assert_called_once_with("Node1")
    assert result.get_name() == "Node1"


def test_project_get_all_stereotypes_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    st = make_fake_element("Stereotype", properties={"name": "MyStereotype"})
    fake.getAllStereotypes.return_value = make_fake_collection([st])
    project = IRPProject(fake)

    result = project.get_all_stereotypes()

    assert isinstance(result, IRPCollection)


def test_project_save_as_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.save_as("C:/path/to/project.rpy")

    fake.saveAs.assert_called_once_with("C:/path/to/project.rpy")


def test_project_find_element_by_binary_id_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    found = make_fake_element("Class", properties={"name": "MyClass"})
    fake.findElementByBinaryID.return_value = found
    project = IRPProject(fake)

    result = project.find_element_by_binary_id("abc123")

    fake.findElementByBinaryID.assert_called_once_with("abc123")
    assert result is not None and result.get_name() == "MyClass"


# --- Task 6: Gateway/Report methods ---
def test_project_gateway_export_to_xml_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.gateway_export_to_xml("C:/out.xml")

    fake.GatewayExportToXML.assert_called_once_with("C:/out.xml")


def test_project_gateway_export_to_xml2_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.gateway_export_to_xml2("C:/out.xml", "-verbose")

    fake.GatewayExportToXML2.assert_called_once_with("C:/out.xml", "-verbose")


def test_project_generate_report_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.generate_report("C:/tmpl.tpl", "C:/report.html")

    fake.GenerateReport.assert_called_once_with("C:/tmpl.tpl", "C:/report.html")


# --- Task 7: Custom Views methods ---
def test_project_add_custom_view_on_browser_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    view_fake = make_fake_element("CustomView", properties={"name": "V1"})

    project.add_custom_view_on_browser(IRPModelElement(view_fake))

    fake.addCustomViewOnBrowser.assert_called_once_with(view_fake)


def test_project_add_custom_view_on_diagram_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    view_fake = make_fake_element("CustomView", properties={"name": "V1"})

    project.add_custom_view_on_diagram(IRPModelElement(view_fake))

    fake.addCustomViewOnDiagram.assert_called_once_with(view_fake)


def test_project_apply_browser_custom_views_on_diagrams_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.apply_browser_custom_views_on_diagrams()

    fake.applyBrowserCustomViewsOnDiagrams.assert_called_once_with()


def test_project_get_active_custom_views_on_browser_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    view = make_fake_element("CustomView", properties={"name": "V1"})
    fake.getActiveCustomViewsOnBrowser.return_value = make_fake_collection([view])
    project = IRPProject(fake)

    result = project.get_active_custom_views_on_browser()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].get_name() == "V1"


def test_project_get_active_custom_views_on_diagram_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    view = make_fake_element("CustomView", properties={"name": "V1"})
    fake.getActiveCustomViewsOnDiagram.return_value = make_fake_collection([view])
    project = IRPProject(fake)

    result = project.get_active_custom_views_on_diagram()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].get_name() == "V1"


def test_project_remove_custom_view_on_browser_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    view_fake = make_fake_element("CustomView", properties={"name": "V1"})

    project.remove_custom_view_on_browser(IRPModelElement(view_fake))

    fake.removeCustomViewOnBrowser.assert_called_once_with(view_fake)


def test_project_remove_custom_view_on_diagram_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    view_fake = make_fake_element("CustomView", properties={"name": "V1"})

    project.remove_custom_view_on_diagram(IRPModelElement(view_fake))

    fake.removeCustomViewOnDiagram.assert_called_once_with(view_fake)


# --- Task 8: CSV methods ---
def test_project_close_csv_file_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.close_csv_file()

    fake.closeCSVFile.assert_called_once_with()


def test_project_open_csv_file_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.open_csv_file("C:/data.csv", 1)

    fake.openCSVFile.assert_called_once_with("C:/data.csv", 1)


def test_project_reload_csv_file_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.reload_csv_file()

    fake.reloadCSVFile.assert_called_once_with()


# --- Task 9: Remote/Roundtrip methods ---
def test_project_apply_roundtrip_diff_merge_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.apply_roundtrip_diff_merge()

    fake.applyRoundtripDiffMerge.assert_called_once_with()


def test_project_enable_rhapsody_model_manager_raises_not_implemented() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    with pytest.raises(NotImplementedError):
        project.enable_rhapsody_model_manager()

    fake.enableRhapsodyModelManager.assert_not_called()


def test_project_find_elements_with_oslc_link_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    elem = make_fake_element("Class", properties={"name": "C1"})
    fake.findElementsWithOSLCLink.return_value = make_fake_collection([elem])
    project = IRPProject(fake)

    result = project.find_elements_with_oslc_link("http://example.com/link")

    fake.findElementsWithOSLCLink.assert_called_once_with("http://example.com/link")
    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].get_name() == "C1"


def test_project_get_remote_resource_packages_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    pkg = make_fake_element("Package", properties={"name": "RemotePkg"})
    fake.getRemoteResourcePackages.return_value = make_fake_collection([pkg])
    project = IRPProject(fake)

    result = project.get_remote_resource_packages()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].get_name() == "RemotePkg"


def test_project_get_roundtrip_shadow_model_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    shadow = make_fake_element("Model", properties={"name": "ShadowModel"})
    fake.getRoundtripShadowModel.return_value = shadow
    project = IRPProject(fake)

    result = project.get_roundtrip_shadow_model()
    result_elem = cast(IRPModelElement, result)
    assert result_elem.get_name() == "ShadowModel"


def test_project_is_actively_managed_returns_int() -> None:
    fake = make_fake_element("Project", isActivelyManaged=1)
    project = IRPProject(fake)

    result = project.is_actively_managed()

    fake.isActivelyManaged.assert_called_once_with()
    assert result == 1


def test_project_migrate_design_manager_links_raises_not_implemented() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    with pytest.raises(NotImplementedError):
        project.migrate_design_manager_links()

    fake.migrateDesignManagerLinks.assert_not_called()


# --- Task 10: Rose Import methods ---
def test_project_import_package_from_rose_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    pkg = make_fake_element("Package", properties={"name": "RosePkg"})
    fake.importPackageFromRose.return_value = pkg
    project = IRPProject(fake)

    result = project.import_package_from_rose("C:/rose.mdl")

    fake.importPackageFromRose.assert_called_once_with("C:/rose.mdl")
    assert result.get_name() == "RosePkg"


def test_project_import_project_from_rose_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.import_project_from_rose("C:/rose.mdl")

    fake.importProjectFromRose.assert_called_once_with("C:/rose.mdl")


# --- Task 11: Events methods ---
def test_project_check_events_base_ids_solve_collisions_returns_int() -> None:
    fake = make_fake_element("Project", checkEventsBaseIdsSolveCollisions=2)
    project = IRPProject(fake)

    result = project.check_events_base_ids_solve_collisions()

    fake.checkEventsBaseIdsSolveCollisions.assert_called_once_with()
    assert result == 2


def test_project_recalculate_events_base_ids_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.recalculate_events_base_ids()

    fake.recalculateEventsBaseIds.assert_called_once_with()


# --- Task 12: Misc methods ---
def test_project_add_spell_checker_result_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.add_spell_checker_result("misspel", "misspelled")

    fake.addSpellCheckerResult.assert_called_once_with("misspel", "misspelled")


def test_project_clean_unresolved_elements_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.clean_unresolved_elements()

    fake.cleanUnresolvedElements.assert_called_once_with()


def test_project_end_transaction_of_no_cg_interest_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.end_transaction_of_no_cg_interest()

    fake.endTransactionOfNoCGInterest.assert_called_once_with()


def test_project_get_default_directory_scheme_returns_int() -> None:
    fake = make_fake_element("Project", getDefaultDirectoryScheme=1)
    project = IRPProject(fake)

    result = project.get_default_directory_scheme()
    assert result == 1


def test_project_get_new_progress_bar_returns_wrapped_element() -> None:
    fake = make_fake_element("Project")
    bar = make_fake_element("ProgressBar", properties={"name": "PB1"})
    fake.getNewProgressBar.return_value = bar
    project = IRPProject(fake)

    result = project.get_new_progress_bar()
    assert result.get_name() == "PB1"


def test_project_get_notify_plugin_on_elements_changed_returns_int() -> None:
    fake = make_fake_element("Project", getNotifyPluginOnElementsChanged=1)
    project = IRPProject(fake)

    result = project.get_notify_plugin_on_elements_changed()
    assert result == 1


def test_project_get_requirements_by_id_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Project")
    req = make_fake_element("Requirement", properties={"name": "Req1"})
    fake.getRequirementsByID.return_value = make_fake_collection([req])
    project = IRPProject(fake)

    result = project.get_requirements_by_id("REQ-001")

    fake.getRequirementsByID.assert_called_once_with("REQ-001")
    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].get_name() == "Req1"


def test_project_remove_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.remove()

    fake.remove.assert_called_once_with()


def test_project_save_as_prev_version_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.save_as_prev_version("C:/old.rpy")

    fake.saveAsPrevVersion.assert_called_once_with("C:/old.rpy")


def test_project_set_default_directory_scheme_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.set_default_directory_scheme(2)

    assert fake.defaultDirectoryScheme == 2


def test_project_set_global_configuration_raises_not_implemented() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    with pytest.raises(NotImplementedError):
        project.set_global_configuration("gc://uri", "MyConfig")

    fake.setGlobalConfiguration.assert_not_called()


def test_project_set_notify_plugin_on_elements_changed_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.set_notify_plugin_on_elements_changed(1)

    fake.setNotifyPluginOnElementsChanged.assert_called_once_with(1)


def test_project_set_object_explicit_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    obj_fake = make_fake_element("Class", properties={"name": "Obj1"})

    project.set_object_explicit(IRPModelElement(obj_fake))

    fake.setObjectExplicit.assert_called_once_with(obj_fake)


def test_project_set_object_implicit_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

    fake = make_fake_element("Project")
    project = IRPProject(fake)
    obj_fake = make_fake_element("Class", properties={"name": "Obj1"})

    project.set_object_implicit(IRPModelElement(obj_fake))

    fake.setObjectImplicit.assert_called_once_with(obj_fake)


def test_project_set_use_unique_stereotype_and_ref_cache_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.set_use_unique_stereotype_and_ref_cache(1)

    assert fake.UseUniqueStereotypeAndRefCache == 1


def test_project_set_wait_dialog_watchdog_value_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.set_wait_dialog_watchdog_value(5000)

    fake.setWaitDialogWatchdogValue.assert_called_once_with(5000)


def test_project_start_transaction_of_no_cg_interest_delegates_to_com() -> None:
    fake = make_fake_element("Project")
    project = IRPProject(fake)

    project.start_transaction_of_no_cg_interest()

    fake.startTransactionOfNoCGInterest.assert_called_once_with()


def test_generated_add_package() -> None:
    fake = make_fake_element("Project")
    fake.addPackage.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_package("x")
    assert result is not None


def test_generated_close() -> None:
    fake = make_fake_element("Project")
    fake.close.return_value = None
    IRPProject(fake).close()


def test_generated_become_active_project() -> None:
    fake = make_fake_element("Project")
    fake.becomeActiveProject.return_value = None
    IRPProject(fake).become_active_project()


def test_generated_find_component() -> None:
    fake = make_fake_element("Project")
    fake.findComponent.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_component("x")
    assert result is not None


def test_generated_get_packages() -> None:
    fake = make_fake_element("Project", properties={"packages": make_fake_collection([])})
    result = IRPProject(fake).get_packages()
    assert result is not None


def test_generated_add_class() -> None:
    fake = make_fake_element("Project")
    fake.addClass.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_class("x")
    assert result is not None


def test_generated_add_actor() -> None:
    fake = make_fake_element("Project")
    fake.addActor.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_actor("x")
    assert result is not None


def test_generated_get_components() -> None:
    fake = make_fake_element("Project", properties={"components": make_fake_collection([])})
    result = IRPProject(fake).get_components()
    assert result is not None


def test_generated_find_element_by_guid() -> None:
    fake = make_fake_element("Project")
    fake.findElementByGUID.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_element_by_guid("x")
    assert result is not None


def test_generated_add_component() -> None:
    fake = make_fake_element("Project")
    fake.addComponent.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_component("x")
    assert result is not None


def test_generated_delete_component() -> None:
    fake = make_fake_element("Project")
    fake.deleteComponent.return_value = None
    IRPProject(fake).delete_component(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_node() -> None:
    fake = make_fake_element("Project")
    fake.addNode.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_node("x")
    assert result is not None


def test_generated_get_nodes() -> None:
    fake = make_fake_element("Project", properties={"nodes": make_fake_collection([])})
    result = IRPProject(fake).get_nodes()
    assert result is not None


def test_generated_find_node() -> None:
    fake = make_fake_element("Project")
    fake.findNode.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_node("x")
    assert result is not None


def test_generated_delete_node() -> None:
    fake = make_fake_element("Project")
    fake.deleteNode.return_value = None
    IRPProject(fake).delete_node(make_fake_element("Class", properties={"name": "x"}))


def test_generated_get_active_configuration() -> None:
    fake = make_fake_element("Project", properties={"activeConfiguration": make_fake_collection([])})
    result = IRPProject(fake).get_active_configuration()
    assert result is not None


def test_generated_set_active_configuration() -> None:
    fake = make_fake_element("Project")
    fake.setActiveConfiguration.return_value = None
    IRPProject(fake).set_active_configuration(make_fake_element("Class", properties={"name": "x"}))


def test_generated_get_active_component() -> None:
    fake = make_fake_element("Project", properties={"activeComponent": make_fake_collection([])})
    result = IRPProject(fake).get_active_component()
    assert result is not None


def test_generated_set_active_component() -> None:
    fake = make_fake_element("Project")
    fake.setActiveComponent.return_value = None
    IRPProject(fake).set_active_component(make_fake_element("Class", properties={"name": "x"}))


def test_generated_get_all_stereotypes() -> None:
    fake = make_fake_element("Project", properties={"allStereotypes": make_fake_collection([])})
    result = IRPProject(fake).get_all_stereotypes()
    assert result is not None


def test_generated_get_new_collaboration() -> None:
    fake = make_fake_element("Project")
    fake.getNewCollaboration.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).get_new_collaboration()
    assert result is not None


def test_generated_add_profile() -> None:
    fake = make_fake_element("Project")
    fake.addProfile.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).add_profile("x")
    assert result is not None


def test_generated_get_profiles() -> None:
    fake = make_fake_element("Project", properties={"profiles": make_fake_collection([])})
    result = IRPProject(fake).get_profiles()
    assert result is not None


def test_generated_save_as() -> None:
    fake = make_fake_element("Project")
    fake.saveAs.return_value = None
    IRPProject(fake).save_as("x")


def test_generated_find_element_by_binary_id() -> None:
    fake = make_fake_element("Project")
    fake.findElementByBinaryID.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_element_by_binary_id("x")
    assert result is not None


def test_generated_find_element_by_file_name() -> None:
    fake = make_fake_element("Project")
    fake.findElementByFileName.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_element_by_file_name("x")
    assert result is not None


def test_generated_get_code_generated_files() -> None:
    fake = make_fake_element("Project")
    fake.getCodeGeneratedFiles.return_value = make_fake_collection([])
    result = IRPProject(fake).get_code_generated_files()
    assert result is not None


def test_generated_allow_auto_save() -> None:
    fake = make_fake_element("Project")
    fake.allowAutoSave.return_value = None
    IRPProject(fake).allow_auto_save(1)


def test_generated_allow_non_unique_names() -> None:
    fake = make_fake_element("Project")
    fake.allowNonUniqueNames.return_value = None
    IRPProject(fake).allow_non_unique_names(1)


def test_generated_get_cg_simplified_model_package() -> None:
    fake = make_fake_element("Project", properties={"cgSimplifiedModelPackage": make_fake_collection([])})
    result = IRPProject(fake).get_cg_simplified_model_package()
    assert result is not None


def test_generated_locate_in_ide() -> None:
    fake = make_fake_element("Project")
    fake.locateInIDE.return_value = None
    IRPProject(fake).locate_in_ide()


def test_generated_is_modified_recursive() -> None:
    fake = make_fake_element("Project")
    fake.isModifiedRecursive.return_value = True
    result = IRPProject(fake).is_modified_recursive()
    assert result is not None


def test_generated_highlight_from_code() -> None:
    fake = make_fake_element("Project")
    fake.highlightFromCode.return_value = None
    IRPProject(fake).highlight_from_code("x", 1)


def test_generated_gateway_export_to_xml() -> None:
    fake = make_fake_element("Project")
    fake.GatewayExportToXML.return_value = None
    IRPProject(fake).gateway_export_to_xml("x")


def test_generated_gateway_export_to_xml2() -> None:
    fake = make_fake_element("Project")
    fake.GatewayExportToXML2.return_value = None
    IRPProject(fake).gateway_export_to_xml2("x", "x")


def test_generated_generate_report() -> None:
    fake = make_fake_element("Project")
    fake.GenerateReport.return_value = None
    IRPProject(fake).generate_report("x", "x")


def test_generated_add_custom_view_on_browser() -> None:
    fake = make_fake_element("Project")
    fake.addCustomViewOnBrowser.return_value = None
    IRPProject(fake).add_custom_view_on_browser(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_custom_view_on_diagram() -> None:
    fake = make_fake_element("Project")
    fake.addCustomViewOnDiagram.return_value = None
    IRPProject(fake).add_custom_view_on_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_apply_browser_custom_views_on_diagrams() -> None:
    fake = make_fake_element("Project")
    fake.applyBrowserCustomViewsOnDiagrams.return_value = None
    IRPProject(fake).apply_browser_custom_views_on_diagrams()


def test_generated_get_active_custom_views_on_browser() -> None:
    fake = make_fake_element("Project")
    fake.getActiveCustomViewsOnBrowser.return_value = make_fake_collection([])
    result = IRPProject(fake).get_active_custom_views_on_browser()
    assert result is not None


def test_generated_get_active_custom_views_on_diagram() -> None:
    fake = make_fake_element("Project")
    fake.getActiveCustomViewsOnDiagram.return_value = make_fake_collection([])
    result = IRPProject(fake).get_active_custom_views_on_diagram()
    assert result is not None


def test_generated_remove_custom_view_on_browser() -> None:
    fake = make_fake_element("Project")
    fake.removeCustomViewOnBrowser.return_value = None
    IRPProject(fake).remove_custom_view_on_browser(make_fake_element("Class", properties={"name": "x"}))


def test_generated_remove_custom_view_on_diagram() -> None:
    fake = make_fake_element("Project")
    fake.removeCustomViewOnDiagram.return_value = None
    IRPProject(fake).remove_custom_view_on_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_close_csv_file() -> None:
    fake = make_fake_element("Project")
    fake.closeCSVFile.return_value = None
    IRPProject(fake).close_csv_file()


def test_generated_open_csv_file() -> None:
    fake = make_fake_element("Project")
    fake.openCSVFile.return_value = None
    IRPProject(fake).open_csv_file("x", 1)


def test_generated_reload_csv_file() -> None:
    fake = make_fake_element("Project")
    fake.reloadCSVFile.return_value = None
    IRPProject(fake).reload_csv_file()


def test_generated_apply_roundtrip_diff_merge() -> None:
    fake = make_fake_element("Project")
    fake.applyRoundtripDiffMerge.return_value = None
    IRPProject(fake).apply_roundtrip_diff_merge()


def test_generated_enable_rhapsody_model_manager_raises_not_implemented() -> None:
    fake = make_fake_element("Project")

    with pytest.raises(NotImplementedError):
        IRPProject(fake).enable_rhapsody_model_manager()

    fake.enableRhapsodyModelManager.assert_not_called()


def test_generated_find_elements_with_oslc_link() -> None:
    fake = make_fake_element("Project")
    fake.findElementsWithOSLCLink.return_value = make_fake_collection([])
    result = IRPProject(fake).find_elements_with_oslc_link("x")
    assert result is not None


def test_generated_get_remote_resource_packages() -> None:
    fake = make_fake_element("Project")
    fake.getRemoteResourcePackages.return_value = make_fake_collection([])
    result = IRPProject(fake).get_remote_resource_packages()
    assert result is not None


def test_generated_get_roundtrip_shadow_model() -> None:
    fake = make_fake_element("Project")
    fake.getRoundtripShadowModel.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).get_roundtrip_shadow_model()
    assert result is not None


def test_generated_is_actively_managed() -> None:
    fake = make_fake_element("Project")
    fake.isActivelyManaged.return_value = 1
    result = IRPProject(fake).is_actively_managed()
    assert result is not None


def test_generated_migrate_design_manager_links_raises_not_implemented() -> None:
    fake = make_fake_element("Project")

    with pytest.raises(NotImplementedError):
        IRPProject(fake).migrate_design_manager_links()

    fake.migrateDesignManagerLinks.assert_not_called()


def test_generated_import_package_from_rose() -> None:
    fake = make_fake_element("Project")
    fake.importPackageFromRose.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).import_package_from_rose("x")
    assert result is not None


def test_generated_import_project_from_rose() -> None:
    fake = make_fake_element("Project")
    fake.importProjectFromRose.return_value = None
    IRPProject(fake).import_project_from_rose("x")


def test_generated_check_events_base_ids_solve_collisions() -> None:
    fake = make_fake_element("Project")
    fake.checkEventsBaseIdsSolveCollisions.return_value = 1
    result = IRPProject(fake).check_events_base_ids_solve_collisions()
    assert result is not None


def test_generated_recalculate_events_base_ids() -> None:
    fake = make_fake_element("Project")
    fake.recalculateEventsBaseIds.return_value = None
    IRPProject(fake).recalculate_events_base_ids()


def test_generated_add_spell_checker_result() -> None:
    fake = make_fake_element("Project")
    fake.addSpellCheckerResult.return_value = None
    IRPProject(fake).add_spell_checker_result("x", "x")


def test_generated_clean_unresolved_elements() -> None:
    fake = make_fake_element("Project")
    fake.cleanUnresolvedElements.return_value = None
    IRPProject(fake).clean_unresolved_elements()


def test_generated_end_transaction_of_no_cg_interest() -> None:
    fake = make_fake_element("Project")
    fake.endTransactionOfNoCGInterest.return_value = None
    IRPProject(fake).end_transaction_of_no_cg_interest()


def test_generated_get_default_directory_scheme() -> None:
    fake = make_fake_element("Project", properties={"defaultDirectoryScheme": make_fake_collection([])})
    result = IRPProject(fake).get_default_directory_scheme()
    assert result is not None


def test_generated_get_new_progress_bar() -> None:
    fake = make_fake_element("Project")
    fake.getNewProgressBar.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).get_new_progress_bar()
    assert result is not None


def test_generated_get_notify_plugin_on_elements_changed() -> None:
    fake = make_fake_element("Project")
    fake.getNotifyPluginOnElementsChanged.return_value = 1
    result = IRPProject(fake).get_notify_plugin_on_elements_changed()
    assert result is not None


def test_generated_get_requirements_by_id() -> None:
    fake = make_fake_element("Project")
    fake.getRequirementsByID.return_value = make_fake_collection([])
    result = IRPProject(fake).get_requirements_by_id("x")
    assert result is not None


def test_generated_remove() -> None:
    fake = make_fake_element("Project")
    fake.remove.return_value = None
    IRPProject(fake).remove()


def test_generated_save_as_prev_version() -> None:
    fake = make_fake_element("Project")
    fake.saveAsPrevVersion.return_value = None
    IRPProject(fake).save_as_prev_version("x")


def test_generated_set_default_directory_scheme() -> None:
    fake = make_fake_element("Project")
    IRPProject(fake).set_default_directory_scheme(1)


def test_generated_set_global_configuration_raises_not_implemented() -> None:
    fake = make_fake_element("Project")

    with pytest.raises(NotImplementedError):
        IRPProject(fake).set_global_configuration("uri", "x")

    fake.setGlobalConfiguration.assert_not_called()


def test_generated_set_notify_plugin_on_elements_changed() -> None:
    fake = make_fake_element("Project")
    fake.setNotifyPluginOnElementsChanged.return_value = None
    IRPProject(fake).set_notify_plugin_on_elements_changed(1)


def test_generated_set_object_explicit() -> None:
    fake = make_fake_element("Project")
    fake.setObjectExplicit.return_value = None
    IRPProject(fake).set_object_explicit(make_fake_element("Class", properties={"name": "x"}))


def test_generated_set_object_implicit() -> None:
    fake = make_fake_element("Project")
    fake.setObjectImplicit.return_value = None
    IRPProject(fake).set_object_implicit(make_fake_element("Class", properties={"name": "x"}))


def test_generated_set_use_unique_stereotype_and_ref_cache() -> None:
    fake = make_fake_element("Project")
    IRPProject(fake).set_use_unique_stereotype_and_ref_cache(1)


def test_generated_set_wait_dialog_watchdog_value() -> None:
    fake = make_fake_element("Project")
    fake.setWaitDialogWatchdogValue.return_value = None
    IRPProject(fake).set_wait_dialog_watchdog_value(1)


def test_generated_start_transaction_of_no_cg_interest() -> None:
    fake = make_fake_element("Project")
    fake.startTransactionOfNoCGInterest.return_value = None
    IRPProject(fake).start_transaction_of_no_cg_interest()
