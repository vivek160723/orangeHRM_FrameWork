import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

# Read Excel file with multiple rows
df = pd.read_excel("/Users/vivekkumar/Downloads/employee_data.xlsx")

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# Login
login_page = LoginPage(driver)
login_page.enter_username("Admin")
login_page.enter_password("admin123")
login_page.click_login()
WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
print("✅ Logged in successfully!")

## Iterate through each employee in Excel
for index, row in df.iterrows():
    first_name = row['First Name']
    last_name = row['Last Name']
    employee_id = str(row['Employee ID'])

    # Navigate to PIM section
    pim_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))
    )
    pim_menu.click()
    time.sleep(1)

    # Click Add
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Add"]'))
    )
    add_button.click()

    # Fill details
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'firstName'))
    )
    last_name_field = driver.find_element(By.NAME, 'lastName')
    employee_id_field = driver.find_element(By.XPATH, '//label[text()="Employee Id"]/../following-sibling::div/input')

    first_name_field.clear()
    first_name_field.send_keys(first_name)

    last_name_field.clear()
    last_name_field.send_keys(last_name)

    employee_id_field.clear()
    employee_id_field.send_keys(employee_id)

    # Click Save (submit)
    next_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    next_button.click()

    # Small wait for form to submit
    time.sleep(2)

    print(f"✅ Employee '{first_name} {last_name}' added successfully.")

    # 🛑 IMPORTANT: After adding, return to PIM list
    pim_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))
    )
    pim_menu.click()
    time.sleep(1)
