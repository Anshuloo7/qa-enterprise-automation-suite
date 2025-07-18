from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    SEARCH_USERNAME_FIELD = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    SEARCH_RESULT_CELL = lambda self, username: (By.XPATH, f"//div[contains(text(), '{username}')]")

    def go_to_admin(self):
        self.click(self.ADMIN_MENU)

    def search_user(self, username):
        self.type(self.SEARCH_USERNAME_FIELD, username)
        self.click(self.SEARCH_BUTTON)

    def is_user_present_in_results(self, username):
        return self.is_visible(self.SEARCH_RESULT_CELL(username))
