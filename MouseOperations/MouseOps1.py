from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class MouseOps1:
    def mouseOps(self):
        driver = webdriver.Firefox()
        driver.get('https://www.amazon.in/')
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'Category')]")).perform()
        time.sleep(2)
        actions.move_to_element(driver.find_element_by_xpath("//span[@data-nav-panelkey='MensFashionPanel']/span")).perform()
        actions.move_to_element(driver.find_element_by_xpath("//span[text()='T-shirts & Polos']")).click().perform()
        time.sleep(10)
        driver.close()

x = MouseOps1()
x.mouseOps()

# The above code opens up amazon.in webpage and then mouse hover's on category and then
# navigates to Men's Fashion link and then clicks Tshirts & Polos link.



