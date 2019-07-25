from selenium import webdriver

class OpenFireFoxAfterSettingEnvVarForDriver:
    def openChromeBrowser(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.close()

win = OpenFireFoxAfterSettingEnvVarForDriver()
win.openChromeBrowser()