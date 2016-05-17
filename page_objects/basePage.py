import os

class BasePage(object):
	def __init__(self,driver):
		self.driver=driver

	def page_title(self):
		return self.driver.title

	def page_source(self):
		return self.driver.page_source

	def all_page_elements(self):
		elements=self.driver.find_elements_by_css_selector('*')
		return elements

	def get_screenshot(self,file_name):
		command='screencapture ./report/screenshots/'+file_name
		os.system(command)
