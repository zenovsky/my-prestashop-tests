import pytest
import allure


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_customer(customer_scenario):
    allure.dynamic.description("New customer registration")
    customer_scenario.create_customer()

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_customer(customer_scenario):
    allure.dynamic.description("Get customer by ID")
    customer = customer_scenario.existing_customer()
    customer_scenario.get_customer(customer["customer_id"])

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_customer(customer_scenario):
    allure.dynamic.description("Update customer: name, email and add note")
    customer = customer_scenario.existing_customer()
    customer_scenario.update_customer(
        customer_data=customer,
        lastname="Updated",
        firstname="User",
        email="updated-user@test.com",
        note="Updated"
    )

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Customers API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_customer(customer_scenario):
    allure.dynamic.description("Delete customer (and check 404 after deletion)")
    customer = customer_scenario.existing_customer()
    customer_scenario.delete_customer(customer["customer_id"]) 