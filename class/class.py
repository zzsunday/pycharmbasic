class MyClass:
    """A example class"""
    xxx=123 # 类属性
    def foo(self):  #类属性foo，也是方法 self指代当前实例本身
        print('foo')
    #def bar():
        #print('bar')
    @classmethod #类的装饰器,相当于其他的静态方法
    def fnmethod(cls):#cls这个标识符可以是而难以合法名称，但是为了易读不要修改
        cls.height = 170
        print('{}.xxx={}'.format(cls.__name__,cls.xxx))

#在类定义中，使用@classmethod装饰漆修饰的方法
#必须至少有一个参数，且第一个参数留给了cls，cls指代调用者即为类对象自身
#cls这个标识符可以是任意合法的名称，但是为了易读，不要修改
#通过cls可以直接操作类的属性，但是无法通过cls操作类的实例。
    @staticmethod #静态方法
    def staticmtd(a):
        print('static','{}.a={}'.format(MyClass.__name__,a))

a=MyClass()
#MyClass.bar()
print(MyClass.__dict__)
print(MyClass.height)
MyClass.clssfn()
a.clssfn()  # =a.__class__.clssfn()
print(a.__dict__)
MyClass.staticmtd('abc')
a.staticmtd(4)
