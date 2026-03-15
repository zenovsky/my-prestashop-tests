import allure
import pytest


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_category(category_scenario):
    allure.dynamic.description("Create an active category with name")
    category_scenario.create_category()


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_category(category_scenario):
    allure.dynamic.description("Get category by ID")
    category = category_scenario.existing_category()
    category_scenario.get_category(category["category_id"])


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_category(category_scenario):
    category = category_scenario.existing_category(name="Old name", active_status="1")
    allure.dynamic.description("Change name and activity of a category")
    category_scenario.update_category(category, new_name="New name", new_active_status="0")


@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("CRUD tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_category(category_scenario):
    allure.dynamic.description("Delete category(and check 404 after deletion)")
    category = category_scenario.existing_category()
    category_scenario.delete_category(category["category_id"])
