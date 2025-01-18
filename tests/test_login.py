
import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils.driver_factory import init_driver
from utils.logger import setup_logger

logger = setup_logger()

@pytest.mark.login
def test_valid_login():
    driver = init_driver(browser="chrome")
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # assert "Dashboard" in driver.title, "Login failed: Dashboard not found in title"
    finally:
        driver.quit()

@pytest.mark.login
def test_invalid_login():
    driver = init_driver(browser="chrome")
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login_page = LoginPage(driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_pass")
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Invalid credentials" in error_message, f"Unexpected error message: {error_message}"
    finally:
        driver.quit()

@pytest.mark.login
def test_empty_username_and_password():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing empty username and password...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Required" in error_message, "Error message for empty fields is not displayed correctly."
    finally:
        driver.quit()

@pytest.mark.login
def test_empty_username():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing empty username...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("")
        login_page.enter_password("admin123")
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Required" in error_message, "Error message for empty username is not displayed correctly."
    finally:
        driver.quit()

@pytest.mark.login
def test_empty_password():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing empty password...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("")
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Required" in error_message, "Error message for empty password is not displayed correctly."
    finally:
        driver.quit()


@pytest.mark.login
def test_logout_functionality():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing logout functionality...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Logout process (adjust selector for logout as per actual DOM structure)
        logout_button = driver.find_element(By.XPATH, "//a[contains(@href, 'logout')]")
        logout_button.click()

        # Verify user is redirected to login page
        assert "login" in driver.current_url, "Logout failed: User is not redirected to login page."
    finally:
        driver.quit()

@pytest.mark.login
def test_login_with_special_characters():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing login with special characters in username...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("!@#$%^&*()")
        login_page.enter_password("admin123")
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Invalid credentials" in error_message, "Special characters test failed: Unexpected behavior."
    finally:
        driver.quit()

@pytest.mark.login
def test_login_with_max_length_inputs():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing login with maximum input length...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        max_length_username = "a" * 255
        max_length_password = "b" * 255

        login_page = LoginPage(driver)
        login_page.enter_username(max_length_username)
        login_page.enter_password(max_length_password)
        login_page.click_login()

        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message, "Max length test failed: Unexpected behavior."
    finally:
        driver.quit()

@pytest.mark.login
def test_login_with_sql_injection():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing login with SQL injection attempt...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        sql_injection_username = "' OR '1'='1"
        sql_injection_password = "' OR '1'='1"

        login_page = LoginPage(driver)
        login_page.enter_username(sql_injection_username)
        login_page.enter_password(sql_injection_password)
        login_page.click_login()

        # error_message = login_page.get_error_message()
        # assert "Invalid credentials" in error_message, "SQL injection test failed: Application may be vulnerable."
    finally:
        driver.quit()

@pytest.mark.login
def test_login_button_disabled_without_input():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing if login button is disabled without input...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        assert not login_button.is_enabled(), "Login button should be disabled without input."
    finally:
        driver.quit()

@pytest.mark.login
def test_valid_username_invalid_password():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing valid username with invalid password...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("wrong_password")
        login_page.click_login()

        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message, "Valid username with invalid password test failed."
    finally:
        driver.quit()

@pytest.mark.login
def test_login_redirect_to_dashboard_url():
    driver = init_driver(browser="chrome")
    try:
        logger.info("Testing login redirect to dashboard...")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        assert driver.current_url.endswith("/dashboard"), "Redirect to dashboard failed after login."
    finally:
        driver.quit()
