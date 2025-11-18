import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.inventory
def test_inventory_page_add_to_cart(driver):
    """
    Test to verify inventory page loads correctly and the Sauce Labs Backpack
    can be added to the cart.
    """
    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Initialize InventoryPage
    inventory = InventoryPage(driver)

    # Step 3: Verify inventory page is visible
    assert inventory.is_logged_in(), "Inventory page not visible after login"

    # Step 4: Add backpack to cart
    inventory.add_backpack_to_cart()

    # Step 5: Open cart and verify backpack is present
    inventory.open_cart()

    # Use correct Selenium By strategy
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge) > 0 and cart_badge[0].text == "1", "Backpack was not added to cart"
