from selenium import webdriver
from Wrappers.HandyWrappers import MyHandyWrapper
import time


class UsingWrappers:

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

        # Call getElement with locator and default ID locator type
        text_field1 = hw.getElement("name")
        text_field1.send_keys("This is a test")
        time.sleep(2)

        # Call getElement with locator and CSS locator type
        text_field2 = hw.getElement("#name", "CSS")
        text_field2.clear()


ff = UsingWrappers()
ff.test()
