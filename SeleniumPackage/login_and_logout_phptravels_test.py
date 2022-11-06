from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from time import sleep

service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver_chrome = webdriver.Chrome(service=service_chrome)
driver_chrome.maximize_window()
driver_chrome.implicitly_wait(20)

driver_chrome.get("https://phptravels.net/api/admin")
email_editbox = driver_chrome.find_element(By.CSS_SELECTOR, "input[name='email'][type='text']")
password_editbox = driver_chrome.find_element(By.NAME, "password")
login_button = driver_chrome.find_element(By.CSS_SELECTOR, ".btn-block")

# Enter to login page
email_editbox.send_keys("admin@phptravels.com")
sleep(0.5)
password_editbox.send_keys("demoadmin")
sleep(0.5)
login_button.click()
sleep(0.5)

# Check if dashboard appear in the page
dashboard_text = driver_chrome.find_element(By.CSS_SELECTOR, ".text-uppercase")
result = dashboard_text.text
expected = "DASHBOARD"
if result == expected:
    print("Test login Pass")
else:
    print(f"Test login Fail: Expected: {expected}")

user_icon_button = driver_chrome.find_element(By.CSS_SELECTOR, "#dropdownMenuProfile")
sleep(0.5)
user_icon_button.click()
sleep(0.5)
buttons_menu = driver_chrome.find_elements(By.CSS_SELECTOR, "a.dropdown-item>div.me-3")
buttons_menu[3].click()
sleep(0.5)

# Check if login page appear
login_text = driver_chrome.find_element(By.CSS_SELECTOR, ".text-center>h1>strong")
result = login_text.text
expected = "Login"
if result == expected:
    print("Test logout Pass")
else:
    print(f"Test logout Fail: Expected: {expected}")
