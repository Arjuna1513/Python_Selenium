import Inspect_stack.module1 as cc
import inspect
def mainMethod():
    print(inspect.stack()[1][3])
    cc.method1()

mainMethod()


"""
when u call a method1 from module a stack will get created with an entry and if u call one
more method method2 deom method1 then an new entry will be added to the stack

so now in main module if we use print(inspect.stack()[0][3]) then the name of the current method will
get printed and in method1 if we use print(inspect.stack()[1][3]) then the name of the method
from where this method is called will be printed.
"""
