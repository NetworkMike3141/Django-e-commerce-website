from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time

# Set up the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("https://www.google.com/")

# Wait up to 10 seconds until the element is interactable
wait = WebDriverWait(driver, 100)
input_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]/div')))

# Check if the element is enabled (i.e., clickable)
if input_element.is_enabled():
    input_element.click()
    print("Element is clickable. Clicked successfully!")
else:
    print("Element is not clickable.")

# Rest of your code
time.sleep(5)

# Close the browser
driver.quit()
