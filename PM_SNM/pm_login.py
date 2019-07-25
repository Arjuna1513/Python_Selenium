from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PMLogin:

    def validLogin(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://10.211.162.111/mp")
        driver.find_element(By.NAME, "userId").send_keys("Arjuna")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys("Arjuna@12345")
        driver.find_element(By.NAME, "login").click()
        # driver.find_element(By.XPATH, "//a/b[contains(text(), 'Logout')]")
        assert driver.find_element(By.XPATH, "//a/b[contains(text(), 'Logout')]").is_enabled(), "Login Failed"
        time.sleep(3)
        driver.close()

x = PMLogin()
x.validLogin()
