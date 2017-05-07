
from selenium import webdriver

class FindbyIdName():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elemId = driver.find_element_by_id("name")
        if elemId is not None:
            print("we found element by Id")
        elemName = driver.find_element_by_name("show-hide")
        if elemName is not None:
            print("we found element by Name")
ff = FindbyIdName()
ff.test()



