from selenium import webdriver
import os

class OpenChromeBrowser:
    def openchrome(self):
        driver_location = "C:\\Users\\mallikar\\Documents\\selenium\\Driver\\chromedriver.exe"
        key = "webdriver.chrome.driver"
        os.environ[key] = driver_location # similar to system.setProperty in java
        driver = webdriver.Chrome(driver_location)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()

chromewindow = OpenChromeBrowser()
chromewindow.openchrome()
print(type(webdriver.Firefox))
