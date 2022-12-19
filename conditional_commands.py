from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://demo.guru99.com/test/newtours/")

# finding the username input box in the website and checking if it is displayed & editable
user_ele = driver.find_element(By.NAME,"userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

# finding the password input box in the website and checking if it is displayed & editable

pass_ele = driver.find_element(By.NAME,"password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

# Entering the username,password and clicking on sign-in button

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")
driver.find_element(By.NAME,"submit").click()

# navigating to flight finder page
driver.get("https://demo.guru99.com/test/newtours/reservation.php")


#To check if Round trip radio button is clicked or not, by using css selector.

roundtrip_radio = driver.find_element(By.CSS_SELECTOR,"input[value=roundtrip]")
print("Status of Roundtrip Radio button :",roundtrip_radio.is_selected())

oneway_radio = driver.find_element(By.CSS_SELECTOR,"input[value=oneway]")
print("Status of Oneway Radio button :",oneway_radio.is_selected())


driver.quit()



