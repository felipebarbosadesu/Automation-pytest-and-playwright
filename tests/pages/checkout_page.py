from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = '[data-test="firstName"]'
    LAST_NAME = '[data-test="lastName"]'
    POSTAL_CODE = '[data-test="postalCode"]'
    CONTINUE = '[data-test="continue"]'
    FINISH = '[data-test="finish"]'
    COMPLETE_HEADER = ".complete-header"

    def fill_info(self, first: str, last: str, postal: str):
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, postal)
        self.page.click(self.CONTINUE)

    def finish(self):
        self.page.click(self.FINISH)

    def success_message(self) -> str:
        return self.page.text_content(self.COMPLETE_HEADER) or ""
