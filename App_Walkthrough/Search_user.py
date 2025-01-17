import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Safari Browser
driver = webdriver.Safari()
driver.maximize_window()

# Step 1: Directly navigate to OrangeHRM demo login page
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)  # Allow the page to load completely

# Step 2: Verify we are on the login page
assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

# Step 3: Enter login credentials
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()

# Step 4: Validate login success
wait.until(EC.url_contains("dashboard"))
time.sleep(3)  # Wait to ensure dashboard fully loads
print("✅ Login successful!")

# Step 5: Navigate to 'Admin' section
admin_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
admin_tab.click()
time.sleep(3)  # Allow the Admin page to load
print("✅ Navigated to Admin panel!")

# Function to enter user details
def enter_user_details():
    try:
        # Enter Username
        user_add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')))
        user_add.clear()
        user_add.send_keys("Radha")
        time.sleep(2)

        # Select 'User Role' dropdown and select role
        user_role_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="searchSystemUser[userType]"]')))
        user_role_dropdown.click()
        user_role_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[text()="Admin"]')))
        user_role_option.click()
        time.sleep(2)

        print("✅ Username and User Role Entered")
    except Exception as e:
        print(f"❌ Error entering user details: {e}")

# Call the function to enter user details
enter_user_details()

try:
    # Enter Employee Name
    e_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input')))
    e_name.clear()
    e_name.send_keys("Radha Radha")
    time.sleep(2)
    print("✅ Employee Name Entered")

    # Select 'Status' dropdown
    status_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Status")]/following::div[1]')))
    status_dropdown.click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Enabled"]'))).click()
    print("✅ Selected Status: Enabled")

    # Click Search Button
    # Find the search button using CSS Selector instead of XPath
    # Find the search button using CSS Selector
    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary"))
    )
    search_button.click()
    time.sleep(5)
    print("✅ User Search Successful!")

except Exception as e:
    print(f"❌ Error during search process: {e}")

# Step 10: Close the browser
time.sleep(5)  # Allow user to see search results before closing
driver.quit()