import allure
import pytest

from page_objects.main_page import MainPage
from steps.currency_steps import CurrencySteps


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Change of currency")
@allure.story("Change of currency scenario")
@allure.severity(allure.severity_level.CRITICAL)
def test_currency_change_on_main_page(browser):
    allure.dynamic.description("Changing currency from euro to dollar")
    MainPage(browser).open_main()
    currency = CurrencySteps(browser)
    price_euro = currency.get_price()
    currency.call_currency_dropdown()
    currency.change_to_usd()
    price_dollar = currency.get_price()
    assert price_euro != price_dollar
    assert "€" in price_euro
    assert "€" not in price_dollar
