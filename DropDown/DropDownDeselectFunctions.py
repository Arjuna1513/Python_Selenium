from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropDownDeselectFunctions:
    def deselectFunctions(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        select = Select(driver.find_element_by_id('carselect'))
        select.select_by_visible_text('Benz')
        # select.deselect_by_visible_text('Benz')
        time.sleep(2)
        driver.close()

x = DropDownDeselectFunctions()
x.deselectFunctions()

"""
Note : If u try to use deslect functions for a single select drop down then an exception
'NotImplementedError : You may only deselect options of a multi-select'  will be thrown
"""