from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url=None):
        self.driver.get(url or self.BASE_URL)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_optional(self, locator, timeout=2):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return None

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        if element.get_attribute("value") == text:
            return

        self.driver.execute_script(
            """
            const element = arguments[0];
            const value = arguments[1];
            const setter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype,
                "value"
            ).set;

            setter.call(element, value);
            element.dispatchEvent(new Event("input", { bubbles: true }));
            element.dispatchEvent(new Event("change", { bubbles: true }));
            """,
            element,
            text,
        )

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_current_url(self):
        return self.driver.current_url
