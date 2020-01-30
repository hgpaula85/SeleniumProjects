from selenium import webdriver
import time


class HiddenElement:

    def testHiddenElement(self):

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

        # Find the state of the text box
        text_box_element = driver.find_element_by_id("displayed-text")
        text_box_state = text_box_element.is_displayed()  # True if visible, False if hidden
        print("Text box is visible? " + str(text_box_state))

        # Click the hide button
        driver.find_element_by_id("hide-textbox").click()
        text_box_state = text_box_element.is_displayed()  # True if visible, False if hidden
        print("Text box is visible? " + str(text_box_state))

        # Click the show button
        driver.find_element_by_id("show-textbox").click()
        text_box_state = text_box_element.is_displayed()  # True if visible, False if hidden
        print("Text box is visible? " + str(text_box_state))

        # Close browser
        driver.close()


ff = HiddenElement()
ff.testHiddenElement()