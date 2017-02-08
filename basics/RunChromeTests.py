from selenium import webdriver
import os

class RunChromeTestsWindows():
    # http://sites.google.com/a/chromium.org.chromedriver.downloads
    # http://chromedriver.storage.googleapis.com/index.html
    def test(self):
        driverLocation = "C:\\Users\HPAULA\\OneDrive\\Util\\SeleniumProjects\\lib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://letskodeit.com")

chromeTest = RunChromeTestsWindows()
chromeTest.test()