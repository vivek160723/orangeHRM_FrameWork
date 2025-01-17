import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup():
    """Setup fixture to initialize and quit the browser."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_orangehrm_login(setup):
    driver = setup

    # Step 1: Navigate to OrangeHRM demo login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)

    # Step 2: Verify we are on the login page
    if "orangehrmlive.com" in driver.current_url:
        print("✅ Navigated to the login page successfully.")
    else:
        print("❌ Failed to navigate to the login page.")

    # Step 3: Enter login credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    login_button.click()
    time.sleep(5)

    # Step 4: Validate login success
    if "dashboard" in driver.current_url.lower():
        print("✅ Login successful on Desktop!")
    else:
        print("❌ Login failed!")

def test_valid_search(setup):
    driver = setup

    # Step 1: Navigate and log in
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 2: Search for a valid term
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("Pim")
    time.sleep(3)

    # Step 3: Validate the search results
    page_source = driver.page_source.lower()
    if "pim" in page_source:
        print("✅ Valid search term produced results.")
    else:
        print("❌ Valid search term did not produce results.")

def test_invalid_search(setup):
    driver = setup

    # Step 1: Navigate and log in
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 2: Search for an invalid term
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("InvalidTerm")
    time.sleep(3)

    # Step 3: Validate no results are shown
    page_source = driver.page_source.lower()
    if "no records found" in page_source or "invalidterm" not in page_source:
        print("✅ Invalid search term handled correctly.")
    else:
        print("❌ Invalid search term produced unexpected results.")

def test_case_insensitive_search(setup):
    driver = setup

    # Step 1: Navigate and log in
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 2: Search for a term with mixed case
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("PiM")
    time.sleep(3)

    # Step 3: Validate the search results are case insensitive
    page_source = driver.page_source.lower()
    if "pim" in page_source:
        print("✅ Case-insensitive search passed.")
    else:
        print("❌ Case-insensitive search failed.")
