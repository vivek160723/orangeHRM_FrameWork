import os
import pytest
from utils.driver_factory import init_driver

# This hook is triggered when pytest configures the tests
def pytest_configure(config):
    # No metadata modification, just configuring the tests
    pass

# This hook removes unnecessary metadata from the report
def pytest_metadata(metadata):
    # Remove unnecessary metadata fields
    metadata.pop('Plugins', None)
    metadata.pop('Platform', None)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot for failures during the test call phase
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver is not None:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(file_name)
            print(f"Screenshot saved to {file_name}")



@pytest.fixture
def driver():
    driver = init_driver(browser="chrome")
    yield driver
    driver.quit()