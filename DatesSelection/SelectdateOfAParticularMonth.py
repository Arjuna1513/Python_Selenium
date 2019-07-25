from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
class SelectdateOfAParticularMonth:
    def date_select(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://www.expedia.com/')
        driver.find_element(By.ID, "package-departing-hp-package").click()
        # Let's select date for a particular month
        while True:
            monthsList = driver.find_elements(By.XPATH,"//caption[@class='datepicker-cal-month-header']")
            for month in monthsList:
                if month.text == 'Dec 2019':
                    element = driver.find_element(By.XPATH,
                                                  "//caption[contains(text(),'Dec 2019')]//following-sibling::tbody/tr/td/button[contains(text(),'30')]")
                    element.click()
                    break
            element = driver.find_elements(By.XPATH,"//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']")
            if len(element) == 0:
                break
            else:
                nextMonth = driver.find_element(By.XPATH,
                                                "//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']")
                nextMonth.click()
        driver.close()

x = SelectdateOfAParticularMonth()
x.date_select()
