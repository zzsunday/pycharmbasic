class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age # 给age属性给隐藏了，私有属性
    def growup(self,incr=1):
        if 0 < incr <150:
            self.__age += incr
    def getage(self):
        return  self.__age
    def _getname(self):
        return self.name

tom = Person('tom')
tom.growup(2)
print(tom.getage())
print(Person.__dict__)
print(tom.__dict__)
tom._Person__age =200 #所以加上__age是给属性改名了 所以找不到
print(tom.getage())
#print(tom.age)
tom.age = 300 #所以这里是给tom新定义一个属性
print(tom.getage())
print(tom.age)
print(tom.__dict__)
#私有变量的本质是如果声明一个实例变量的时候,python会为其改名
#改成_类名___变量名的名称，所以原来的名称就访问不到了
#在变量名前加一个下划线例如_name和普通舒心一样，解释器不做任任何特殊处理
print('========private method==========')
print(tom._getname())#没有改名
#print(tom.__getname__())
print(tom.__dict__)
print(tom.__class__.__dict__)
在python

