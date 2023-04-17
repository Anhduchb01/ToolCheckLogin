import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
	browser, service = None, None

	# Initialise the webdriver with the path to chromedriver.exe
	def __init__(self, driver: str):
		self.service = Service(driver)
		self.options = webdriver.ChromeOptions()
		self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

		self.browser = webdriver.Chrome(service=self.service,options= self.options)

	def open_page(self, url: str):
		self.browser.get(url)

	def close_browser(self):
		self.browser.close()

	def add_input(self, by: By, value: str, text: str):
		field = self.browser.find_element(by=by, value=value)
		field.send_keys(text)
		time.sleep(1)

	def click_button(self, by: By, value: str):
		button = self.browser.find_element(by=by, value=value)
		button.click()
		time.sleep(1)

	def login_linkedin(self, username: str, password: str):
		self.add_input(by=By.ID, value='PasswordEmail', text=username)
		self.add_input(by=By.ID, value='txtPassword', text=password)
		self.click_button(by=By.ID, value='PasswordLoginSubmit')
	def page_loading(self):
		print("Checking if {} page is loaded.".format(self.browser.current_url))
		page_state = self.browser.execute_script('return document.readyState;')
		if  page_state == 'complete':
			print('Complete')
			return False
		else :
			print('Not Complete')
			return True

	def check_page_qc(self):
		try:
			self.browser.find_element(by=By.CLASS_NAME, value='evg-main-panel')
			print('QC')
			self.click_button(by=By.CLASS_NAME, value='evg-btn-dismissal')
		except:
			print('Not QC')





if __name__ == '__main__':
	browser = Browser('drivers/chromedriver')

	browser.open_page('https://www.shophq.com/Account/Login?cm_re=GH_SignIn&returnUrl=https%3A%2F%2Fwww.shophq.com%2F')
	time.sleep(3)
	browser.check_page_qc()


	browser.login_linkedin(username='anhducythb003@gmail.com', password='anhducythb01')
	time.sleep(5)

	page_loading= True
	while page_loading:
		print(page_loading)
		check_loaded = browser.page_loading()
		if check_loaded ==False:
			page_loading = False
			curentUrl = browser.browser.current_url; 
			if curentUrl =='https://www.shophq.com/?SignInSuccess=true':
				print(curentUrl)
				print('Login OK')
			else:
				print('Login Failt')
			time.sleep(5)
			browser.close_browser()
		time.sleep(5)
