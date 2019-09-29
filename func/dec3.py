import datetime
import time
def logger(fn):
    def warp(*args,**kwargs):
        '''this is a wrapper'''
        print("args={},kwargs={}".format(args, kwargs))
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        # after
        delta = (datetime.datetime.now() - start).total_seconds()
        if delta > 2:
            print("{} took {}s".format(fn.__name__,delta))
        return ret
    return  warp
@logger #相当于 add = logger（add)
def add(x,y):
    time.sleep(2)
    return x+y

#foo=logger(add)
#print(type(foo))
#print(foo(4,6))
#add = logger(add) #当将add这个函数传给fn后，add就给这个add给覆盖了,从而指向warp
#print(add(4,6))
print(add(4,6))
print(add.__name__,add.__doc__)
