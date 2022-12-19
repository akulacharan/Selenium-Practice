from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

#driver.maximize_window()

driver.get("https://www.expedia.co.in/")

driver.implicitly_wait(10)


c = driver.find_element(By.CSS_SELECTOR,"a.span.uitk-tab-text")

print(c)


driver.implicitly_wait(5)