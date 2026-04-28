from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_inventory_count(self):
        return len(self.find_all(self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_products(self, visible_text):
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(visible_text)

    def get_product_names(self):
        elements = self.find_all(self.INVENTORY_ITEM_NAMES)
        return [element.text for element in elements]
