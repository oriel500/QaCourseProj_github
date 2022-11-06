from time import sleep
from selenium import webdriver  # Import webdriver
from selenium.webdriver.chrome.service import Service  # Import Object chrome services location
from selenium.webdriver.common.by import By  # Import By
from selenium.webdriver.common.keys import Keys  # Import Keys


# ===Selenium3===
# driver_chrome = webdriver.Chrome(executable_path=r"C:\seleniumQA7\chromedriver.exe",options=options_chrome)

# ===Selenium4===
# SetUp options
# from selenium.webdriver.chrome.options import Options
# options_chrome = Options()
# options_chrome.add_experimental_option("detach", True)

# Create webdriver chrome with Service object
service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver_chrome = webdriver.Chrome(service=service_chrome)

# ===Start test===
driver_chrome.get("https://www.google.com/")
driver_chrome.maximize_window()
driver_chrome.implicitly_wait(3)

search_line = driver_chrome.find_element(By.NAME, "q")
search_line.send_keys("python")
sleep(0.5)
search_line.clear()
sleep(0.5)
search_line.send_keys("java")
sleep(0.5)
search_line.clear()
sleep(0.5)
search_line.send_keys("Hello World")
search_line.send_keys(Keys.ENTER)

search_line2 = driver_chrome.find_element(By.CSS_SELECTOR, "input.gLFyf")
result_str = search_line2.get_attribute("value")
expected_str = "Hello World"

# Check "Hello World" in the search line
if result_str == expected_str:
    print("Test Pass")
else:
    print(f"Test Fail, Expected: {expected_str}")

driver_chrome.back()


# Check write "Gmail" in the main page
gmail_title_element = driver_chrome.find_element(By.CSS_SELECTOR, "[class='gb_d'][data-pid='23']")
result_str = gmail_title_element.text
expected_str = "Gmail"
if result_str == expected_str:
    print("Test Pass")
else:
    print(f"Test Fail, Expected: {expected_str}")

sleep(1)
