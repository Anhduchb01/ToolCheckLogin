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
	
	browser.add_input(by=By.ID,value='ShippingAddresses_SelectedAddress_FirstName',text=first_name)
	browser.add_input(by=By.ID,value='ShippingAddresses_SelectedAddress_LastName',text=last_name)
	browser.add_input(by=By.ID,value='ShippingAddresses_SelectedAddress_Address1',text=address)
	browser.add_input(by=By.ID,value='ShippingAddresses_SelectedAddress_City',text=city)
	browser.select_option('ShippingAddresses_SelectedAddress_State',state)
	browser.add_input(by=By.ID,value='ShippingAddresses_SelectedAddress_Zip',text=zip_code)
	
	# add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn")
	add_address_button = browser.excute_js1('$("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").click();')
	try:
		# add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn")
		add_address_button = browser.excute_js1('$("#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn").click();')
	except:
		print('Ok ship address')

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
	
	browser.add_input(by=By.ID,value='BillingAddresses_SelectedAddress_Address1',text=address)
	browser.add_input(by=By.ID,value='BillingAddresses_SelectedAddress_City',text=city)
	browser.select_option('BillingAddresses_SelectedAddress_State',state)
	browser.add_input(by=By.ID,value='BillingAddresses_SelectedAddress_Zip',text=zip_code)
	browser.add_input(by=By.ID,value='PhoneNumber',text=phone)
	
	# add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn")
	
	add_address_button = browser.excute_js1('$("#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn").click();')
	try:
		add_address_button = browser.excute_js1('$("#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn").click();')
		add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-override-address-btn")
	except:
		print('ok bill address')
		


def action_add_creadit(browser,number:str,month:str,year:str):

	print('start click')
	# radio_button = browser.find_element_input(By.ID,'cphBody_optCreditCards')

	# radio_button = browser.find_element_input(By.ID,'cphBody_optCreditCards')
	# radio_button =  browser.excute_js1('document.getElementById("cphBody_optCreditCards").click()')
	radio_button = browser.excute_js1('$("#cphBody_optCreditCards").click();')
	print('ok')

	try:
		print('start click')
		# radio_button = browser.find_element_input(By.ID,'cphBody_optCreditCards')
		radio_button = browser.excute_js1('$("#cphBody_optCreditCards").click();')
		# radio_button =  browser.excute_js('document.getElementById("cphBody_optCreditCards").click()')
		print('ok')
	except:
		print('expand')
		page_loading= True
		while page_loading:
			page_loading = browser.page_loading()
			if page_loading==False :
				time.sleep(2)
				edit_credit = browser.click_button(By.CSS_SELECTOR,'#MainContent > div.checkout-page-body > div > div.col-sm-12.col-md-8 > div:nth-child(4) > div > div:nth-child(6) > div.col-sm-4.col-xs-4.checkout-section-header-button > a')
				print('expand ok')
				# radio_button = browser.find_element_input(By.CSS_SELECTOR,'#cphBody_optCreditCards')
				radio_button = browser.excute_js1('$("#cphBody_optCreditCards").click();')
		
		
	
	# check if the radio button is selected
	if  radio_button.isSelected():
		print('have exits credit')

		time.sleep(2)
		browser.add_input(By.ID,'cc_number',number)
		browser.add_input(By.ID,'expiration-month',month)
		browser.add_input(By.ID,'expiration-year',year)
		browser.add_input(By.ID,'cc_cvv','000')
		time.sleep(3)
		browser.click_button(By.ID,'btnSaveCreditCard')
		time.sleep(3)
	else:
		
		time.sleep(2)
		browser.add_input(By.ID,'cc_number',number)
		browser.add_input(By.ID,'expiration-month',month)
		browser.add_input(By.ID,'expiration-year',year)
		browser.add_input(By.ID,'cc_cvv','000')
		time.sleep(3)
		browser.click_button(By.ID,'btnSaveCreditCard')
		time.sleep(3)
def action_place_my_order(browser):
	time.sleep(3)
	try:
		browser.click_button(By.CSS_SELECTOR,'#PlaceOrderFormTop > button')
	except:
		browser.click_button(By.CSS_SELECTOR,'#PlaceOrderForm > button')
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
		if 'shophq.com/Checkout/QuickBuy' in browser.browser.current_url:
			time.sleep(2)
		else:
			browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
			regquick_buy_checkister =False
			print('ok continue')
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Checkout/QuickBuy' in curentUrl:
				try:
					browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
					action_add_ship_address(browser,email,password,first_name,last_name,address,city,state,zip_code)		
					time.sleep(3)
				except:
					
					print('Da co thong tin ship address')
				try:
					browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
					action_add_bill_address(browser,email,password,address,city,state,zip_code,phone)	
					time.sleep(3)
				except:
					print('Da co thong tin bill address')
			elif 'https://www.shophq.com/Account/Login' in curentUrl:
				try:
					action_login(browser,email,password)
				except:
					print('Not')
			else:
				time.sleep(6)
				print('Not make order')
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
	
