from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click to open the popup
        driver.find_element(By.ID, "name").send_keys("Steven Universe")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        driver.find_element(By.ID, "name").send_keys("Jake")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)

        alert2 = driver.switch_to.alert
        alert2.dismiss()


my_test = SwitchToAlert()
my_test.test()
