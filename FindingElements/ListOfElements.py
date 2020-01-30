# Finding lists of elements

from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def find(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementsListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")

        if elementsListByClassName is not None:
            lenght1 = len(elementsListByClassName)
            print("We found a list of elements by Class Name with size equal to " + str(lenght1))

        elementsListByTagName = driver.find_elements(By.TAG_NAME, "a")

        if elementsListByTagName is not None:
            lenght2 = len(elementsListByTagName)
            print("We found a list of elements By Tag Name with size equal to " + str(lenght2))

ff = ListOfElements()
ff.find()