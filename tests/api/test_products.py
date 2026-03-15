import pytest
import allure


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_product(product_scenario):
    allure.dynamic.description("Create a new product with minimal fields")
    product_scenario.create_product()  

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_product(product_scenario):
    allure.dynamic.description("Get product by ID")
    product = product_scenario.existing_product()
    product_scenario.get_product(product["product_id"])    

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_product(product_scenario):
    allure.dynamic.description("Change price and name of the product")
    product = product_scenario.existing_product(name="Old name", price=10.0)
    product_scenario.update_product(
        product,
        new_price=42.90,
        new_name="New Name"
    )    

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product(product_scenario):
    allure.dynamic.description("Delete product (and check 404 after deletion)")
    product = product_scenario.existing_product()
    product_scenario.delete_product(product["product_id"])    