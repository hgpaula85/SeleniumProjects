from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Find parent handle (Main window)
        parent_handle = driver.current_window_handle
        print("Parent handle: " + parent_handle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles (there should be two)
        all_handles = driver.window_handles

        # Switch to window and search course
        for handle in all_handles:
            print("Handle: " + handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)

                # Search for course
                search_box = driver.find_element(By.ID, "search-courses")
                search_box.send_keys("python")
                time.sleep(3)
                driver.close()
                break

        # Switch back to parent handle
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID, "name").send_keys("Test successful")
        time.sleep(3)
        driver.close()


my_test = SwitchToWindow()
my_test.test()
