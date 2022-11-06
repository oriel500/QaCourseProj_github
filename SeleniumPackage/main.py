from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_chrome = Service(r"C:\seleniumQA7\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)