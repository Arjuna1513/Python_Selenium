from selenium import webdriver
import time
class Implicitly_Wait_Ex1:
    def implicitly_wait(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        print(driver.find_element_by_id('openwindow').is_enabled())
        print(driver.find_element_by_id('openwindow').is_displayed())
        driver.close()

x = Implicitly_Wait_Ex1()
x.implicitly_wait()