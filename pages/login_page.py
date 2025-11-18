from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

        # Locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.XPATH, "//h3[@data-test='error']")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text

    def is_login_page_visible(self):
        return self.wait.until(EC.element_to_be_clickable(self.login_button))
