from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class Alert_Ex2:
    def switchToAlert(self):
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        driver.find_element_by_id("name").send_keys("Arjuna")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(3)
        alert = driver.switch_to.alert
        print(f"Alert text is = {alert.text}")
        # alert.accept()
        alert.dismiss()
        # driver.close()

x = Alert_Ex2()
x.switchToAlert()