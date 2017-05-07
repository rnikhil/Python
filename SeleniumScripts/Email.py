# How to get email address from any web page
#  Extracting email using Regex (regular expression)

from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("http://www.airindia.in/customer-support.htm")

doc = driver.page_source  # we will create a doc variable to extract the page source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)  # And we will be going to read it and extract the email addresses

for email in emails:
     print(email)




# Extracting phone numbers using regex (regular expression)
"""
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("http://www.airindia.in/customer-support.htm")

doc = driver.page_source
phones = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for phone in phones:
     print(phone)

"""
