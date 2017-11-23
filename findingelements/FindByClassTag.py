# Finding an element by Class and Tag name

from selenium import webdriver


class FindByClassTag():

    def find(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
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