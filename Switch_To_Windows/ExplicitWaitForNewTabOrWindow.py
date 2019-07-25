from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ExplicitWaitForNewTabOrWindow:
    def switchNewTab(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        parentWindow = driver.current_window_handle
        driver.find_element_by_id("opentab").click()
        wait.until(ec.number_of_windows_to_be(2))
        handles = driver.window_handles
        print(handles)
        # time.sleep(3)
        for window in handles:
            if window != parentWindow:
                driver.switch_to.window(window)
                wait.until(ec.visibility_of_element_located((By.ID, "search-courses")))
                driver.find_element(By.ID, "search-courses").send_keys("Python", Keys.ENTER)
                time.sleep(3)
                break
        driver.close()
        driver.switch_to.window(parentWindow)
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test_Successful")
        time.sleep(3)
        driver.close()



x = ExplicitWaitForNewTabOrWindow()
x.switchNewTab()

"""
Note :
Instead of using sleep after a link is clicked which opens new window or tab, it is
better to use ec.number_of_windows_to_be(any_number) in this way we can dynamically wait for 
the given time when we are not sure about how many seconds does it take to open the new 
window/tab.

"""