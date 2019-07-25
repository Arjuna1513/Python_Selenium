import logging as log
class Py_Logging_Ex2:
    def logging(self):
        log.basicConfig(filename="test.log", level=log.DEBUG, filemode='w')
        log.debug("Debug Message")
        log.info("Info Message")
        log.warning("Warning Message")
        log.error("Error Message")
        log.critical("Critical Message")
        # by default loglevel will be set to warning so only warning/error/critical log messages
        # will be displayed to change log level change it using log.basicConfig() method.
        # make sure that u will not provide level="value" i.e. level's value should not
        # be given in double quotes if u give value error will be thrown.
        # if u do not specify the filemode, by default it will open in append mode so
        # everything will get appended to the end of the existing content in a  file.

x = Py_Logging_Ex2()
x.logging()
