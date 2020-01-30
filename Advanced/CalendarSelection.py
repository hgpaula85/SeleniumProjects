from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection:

    def test1(self):
        # Define base URL and location to Gecko driver
        base_url = "http://www.expedia.com"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Maximize screen (or resize)
        driver.maximize_window()

        # Open base url
        driver.get(base_url)

        # Wait for page to load
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()

        # Find departing date field
        departing_field = driver.find_element_by_id("flight-departing-hp-flight")

        # Click departing field
        departing_field.click()

        # Wait for page to load
        driver.implicitly_wait(3)

        # Find the date to be selected
        cal_month = driver.find_element(By.XPATH, "(//div[@class='datepicker-cal-month'])[1]")
        all_valid_dates = cal_month.find_elements(By.TAG_NAME, "button ")

        # Click the date
        for date in all_valid_dates:
            data_day = date.get_attribute("data-day")

            if data_day is not None:
                print(str(data_day), end=", ")

            if date.get_attribute("data-day") == "30":
                date.click()
                break

        time.sleep(3)
        driver.quit()


ff = CalendarSelection()
ff.test1()
