from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginAndLogout:

    def test(self):

        # Define base URL and location to Gecko driver
        baseurl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Open base url
        driver.get(baseurl)

        # Maximize screen (or resize)
        # driver.maximize_window()
        driver.set_window_size(1024, 500)

        # Wait for page to load
        driver.implicitly_wait(5)

        # Go to login page
        clk_login = driver.find_element(By.LINK_TEXT, "Login")
        clk_login.click()

        # Find user, password and login elements
        clk_login = driver.find_element(By.CSS_SELECTOR, "input[name='commit']")
        inp_user = driver.find_element(By.ID, "user_email")
        inp_password = driver.find_element(By.ID, "user_password")

        # Type user, password and login
        inp_user.send_keys("hgpaula85@gmail.com")
        inp_password.send_keys("Palmeiras2019")
        clk_login.click()

        # Close
        driver.close()


ff = LoginAndLogout()
ff.test()
