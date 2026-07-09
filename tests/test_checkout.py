import pytest


@pytest.mark.checkout
@pytest.mark.regression
def test_checkout_requires_first_name(checkout_page_with_item):
    checkout_page_with_item.continue_checkout()

    assert "First Name is required" in checkout_page_with_item.get_error_message()


@pytest.mark.checkout
@pytest.mark.smoke
def test_checkout_requires_last_name(checkout_page_with_item):
    checkout_page_with_item.enter_first_name("Anna")
    checkout_page_with_item.continue_checkout()

    assert "Last Name is required" in checkout_page_with_item.get_error_message()


@pytest.mark.checkout
@pytest.mark.regression
def test_checkout_requires_postal_code(checkout_page_with_item):
    checkout_page_with_item.enter_first_name("Anna")
    checkout_page_with_item.enter_last_name("Tester")
    checkout_page_with_item.continue_checkout()

    assert "Postal Code is required" in checkout_page_with_item.get_error_message()


@pytest.mark.checkout
@pytest.mark.regression
def test_checkout_overview_displays_order_summary(checkout_page_with_item):
    checkout_page_with_item.fill_customer_information(
        first_name="Anna",
        last_name="Tester",
        postal_code="12345",
    )
    checkout_page_with_item.continue_checkout()

    assert checkout_page_with_item.get_page_title() == "Checkout: Overview"
    assert checkout_page_with_item.get_checkout_item_names() == ["Sauce Labs Backpack"]
    assert checkout_page_with_item.get_summary_subtotal() == "Item total: $29.99"
    assert checkout_page_with_item.get_summary_tax() == "Tax: $2.40"
    assert checkout_page_with_item.get_summary_total() == "Total: $32.39"


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
