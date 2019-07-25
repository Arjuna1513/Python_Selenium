import logging as log
class Py_Logging_Ex6:
    def logging(self):
        log.basicConfig(datefmt="%d/%m/%Y %I:%M:%S %p", format="%(asctime)s : %(levelname)s : %(message)s", filename="test.log", level=log.DEBUG, filemode='w')
        log.debug("Debug Message")
        log.info("Info Message")
        log.warning("Warning Message")
        log.error("Error Message")
        log.critical("Critical Message")
        print(log.getLevelName(50)) # will return the loglevel of the provided numerical value
        # level = getattr(log, log.info())
        """
        To print time in the beginning of the log messages use format method and mention "%(asctime)s"
        and the output will look something like:
        
        2019-07-01 11:23:25,382 : DEBUG : Debug Message
        2019-07-01 11:23:25,384 : INFO : Info Message
        2019-07-01 11:23:25,385 : WARNING : Warning Message
        2019-07-01 11:23:25,385 : ERROR : Error Message
        2019-07-01 11:23:25,385 : CRITICAL : Critical Message
        
        but to change the time and date format there is a argument to basicConfig(datefmt) 
        datefmt = "%d/%m/%Y  %I:%M:%S"  I for 12 hour format and H for 24 hour format
        and if u mention H then no need to specify %p(which is for am and pm)
        """


x = Py_Logging_Ex6()
x.logging()
