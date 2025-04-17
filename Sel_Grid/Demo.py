from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define the Selenium Grid Hub URL with your IP address
grid_url = "http://192.168.0.8:4444/wd/hub"

# Define desired capabilities for the browser
capabilities = DesiredCapabilities.CHROME  # Replace with FIREFOX, EDGE, etc., as needed

# Create a remote WebDriver session
driver = webdriver.Remote(
    command_executor=grid_url,
    desired_capabilities=capabilities
)

# Open a website
driver.get("https://www.example.com")

# Print the title of the webpage
print("Page title is:", driver.title)

# Close the browser
driver.quit()