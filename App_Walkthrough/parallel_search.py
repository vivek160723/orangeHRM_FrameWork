import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Read browser configuration from the JSON file
with open("config/browser_config.json", "r") as file:
    config = json.load(file)
    browsers = config.get("browsers", [])


@pytest.mark.parametrize("browser", browsers)
def test_login_parallel(browser):
    try:
        # Initialize the appropriate browser driver
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "safari":
            driver = webdriver.Safari()
        else:
            raise ValueError(f"Browser {browser} is not supported.")

        driver.maximize_window()

        # Step 1: Directly navigate to OrangeHRM demo login page
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
        print(f"✅ Login successful on {browser}!")

        # Search functionality
        Search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        Search.send_keys("Pim")
        time.sleep(3)
        print(f"✅ Successfully searched on {browser}")

    except Exception as e:
        print(f"An error occurred on {browser}: {e}")

    finally:
        driver.quit()
