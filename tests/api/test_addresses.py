import allure
import pytest


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Addresses API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_address(address_scenario):
    allure.dynamic.description("Create a new address")
    address_scenario.create_address()


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Addresses API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_address(address_scenario):
    allure.dynamic.description("Get address by ID")
    address = address_scenario.existing_address()
    address_scenario.get_address(address["address_id"])


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Addresses API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_address(address_scenario):
    allure.dynamic.description("Add mobile phone to the address")
    address = address_scenario.existing_address()
    address_scenario.update_address(address, "942942")


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Addresses API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_address(address_scenario):
    allure.dynamic.description("Delete address (and check 404 after deletion)")
    address = address_scenario.existing_address()
    address_scenario.delete_address(address["address_id"])
