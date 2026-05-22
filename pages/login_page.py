#
# pages/login_page.py

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    URL = "/login"

    @property
    def username_input(self):
        return self.page.get_by_label("Username")

    @property
    def password_input(self):
        return self.page.get_by_label("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def flash_message(self):
        return self.page.locator("#flash")

    def open(self):
        self.navigate(self.URL)
        return self

    def fill_username(self, username: str):
        self.username_input.fill(username)
        return self

    def fill_password(self, password: str):
        self.password_input.fill(password)
        return self

    def click_login(self):
        self.login_button.click()
        return self

    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        return self

    def expect_success(self):
        expect(self.flash_message).to_contain_text("secure area")
        return self

    def expect_error(self, text: str):
        expect(self.flash_message).to_contain_text(text)
        return self

    def expect_url_is_login(self):
        self.expect_url(f"{self.BASE_URL}{self.URL}")
        return self