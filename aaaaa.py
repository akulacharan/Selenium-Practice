from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")

rows = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))

print("Rows: ",rows)

cols = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td"))

print("Cols :",cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        data = driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text, end="               ")
    print()

time.sleep(2)