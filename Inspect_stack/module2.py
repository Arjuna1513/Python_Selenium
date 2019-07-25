import Inspect_stack.module3 as cc
import inspect
def method2():
    print(inspect.stack()[2][3])
    cc.method3()