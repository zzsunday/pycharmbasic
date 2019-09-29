class Car:
    def __init__(self,mark,speed,color,price):
        self.mark=mark
        self.speed=speed
        self.color=color
        self.price=price

class CarInfo:
    def __init__(self):
        self.info=[]
    def addcar(self,car:Car):#注意类的注释
        self.info.append(car)
    def getall(self):
        return self.info
import class4
from functools import partial
print(dir())
print(dir(class4))
print('*'*20)
ci=CarInfo()
car=Car('audi',400,'red',100)
ci.addcar(car)
print(ci.getall())
print(ci.info)