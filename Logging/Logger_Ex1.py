import logging

class Logger_Ex1:
    def loggerEx1(self):
        Logger = logging.getLogger(Logger_Ex1.__name__)  # created a custom logger with same name as of module.
        Logger.setLevel(logging.INFO)  # setting the log level to Info

        cHandler = logging.StreamHandler()  # created a handler cHandler
        cHandler.setLevel(logging.INFO)  # setting a log level INFO to handler

        cHandler1 = logging.FileHandler("fHandler.log", mode="w")
        cHandler1.setLevel(logging.ERROR)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                      datefmt="%d/%m/%Y - %I:%M:%S-%p")
        fFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                       datefmt="%d/%m/%Y - %I:%M:%S-%p")

        cHandler.setFormatter(formatter)
        cHandler1.setFormatter(fFormatter)

        Logger.addHandler(cHandler)
        Logger.addHandler(cHandler1)

        Logger.info("Info Log Message")
        Logger.debug("Debug Log Message")
        Logger.warning("Warning Log Message")
        Logger.error("Error Log Message")
        Logger.critical("Critical Log Message")

x = Logger_Ex1()
x.loggerEx1()



"""
As u can see first u need to get a logger and set the loglevel

now define a Handler and set the loglevel. it's because the single logger can have many 
handlers and each handler can be used to output the content to console/file or email
so u can have different log messages of different levels in different destinations.

now define a formatter.

Add the formatter to handler created.

Add the handler to logger.

Note : If u mention info for 1 handler and debug for another hnadler and if logger level is Info
the output of first handler will be debug/info/warning/error/critical and the other handler output
will be info/warning/error/critical. 

And for e.g. if logger level is set to Error and Handler level is set to Info then the handler will display 
only error/critical

we can specify the name in formatter e.g. %(name)s and if u give getLogger(className.__name__) u will see 
ClassName in the output but since we have not defined class ass it displays is __main__ so better have class
"""