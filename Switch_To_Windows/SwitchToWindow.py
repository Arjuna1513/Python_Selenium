from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

class SwitchToWindow:
    def switchWindow(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        print(driver.title)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, 'openwindow')))
        print(driver.find_element_by_id('openwindow').is_enabled())
        print(driver.find_element_by_id('openwindow').is_displayed())
        driver.find_element_by_id('openwindow').click()

        #  Now let's find out the total number of windows opened.
        parentWindow = driver.current_window_handle
        ttlWindows = driver.window_handles
        print(type(ttlWindows))
        print(parentWindow)
        for window in ttlWindows:
            if window != parentWindow:
                print(window)
                driver.switch_to.window(window)
                driver.maximize_window()
                print(driver.title)
                # driver.close() # U can either close here or just use break and when u r out of for loop use driver.close
                break
                # time.sleep(1)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(parentWindow)
        driver.find_element_by_id('name').send_keys('Switched window')
        time.sleep(3)
        driver.close()
        # driver.switch_to.window(parentWindow)

x = SwitchToWindow()
x.switchWindow()