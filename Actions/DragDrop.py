from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragAndDrop:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Switch to the frame
        driver.switch_to.frame(0)

        # Find both elements, drag and drop
        drag_me = driver.find_element(By.ID, 'draggable')
        drop_me = driver.find_element(By.ID, 'droppable')

        # Drag and drop the element
        try:
            actions = ActionChains(driver)
            # This is one way to do it
            # actions.drag_and_drop(drag_me, drop_me).perform()
            # This is another way to do it
            actions.click_and_hold(drag_me).move_to_element(drop_me).release().perform()
            print("Drag and drop OK")

        except:
            print("Drag and drop failed")


my_test = DragAndDrop()
my_test.test()
