#Finding an element by link text and partial link text

from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Sign")

        if elementByLinkText is not None:
            print("We found element by link text", elementByLinkText)

        if elementByPartialLinkText is not None:
            print("We found element by partial link text", elementByPartialLinkText)

ff = FindByLinkText()
ff.test()