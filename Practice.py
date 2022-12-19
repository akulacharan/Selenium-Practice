from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")
"""
action = ActionChains(driver)

driver.execute_script("window.scroll(0.600")
source = driver.find_element(By.XPATH,"//*[@id='gallery']/li[1]")
destination = driver.find_element(By.XPATH,"//*[@id='trash']")

action.drag_and_drop(source,destination).perform()
time.sleep(4)
"""

#driver.find_element(By.XPATH,"//*[@id='slider']/span").click()
ele = driver.find_element(By.TAG_NAME,"table")
print(ele.text)
time.sleep(2)
driver.quit()