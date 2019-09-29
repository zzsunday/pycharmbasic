print('This is test1 module')

class A:
    def ShowModule(self):
        print('{}.a={}'.format(self.__module__, self))
        print(self.__class__.__name__)


a = A()
a.ShowModule()