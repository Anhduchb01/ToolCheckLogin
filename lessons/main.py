import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from generate import Generate
from browser import Browser

import os

# Get the current folder
current_folder = os.getcwd()
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
	# check_register = True
	# while check_register:
		# loop when page finish
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Account/RegisterConfirmation' not in curentUrl:
				if browser.check_Visible(by=By.ID, value='validate-email-proceed') == True :
					time.sleep(3)
					print('invalid email')
					email = generate.random_email(last)
					print(first,last, email,password)
					browser.register_again(email=email)
					print('Register OK')
					print(f'{email}|{password}')
					with open(current_folder+'/account.txt', 'w') as f:
						f.write(f'{email}|{password}')
			else:
				print('Register OK')
				print(f'{email}|{password}')
				with open(current_folder+'/account.txt', 'w') as f:
					f.write(f'{email}|{password}')
					# check_register = False
	register = True
	while register:
		if 'shophq.com/Account/RegisterConfirmation' not in browser.browser.current_url:
			time.sleep(2)
		else:
			register =False
			print('ok continue')

def action_make_order(browser,urls):
	browser.browser.get(urls[0])
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.color-box-container:first-of-type')
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.size-box-container:first-of-type')
	time.sleep(2)
	browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
	browser.click_button(by=By.ID,value="btn-quick-buy-pdp")
	browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
	time.sleep(2)
	browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
def action_login(browser,mail,password):
	
	time.sleep(2)
	browser.login(mail,password)
	time.sleep(2)
def action_add_ship_address(browser,email,password,first_name,last_name,address,city,state,zip_code):
	browser.add_ship_address()
	time.sleep(2)
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Account/Login' in curentUrl:
				browser.remove_input(By.ID,'PasswordEmail')
				action_login(browser,email,password)
	
	browser.add_input_js(by=By.ID,value='ShippingAddresses_SelectedAddress_FirstName',text=first_name)
	browser.add_input_js(by=By.ID,value='ShippingAddresses_SelectedAddress_LastName',text=last_name)
	browser.add_input_js(by=By.ID,value='ShippingAddresses_SelectedAddress_Address1',text=address)
	browser.add_input_js(by=By.ID,value='ShippingAddresses_SelectedAddress_City',text=city)
	browser.select_option('ShippingAddresses_SelectedAddress_State',state)
	browser.add_input_js(by=By.ID,value='ShippingAddresses_SelectedAddress_Zip',text=zip_code)
	
	check_address_button = browser.excute_js1('return $("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").length >0 ;')
	if check_address_button :
		add_address_button = browser.excute_js1('$("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").click();')
	check_address_button_overide = browser.excute_js1('return $("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn").length > 0 ;')
	if check_address_button_overide :
	
		add_address_button = browser.excute_js1('$("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn").click();')


def action_add_bill_address(browser,email,password,address,city,state,zip_code,phone):
	browser.add_bill_address()
	time.sleep(2)
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Account/Login' in curentUrl:
				browser.remove_input(By.ID,'PasswordEmail')
				action_login(browser,email,password)
	
	browser.add_input_js(by=By.ID,value='BillingAddresses_SelectedAddress_Address1',text=address)
	browser.add_input_js(by=By.ID,value='BillingAddresses_SelectedAddress_City',text=city)
	browser.select_option('BillingAddresses_SelectedAddress_State',state)
	browser.add_input_js(by=By.ID,value='BillingAddresses_SelectedAddress_Zip',text=zip_code)
	browser.add_input_js(by=By.ID,value='PhoneNumber',text=phone)
	
	check_address_button = browser.excute_js1('return $("#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").length >0 ;')
	if check_address_button :
		add_address_button = browser.excute_js1('$("#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").click();')
	check_address_button_overide = browser.excute_js1('return $("#save-billing-address-section > div:nth-child(10) > div > div > button.btn.btn-outline-primary.save-address-btn").length >0 ;')
	if check_address_button_overide :
		add_address_button = browser.excute_js1('$("#save-billing-address-section > div:nth-child(10) > div > div > button.btn.btn-outline-primary.save-address-btn").click();')
	# try:
	# 	add_address_button = browser.excute_js1('$("#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn").click();')
	# except:
	# 	print('ok bill address')
		


