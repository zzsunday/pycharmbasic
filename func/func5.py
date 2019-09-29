import inspect
import functools
def add(x,y):
    ret = x+y
    print(ret)
    return x+y
print(inspect.signature(add))
newadd = functools.par tial(add)