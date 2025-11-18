from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inv.add_backpack_to_cart()
    inv.open_cart()

    assert "Sauce Labs Backpack" in driver.page_source
