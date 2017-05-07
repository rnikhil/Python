from selenium import webdriver
import os  # In order to work with OS(operating System) commands
class InternetTests():
    def test(self):
        driverLocation = "C:\\Python34\\Scripts\\IEDriverServer.exe"
        os.environ['webdriver.ie.driver'] = driverLocation
        driver = webdriver.Ie(driverLocation)  # Instantiates the Firefox Browser
        driver.get("https://www.google.com")  # Opens the provided URL

ex = InternetTests()
ex.test()

"""
from selenium import webdriver
import os

class RunSafariTests():
    # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver
    # http://selenium-release.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "C:\\Python34\\Scripts\\selenium-server-standalone-3.0.1.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)
        # Open the provided URL
        driver.get("http://www.google.com")

safari = RunSafariTests()
safari.test()
"""