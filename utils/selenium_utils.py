from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")  # Remove this line if you want to see the browser
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            cls._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None