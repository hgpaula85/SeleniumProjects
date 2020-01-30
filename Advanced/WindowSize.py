from selenium import webdriver


class WindowSize:

    def test(self):

        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        # Open base url
        driver.get(base_url)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width : " + str(width))
        driver.close()


my_test = WindowSize()
my_test.test()
