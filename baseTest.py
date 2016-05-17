from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import os,platform


class BaseTest(unittest.TestCase):
    os_name=platform.system()

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        if cls.os_name=='Windows':
            cls.chromedriver_path = "./supply/drivers/chromedriver.exe"
            cls.options.binary_location = '../node_modules/electron-prebuilt/dist/electron.exe'

        elif cls.os_name=='Darvin':
            cls.chromedriver_path = "./supply/drivers/chromedriver"
            cls.options.binary_location = '../node_modules/electron-prebuilt/dist/Electron.app/Contents/MacOS/Electron'

        else:
            print('Unknown OS') #todo  -  implement logging

        cls.options.add_argument("app=../main.js")
        cls.options.add_argument('no-sandbox')     #todo: do we need it ?
        cls.driver = webdriver.Chrome(executable_path=cls.chromedriver_path, chrome_options=cls.options)
        cls.driver.implicitly_wait(5)     #todo: do we need it ?

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


