import logging as log
class Py_Logging_Ex4:
    def logging(self):
        log.basicConfig(format="%(levelname)s : %(message)s", filename="test.log", level=log.DEBUG, filemode='w')
        log.debug("Debug Message")
        log.info("Info Message")
        log.warning("Warning Message")
        log.error("Error Message")
        log.critical("Critical Message")
        """in the basicConfig we have not mentioned the format so by default the content will print as
        DEBUG:root:Debug Message
        INFO:root:Info Message
        WARNING:root:Warning Message
        ERROR:root:Error Message
        CRITICAL:root:Critical Message 
        
        i.e. level : roor : message
        
        we can format it to print only level : message using format method 
        format="%(levelname)s : %(message)s"
        """


x = Py_Logging_Ex4()
x.logging()
