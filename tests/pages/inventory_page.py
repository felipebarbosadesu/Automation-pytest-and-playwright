from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = ".title"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.TITLE)

    def add_item_by_name(self, name: str):
        # SauceDemo uses stable data-test values like:
        # add-to-cart-sauce-labs-backpack
        slug = name.lower().replace(" ", "-")
        self.page.click(f'[data-test="add-to-cart-{slug}"]')

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def cart_badge_count(self) -> int:
        if self.page.is_visible(self.CART_BADGE):
            return int(self.page.text_content(self.CART_BADGE))
        return 0
