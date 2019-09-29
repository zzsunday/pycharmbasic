class Person:
    def normal_method():
        print('normal')
    def method(self):
        print("{}'s method".format(self))
    @classmethod
    def class_method(cls):
        print('class= {0.__name__}({0})'.format(cls))
        print('{}.xxx={}'.format(cls.__name__, cls.xxx))
        cls.HEIGHT = 170
    @staticmethod
    def static_method():
        print(Person.HEIGHT)

print('---类访问')
print(Person.__dict__)
print(1,Person.normal_method())
print(2,Person.method())
print(3.Person.class_method())
print('---实例访问')
tom=Person()
print(1,tom.normal_method())
print(2,tom.method())
print(3.tom.class_method())

