import logging
import LoggerGenericMethod.GenericMethodForLogger as lg

class MainClass:
    log = lg.customLogger(logging.DEBUG)

    def method1(self):
        self.log.info("Info Message")
        self.log.debug("Debug Message")
        self.log.warning("Warning Message")
        self.log.error("Error Message")
        self.log.critical("Critical Message")

    def method2(self):
        log1 = lg.customLogger(logging.WARNING)
        log1.info("Info Message")
        log1.debug("Debug Message")
        log1.warning("Warning Message")
        log1.error("Error Message")
        log1.critical("Critical Message")

    def method3(self):
        log1 = lg.customLogger(logging.ERROR)
        log1.info("Info Message")
        log1.debug("Debug Message")
        log1.warning("Warning Message")
        log1.error("Error Message")
        log1.critical("Critical Message")


x = MainClass()
x.method1()
x.method2()
x.method3()