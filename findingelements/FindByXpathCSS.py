# Finding an element by XPATH and CSS

from selenium import webdriver


class FindByXpathCSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath(".//*[@id='carselect']")
        elementByCSS   = driver.find_element_by_css_selector("#alertbtn")

        if elementByXpath is not None:
            print("We found an element by XPATH: ", elementByXpath)

        if elementByCSS is not None:
            print("We found an element by CSS Selector: ", elementByCSS)

ff = FindByXpathCSS()
ff.test()