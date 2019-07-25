from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class MultiSelectDropDown:
    def selectMultiOptions(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        select = Select(driver.find_element_by_id('multiple-select-example'))
        list1 = select.options
        for item in list1:
            item.click()
            time.sleep(2) #selects all the elements from the multi drop-down with 2 seconds gap in between.
        print(select.first_selected_option.text)
        list2 = select.all_selected_options # this gets the list of all selected options
        for item in list2:
            print(item.text) # text is a variable, not a method

        # Now deselect all the selected options from multi select drop down
        # for i in range(len(list1)-1, -1, -2):
        #     select.deselect_by_index(i)
        #     time.sleep(2)
        driver.close()
x = MultiSelectDropDown()
x.selectMultiOptions()

"""
Note : the syntax to define decremental for-loop is : for i in range(len(list1)-1, -1, -1):
since we want to start from last give the len(list1)-1 and second param is till zero we want so give 0 and then
decremental range so give -1 and if u give -2 here every second element from last will get selected.
"""