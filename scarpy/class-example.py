class Person:
    age=3
    height=170
    def __init__(self,name,age=18):
        self.name=name
        self.age=age

tom=Person('tom')
jerry=Person('jerry', 20)
Person.age = 30
print(Person.age, tom.age, jerry.age)
print(Person.__dict__,tom.__dict__,jerry.__dict__)
print(Person.__dict__,tom.__dict__,jerry.__dict__,sep='\n')

Person.height +=20
print(Person.height,tom.height,jerry.height)

tom.height=168
print(Person.height,tom.height,jerry.height)

jerry.height += 30
print(Person.height,tom.height,jerry.height)