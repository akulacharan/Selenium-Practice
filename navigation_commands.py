

# This code is for moving forward and backward in browser using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://demo.guru99.com/test/newtours/")

print(driver.title)

driver.get("https://www.pavantestingtools.com/")
time.sleep(4)
print(driver.title)


driver.get("https://www.google.com/")
time.sleep(4)
print(driver.title)

#Going Backward ........!
print('going backward')

driver.back()
time.sleep(2)
print(driver.title)

#Going Forward........!
print('going forward')

driver.forward()
time.sleep(2)
print(driver.title)

time.sleep(3)

driver.quit()



