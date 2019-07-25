from selenium import webdriver
import time
class VerticalScroll:
    def vertScroll(self):
        driver = webdriver.Firefox()
        driver.get('https://www.amazon.in/')
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,-1000);")
        time.sleep(3)

        #  Let's scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        # Let's get the total height of the web page
        height = driver.execute_script("return document.body.scrollHeight;")
        print(f"The Vertical height is = {str(height)}")
        time.sleep(3)
        driver.close()

x = VerticalScroll()
x.vertScroll()
