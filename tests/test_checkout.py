import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

#@pytest.mark.skip(reason="not implemented")
def test_end_to_end_checkout(driver):
    # Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(driver)
    assert inventory.is_logged_in(), "Inventory did not load after login"

    # Add product
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    # Cart page
    cart = CartPage(driver)
    items = cart.get_cart_items_texts()
    assert any("Sauce Labs Backpack" in t for t in items), "Product is not in the cart"

    cart.proceed_to_checkout()

    # Checkout
    checkout = CheckoutPage(driver)
    checkout.enter_customer_info("Abdul ur Rehman", "Chattha", "60600")

    assert checkout.is_overview_visible(), "Overview page did not appear"

    checkout.finish_checkout()

    assert checkout.is_complete(), "Order completion message not found"
