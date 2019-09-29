class Property:
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset
        pass

    def __get__(self, instance, owner):
        if instance is not None:
        #print('p.get', self, instance, owner)
            return self.fget(instance)
        return

    def __set__(self, instance, value):
        if callable(self.fset):
        # print('p.set', instance, value)
            return self.fset(instance, value)
        else:
            raise AttributeError('cant set attribute')

    def setter(self, fn):
        self.fset = fn
        return self
class A:
    def __init__(self, data):
        self._data = data

    @Property #data = Propery(data) => data= obj
    def data(self):
        return self._data

    @data.setter
    def data(self, value): #data = data.setter(data) => data= obj
        self._data = value

a = A(2)
print(a.data)
a.data = 200
print(a.data)
