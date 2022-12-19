from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

#driver.get("https://www.google.co.in/")

#driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('Akula charanteja HCL')
#driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
#time.sleep(5)
#driver.find_element(By.XPATH,"//*[@id='hdtb-msb']/div[1]/div/div[2]/a").click()

""" Forward and backward commands
driver.get("https://www.youtube.com/watch?v=QqHz-Lj57ow")
time.sleep(2)
driver.back()

driver.forward()

time.sleep(5)
"""

""" Finding element by ID
driver.get("http://vambha.herokuapp.com/")

driver.find_element(By.ID,"Input").send_keys("Hi iam typing here....!")
time.sleep(5)
"""
""" Find element by XPATH 
driver.get("https://www.w3schools.com/html/html_form_input_types.asp")
driver.find_element(By.XPATH,"//*[@id='javascript']").click()

time.sleep(2)
"""
""" To find all the links a page
driver.get("https://www.youtube.com/results?search_query=vamsi+bhavani+c+language")
links = driver.find_elements(By.TAG_NAME,"a")

for i in links:
    print(i.text)

time.sleep(4)
"""
""" Switching to alert box 
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
driver._switch_to.alert.accept()

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
driver._switch_to.alert.dismiss()

time.sleep(4)
"""
""" For double clicking a button and also drag and drop option in a website 

driver.get("https://testautomationpractice.blogspot.com/")

action = ActionChains(driver)
ele = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
driver.maximize_window()

#action.double_click(ele).perform()
#action.context_click(ele).perform()

#source = driver.find_element(By.ID,"draggable")
#destination = driver.find_element(By.ID,"droppable")

action.drag_and_drop(source,destination).perform()
time.sleep(2)
"""
""" To upload a file

driver.get("http://vambha.herokuapp.com/")
driver.execute_script("window.scroll(0,600)")
driver.find_element(By.XPATH,"//*[@id='File']").send_keys(r'/Users/akulac/PycharmProjects/Selenium project/upload.Vambha')
driver.find_element(By.XPATH,"//*[@id='Button']").click()
time.sleep(2)
"""

""" To get cookies of our websites 
driver.get("https://www.google.co.in/")
cookies = driver.get_cookies()
for i in cookies:
    print(i)
time.sleep(4)
"""

""" To select from a dropdown (Select) menu 
driver.get("https://testautomationpractice.blogspot.com/")

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID,"speed"))
time.sleep(4)
select.select_by_visible_text('Fast')
time.sleep(4)

"""

driver.quit()