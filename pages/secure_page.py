# 

# pages/secure_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class SecurePage(BasePage):
    """Page object for the secure area."""

    URL = "/secure"

    @property
    def heading(self):
        return self.page.get_by_role("heading", name="Secure Area", exact=True)

    @property
    def logout_button(self):
        return self.page.get_by_role("link", name="Logout")

    def logout(self):
        self.logout_button.click()
        return self

    def expect_secure_area_visible(self):
        expect(self.heading).to_be_visible()
        return self

    def expect_logout_visible(self):
        expect(self.logout_button).to_be_visible()
        return self

    def expect_on_secure_page(self):
        self.expect_url(f"{self.BASE_URL}{self.URL}")
        return self