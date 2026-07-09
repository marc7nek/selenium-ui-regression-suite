from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def continue_checkout(self):
        self.js_click(self.CONTINUE_BUTTON)

    def enter_first_name(self, first_name):
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def fill_customer_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def finish_checkout(self):
        self.js_click(self.FINISH_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_checkout_item_names(self):
        elements = self.find_all(self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def get_summary_subtotal(self):
        return self.get_text(self.SUMMARY_SUBTOTAL)

    def get_summary_tax(self):
        return self.get_text(self.SUMMARY_TAX)

    def get_summary_total(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
