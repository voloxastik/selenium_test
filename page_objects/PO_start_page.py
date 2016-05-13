from selenium.webdriver.common.by import By as by
from page_objects.basePage import BasePage

class StartPage(BasePage):

    def input_field(self):
        return self.driver.find_element(by.ID, 'magnet-input')

    def enter_magnet_button(self):
        return self.driver.find_element(by.ID, 'enter-magnet')

    def page_refresh(self):
        self.driver.refresh()

    def error_message(self):
        return self.driver.find_element(by.CLASS_NAME,'overlay-title').text
