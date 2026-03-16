from page_objects.currency_change import CurrencyChange
from utils.decorators import allure_attach_on_fail, allure_step, log_action


class CurrencySteps:
    def __init__(self, browser):
        self.page = CurrencyChange(browser)

    @allure_attach_on_fail
    @log_action
    @allure_step("Get the current price")
    def get_price(self):
        return self.page.get_price_text()

    @allure_attach_on_fail
    @log_action
    @allure_step("Call the drop-down list to change the currency")
    def call_currency_dropdown(self):
        self.page.click_currency_dropdown()

    @allure_attach_on_fail
    @log_action
    @allure_step("Change currency to USD")
    def change_to_usd(self):
        self.page.select_currency(self.page.PRICE_DOLLAR)
