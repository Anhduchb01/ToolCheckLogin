import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import random
import string
import re
class Browser:
	browser, service = None, None

	# Initialise the webdriver with the path to chromedriver.exe
	def __init__(self, driver: str):
		self.service = Service(driver)
		self.options = webdriver.ChromeOptions()
		self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
		# self.options.add_argument("--disable-extensions")
		# self.options.add_argument("--disable-gpu")
		# self.options.add_argument("--headless")
		self.browser = webdriver.Chrome(service=self.service,options= self.options)

	def open_page(self, url: str):
		self.browser.get(url)
		self.check_page_qc()

	def close_browser(self):
		self.browser.close()

	
	def add_input_container(self,byContainer: By, valueContainer: str, by: By, value: str, text: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((byContainer, valueContainer)))
		container = self.browser.find_element(by=byContainer, value=valueContainer)
		field = container.find_element(by=by, value=value)
		field.send_keys(text)
		time.sleep(1)
		
	def remove_input(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		field = self.browser.find_element(by=by, value=value)
		field.clear()
		time.sleep(1)
	def click_button(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 20)
		wait.until(EC.element_to_be_clickable((by, value)))
		button = self.browser.find_element(by=by, value=value)
		button.click()
		time.sleep(1)
	def add_input(self, by: By, value: str, text: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		field = self.browser.find_element(by=by, value=value)
		field.clear()
		field.send_keys(text)
		time.sleep(1)
	def login(self, username: str, password: str):
		print(username+'|'+password+'|')
		self.add_input(by=By.ID, value='PasswordEmail', text=username)
		self.add_input(by=By.ID, value='txtPassword', text=password)
		time.sleep(10)
		self.click_button(by=By.ID, value='PasswordLoginSubmit')
	def check_page_qc(self):
		try:
			print('QC')
			self.browser.find_element(by=By.CLASS_NAME, value='evg-main-panel')
			self.click_button(by=By.CLASS_NAME, value='evg-btn-dismissal')
		except:
			print('Not QC')
			pass
			
	def page_loading(self):
		print("Checking if {} page is loaded.".format(self.browser.current_url))
		page_state = self.browser.execute_script('return document.readyState;')
		if  page_state == 'complete':
			print('Complete')
			return False
		else :
			print('Not Complete')
			return True

	
	def register(self, first_name: str, last_name: str, email: str,password: str):
		page_loading= True
		while page_loading:
			page_loading = self.page_loading()
			if page_loading==False :
				self.check_page_qc()
				self.add_input(by=By.ID, value='RegisterFirstName', text=first_name)
				self.add_input(by=By.ID, value='RegisterLastName', text=last_name)
				self.add_input(by=By.ID, value='RegisterEmailId', text=email)
				self.add_input(by=By.ID, value='NewPassword', text=password)
				time.sleep(3)
				self.check_page_qc()
				self.click_button(by=By.ID, value='Save')
	def register_again(self, email: str):
		page_loading= True
		while page_loading:
			page_loading = self.page_loading()
			if page_loading==False :
				self.check_page_qc()
				self.remove_input(by=By.ID, value='RegisterEmailId')
				self.add_input(by=By.ID, value='RegisterEmailId', text=email)
				time.sleep(3)
				self.check_page_qc()
				print('start click submid-proceed')
				# self.click_button(by=By.ID, value='submit-proceed')
				self.excute_js('document.getElementById("submit-proceed").click()')
	def check_Visible(self, by: By, value: str):
		try:	
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.presence_of_element_located((by, value)))
			span_error_email = self.browser.find_element(by=by, value=value)
			if span_error_email.get_attribute('style') == 'display: none;':
				return False
			else:
				return True
		except NoSuchElementException:
			print("No span element with id='validate-email-proceed' found on the page")
	def chooseTypeProduct(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		color_box_container = self.browser.find_element(by,value)
		# Find the img element within the li element and click on it

		try:
			img = color_box_container.find_element(By.TAG_NAME, 'img')
			# If img is found, click on it
			img.click()
		except NoSuchElementException:
		# If img is not found, find the button and click on it
			button = color_box_container.find_element(By.TAG_NAME, 'button')
			button.click()
		time.sleep(3)
	def turn_off_modal(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		color_box_container = self.browser.find_element(by,value)
		# wait.until(EC.visibility_of((By.CLASS_NAME,'close')))
		try:
			wait = WebDriverWait(self.browser, 10)
			wait.until(EC.presence_of_element_located((By.ID, 'btnDecline')))
			exit_button = color_box_container.find_element(By.ID,'btnDecline')
			exit_button.click()
		except:
			print('Not show')
			pass
	def add_ship_address(self):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'shipping-addresses-section')))
		click_add = self.excute_js1('$("#shipping-addresses-section > div:nth-child(3) > div > button").click();')
		# try:
			
		# 	# add_button = ship_address_container.find_element(By.CLASS_NAME,'add-address-btn')
		# 	# add_button.click()	
		# except:
		# 	print('Not add ship address')
		# 	pass
	def add_bill_address(self):
		# self.click_button(By.CSS_SELECTOR,'#billing-addresses-section > div:nth-child(3) > div > button')
		click_add = self.excute_js1('$("#billing-addresses-section > div:nth-child(3) > div > button").click();')
	def select_option(self,id: str,value:str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, id)))
		dropdown = Select(self.browser.find_element(By.ID,id))
		# select the option with value 'AK'
		dropdown.select_by_value(value)
	def find_element_input(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 60)
		wait.until(EC.element_to_be_clickable((by, value)))
		element = self.browser.find_element(by, value)
		print(element)
		print('start click')
		element.click()
	def excute_js(self,cmd:str):
		print('run',cmd)
		self.browser.execute_script(cmd)
	def excute_js1(self,cmd:str):
		# 1) Get back to the main body page
		self.browser.switch_to.default_content()

		# 2) Download jquery lib file to your current folder manually & set path here
		with open('./_lib/jquery-3.3.1.min.js', 'r') as jquery_js: 
			# 3) Read the jquery from a file
			jquery = jquery_js.read() 
			# 4) Load jquery lib
			self.browser.execute_script(jquery)
			# 5) Execute your command 
			# self.browser.execute_script('$("#myId").click()')
			self.browser.execute_script(cmd)
		