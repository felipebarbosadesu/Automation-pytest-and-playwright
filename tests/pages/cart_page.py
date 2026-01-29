from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = '[data-test="checkout"]'
    ITEM_NAME = ".inventory_item_name"

    def has_item(self, name: str) -> bool:
        names = self.page.locator(self.ITEM_NAME).all_text_contents()
        return name in names

    def go_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)
