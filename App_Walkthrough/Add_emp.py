from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

# Step 5: Navigate to the PIM section in the sidebar
pim_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'))
)
pim_menu.click()
time.sleep(2)

# Step 6: Click the "Add" button to add a new employee
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
)
add_button.click()
time.sleep(2)

# Step 7: Fill in the employee details
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))
)
last_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
employee_id = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')

# Input employee information
first_name.send_keys("Gaurav")
last_name.send_keys("Kumar")
employee_id.send_keys("12345")
time.sleep(2)

# Click the "Next" button to proceed
next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
next_button.click()
time.sleep(6)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
time.sleep(4)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Gaurav")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
time.sleep(5)

print("✅ ")

# Step 11: Quit the driver after completing the task
driver.quit()