from selenium import webdriver
from selenium.webdriver.support.select import Select

class GettingAllValuesFromDropDown:
    def getAllValues(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        select = Select(driver.find_element_by_id('carselect'))
        list1 = select.options
        [print(item.text) for item in list1]
        # for item in list1:
        #     print(item.text)
        driver.close()

x = GettingAllValuesFromDropDown()
x.getAllValues()

"""
In the above code select.options returns the list with all the option webelements and to 
print all those have a forloop and for each item in the list extract text value by using text variable
NOTE : Unlike in java in python text, and options are not methods they are just variables.

U can even use comprehension to print values '[print(item.text) for item in list1]'
remember that when u type item.    in python it wont show text u have to typoe it manually
"""