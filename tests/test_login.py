from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    login = LoginPage(driver)
    inv = InventoryPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    assert inv.is_logged_in()
