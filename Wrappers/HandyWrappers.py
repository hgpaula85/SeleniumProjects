from selenium.webdriver.common.by import By


class MyHandyWrapper:

    # Create a constructor to receive the driver object
    def __init__(self, driver):
        self.driver = driver

    # Method to select the locator type
    def getByType(self, locator_type):
        locator_type = locator_type.lower()

        # Check which locator was received and if its a valid locator type
        if locator_type == "id":
            return By.ID

        elif locator_type == "name":
            return By.NAME

        elif locator_type == "xpath":
            return By.XPATH

        elif locator_type == "css":
            return By.CSS_SELECTOR

        elif locator_type == "link_text":
            return By.LINK_TEXT

        else:
            print("Locator type " + locator_type + " not supported")
            return False

    # Method to find and return the element using the locator and locator type provided
    def getElement(self, locator, locator_type="id"):
        element = None

        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element [" + str(locator) + "] found by " + str(by_type))

        except:
            print("Element [" + str(locator) + "] not found")
        return element

    # Method to check if element is present on webpage
    def isElementPresent(self, locator, locator_type):
        try:
            element = self.getElement(locator, locator_type)

            if element is not None:
                print("Element [" + locator + "] present")
                return True

            else:
                print("Element " + locator + " not present")
                return False

        except:
            print("Element " + locator + " not found")
            return False
