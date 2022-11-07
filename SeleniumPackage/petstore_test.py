from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from random import choice
from selenium.common.exceptions import NoSuchElementException

# Setup
service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
wait = WebDriverWait(driver, 10)

# Enter to the site
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.maximize_window()
driver.implicitly_wait(5)

# Buy 3 pets random
for i in range(3):
    # Navigate to product page
    kinds_of_pets = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a")
    kind_of_pet = choice(kinds_of_pets)
    kind_of_pet.click()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    # Choose the random kind
    table_of_products = driver.find_element(By.TAG_NAME, "table")
    products = table_of_products.find_elements(By.TAG_NAME, "tr")
    product_rnd = choice(products[1:])
    cols = product_rnd.find_elements(By.TAG_NAME, "td")
    cols[0].click()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

    # Choose random pet in the page of kinds
    table_of_products = driver.find_element(By.TAG_NAME, "table")
    products = table_of_products.find_elements(By.TAG_NAME, "tr")
    product_rnd = choice(products[1:])
    isFoundButton = False
    while not isFoundButton:  # Try other choice if not found the add to cart button
        try:
            cols = product_rnd.find_elements(By.TAG_NAME, "td")
            add_to_cart_button = cols[-1].find_element(By.TAG_NAME, "a")
            add_to_cart_button.click()
            sleep(0.5)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))
            isFoundButton = True
        except NoSuchElementException:
            product_rnd = choice(products[1:])

    # Navigate to Main Page
    driver.find_element(By.LINK_TEXT, "Return to Main Menu").click()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "area[alt='Fish']")))

# Navigate to cart
driver.find_element(By.CSS_SELECTOR, "[name='img_cart']").click()
sleep(0.5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))

# Change Quantity to 2 in first item
table_of_products = driver.find_element(By.TAG_NAME, "table")
items = table_of_products.find_elements(By.TAG_NAME, "tr")
cols = items[1].find_elements(By.TAG_NAME, "td")

cols[4].find_element(By.TAG_NAME, "input").clear()
cols[4].find_element(By.TAG_NAME, "input").send_keys("2")
sleep(0.5)
driver.find_element(By.CSS_SELECTOR, "[value='Update Cart']").click()
sleep(0.5)

# Calculate the sum of price
table_of_products = driver.find_element(By.TAG_NAME, "table")
items = table_of_products.find_elements(By.TAG_NAME, "tr")
cols = items[1].find_elements(By.TAG_NAME, "td")

sum_price = 0
for item in items[1:-1]:
    cols = item.find_elements(By.TAG_NAME, "td")
    quantity = float(cols[4].find_element(By.TAG_NAME, "input").get_attribute("value"))
    price = float(cols[5].text[1:])
    total_cost = price * quantity
    sum_price += total_cost
sub_total = items[-1].find_element(By.TAG_NAME, "td").text.split()
sub_total_price = sub_total[2]

# Check if sub_total equal to sum_price
if float(sub_total_price[1:]) == sum_price:
    print("Test Pass")
else:
    print("Test Fail")
print(f"sum price: {sum_price}")
print(f"sub_total: {sub_total_price[1:]}")
