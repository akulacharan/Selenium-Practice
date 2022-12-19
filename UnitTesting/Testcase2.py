import unittest
import time

from selenium import webdriver

class searchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
        self.driver.get("https://www.google.co.in/")
        print("The title of the page is :" + self.driver.title)
        self.driver.close()
        time.sleep(2)

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
        self.driver.get("https://www.bing.com/")
        print("The title of the page is :" + self.driver.title)
        self.driver.close()




if __name__ == "__main__":
    unittest.main()