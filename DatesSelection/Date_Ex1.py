from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Date_Ex1:
    def date_select(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://www.expedia.com/')
        driver.find_element(By.ID, "package-departing-hp-package").click()
        element = driver.find_element(By.XPATH, "(//tbody[@class='datepicker-cal-dates'])[1]//button[contains(text(),'30')]")
        element.click()
        time.sleep(3)
        driver.close()

x = Date_Ex1()
x.date_select()
