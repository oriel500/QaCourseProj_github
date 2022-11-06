from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver_chrome = webdriver.Chrome(service=service_chrome)
driver_chrome.maximize_window()
driver_chrome.implicitly_wait(20)

# Enter to login page
driver_chrome.get("https://phptravels.net/api/admin")
email_editbox = driver_chrome.find_element(By.CSS_SELECTOR, "input[name='email'][type='text']")
password_editbox = driver_chrome.find_element(By.NAME, "password")
email_editbox.send_keys("admin@phptravels.com")
password_editbox.send_keys("demoadmin")
password_editbox.send_keys(Keys.ENTER)

# Check if dashboard appear in the page
dashboard_text = driver_chrome.find_element(By.CSS_SELECTOR, "[class='text-uppercase font-monospace']")
result = dashboard_text.text
expected = "DASHBOARD"
if result == expected:
    print("Test login Pass")
else:
    print(f"Test login Fail: Expected: {expected}")

user_icon_button = driver_chrome.find_element(By.CSS_SELECTOR, "#dropdownMenuProfile > i:nth-child(1)")
sleep(0.5)
user_icon_button.click()
logout_button = driver_chrome.find_element(By.CSS_SELECTOR, "[href= 'https://phptravels.net/api/admin/logout']")
sleep(0.5)
logout_button.click()

# Check if login page appear
login_text = driver_chrome.find_element(By.CSS_SELECTOR, "[class = 'display-5 mb-0']")
result = login_text.text
expected = "Login"
if result == expected:
    print("Test logout Pass")
else:
    print(f"Test logout Fail: Expected: {expected}")

sleep(1)