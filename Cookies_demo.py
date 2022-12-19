from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")

driver.get("https://www.amazon.in/")

# Capture all cookies created by browser

cookies = driver.get_cookies()
print(len(cookies))  #prints cookie count
print(cookies) #Print all cookie pairs


# Adding new cookie to the browser
cookie = {'name':'Mycookie','value':'12345678'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))  #prints cookie count
print(cookies) #Print all cookie pairs


# Delete an existing cookie

driver.delete_cookie('Mycookie')
time.sleep(2)
cookies = driver.get_cookies()
print(len(cookies))  #prints cookie count
print(cookies) #Print all cookie pairs

# Delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))  #prints cookie count
print(cookies) #Print all cookie pairs