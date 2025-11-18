from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--force-device-scale-factor=1")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    return driver
