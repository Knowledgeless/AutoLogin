#############################################
# Facebook login automation script.			#
# Author: https://github.com/Knowledgeless/	#
#############################################

#importing modules
from selenium import webdriver
from getpass import getpass

try:

	#link & user informaiton
	url = "https://www.facebook.com/"
	username = input("Phone / E-mail: ")
	password = getpass("Password: ")

	#opening browser
	path = input("Enter your ChromeDriver path: ")
	driver = webdriver.Chrome(path)
	driver.get(url)

	#placeholding user informaitons
	user = driver.find_element_by_id("email").send_keys(username)
	pwd = driver.find_element_by_id("pass").send_keys(password)
	submit = driver.find_element_by_id("loginbutton").submit()

#error handling
except KeyboardInterrupt:
	print("\nYou Killed The Process Manually")

except AttributeError:
	print("\nGive It A Little Bit Time To Run Chrome & Take Action.\n")

except ImportError:
	print("\nRead 'README.md' Text Carefully.\n")

except:
	print('''
			\tCheck Your Connection

			 Read "README.md" Text Carefully.
			 If You Get Any Alien Type Error To Run This Script 
			 Let Me Know.
			 Github: https://github.com/Knowledgeless
		''')