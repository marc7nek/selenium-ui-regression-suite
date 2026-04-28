import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


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
