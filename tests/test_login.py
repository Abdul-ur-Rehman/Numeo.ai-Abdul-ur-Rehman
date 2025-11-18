import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.login
class TestLogin:

    #Test suite for login functionality including positive and negative scenarios.

    def test_valid_login(self, driver):

        #Verify user can log in with correct credentials (`standard_user`, `secret_sauce`).

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.load()
        login.login("standard_user", "secret_sauce")

        assert inventory.is_logged_in(), "Login failed or inventory not visible"

    def test_invalid_login(self, driver):

        #Verify proper error message is displayed when using wrong username/password.

        login = LoginPage(driver)
        login.load()
        login.login("invalid_user", "wrong_password")

        error_text = login.get_error_message()
        assert "Username and password do not match" in error_text, "Error message not displayed for invalid login"

    def test_empty_username(self, driver):

        #Verify proper error message when username field is left empty.

        login = LoginPage(driver)
        login.load()
        login.login("", "secret_sauce")

        error_text = login.get_error_message()
        assert "Username is required" in error_text, "No error shown for empty username"

    def test_empty_password(self, driver):

        #Verify proper error message when password field is left empty.

        login = LoginPage(driver)
        login.load()
        login.login("standard_user", "")

        error_text = login.get_error_message()
        assert "Password is required" in error_text, "No error shown for empty password"

    def test_logout(self, driver):

        #Verify user can log out successfully from the inventory page.

        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.load()
        login.login("standard_user", "secret_sauce")

        assert inventory.is_logged_in(), "Login failed"


        inventory.logout()

        assert login.is_login_page_visible(), "Logout failed; login page not visible"
