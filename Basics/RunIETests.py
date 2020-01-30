from selenium import webdriver
import os

class RunIETests():

    def test(self):
        driverlocation = "C:\\Users\HPAULA\\OneDrive\\Util\\SeleniumProjects\\lib\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverlocation
        driver = webdriver.Ie(driverlocation)
        driver.get("http://www.letskodeit.com")

IeTest = RunIETests()
IeTest.test()