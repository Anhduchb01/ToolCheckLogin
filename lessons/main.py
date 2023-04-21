import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
import string
import re
class Generate:
	def __init__(self) -> None:
		# list of popular first names in the US
		self.list_first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Oliver", "Charlotte", "Benjamin", "Amelia", "Elijah", "Mia", "Lucas", "Harper", "Mason", "Evelyn", "Logan"]
		# list of popular last names in the US
		self.list_last_names = ["Smith", "Johnson", "Brown", "Garcia", "Miller", "Jones", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Taylor", "Anderson", "Wilson", "Jackson", "Moore", "Martin", "Lee"]
	def random_first_name(self):
		# choose a random first name from the list of popular first names
			return random.choice(self.list_first_names)
	def random_last_name(self):
		# choose a random last name from the list of popular last names
		return random.choice(self.list_last_names)

	def random_email(self, last: str):
		number_random = ''.join(random.choices(string.digits, k=4))
		string_random = ''.join(random.choices(string.ascii_uppercase , k=2))
		email = f"{last.lower()}{string_random.lower()}{number_random}@gmail.com"
		return email
	def random_password(self):
		# generate a random password consisting of letters (both upper and lower case) and digits
		alphabet = string.ascii_letters + string.digits
		password = ''.join(random.choices(alphabet, k=12))
		return password
		
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
		self.check_page_qc()

	def close_browser(self):
		self.browser.close()

	def add_input(self, by: By, value: str, text: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		field = self.browser.find_element(by=by, value=value)
		field.send_keys(text)
		time.sleep(1)
	def remove_input(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		field = self.browser.find_element(by=by, value=value)
		field.clear()
		time.sleep(1)
	def click_button(self, by: By, value: str):
		wait = WebDriverWait(self.browser, 10)
		wait.until(EC.presence_of_element_located((by, value)))
		button = self.browser.find_element(by=by, value=value)
		button.click()
		time.sleep(1)

	def login(self, username: str, password: str):
		self.add_input(by=By.ID, value='PasswordEmail', text=username)
		self.add_input(by=By.ID, value='txtPassword', text=password)
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
				self.click_button(by=By.ID, value='submit-proceed')
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
		color_box_container = browser.browser.find_element(by,value)
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
		color_box_container = browser.browser.find_element(by,value)
		exit_button = color_box_container.find_element(By.CLASS_NAME,'close')
		exit_button.click()

def action_register(browser):
	generate = Generate()
	browser.open_page('https://www.shophq.com/Account/Register')
	time.sleep(3)
	
	first = generate.random_first_name()
	last = generate.random_last_name()
	email = generate.random_email(last)
	password = generate.random_password()
	print(first,last, email,password)
	browser.register(first_name=first, last_name=last,email=email,password=password)
	check_register = True
	while check_register:
		# loop when page finish
		page_loading= True
		while page_loading:
			page_loading = browser.page_loading()
			if page_loading==False :
				curentUrl = browser.browser.current_url
				if curentUrl=='https://www.shophq.com/Account/Register':
					if browser.check_Visible(by=By.ID, value='validate-email-proceed') == True :
						time.sleep(3)
						print('invalid email')
						email = generate.random_email(last)
						print(first,last, email,password)
						browser.register_again(email=email)
					else:
						check_register = False
				else:
					print('Register OK')
					check_register = False
def action_make_order(browser):
	browser.browser.get(urls[0])
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.color-box-container:first-of-type')
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.size-box-container:first-of-type')
	time.sleep(2)
	browser.click_button(by=By.ID,value="btn-quick-buy-pdp")
	browser.turn_off_modal(by=By.CLASS_NAME,value='modal-content')
if __name__ == '__main__':
	urls = []

	# Read each line of the file and append to the urls array
	with open('url_product.txt', 'r') as f:
		for line in f:
			url = line.strip()
			urls.append(url)
	print(urls)
	# Load the first URL using the webdriver object

	browser = Browser('drivers/chromedriver')
	# Register Account
	action_register(browser)
	time.sleep(2)
	# go to product and Buy
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			action_make_order(browser)
			time.sleep(5)
		time.sleep(3)
	page_loading= True
	# while page_loading:
	# 	page_loading = browser.page_loading()
	# 	if page_loading==False :

		
	# 	time.sleep(3)
			

	
	browser.close_browser()
	
