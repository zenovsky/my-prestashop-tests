import allure
import pytest

from page_objects.main_page import MainPage


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Home page")
@allure.story("Checking home page title")
@allure.severity(allure.severity_level.CRITICAL)
def test_main_title(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_title_main()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Home page")
@allure.story("Checking the display of header elements")
@allure.severity(allure.severity_level.CRITICAL)
def test_header_elements(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_header_elements()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Home page")
@allure.story("Checking display of product list on home page")
@allure.severity(allure.severity_level.CRITICAL)
def test_products(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_product_blocks()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Home page")
@allure.story("Checking the display of the main blocks on home page")
@allure.severity(allure.severity_level.CRITICAL)
def test_key_blocks(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_key_blocks()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Home page")
@allure.story("Checking the display of footer elements")
@allure.severity(allure.severity_level.CRITICAL)
def test_footer(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_footer_elements()
