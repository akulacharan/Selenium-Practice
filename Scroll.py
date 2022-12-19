from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# 1. Scroll down by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# 2. Scroll down page till we find a perticular element in that page

#flag = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)


# 3. Scroll till end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(4)