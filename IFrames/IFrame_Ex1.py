from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class IFrames_Ex1:
    def switchToIframe(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://learn.letskodeit.com/p/practice')

        # courses is present in the iframe so we have to switch to it and then click the courses.
        # driver.switch_to.frame(0) # we can switch to iframe based on index also

        # Lets scroll to the place where iframe is present
        element = driver.find_element(By.ID, "courses-iframe")
        location = element.location_once_scrolled_into_view

        # driver.switch_to.frame("courses-iframe") switched using iframe id
        driver.switch_to.frame("courses-iframe") # switch using name
        driver.find_element(By.ID, "search-courses").send_keys("Python",Keys.ENTER)
        time.sleep(3)

        # Now let's come out of the iframe and then do some operations
        # default_content() will come out of all the iframes and parent_iframe() will come out of
        # the current iframe , this will be used in case of nested iframes.
        driver.switch_to.default_content()
        time.sleep(3)
        element1 = driver.find_element(By.ID, 'name')
        location1 = element1.location_once_scrolled_into_view
        # driver.execute_script("window.scrollTo(0, )")
        time.sleep(3)
        driver.find_element(By.ID, 'name').send_keys("Python")
        # driver.close()

x = IFrames_Ex1()
x.switchToIframe()

"""In the above we tried to first move the cursor to the element and then we switched to the
iframe and then entered course name and clicked enter

We tried switching using index value which begins from 0 and then we switched using id and name as well.
we can switch to iframe using id, name, index values.

"""