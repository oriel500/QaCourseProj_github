from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

# Login
userName_editbox = driver.find_element(By.NAME, "userName")
password_editbox = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

userName_editbox.send_keys("tutorial")
password_editbox.send_keys("tutorial")
submit_button.click()

# Check if login successes
login_text = driver.find_element(By.TAG_NAME, "h3").text
if login_text == "Login Successfully":
    print("Test login pass")
else:
    print(f"Test fail, Excepted: {login_text}")

# Enter to flights page
driver.find_element(By.LINK_TEXT, "Flights").click()
sleep(0.5)

# Close the ad
try:
    driver.find_element(By.CSS_SELECTOR, "div#card>div>div.btn").click()
    print("Have ad")
    sleep(0.5)
except:
    print("Not have ad")
    pass

# Choose one way and First class
driver.find_element(By.CSS_SELECTOR, "[value='oneway']").click()
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "[value='First']").click()
sleep(0.5)
driver.find_element(By.NAME, "findFlights").click()
sleep(0.5)
