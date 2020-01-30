from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        # Maximize screen (or resize)
        driver.maximize_window()

        # Open base url
        driver.get(base_url)

        # Wait for page to load
        driver.implicitly_wait(3)

        # Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.implicitly_wait(3)
        driver.find_element(By.ID, "user_email").send_keys("test@testmail.com")
        driver.find_element(By.NAME, "commit").click()
        self.take_screenshot(driver)
        driver.close()

    def take_screenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver:
        :return True or False:
        """
        file_name = str(round(time.time() * 100)) + ".png"
        default_directory = 'C:/Users/Public/Pictures/'
        destination_file = default_directory + file_name

        try:
            driver.save_screenshot(destination_file)
            print("Screenshot saved to: " + destination_file)
            return True

        except NotADirectoryError:
            print("Not a directory")
            return False


my_test = Screenshots()
my_test.test()
