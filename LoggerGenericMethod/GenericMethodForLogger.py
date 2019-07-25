import logging
import inspect

def customLogger(loglevel):
    loggerName = inspect.stack()[1][3] # this will get the name of the class/method from where it is called...
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    sHandler = logging.StreamHandler()
    sHandler.setLevel(loglevel)


    fHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    fHandler.setLevel(loglevel)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d/%m/%Y %I:%M:S %p")

    sHandler.setFormatter(formatter)
    fHandler.setFormatter(formatter)

    logger.addHandler(sHandler)
    logger.addHandler(fHandler)

    return logger
