from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import time

class DragAndDrop_Ex1:
    def dragAndDrop(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://code.makery.ch/library/dart-drag-and-drop/')
        element = driver.find_element(By.XPATH,"//iframe[@src='https://marcojakob.github.io/dart-dnd/basic/']")
        location = element.location_once_scrolled_into_view
        actions = ActionChains(driver)
        for i in range(0,4):
            driver.switch_to.frame(0)
            dest = driver.find_element_by_xpath("//div[@class='container']/div")
            src1 = driver.find_element_by_xpath("(//div[@class='container']/img)[1]")
            actions.drag_and_drop(src1, dest).perform()
            time.sleep(4)
        # srcList = driver.find_elements_by_xpath("//img[@class='document']")

        driver.close()


x = DragAndDrop_Ex1()
x.dragAndDrop()