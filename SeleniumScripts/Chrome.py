from selenium import webdriver
import os  # In order to work with OS(operating System) commands
class ChromeTests():
    def test(self):
        driverLocation = "C:\\Python34\\Scripts\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver = webdriver.Chrome(driverLocation)  # Instantiates the Firefox Browser
        driver.get("https://www.google.com")  # Opens the provided URL

ch = ChromeTests()
ch.test()