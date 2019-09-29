class Car:
    def __init__(self,mark,speed,color,price):
        self.mark=mark
        self.speed=speed
        self.color=color
        self.price=price

class CarInfo:
    def __init__(self):
        self.info=[]
    def addcar(self,car:Car):
        self.info.append(car)
    def getall(self):
        return self.info

ci=CarInfo()
car=Car('audi',400,'red',100)
type(car)