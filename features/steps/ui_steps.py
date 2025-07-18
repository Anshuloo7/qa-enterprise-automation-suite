from behave import given, when, then
from pages.admin_page import AdminPage
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
    context.admin_page = AdminPage(context.driver)

@then('I should see the dashboard')
def step_verify_dashboard(context):
    assert context.login_page.is_dashboard_visible(), "Dashboard was not visible after login"

@when('I search for user "{username}" in the Admin panel')
def step_search_user(context, username):
    context.admin_page.go_to_admin()
    context.admin_page.search_user(username)

@then('I should see user "{username}" in the search results')
def step_validate_user(context, username):
    assert context.admin_page.is_user_present_in_results(username), f"User {username} not found in results"
