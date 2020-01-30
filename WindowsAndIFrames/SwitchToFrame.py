from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Scroll element into view
        frame = driver.find_element(By.ID, "courses-iframe")
        frame.location_once_scrolled_into_view
        driver.execute_script("window.scrollBy(0, -150)")

        # Switch to frame using Id
        # driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        driver.switch_to.frame(0)

        # Search course
        search_box = driver.find_element(By.ID, "search-courses")
        search_box.send_keys("python")
        driver.find_element(By.ID, "search-course-button").click()
        time.sleep(2)

        # Switch back to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1500)")
        driver.find_element(By.ID, "name").send_keys("Test successful")
        time.sleep(2)


my_test = SwitchToFrame()
my_test.test()
