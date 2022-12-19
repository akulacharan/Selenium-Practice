from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")
# driver.save_screenshot("/Users/akulac/Downloads/cherry.png") #Saves in downloads folder with "cherry.png" name

driver.get_screenshot_as_file("/Users/akulac/Downloads/cherry2.png")

time.sleep(4)