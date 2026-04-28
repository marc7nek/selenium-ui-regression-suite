import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def checkout_page_with_item(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.start_checkout()

    return checkout_page


@pytest.mark.checkout
@pytest.mark.regression
def test_checkout_requires_first_name(checkout_page_with_item):
    checkout_page_with_item.continue_checkout()

    assert "First Name is required" in checkout_page_with_item.get_error_message()


@pytest.mark.checkout
@pytest.mark.smoke
def test_user_can_complete_checkout(checkout_page_with_item):
    checkout_page_with_item.fill_customer_information(
        first_name="Anna",
        last_name="Tester",
        postal_code="12345",
    )
    checkout_page_with_item.continue_checkout()
    checkout_page_with_item.finish_checkout()

    assert checkout_page_with_item.get_complete_message() == "Thank you for your order!"
