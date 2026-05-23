![CI](https://github.com/KajalKadam2/playwright-ui-tests/actions/workflows/ci.yml/badge.svg)

# playwright-ui-tests
UI automation test suite using Playwright + pytest + Page Object Model.

## Stack
- Python 3.10 | Playwright | pytest | Page Object Model

## Structure
- `pages/` — Page Object classes (BasePage, LoginPage, SecurePage, CheckboxesPage)
- `conftest.py` — shared fixtures + auto screenshot on failure
- `tests/ui/` — Playwright UI tests (POM + parametrize)
- `tests/api/` — API tests (reqres.in CRUD + schema validation)

## Run
pip install pytest-playwright
playwright install
pytest -v --headed

## Features
- Page Object Model — locators in one place, tests never touch selectors directly
- pytest fixtures — zero page.goto() in test files
- parametrize — data-driven tests with readable ids
- Auto screenshot on failure — saved to screenshots/