import pytest
import allure
from steps.contact_us_steps import ContactUsSteps
from page_objects.contact_us_page import ContactUsPage

@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Contact Us page")
@allure.story("Open page and check title")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_contact_us_page(browser):
    allure.dynamic.description("Checking if a Contact Us page opens")
    steps = ContactUsSteps(browser)
    steps.check_contact_us_title()


@pytest.mark.ui
@pytest.mark.parametrize(
    "element_name, selector",
    [
        ("Store information block", ContactUsPage.STORE_BLOCK),
        ("Contact form", ContactUsPage.FORM_BLOCK),
    ],
)
@allure.epic("UI tests")
@allure.feature("Contact Us page")
@allure.story("Check page elements")
@allure.severity(allure.severity_level.CRITICAL)
def test_elements_visible_on_contact_us_page(browser, element_name, selector):
    allure.dynamic.description(f"Checking a display {element_name} on a page")
    steps = ContactUsSteps(browser)
    steps.check_contact_us_title()
    assert steps.check_element_visible(selector), f"{element_name} is not visible"