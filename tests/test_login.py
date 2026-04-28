import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.login
@pytest.mark.smoke
def test_valid_user_can_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in inventory_page.get_current_url()
    assert inventory_page.get_page_title() == "Products"


@pytest.mark.login
@pytest.mark.regression
def test_invalid_user_sees_error_message(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    assert "Username and password do not match" in login_page.get_error_message()


@pytest.mark.login
@pytest.mark.regression
def test_locked_out_user_sees_error_message(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_message()
