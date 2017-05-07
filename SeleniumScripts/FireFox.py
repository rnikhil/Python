from selenium import webdriver

class FireTests():
    def test(self):
        driver = webdriver.Firefox()  # Instantiates the Firefox Browser
        driver.get("https://www.google.com")  # Opens the provided URL

ff = FireTests()
ff.test()
