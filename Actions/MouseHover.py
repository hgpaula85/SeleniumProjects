from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class MouseHover:

    def test(self):
        # Define base URL and location to Gecko driver
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(
            executable_path='C:/Python/Drivers/Gecko/geckodriver-v0.26.0-win32/geckodriver.exe')

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Scroll down to element into view
        mouse_hover_element = driver.find_element(By.ID, 'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true)", mouse_hover_element)
        driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(2)

        try:
            # Hover the mouse and click on element
            actions = ActionChains(driver)
            actions.move_to_element(mouse_hover_element).perform()
            print('Mouse hovered')
            time.sleep(3)

            # Find element on mouse hover menu
            item_to_click = driver.find_element(By.CSS_SELECTOR, "div[class=mouse-hover-content] a[href='#top']")
            actions.move_to_element(item_to_click).click().perform()
            print('Item clicked')
            time.sleep(3)

        except:
            print('Element not found')

        driver.close()


my_test = MouseHover()
my_test.test()
