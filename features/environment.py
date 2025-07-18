import os
from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.logger_setup import setup_logger
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from utils.selenium_utils import DriverFactory
import traceback

# Ensure screenshot directory exists
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def before_all(context):
    context.logger = setup_logger()
    context.logger.info("=== Test Execution Started ===")

    env = context.config.userdata.get("env")
    context.env_config = load_config(env)
    context.logger.info(f"Running tests in environment: {env or 'default'}")

def before_scenario(context, scenario):
    context.test_data = {"payments": load_test_data("payments.yaml")}
    context.logger.info(f"Starting scenario: {scenario.name}")

    # Initialize Selenium driver for @ui tagged scenarios
    if "ui" in scenario.effective_tags:
        context.driver = DriverFactory.get_driver()
        context.logger.info("Selenium WebDriver initialized for UI test")

def before_step(context, step):
    context.logger.info(f"STEP START: {step.keyword} {step.name}")

def after_step(context, step):
    if step.status == "passed":
        context.logger.info(f"STEP PASSED: {step.keyword} {step.name}")
    elif step.status == "failed":
        context.logger.error(f"STEP FAILED: {step.keyword} {step.name} - Error: {step.exception}")

def after_scenario(context, scenario):
    context.logger.info(f"Scenario '{scenario.name}' - Status: {scenario.status}")

    # Attach logs to Allure
    log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "behave.log")
    if os.path.exists(log_path):
        with open(log_path, "r") as log_file:
            attach(log_file.read(), name="Execution Log", attachment_type=AttachmentType.TEXT)

    # UI-specific failure handling
    if scenario.status == "failed" and "ui" in scenario.effective_tags:
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"{scenario.name}.png")
        try:
            context.driver.save_screenshot(screenshot_path)
            attach.file(screenshot_path, name="UI Failure Screenshot", attachment_type=AttachmentType.PNG)
            context.logger.info(f"Screenshot captured: {screenshot_path}")
        except Exception as e:
            context.logger.error(f"Failed to capture screenshot: {e}")

    # Attach detailed failure info
    if scenario.status == "failed":
        # Attach step-level error
        failed_steps = [step for step in scenario.steps if step.status == "failed"]
        for step in failed_steps:
            attach(f"Failed Step: {step.keyword} {step.name}\nError: {step.exception}",
                   name="Step Failure Details",
                   attachment_type=AttachmentType.TEXT)

        # Attach API request & response details (if any)
        if hasattr(context, "response"):
            try:
                attach(
                    f"REQUEST:\n{context.response.request.method} {context.response.request.url}\n"
                    f"Headers: {context.response.request.headers}\n"
                    f"Body: {context.response.request.body}\n\n"
                    f"RESPONSE:\nStatus: {context.response.status_code}\n"
                    f"Headers: {context.response.headers}\n"
                    f"Body: {context.response.text}",
                    name="API Request & Response",
                    attachment_type=AttachmentType.TEXT
                )
            except Exception as e:
                context.logger.error(f"Failed to attach API details: {e}")

    # Quit driver for UI tests
    if "ui" in scenario.effective_tags:
        DriverFactory.quit_driver()
        context.logger.info("Selenium WebDriver closed after UI test")

def after_all(context):
    context.logger.info("=== Test Execution Completed ===")