from selenium import webdriver

class OpenFFBrowser:
    def openFbPage(self):
        driver = webdriver.Firefox(executable_path='C:\\Users\\mallikar\\Documents\\selenium\\Driver\\geckodriver.exe')
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.close()

browser = OpenFFBrowser()
browser.openFbPage()

"""
Do not forget to mention executable_path in firefox(constructor)
get the location of the geckodriver by rightclick-->properties and do not forget to mention
\\ instead of / in driver path for windows and also u need to mention .exe compulsorily in driver
path.
"""

print(type(webdriver.Firefox))