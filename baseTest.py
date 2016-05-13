from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chromedriver_path = "./supply/drivers/chromedriver"
        cls.options = Options()
        cls.options.binary_location = "/Users/sergey/Desktop/electron/next/next/node_modules/electron-prebuilt/dist/Electron.app/Contents/MacOS/Electron"
        cls.options.add_argument("app=/Users/sergey/Desktop/electron/next/next/main.js")
        cls.options.add_argument('no-sandbox')     #todo: do we need it ?
        cls.driver = webdriver.Chrome(executable_path=cls.chromedriver_path, chrome_options=cls.options)
        cls.driver.implicitly_wait(5)     #todo: do we need it ?

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


