#__name__ = 'abc'
print('--------',__name__)

print('A module')
import sys
class A:
    def show(self):
        print(type(self).__name__)
        print('=================',self.__module__)
if __name__ == "__main__":
    print('in main')
else:
    print('in module {}'.format(__name__))
#

a = A()

a.show()
print(sys.modules['__main__'])
print(dir())
