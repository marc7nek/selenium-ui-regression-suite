# Selenium UI Regression Suite

The Python Selenium UI automation project using **PyTest**, **Page Object Model**, and **HTML reporting**.

This project tests a demo e-commerce web application: [SauceDemo](https://www.saucedemo.com/)

## Project Goals

This project demonstrates practical QA Automation skills:

- Browser automation with Selenium
- Automated test scripts with Python and PyTest
- Page Object Model design pattern
- Web validation using HTML/CSS selectors
- Test result reporting with `pytest-html`
- CI/CD execution with GitHub Actions
- Clear QA documentation and defect-style thinking

## Stack

- Python 3.10+
- Selenium
- PyTest
- webdriver-manager
- pytest-html
- PyGithub

## Test Coverage

### Login Tests

- Valid user can log in
- Invalid user sees an error message
- Locked out user sees an error message

### Inventory Tests

- Inventory page loads after login
- User can add an item to the cart
- User can remove an item from the cart
- Cart badge updates correctly
- Product sorting works

### Cart and Checkout Tests

- User can open cart
- Checkout form validates missing first name
- User can complete checkout successfully

## Project Structure

```text
selenium-ui-regression-suite/
│── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
│── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
│
│── .github/
│   └── workflows/
│       └── ui-tests.yml
│
│── conftest.py
│── pytest.ini
│── requirements.txt
│── test_plan.md
│── defects_example.md
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate virtal environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Run all tests:

```bash
pytest
```

Run tests with an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Run only login tests:

```bash
pytest tests/test_login.py
```

Run tests in headed mode:

```bash
pytest --headed
```

Run tests in Chrome:

```bash
pytest --browser chrome
```

Run tests in Firefox:

```bash
pytest --browser firefox
```

## Test Reports

After running:

```bash
pytest --html=reports/report.html --self-contained-html
```

Open:

```text
reports/report.html
```

## CI/CD

This project includes a GitHub Actions workflow.

On every push or pull request to `main`, GitHub Actions will:

1. Install Python
2. Install dependencies
3. Run Selenium tests in headless mode
4. Upload the HTML test report as an artifact

Workflow file:

```text
.github/workflows/ui-tests.yml
```

## Disclaimer

This project uses SauceDemo, a public demo application for test automation practice.
