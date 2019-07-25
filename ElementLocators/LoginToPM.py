from selenium import webdriver
from selenium.webdriver.firefox.webelement import FirefoxWebElement

import time
class LoginToPM:
    def login(self):
        url = 'http://10.211.162.213/'
        driver = webdriver.Firefox()
        driver.get(url)

        # identify name
        driver.find_element_by_name('userId').send_keys('Arjuna')
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys('Arjuna@12345')
        print(driver.find_element_by_name('login'))
        driver.find_element_by_name('login').click()
        time.sleep(5)
        driver.find_element_by_link_text('Logout').click()
        driver.close()

x = LoginToPM()
x.login()


