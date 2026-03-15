from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class AdminPage(BasePage):
    TITLE = "Dashboard • PrestaShop"
    ADMIN_ICON = ".employee_name.dropdown-toggle"
    ADMIN_LOGOUT = "#header_logout"
    ADMIN_HEADER_SEARCH = "#bo_query"
    ADMIN_HEADER_SEARCH_DROPDOWN = (By.XPATH, "//button[contains(text(), 'Everywhere')]")
    ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG = 'a[data-item="Catalog"]'
    ADMIN_CATALOG_SUBMENU = "#subtab-AdminCatalog"
    ADMIN_CATALOG_PRODUCTS = "#subtab-AdminProducts"

    @allure_attach_on_fail
    @log_action
    @allure_step("The administrator page has opened")
    def check_admin_page_title(self):
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Check for the presence of the administrator icon")
    def check_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON)

    @allure_attach_on_fail
    @log_action
    @allure_step("Check for the presence of a logout button on the admin page")
    def check_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT)

    @allure_attach_on_fail
    @log_action
    @allure_step("Click on the administrator icon")
    def click_admin_dropdown_toggle(self):
        self.wait_element(self.ADMIN_ICON).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Log out of the admin page")
    def click_admin_logout_button(self):
        self.wait_element(self.ADMIN_LOGOUT).click()

    allure_attach_on_fail

    @log_action
    @allure_step("Check for the presence of a catalog submenu")
    def check_admin_catalog_submenu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU)

    @allure_attach_on_fail
    @log_action
    @allure_step("Go to the catalog submenu")
    def click_admin_catalog_submemu(self):
        self.wait_element(self.ADMIN_CATALOG_SUBMENU).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Go to the products section")
    def click_admin_catalog_products(self):
        self.wait_element(self.ADMIN_CATALOG_PRODUCTS).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Check for the presence of a search field in the admin page header")
    def check_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH)

    @allure_attach_on_fail
    @log_action
    @allure_step("Click on the search field in the header of the admin page")
    def click_admin_header_search(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Fill in the search field in the admin page header")
    def fill_admin_header_search(self, search):
        search_input = self.wait_element(self.ADMIN_HEADER_SEARCH)
        search_input.send_keys(search)

    @allure_attach_on_fail
    @log_action
    @allure_step("Start your search from the admin page header")
    def click_admin_header_search_dropdown(self):
        by, selector = self.ADMIN_HEADER_SEARCH_DROPDOWN
        self.wait_element(selector, by=by).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("In the search drop-down list in the header, select 'Products'")
    def click_admin_header_search_dropdown_catalog(self):
        self.wait_element(self.ADMIN_HEADER_SEARCH_DROPDOWN_CATALOG)
