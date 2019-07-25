from selenium import webdriver
from selenium.webdriver.support.select import Select # do not forget to import the modules Select
import time
class SelectValueFromDropDown:
    def selectDropDownValue(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        select = Select(driver.find_element_by_id('carselect'))
        # select.select_by_visible_text('Honda') # selects the given value from drop-down
        # select.select_by_index(3) # selects element based on index value given, if value is not
        # present at given index NoSuchElementException will be thrown
        select.select_by_value('honda') # selects value based on option value
        time.sleep(5)
        driver.close()

x = SelectValueFromDropDown()
x.selectDropDownValue()