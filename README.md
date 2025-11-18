# Numeo.ai_Abdul-ur-Rehman (Take Home Assignment) — Selenium + Pytest Automation Project

## Project Overview
This repository contains a **Selenium + Pytest automation framework** built to demonstrate end-to-end testing for a web application (SauceDemo). The automation covers critical flows including:

- User login
- Adding products to cart
- Checkout process

The purpose of this project is to showcase **test automation skills**, framework design, and CI/CD integration.

---

## Folder Structure

- **Numeo.ai_Abdul-ur-Rehman/**
  - **pages/**  
    Page Object Models (POM) for modular and reusable page interactions:  
    - `login_page.py` – Login page locators and actions  
    - `inventory_page.py` – Inventory/product page actions  
    - `cart_page.py` – Cart page actions and verification  
    - `checkout_page.py` – Checkout page actions and verifications
  - **utilities/**  
    Helper functions and driver setup:  
    - `driver_factory.py` – Selenium WebDriver setup (headless mode, options)  
  - **tests/**  
    Test cases for different application flows:  
    - `test_login.py` – Test user login flow  
    - `test_inventory.py` – Test inventory/product functionality  
    - `test_cart.py` – Test adding/removing items from cart  
    - `test_checkout.py` – Test checkout process end-to-end
  - `conftest.py` – Pytest fixtures for driver setup and teardown  
  - `requirements.txt` – Python dependencies  
  - `README.md` – Project documentation  
  - `TEST_STRATEGY.md` – QA/Test strategy document  
  - `ARCHITECTURE.md` – Framework architecture and design  
  - `.github/workflows/tests.yml` – GitHub Actions CI/CD workflow

---

## Setup & Installation

### Prerequisites
- Python 3.10+ installed
- Google Chrome installed
- Git (optional, for cloning repo)

### Steps
1. Clone the repository:

```bash
git clone <your-github-repo-url>
cd Numeo.ai_Abdul-ur-Rehman
```
2. Create a virtual environment (recommended):
```python -m venv venv
# Activate environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Install dependencies:
````
pip install --upgrade pip
pip install -r requirements.txt
````
4. Run tests locally:
```
pytest -v --disable-warnings
```

## Test Coverage

- Login flow: Verifies that users can log in with valid credentials.

- Inventory flow: Verifies products are visible and can be added to the cart.

- Cart flow: Verifies cart operations like adding/removing items.

- Checkout flow: Verifies end-to-end checkout with customer information and order completion.

Current submission demonstrates login and inventory flows fully. Cart and checkout flows are structured in the framework and can be expanded.

## Design Decisions
- Pytest: Lightweight, modular, and easy to scale.

- Page Object Model (POM): Separates locators and page actions from test logic.

- Utilities folder: Centralized driver setup and reusable helpers.

- CI/CD: GitHub Actions runs tests automatically on push/PR.

- Headless Chrome: Ensures tests run in CI/CD environments without GUI.

- Stable Locators: IDs, Class Names, and XPaths are used for reliable element selection.

## Future Enhancements
- Add full checkout and cart flow automation.

- Implement API testing for backend verification.

- Generate HTML/Allure test reports integrated with CI/CD.

- Integrate Slack or email notifications for failed tests.
