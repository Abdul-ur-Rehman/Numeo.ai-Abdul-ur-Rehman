from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_logged_in(self):
        return "inventory" in self.driver.current_url

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def open_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart_btn.click()
        time.sleep(1)  # CI-safe wait
        self.driver.execute_script("window.scrollTo(0, 0)")

    def get_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [i.text for i in items]

    def get_cart_count(self):
        badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge[0].text) if badge else 0

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
