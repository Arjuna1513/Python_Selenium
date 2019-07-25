import logging as log
class Py_Logging_Ex3:
    def logging(self):
        print(log.DEBUG)
        print(log.INFO)
        print(log.WARNING)
        print(log.ERROR)
        print(log.CRITICAL)
        # DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50 these are values associated with log levels.

x = Py_Logging_Ex3()
x.logging()
