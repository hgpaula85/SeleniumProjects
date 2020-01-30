from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class Slider:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Switch to the frame
        driver.switch_to.frame(0)

        # Find element to slide
        slide_me = driver.find_element(By.ID, 'slider')

        # Slide element
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slide_me, 100, 0).perform()
            time.sleep(3)
            print("Element slide OK")

        except:
            print("Element slide failed")

        driver.close()


my_test = Slider()
my_test.test()

