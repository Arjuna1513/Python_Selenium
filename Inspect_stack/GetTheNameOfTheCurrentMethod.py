import inspect

def method1():
    print(inspect.stack()[0][3])

print(method1.__name__)
method1()


"""
If u want to the know the name of the method in python there are two possible ways
1. use methodName.__name__ or className.__name__
2. inspect.stack()[0][3]
second will return only if the method is being called directly from the same module
but if we want to know the name of the method that has been called from another 
"""