from selenium import webdriver

from selenium.webdriver.chrome.service import Service

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    #options.add_argument("--headless")
    return webdriver.Chrome(options=options)
