import allure
import pytest

from api.models.customer_builder import CustomerBuilder


@pytest.mark.api
@pytest.mark.parametrize(
    "email",
    ["invalid-email", "test@", "@mail.com", ""],
)
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("Negative tests")
@allure.step("Attempt to create a product")
def test_create_customer_invalid_email(customers_api, email):
    allure.dynamic.description("Attempt to create a customer with an invalid email")
    xml = CustomerBuilder.create(lastname="Test", firstname="User", email=email)
    response = customers_api.create_raw(xml)
    assert response.status_code == 400


@pytest.mark.api
@pytest.mark.parametrize("customer_id", [-1, 0, 999999])
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("Negative tests")
@allure.step("Attempt to get a customer")
def test_get_invalid_customer_ids(customers_api, customer_id):
    allure.dynamic.description("Attempt to get customer by invalid ID")
    response = customers_api.get_raw(customer_id)

    assert response.status_code in [400, 404]


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("Negative tests")
@allure.step("Attempt update a customer")
def test_update_non_existing_customer(customers_api):
    allure.dynamic.description("Attempt update non existing customer")
    xml = CustomerBuilder.update(
        customer_id=999999, lastname="New name", firstname="New first name", email="test@mail.com", note="Updated"
    )
    response = customers_api.update_raw(999999, xml)
    assert response.status_code in [400, 404]
