from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class TakeScreenShot:
    def screenShots(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.save_screenshot('C:\\Users\\mallikar\\Documents\\Python_Workspace\\'+
                               'Pthon_Selenium\\ScreenShotsLocation\\FirstScreen.png')
        print(self)
x = TakeScreenShot()
x.screenShots()


"""
The method save_screenshot('fileNameWithPath') will take the screen shot and save the file in the given path.
"""