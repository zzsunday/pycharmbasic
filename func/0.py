class Animal:
    x=123
    def __init__(self,name,age=10):
        self.name=name
        self.__age=10
    @property
    def name(self):
        return self.catname
    @property
    def age(self):
        return self.__age
    def shout(self):
        print('animal shout')

class Cat(Animal):
    x='cat'
    def __init__(self,name,age=20):
        self.__age=age
        self.catname=name
    @property
    def age(self):
        return self.__age
    def shout(self):
        print('miao')

class Carfield(Cat):
    pass

tom=Carfield('tom')
print(tom.name)
P