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
        driver.get('https://jqueryui.com/slider/')
        # element = driver.find_element(By.XPATH,"//iframe[@src='https://marcojakob.github.io/dart-dnd/basic/']")
        # location = element.location_once_scrolled_into_view
        actions = ActionChains(driver)
        driver.switch_to.frame(0)
        src = driver.find_element_by_xpath("//div[@id='slider']/span")
        # actions.drag_and_drop_by_offset(src, 100, 0).perform()
        actions.click_and_hold(src).move_to_element_with_offset(driver.find_element_by_xpath("//div[@id='slider']/span"), 100, 0).perform()
        time.sleep(3)
        driver.close()


x = DragAndDrop_Ex1()
x.dragAndDrop()