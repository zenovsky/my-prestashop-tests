import pytest
import allure

from api.models.product_builder import ProductBuilder


@pytest.mark.api
@pytest.mark.parametrize(
    "name, price, expected_status",
    [
        ("Test product", "14,90", 400),
        ("Test product", -10, 400),
    ],
)
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("Negative tests")
@allure.step("Attempt to create a product")
def test_create_product_negative(products_api, name, price, expected_status):
    allure.dynamic.description("Attempt to create a product with an invalid price value")
    xml = ProductBuilder.create(
        name=name,
        price=price
    )
    response = products_api.create_raw(xml)
    assert response.status_code == expected_status

@pytest.mark.api
@pytest.mark.parametrize("product_id", [-1, 0, 999999])
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("Negative tests")
@allure.step("Attempt to get a product")
def test_get_invalid_product_ids(products_api, product_id):
    allure.dynamic.description("Attempt to get product by invalid ID")
    response = products_api.get_raw(product_id)
    assert response.status_code in [400, 404]

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Products API")
@allure.story("Negative tests")
@allure.step("Attempt update a product")
def test_update_non_existing_product(products_api):
    allure.dynamic.description("Attempt update non existing product")
    xml = ProductBuilder.update(
        product_id=999999,
        price=42.90,
        name="Updated"
    )
    response = products_api.update_raw(999999, xml)
    assert response.status_code in [400, 404]    