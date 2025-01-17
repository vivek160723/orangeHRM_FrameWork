import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def setup():
    """Setup fixture to initialize and quit the browser."""
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_orangehrm_login(setup):
    driver = setup

    # Step 1: Navigate to OrangeHRM demo login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)

    # Step 2: Verify we are on the login page
    assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

    # Step 3: Enter login credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    login_button.click()
    time.sleep(5)

    # Step 4: Validate login success
    assert "dashboard" in driver.current_url.lower(), "Login Failed!"
    print("✅ Login successful on Desktop!")


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

    # Step 3: Validate the search results (if applicable)
    assert "pim" in driver.page_source.lower(), "Valid search term did not produce results!"
    print("✅ Valid search successful")


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
    search.send_keys("@12")
    time.sleep(3)

    # Step 3: Validate no results are shown
    assert "no records found" in driver.page_source.lower() or "InvalidTerm" not in driver.page_source.lower(), \
        "Invalid search term produced results unexpectedly!"
    print("✅ Invalid search handled correctly")


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
    assert "pim" in driver.page_source.lower(), "Case-insensitive search failed!"
    print("✅ Case-insensitive search successful")
def login(driver):
    """Reusable function to log in to the OrangeHRM website."""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)


def test_empty_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Leave search field empty and press enter
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("")
    time.sleep(2)

    # Step 3: Validate no change in results or default behavior
    if "dashboard" in driver.current_url.lower():
        print("✅ Empty search handled correctly")
    else:
        print("❌ Empty search caused unexpected behavior!")


def test_special_character_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search with special characters
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("!@#$%^&*()")
    time.sleep(3)

    # Step 3: Validate no results are shown
    if "no records found" in driver.page_source.lower():
        print("✅ Special character search handled correctly")
    else:
        print("❌ Special character search produced unexpected results!")


def test_numeric_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search with numeric input
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("12345")
    time.sleep(3)

    # Step 3: Validate no results or appropriate response
    if "no records found" in driver.page_source.lower():
        print("✅ Numeric search handled correctly")
    else:
        print("❌ Numeric search produced unexpected results!")


def test_whitespace_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search with only spaces
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("     ")
    time.sleep(2)

    # Step 3: Validate no change in results or appropriate response
    if "dashboard" in driver.current_url.lower():
        print("✅ Whitespace search handled correctly")
    else:
        print("❌ Whitespace search caused unexpected behavior!")


def test_partial_match_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search with a partial match (e.g., 'Pi' instead of 'Pim')
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("Pi")
    time.sleep(3)

    # Step 3: Validate partial match results
    if "pim" in driver.page_source.lower():
        print("✅ Partial match search successful")
    else:
        print("❌ Partial match search failed!")


def test_search_field_clear(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search for a term and then clear the field
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys("Pim")
    time.sleep(2)
    search.clear()
    time.sleep(2)

    # Step 3: Validate field cleared and behavior reset
    if search.get_attribute("value") == "":
        print("✅ Search field cleared successfully")
    else:
        print("❌ Search field not cleared successfully!")


def test_long_text_search(setup):
    driver = setup

    # Step 1: Log in
    login(driver)

    # Step 2: Search with a very long string
    long_text = "a" * 500
    search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    search.send_keys(long_text)
    time.sleep(3)

    # Step 3: Validate no crash or unexpected behavior
    if "no records found" in driver.page_source.lower():
        print("✅ Long text search handled correctly")
    else:
        print("❌ Long text search caused unexpected behavior!")

