import datetime
import time

def logger(t):# def logger(t1, t2, t3....tn):
    def _logger(fn):
        #@copy_properties(fn) 可以把上面写的复制属性的函数装饰在此
        def wrap(*args, **kwargs):
            #before 功能增强
            # print("args={},kwargs={}".format(args, kwargs))
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            #after 功能增强
            duration = (datetime.datetime.now() - start).total_seconds()
            if duration > t:
                print("function {} took {}s.".format(fn.__name__, duration))
            return ret
        return wrap
    return _logger

@logger(3)# add = logger(3)(add), @logger(3, 5, 9,...n)
def add(x, y):
    print("======call add======")
    time.sleep(5)
    return x + y

print(add(4, y=5))