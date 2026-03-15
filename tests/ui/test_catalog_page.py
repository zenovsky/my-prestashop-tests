import allure
import pytest

from page_objects.catalog_page import CatalogPage


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of catalog page title")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_title(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_catalog_title()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of product categories")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_categories_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_categories_links()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of filters by suppliers")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_suppliers(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of links to suppliers")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_suppliers_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers_links()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of brand filters")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_brands(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of brand links")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_brands_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands_links()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of search filters")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_search_filters(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_search_filters()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of product subcategories")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_subcategories(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_subcategories()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of product list")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_products_list(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list()


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Catalog page")
@allure.story("Checking display of catalog page content")
@allure.severity(allure.severity_level.NORMAL)
def test_catalog_products_list_content(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list_content()
