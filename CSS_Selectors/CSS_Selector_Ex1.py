from selenium import webdriver
import time

class CSS_Selector_Ex1:
    def cssEx1(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice#top")
        # find using css selector
        # driver.find_element_by_css_selector("input[id='name']").send_keys('Hello')

        #  find element using css selector using # for id
        # driver.find_element_by_css_selector("input#name").send_keys('Hello')

        # find element using css selector for class
        # driver.find_element_by_css_selector("input[class='inputs']").send_keys('Bajrang')
        # find element using css selector for class using '.
        # driver.find_element_by_css_selector('input.inputs').send_keys('Malli')

        # now when we have 2 elements with class values for 1st is 'inputs displayed-class' and class
        # class value for second element is 'inputs' and now if i use input.inputs it will select
        # both first and second and if u want to select 1st one use input.inputs.displayed-class
        driver.find_element_by_css_selector('input.inputs.displayed-class').send_keys('Mitel')
        time.sleep(5)
        driver.close()

x = CSS_Selector_Ex1()
x.cssEx1()