def action_add_creadit(browser,number:str,month:str,year:str):

	print('start click')
	while True:
		if browser.page_loading() :
			time.sleep(4)
		else:
			break
	print('load ok')
	check_error = browser.excute_js1('return $("#checkout-error").length > 0;')
	if check_error:
		loop = True
		while loop:
			while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
			print('load ok')
			click_edit = browser.excute_js1('$("#payment-collapse-button-title").click()')
			time.sleep(10)
			reFresh = True
			i=0
			while i<10:
				i+=1
				time.sleep(30)
				exists = browser.excute_js1('return $("#cphBody_optCreditCards").length > 0;')
				print(exists)
				if exists:
					print('da click')
					browser.excute_js1('$("#cphBody_optCreditCards").click();')
					reFresh = False
					loop = False
					break
			if reFresh:
				print('refresh')
				browser.browser.refresh()

		print('ok')
		time.sleep(2)
		browser.add_input_js(By.ID,'cc_number',number)
		browser.add_input_js(By.ID,'expiration-month',month)
		browser.add_input_js(By.ID,'expiration-year',year)
		browser.add_input_js(By.ID,'cc_cvv','000')
		browser.excute_js1('$("#btnSaveCreditCard").click();')
		
	else:
		loop = True
		while loop:
			while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
			print('load ok')
			time.sleep(10)
			element = browser.browser.find_element(By.ID,'ifmCCForm')
			print(element)
			html = element.get_attribute("innerHTML")
			print(html)
			browser.browser.switch_to.frame(browser.browser.find_element(By.ID,'ifmCCForm'))
			
			print('ok')
			html = browser.browser.execute_script("return document.documentElement.outerHTML;")
			print(html)
			reFresh = True
			i=0
			while i<10:
				i+=1
				time.sleep(40)
				exists = browser.excute_js1('return $("#cphBody_optCreditCards").length > 0;')
				print(exists)
				if exists:
					print('da click')
					browser.excute_js1('$("#cphBody_optCreditCards").click();')
					reFresh = False
					loop = False
					break
			if reFresh:
				print('refresh')
				browser.browser.refresh()

		print('ok')
		time.sleep(2)
		browser.add_input_js(By.ID,'cc_number',number)
		browser.add_input_js(By.ID,'expiration-month',month)
		browser.add_input_js(By.ID,'expiration-year',year)
		browser.add_input_js(By.ID,'cc_cvv','000')
		browser.excute_js1('$("#btnSaveCreditCard").click();')
		
def action_place_my_order(browser):
	time.sleep(3)
	try:
		browser.excute_js1('$("#PlaceOrderFormTop > button").click();')
	except:
		browser.excute_js1('$("#PlaceOrderForm > button > button").click();')
	time.sleep(3)
def save_result(line):
	with open(current_folder+'/result.txt', 'a') as f:
		f.write('\n'+ line)
def run():
	urls = []

	# Read each line of the file and append to the urls array
	with open(current_folder+'/url_product.txt', 'r') as f:
		for line in f:
			url = line.strip()
			urls.append(url)
	print(urls)
	# Load the first URL using the webdriver object
	with open(current_folder+'/account.txt', 'r') as f:
		for line in f:
			email, password = line.strip().split('|')
			email = email.replace(' ','')
			password= password.replace(' ','')
	print(email,password)
	form_ship_address = []
	with open(current_folder+'/ship_address.txt', 'r') as f:
		for line in f:
			# Split the line into separate fields
			raw = line.strip()
			form_ship_address.append(raw)
			# Extract the individual fields
	print(form_ship_address)
	first_name = form_ship_address[0]
	last_name = form_ship_address[1]
	address = form_ship_address[2]
	city = form_ship_address[3]
	state = form_ship_address[4]
	zip_code = form_ship_address[5]
	phone = form_ship_address[6]
	check_box_exist_info = form_ship_address[7]
	list_creadit = []
	
	with open(current_folder+'/credit.txt', 'r') as f:
		for line in f:
			number, month, year = line.strip().split('|')
			list_creadit.append([number, month, year])

	browser = Browser('drivers/chromedriver')
	# Register Account
	# action_register(browser)
	browser.open_page('https://www.shophq.com/Account/Login')
	action_login(browser,email,password)
	time.sleep(2)
	page_loading =True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'www.shophq.com/?SignInSuccess=true' not in curentUrl:
				action_register(browser)
	time.sleep(2)
	
	# go to product and Buy
	print(browser.browser.current_url)

	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			action_make_order(browser,urls)
		time.sleep(3)

	quick_buy_check = True
	while quick_buy_check:
		if 'shophq.com/Checkout/QuickBuy' not in browser.browser.current_url:
			browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
			time.sleep(2)
		else:
			browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
			quick_buy_check =False
			print('ok continue')
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()

		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Checkout/QuickBuy' in curentUrl:
				# try:
				print(check_box_exist_info)
				if check_box_exist_info == "0" or check_box_exist_info ==0:
					browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
					action_add_ship_address(browser,email,password,first_name,last_name,address,city,state,zip_code)		
					time.sleep(3)
					# except :
						
					# 	print('Da co thong tin ship address')
					# try:
					browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
					action_add_bill_address(browser,email,password,address,city,state,zip_code,phone)	
					time.sleep(3)
				# except:
				# 	print('Da co thong tin bill address')
			elif 'https://www.shophq.com/Account/Login' in curentUrl:
				try:
					action_login(browser,email,password)
				except:
					print('Not')
			else:
				time.sleep(6)
				print('Not make order')
		time.sleep(3)
	for i in range(len(list_creadit)):
		# try:
		number = list_creadit[i][0]
		month = list_creadit[i][1]
		year = list_creadit[i][2]
		time.sleep(3)
		action_add_creadit(browser,number,month,year)
			
		try:
			action_place_my_order(browser)
		except:
			print('Not make order')

		time.sleep(3)
		try:
			browser.browser.find_element(By.ID,'checkout-error')
			print('Khong thanh toan duoc')
			line= f'{number}|{month}|{year}|fail'
			save_result(line)
		except NoSuchElementException :
			print('thanh toan duwoc')
			line= f'{number}|{month}|{year}|pass'
			save_result(line)
	browser.close_browser()
	
