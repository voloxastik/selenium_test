from selenium.webdriver.common.by import By as by
#from basePage import BasePage
from page_objects.PO_start_page import StartPage

import time

class PlayerPage(StartPage):
    def get_player(self,magnet_link):
        self.page_refresh()
        self.input_field().send_keys(magnet_link)
        self.enter_magnet_button().click()
        time.sleep(10)  # todo   implement wait