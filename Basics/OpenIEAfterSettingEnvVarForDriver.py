from selenium import webdriver

class OpenIEAfterSettingEnvVarForDriver:
    def openChromeBrowser(self):
        driver = webdriver.Ie() #//No path is specified since path is added to env variable
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.close()

win = OpenIEAfterSettingEnvVarForDriver()
win.openChromeBrowser()