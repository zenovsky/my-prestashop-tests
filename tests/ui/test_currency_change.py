import allure
import pytest

from page_objects.main_page import MainPage
from page_objects.currency_change import CurrencyChange


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Change of currency")
@allure.story("Change of currency scenario")
@allure.severity(allure.severity_level.CRITICAL)
def test_currency_change(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    currency_change = CurrencyChange(browser)
    price_euro = currency_change.get_price_text()
    currency_change.click_currency_dropdown()
    currency_change.select_currency(currency_change.PRICE_DOLLAR)
    price_dollar = currency_change.get_price_text()
    assert price_euro != price_dollar, "Prices have not changed after switching currencies!"
    assert "€" in price_euro, "The price does not contain the EUR symbol (€)"
    assert "€" not in price_dollar, "The currency symbol has not changed to USD"