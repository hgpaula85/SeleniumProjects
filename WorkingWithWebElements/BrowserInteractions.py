from selenium import webdriver

class BrowserInteractions:

    def test(self):
        baseurl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path="C:\\Python\\Drivers\\Gecko\\geckodriver-v0.26.0-win32\\geckodriver.exe")

        # Windows Maximize
        driver.maximize_window()

        # Open URL
        driver.get(baseurl)

        # Get title
        title = driver.title

        # Get URL
        currenturl = driver.current_url

        # Print title of the page
        print("Title of page is: " + title)

        # Print current url
        print("Current url is " + currenturl)

        # Browser refresh
        driver.refresh()
        print("Browser refreshed 1st time")

        driver.refresh()
        print("Browser refreshed 2nd time")

        # Open another URL
        driver.get("https://www.udemy.com/")

        # Browser back and forward
        driver.back()
        print("Go back in browser history")
        driver.forward()
        print("Go forward in browser history")

        # Get page source
        pagesource = driver.page_source

        # Browser close/quit
        # driver.close()
        driver.quit()
        print("Quit browser")


ff = BrowserInteractions()
ff.test()
