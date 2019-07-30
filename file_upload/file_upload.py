from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def fileUploading():
    print(os.getcwd())
    current_dir = os.getcwd()
    current_dir = current_dir.replace("\\", "/")
    print(current_dir)
    path = os.getcwd().replace('\\','\\'+'\\')
    driver = webdriver.Firefox()
    driver.get("file:///" + current_dir + "/Upload.html")
    time.sleep(5)
    driver.find_element(By.ID, "fileToUpload").\
        send_keys(path + "\\Diversion__.png")

    # path = path.replace("\\", "\\\\")
    # print(path)


fileUploading()