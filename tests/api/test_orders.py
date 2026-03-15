import allure
import pytest


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Order API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order(order_scenario):
    allure.dynamic.description("Create a new order")
    order_scenario.create_order()


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Order API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_order(order_scenario):
    allure.dynamic.description("Get order by ID")
    order = order_scenario.existing_order()
    order_scenario.get_order(order["order_id"])


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Order API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_order(order_scenario):
    allure.dynamic.description("Add comment to order")
    order = order_scenario.existing_order()
    order_scenario.update_order(order, "Update check")


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Order API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_order(order_scenario):
    allure.dynamic.description("Delete order (and check 404 after deletion)")
    order = order_scenario.existing_order()
    order_scenario.delete_order(order["order_id"])
