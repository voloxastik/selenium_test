class BasePage(object):
	def __init__(self,driver):
		self.driver=driver
		#self.driver.get(page)

	def page_title(self):
		return self.driver.title

	def page_source(self):
		return self.driver.page_source

	def all_page_elements(self):
		elements=self.driver.find_elements_by_css_selector('*')
		return elements

