import logging
import logging.config

class CustomLogger:
    def logLogging(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(CustomLogger.__name__)

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

x = CustomLogger()
x.logLogging()

