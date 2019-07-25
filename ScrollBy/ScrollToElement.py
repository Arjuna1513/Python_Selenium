from selenium import webdriver
import time
class ScrollToElement:
    def scrollToElement(self):
        driver = webdriver.Firefox()
        driver.get('https://www.amazon.in/')
        time.sleep(3)
        element = driver.find_element_by_link_text('About Us')
        location =  element.location_once_scrolled_into_view
        element.click()
        time.sleep(3)


x = ScrollToElement()
x.scrollToElement()