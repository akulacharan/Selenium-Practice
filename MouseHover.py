from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")

time.sleep(1)

products = driver.find_element(By.XPATH,"//*[@id='product-menu-toggle']")
prdoucts_hover = driver.find_element(By.XPATH,"//*[@id='product-menu-dropdown']/div[1]/ul[1]/li[2]/a/div[2]/div[1]")

#To click on live option present in products menu we have to use ActionChains

actions = ActionChains(driver)
actions.move_to_element(products).move_to_element(prdoucts_hover).click().perform()
time.sleep(2)

# To inspect in browser
to_inpect = driver.find_element(By.XPATH,"//*[@id='live-form-url']")
actions.context_click(to_inpect).perform()

time.sleep(4)