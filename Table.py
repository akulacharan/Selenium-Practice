from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/#")


rows = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))
print("No of Rows: ",rows)



cols = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))
print("No of Cols: ",cols)

print("BookName"+"            "+"Author"+"        "+"Subject"+"        "+"Price")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(value.text,end="           ")  #BookName   Author   Subject   Price
    print()
time.sleep(4)