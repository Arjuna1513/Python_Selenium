from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class GetAllVisibleDates:
    def date_select(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://www.expedia.com/')
        driver.find_element(By.ID, "package-departing-hp-package").click()
        # Let's select date for a particular month
        element = driver.find_elements(By.XPATH, "//caption[contains(text(), 'Jul 2019')]//following-sibling::tbody/tr/td/button[@class='datepicker-cal-date']")
        for date in element:
            print(date.text)

        time.sleep(3)
        driver.close()

x = GetAllVisibleDates()
x.date_select()