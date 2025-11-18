from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_btn = (By.ID, "checkout")   # using ID instead of CSS
        self.continue_shopping = (By.ID, "continue-shopping")

    def get_cart_items_texts(self):
        self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        elements = self.driver.find_elements(*self.cart_items)
        return [e.text for e in elements]

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_btn)).click()

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.cart_items)) == 0
