def logger(fn):
    def warp(*args,**kwargs):
        #befor
        ret=fn(*args,**kwargs) #参数的解构
        #after
        return ret
    return  warp

def add(x,y):
    return x+y

foo=logger(add) #嵌套函数运行的原理
print(type(foo))
