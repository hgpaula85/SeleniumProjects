
from selenium import webdriver
from selenium.webdriver.common.by import By


class WorkingWithList:

    def test_list(self):
        # Define base URL and location to Gecko driver
        wait_time = 100
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Open base url
        driver.get(base_url)

        # Maximize screen (or resize)
        driver.set_window_size(1024, 600)

        # Wait for page to load
        driver.implicitly_wait(wait_time)

        # Get elements list
        radio_button_list = driver.find_elements(By.CSS_SELECTOR, "[type=radio][name=cars]")
        list_size = len(radio_button_list)
        print("Size of my list is " + str(list_size))

        # Loop trough list and click button that is not selected
        for radio_button in radio_button_list:
            is_selected = radio_button.is_selected()

            if not is_selected:
                radio_button.click()
                driver.implicitly_wait(time_to_wait=wait_time)


ff = WorkingWithList()
ff.test_list()
