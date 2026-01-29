import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage

@pytest.mark.smoke
def test_add_item_to_cart(page):
    LoginPage(page).login("standard_user", "secret_sauce")

    inv = InventoryPage(page)
    assert inv.is_loaded()

    item = "Sauce Labs Backpack"
    inv.add_item_by_name(item)

    assert inv.cart_badge_count() == 1

    inv.open_cart()
    cart = CartPage(page)
    assert cart.has_item(item)
