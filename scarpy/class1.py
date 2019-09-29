class MyClass:
    """A example class"""
    x=123 # 类属性
    def foo(self):  #类属性foo，也是方法 self指代当前实例本身
        print(self.x) #也可以return，没有return说明return none

print(MyClass)
print(MyClass.__name__)
print(MyClass.x)
print(MyClass.foo)
print(MyClass.__doc__)
# if __name__=__main__ 没有这个 说明是在main模块中运行的
#类对象：类的定义就会产生一个类对象
#类的属性 类定义中的变量（x)类中定义的方法都是类的方法（foo）

print('zzzzzzzzzzzzzzzzzzz')
y=MyClass()
print(y.foo()) #会输出none是因为foo函数没有return
print(y.foo)