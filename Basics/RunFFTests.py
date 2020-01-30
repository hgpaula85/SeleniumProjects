# Running tests on Firefox first

from selenium import webdriver


class RunFFTests:

    def test(self):
        # Initiate driver instance
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Open the provided URL
        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.test()
