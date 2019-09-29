class Typed:
    def __init__(self, type):
        self.type = type

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        print('T.set', self, instance, value)
        if not isinstance(value, self.type):
            raise ValueError(value)
import inspect
class TypeAssert:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        params = inspect.signature(Person).parameters
        print(params, params.items(), sep='\n')
        for name, param in params.items():
            print(name, param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls, name, Typed(param.annotation))#nmae = Type(str)

@TypeAssert
class Person:
    #name = Typed(str)
    #age = Type(int)

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

