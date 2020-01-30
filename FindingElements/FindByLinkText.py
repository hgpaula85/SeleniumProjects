#Finding an element by link text and partial link text

from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")
        driver.set_window_size(600, 500)
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Login")

        if elementByLinkText is not None:
            print("We found element by link text", elementByLinkText)

        if elementByPartialLinkText is not None:
            print("We found element by partial link text", elementByPartialLinkText)

ff = FindByLinkText()
ff.test()