from selenium import webdriver
from Wrappers.HandyWrappers import MyHandyWrapper
import time

class ElementPresentCheck:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Maximize screen (or resize)
        driver.maximize_window()

        # Open base url
        driver.get(base_url)

        # Wait for page to load
        driver.implicitly_wait(10)

        # Create an object HandyWrapper
        hw = MyHandyWrapper(driver)

        # Check if element is present on webpage
        element_result1 = hw.isElementPresent("#name", "CSS")
        print(str(element_result1))

        driver.close()


ff = ElementPresentCheck()
ff.test()
