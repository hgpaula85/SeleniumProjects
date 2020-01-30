# Find elements using By method

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindBy():

    def find(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")
        driver.set_window_size(600, 500)
        driver.get(baseUrl)

        elementByIdName = driver.find_element(By.ID, "name")

        if elementByIdName is not None:
            print("We found an element by Id Name")


        elementByXPath = driver.find_element(By.XPATH, "//button[@id='mousehover']")

        if elementByXPath is not None:
            print("We found an element by XPath")

        elementByClass = driver.find_element(By.CLASS_NAME, "dropbtn")

        if elementByClass is not None:
            print("we found an element by Class Name")

        elementByTag = driver.find_element(By.TAG_NAME, "h1")

        if elementByTag is not None:
            print("We found an element by Tag Name")
        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")


ff = FindBy()
ff.find()