import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
time.sleep(5)

driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
namebox = driver.find_element(By.NAME, 'username')
namebox.send_keys("Admin")
time.sleep(5)
password = driver.find_element(By.NAME, 'password')
password.send_keys("admin123")
time.sleep(5)
button1 = driver.find_element(By.CLASS_NAME, "oxd-button")
button1.click()
time.sleep(5)
admin=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
admin.click()
time.sleep(2)
namebox=driver.find_element(By.CLASS_NAME,'oxd-input')
namebox.send_keys("Divya")
time.sleep(5)
userrole=Select(driver.find_element(By.CLASS_NAME,'oxd-select-text-input'))
userrole.select_by_value("Admin")
time.sleep(5)
en=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input")
en.send_keys("Divya101")
status=Select(driver.find_element(By.XPATH,"oxd-select-text-input"))
status.select_by_value("Enabled")
button=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
button.click()