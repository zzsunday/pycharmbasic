class Person:
    x=123 #；类的属性,也可以成为变量
    def __init__(self,name,age=18):
        self.name=name #实例的属性，变量
        self.y=age
    def show(self):
        print(self.name,self.y) # print(a.y,b.y)

a=Person('tom')
b=Person('Jerry')
print(a.name,b.name)
#构建一个新的实例其实是调用一个__new__函数
#Myclss()实际上调用的是__init__，可以不定义，如果没有定义会在实例化后隐式的调用。
#初始化隐式调用的化 就相当于啥都没干
print('==============')
a.show()