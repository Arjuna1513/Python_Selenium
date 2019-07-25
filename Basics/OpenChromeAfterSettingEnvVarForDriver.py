from selenium import webdriver

class OpenChromeAfterSettingEnvVarForDriver:
    def openChromeBrowser(self):
        driver = webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.close()

win = OpenChromeAfterSettingEnvVarForDriver()
win.openChromeBrowser()