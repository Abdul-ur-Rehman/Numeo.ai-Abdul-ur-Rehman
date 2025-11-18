import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.inventory
def test_inventory_page_items(driver):
    """
    Test to verify inventory page loads correctly and products can be added to cart.
    """
    # Login first
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Open Inventory Page
    inventory = InventoryPage(driver)

    # Verify user is logged in and inventory is visible
    assert inventory.is_logged_in(), "Inventory page not visible after login"

    # Verify at least one product is visible
    products = inventory.get_product_names()
    assert len(products) > 0, "No products found on inventory page"

    # Add a product to cart (e.g., Sauce Labs Backpack)
    inventory.add_backpack_to_cart()

    # Verify the product was added to cart
    cart_count = inventory.get_cart_count()
    assert cart_count == 1, "Cart count should be 1 after adding a product"
