class A:
    X = 1
    __slot__ =('y','z')
    def __init__(self):
        self.y =5
        self.z =6
    def show(self):
        print(self.x, self.y,self.z)

a = A()
print(a.__dict__)
print(A.__dict__)
a.show()