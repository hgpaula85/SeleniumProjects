# Finding an element by XPATH and CSS

from selenium import webdriver


class FindByXpathCSS():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")
        driver.set_window_size(600, 500)
        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath(".//*[@id='carselect']")
        elementByCSS   = driver.find_element_by_css_selector("#alertbtn")

        if elementByXpath is not None:
            print("We found an element by XPATH: ", elementByXpath)

        if elementByCSS is not None:
            print("We found an element by CSS Selector: ", elementByCSS)

ff = FindByXpathCSS()
ff.test()