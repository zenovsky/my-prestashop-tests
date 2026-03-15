from page_objects.contact_us_page import ContactUsPage
from utils.decorators import allure_attach_on_fail, allure_step, log_action

class ContactUsSteps:

    def __init__(self, browser):
        self.page = ContactUsPage(browser)

    @allure_attach_on_fail
    @log_action
    @allure_step("Open Contact Us page and check title")
    def check_contact_us_title(self):
        self.page.open_contact_us_page()
        self.page.wait_title_contact_us()

    @allure_attach_on_fail
    @log_action
    @allure_step("Check visibility of element")
    def check_element_visible(self, selector):
        return self.page.element_visible(selector)