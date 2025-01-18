from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoAlertPresentException

# Open Safari Browser
driver = webdriver.Safari()
driver.maximize_window()

# Step 1: Navigate to the OrangeHRM demo login page
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# Step 2: Verify that we are on the login page
assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

# Step 3: Enter login credentials and login
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()

# Wait for login to complete
time.sleep(5)

# Step 4: Verify successful login by checking if 'dashboard' is in the URL
assert "dashboard" in driver.current_url.lower(), "Login Failed!"
print("✅ Login successful!")

# Navigate to PIM section
pim_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'))
)
pim_menu.click()
time.sleep(2)

# Click the "Add Employee" button
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
time.sleep(4)

# Fill in employee details
driver.find_element(By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(
    "Gaurav")
time.sleep(2)

# Save the new employee
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
time.sleep(5)

# Click the delete button (assuming there's one employee to delete)
delete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'))
)
delete_button.click()
time.sleep(3)

# Handle the alert
try:
    # Wait for the alert to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div')))

    # Switch to the alert and accept it
    alert = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div')
    print("✅ Alert found")

    # Click the "Yes, Delete" button
    yes_delete_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
    yes_delete_button.click()
    print("✅ Employee deleted")

except NoAlertPresentException:
    print("⚠️ No alert present")
except Exception as e:
    print(f"❌ Error: {e}")

# Quit the driver after completing the task
driver.quit()