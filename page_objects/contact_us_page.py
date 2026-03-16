from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class ContactUsPage(BasePage):
    TITLE = "Contact us"

    STORE_BLOCK = ".contact-rich"
    FORM_BLOCK = ".contact-form"

    @allure_attach_on_fail
    @log_action
    @allure_step("Open Contact Us page")
    def open_contact_us_page(self):
        self.open("/contact-us")

    @allure_attach_on_fail
    @log_action
    @allure_step("Wait for Contact Us page title")
    def wait_title_contact_us(self):
        self.wait_title(self.TITLE)

    @allure_attach_on_fail
    @log_action
    @allure_step("Wait for element visible: {selector}")
    def element_visible(self, selector):
        return self.wait_element(selector).is_displayed()
