"""
Running tests on Firefox first
"""

from selenium import webdriver

class RunFFTests():

    def test(self):
        # Instantiate FF browser command
        driver = webdriver.Firefox()

        # Open the provided URL
        driver.get("https://www.letskodeit.com")

ff = RunFFTests()
ff.test()