import inspect
import Inspect_stack.module2 as cc
def method1():
    print(inspect.stack()[1][3])
    cc.method2()