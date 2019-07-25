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
        driver.switch_to.frame(0)
        dest = driver.find_element_by_xpath("//div[@class='container']/div")
        for i in range(0,4):
            actions.click_and_hold(driver.find_element_by_xpath
                               ("(//img[@class='document'])[1]")).move_to_element(dest).release().perform()
            time.sleep(3)
        # srcList = driver.find_elements_by_xpath("//img[@class='document']")

        driver.close()


x = DragAndDrop_Ex1()
x.dragAndDrop()