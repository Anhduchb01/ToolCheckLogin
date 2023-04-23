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