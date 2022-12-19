import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
        driver.get("https://www.google.co.in/")
        titleOfWebpage = driver.title

        print(titleOfWebpage)

        #self.assertTrue(titleOfWebpage == "Google")  # returns true if both title are same
        self.assertFalse(titleOfWebpage == "Google123")  # returns true if both title are not same


if __name__ == "__main__":
    unittest.main()