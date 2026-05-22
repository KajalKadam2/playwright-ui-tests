#
# pages/base_page.py


from playwright.sync_api import Page, expect


class BasePage:
    """Base class for all page objects."""

    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = "/"):
        self.page.goto(f"{self.BASE_URL}{path}")
        return self

    def get_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()

    def expect_url(self, expected: str):
        expect(self.page).to_have_url(expected)
        return self

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)
        return self