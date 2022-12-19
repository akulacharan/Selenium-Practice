from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

import time


driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileDownload.html")


#To download text file
driver.find_element(By.ID,"textbox").send_keys("Hi this is Akula Charanteja from Kalyandurg.")
driver.execute_script("window.scroll(0,600)")     #To scroll
driver.find_element(By.ID,"createTxt").click()    #To create file
driver.find_element(By.XPATH,"//*[@id='link-to-download']").click()    #To download a file


#To download pdf file

driver.find_element(By.ID,"pdfbox").send_keys("hi Iam creating a pdf now please check in downloads folder after creating")
driver.find_element(By.ID,"createPdf").click() #To create pdf

time.sleep(4)
driver.find_element(By.ID,"pdf-link-to-download").click()

time.sleep(4000)