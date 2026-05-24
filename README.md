# playwright-ui-tests

![CI](https://github.com/KajalKadam2/playwright-ui-tests/actions/workflows/ci.yml/badge.svg)

Production-grade UI and API automation suite built with **Python + Playwright + pytest**.  
Demonstrates Page Object Model, data-driven testing, API client pattern, and CI/CD.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core language |
| Playwright | Browser automation |
| pytest | Test runner and fixtures |
| requests | API testing |
| GitHub Actions | CI/CD pipeline |

---

## Project Structure

```
playwright-ui-tests/
├── pages/                         # Page Object Model classes
│   ├── base_page.py               # Shared navigation and utilities
│   ├── login_page.py              # Login page — locators + actions + assertions
│   ├── checkboxes_page.py         # Checkboxes page
│   └── secure_page.py             # Secure area page
├── tests/
│   ├── ui/                        # Playwright browser tests
│   │   ├── test_login_pom.py      # Login tests with parametrize
│   │   └── test_checkboxes_pom.py # Checkbox interaction tests
│   └── api/                       # REST API tests
│       ├── test_api_complete.py   # ReqresAPI class — full CRUD lifecycle
│       └── test_day22_challenge.py# Schema validation + parametrized scenarios
├── conftest.py                    # Fixtures + auto screenshot on failure
├── requirements.txt
└── .github/workflows/ci.yml      # GitHub Actions CI/CD
```

---

## UI Test Features — Playwright + POM

- **Page Object Model** — BasePage, LoginPage, CheckboxesPage, SecurePage
- **pytest fixtures** — zero `page.goto()` in any test file
- **Parametrize** — data-driven login scenarios with readable `ids=`
- **Auto screenshot on failure** — saved to `screenshots/` automatically
- **Assertions** — `to_be_visible`, `to_have_url`, `to_be_checked`, `to_have_count`

## API Test Features — requests + pytest

- **ReqresAPI helper class** — thin wrapper around all endpoints
- **Full CRUD coverage** — GET, POST, PATCH, DELETE
- **Schema validation** — every user field checked across all records
- **Parametrized scenarios** — login, user IDs, error cases with readable `ids=`
- **Response time assertions** — performance checks on critical endpoints

---

## Test Coverage

| Suite | Tests | Type |
|-------|-------|------|
| Login — valid, invalid, parametrized | 7 | UI + POM |
| Checkboxes — state, interaction | 3 | UI + POM |
| API — CRUD lifecycle, pagination, schema | 3 | API |
| API — schema, parametrized, 404, login | 16 | API |
| **Total** | **29** | |

---

## Setup and Run

```bash
# Clone
git clone https://github.com/KajalKadam2/playwright-ui-tests.git
cd playwright-ui-tests

# Install
pip install -r requirements.txt
playwright install chromium

# Run everything
pytest tests/ -v

# Run UI tests only
pytest tests/ui/ -v --headed

# Run API tests only
pytest tests/api/ -v
```

---

## CI/CD Pipeline

GitHub Actions runs automatically on every push to `main`:

- **API Tests job** — `pip install requests pytest` only, no browser, runs in ~12s
- **Playwright UI Tests job** — installs Chromium, full suite runs in ~45s
- Screenshots uploaded as artifacts on any UI test failure

---

## Test Sites

- UI tests → [The Internet](https://the-internet.herokuapp.com) — purpose-built Playwright practice site
- API tests → [ReqRes](https://reqres.in) — hosted REST API for testing

---
