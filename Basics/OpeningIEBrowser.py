from selenium import webdriver
import os
class OpeningIeBrowser:
    def openIEBrowser(self):
        driver_location = "C:\\Users\\mallikar\\Documents\\selenium\\Driver\\IEDriverServer.exe"
        key = "webdriver.ie.driver"
        os.environ[key] = driver_location
        driver = webdriver.Ie(driver_location)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.close()

cls = OpeningIeBrowser()
cls.openIEBrowser()