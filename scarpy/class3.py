#添加一个name属性
def setname(name):
    def wrapper(cls):
        cls.name = name
        return cls
    return wrapper
@setname('myclass')
class MyClass:
    pass

print(MyClass.__dict__)
