from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = '[data-test="username"]'
    PASSWORD = '[data-test="password"]'
    LOGIN_BTN = '[data-test="login-button"]'
    ERROR = '[data-test="error"]'

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def error_text(self) -> str:
        return self.page.text_content(self.ERROR) or ""
