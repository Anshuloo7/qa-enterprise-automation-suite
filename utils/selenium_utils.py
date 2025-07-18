import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-software-rasterizer")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--lang=en-US")

            # Detect environment
            if os.path.exists("/.dockerenv"):  # Running inside Docker
                options.binary_location = "/usr/bin/chromium"
                driver_path = "/usr/bin/chromedriver"
            else:  # Running locally
                driver_path = ChromeDriverManager().install()

            cls._driver = webdriver.Chrome(service=Service(driver_path), options=options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None