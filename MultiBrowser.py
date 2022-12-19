from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://demo.automationtesting.in/Windows.html")

print(driver.title)      # Gives Title of the page
print(driver.current_url)   # returns url of the page
# print(driver.page_source)   # HTML code of the page

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()  #use single quotes in xpath

time.sleep(10)

#driver.close()  # Closes currently focused  browser

driver.quit() # Closes all the browsers