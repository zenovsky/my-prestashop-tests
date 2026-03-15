import pytest
import allure

from api.models.category_builder import CategoryBuilder


import pytest
import allure
from api.models.category_builder import CategoryBuilder


@pytest.mark.api
@pytest.mark.parametrize(
    "name, expected_status",
    [
        ("", 400),
        ("a" * 300, 400),
    ],
)
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("Negative tests")
@allure.step("Attempt to create a category")
def test_create_category_invalid_name(categories_api, name, expected_status):
    allure.dynamic.description("Attempt to create a categoey with an invalid name")
    xml = CategoryBuilder.create(name=name)
    response = categories_api.create_raw(xml)
    assert response.status_code == expected_status 

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("Negative tests")
@allure.step("Attempt to get a category")
def test_get_non_existing_category(categories_api):
    allure.dynamic.description("Attempt to get category by invalid ID")
    response = categories_api.get_raw(999999)
    assert response.status_code == 404

@pytest.mark.api
@allure.epic("API tests")
@allure.feature("Categories API")
@allure.story("Negative tests")
@allure.step("Attempt update a category")
def test_update_non_existing_category(categories_api):
    allure.dynamic.description("Attempt update non existing category")
    xml = CategoryBuilder.update(
        category_id=999999,
        active_status="1",
        name="Updated"
    )
    response = categories_api.update_raw(999999, xml)
    assert response.status_code in [400, 404]       