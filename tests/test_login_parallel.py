import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of browsers you want to run the test in
browsers = ["chrome", "safari"]

@pytest.mark.parametrize("browser", browsers)
def test_login_parallel(browser):
    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "safari":
            driver = webdriver.Safari()
        else:
            raise ValueError(f"Browser {browser} is not supported.")

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Wait until username field is present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        # Verify we are on the login page
        assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

        # Enter login credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        login_button.click()

        # Wait until dashboard loads (or some element on dashboard appears)
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

        # Validate login success
        assert "dashboard" in driver.current_url.lower(), "Login Failed!"
        print(f"✅ Login successful on {browser}!")

        # Search functionality
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'))
        )
        search.send_keys("Pim")
        print(f"✅ Successfully searched on {browser}")

    except Exception as e:
        print(f"An error occurred on {browser}: {e}")

    finally:
        driver.quit()
