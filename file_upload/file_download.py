from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display

def fileUploading():

    # firefoxProfile = webdriver.FirefoxProfile()
    # firefoxProfile.set_preference("browser.download.folderList", 2)
    # firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
    # firefoxProfile.set_preference("browser.download.dir", "C:\\Users\\mallikar\\Desktop\\downloads")
    # firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv/jar")

    # display = Display(visible=0, size=(1024, 768))
    # display.start()

    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)  # custom location
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', 'C:\\Users\\mallikar\\Desktop\\downloads')
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.closeWhenDone", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    # application/octet-stream,application/vnd.ms-excel
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                           'application/java-archive')

    driver = webdriver.Firefox(profile)
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    driver.get("https://docs.seleniumhq.org/download/")
    driver.find_element(By.LINK_TEXT, "Selenium Html Runner").click()


fileUploading()