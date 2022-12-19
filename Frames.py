
#We will learn how to switch through the frames

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Switching to first frame (you have to select name of the frame) here .....!
driver._switch_to.frame("packageListFrame")


time.sleep(2)

driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

# Here the first frame is selected, inorder to move to second frame --> first we need to come back to the original (first) frame

driver.switch_to.default_content()

# Again switching to second frame (you have to select name of the frame) here

time.sleep(2)
driver._switch_to.frame("packageFrame")

driver.find_element(By.LINK_TEXT,"WebDriver").click()

# Here the second frame is selected, inorder to move to third frame --> first we need to come back to the original (first) frame
driver.switch_to.default_content()


# Again switching to third frame (you have to select name of the frame) here
time.sleep(2)
driver._switch_to.frame("classFrame")

driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()


time.sleep(4)

driver.quit()
