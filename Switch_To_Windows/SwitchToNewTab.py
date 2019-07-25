from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""class SwitchToNewTab:
    def switchNewTab(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        parentWindow = driver.current_window_handle
        driver.find_element_by_id("openwindow").click()
        handles = driver.window_handles
        time.sleep(3)
        driver.switch_to.window(handles[-1])
        driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        time.sleep(3)
        driver.close()
        # for window in handles:
        #     if window is not parentWindow:
        #         driver.switch_to.window(window)
        #         driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        #         time.sleep(3)
        #         break
        driver.switch_to.window(handles[0])
        # driver.close()
        # driver.switch_to.window(parentWindow)
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test_Successful")

        # driver.close()



x = SwitchToNewTab()
x.switchNewTab()"""



"""class SwitchToNewTab:
    def switchNewTab(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        parentWindow = driver.current_window_handle
        driver.find_element_by_id("openwindow").click()
        # handles = driver.window_handles
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        time.sleep(3)
        driver.close()
        # for window in handles:
        #     if window is not parentWindow:
        #         driver.switch_to.window(window)
        #         driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        #         time.sleep(3)
        #         break
        driver.switch_to.window(driver.window_handles[0])
        # driver.close()
        # driver.switch_to.window(parentWindow)
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test_Successful")
        time.sleep(3)
        driver.close()

        # driver.close()



x = SwitchToNewTab()
x.switchNewTab()"""



# Navigating to new window using window_handles[-1]/window_handles[0]
"""class SwitchToNewTab:
    def switchNewTab(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        parentWindow = driver.current_window_handle
        driver.find_element_by_id("opentab").click()
        # handles = driver.window_handles
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        time.sleep(3)
        driver.close()
        # for window in handles:
        #     if window is not parentWindow:
        #         driver.switch_to.window(window)
        #         driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
        #         time.sleep(3)
        #         break
        driver.switch_to.window(driver.window_handles[0])
        # driver.close()
        # driver.switch_to.window(parentWindow)
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test_Successful")
        time.sleep(3)
        driver.close()

        # driver.close()



x = SwitchToNewTab()
x.switchNewTab()"""


# Navigating to new tab using switch_to method and for loop
class SwitchToNewTab:
    def switchNewTab(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')

        parentWindow = driver.current_window_handle

        driver.find_element_by_id("opentab").click()
        time.sleep(3) # remember to put some delay after clicking so that when a new tab/window is
        # opened it takes some time to add it to the window_handles list
        handles = driver.window_handles
        # time.sleep(10)
        for window in handles:
            if window != parentWindow:
                driver.switch_to.window(window)
                print(window.title())
                wait.until(ec.visibility_of_element_located((By.ID, "search-courses")))
                driver.find_element(By.ID,"search-courses").send_keys("Python", Keys.ENTER)
                time.sleep(3)
                break
        driver.close()
        time.sleep(3)
        driver.switch_to.window(parentWindow)
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test_Successful")
        time.sleep(3)
        driver.close()

        # driver.close()



x = SwitchToNewTab()
x.switchNewTab()



"""Switching to new window can be done this way as well.
There will be an window_handles list object and when ever a new new window is opened its 
ID will be appended to the end of the list so now if we want to switch_to new window just
get the window_handles and save it in some variable handles.

Now to switch to new window use handles[-1] and to switch back to main window use handles[0]

when working with tab it's better to use some delay after clicking the link that opens 
new tab so that we will not run in to trouble becoz sometimes it takes time to open new tab and add it to
window_handles list...
"""