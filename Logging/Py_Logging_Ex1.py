import logging as log
class Py_Logging_Ex1:
    def logging(self):
        log.debug("Debug Message")
        log.info("Info Message")
        log.warning("Warning Message")
        log.error("Error Message")
        log.critical("Critical Message")
        # by default loglevel will be set to warning so only warning/error/critical log messages
        # will be displayed to change log level change it using log.basicConfig() method.

x = Py_Logging_Ex1()
x.logging()
