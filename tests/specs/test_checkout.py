import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage

@pytest.mark.regression
def test_checkout_happy_path(page):
    LoginPage(page).login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    inv.add_item_by_name("Sauce Labs Backpack")
    inv.open_cart()

    cart = CartPage(page)
    cart.go_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_info("Felipe", "QA", "40000-000")
    checkout.finish()

    assert "Thank you" in checkout.success_message()
