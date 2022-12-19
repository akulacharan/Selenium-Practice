import unittest

from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path="/Users/akulac/PycharmProjects/Selenium project/venv/bin/chromedriver")
        driver.get("https://www.google.co.in/")
        titleOfWebpage = driver.title
        print(titleOfWebpage)
        #assertEqul
        #self.assertEqual("Google",titleOfWebpage,"Web pages title are not same")  # returns true if both title are same
        self.assertNotEqual("Google",titleOfWebpage,"Web pages title are same")    # Returns true if both title are not same




if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
