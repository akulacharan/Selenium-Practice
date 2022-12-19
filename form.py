from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

# Without select option..!


import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeGtPdxWWJlRfAgbn1RMlscljTox_zI9Uo03FoUDoBvdQNv3w/viewform")

driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("Bhargavi")

time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("9490549935")
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys('bhargavi.akulak9@gmail.com')

time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys("10/03/1998")

time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='i36']").click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='i39']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys("12")

time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys("24")
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div").click()

time.sleep(1)

#For description
driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys("I build new projects to tickle my brain and love teaching others how they're made. While I keep busy teaching courses, I also like to learn new technologies. Fullstack developer with primary focus on Django + (HTML,CSS,JS):")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div").click()

time.sleep(6)

driver.quit()