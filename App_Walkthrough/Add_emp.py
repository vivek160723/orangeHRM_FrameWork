from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from pages.login_page import LoginPage

# Read data from Excel
df = pd.read_excel('/Users/vivekkumar/Downloads/employee_data.xlsx')  # Replace with the actual path to your Excel file

# Extract the first row data (adjust accordingly if your data is in multiple rows)
first_name = df.iloc[0]['First Name']  # Replace 'First Name' with the exact column name from your Excel sheet
last_name = df.iloc[0]['Last Name']    # Replace 'Last Name' with the exact column name from your Excel sheet
employee_id = df.iloc[0]['Employee ID']  # Replace 'Employee ID' with the exact column name from your Excel sheet

# Open Safari Browser
driver = webdriver.Safari()
driver.maximize_window()

# Step 1: Navigate to the OrangeHRM demo login page
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# Step 2: Verify that we are on the login page
assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

# Step 3: Use POM for login
login_page = LoginPage(driver)
login_page.enter_username("Admin")
login_page.enter_password("admin123")
login_page.click_login()


time.sleep(5)

# Step 4: Verify successful login
assert "dashboard" in driver.current_url.lower(), "Login Failed!"
print("✅ Login successful!")

# Step 5: Navigate to the PIM section
pim_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'))
)
pim_menu.click()
time.sleep(2)

# Step 6: Click the "Add" button
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
)
add_button.click()
time.sleep(2)

# Step 7: Fill in employee details using data from Excel
first_name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))
)
last_name_field = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
employee_id_field = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')

first_name_field.send_keys(first_name)
last_name_field.send_keys(last_name)
employee_id_field.send_keys(str(employee_id))  # Ensure employee ID is a string
time.sleep(2)

# Click Next button
next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
next_button.click()
time.sleep(6)

# Search employee
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(first_name)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
time.sleep(5)

print("✅ Employee added and searched successfully!")


driver.quit()
