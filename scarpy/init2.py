class Person:
    x=123
    def __init__(self,name,age=18):
        self.name=name
        self.y=age   #init方法不能有返回值，只能是none
    def show(self,x,y):
        print(self.name, self.y, x, y)
        self.y=x   #将y限定在实例上
        Person.x=x
        print(self.name,self.y,x,y)

a=Person('tom') #实例化后就是一个实例对象
a.show(50,'a')
print(a.__dict__)
a.y=200
print(a.y)

#面对对象三要素
#封装：将数据和操作组装到一块 2 影藏数据：只对外暴露一些接口，通过接口访问对象
#比如驾驶汽车，只用知道怎么驾驶不用知道内部构造就好
print('tttttttttttttttttttt')
print(a.__class__)
print(a.__class__.__qualname__,a.__class__.__name__)
print(Person.__dict__)
print(a.__dict__)
print('111111111111111111111')
print(sorted(a.__class__.__dict__.items()))
print(sorted(a.__class__.__dict__.items()),end='\n')
