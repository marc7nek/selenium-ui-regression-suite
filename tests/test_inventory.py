import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_inventory_page(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return inventory_page


@pytest.mark.smoke
@pytest.mark.regression
def test_inventory_page_displays_products(logged_in_inventory_page):
    assert logged_in_inventory_page.get_page_title() == "Products"
    assert logged_in_inventory_page.get_inventory_count() > 0


@pytest.mark.regression
def test_user_can_add_item_to_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_backpack_to_cart()

    assert logged_in_inventory_page.get_cart_badge_count() == "1"


@pytest.mark.regression
def test_user_can_remove_item_from_cart(logged_in_inventory_page):
    logged_in_inventory_page.add_backpack_to_cart()
    logged_in_inventory_page.remove_backpack_from_cart()

    product_names = logged_in_inventory_page.get_product_names()
    assert "Sauce Labs Backpack" in product_names


@pytest.mark.regression
def test_products_can_be_sorted_by_name_z_to_a(logged_in_inventory_page):
    logged_in_inventory_page.sort_products("Name (Z to A)")
    product_names = logged_in_inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True)
