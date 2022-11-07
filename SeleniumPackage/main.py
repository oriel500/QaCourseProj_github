from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
wait = WebDriverWait(driver,10)
