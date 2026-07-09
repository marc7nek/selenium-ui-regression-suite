import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if not headed:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
        driver.set_window_size(1440, 900)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_inventory_page(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    return inventory_page


@pytest.fixture
def checkout_page_with_item(logged_in_inventory_page):
    cart_page = CartPage(logged_in_inventory_page.driver)
    checkout_page = CheckoutPage(logged_in_inventory_page.driver)

    logged_in_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_inventory_page.open_cart()
    cart_page.start_checkout()

    return checkout_page
