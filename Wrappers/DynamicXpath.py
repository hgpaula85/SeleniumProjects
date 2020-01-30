from selenium import webdriver
from Wrappers.HandyWrappers import MyHandyWrapper

class DynamicXpathFormat:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Maximize screen (or resize)
        driver.maximize_window()

        # Open base url
        driver.get(base_url)

        # Wait for page to load
        driver.implicitly_wait(3)

        # Login
        hw = MyHandyWrapper(driver)
        btn_login = hw.getElement("Login", "Link_Text")
        btn_login.click()

        # Enter email and password
        txt_email = hw.getElement("#user_email", "CSS")
        txt_password = hw.getElement("#user_password", "CSS")
        txt_email.send_keys("hgpaula85@gmail.com")
        txt_password.send_keys("Palmeiras2019")

        btn_login = hw.getElement(".btn.btn-primary.login-button", "CSS")
        btn_login.click()

        # Find 'JavaScript for beginners course using Dynamic Xpath
        # XPATH = //div[contains(@class, 'course-listing-title') and contains(text(), 'JavaScript for beginners')]
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _course_locator = _course.format("JavaScript for beginners")

        course_element = hw.getElement(_course_locator, "xpath")
        course_element.click()


my_test = DynamicXpathFormat()
my_test.test()
