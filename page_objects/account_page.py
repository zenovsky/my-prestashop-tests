from page_objects.base_page import BasePage
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class AccountInfoPage(BasePage):
    ACCOUNT_INFORMATION_LINK = "#identity-link"
    FIELDS_MAP = {
        "firstname": "#field-firstname",
        "lastname": "#field-lastname",
        "email": "#field-email",
        "password": "#field-password",
        "birthday": "#field-birthday",
    }

    @allure_attach_on_fail
    @log_action
    @allure_step("Go to the account information section")
    def click_information_link(self):
        self.wait_element(self.ACCOUNT_INFORMATION_LINK).click()

    @allure_attach_on_fail
    @log_action
    @allure_step("Verifying the created user's data")
    def verify_field_value(self, field_name: str, expected_value: str):
        try:
            selector = self.FIELDS_MAP[field_name.lower()]
        except KeyError:
            raise ValueError(f"Unknown field: '{field_name}'")
        FIELD_LOCATOR = selector
        field_element = self.wait_element(FIELD_LOCATOR)
        actual_value = field_element.get_attribute("value")
        if actual_value == expected_value:
            print(f"Verification successful: Field '{field_name}' contains the expected value '{expected_value}'.")
        else:
            raise AssertionError(
                f"Field validation error '{field_name}'. It was expected: '{expected_value}', actual: '{actual_value}'"
            )
