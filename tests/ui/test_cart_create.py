import allure
import pytest

from page_objects.add_to_cart import AddToCart
from page_objects.main_page import MainPage


@pytest.mark.ui
@allure.epic("UI tests")
@allure.feature("Cart")
@allure.story("Add product to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_add_to_cart(browser):
    allure.dynamic.description("Checking the creation of a cart")
    main_page = MainPage(browser)
    main_page.open_main()

    add_to_cart = AddToCart(browser)
    add_to_cart.click_product()
    product_in_card = AddToCart(browser).get_product_name_in_card()
    add_to_cart.click_add_to_cart()
    modal_title = add_to_cart.check_modal_element_title()
    assert "successfully added" in modal_title.text, "The product was not added"
    product_in_cart = add_to_cart.get_product_name_in_cart()
    assert product_in_card == product_in_cart, (
        f"The product does not match! On the card:'{product_in_card}', In the cart: '{product_in_cart}'"
    )
