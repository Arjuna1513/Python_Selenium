from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

def fileUploading():
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory":"C:\\Users\\mallikar\\Desktop\\downloads",
                                                         "safebrowsing.enabled":"false"}
    options.add_experimental_option("prefs",preferences)
    # options.add_argument("download.default_directory=C:\\Users\\mallikar\\Desktop\\downloads")

    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    # wait = WebDriverWait(driver, 10)
    driver.get("https://docs.seleniumhq.org/download/")
    driver.find_element(By.LINK_TEXT, "Selenium Html Runner").click()
    time.sleep(20)


fileUploading()