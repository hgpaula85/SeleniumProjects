# Find elements using By method

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindBy():

    def find(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementByIdName = driver.find_element(By.ID, "name")

        if elementByIdName is not None:
            print("We found an element by Id Name")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByXPath = driver.find_element(By.XPATH, ".//*[@id='mousehover']")

        if elementByXPath is not None:
            print("We found an element by XPath")

        elementByClass = driver.find_element(By.CLASS_NAME, "displayed-class")

        if elementByClass is not None:
            print("we found an element by Class Name")

        elementByTag = driver.find_element(By.TAG_NAME, "h1")

        if elementByTag is not None:
            print("We found an element by Tag Name")

ff = FindBy()
ff.find()