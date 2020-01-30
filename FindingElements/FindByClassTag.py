# Finding an element by Class and Tag name

from selenium import webdriver


class FindByClassTag():

    def find(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")
        driver.set_window_size(600, 500)
        driver.get(baseUrl)

        elementByClass = driver.find_element_by_class_name("displayed-class")

        if elementByClass is not None:
            print("We found an element by class name")

        elementByTag = driver.find_element_by_tag_name("h1")

        if elementByTag is not None:
            elementText = elementByTag.text
            print("We found an element by Tag name: " + elementText)

ff = FindByClassTag()
ff.find()