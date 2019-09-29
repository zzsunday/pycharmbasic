class Animal:
    x=123
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name
    def shout(self):
        print('animal shout')

class Cat(Animal):
    x='cat'
    def __init__(self,name):
        super().__init__(name)
        self.name=name
    def shout(self):
        print('miao')

class Carfield(Cat):
    pass

class PersiaCat(Cat):
    pass

class Dog(Animal):
    def run(self):
        print('dog run')

tom=Cat('tom')
print(tom.name)
print(tom.shout())


dog=Dog('ahuang')
print(dog.name)
print(dog.shout())

gf=Carfield('gf')
gf.shout()
print('gf.x',gf.x)
print('gf',gf.__dict__)

# print('gf.mro={}'.format(gf.__class__.__mro__))#
# # print('gf.mro={}'.format(gf.__class__.__bases__)) #基类
