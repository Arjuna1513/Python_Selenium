import logging as log
class Py_Logging_Ex5:
    def logging(self):
        log.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", filename="test.log", level=log.DEBUG, filemode='w')
        log.debug("Debug Message")
        log.info("Info Message")
        log.warning("Warning Message")
        log.error("Error Message")
        log.critical("Critical Message")
        """
        To print time in the beginning of the log messages use format method and mention "%(asctime)s"
        and the output will look something like:
        
        2019-07-01 11:23:25,382 : DEBUG : Debug Message
        2019-07-01 11:23:25,384 : INFO : Info Message
        2019-07-01 11:23:25,385 : WARNING : Warning Message
        2019-07-01 11:23:25,385 : ERROR : Error Message
        2019-07-01 11:23:25,385 : CRITICAL : Critical Message
        """


x = Py_Logging_Ex5()
x.logging()
