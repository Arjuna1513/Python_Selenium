def yieldEx1():
    i=1
    n=5
    value = None
    while i < n:
        yield i*i
        i = i + 1

print(list(yieldEx1()))

"""
If the compiler detects the yield keyword anywhere inside a function, that function no longer returns 
via the return statement. Instead, it immediately returns a lazy 'pending list' object called a generator. 
A generator is iterable. iterable is anything like a list or set or range or dict-view, with a 
built-in protocol for visiting each element in a certain order.

So basically, a function with 'yield' is not a normal function anymore, instead it becomes a generator . 
Every time the code is executed to "yield", it returns the right side of "yield", then it continues to loop 
the code.
"""