import allure
import pytest


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Cart API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_cart(cart_scenario):
    allure.dynamic.description("Create a new cart with minimal fields")
    cart_scenario.create_cart()


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Cart API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_cart(cart_scenario):
    allure.dynamic.description("Get cart by ID")
    cart = cart_scenario.existing_cart()
    cart_scenario.get_cart(cart["cart_id"])


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Cart API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_cart(cart_scenario):
    allure.dynamic.description("Add quantity of product to cart")
    cart = cart_scenario.existing_cart()
    cart_scenario.update_cart(cart, "3")


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Cart API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_cart(cart_scenario):
    allure.dynamic.description("Delete cart (and check 404 after deletion)")
    cart = cart_scenario.existing_cart()
    cart_scenario.delete_cart(cart["cart_id"])
