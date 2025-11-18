from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.backpack_add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def is_logged_in(self):
        return self.wait.until(EC.visibility_of_element_located(self.inventory_list))

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.backpack_add_btn)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def logout(self):
        """Logs out the current user"""
        self.wait.until(EC.element_to_be_clickable(self.burger_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
