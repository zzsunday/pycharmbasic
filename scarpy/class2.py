class MyClass:
    """A example class"""
    x=123 # 类属性
    def foo(self):  #self指代当前实例本身,是个形参，名字可以更改
        print(id(self)) #也可以return，没有return说明return none
        return self

a=MyClass()#实例化 初始化
print(a.foo())
print(id(a))
