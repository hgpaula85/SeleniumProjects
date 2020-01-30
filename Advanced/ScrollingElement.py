from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollingElement:

    def test(self):

        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        # Open base url
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Scroll down
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

        # Scroll up
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(2)

        # Scroll element into view
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(2)

        # Native way to scroll element into view
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(2)

        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))
        driver.execute_script("window.scrollBy(0, -150);")

        driver.close()


my_test = ScrollingElement()
my_test.test()
