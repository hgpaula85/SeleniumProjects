from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropDownSelect:

    def testSelect(self):

        # Define base URL and location to Gecko driver
        wait_time = 3
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Open base url
        driver.get(base_url)

        # Maximize screen (or resize)
        driver.maximize_window()

        # Wait for page to load
        time.sleep(wait_time)

        # Find dropdown element
        dropdown_element = driver.find_element(By.CSS_SELECTOR, "#carselect")
        select_obj = Select(dropdown_element)

        # Select dropdown elements by value, index and visible text
        select_obj.select_by_value("benz")
        time.sleep(wait_time)

        select_obj.select_by_index(0)
        time.sleep(wait_time)

        select_obj.select_by_visible_text("Honda")


ff = DropDownSelect()
ff.testSelect()
