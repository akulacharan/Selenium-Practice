from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

#driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle) #CDwindow-A29ACF77A86CD82CAAA94F3ECF3F8153 returns current window handle

handles = driver.window_handles  #returns all the window handlers opemed in our browser

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

    if driver.title == "Frames & windows":
        driver.close()  #Closes only parent window (or window with that perticular title)

time.sleep(5)

driver.quit()