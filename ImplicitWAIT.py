from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
driver.get("https://demo.guru99.com/test/newtours/")

#This is completely based on the time ony, even if the element is not loaded in that perticular time --> It will throw an excepption
driver.implicitly_wait(10)  #seconds


assert "Welcome: Mercury Tours" in driver.title

#time.sleep(5)

driver.find_element(By.NAME,"userName").send_keys("mercury")
driver.find_element(By.NAME,"password").send_keys("mercury")

driver.find_element(By.NAME,"submit").click()
