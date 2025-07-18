# features/environment.py
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.logger_setup import setup_logger
from utils.selenium_utils import DriverFactory
from utils.db_utils import DBUtils
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
import os

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def before_all(context):
    context.logger = setup_logger()
    context.logger.info("=== Test Execution Started ===")

    env = context.config.userdata.get("env")
    context.env_config = load_config(env)

    # Initialize DB
    context.db = DBUtils()
    context.logger.info("SQLite DB initialized.")

def before_scenario(context, scenario):
    context.test_data = {"payments": load_test_data("payments.yaml")}
    context.db.clear_table()  # Clear data before each scenario
    context.logger.info(f"Starting scenario: {scenario.name}")

    if "ui" in scenario.effective_tags:
        context.driver = DriverFactory.get_driver()
        context.logger.info("Selenium WebDriver initialized for UI test")

def after_scenario(context, scenario):
    context.logger.info(f"Scenario '{scenario.name}' - Status: {scenario.status}")

    # Attach logs
    log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "behave.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as log_file:
            attach(log_file.read(), name="Execution Log", attachment_type=AttachmentType.TEXT)

    if scenario.status == "failed" and "ui" in scenario.effective_tags:
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"{scenario.name}.png")
        if context.driver:
            context.driver.save_screenshot(screenshot_path)
            attach.file(screenshot_path, name="UI Failure Screenshot", attachment_type=AttachmentType.PNG)

    if "ui" in scenario.effective_tags:
        DriverFactory.quit_driver()

def after_all(context):
    context.db.close()
    context.logger.info("SQLite DB connection closed.")
    context.logger.info("=== Test Execution Completed ===")