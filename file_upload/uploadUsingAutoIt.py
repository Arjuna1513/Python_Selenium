from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def fileUploading():

    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    wait = WebDriverWait(driver, 10)
    driver.get("https://demo.actitime.com/login.do");
    driver.find_element(By.ID,"username").send_keys("admin")
    driver.find_element(By.NAME, "pwd").send_keys("manager")
    driver.find_element(By.XPATH, "//div[.='Login ']").click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[@class='popup_menu_icon'])[3]")))
    driver.find_element(By.XPATH, "(//div[@class='popup_menu_icon'])[3]").click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Contact actiTIME Support')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Contact actiTIME Support')]").click()
    wait.until(ec.element_to_be_clickable((By.XPATH,"//div[@class='dz-default dz-message']")))
    driver.find_element(By.XPATH,"//div[@class='dz-default dz-message']").click()
    os.system("C:\\Users\\mallikar\\Desktop\\screenUpload.exe")
    time.sleep(2000)



fileUploading()