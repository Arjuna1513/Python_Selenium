from selenium import webdriver
import time
class WebDriver_Methods_properties:
    def sel_Methods_porperties(self):
        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice#top')

        # Let's maximize the window size
        # driver.maximize_window()
        # driver.find_element_by_link_text('Coupons').click()
        # time.sleep(3)
        #
        # # Let's get back to the previous web page
        # driver.back()
        # time.sleep(3)
        #
        # # Let's get back to the forward window
        # driver.forward()
        # time.sleep(3)
        #
        # # Let's get the title of the current window opened.
        # print(driver.title)
        # time.sleep(3)
        #
        # # Let's get the url of the current page opened
        # print(driver.current_url)
        # time.sleep(3)

        # driver.find_element_by_id('opentab').send_keys()

        driver.close()

x = WebDriver_Methods_properties()
x.sel_Methods_porperties()