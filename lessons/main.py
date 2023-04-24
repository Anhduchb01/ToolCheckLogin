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
					print(f'{email}|{password}')
					with open('account.txt', 'w') as f:
						f.write(f'{email}|{password}')
					check_register = False
def action_make_order(browser):
	browser.browser.get(urls[0])
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.color-box-container:first-of-type')
	browser.chooseTypeProduct(by=By.CSS_SELECTOR, value='li.size-box-container:first-of-type')
	time.sleep(2)
	browser.click_button(by=By.ID,value="btn-quick-buy-pdp")
	time.sleep(2)
	browser.turn_off_modal(by=By.CLASS_NAME,value='pdp-promo-modal')
def action_login(browser,mail,password):
	browser.open_page('https://www.shophq.com/Account/Login')
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
	add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-shipping-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn")

def action_add_bill_address(browser,email,password,address,city,state,zip_code,phone):
	browser.click_button(By.CSS_SELECTOR,'#billing-addresses-section > div:nth-child(3) > div > button')
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
	add_address_button = browser.click_button(By.CSS_SELECTOR,"#save-billing-address-section > div:nth-child(11) > div > div > button.btn.btn-outline-primary.save-address-btn")


def action_add_creadit(browser,number:str,month:str,year:str):
	try:
		radio_button = browser.find_element_input(By.CSS_SELECTOR,'#cphBody_optCreditCards')
	except:
		print('expand')
		page_loading= True
		while page_loading:
			page_loading = browser.page_loading()
			if page_loading==False :
				time.sleep(2)
				edit_credit = browser.click_button(By.CSS_SELECTOR,'#MainContent > div.checkout-page-body > div > div.col-sm-12.col-md-8 > div:nth-child(4) > div > div:nth-child(6) > div.col-sm-4.col-xs-4.checkout-section-header-button > a')
				print('expand ok')
				radio_button = browser.find_element_input(By.CSS_SELECTOR,'#cphBody_optCreditCards')
		
		
	
	# check if the radio button is selected
	if  radio_button.isSelected():
		print('have exits credit')
		browser.click_button(By.CSS_SELECTOR,'#cphBody_optNewCard')
		time.sleep(2)
		browser.add_input(By.ID,'cc_number',number)
		browser.add_input(By.ID,'expiration-month',month)
		browser.add_input(By.ID,'expiration-year',year)
		browser.add_input(By.ID,'cc_cvv','000')
		time.sleep(3)
		browser.click_button(By.ID,'btnSaveCreditCard')
		time.sleep(3)
	else:
		print(' not have exits credit')
		browser.click_button(By.CSS_SELECTOR,'#cphBody_optCreditCards')
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
	with open('result.txt', 'a') as f:
		f.write('\n'+ line)
if __name__ == '__main__':
	urls = []

	# Read each line of the file and append to the urls array
	with open('url_product.txt', 'r') as f:
		for line in f:
			url = line.strip()
			urls.append(url)
	print(urls)
	# Load the first URL using the webdriver object
	with open('account.txt', 'r') as f:
		for line in f:
			email, password = line.strip().split('|')
			email = email.replace(' ','')
			password= password.replace(' ','')
	print(email,password)
	form_ship_address = []
	with open('ship_address.txt', 'r') as f:
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
	with open('credit.txt', 'r') as f:
		for line in f:
			number, month, year = line.strip().split('|')
			list_creadit.append([number, month, year])

	browser = Browser('drivers/chromedriver')
	# Register Account
	# action_register(browser)

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
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			action_make_order(browser)
		time.sleep(3)
	page_loading= True
	while page_loading:
		page_loading = browser.page_loading()
		if page_loading==False :
			curentUrl = browser.browser.current_url
			if 'shophq.com/Checkout/QuickBuy' in curentUrl:
				try:
					action_add_ship_address(browser,email,password,first_name,last_name,address,city,state,zip_code)		
					time.sleep(3)
				except:
					print('Da co thong tin ship address')
				try:
					action_add_bill_address(browser,email,password,address,city,state,zip_code,phone)	
					time.sleep(3)
				except:
					print('Da co thong tin bill address')
			
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
	
