from selenium import webdriver
import time
class Implicitly_Wait_Ex1:
    def implicitly_wait(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://letskodeit.teachable.com/p/practice#top')
        time.sleep(1)
        driver.close()

x = Implicitly_Wait_Ex1()
x.implicitly_wait()

"""Implicitly_wait method works similar to implicitly_wait method of java selenium.
every 500 milliseconds it keeps pooling for the element and as soon as 
the element is found with in the given time, the next lines will be executed and if the element is not
found with in the given period of time then TimeOutException will be thrown.
"""