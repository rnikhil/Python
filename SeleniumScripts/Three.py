import time  # It is used to add some delay
from selenium import webdriver # It imports webdriver from webdriver

driver = webdriver.Firefox()  # creates webdriver object to call web driver
                              # It is used to start Firefox Browser

driver.set_page_load_timeout(30)  # If the page we are going to load doesnot load in 30s it will timeout
driver.get("https://www.facebook.com")  # it will open the desired url, here it will open facebook
assert "Facebook - Log In or Sign Up" in driver.title
driver.maximize_window()  # It is used to maximize the browser window
driver.implicitly_wait(20)
elem = driver.find_element_by_id("email")
elem.send_keys("mnikhil.25@gmail.com")
elem = driver.find_element_by_id("pass")
elem.send_keys("nikhil25")
elem.clear()
driver.find_element_by_id("u_0_o").click()
driver.get_screenshot_as_file("C:\\Python34\\screenshots\\facebook1.png")
time.sleep(5)
driver.quit()