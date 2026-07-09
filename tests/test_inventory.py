import pytest
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.regression
def test_inventory_page_displays_products(logged_in_inventory_page):
    assert logged_in_inventory_page.get_page_title() == "Products"
    assert logged_in_inventory_page.get_inventory_count() > 0


@pytest.mark.regression
def test_user_can_add_item_to_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_product_to_cart("Sauce Labs Backpack")

    assert logged_in_inventory_page.get_cart_badge_count() == "1"


@pytest.mark.regression
def test_user_can_remove_item_from_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_inventory_page.remove_product_from_cart("Sauce Labs Backpack")

    assert logged_in_inventory_page.get_cart_badge_count() == "0"


@pytest.mark.regression
def test_added_items_are_displayed_in_cart(logged_in_inventory_page):
    cart_page = CartPage(logged_in_inventory_page.driver)

    logged_in_inventory_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    logged_in_inventory_page.open_cart()

    assert cart_page.get_cart_item_count() == 2
    assert cart_page.get_cart_item_names() == [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]


@pytest.mark.regression
def test_products_can_be_sorted_by_name_z_to_a(logged_in_inventory_page):
    logged_in_inventory_page.sort_products("Name (Z to A)")
    product_names = logged_in_inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True)
