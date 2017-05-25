# This script automatically logs you into Reddit. Just change the chromedriver path and the username/password
# 1st: install selenium. Selenium fills out forms and clicks buttons for you
# 2nd: install chromedriver to interface with the chrome browser

import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/YOUR_PATH_HERE/Applications/chromedriver')  # <--- change/insert chromedriver path
driver.get('http://www.reddit.com/post/login')

username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("passwd_login")
button = driver.find_element_by_class_name('c-btn')
button = driver.find_element_by_css_selector("button[tabindex='3']")

time.sleep(0.5)

username.send_keys("YOUR_USERNAME")# <------change to reddit username
password.send_keys("YOUR_PASSWORD")# <------change to reddit password
button.submit()
