# # pages/checkboxes_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Page object for the checkboxes page."""

    URL = "/checkboxes"

    def open(self):
        self.navigate(self.URL)
        return self

    def get_checkbox(self, index: int):
        return self.page.locator("input[type='checkbox']").nth(index)

    def check(self, index: int):
        self.get_checkbox(index).check()
        return self

    def uncheck(self, index: int):
        self.get_checkbox(index).uncheck()
        return self

    def expect_checked(self, index: int):
        expect(self.get_checkbox(index)).to_be_checked()
        return self

    def expect_unchecked(self, index: int):
        expect(self.get_checkbox(index)).not_to_be_checked()
        return self