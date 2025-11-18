import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.login
class TestLogin:
    """
    Test suite for login functionality including positive and negative scenarios.
    """

    def test_valid_login(self, driver):
        """
        Test login with valid credentials.
        """
        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.load()
        login.login("standard_user", "secret_sauce")

        assert inventory.is_logged_in(), "Login failed or inventory not visible"

    def test_invalid_login(self, driver):
        """
        Test login with invalid credentials.
        """
        login = LoginPage(driver)
        login.load()
        login.login("invalid_user", "wrong_password")

        # Verify error message is displayed
        error_text = login.get_error_message()
        assert "Username and password do not match" in error_text, "Error message not displayed for invalid login"

    def test_empty_username(self, driver):
        """
        Test login with empty username.
        """
        login = LoginPage(driver)
        login.load()
        login.login("", "secret_sauce")

        error_text = login.get_error_message()
        assert "Username is required" in error_text, "No error shown for empty username"

    def test_empty_password(self, driver):
        """
        Test login with empty password.
        """
        login = LoginPage(driver)
        login.load()
        login.login("standard_user", "")

        error_text = login.get_error_message()
        assert "Password is required" in error_text, "No error shown for empty password"

    def test_logout(self, driver):
        """
        Test user can log out successfully.
        """
        login = LoginPage(driver)
        inventory = InventoryPage(driver)

        login.load()
        login.login("standard_user", "secret_sauce")

        assert inventory.is_logged_in(), "Login failed"

        # Perform logout
        inventory.logout()

        # Verify login page is displayed again
        assert login.is_login_page_visible(), "Logout failed; login page not visible"
