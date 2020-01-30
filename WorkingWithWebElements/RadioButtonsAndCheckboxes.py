from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioButtonAndCheckboxes():

    def test(self):

        # Define base URL and location to Gecko driver
        wait_time = 50
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Open base url
        driver.get(base_url)

        # Maximize screen (or resize)
        driver.set_window_size(1024, 600)

        # Wait for page to load
        driver.implicitly_wait(wait_time)

        # Find radio buttons and checkboxes
        rbtn_BMW = driver.find_element(By.CSS_SELECTOR, "#bmwradio")
        rbtn_Benz = driver.find_element(By.CSS_SELECTOR, "#benzradio")
        rbtn_Honda = driver.find_element(By.CSS_SELECTOR, "#hondaradio")

        chk_BMW = driver.find_element(By.CSS_SELECTOR, "#bmwcheck")
        chk_Benz = driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        chk_Honda = driver.find_element(By.CSS_SELECTOR, "#hondacheck")

        # Click on radio buttons
        rbtn_BMW.click()
        driver.implicitly_wait(wait_time)

        rbtn_Benz.click()
        driver.implicitly_wait(wait_time)

        rbtn_Honda.click()
        driver.implicitly_wait(time_to_wait=wait_time)

        # Select checkboxes
        chk_BMW.click()
        chk_Benz.click()
        chk_Honda.click()

        # Unselect checkboxes
        chk_BMW.click()
        chk_Honda.click()

        # Verify which checkboxes are selected
        print("BWM checkbox is selected? " + str(chk_BMW.is_selected()))
        print("Benz checkbox is selected? " + str(chk_Benz.is_selected()))
        print("Honda checkbox is selected? " + str(chk_Honda.is_selected()))


ff = RadioButtonAndCheckboxes()
ff.test()
