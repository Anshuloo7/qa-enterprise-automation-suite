from behave import given, when, then
from utils.selenium_utils import DriverFactory
from pages.login_page import LoginPage

@given('I am on the OrangeHRM login page')
def step_open_login(context):
    driver = DriverFactory.get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    context.login_page = LoginPage(driver)

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)

@then('I should see the dashboard')
def step_verify_dashboard(context):
    assert context.login_page.is_dashboard_visible(), "Dashboard was not visible after login"