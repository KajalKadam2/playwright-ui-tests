# playwright-ui-tests

![CI](https://github.com/KajalKadam2/playwright-ui-tests/actions/workflows/ci.yml/badge.svg)

Production-grade UI and API automation suite built with **Python + Playwright + pytest**.
Demonstrates Page Object Model, data-driven testing, fixtures, and CI/CD.

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
````
playwright-ui-tests/
├── pages/                       # Page Object Model classes
│   ├── base_page.py             # Shared navigation and utilities
│   ├── login_page.py            # Login page — locators + actions + assertions
│   ├── checkboxes_page.py       # Checkboxes page
│   └── secure_page.py           # Secure area page
├── tests/
│   ├── ui/                      # Playwright browser tests
│   │   ├── test_login_pom.py    # Login tests with parametrize
│   │   └── test_checkboxes_pom.py
│   └── api/                     # REST API tests
│       ├── test_api_complete.py # Full CRUD lifecycle
│       └── test_day22_challenge.py
├── conftest.py                  # Fixtures + auto screenshot on failure
├── requirements.txt
└── .github/workflows/ci.yml    # GitHub Actions CI/CD
````
---

## Key Features

- **Page Object Model** — locators and actions in page classes, tests stay clean
- **pytest fixtures** — zero `page.goto()` in any test file
- **Parametrize** — data-driven tests with readable `ids=`
- **Auto screenshot on failure** — saved to `screenshots/` automatically
- **CI/CD** — GitHub Actions runs UI and API tests separately on every push
- **Full CRUD API coverage** — GET POST PATCH DELETE with schema validation

---

## Test Coverage

| Suite | Tests | Type |
|-------|-------|------|
| Login — valid, invalid, parametrized | 7 | UI + POM |
| Checkboxes — state, interaction | 3 | UI + POM |
| API users — CRUD lifecycle | 3 | API |
| API challenge — schema, parametrized | 16 | API |
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

# Run all tests
pytest tests/ -v

# Run UI tests only
pytest tests/ui/ -v --headed

# Run API tests only
pytest tests/api/ -v
```

---

## CI/CD Pipeline

GitHub Actions runs automatically on every push to `main`:

- **API Tests** — runs in ~12s, no browser needed
- **Playwright UI Tests** — installs Chromium, runs full suite ~45s
- Screenshots uploaded as artifacts on any failure

---

## Test Sites

- UI tests → [The Internet](https://the-internet.herokuapp.com) — purpose-built test practice site
- API tests → [ReqRes](https://reqres.in) — hosted REST API for testing

---
