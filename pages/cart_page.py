from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.cart_items = (By.CSS_SELECTOR, "div.cart_item")
        self.checkout_btn = (By.ID, "checkout")   # using ID instead of CSS
        self.continue_shopping = (By.ID, "continue-shopping")

    def get_cart_items_texts(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.cart_items)
        )

        return [item.text.strip() for item in items]

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_btn)).click()

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.cart_items)) == 0
