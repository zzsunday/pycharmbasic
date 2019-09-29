class Person:
    xxx = 123
    def foo(self):  #类属性foo，也是方法 self指代当前实例本身
        print('foo')
    @classmethod
    def class_method(cls):
        print('class= {0.__name__}({0})'.format(cls))
        print('{}.xxx={}'.format(cls.__name__, cls.xxx))
        cls.HEIGHT=170
    @staticmethod  # 静态方法
    def staticmtd(a):
        print('static', '{}.a={}'.format(MyClass.__name__, a))

Person.class_method()
print(Person.__dict__)
print(Person.HEIGHT)