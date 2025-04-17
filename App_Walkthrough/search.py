from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Open Safari Browser (Desktop Mode)
    driver = webdriver.Safari()
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
    print("✅ Login successful on Desktop!")

    Search = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
    Search.send_keys("Pim")
    time.sleep(3)
    print("✅ successfully searched")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()