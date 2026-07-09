from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_inventory_count(self):
        return len(self.find_all(self.INVENTORY_ITEMS))

    def add_product_to_cart(self, product_name):
        self._click_product_button(product_name, expected_action="Add to cart")

    def add_backpack_to_cart(self):
        self.add_product_to_cart("Sauce Labs Backpack")

    def remove_product_from_cart(self, product_name):
        self._click_product_button(product_name, expected_action="Remove")

    def remove_backpack_from_cart(self):
        self.remove_product_from_cart("Sauce Labs Backpack")

    def get_cart_badge_count(self):
        badge = self.find_optional(self.CART_BADGE)
        return badge.text if badge else "0"

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_products(self, visible_text):
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(visible_text)

    def get_product_names(self):
        elements = self.find_all(self.INVENTORY_ITEM_NAMES)
        return [element.text for element in elements]

    def _click_product_button(self, product_name, expected_action):
        for item in self.find_all(self.INVENTORY_ITEMS):
            name = item.find_element(*self.INVENTORY_ITEM_NAME).text
            if name != product_name:
                continue

            button = item.find_element(*self.INVENTORY_ITEM_BUTTON)
            if button.text != expected_action:
                raise ValueError(
                    f"Product '{product_name}' action is '{button.text}', "
                    f"expected '{expected_action}'."
                )

            button.click()
            return

        raise ValueError(f"Product '{product_name}' was not found on inventory page.")
