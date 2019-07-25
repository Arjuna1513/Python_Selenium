from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def test_openWindowInNewTab():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    driver.implicitly_wait(5)
    action = ActionChains(driver)
    time.sleep(2)
    # action.move_to_element(driver.find_element_by_xpath
    #                        ("//a[contains(text(),'Gmail')]")).perform()
    driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").send_keys(Keys.CONTROL+'T')
    # action.context_click(element).send_keys('t').perform()
    time.sleep(3)
    # driver.close()