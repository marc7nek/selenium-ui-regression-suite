from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
