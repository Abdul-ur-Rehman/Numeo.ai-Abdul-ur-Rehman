from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Step 1 - Your Info
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

        # Step 2 - Overview
        self.summary_info = (By.CLASS_NAME, "summary_info")
        self.finish_btn = (By.ID, "finish")

        # Step 3 - Complete Order
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def enter_customer_info(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_btn).click()

    def is_overview_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.summary_info))

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()

    def is_complete(self):
        header = self.wait.until(
            EC.visibility_of_element_located(self.complete_header)
        ).text
        return "Thank you for your order" in header
