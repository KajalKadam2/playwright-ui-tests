#
# conftest.py
import pytest
from pathlib import Path
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.checkboxes_page import CheckboxesPage
from pages.secure_page import SecurePage


@pytest.fixture
def login_page_obj(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    yield lp


@pytest.fixture
def checkboxes_page_obj(page: Page) -> CheckboxesPage:
    cp = CheckboxesPage(page)
    cp.open()
    yield cp


@pytest.fixture
def secure_page_obj(page: Page) -> SecurePage:
    lp = LoginPage(page)
    lp.open().login("tomsmith", "SuperSecretPassword!")
    sp = SecurePage(page)
    yield sp


# Auto screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield
    # Only take screenshot if page fixture exists (UI tests only)
    page = request.node.funcargs.get("page", None)
    if page is None:
        return
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        Path("screenshots").mkdir(exist_ok=True)
        name = request.node.name.replace("[", "_").replace("]", "")
        page.screenshot(path=f"screenshots/{name}.png", full_page=True)
        print(f"\n  📸 Screenshot: screenshots/{name}.png")