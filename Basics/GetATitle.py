from selenium import webdriver

class GetATitle:
    def getTitle(self):
        driver = webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/p/practice")
        title = driver.title
        print(f"The title of webpage opened is '{title}'")
        print(type(driver.title))
        driver.close()

x = GetATitle()
x.getTitle()