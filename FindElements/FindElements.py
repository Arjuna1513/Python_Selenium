from selenium import webdriver
import time
class FindElements:
    def findelements(self):
        driver = webdriver.Firefox()
        driver.get("http://10.211.162.111/mp")
        driver.find_element_by_name('userId').send_keys('Arjuna')
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys('Arjuna@12345')
        driver.find_element_by_name('login').click()
        driver.find_element_by_id('Services').click()
        driver.find_element_by_id('Extension').click()
        driver.find_element_by_name('rangeFields[1]').send_keys('*')
        driver.find_element_by_name('onViewRangeButton').click()
        list1 = driver.find_elements_by_xpath("//input[@name='selectItem']")
        list2 = []
        size = len(list1)
        for i in range(1,size+1):
            list2.append(driver.find_element_by_xpath("((//input[@name='selectItem']//parent::td)["+str(i)+"]//following-sibling::td)[25]"))
        print(len(list2))
        for extension in list2:
            print(extension.text)
        time.sleep(5)
        driver.close()

x = FindElements()
x.findelements()

"""
In the above I tried to get the list of extensions but could not do it in 1 step so what I dis is 
I first took the count of total rows and then I iterated over each row and using indexing i got the value
of each extension
"""