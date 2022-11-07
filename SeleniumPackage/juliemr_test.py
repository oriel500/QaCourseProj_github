from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Open the site
service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
wait = WebDriverWait(driver, 10)
driver.get("https://juliemr.github.io/protractor-demo/")
driver.maximize_window()
driver.implicitly_wait(5)

# Fill the fields
numbers = driver.find_elements(By.CSS_SELECTOR, "input.input-small")
number1 = numbers[0]
number2 = numbers[1]
operator = driver.find_element(By.CSS_SELECTOR, "select.ng-pristine")
operator_select = Select(operator)
result = driver.find_element(By.CSS_SELECTOR, "h2")
go_button = driver.find_element(By.CSS_SELECTOR, "#gobutton")

number1_list = ['1', '4', '3']
number2_list = ['1', '2', '2']
operator_list = ['+', '/', '/']

for i in range(3):
    number1.clear()
    number2.clear()
    try:
        history_list = driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
        history_len = len(history_list)
        history_len_now = len(history_list)
    except:
        history_len = 0
        history_len_now = 0
    number1.send_keys(number1_list[i])
    sleep(0.5)
    operator_select.select_by_visible_text(operator_list[i])
    sleep(0.5)
    number2.send_keys(number2_list[i])
    sleep(0.5)
    go_button.click()
    while history_len == history_len_now:
        history_list = driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
        history_len_now = len(history_list)
    # while result.text[0] == '.':
    #     continue
    print(result.text)

# Print the history table
# table = driver.find_element(By.CLASS_NAME, "table")
# rows = table.find_elements(By.TAG_NAME, "tr")
# for row in rows[1:]:
#     cols = row.find_elements(By.TAG_NAME, "td")
#     for col in cols:
#         print(col.text, end="\t")
#     print()



# # 1 + 1 = 2
# number1.send_keys("1")
# sleep(0.5)
# number2.send_keys("1")
# sleep(0.5)
# go_button.click()
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.ng-binding")))
# # while not result.text.isnumeric():
# #     continue
# if result.text == "2":
#     print("Test Pass, 1+1 = 2")
# else:
#     print("Test failed")
#
# # 4 / 2 = 2
# number1.clear()
# number2.clear()
# number1.send_keys("4")
# sleep(0.5)
# operator_select.select_by_visible_text("/")
# sleep(0.5)
# number2.send_keys("2")
# sleep(0.5)
# go_button.click()
# while result.text[0] == '.':
#     continue
# if result.text == "2":
#     print("Test Pass, 4/2 = 2")
# else:
#     print("Test failed")
#
# # 4 / 2 = 2
# number1.clear()
# number2.clear()
# number1.send_keys("3")
# sleep(0.5)
# operator_select.select_by_visible_text("/")
# sleep(0.5)
# number2.send_keys("2")
# sleep(0.5)
# go_button.click()
#
# while result.text[0] == '.':
#     continue
# if result.text == "1.5":
#     print("Test Pass, 3/2 = 1.5")
# else:
#     print("Test failed")
